"""
FastAPI server for the AI Discovery Engine Dashboard.
Serves the static HTML dashboard and provides the RAG chatbot API.
"""
import os
import sys
import threading
import time
from collections import defaultdict, deque
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
import uvicorn

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.phase_03.rag_engine import get_engine

MAX_QUERY_CHARS = 500
RATE_LIMIT_PER_MIN = int(os.getenv("RATE_LIMIT_PER_MIN", "20"))

# Browsers may call the API from the Vercel front-end (incl. preview deploys)
# and from localhost. Override with CORS_ORIGINS="https://a.com,https://b.com".
CORS_ORIGINS = [o.strip() for o in os.getenv("CORS_ORIGINS", "").split(",") if o.strip()]
CORS_ORIGIN_REGEX = (
    None if CORS_ORIGINS
    else r"https://ai-discovery-engine[a-z0-9-]*\.vercel\.app|http://(localhost|127\.0\.0\.1)(:\d+)?"
)


class RateLimiter:
    """Sliding-window per-client limiter (in-memory; fine for a single free-tier instance)."""

    def __init__(self, limit: int, window_s: float = 60.0):
        self.limit = limit
        self.window_s = window_s
        self._hits = defaultdict(deque)
        self._lock = threading.Lock()

    def check(self, key: str, now: float | None = None) -> float:
        """Record a hit. Returns 0 if allowed, else seconds until the client may retry."""
        if self.limit <= 0:
            return 0.0
        now = time.monotonic() if now is None else now
        with self._lock:
            hits = self._hits[key]
            while hits and now - hits[0] >= self.window_s:
                hits.popleft()
            if len(hits) >= self.limit:
                return max(self.window_s - (now - hits[0]), 1.0)
            hits.append(now)
            # Drop idle keys so memory can't grow without bound.
            if len(self._hits) > 1024:
                for k in [k for k, v in self._hits.items() if not v or now - v[-1] >= self.window_s]:
                    del self._hits[k]
            return 0.0


chat_limiter = RateLimiter(RATE_LIMIT_PER_MIN)


def client_key(request: Request) -> str:
    """Client identity for rate limiting; honours the proxy's X-Forwarded-For (Render)."""
    forwarded = request.headers.get("x-forwarded-for", "")
    if forwarded:
        return forwarded.split(",")[0].strip()
    return request.client.host if request.client else "unknown"


class ChatRequest(BaseModel):
    query: str

    @field_validator("query")
    @classmethod
    def validate_query(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("query must not be empty")
        if len(v) > MAX_QUERY_CHARS:
            raise ValueError(f"query must be at most {MAX_QUERY_CHARS} characters")
        return v


@asynccontextmanager
async def lifespan(_: FastAPI):
    # Build the index at startup so the first user request isn't the slow one.
    try:
        get_engine()
    except Exception as e:  # keep the process up; /api/health reports the failure
        print(f"[API] Engine failed to load at startup: {e}")
    yield


app = FastAPI(title="AI Discovery Engine", version="2.4", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_origin_regex=CORS_ORIGIN_REGEX,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["Content-Type"],
)


@app.middleware("http")
async def security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    return response


# Serve static files (the dashboard HTML, CSS, JS)
WEB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "web")
app.mount("/static", StaticFiles(directory=WEB_DIR), name="static")

# Serve data files
DATA_DIR = os.path.join(WEB_DIR, "data")
if os.path.exists(DATA_DIR):
    app.mount("/data", StaticFiles(directory=DATA_DIR), name="data")


@app.get("/")
async def root():
    """Serve the main dashboard."""
    return FileResponse(os.path.join(WEB_DIR, "index.html"))


# Declared `def` (not `async def`): retrieval and the LLM call are blocking, so
# FastAPI runs this in its threadpool instead of stalling the event loop.
@app.post("/api/chat")
def chat(body: ChatRequest, request: Request):
    """RAG chatbot endpoint. Accepts a query, retrieves relevant reviews, and generates a grounded answer."""
    retry_after = chat_limiter.check(client_key(request))
    if retry_after:
        return JSONResponse(
            {"status": "rate_limited", "error": "Too many requests. Please slow down."},
            status_code=429,
            headers={"Retry-After": str(int(retry_after))},
        )

    try:
        result = get_engine().generate_answer(body.query)
    except Exception as e:
        # Log details server-side; never leak internals to the client.
        print(f"[API] Chat error: {e!r}")
        raise HTTPException(status_code=500, detail="The discovery engine hit an internal error.") from e

    return {
        "answer": result["answer"],
        "citations": result["citations"],
        "review_count": result["review_count"],
        "total_corpus": result.get("total_corpus", 0),
        "mode": result.get("mode", "extractive"),
        "latency_ms": result.get("latency_ms"),
        "status": "ok",
    }


@app.get("/api/health")
def health():
    """Health check endpoint."""
    try:
        engine = get_engine()
    except Exception as e:
        print(f"[API] Health check: engine unavailable: {e!r}")
        return JSONResponse({"status": "degraded", "index_ready": False}, status_code=503)
    return {
        "status": "ok",
        "corpus_size": len(engine.reviews),
        "excluded_off_topic": engine.excluded_off_topic,
        "index_ready": engine.vectorizer is not None,
        "llm_enabled": engine.llm_enabled,
    }


@app.get("/api/meta")
def meta():
    """Return analysis metadata for the dashboard."""
    engine = get_engine()
    return {
        "metadata": engine.analysis.get("metadata", {}),
        "synthesis": engine.analysis.get("synthesis", {})
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    print(f"Starting AI Discovery Engine Server on http://localhost:{port}")
    uvicorn.run(app, host="0.0.0.0", port=port, reload=False)
