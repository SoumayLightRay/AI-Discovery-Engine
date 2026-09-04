# 10-Slide Deck Architecture — NL Myntra

> **Naming:** `NL Myntra`  
> **Format:** Google Slides / Canva (1920×1080)  
> **Min font:** 22 (Canva) / 26 (Figma) / 14 (Google Slides)  
> **Max file size:** < 40 MB  
> **Rule:** No Fellow name anywhere. Title of every slide = key message, not a generic label.

---

## SLIDE 1 — Title + Business Problem

**Title:** *"Myntra's Biggest Untapped Growth Lever: The Wishlist That Never Converts"*

**Content:**
- One-line context: "Millions of users wishlist fashion items every day — expressing explicit purchase intent — but only a fraction convert within 30 days."
- The strategic goal (verbatim from project brief): *"Increase the % of users who purchase ≥1 wishlisted item within 30 days of adding it."*
- Why it matters: "Wishlisting is the highest-intent signal short of adding to cart. Improving this conversion rate increases purchase frequency and monetises existing demand — without needing new user acquisition."
- Constraint callout: **No monetary incentives permitted.**

**Visual:** A simple funnel graphic: Browse → Wishlist → ??? → Purchase, with the "???" highlighted as the gap.

**Links:** [Live Dashboard](https://ai-discovery-engine-rose.vercel.app/) · [Full Report](https://ai-discovery-engine-rose.vercel.app/discovery_research_report.html) · [GitHub](https://github.com/SoumayLightRay/AI-Discovery-Engine)

---

## SLIDE 2 — Metric Decomposition: Where the Journey Breaks

**Title:** *"The Wishlist-to-Purchase Journey Breaks at 5 Stages — Stage 2 (Evaluation) Has the Highest Friction"*

**Content:** The 4-stage behavioural funnel with friction percentages:

```
Stage 1: Discovery & Wishlisting
  ├── Genuine intent (4.2%)
  ├── Aspirational bookmarking
  └── Social/trend saving (1.9%)

Stage 2: Evaluation & Confidence Building ← 30.1% OF ALL FRICTION
  ├── Quality/Material doubt (14.1%)
  ├── Reviews/Info gap (6.1%)
  ├── Fit/Size uncertainty (4.5%)
  ├── Styling/Occasion doubt (3.5%)
  └── Social validation (1.9%)

Stage 3: Decision & Commitment (27.1%)
  ├── Price expectations (10.5%)
  ├── Return policy fear (9.9%)
  ├── Availability (5.4%)
  └── Alternatives (1.3%)

Stage 4: Conversion or Drop-off (3.2%)
```

**Key callout box:** "Stage 2 is the highest-leverage intervention point AND the most solvable without monetary incentives."

**Visual:** Colour-coded funnel or horizontal pipeline. Red highlight on Stage 2.

---

## SLIDE 3 — AI Discovery Engine: How We Investigated

**Title:** *"We Built an AI Engine That Analysed 1,367 Reviews Across 4 Channels and Identified 12 Friction Hypotheses"*

**Content:**

**Pipeline diagram:**
```
INGEST → ANALYSE → RETRIEVE → DELIVER
Apify      Groq LLaMA    BM25+TF-IDF    Vercel
4 channels  3.3 70B       Semantic       Dashboard
1,367 reviews  13-theme    Search         + Chatbot
```

**Data sources table (compact):**

| Channel | N | Signal Type |
|---|---|---|
| Google Play | 78 | Delivery, returns, quality |
| App Store | 77 | Returns, wrong products |
| YouTube | 79 | Aspirational, styling |
| Reddit | 79 | Price, fit, honest reviews |

**Critical framing:** "These 12 themes are **hypotheses**, not conclusions. The engine assists research — it does not replace the PM's thinking."

**Link:** [Try the Live Engine →](https://ai-discovery-engine-rose.vercel.app/)

---

## SLIDE 4 — What the Evidence Revealed: Competing Opportunities

**Title:** *"Quality Doubt is the Highest-Volume Friction (14.1%), but Returns is the Most Toxic (93.5% Negative) — Severity ≠ Frequency"*

**Content:**

**Top 5 opportunity table:**

| Theme | Volume | Negativity | Insight |
|---|---|---|---|
| Quality/Material | 14.1% | 6.8% | Diffuse uncertainty — users aren't angry, they're unsure |
| Price | 10.5% | 36.4% | Only 1 in 3 mentions is a complaint; rest are neutral comparisons |
| Returns | 9.9% | **93.5%** | Nearly every mention is toxic — but not top-of-mind for most users |
| Reviews/Info | 6.1% | **0.0%** | "Invisible friction" — absence of info kills silently |
| Fit/Size | 4.5% | 42.9% | All from Reddit; users actively research offline/YouTube |

**Key insight box:** "High volume ≠ High severity. The engine's negativity-rate analysis reveals which themes cause silent hesitation (Quality, Reviews) vs. which cause visceral anger (Returns, Availability)."

**Channel cross-tab mini-chart:** Show that Returns is universal (all channels), Price is Reddit-specific, Availability is Google Play-specific.

**Visual:** Horizontal bar chart or bubble chart plotting Volume vs. Negativity Rate.

---

## SLIDE 5 — Primary Research: What Changed Our Thinking

**Title:** *"Survey of 29 Users Confirmed Our Core Hypothesis — and Revealed That 'Comparison' is Far More Prevalent Than AI Data Suggested"*

**Content:**

**AI ↔ Survey cross-validation (compact):**

| AI Hypothesis | Survey Verdict |
|---|---|
| Quality/Material = top friction | ✅ Confirmed — split into "quality-truth" and "value-justification" |
| Price = major blocker | ⚠️ Refined — rarely standalone; 3 sub-problems (sale-waiting, cash-timing, value-unproven) |
| Comparison = minor (1.6%) | 🔄 Underweighted — **#1 most-ticked reason** in survey |
| Fit/Size = watch | ✅ Confirmed — users leave app to resolve via YouTube/offline |

**Key disconfirmation (the credibility):**
> "We expected Price to be the dominant blocker. The survey showed that price is almost never ticked alone — it co-occurs with fit/comparison doubts. The real friction is confidence, not cost."

**Verbatim quotes:** *"Will it be worth it!"*, *"no reviews with pictures"*, *"not sure how it fits"*

**Visual:** Before/After hypothesis ranking showing how survey changed the priority order.

---

## SLIDE 6 — Target Segment + Root Cause

**Title:** *"60% of Stalled Users Are 'Confidence-Starved Evaluators' — They Want to Buy but Can't Decide Without Leaving the App"*

**Content:**

**Behavioural segment table:**

| Segment | % | Actionable? |
|---|---|---|
| **Value-unproven evaluators** | ~35% | ✅ Primary target |
| **Fit/style researchers** | ~25% | ✅ Secondary target |
| Stock-out-blocked | ~15% | ⚠️ Logistics |
| Cash-timing-blocked | ~10% | ❌ External |
| Price-waiters | ~10% | ❌ Constrained |
| Passive decayers | ~5% | ⚠️ Nudge only |

**Root cause chain (visual arrow flow):**
```
Symptom: Wishlisted items sit unconverted
    ↓
Behaviour: User delays purchase
    ↓
Reason: "I'm not sure if it's worth it"
    ↓
Workaround: Leaves app → YouTube, Instagram, competitors (4–6 actions per item)
    ↓
Consequence: Finds alternative → buys from competitor → Myntra loses the sale
    ↓
ROOT CAUSE: Product page lacks real-world evidence → user can't decide on-platform
```

**Problem statement:**
> "Among high-intent users who wishlist fashion items, those who lack sufficient real-world evidence (verified buyer photos, honest fit feedback, quality proof) delay purchasing because Myntra's product page creates uncertainty. They leave the app to research on YouTube and Instagram, where competitors intercept the purchase."

---

## SLIDE 7 — Solution Alternatives + Why One Wins

**Title:** *"We Evaluated 6 Mechanisms — 'Wishlist Confidence Layer' Wins Because It Directly Resolves the Root Cause Without Monetary Incentives"*

**Content:**

**6 mechanisms evaluated:**

| # | Mechanism | Problem Fit | Differentiation | Defensibility | Verdict |
|---|---|---|---|---|---|
| 1 | **Wishlist Confidence Layer** (verified photos + fit consensus + return badge) | ✅ Directly resolves info asymmetry | ✅ No competitor does this on wishlist | ✅ Accumulates proprietary buyer data | **WINNER** |
| 2 | AI Outfit Recommender | ⚠️ Addresses styling, not confidence | ❌ Multiple competitors have this | ❌ Easily copied | Rejected |
| 3 | Smart Price Alert | ❌ Requires monetary incentive logic | ⚠️ Flipkart already does this | ❌ No moat | Rejected |
| 4 | Social Proof Nudges ("X people bought this") | ⚠️ Partial — social, not product evidence | ❌ Amazon already does this | ❌ Trivial to copy | Rejected |
| 5 | Wishlist Reminder Notifications | ⚠️ Addresses forgetting (5%), not confidence (60%) | ❌ Every app does this | ❌ No moat | Rejected |
| 6 | AR Virtual Try-On | ✅ Great for fit | ❌ Capital-intensive | ✅ Hard to copy | Too complex for MVP |

**Three-level creativity test (from Arindam's feedback):**
- **Level 1 (Problem Fit):** Directly solves the validated root cause (information asymmetry)
- **Level 2 (Differentiation):** No fashion platform surfaces confidence evidence directly on the wishlist page
- **Level 3 (Defensibility):** Accumulates proprietary verified-buyer photo and fit-consensus data over time

---

## SLIDE 8 — MVP: How It Works in the Real Journey

**Title:** *"The Wishlist Confidence Layer: Bringing YouTube-Level Evidence Onto the Wishlist Page"*

**Content:**

**What the user sees on each wishlisted item:**

| Component | What It Shows | Friction Addressed |
|---|---|---|
| 📸 Verified Buyer Photos | Real customer photos (not marketing) | Quality uncertainty |
| 📏 Fit Consensus | "85% of buyers say true to size" | Fit/Size doubt |
| 🔄 Return Clarity Badge | "✅ Returnable within 15 days" or "⚠️ Non-returnable" | Return anxiety |
| ⭐ AI Review Digest | 3-line summary: "Buyers love the fabric but say it runs small" | Information gap |

**User flow (3 steps):**
1. User opens wishlist → sees Confidence Layer on each item
2. Taps for detail → verified photos + fit consensus + return policy
3. Confidence resolved → moves to cart without leaving the app

**Architecture:**
```
Myntra Reviews DB → AI Summariser → Confidence Score API → Wishlist UI Overlay
```

**Link:** [Try the Live MVP →](https://ai-discovery-engine-rose.vercel.app/)

**Screenshots/wireframes** of the deployed MVP

---

## SLIDE 9 — Success Metrics & Guardrails

**Title:** *"North Star: 30-Day Wishlist → Purchase Conversion. If Guardrails Break, We Kill the Feature."*

**Content:**

**Causal metric chain:**

```
NORTH STAR
  30-day Wishlist → Purchase Conversion Rate
    ↓
SOLUTION METRIC
  % of users who view Confidence Layer and move item to cart
    ↓
LEADING INDICATORS
  • Confidence Layer view rate (target: ≥15%)
  • Buyer photo click-through rate
  • Reduced time: wishlist-add → cart-add
  • Decreased off-platform research exits
    ↓
GUARDRAILS (must NOT worsen)
  • Core purchase conversion rate
  • Average order value
  • Wishlist addition rate (don't discourage wishlisting)
  • Return rate (better info should NOT increase returns)
```

**Kill criteria:** "If leading indicators don't move within 14 days of A/B test launch, we stop the experiment."

---

## SLIDE 10 — Risks, Experiment Design & What's Next

**Title:** *"Here's How We Could Be Wrong — and the 60-Day Experiment to Find Out"*

**Content:**

**Top risks:**

| Risk | Why It Could Fail | Mitigation |
|---|---|---|
| Wrong root cause | Confidence may not be the real blocker at scale | A/B test with kill switch at Day 14 |
| AI content errors | Review summaries could be inaccurate | Deterministic rules > LLM guesses; confidence thresholds |
| Data sparsity | Some products have zero buyer photos | Fallback to brand content with clear labelling |
| Cannibalisation | Shifts purchases to wishlist flow without net new | Track total purchase volume as guardrail |

**60-day experiment plan:**

| Phase | Days | Action | Gate |
|---|---|---|---|
| Shadow | 0–14 | 5% of users, measure engagement | ≥15% view rate |
| A/B Test | 15–30 | 50/50 split on wishlist page | ≥5% conversion lift |
| Scale | 31–60 | 100% if gates pass | No guardrail violations |

**What's next (beyond MVP):**
- Phase 2: Expand to cart page (pre-checkout confidence)
- Phase 3: Personalised confidence — learn which evidence type matters most per user
- Long-term: Proprietary "Trust Graph" across all products — defensible data moat

---

## Storytelling Arc Summary

```
Slide 1:  "Here's the business problem"
Slide 2:  "Here's where the behaviour breaks"
Slide 3:  "Here's how we investigated"
Slide 4:  "Here's what the evidence said"
Slide 5:  "Here's what primary research changed"     ← THE CREDIBILITY MOMENT
Slide 6:  "Here's who the problem affects and why"
Slide 7:  "Here's why this solution beats 5 alternatives"
Slide 8:  "Here's the MVP — try it yourself"
Slide 9:  "Here's how we'd measure success"
Slide 10: "Here's how we could be wrong"
```

**The story is NOT:** "I had an idea → research agreed → I built it."  
**The story IS:** "We started with a metric → decomposed behaviour → investigated without assuming → evidence changed our hypotheses → primary research narrowed the problem → we found a specific root cause → several solutions were considered → one mechanism won → we built the smallest thing that could test it."
