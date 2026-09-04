# Key Technical & Product Decisions

## 1. LLM Selection
- **Decision:** Use **Groq (Llama-3.3-70b-versatile)** for the analysis engine.
- **Rationale:** Groq provides extremely fast inference which is crucial for processing hundreds of reviews interactively. It is cost-effective and capable of complex thematic extraction. 
- **Constraints Managed:** We will enforce a chunking strategy to respect the 30 Requests Per Minute (RPM) and 12K Tokens Per Minute (TPM) limits.

## 2. Integration Pattern (Reporting)
- **Decision:** Use **Model Context Protocol (MCP)** for Google Docs integration rather than building direct REST API/OAuth clients in the core app.
- **Rationale:** Keeps the core orchestration script clean. The MCP server handles all Google OAuth and document formatting complexities.

## 3. Data Processing Rules
- **Decision:** Exclude short reviews (< 6 words) and non-English text.
- **Rationale:** Short reviews (e.g., "Good app", "Nice clothes") lack the qualitative depth required to answer complex questions about wishlist intent and purchase hesitancy.

## 4. Problem Space Constraint
- **Decision:** No monetary incentives.
- **Rationale:** Strict requirement from the PM Fellowship brief. The solution must focus on UX, information architecture, confidence-building (fit/style), or workflow improvements, not discounts.
