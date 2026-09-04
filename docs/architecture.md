# Architecture: AI Discovery Engine (Weekly Review Pulse)

This document describes how an AI agent produces the discovery report defined in `problem_statement.md` and delivers it through **Google Docs** and **Gmail** using **MCP servers**, not direct Google API clients in the application layer.

It is written for builders and reviewers: what subsystems exist, how data flows, where trust boundaries sit, and what must remain true for the milestone to be satisfied.

## 1. Purpose and scope

### 1.1 What this system does
1. **Ingests** recent, public mobile-store review exports (App Store and Play Store) and other community feedback (Reddit, YouTube) for the chosen product.
2. **Synthesizes** a short weekly narrative: dominant themes (fit, pricing, intent), grounded user language, and actionable opportunity areas.
3. **Writes** a stakeholder-readable artifact in **Google Docs** via MCP.
4. **Creates a Gmail draft** (typically to the operator or an alias) via MCP so distribution is one click away without bypassing review.

### 1.2 Explicit non-goals
- **No** authenticated scraping, headless store browsing, or gray-area automation against storefronts.
- **No** replacing Google APIs with hand-rolled OAuth clients for Docs/Gmail as the primary integration pattern—MCP servers own that surface.
- **No** open-ended “market research agent” beyond the scoped pulse format (caps on themes, quotes, words).

### 1.3 Quality attributes (prioritized)

| Priority | Attribute | Meaning here |
| :--- | :--- | :--- |
| 1 | **Constraint safety** | Word limits, theme caps, and PII rules are enforced **before** external write operations. |
| 2 | **Traceability** | Quotes trace back to normalized review text; runs emit enough metadata to reproduce a demo. |
| 3 | **Operational simplicity** | Few moving parts: ingestion → analysis → validation → MCP deliveries. |
| 4 | **Recoverability** | Failures at MCP calls do not silently corrupt partial state; errors are visible in logs or operator UI. |

## 2. Stakeholders and consumers

| Role | Interest |
| :--- | :--- |
| **Product / Growth** | Prioritized themes and quotes that justify roadmap bets to improve wishlist conversion. |
| **Support / Research** | Language users actually use; reduces mismatch between assumptions and reality. |
| **Leadership** | One screen of signal per week without raw-review noise. |
| **Operator (you)** | Repeatable run, clear draft email, Doc link for archiving. |

## 3. Context diagram (external actors)

**Your pulse system** talks to:
- App Store / Play Store export files
- Groq LLM API
- MCP host / runtime
- Google Docs MCP server
- Gmail MCP server

**Pipeline**: Ingest → Sample → Theme + Draft → Validate → Deliver

## 4. Logical components

### 4.1 Review ingestion (non-MCP)
**Responsibility**: Turn heterogeneous export files into a single canonical representation suitable for analysis.
- **Parsing & Normalization**: Map platform-specific columns into shared semantics (date, rating, title, body, platform).
- **Time windowing**: Retain only reviews from the last 8–12 weeks.
- **Deduping**: Collapse duplicates that would double-count sentiment.
- **PII minimization at source**: Remove or never retain reviewer handles.

### 4.2 Analysis and pulse drafting (LLM-centric)
**Responsibility**: Transform normalized reviews into a structured pulse that matches the milestone format.
- **LLM provider**: Groq (OpenAI-compatible HTTP API) for fast Llama-class inference.
- **Pre-LLM sampling**: Stratified sampling (e.g., bucketing by rating tier × week) to reduce O(thousands) of reviews to ~500–600 inputs, avoiding Groq's 30 RPM / 12K TPM limits.
- **Two-stage LLM call sequence**:
  1. **Stage A (Theme discovery)**: Send the stratified sample and request a JSON list of ≤5 themes (e.g., Fit, Price, Styling).
  2. **Stage B (Pulse drafting)**: Send discovered themes + evidence. Request final `WeeklyPulse`: top 3 themes, 3 verbatim quotes, 3 action ideas, ≤250 words.

### 4.3 Validation layer (deterministic)
**Responsibility**: Act as the contract enforcer between creative LLM output and the outside world.
- **Structural**: Correct counts for themes, quotes, actions.
- **Length**: Pulse body ≤ 250 words.
- **Provenance**: Quotes ⊆ normalized corpus.
- **PII**: Block patterns for emails, phone numbers.
*Outputs: accept (hand off to MCP) or reject (retry).*

### 4.4 MCP delivery — Google Docs & Gmail
**Responsibility**: Persist and distribute the pulse.
- **Google Docs MCP**: Create a new document or update an append-only master log. Capture returned Document ID/URL.
- **Gmail MCP**: Compose a draft email containing a link to the Doc and a terse summary.

## 5. Trust boundaries and privacy

| Boundary | Inside | Must not leak outward |
| :--- | :--- | :--- |
| **Exports → Normalization** | Raw export blobs | Unredacted reviewer identifiers into logs |
| **Normalization → LLM** | Review text needed for theming | Fields you promised to strip |
| **LLM → Validators** | Draft pulse | Treat as untrusted until validated |
| **Validators → MCP** | Validated pulse | Anything that failed validation |

## 6. Data contracts (logical model)

| Artifact | Carries | Consumers |
| :--- | :--- | :--- |
| `NormalizedReview` | Stable review identity, platform, date, rating, title, body | Analysis, quote provenance checks |
| `ThemeCluster` | Theme id/label, membership references, optional rationale | Pulse drafting, ranking |
| `WeeklyPulse` | Top themes (3), quotes (3), actions (3), optional headline, word count | Validators, Docs, Gmail |
| `DeliveryResult` | Doc locator, Gmail draft locator, timestamps | Logging, demo narrative |

## 7. Failure and retry philosophy

| Failure | Desired behavior |
| :--- | :--- |
| **Malformed export** | Stop early with readable diagnostic; partial ingest only if supported |
| **Groq Stage A invalid JSON** | Bounded retries with stricter system prompt; abort if still invalid |
| **Groq Stage B fails validation** | Bounded retries with corrective instructions (point at offending rule) |
| **Docs MCP transient error** | Retry with backoff; mitigate via naming/idempotency |
| **Gmail MCP failure** | Preserve Doc outcome; surface partial success |

## 8. Deployment shapes
- **Interactive mode**: Operator launches the flow in an MCP-capable environment (e.g., IDE agent).
- **Batch mode**: Scheduler invokes the orchestration on a cadence (weekly), requiring unattended auth refresh.
