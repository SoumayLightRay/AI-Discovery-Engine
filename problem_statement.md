# Problem Statement: Wishlist Conversion AI Discovery Engine

## Problem Statement

Millions of users browse fashion products on platforms like Myntra, AJIO, and Nykaa Fashion, saving items they like to their wishlists. A wishlist represents explicit user interest, yet users can accumulate dozens—or even hundreds—of products while only a small proportion eventually translate into purchases. 

**The User Problem (Discovered):**
Wishlist users who still want their saved items (56% of wishlisters) cannot confidently decide whether to buy because the product page lacks real-world evidence — verified buyer photos, honest fit consensus, and quality proof. This forces them off-platform to research on Amazon, Instagram, YouTube, and brand websites (89% of users do this), where **42% end up buying from competitors**. Price is the #1 stated barrier (44%), but 11/12 interview respondents have paid MORE for products with stronger confidence signals — revealing that information asymmetry, not price sensitivity, is the root cause for the solvable segment.

**The Business Metric:**
**Increase the percentage of users who purchase at least one item from their wishlist within 30 days of adding it.** Improving this conversion could increase purchase frequency, improve monetization, and extract greater value from high-intent demand already present on the platform.

However, the underlying user problem was unknown at the start. The task was to discover this problem and build an MVP solution with one strict constraint: **NO monetary incentives can be offered to the users.**

Before proposing a solution, we built an **AI-Powered Discovery Engine** that analyzes public user feedback at scale to understand user behavior, friction points, and unmet needs regarding wishlists.

## End-to-end flow (what “done” looks like):

1. **Ingest** user feedback from diverse, public sources (App Store reviews, Play Store reviews, Reddit discussions, YouTube comments, and fashion communities).
2. **Process & Analyze** the unstructured data using an AI-native stack (e.g., Claude, GPT, Agents, n8n, Zapier) to extract deep qualitative insights.
3. **Synthesize** the findings to answer specific behavioral questions (e.g., intent vs. bookmarking, uncertainties around fit/styling, external validation needs).
4. **Deliver** a structured discovery report that identifies, quantifies (where possible), and compares potential opportunity areas to influence the wishlist-to-purchase metric.

## Deliverables

- **AI Discovery Engine**: A testable workflow, script, or agent pipeline that ingests and analyzes the data.
- **Discovery Output**: The synthesized findings that answer the core research questions and highlight opportunity areas.
- **Methodology Documentation**: A 1-slider (or brief document) explaining how the AI engine works.

## Who This Helps

| Audience | Why |
| :--- | :--- |
| **Product / Growth Teams** | To discover the root causes preventing wishlist conversion and prioritize high-potential, non-monetary opportunity areas. |
| **User Researchers** | To use AI-generated insights at scale as a foundational starting point before conducting targeted 1:1 user interviews. |
| **Leadership** | To understand the "why" behind wishlist stagnation and align on the strategic direction for the MVP. |

## What You Must Build

An AI-driven pipeline that answers the following core questions:
- Why do users add fashion products to their wishlist?
- What prevents wishlisted products from eventually being purchased?
- What uncertainties remain after users have identified a product they like?
- What causes users to postpone a purchase?
- How do users compare multiple shortlisted products?
- What information do users seek outside the platform before purchasing?
- What role do fit, size, styling, price, reviews, occasion, and social validation play?
- When do users use the wishlist as genuine purchase intent versus simply as a bookmarking mechanism?
- How do these behaviors differ across user segments?
- What unmet needs emerge consistently across user conversations?

**Crucially, the workflow must go beyond basic summarization or sentiment analysis. It must enable the identification and comparison of actionable opportunity areas.**

## Key Constraints

- **No Monetary Incentives:** The final solution addressing the discovered problem cannot rely on discounts, cashbacks, or financial rewards.
- **Data Privacy:** Use only publicly available conversations and reviews. Do not scrape behind logins or violate terms of service.
- **Depth of Analysis:** Output must be structured into themes, user segments, and specific friction points, not just generic summaries.

## Logical Architecture (Proposed)

1. **Data Ingestion & Normalization**
   - **Sources:** Public APIs or exports from App/Play Stores, Reddit (via API), YouTube comments.
   - **Normalization:** Map heterogeneous data into a unified schema (source, timestamp, text, context).
   
2. **AI Analysis Engine (LLM-centric)**
   - **Stage A (Theme Discovery & Classification):** Pass batches of text to an LLM to classify intent (bookmarking vs. purchasing) and extract friction points (fit, price, validation).
   - **Stage B (Question Answering & Synthesis):** Prompt the LLM to aggregate the classified data and answer the specific PM research questions with verbatim quotes as evidence.
   
3. **Validation & Output Layer**
   - **Structuring:** Ensure the LLM output maps directly to the required opportunity areas.
   - **Delivery:** Output the final insights into a readable format (e.g., Markdown, Google Docs via MCP, or a Notion database) for the Product Manager to review before proceeding to primary user research.
