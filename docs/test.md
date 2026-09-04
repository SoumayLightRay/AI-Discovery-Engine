# Verification & Testing Blueprint: AI Discovery Engine

This document defines the automated test scripts, verification workflows, and exit criteria for each phase of the project.

---

## 1. Test Suite Overview

| Test ID | Subsystem | Target | Verification Method | Pass Criteria |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Phase 1: Ingestion | Google Play Store | `test_scrapers_full.py` | Pulls ≥ 100 valid reviews with > 5 words |
| **TC-02** | Phase 1: Ingestion | Apple App Store | `test_scrapers_full.py` | Parses XML/JSON RSS feed successfully |
| **TC-03** | Phase 1: Ingestion | YouTube Downloader | `test_scrapers_full.py` | Extracts ≥ 50 comments without YouTube API key |
| **TC-04** | Phase 1: Ingestion | Apify Reddit Scraper | `test_apify_reddit.py` | Authenticates via `.env` token and yields ≥ 20 posts |
| **TC-05** | Phase 1: Normalization | Deduplication & PII | `ingestion.py` | Zero email/phone handles, text length ≥ 6 words |
| **TC-06** | Phase 2: AI Tagging | Groq / Gemini API | `src/phase_02/analysis.py` | Produces valid JSON conforming to schema |
| **TC-07** | Phase 2: Grounding | Quote Provenance | `validate_provenance.py` | 100% of quotes exist verbatim in dataset |
| **TC-08** | Phase 3: Dashboard | Web UI & RAG Chat | Browser / Manual test | RAG chatbot accurately answers queries with citations |

---

## 2. Automated Test Commands

### 2.1 Testing Phase 1 Ingestion
Run the full ingestion pipeline:
```bash
python src/phase_01/ingestion.py
```
**Verification Check:**
```bash
python -c "import json; data = json.load(open('docs/phases/phase-01/normalized_data.json', 'r', encoding='utf-8')); assert len(data) >= 1000, f'Expected >= 1000 items, got {len(data)}'; print(f'PASS: {len(data)} items verified!')"
```

### 2.2 Testing Phase 2 AI Analysis & Schema Compliance
Run Phase 2 analysis:
```bash
python src/phase_02/analysis.py
```
**Verification Check:**
```bash
python -c "import json; res = json.load(open('docs/phases/phase-02/analysis_results.json', 'r', encoding='utf-8')); assert 'synthesis' in res and 'tagged_reviews' in res; print('PASS: Phase 2 output conforms to schema!')"
```

### 2.3 Testing Quote Provenance (Anti-Hallucination Guardrail)
```python
# Verifies that every quote extracted by the LLM is an exact substring of raw data
import json

raw_corpus = [r['text'] for r in json.load(open('docs/phases/phase-01/normalized_data.json', 'r', encoding='utf-8'))]
pulse = json.load(open('docs/phases/phase-02/analysis_results.json', 'r', encoding='utf-8'))

for opp in pulse['synthesis']['opportunity_areas']:
    quote = opp['grounded_quote']
    found = any(quote in text for text in raw_corpus)
    print(f"Quote check: {'[PASS]' if found else '[FAIL]'} -> \"{quote[:60]}...\"")
```

---

## 3. Exit Criteria Matrix

- [x] **Phase 1 Complete:** ≥ 1,000 clean data points gathered across 4 distinct platforms (Achieved: 1,367 items).
- [ ] **Phase 2 Complete:** Structured JSON output generated with quantified theme distribution and verified quotes.
- [ ] **Phase 3 Complete:** Responsive Dashboard UI live with interactive RAG chatbot querying the dataset.
