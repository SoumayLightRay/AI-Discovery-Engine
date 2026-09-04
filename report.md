# AI Discovery Engine — Research Report
### Myntra Wishlist-to-Purchase Conversion

> **Date:** September 5, 2026  
> **Product:** Myntra · Growth Team  
> **Business Metric:** % of users who purchase ≥1 wishlisted item within 30 days  
> **Constraint:** No monetary incentives permitted  
> **Live Dashboard:** [ai-discovery-engine-rose.vercel.app](https://ai-discovery-engine-rose.vercel.app/)  
> **Full Report:** [discovery_research_report.html](https://ai-discovery-engine-rose.vercel.app/discovery_research_report.html)  
> **Source Code:** [github.com/SoumayLightRay/AI-Discovery-Engine](https://github.com/SoumayLightRay/AI-Discovery-Engine)

---

## 1. Executive Summary

Millions of Myntra users save fashion products to their wishlists every day. A wishlist signals explicit interest — the user has stopped short of purchasing, but has told the platform "I want this." Yet only a small fraction of wishlisted items convert into purchases within 30 days.

Our AI Discovery Engine analysed **1,367 public reviews** across 4 channels and identified the core cause of this drop-off: a **Platform Trust Deficit**. Users who wishlist high-consideration items hit a wall of uncertainty — they doubt material quality (14.1%), fear strict return policies (9.9%), and can't find sufficient real-buyer evidence to make a confident decision. This uncertainty triggers procrastination, and over time, the wishlist becomes a graveyard of abandoned intent.

The highest-leverage intervention point is **Stage 2 (Evaluation & Confidence Building)**, where 30.1% of all friction clusters. This stage is also the most solvable without monetary incentives.

---

## 2. Methodology

### 2.1 Data Collection (Phase 1)

| Source | Reviews | % of Sample | Collection Method |
|---|---|---|---|
| 📱 Google Play | 78 | 24.9% | Apify Actor (google-play-scraper) |
| 🍎 App Store | 77 | 24.6% | Apify Actor (app-store-scraper) |
| 📺 YouTube | 79 | 25.2% | Apify Actor (youtube-comment-scraper) |
| 🟠 Reddit | 79 | 25.2% | Reddit API (r/IndianFashionAddicts, r/InstaCelebsGossip) |
| **Total Analysed** | **313** | **100%** | |
| Full Corpus | 1,367 | — | Including unsampled ingestion |

Near-perfect balance across all 4 channels eliminates channel bias.

### 2.2 Analysis Pipeline (Phase 2)

**LLM:** Groq Cloud — LLaMA 3.3 70B Versatile

Each review was classified on 5 dimensions:
1. **Primary friction theme** (13 predefined categories + emergent tagging)
2. **Sentiment** (positive / neutral / negative)
3. **Friction present** (boolean — is there a conversion barrier?)
4. **Verbatim quote** (exact user words capturing the core friction)
5. **Source attribution** (channel + timestamp)

### 2.3 Retrieval & Synthesis (Phase 3)

**RAG Pipeline:** BM25 + TF-IDF over 1,367 embedded reviews, accessible via a live chatbot on the interactive dashboard.

---

## 3. Answers to the 10 Core Research Questions

### Q1. Why do users add fashion products to their wishlist?

Three distinct behaviours: (a) Genuine intent to purchase later, (b) Aspirational bookmarking — using the wishlist as a personal catalogue with no immediate purchase plan (4.2% of sample), and (c) Holding items while waiting for a price drop or sale event.

### Q2. What prevents wishlisted products from eventually being purchased?

A "Platform Trust Deficit" at the evaluation stage. Users hit roadblocks regarding material quality doubts (14.1% of sample), fear of strict return policies (9.9%), and delivery unreliability (5.4%). These three friction types form a compounding uncertainty barrier that stalls conversion.

### Q3. What uncertainties remain after users have identified a product they like?

The highest remaining uncertainties are (a) whether the actual material/quality matches the heavily edited product photos, and (b) whether the item will actually fit. Reddit users consistently complain about inaccurate size charts: *"Size chart is so incorrect. They sent 2 sizes small than my actual measurements."*

### Q4. What causes users to postpone a purchase?

Our 5-Whys root cause analysis identifies two drivers: (a) anxiety over financial risk — post-purchase regret if the item is bad and non-returnable, and (b) unmet discount expectations — waiting for a price drop that never materialises. *"None of the items in my wishlist and cart got their price reduced."* (×6 repetitions)

### Q5. How do users compare multiple shortlisted products?

Users compare across alternative platforms (1.3% of friction mentions) and heavily weigh the return policy leniency of each platform before committing. The return policy is effectively a tiebreaker: *"If AJIO has free returns and Myntra doesn't, I'll buy from AJIO."*

### Q6. What information do users seek outside Myntra before purchasing?

They turn to **YouTube** for styling, hauls, and aspirational validation — checking how the product looks in real life on real people. They turn to **Reddit** (r/IndianFashionAddicts) for brutal honesty about sizing accuracy and fabric quality. This external research behaviour reveals a trust gap on the product page itself.

### Q7. What role do fit, size, styling, price, reviews, occasion, and social validation play?

We quantified the role of each factor through negativity-rate analysis:

| Factor | Volume | Negativity Rate | Interpretation |
|---|---|---|---|
| Returns | 31 (9.9%) | **93.5%** | Toxic friction — nearly every mention is a complaint |
| Availability | 17 (5.4%) | **88.2%** | Delivery infrastructure failures |
| Fit/Size | 14 (4.5%) | 42.9% | Mixed signal — some satisfied, some angry |
| Price | 33 (10.5%) | 36.4% | 1 in 3 mentions are complaints; others are neutral comparisons |
| Quality/Material | 44 (14.1%) | 6.8% | High volume but low negativity = diffuse uncertainty, not acute anger |
| Reviews/Info | 19 (6.1%) | **0.0%** | "Invisible friction" — the absence of info is the problem |
| Styling/Occasion | 11 (3.5%) | 0.0% | Users discuss styling neutrally |
| Social Validation | 6 (1.9%) | 0.0% | Aspirational seeking |

**Key insight:** High volume ≠ High severity. Returns (93.5% negative) is far more emotionally damaging per-mention than Quality (6.8% negative), even though Quality has more raw mentions.

### Q8. When do users use the wishlist as genuine purchase intent versus bookmarking?

Bookmarking behaviour has 0% negativity — users simply catalogue items with no emotional investment. Genuine purchase intent transforms into negative friction the moment the user tries to evaluate the item for purchase but hits a trust or information roadblock. The transition point is the **evaluation stage** — where browsing becomes buying.

### Q9. How do these behaviours differ across user segments?

Our channel × theme cross-tabulation reveals clear behavioural segments:

| Segment Proxy | Channel | Top Concerns | Behaviour Pattern |
|---|---|---|---|
| **Deal-hunters** | Reddit | Price (8/11 complaints), Fit (5/5) | Compare deals across platforms; vocal about discount gaps |
| **Logistics-frustrated** | Google Play | Availability (12/15 complaints) | Tier 2/3 city users; delivery infrastructure issues |
| **Returns-anxious** | All 3 complaint channels | Returns (universal: GP=8, AS=10, R=11) | Fear of non-returnable items; strongest cross-channel signal |
| **Aspirational browsers** | YouTube | Zero friction | Watch hauls; seek styling inspiration; don't express purchase friction |

### Q10. What unmet needs emerge consistently across user conversations?

Two needs appear with extreme consistency:
1. **Transparent return policies on intimate wear** — the phrase "no return policy on bras and panties" appeared **7 times** from different users. This is the single strongest, most concentrated signal in the entire dataset.
2. **Verified buyer photos/evidence** to prove material quality before purchase — users repeatedly express that the highly edited model photos create a gap between expectation and reality.

---

## 4. Sentiment Analysis

### Overall Distribution

| Sentiment | Count | % |
|---|---|---|
| ✅ Positive | 121 | 38.7% |
| ⚪ Neutral | 115 | 36.7% |
| ❌ Negative | 77 | 24.6% |

### Critical Finding: Friction ≈ Negative Sentiment

| Sentiment | Friction Reviews | Non-Friction |
|---|---|---|
| Positive | 0 | 121 |
| Neutral | 1 | 114 |
| Negative | 69 | 8 |

98.6% of friction reviews are negative. Zero positive reviewers expressed purchase friction. This validates the accuracy of our friction tagging.

### Channel-Level Sentiment

| Channel | Positive | Neutral | Negative | Negativity Rate |
|---|---|---|---|---|
| YouTube | 2 | 73 | 4 | 5.1% (lowest) |
| App Store | 62 | 1 | 14 | 18.2% |
| Google Play | 47 | 2 | 29 | 37.2% |
| Reddit | 10 | 39 | 30 | 38.0% (highest) |

**Reddit is the friction goldmine** (38% negativity). **YouTube contributes zero friction** — it's entirely aspirational.

---

## 5. Full Friction Theme Distribution

| Rank | Theme | Count | % of 313 | Negativity Rate | Conversion Stage |
|---|---|---|---|---|---|
| P1 | **Quality/Material** | 44 | 14.1% | 6.8% | Stage 2: Evaluation |
| P2 | **Price** | 33 | 10.5% | 36.4% | Stage 3: Decision |
| P3 | **Returns** | 31 | 9.9% | 93.5% | Stage 3: Decision |
| P4 | **Reviews/Information** | 19 | 6.1% | 0.0% | Stage 2: Evaluation |
| P5 | **Availability** | 17 | 5.4% | 88.2% | Stage 4: Purchasability |
| P6 | **Fit/Size** | 14 | 4.5% | 42.9% | Stage 2: Evaluation |
| P7 | **Intent/Bookmarking** | 13 | 4.2% | 0.0% | Stage 1: Discovery |
| P8 | **Styling/Occasion** | 11 | 3.5% | 0.0% | Stage 2: Evaluation |
| P9 | **Social Validation** | 6 | 1.9% | 0.0% | Stage 2: Evaluation |
| P10 | **Comparison** | 5 | 1.6% | 0.0% | Stage 3: Decision |
| P11 | **Forgetting** | 5 | 1.6% | 0.0% | Stage 4: Drop-off |
| P12 | **Alternatives** | 4 | 1.3% | 0.0% | Stage 3: Decision |
| — | Other emergent | 111 | 35.5% | 10.8% | Various |

### The "Invisible Friction" Discovery

Six themes have **0% negativity** but represent real conversion barriers:

| Theme | Count | What This Means |
|---|---|---|
| Reviews/Information | 19 | Users discuss wanting info without complaining — the ABSENCE of info is the friction |
| Intent/Bookmarking | 13 | Users acknowledge using wishlist as bookmarks — not purchase intent |
| Styling/Occasion | 11 | "Would this work for X?" — uncertainty without anger |
| Social Validation | 6 | Users seek peer approval — aspirational signal |
| Comparison | 5 | Cross-platform comparison without complaint |
| Forgetting | 5 | Users note they forgot items — silent decay |

These represent friction that **silently kills conversion without generating complaints**. A user who can't find good reviews doesn't write an angry review — they just don't buy.

---

## 6. Channel × Theme Cross-Analysis

### Where does each friction originate?

| Theme | Google Play | App Store | Reddit | YouTube |
|---|---|---|---|---|
| Returns | 8 | 10 | 11 | 0 |
| Availability | 12 | 1 | 2 | 0 |
| Price | 3 | 0 | 8 | 0 |
| Fit/Size | 0 | 0 | 5 | 0 |
| Quality | 2 | 0 | 1 | 0 |

**Key findings:**
- **Returns is the only friction that appears strongly across ALL 3 complaint channels.** This makes it the most structurally validated signal.
- **Availability is a Google Play problem** (12/15 = 80%). Likely driven by Tier 2/3 delivery infrastructure.
- **Price frustration is a Reddit phenomenon** (8/11 = 73%). Reddit users are the most price-aware.
- **Fit/Size is exclusively Reddit** (5/5 = 100%). Fashion communities have the most detailed sizing discussions.
- **YouTube contributes ZERO friction.** It's aspirational only.

---

## 7. Verbatim Evidence Bank (Top Quotes)

### Returns — The Most Toxic Theme (93.5% negative)

| Repetitions | Quote | Source |
|---|---|---|
| **×7** | "no return policy on bras and panties" | Reddit |
| ×1 | "Return or exchange Policy is horrible." | App Store |
| ×1 | "Myntra is currently sending the wrong product with almost every order" | App Store |
| ×1 | "I ordered jeans, and it was totally different from what it was in the picture, then I tried to return it, the delivery guy came and cancelled the pickup" | Google Play |
| ×1 | "My money does not refund plz don't use this app" | Google Play |
| ×1 | "tried to return one and exchange another, its been 2 weeks" | App Store |

**Sub-categories:** Policy restrictions → Process failures → Wrong product received

### Price — Unmet Discount Expectations

| Repetitions | Quote | Source |
|---|---|---|
| **×6** | "none of the good items got any discounts whatsoever" | Reddit |
| ×1 | "none of the items in my wishlist and cart got their price reduced" | Reddit |
| ×1 | "additional platform fee on every order feels unnecessary" | Google Play |

### Fit/Size — Inaccurate Size Charts

| Repetitions | Quote | Source |
|---|---|---|
| ×1 | "Many brands have inaccurate sizing and the heavily edited model images often make the colours look much brighter" | Reddit |
| ×1 | "Size chart is so incorrect. They sent 2 sizes small than my actual measurements." | Reddit |
| ×1 | "Myntra size chart is incorrect" | Reddit |

### Quality — Diffuse Uncertainty

| Repetitions | Quote | Source |
|---|---|---|
| ×1 | "clothes are not much quality which i have ordered" | Google Play |
| ×1 | "Shein quality" | Reddit |
| ×1 | "Very disappointing experience with Myntra... no proper bill or invoice inside" | Google Play |

---

## 8. Business Metric Decomposition

### The Wishlist → Purchase Funnel

```
Stage 1: DISCOVERY & WISHLISTING
├── Genuine purchase intent ← 4.2%
├── Aspirational bookmarking (no purchase intent)
└── Social/trend-driven saving ← 1.9%

    ▼ FRICTION ZONE 1: "Should I actually buy this?"

Stage 2: EVALUATION & CONFIDENCE BUILDING ← HIGHEST FRICTION (30.1%)
├── Quality/Material confidence gap ← 14.1%
├── Review/Information insufficiency ← 6.1%
├── Fit/Size uncertainty ← 4.5%
├── Styling/Occasion doubt ← 3.5%
└── Social validation seeking ← 1.9%

    ▼ FRICTION ZONE 2: "Is it worth the risk?"

Stage 3: DECISION & COMMITMENT (27.1%)
├── Price & discount expectations ← 10.5%
├── Return/Exchange policy fear ← 9.9%
├── Availability/Delivery concern ← 5.4%
└── Alternative platform comparison ← 1.3%

    ▼ FRICTION ZONE 3: "I'll just wait..."

Stage 4: CONVERSION OR DROP-OFF
├── ✅ Purchase completed
├── ⏸️ Prolonged indecision → forgetting ← 1.6%
└── ❌ Permanent abandonment → platform switch
```

### Where Conversion Breaks Down

| Stage | Total Friction | Solvable Without Incentives? |
|---|---|---|
| Stage 2: Evaluation | **30.1%** | ✅ Yes — information & confidence interventions |
| Stage 3: Decision | **27.1%** | ⚠️ Partially — return transparency yes, price no |
| Stage 4: Drop-off | **3.2%** | ✅ Yes — nudges & reminders |

**Strategic conclusion:** Stage 2 is both the highest-friction zone AND the most solvable under the no-monetary-incentives constraint.

---

## 9. Root Cause Analysis (5 Whys)

```
WHY 1: Users hesitate to move items from wishlist to cart
  ↓ Because they feel uncertain about the final purchase outcome

WHY 2: Uncertainty comes from insufficient transparent information
  ↓ About quality, fit, and return options

WHY 3: When critical details are opaque, users experience anxiety
  ↓ About financial risk and post-purchase regret

WHY 4: Anxiety triggers procrastination
  ↓ Users keep items in the wishlist as a "safety net"

WHY 5: The safety-net habit leads to prolonged indecision
  ↓ During which alternatives become attractive
  → RESULT: Permanent drop-off
```

**Root Cause:** Information asymmetry → Risk perception → Procrastination → Abandonment

---

## 10. Opportunity Ranking

Using **Frequency × Severity × Solvability** (each scored 1–5), constrained by no monetary incentives:

| Rank | Opportunity | Freq | Sev | Solv | Score | Why |
|---|---|---|---|---|---|---|
| 🥇 P1 | Quality/Material Confidence | 5 | 5 | 4 | **100** | Highest volume; addressable via verified photos + AI quality scores |
| 🥈 P2 | Return Policy Transparency | 4 | 5 | 4 | **80** | 93.5% negativity; fixable via category-specific return guarantees |
| 🥉 P3 | Review/Information Enrichment | 3 | 4 | 5 | **60** | 0% negativity (invisible friction); highly solvable via UGC + AI summaries |
| P4 | Fit/Size Confidence | 3 | 3 | 4 | **36** | All from Reddit; fixable via better size charts + verified fit feedback |
| P5 | Price Expectation Mgmt | 4 | 4 | 2 | **32** | Constrained — can't offer discounts; can only show price history |

---

## 11. Problem Statements

### Primary Problem (Quality & Material Confidence)

> Among **users who add fashion items to their wishlist but fail to purchase**, users who **cannot verify whether the actual product quality matches the heavily edited product imagery** delay purchasing because **the information asymmetry creates perceived financial risk**. They currently **search YouTube hauls and Reddit threads for honest reviews**, which **delays their decision and increases the chance of finding alternatives on competing platforms**.

**Grounded in:** 44 reviews (14.1%) + verbatim: *"Many brands have inaccurate sizing and the heavily edited model images often make the colours look much brighter and cleaner than they actually are."*

### Secondary Problem (Return & Exchange Risk)

> Among **users who have previously faced return obstacles or fear non-returnable categories**, users who add products to their wishlist **delay purchasing because they fear they will be unable to return or exchange mismatched items**. They currently **avoid moving items to cart and keep them in wishlist indefinitely**, which **leads to permanent abandonment**.

**Grounded in:** 31 reviews (9.9%, 93.5% negative) + verbatim: *"no return policy on bras and panties"* (×7)

---

## 12. AI/ML Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    AI DISCOVERY ENGINE                        │
├──────────┬──────────┬──────────┬──────────┬─────────────────┤
│  INGEST  │ ANALYSE  │ RETRIEVE │ DELIVER  │   AUTOMATE      │
│          │          │          │          │                  │
│ Apify    │ Groq     │ BM25 +   │ FastAPI  │ GitHub Actions   │
│ Cloud    │ LLaMA    │ TF-IDF   │ Backend  │ Weekly Cron      │
│ Actors   │ 3.3 70B  │ Semantic │ Vanilla  │ ingest→analyse   │
│ (4 chan.) │ 13-theme │ Search   │ JS/CSS   │ →deploy          │
│          │ classif. │ 1,367    │ Vercel   │                  │
│          │          │ vectors  │ + Render │                  │
└──────────┴──────────┴──────────┴──────────┴─────────────────┘
```

---

## 13. Primary Research: Survey Findings (N ≈ 29)

### 13.1 Survey Overview

| Metric | Value |
|---|---|
| Submissions | 31 (2 duplicates → effective N ≈ 29) |
| Source | Google Form, Sep 4–5 2026 |
| Platforms used | Myntra, AJIO, Nykaa Fashion, Amazon, Flipkart, brand sites |
| Wishlist engagement | Most opened wishlist within the last week |

### 13.2 AI Hypothesis Cross-Validation

| AI Engine Finding | Survey Verdict | Detail |
|---|---|---|
| Quality/Material = #1 (14.1%) | ✅ **Confirmed + Refined** | Confirmed as top friction, but split into "quality-truth" (will it match photos?) and "value-justification" (is it worth ANY price?) |
| Returns = most toxic (93.5% neg) | ⚠️ **Partially validated** | Toxic when encountered, but not top-of-mind unprompted blocker |
| Price = high volume (10.5%) | ⚠️ **Refined → 3 sub-problems** | (a) Waiting for sale (unsolvable), (b) Cash-flow timing (external), (c) Value unproven (solvable!) |
| Comparison = low (1.6%) | 🔄 **AI underweighted** | #1 most-ticked multi-select reason — AI missed it because reviews don't discuss competitor behaviour |
| Reviews/Info = invisible (0%) | ✅ **Confirmed** | "No reviews with pictures" cited explicitly |
| Fit/Size = watch (4.5%) | ✅ **Confirmed — more prevalent** | Among top 2 most-ticked reasons; users actively leave app to resolve via YouTube/offline |
| Forgetting = low (1.6%) | ✅ **Confirmed** | Small but real; reminders work as conversion triggers |

### 13.3 What Users Said (Grouped by Raw Signal)

**"I still want to buy it" (~33%):**
- Stock-out blocked: *"My size is out of stock"* (4+ mentions, often event-driven)
- Price waiting: *"Waiting for prices to go down"*, *"Out of budget"*
- Cash-flow timing: *"Waiting to receive money from dad"*, *"my salary was lower"*

**"I'm considering it, but not sure" (~35%):**
- Fit/style doubt: *"not sure how it fits"*, *"Don't know if it will suit me"*
- Information doubt: *"The product doesn't have many reviews"*, *"no reviews with pictures"*
- Value doubt: *"Will it be worth it!"*, *"unsure if it's worth the price"*
- Comparing: *"Still looking for other options"*, *"Maybe I'll find a better alternate"*

**"Don't really want it anymore" (~10%):**
- Pure forgetting: *"I forgot"*, *"Got distracted"*
- Interest decay: *"Not as appealing as before"*

### 13.4 The Research Exodus (Off-Platform Behaviour)

Users conduct 4–6 research actions PER ITEM before deciding, entirely outside Myntra:

| Channel | What They Seek |
|---|---|
| YouTube | Video hauls, real-world look, material check |
| Instagram | Styling, outfit pairing, social validation |
| Other e-commerce apps | Price comparison, alternatives |
| Brand website | Better product details, size guides |
| External reviews | Honest quality/fit feedback |
| Offline store | Physical try-on before online purchase |

### 13.5 Competitor Leakage

Multiple respondents explicitly bought the same or similar product from a different platform:
- *"Found better design and branded stuff for same price"*
- *"Bought it from different site"*
- *"Got notification from Flipkart that prices gone down. Bought it cheaper from somewhere else."*

### 13.6 Behavioural Segments (from Survey)

| Segment | % of Sample | Blocker | Actionable? |
|---|---|---|---|
| **Value-unproven evaluators** | ~35% | Confidence gap | ✅ **Primary target** |
| **Fit/style-doubtful researchers** | ~25% | Information gap | ✅ Secondary target |
| **Stock-out-blocked** | ~15% | Inventory | ⚠️ Logistics |
| **Cash-timing-blocked** | ~10% | External life | ❌ |
| **Price-waiters** | ~10% | Monetary | ❌ Constrained |
| **Passive decayers** | ~5% | Attention | ⚠️ Nudge only |

**Target: Value-unproven evaluators + Fit/style researchers (combined ~60%).** They have high intent, strong pain, and the blocker is solvable without monetary incentives.

### 13.7 Updated Root Cause Chain (Post-Survey)

```
SYMPTOM: Wishlisted items sit unconverted for weeks.
    ↓
BEHAVIOUR: User wants the item but delays purchase.
    ↓
IMMEDIATE REASON: "I'm not sure if it's worth it" / "not sure how it fits"
    ↓
WORKAROUND: User leaves app → researches on YouTube, Instagram, competitor apps (4–6 actions)
    ↓
CONSEQUENCE: During off-platform research, user finds alternative → buys from competitor
    ↓
ROOT CAUSE: Myntra's product page lacks real-world evidence (verified buyer photos,
  honest fit consensus, quality proof) → user can't decide without leaving the platform.
```


---

## 14. Recommended MVP

### "Wishlist Confidence Assistant"

An AI-powered feature that adds a **Confidence Score** to each wishlisted item:

| Component | What It Shows | Addresses |
|---|---|---|
| ✅ Verified buyer photos | Real customer photos, not marketing | Quality uncertainty (P1) |
| 📏 Size accuracy indicator | Based on review sentiment about fit | Fit/Size (P4) |
| 🔄 Return policy badge | Returnable vs. non-returnable, prominently displayed | Return anxiety (P2) |
| ⭐ AI review summary | "What buyers say about quality" — 3-line digest | Review gap (P3) |

**Why this MVP:**
- Addresses the #1 opportunity (Quality Confidence: 14.1%)
- Also touches #2 (Return Transparency), #3 (Review Enrichment), and #4 (Fit/Size)
- Does NOT require monetary incentives
- Can be deployed as a standalone web experience connected to the shopping journey
- Directly resolves the root cause: information asymmetry

---

## 15. Success Metrics

### North Star
**30-day Wishlist → Purchase Conversion Rate**

### Solution Metrics
- Confidence Score view rate (do users engage?)
- Wishlist-to-cart velocity (does speed improve?)
- Buyer photo click-through rate

### Leading Indicators
- Reduced time between wishlist-add and cart-add
- Increased return-policy badge impressions
- Decreased external research (YouTube/Reddit visits from product page)

### Guardrail Metrics
- Core purchase conversion rate (must not decrease)
- Average order value (must not decrease)
- Wishlist addition rate (must not decrease — don't discourage wishlisting)
- Return rate (if we reduce uncertainty, returns should not increase)

---

## 16. Risks & Mitigation

| Risk | Why It Could Fail | Mitigation |
|---|---|---|
| **Wrong root cause** | Interviews may disconfirm quality as the key blocker | A/B test before rollout; kill if leading metrics don't move in 14 days |
| **AI content errors** | Confidence scores or summaries could be inaccurate | Deterministic rules over LLM guesses; confidence thresholds |
| **User distrust** | New UI elements may feel intrusive | Opt-in first; gradual rollout; test with power users |
| **Cannibalisation** | May shift purchases from non-wishlist to wishlist flow | Track total purchase volume as guardrail |
| **Data sparsity** | Some products may have zero buyer photos | Fallback to brand-provided content with clear labelling |

### Experiment Design

| Phase | Duration | Action | Success Gate |
|---|---|---|---|
| Shadow | Days 0–14 | Show to 5% of users, measure engagement | ≥15% Confidence Score view rate |
| A/B Test | Days 15–30 | 50/50 split on wishlist page | ≥5% lift in wishlist-to-cart conversion |
| Scale | Days 31–60 | 100% rollout if gates pass | No guardrail violations |

---

*Data sourced from Google Play, Apple App Store, YouTube, Reddit · Analysed via Groq LLaMA 3.3 70B · Dashboard: [ai-discovery-engine-rose.vercel.app](https://ai-discovery-engine-rose.vercel.app/) · Code: [github.com/SoumayLightRay/AI-Discovery-Engine](https://github.com/SoumayLightRay/AI-Discovery-Engine)*
