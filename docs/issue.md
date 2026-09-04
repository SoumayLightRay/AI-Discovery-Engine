# Known Issues, Edge Cases & Technical Risks

This document tracks known constraints, external platform quirks, and mitigation strategies for the AI Discovery Engine.

---

## 1. Scraping & Data Ingestion Issues (Phase 1)

### Issue 1.1: Direct Reddit API Lockdown (403 Forbidden)
- **Symptom:** Unauthenticated requests to Reddit `.json` endpoints or standard scrapers fail with `403 Forbidden`.
- **Root Cause:** Reddit's aggressive anti-AI scraping policy implemented in 2024–2025.
- **Resolution:** Integrated official **Apify Actor (`trudax/reddit-scraper-lite`)**. The actor utilizes rotating residential proxies to reliably fetch Reddit discussions from `r/MyntraSucks`, `r/IndianBeautyDeals`, and `r/Myntradiscount`.
- **Status:** **Resolved.** (Token stored in `.env`).

### Issue 1.2: Apple App Store RSS Feed Limitations
- **Symptom:** Apple's public customer reviews RSS endpoint (`https://itunes.apple.com/in/rss/customerreviews/...`) returns at most 50 reviews per page and caps out at page 10.
- **Root Cause:** Hard limit set by Apple iTunes RSS architecture.
- **Mitigation:** Implemented multi-page pagination (pages 1–5) capturing up to 250 iOS reviews.
- **Status:** **Monitored / Mitigated.**

### Issue 1.3: YouTube Comment Timestamps Format Inconsistency
- **Symptom:** YouTube comments return relative strings like `"2 days ago"`, `"3 months ago"`, or `"6 years ago"` rather than ISO timestamps.
- **Risk:** Older reviews could skew recency-focused weekly analysis.
- **Mitigation:** Filter YouTube comments to prioritize top upvoted recent comments or parse relative strings into approximate ISO dates.
- **Status:** **In Progress.**

---

## 2. AI Model & Inference Issues (Phase 2)

### Issue 2.1: Groq Free-Tier Rate Limits (30 RPM, 12K TPM)
- **Symptom:** Firing large batches of reviews can cause `429 Too Many Requests`.
- **Mitigation:** 
  - Batched processing in chunks of 15–20 reviews.
  - Added strict `time.sleep(2.0)` pacing between calls.
  - Stratified sampling (analyzing ~320 reviews per weekly run across all 4 platforms).
- **Dual-Model Fallback:** Added support for **Google Gemini 2.0 Flash (Free API Key)** with 15 RPM / 1,000,000 TPM limit as an automatic fallback when Groq hits capacity.

### Issue 2.2: LLM Hallucination Risk in Thematic Quotes
- **Symptom:** Generative models often paraphrase or invent user quotes to fit a clean narrative.
- **Violation:** Violates Arindam's strict anti-hallucination and evidence-grounding mandate.
- **Mitigation:**
  - In Stage A, the prompt requires the model to return an exact substring from the provided review.
  - In Stage B, the validator checks quote provenance (`quote in raw_review_text`) before publishing to Google Docs or Dashboard UI.

---

## 3. GitHub Actions & Operational Issues

### Issue 3.1: Missing Secrets in Forked or Cloud Environments
- **Symptom:** GitHub Actions cron fails if `APIFY_API_TOKEN` or `GROQ_API_KEY` are not added to GitHub Secrets.
- **Resolution:** Added clear setup instructions and graceful fallbacks in code if tokens are missing.
