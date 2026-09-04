# PM Fellowship 10-Slide Deck Framework

Based on a teardown of high-quality submissions, here is the proven structural framework for your 10-slide PM Fellowship presentation. The core philosophy of this framework is **Evidence-Driven Decision Making**. Every slide must connect the previous finding to the next logical step.

---

## 🏗️ Slide-by-Slide Structure

### Slide 1: The Hook & Business Objective
*   **Purpose:** Set the strategic context and state the primary goal clearly.
*   **Key Elements:**
    *   The overarching business context (e.g., market share, profitability constraints).
    *   The exact stated goal: *"Increase the percentage of Monthly Active Customers who purchase products from at least one new category every month."*
    *   The "So What": Why this metric matters right now (e.g., Frequency is won, breadth is the only uncapped lever).

### Slide 2: Metric Breakdown & Strategic Focus
*   **Purpose:** Deconstruct the North Star metric into actionable inputs.
*   **Key Elements:**
    *   KPI Tree: Show how the North Star rolls up into Revenue/Profitability.
    *   Identify the specific behavioral lever you need to pull (e.g., converting routine mission-driven shoppers into cross-category explorers).
    *   A clear statement of the growth challenge vs. the current product reality.

### Slide 3: AI Discovery Engine Findings (The 'What')
*   **Purpose:** Show what you learned from analyzing public data at scale.
*   **Key Elements:**
    *   Brief methodology (Data sources + AI stack used).
    *   Top recurring themes/frictions identified by the AI (e.g., Quality paranoia, Price anchoring, Fear of the unknown).
    *   **Crucial pivot:** Explicitly state that these AI findings are *hypotheses* that require human validation, not absolute facts.

### Slide 4: Primary Research Validation (The 'Why')
*   **Purpose:** Ground the AI hypotheses in reality through user interviews/surveys.
*   **Key Elements:**
    *   Who you spoke to (Sample size and demographics).
    *   What the data actually proved vs. what the AI hallucinated/assumed.
    *   Real verbatim quotes that capture the essence of the friction.
    *   **The Decision:** What assumptions are you killing based on this research?

### Slide 5: Target Segment & Problem Framing
*   **Purpose:** Define exactly *who* you are solving for and the *root cause* of their friction.
*   **Key Elements:**
    *   The Persona (e.g., "The Habit-Led Shopper" or "The Urgency Restocker").
    *   Root Cause Analysis (e.g., 5 Whys framework mapping surface behavior to underlying fear).
    *   The "Job to be Done" or the specific behavioral block (e.g., They have intent, but lack trust at the moment of decision).
    *   Why this segment represents the highest ROI.

### Slide 6: Ideation & Strategic Approach
*   **Purpose:** Show your structured thinking in selecting the right solution.
*   **Key Elements:**
    *   The "How Might We" statement.
    *   Comparison of 2-3 approaches (e.g., AI Mission Intelligence vs. Better Search vs. Post-purchase push).
    *   A prioritization matrix (e.g., RICE score or Impact/Effort) to justify the chosen MVP.
    *   **The Decision:** Why the chosen path is the *only* rational bet for this specific problem.

### Slide 7: The MVP Architecture (The Solution)
*   **Purpose:** Explain what the feature actually is and how it works under the hood.
*   **Key Elements:**
    *   Clear, concise explanation of the core mechanics.
    *   How the AI enables the experience (e.g., Ingestion → Inference → Retrieval → Delivery).
    *   Emphasis on how it fits into the *existing* user flow without adding friction.

### Slide 8: The User Journey (The Experience)
*   **Purpose:** Walk through the feature from the user's perspective.
*   **Key Elements:**
    *   Screenshots/Wireframes of the MVP.
    *   Step-by-step flow (e.g., Cart → Trigger → Nudge → Proof → Decision).
    *   Highlight how the solution specifically dismantles the friction identified in Slide 5.

### Slide 9: Success Metrics & Guardrails
*   **Purpose:** Define how you will measure success and protect the core business.
*   **Key Elements:**
    *   **North Star:** % of MACs buying ≥1 new category / month.
    *   **Leading/Primary Metrics:** E.g., Category Expansion Rate (CER), Suggestion Accept Rate, Trial-to-Repeat Conversion.
    *   **Guardrail Metrics (Critical):** Checkout time, cart abandonment rate, core grocery basket size. (If these break, the experiment dies).

### Slide 10: Risks, Mitigations & Rollout Plan
*   **Purpose:** Show product maturity by anticipating failure modes.
*   **Key Elements:**
    *   Top 3-4 risks (e.g., Irrelevant suggestions eroding trust, added checkout friction, AI hallucinations).
    *   Specific mitigations for each risk (e.g., confidence thresholds, deterministic rules over LLM guesses).
    *   Phased Go-To-Market (GTM) plan (e.g., Days 0-30: Test UI, Days 31-60: A/B Test AI, Days 61-90: Scale).

---

## 🧠 Core Principles for a Winning Deck

1.  **The "So What" Header:** The title of every slide should be the key takeaway or conclusion, not a generic label. (e.g., Instead of "Problem", use "Users shop by mission, not by category").
2.  **Explicit Decisions:** High-scoring decks don't just present data; they show how data forced a decision. Use callouts like **DECISION: We will not require browse-first behavior.**
3.  **Respect the Habit Loop:** If addressing quick-commerce/fashion, recognize that users are in a habit loop. The best MVPs insert a safe trial *inside* an existing mission, rather than trying to force users to aimlessly browse.
4.  **Guardrails are Non-Negotiable:** Always show that you understand the risk of damaging the core business (e.g., slowing down checkout or causing cart abandonment) and have metrics to kill the feature if it hurts the baseline.
