# Phase-Wise Implementation Plan: AI Discovery Engine

*Note: This implementation plan focuses strictly on building the AI Discovery Engine. Downstream PM tasks such as Primary User Research, Problem Definition, and MVP Building have been removed from this technical track.*

## Phase 1: Automated Data Ingestion & Normalization
**Objective:** Collect, clean, and standardize the raw data required for the discovery engine on a scheduled cadence.
- **Tasks:**
  1. Create a Python ingestion script to pull recent App Store & Play Store reviews, and scrape relevant Reddit/YouTube discussions concerning fashion wishlist behavior.
  2. Implement the normalization logic: filter out <6 word reviews, remove non-English text, and strip all PII (usernames, handles).
  3. **GitHub Actions Integration:** Set up a GitHub Actions workflow with a cron schedule (e.g., weekly) to run the ingestion script automatically in batch mode.
  4. Store the normalized output securely (e.g., local JSON or cloud storage).
  5. **AI Guardrails:** Document where AI is used. Ensure AI is strictly used for execution tasks (scraping, extraction) and not for core thinking. Estimate token consumption and cost math for LLM calls.
- **Exit Criteria:** GitHub Action runs successfully on schedule and produces a clean dataset of at least 1,000 relevant data points.

## Phase 2: AI Analysis & Theme Discovery
**Objective:** Process the normalized data to extract themes and synthesize answers using Groq (Llama-3.3-70b-versatile).
- **Tasks:**
  1. Load the normalized dataset and apply stratified sampling to ensure platform balance.
  2. Map reviews to one of **13 unconstrained themes**.
  3. Construct batched prompts (using JSON output enforcement) and run them through Groq's LLaMA 3.3 70B model. Handle rate limits with intelligent sleep delays and chunking.
  4. Aggregate the classifications and synthesize a final Markdown report (`analysis_results.md`). This report must output opportunities using a strict problem definition format.
  5. The output must retain verbatim user quotes for provenance. AI provides the starting points for probing; core synthesis and problem structuring must remain human-driven.
  6. **Risk Mitigation:** Explicitly enumerate AI failure modes (e.g., hallucinations, probabilistic variance) and define mitigation strategies (e.g., grounding in verbatim quotes).
- **Exit Criteria:** A structured JSON object containing verified opportunity areas, quantified metrics, and verbatim user quotes.

## Phase 3: Insights Dashboard UI & RAG-Based Discovery Chatbot
**Objective:** Visualize discovery insights for stakeholders and provide an interactive RAG-based chatbot to query raw review data.
- **Tasks:**
  1. **Dashboard UI:** Build a modern, responsive web dashboard (React/Next.js or Streamlit) displaying the Weekly Discovery Pulse, top friction themes, source distributions, and opportunity areas.
  2. **RAG-Based Discovery Chatbot:** Embed an interactive AI assistant into the dashboard allowing PMs and evaluators to query the raw review dataset using Retrieval-Augmented Generation (e.g., *"What are users saying about platform fees on wishlisted items?"*, *"Show me return policy complaints from Reddit"*).
  3. **MCP Reporting Automation:** Setup the local Python MCP server (`saksham-mcp-server`) and trigger it via GitHub Actions to append summary pulses to Google Docs.
  4. **Multi-Platform Extensions (Post-MVP):** Add Instagram (IG) comment scraper via Apify for fashion influencer campaign feedback.
- **Exit Criteria:** A live Dashboard UI with interactive charts, a functional RAG chatbot querying the dataset, and an automated report delivery pipeline.
