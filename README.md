# AI Discovery Engine — Myntra Wishlist → Purchase

An AI-powered discovery engine built for a Product Manager Fellowship graduation project (product: **Myntra**).
It ingests public user feedback, tags it with an LLM into friction themes, synthesises opportunity areas, and lets
you interrogate the evidence through a grounded RAG chat. The research, deck and MVP that came out of it live in this repo too.

| Deliverable | Link |
|---|---|
| Discovery Engine dashboard + RAG chat | https://ai-discovery-engine-rose.vercel.app/ |
| Deployed MVP ("Myntra Verified Confidence Layer") | https://ai-discovery-engine-rose.vercel.app/wishlist_mvp.html |
| Backend API (Render) | https://discovery-engine-api-mk0d.onrender.com/api/health |

> The backend runs on a free tier and sleeps when idle; the dashboard pings it on load and tells you if it is waking up.

## How it works

```
Phase 1  src/phase_01/ingestion.py   Google Play · App Store · Reddit (Apify) · YouTube  ──►  docs/phases/phase-01/normalized_data.json
                │  relevance gate (src/phase_01/relevance.py) drops off-topic records
Phase 2  src/phase_02/analysis.py    stratified sample ► LLM tagging (13 friction themes) ► synthesis  ──►  docs/phases/phase-02/analysis_results.json
Phase 3  src/phase_03/server.py      FastAPI: static dashboard + /api/chat (TF-IDF retrieval ► Groq LLM, cited answers)
         src/phase_03/web/           index.html (dashboard) · wishlist_mvp.html · nl_myntra_deck.html · research report
```

* **Grounded answers.** `/api/chat` retrieves the 8 most relevant reviews (TF-IDF), fences them as untrusted data in the
  prompt, and asks the model to cite `[Review #id]`; ids are row numbers in `normalized_data.json`. Without a `GROQ_API_KEY`
  it degrades to an extractive answer (and says so).
* **Statistics that admit uncertainty.** The analysed sample is balanced per source, so `analysis.py` also reports a
  corpus-weighted friction rate and Wilson 95% intervals per theme next to the raw sample percentages.
* **Weekly refresh.** `.github/workflows/weekly_ingestion.yml` re-ingests, re-analyses and commits the results.

## Run it locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt          # server + tests (use requirements-pipeline.txt for ingestion)
cp .env.example .env                         # add GROQ_API_KEY for LLM answers (optional)
python src/phase_03/server.py                # http://localhost:3000
pytest -q && ruff check .
```

Re-running the pipeline: `python src/phase_01/ingestion.py` then `python src/phase_02/analysis.py` (needs `GROQ_API_KEY`;
ingestion needs `APIFY_API_TOKEN` for Reddit and `YOUTUBE_VIDEO_IDS` — see below) and `python src/phase_03/export_report.py`.

### Configuration

| Variable | Purpose | Default |
|---|---|---|
| `GROQ_API_KEY` | LLM synthesis + tagging | unset → extractive answers |
| `APIFY_API_TOKEN` | Reddit ingestion | unset → Reddit skipped |
| `YOUTUBE_VIDEO_IDS` | Comma-separated IDs of Myntra haul/review videos | unset → YouTube skipped |
| `RATE_LIMIT_PER_MIN` | Per-IP limit on `/api/chat` | `20` |
| `CORS_ORIGINS` | Comma-separated allowed origins | Vercel project + localhost |
| `RAG_INCLUDE_OFF_TOPIC` | Index records the relevance gate rejects | off |

### API

`POST /api/chat {"query": "..."}` (1–500 chars) → `{answer, citations[], review_count, total_corpus, mode: "llm"|"extractive", latency_ms}` ·
`GET /api/health` · `GET /api/meta`.

## Data-quality notes (read before quoting numbers)

* **The committed YouTube data is off-topic.** All 190 YouTube comments in `normalized_data.json` come from unrelated
  entertainment videos; none contains a fashion or shopping term. They are 79 of the 313 analysed reviews (74 tagged
  "Other emergent themes", 0 with friction). The code now excludes them from retrieval and from future analysis, and ingestion
  requires explicit `YOUTUBE_VIDEO_IDS`. Headline figures such as *1,367 reviews* and the *22.4% friction rate* in the
  committed results/deck still include them: excluding YouTube the sample friction rate is **29.9%** (70 / 234). Re-run the
  pipeline with real Myntra videos to refresh the committed numbers.
* **Volume ≠ friction.** *Quality/material* is the most-mentioned theme (44) but only 3 of those reviews report friction;
  *Returns* (29/31), *Availability* (15/17) and *Price* (11/33) are far more often actual blockers. The dashboard now shows both.
* The analysis is a single LLM pass over a ~313-review sample, so small themes carry wide confidence intervals.

## Repository map

`src/` code · `docs/` research notes, 12 interview write-ups, phase outputs · `tests/` pytest suite ·
`report.md`, `framework.md`, `primary_research.md`, `slide_deck_plan.md` — the written case ·
`src/phase_03/dashboard.py` — legacy Streamlit prototype (not deployed) · `scratch/` — throwaway scraper probes.
