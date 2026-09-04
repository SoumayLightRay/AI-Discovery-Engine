"""
FastAPI server for the AI Discovery Engine Dashboard.
Serves the static HTML dashboard and provides the RAG chatbot API.
"""
import os
import sys
import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.phase_03.rag_engine import get_engine

app = FastAPI(title="AI Discovery Engine", version="2.4")

# CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (the dashboard HTML, CSS, JS)
WEB_DIR = os.path.join(os.path.dirname(__file__), "web")
app.mount("/static", StaticFiles(directory=WEB_DIR), name="static")

# Serve data files
DATA_DIR = os.path.join(WEB_DIR, "data")
if os.path.exists(DATA_DIR):
    app.mount("/data", StaticFiles(directory=DATA_DIR), name="data")


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main dashboard."""
    index_path = os.path.join(WEB_DIR, "index.html")
    return FileResponse(index_path)


@app.post("/api/chat")
async def chat(request: Request):
    """RAG chatbot endpoint. Accepts a query, retrieves relevant reviews, and generates a grounded answer."""
    try:
        body = await request.json()
        query = body.get("query", "").strip()

        if not query:
            return JSONResponse({"error": "Empty query"}, status_code=400)

        engine = get_engine()
        result = engine.generate_answer(query)

        return JSONResponse({
            "answer": result["answer"],
            "citations": result["citations"],
            "review_count": result["review_count"],
            "total_corpus": result.get("total_corpus", 0),
            "status": "ok"
        })

    except Exception as e:
        print(f"[API] Chat error: {e}")
        return JSONResponse({
            "answer": f"Server error: {str(e)}",
            "citations": [],
            "review_count": 0,
            "status": "error"
        }, status_code=500)


@app.get("/api/health")
async def health():
    """Health check endpoint."""
    engine = get_engine()
    return {
        "status": "ok",
        "corpus_size": len(engine.reviews),
        "index_ready": engine._loaded
    }


@app.get("/api/meta")
async def meta():
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
