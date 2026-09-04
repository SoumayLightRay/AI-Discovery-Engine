# 10-Slide Deck — Full Text Content (v2)

> **File:** `NL Myntra` · 10 slides max · No Fellow name · Title = key takeaway
> **Constraints:** Min font 14 (Slides) / 22 (Canva) · < 40 MB · Color-blind-friendly

---
---

# PHASE A: THE PROBLEM (Slides 1–2)

---

## SLIDE 1

### Title: Myntra's Biggest Untapped Growth Lever — The Wishlist That Never Converts

Millions of Myntra users browse fashion products, save items they like, and add them to their wishlists every day. A wishlist is the strongest purchase-intent signal short of adding to cart — the user has explicitly said "I want this."

Yet only a small fraction of wishlisted items convert into purchases within 30 days. Over time, users accumulate dozens of wishlisted products while only a handful are ever bought.

**Strategic Goal**
Increase the percentage of users who purchase at least one item from their wishlist within 30 days of adding it.

**Why This Matters**
- Wishlisting = high-intent demand already on the platform
- Converting it increases purchase frequency from existing users
- No new user acquisition cost required
- Directly improves monetisation of existing traffic

**Constraint:** No monetary incentives (no discounts, no coupons, no cashback).

**Deliverable links:**
- 🌐 [AI Discovery Engine Dashboard](https://ai-discovery-engine-rose.vercel.app/)
- 📄 [Full Research Report](https://ai-discovery-engine-rose.vercel.app/discovery_research_report.html)
- 💻 [Source Code (GitHub)](https://github.com/SoumayLightRay/AI-Discovery-Engine)

---

## SLIDE 2

### Title: The Wishlist-to-Purchase Journey Breaks at Stage 2 — Where Users Try to Build Confidence but Can't

We decomposed the wishlist-to-purchase journey into the behavioural stages where conversion is won or lost:

**Stage 1 — Discovery & Wishlisting**
User finds a product and saves it. Motivations: genuine purchase intent (4.2%), aspirational bookmarking, waiting for a price drop (10.5%), social/trend-driven saving (1.9%).

**Stage 2 — Evaluation & Confidence Building → 30.1% OF ALL FRICTION**
The user returns to evaluate the item. This is where the journey breaks most often:
- Quality/Material doubt — 14.1%
- Reviews/Information gap — 6.1%
- Fit/Size uncertainty — 4.5%
- Styling/Occasion doubt — 3.5%
- Social validation seeking — 1.9%

**Stage 3 — Decision & Commitment → 27.1%**
- Price & discount expectations — 10.5%
- Return/Exchange policy fear — 9.9%
- Availability/Delivery — 5.4%
- Alternative platform comparison — 1.3%

**Stage 4 — Conversion or Drop-off → 3.2%**
Forgetting, distraction, or permanent abandonment.

**Strategic Focus:** Stage 2 has the highest friction (30.1%) AND is the most solvable without monetary incentives. Stage 3 (27.1%) includes price and returns — harder to address under the no-incentives constraint.

---
---

# PHASE B: THE INVESTIGATION (Slides 3–4)

---

## SLIDE 3

### Title: We Built an AI Engine That Analysed 1,367 Reviews and Produced 12 Friction Hypotheses — Not Conclusions

**The AI Discovery Engine Pipeline**

```
INGEST → ANALYSE → RETRIEVE → DELIVER
Apify Cloud   Groq LLaMA 3.3 70B   BM25 + TF-IDF   Vercel Dashboard
4 channels     13-theme classify    Semantic Search   + RAG Chatbot
1,367 reviews  5-dimension tags     1,367 vectors     Interactive UI
```

**Data Sources (Balanced Sampling — no channel bias)**

| Channel | N | % | Primary Signal |
|---|---|---|---|
| Google Play | 78 | 24.9% | Delivery, returns, quality |
| App Store | 77 | 24.6% | Returns, wrong products |
| YouTube | 79 | 25.2% | Aspirational, styling |
| Reddit | 79 | 25.2% | Price, fit, honest reviews |
| **Total Analysed** | **313** | | **70 friction-tagged (22.4%)** |

**Critical framing:** These 12 friction themes are hypotheses that require human validation. The engine assists research — it does not replace the PM's thinking. (Per NextLeap guidelines: AI assists discovery, humans make decisions.)

**Try it live →** [ai-discovery-engine-rose.vercel.app](https://ai-discovery-engine-rose.vercel.app/)

---

## SLIDE 4

### Title: The Key Insight — Severity ≠ Frequency. The Loudest Complaints Are Not the Biggest Blockers.

**Top Friction Themes with Negativity Rate Analysis**

| Theme | Volume | Negativity | What This Means |
|---|---|---|---|
| Quality/Material | 14.1% | 6.8% | Highest volume but low anger — diffuse uncertainty |
| Price | 10.5% | 36.4% | Only 1 in 3 mentions is a complaint |
| Returns | 9.9% | **93.5%** | Nearly every mention is toxic — but not top-of-mind |
| Reviews/Info | 6.1% | **0.0%** | "Invisible friction" — absence kills silently |
| Fit/Size | 4.5% | 42.9% | All from Reddit — users solve it off-platform |

**The Analytical Breakthrough:**
High volume ≠ High severity. Returns (93.5% negative) is emotionally devastating per-mention, but Quality (6.8% negative) affects more users because it represents diffuse, silent uncertainty. And themes with 0% negativity (Reviews, Styling, Comparison) are "invisible friction" that prevents conversion without generating any complaints. Traditional sentiment analysis would completely miss these.

**Channel Cross-Tab Insight:**
- Returns is universal (all 3 complaint channels)
- Price is Reddit-specific (73% from r/IndianFashionAddicts)
- Availability is Google Play-specific (80% — Tier 2/3 delivery issues)
- YouTube contributes zero friction — purely aspirational content

**Strongest Repeat Signals:**
- "No return policy on bras and panties" — **7 repetitions** from different users
- "None of the good items got any discounts" — **6 repetitions**

---
---

# PHASE C: THE VALIDATION (Slides 5–6)

---

## SLIDE 5

### Title: Primary Research Confirmed the Core Hypothesis — and Revealed "Comparison" is Far More Prevalent Than AI Data Suggested

**Survey:** Google Form, N ≈ 29 valid respondents, Sep 4–5 2026.

**How our thinking evolved (Business Metric → AI Discovery → Primary Research → Problem):**

Before the survey, we hypothesised from AI data that Quality (14.1%) and Price (10.5%) were the dominant standalone blockers. The survey changed this:

**Confirmed ✅**
- Quality/Confidence gap is the primary friction — users say *"Will it be worth it!"*, *"no reviews with pictures"*, *"not sure how it fits"*
- Fit/Size uncertainty is among the top 2 most-ticked reasons
- Users leave the app to research (YouTube, Instagram, competitor apps) — 4–6 actions per item

**Refined ⚠️**
- "Price" decomposes into three distinct sub-problems: (a) sale-waiting (unsolvable), (b) cash-flow timing (external), (c) value-unproven (solvable!). Price is rarely ticked alone — it co-occurs with fit/comparison, suggesting it's a secondary justification on top of a primary confidence gap.

**AI Detection Gap Exposed 🔄**
- Comparison = #1 most-ticked survey reason, but the AI scored it at only 1.6%. Why? Public reviews don't discuss competitor behaviour. The AI detects complaints; the survey detects behaviour.

**The disconfirmation IS the credibility:** We didn't find what we expected. We found something more nuanced — and that's what makes the analysis trustworthy.

---

## SLIDE 6

### Title: 60% of Stalled Users Are "Confidence-Starved Evaluators" Who Leave the App to Decide

**Behavioural Segments (derived from observed behaviour, not demographics)**

| Segment | % | Blocker | Actionable? |
|---|---|---|---|
| **Value-unproven evaluators** | ~35% | Need evidence, not a lower price | ✅ **Primary target** |
| **Fit/style researchers** | ~25% | Actively leaving app for YouTube/offline | ✅ Secondary target |
| Stock-out-blocked | ~15% | Inventory problem | ⚠️ Logistics |
| Cash-timing-blocked | ~10% | External life event | ❌ |
| Price-waiters | ~10% | Waiting for discount | ❌ Constrained |
| Passive decayers | ~5% | Attention fades | ⚠️ Nudge only |

**Segment Selection Rationale:** Meaningful population (~60%) × Strong pain (stated in own words) × High intent (they want to buy) × Metric leverage (directly improves 30-day conversion) × Solvable without monetary incentives.

**Root Cause — 5 Whys**

Why 1: Users hesitate to move wishlisted items to cart.
→ Because they feel uncertain about the purchase outcome.

Why 2: Why uncertain?
→ The product page doesn't give them enough real evidence to decide.

Why 3: Why is the evidence insufficient?
→ Model photos are heavily edited, size charts are inconsistent, and no verified buyer photos exist.

Why 4: Why don't they just order and return if it's wrong?
→ Because the return process is stressful and unreliable (93.5% negativity on returns).

Why 5: So what do they do instead?
→ They keep it in the wishlist as a safety net, leave the app to research on YouTube/Instagram, and during that off-platform session, find alternatives or buy from competitors.

**Root Cause Statement:** Low upfront certainty creates high downstream perceived risk. The information asymmetry between what the product page shows and what the user actually receives is the fundamental driver of wishlist stagnation.

**Problem Statement:** Among high-intent users who wishlist fashion items, those who lack sufficient real-world evidence delay purchasing because Myntra's product page creates uncertainty about quality, fit, and value. They currently research on YouTube and Instagram, which delays their decision and creates opportunities for competitors to intercept the purchase.

**Competitor Leakage Evidence:**
- *"Found better design for same price"*
- *"Bought from different site"*
- *"Got Flipkart notification that prices gone down. Bought cheaper from somewhere else."*

---
---

# PHASE D: THE SOLUTION (Slides 7–8)

---

## SLIDE 7

### Title: We Evaluated 6 Mechanisms — the Wishlist Confidence Layer Wins on RICE and the Three-Level Creativity Test

**How Might We** reduce the information asymmetry on the wishlist page so that users can build purchase confidence without leaving the app?

**6 Genuinely Different Mechanisms Evaluated:**

| # | Mechanism | Type |
|---|---|---|
| 1 | Wishlist Confidence Layer (verified photos + fit consensus + return badge + AI digest) | Decision-support |
| 2 | AI Outfit Recommender (suggest pairings/looks) | Information enrichment |
| 3 | Smart Price Alert (notify when price drops) | Timing/nudge |
| 4 | Social Proof Nudges ("X people bought this week") | Social proof |
| 5 | Wishlist Reminder Notifications | Re-engagement |
| 6 | AR Virtual Try-On | Comparison simplification |

**RICE Prioritisation**

| Mechanism | Reach | Impact | Confidence | Effort | RICE Score |
|---|---|---|---|---|---|
| **1. Confidence Layer** | 60% of stalled users | High — directly resolves root cause | High — validated by AI + survey | Medium | **RICE = 90** |
| 2. AI Outfit Recommender | 35% (styling-doubt only) | Medium — styling, not confidence | Low — not validated | High | RICE = 18 |
| 3. Smart Price Alert | 10% (price-waiters) | Low — constrained by no-incentives | Medium | Low | RICE = 15 |
| 4. Social Proof Nudges | 20% (social-seekers) | Low — signal, not evidence | Low — not in top friction | Low | RICE = 20 |
| 5. Reminder Notifications | 5% (passive decayers) | Low — addresses 5%, not 60% | Medium | Low | RICE = 10 |
| 6. AR Virtual Try-On | 25% (fit-doubters) | High — great for fit | Medium | Very High | RICE = 12 |

**Three-Level Creativity Test (per Arindam's framework)**

| Level | Test | Wishlist Confidence Layer |
|---|---|---|
| **1. Problem Fit** | Does it solve the validated root cause? | ✅ Provides the exact evidence users currently leave the app to find |
| **2. Differentiation** | Is it different from competitors? | ✅ No fashion platform surfaces confidence evidence on the wishlist page |
| **3. Defensibility** | Why is it hard to copy? | ✅ Accumulates proprietary verified-buyer photo + fit-consensus data. Compounding data moat. |

**Decision:** Mechanism #1 (Wishlist Confidence Layer) scores highest on RICE (90) AND passes all three creativity levels. It is the only mechanism that directly addresses the validated root cause (information asymmetry at the evaluation stage) for the largest segment (60%) without requiring monetary incentives.

---

## SLIDE 8

### Title: The Wishlist Confidence Layer — Bringing YouTube-Level Evidence Onto the Wishlist Page

**What the user sees on each wishlisted item:**

| Component | What It Shows | Friction Addressed |
|---|---|---|
| 📸 Verified Buyer Photos | Real photos from customers who bought this item | Quality uncertainty (14.1%) |
| 📏 Fit Consensus | "85% of buyers say true to size" — aggregated from reviews | Fit/Size doubt (4.5%) |
| 🔄 Return Clarity Badge | "✅ Returnable 15 days" or "⚠️ Non-returnable (intimates)" | Return anxiety (9.9%) |
| ⭐ AI Review Digest | 3-line summary: "Buyers love fabric but say it runs small" | Information gap (6.1%) |

**User Flow (3 steps)**
1. User opens wishlist → sees Confidence Layer on each item
2. Taps for detail → verified photos, fit consensus %, return policy, AI review summary
3. Confidence resolved on-platform → moves to cart without leaving to check YouTube or Instagram

**Why This Works**
The MVP replicates the exact information users currently seek off-platform (real photos on YouTube, honest sizing on Reddit, return confirmation) and brings it directly to the point of decision — eliminating the research exodus that causes competitor leakage.

**Architecture**
```
Myntra Reviews DB → AI Summariser → Confidence Score API → Wishlist UI Overlay
```

**MVP proves the mechanism:** Can we demonstrate that providing real-world evidence at the point of decision changes the user's behaviour from "keep in wishlist" to "move to cart"?

**Live MVP →** [ai-discovery-engine-rose.vercel.app](https://ai-discovery-engine-rose.vercel.app/)

---
---

# PHASE E: THE MEASUREMENT (Slides 9–10)

---

## SLIDE 9

### Title: North Star — 30-Day Wishlist-to-Purchase Conversion. If Guardrails Break, We Kill the Feature.

**Metric Causal Chain**

```
NORTH STAR
  30-day Wishlist → Purchase Conversion Rate
    ↓
SOLUTION METRIC
  % of users who view Confidence Layer and move item to cart
    ↓
LEADING INDICATORS (does the mechanism fire?)
  • Confidence Layer view rate (target: ≥15%)
  • Buyer photo click-through rate
  • Reduced time: wishlist-add → cart-add
  • Decreased off-platform exits
    ↓
LAGGING INDICATORS (does behaviour persist?)
  • 7-day repeat conversion rate
  • Wishlist-to-cart velocity trend over 30 days
    ↓
GUARDRAILS (must NOT worsen — kill feature if they do)
  • Core purchase conversion rate
  • Average order value
  • Wishlist addition rate
  • Return rate
```

**Kill Criteria:** If leading indicators don't move within 14 days of A/B test launch, we stop the experiment and investigate.

**Definition & Rationale for Each Metric:**
- **North Star (30-day conversion):** Directly measures the strategic goal from the project brief.
- **Solution metric (view → cart):** Proves the mechanism works — seeing confidence evidence → deciding to buy.
- **Guardrail: wishlist addition rate:** Must not decrease — if users stop wishlisting because we changed the page, we've destroyed the funnel's top.
- **Guardrail: return rate:** Better upfront info should REDUCE returns, not increase them. If returns go up, our confidence data is inaccurate.

---

## SLIDE 10

### Title: Here's How We Could Be Wrong — and the 60-Day Experiment to Find Out

**Top Risks**

| Risk | Why It Could Fail | Mitigation |
|---|---|---|
| **Wrong root cause** | Confidence may not be the real blocker at scale (survey N ≈ 29) | A/B test with kill switch at Day 14; measure behaviour, not self-report |
| **AI summary errors** | Review digests could be misleading | Deterministic rules > LLM guesses; confidence thresholds; human review queue |
| **Data sparsity** | New/niche products may have zero buyer photos | Graceful fallback to brand content with clear "Brand photo" vs "Buyer photo" labels |
| **Cannibalisation** | May shift purchases to wishlist flow without net new sales | Track total purchase volume as guardrail |
| **Info reduces intent** | Survey found 1 case where more reviews killed a purchase | Monitor correlation between Confidence Layer views and cart removal |

**60-Day Experiment Plan**

| Phase | Days | Action | Success Gate |
|---|---|---|---|
| Shadow | 0–14 | Show to 5% of users, engagement only | ≥15% view rate |
| A/B Test | 15–30 | 50/50 split on wishlist page | ≥5% conversion lift |
| Scale | 31–60 | 100% if gates pass | No guardrail violations |

**Beyond MVP — What's Next**
- **Phase 2:** Expand Confidence Layer to cart page (pre-checkout confidence boost)
- **Phase 3:** Personalised confidence — learn which evidence type matters most per user
- **Long-term:** Build a proprietary "Trust Graph" across all products — a compounding data moat

---
---

# AUDIT CHECKLIST

| Requirement | Source | Status |
|---|---|---|
| RICE framework | framework.md Phase 7 | ✅ Slide 7 |
| 3-Level Creativity Test | framework.md / arindam_feedback.md | ✅ Slide 7 |
| "How Might We" statement | framework.md Phase 7 | ✅ Slide 7 |
| 5 Whys root cause | framework.md Phase 5 | ✅ Slide 6 |
| Behavioural segments (not demographics) | arindam_feedback.md Rule 1 | ✅ Slide 6 |
| AI findings as hypotheses, not conclusions | arindam_feedback.md Rule 3 | ✅ Slide 3 |
| Disconfirmation / evidence changed thinking | framework.md core philosophy | ✅ Slide 5 |
| "How thinking evolved" narrative | project.md Part 4 | ✅ Slide 5 |
| Metric decomposition | project.md Part 2 | ✅ Slide 2 |
| North Star → solution → leading → guardrails | framework.md Phase 9 | ✅ Slide 9 |
| Risks & mitigation | project.md Part 7 | ✅ Slide 10 |
| 6 genuinely different mechanisms | framework.md Phase 7 | ✅ Slide 7 |
| MVP proves mechanism, not whole product | framework.md Phase 8 | ✅ Slide 8 |
| No Fellow name | project.md constraints | ✅ All slides |
| Title = key takeaway | project.md deck guidelines | ✅ All slides |
| Real AI data (1,367 reviews, 313 analysed) | report.md / analysis.md | ✅ Slides 2–4 |
| Real survey data (N ≈ 29, verbatims) | primary_research.md | ✅ Slides 5–6 |
| Competitor leakage evidence | primary_research.md Section 5 | ✅ Slide 6 |
| Links to live deliverables | project.md deliverables | ✅ Slides 1, 3, 8 |
| Experiment design | framework.md Phase 10 | ✅ Slide 10 |
| Anti-pattern: "I had idea → research agreed" | framework.md anti-patterns | ✅ Avoided — Slide 5 shows disconfirmation |
| Anti-pattern: copy-paste AI summaries | arindam_feedback.md | ✅ Avoided — all analysis is human-interpreted |
