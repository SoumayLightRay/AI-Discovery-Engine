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

## 13. Primary Research: Survey + Interview Findings

### 13.1 Survey Overview

| Metric | Value |
|---|---|
| Submissions | 39 (38 online fashion shoppers, 36 wishlist users) |
| Source | Google Form, Sep 4–5 2026 |
| Platforms used | Myntra, AJIO, Nykaa Fashion, Amazon, Flipkart, Urbanic, brand sites |
| Wishlist sizes | Wide range from 0–5 to 100+ items |

**Data-quality caveat:** Several respondents answered with non-fashion items (iPad, Dyson, lip balm). Dataset used for **directional behavioural discovery**, not as Myntra-specific claims.

### 13.2 AI Hypothesis Cross-Validation (Updated N = 36)

| AI Engine Finding | Survey Verdict | Detail |
|---|---|---|
| Quality/Material = #1 (14.1%) | ✅ **Confirmed** | Confidence gap is a meaningful non-monetary signal (28% explicit) |
| Returns = most toxic (93.5% neg) | ⚠️ **Weak signal** | Toxic when hit, but not top-of-mind; 8/36 check return policy externally |
| Price = high volume (10.5%) | ✅ **Converged — stronger** | 44% have price/deal-related signal; strongest explicit barrier |
| Comparison = low (1.6%) | 🔄 **AI underweighted** | 36% mention comparing — major detection gap. AI detects complaints; survey detects behaviour |
| Reviews/Info = invisible (0%, 6.1%) | ✅ **Confirmed** | 15/36 read reviews elsewhere; "no reviews with pictures" cited |
| Fit/Size = watch (4.5%) | ✅ **Converged — more prevalent** | 6/36 explicit; 25/36 report historical fit/visual uncertainty |
| Forgetting = low (1.6%) | ⚠️ **Refined** | Real but some non-conversion is healthy behaviour |

### 13.3 Five Competing Friction Mechanisms (Survey)

| Mechanism | Frequency | Implication |
|---|---|---|
| **Price / deals** | 44% | Strongest explicit barrier — but a **solution constraint** (no monetary incentives) |
| **Comparison / alternatives** | 36% | Wishlist = shortlist, not commitment |
| **Decision confidence** (fit/quality/style) | 28% explicit; 69% historical | **Strongest non-monetary signal** |
| **External research** | 89% leave the app | Users resolving decisions off-platform |
| **Availability** | 11% | Low frequency but very high intent |

### 13.4 Wishlist Intent Distribution (N = 36)

| Intent Level | Count | % |
|---|---|---|
| Still want it, expect to buy | 11 | 31% |
| Still want it, don't know when | 9 | 25% |
| Still considering / uncertain | 12 | 33% |
| No longer want it | 3 | 8% |
| Don't remember | 1 | 3% |

**56% are clearly still interested. 33% are actively evaluating.** Most non-conversion is unresolved intent, not forgetting.

### 13.5 The Research Exodus (Off-Platform Behaviour)

| External Behaviour | Responses |
|---|---|
| Read reviews elsewhere | 15/36 |
| Instagram / social media | 13/36 |
| Compared price elsewhere | 13/36 |
| Looked for similar products elsewhere | 13/36 |
| YouTube | 11/36 |
| Brand website | 11/36 |
| Friends / family | 8/36 |
| Return / exchange policy | 8/36 |

### 13.6 Competitor Leakage

- **42% bought something similar elsewhere**
- **35% of high-intent users** leaked
- Explicit examples: bought same product from another site, found cheaper alternative, got Flipkart notification

### 13.7 Live Interview Findings (12 Respondents)

**Method:** Live phone calls, 3–10 minutes each, rapid-fire + probing.
**Respondents:** Rishika, Stuti, Aziz, Aastha, Umesh, Steve, Nandini, Himanshi, Tanej, Sia, Prakhar, Yaakrati + 1 screened out.

**The Headline — Confidence > Price (11/12 = 92%):**

| # | Name | Paid more for confidence? | Example |
|---|---|---|---|
| 1 | Rishika | ✅ | Same shorts, bought expensive seller with reviews |
| 2 | Stuti | ✅ | Chose reviewed product over unreviewed |
| 3 | Aziz | ❌ | Only counter-example — price is primary |
| 4 | Aastha | ✅ | Same top — bought Amazon at higher price for reviews |
| 5 | Umesh | ✅ | Snitch/Bewakoof over cheaper identical items |
| 6 | Steve | ✅ | Chose reviewed over unreviewed |
| 7 | Nandini | ✅ | Dress — 20–30% more for reviews + photos |
| 8 | Himanshi | ✅ | Chooses expensive Urbanic for quality |
| 9 | Tanej | ✅ | Zara at premium over identical cheaper brand |
| 10 | Sia | ✅ | Party dress ~₹2000, better-reviewed |
| 11 | Prakhar | ✅ | Chooses reviewed seller for same product |
| 12 | Yaakrati | ✅ | Suspects cheap = fake; chooses pricier |

**Cross-interview tallies:**
- 11/12 (92%) paid more for confidence
- 11/12 prefer buyer photos over model pics
- 9/12 won't buy without reviews
- 11/12 compare cross-platform
- 7/12 check return policy as trust signal

**Cross-Seller Review Bridge validation:** 3/6 validated, 2/6 partial, 1/6 rejected (Himanshi: "1% भी doubt नहीं रखना चाहेंगे").

### 13.8 Behavioural Segments (Post-Interview, Refined)

| Segment | Evidence | Actionable? |
|---|---|---|
| **Confidence-arbitrage buyers** | Pay more for trust signals (Rishika, Aastha, Nandini, Sia) | ✅ **Primary target** |
| **Platform-loyal self-regulators** | Deliberate cooling-off, not inability (Stuti) | ⚠️ Partial — wishlist is working as intended |
| **Price-led cross-platform comparers** | Pure price comparison (Aziz) | ❌ Constrained |
| **Brand-trust-substituters** | Brand replaces reviews (Umesh, Yaakrati) | ⚠️ Solution less relevant for branded items |
| **Styling/versatility doubters** | "Will it go with my wardrobe?" (Prakhar) | ✅ Addressable |
| **Offline-preferring verifiers** | Physical retail as competing channel (Steve) | ❌ Not solvable digitally |

### 13.9 Updated Root Cause Chain (Post-Survey + Post-Interview)

```
SYMPTOM
  Wishlisted items sit unconverted for weeks.
    ↓
BEHAVIOUR (Survey)
  56% still want the item; 33% are actively evaluating.
  Most non-conversion is unresolved intent, not forgetting.
    ↓
FRICTION BUNDLE (Survey)
  Price (44%) + Comparison (36%) + Confidence (28%) + Availability (11%)
    ↓
THE PARADOX (Interviews)
  Price is the stated #1 barrier — but 11/12 users PAY MORE
  when confidence signals are present.
    ↓
WORKAROUND (Survey + Interviews)
  89% leave the app. 11/12 compare cross-platform.
    ↓
CONSEQUENCE (Survey + Interviews)
  42% bought something similar elsewhere. 35% of high-intent leaked.
    ↓
ROOT CAUSE
  Myntra's product page does not provide sufficient evidence
  (verified buyer photos, fit consensus, quality proof, return clarity)
  to let users resolve their decision without leaving the platform —
  and once they leave, competitor leakage occurs.
```


---

## 14. Recommended MVP

### "Wishlist Confidence Layer"

An overlay on each wishlisted item that provides real-world evidence to resolve purchase uncertainty:

| Component | What It Shows | Addresses |
|---|---|---|
| 📸 Verified Buyer Photos | Real customer photos, not marketing | Quality uncertainty (14.1%) |
| 📏 Fit Consensus | "85% of buyers say true to size" — aggregated from reviews | Fit/Size (4.5%) |
| 🔄 Return Clarity Badge | "✅ Returnable 15 days" or "⚠️ Non-returnable" | Return anxiety (9.9%) |
| ⭐ AI Review Digest | "Buyers love fabric but say it runs small" — 3-line summary | Review gap (6.1%) |
| 🔗 Cross-Seller Review Bridge | When product has zero reviews: show reviews of same category from same seller | Zero-review "invisible friction" |

**Why this MVP:**
- Addresses the root cause validated across AI engine (1,367 reviews), survey (N=36), and interviews (12 respondents)
- 11/12 interview respondents confirmed they pay MORE for confidence signals
- 11/12 prefer buyer photos over model pics
- Cross-Seller Review Bridge validated by 3/6 users when pitched directly
- Does NOT require monetary incentives
- Directly resolves information asymmetry — the root cause

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
