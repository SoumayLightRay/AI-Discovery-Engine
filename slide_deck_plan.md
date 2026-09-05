# 10-Slide Deck — Full Text Content (v4 — Final)

> **File:** `NL Myntra` · 10 slides max · No Fellow name · Title = key takeaway
> **Constraints:** Min font 14 (Slides) / 22 (Canva) · < 40 MB · Color-blind-friendly
> **Changes from v3:** Myntra Verified Badge (Level 2), Post-Purchase Confidence Flywheel (Level 3), 3-layer × 8-component architecture, KPI tree decomposition, interview-refined segments, Confidence Gap Paradox framing

---
---

# PHASE A: THE PROBLEM (Slides 1–2)

---

## SLIDE 1

### Title: Myntra's Biggest Untapped Growth Lever — The Wishlist That Never Converts

Millions of Myntra users browse fashion products, save items they like, and add them to their wishlists every day. A wishlist is the strongest purchase-intent signal short of adding to cart — the user has explicitly said "I want this."

Yet only a small fraction of wishlisted items convert into purchases within 30 days. Over time, users accumulate dozens of wishlisted products while only a handful are ever bought.

**The User Problem**
Wishlist users who still want their saved items cannot confidently decide whether to buy because the product page lacks real-world evidence — forcing them off-platform to research, where 42% end up buying from competitors.

**The Business Metric**
Increase the percentage of users who purchase at least one item from their wishlist within 30 days of adding it.

**Why This Matters**
- Wishlisting = high-intent demand already on the platform
- Converting it increases purchase frequency from existing users
- No new user acquisition cost required
- Directly improves monetisation of existing traffic

**Constraint:** No monetary incentives (no discounts, no coupons, no cashback).

**Deliverable links:**
- 🌐 [AI Discovery Engine Dashboard](https://ai-discovery-engine-rose.vercel.app/)
- 📱 [Wishlist Confidence Layer MVP](https://ai-discovery-engine-rose.vercel.app/wishlist_mvp.html)
- 📄 [Full Research Report](https://ai-discovery-engine-rose.vercel.app/discovery_research_report.html)
- 💻 [Source Code (GitHub)](https://github.com/SoumayLightRay/AI-Discovery-Engine)

---

## SLIDE 2

### Title: The Wishlist-to-Purchase Journey Breaks at Stage 2 — Where Users Try to Build Confidence but Can't

**Business Metric Decomposition:**

The North Star metric (30-day wishlist → purchase %) improves only if we change the right user behaviours through the right product outcomes. We decomposed the conversion journey to find exactly where intervention has the highest leverage.

```
NORTH STAR: 30-Day Wishlist → Purchase Conversion %
    │
    ├── [INPUT] Wishlist Addition Rate
    │     └── Healthy — users ARE wishlisting (high-intent signal)
    │
    ├── [STAGE 1] Intent Quality at Wishlisting
    │     ├── Genuine purchase intent — 4.2%
    │     ├── Price-drop waiting — 10.5%
    │     └── Aspirational / social saving — 1.9%
    │
    ├── [STAGE 2] Decision Confidence Rate  ← 30.1% FRICTION HERE
    │     ├── Quality/Material doubt — 14.1%
    │     ├── Reviews/Info gap — 6.1%
    │     ├── Fit/Size uncertainty — 4.5%
    │     ├── Styling doubt — 3.5%
    │     └── Social validation — 1.9%
    │
    ├── [STAGE 3] Commitment Rate ← 27.1% friction
    │     ├── Price expectations — 10.5% (CONSTRAINED: no incentives)
    │     ├── Return anxiety — 9.9% (93.5% negativity)
    │     ├── Availability — 5.4%
    │     └── Platform comparison — 1.6% + 1.3% = 2.9% (AI underdetected: actual 36% from survey)
    │
    └── [STAGE 4] Conversion / Drop-off ← 3.2%
          └── Forgetting, distraction, permanent abandonment
```

**What needs to change — User Behaviours × Product Outcomes:**

For the metric to improve, specific user behaviours need to shift. Each requires a corresponding product outcome (Myntra-controlled lever):

| User Behaviour That Needs to Change | Product Outcome (Myntra Lever) | Stage | AI Engine Evidence |
|---|---|---|---|
| Users leave the app to check reviews elsewhere | Bring trusted review signals onto the wishlist page | Stage 2 | Reviews/Info = 6.1%, 0.0% negativity (invisible friction) |
| Users don't trust model photos | Surface real buyer photos at point of decision | Stage 2 | Quality = 14.1%, 6.8% negativity (diffuse doubt) |
| Users can't determine fit without ordering | Provide brand-level sizing intelligence | Stage 2 | Fit/Size = 4.5%, 42.9% negativity, Reddit-only |
| Users compare across Amazon/AJIO for confidence | Make Myntra the most trusted information source | Stage 2+3 | Comparison = 2.9% AI, but 36% survey (detection gap) |
| Users fear returns if product doesn't match | Make return policy visible and clear upfront | Stage 3 | Returns = 9.9%, **93.5% negativity** (toxic) |
| Users abandon zero-review products entirely | Provide alternative trust signals for new products | Stage 2 | Zero-review = undetectable in AI data (no reviews = no complaints) |

**Current intent status (Survey, N=36):** 56% still want the item, 33% actively evaluating, only 8% abandoned entirely. Most non-conversion is unresolved intent, not lost interest.

**Metric Decomposition × AI Engine — Where Is the Highest-Potential Opportunity?**

| Stage | Total Friction | Solvable Under Constraint? | AI Engine Signal | Opportunity |
|---|---|---|---|---|
| Stage 1 (Intent) | — | N/A (input quality) | 4.2% genuine intent | Low — can't change WHY users wishlist |
| **Stage 2 (Confidence)** | **30.1%** | **✅ YES — no monetary incentives needed** | Quality 14.1%, Reviews 6.1%, Fit 4.5% | **🎯 HIGHEST — largest friction, most solvable** |
| Stage 3 (Commitment) | 27.1% | ❌ Partially — price (10.5%) is constrained | Returns 9.9% partially solvable | Medium — limited by no-incentives rule |
| Stage 4 (Drop-off) | 3.2% | ⚠️ Minimal | Forgetting 1.6% | Low — small volume |

**Conclusion:** Stage 2 (Decision Confidence) has the highest friction (30.1%), is entirely solvable without monetary incentives, and maps directly to the AI engine's top themes (Quality + Reviews + Fit = 24.7% of all friction). This is where the product intervention should focus.

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
1,367 ingested 5-dimension tags     313 vectors       Interactive UI
```

**Data Sources (Balanced Sampling — no channel bias)**

| Channel | N | % | Primary Signal |
|---|---|---|
| Google Play | 78 | 24.9% | Delivery, returns, quality |
| App Store | 77 | 24.6% | Returns, wrong products |
| YouTube | 79 | 25.2% | Aspirational, styling |
| Reddit | 79 | 25.2% | Price, fit, honest reviews |
| **Total Analysed** | **313** | | **70 friction-tagged (22.4%)** |
| Full Corpus (ingested) | 1,367 | | Including unsampled reviews |

**Critical framing:** These 12 friction themes are hypotheses that require human validation. The engine assists research — it does not replace the PM's thinking.

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
| Fit/Size | 4.5% | 42.9% | All from Reddit — users research sizing externally |

**The Analytical Breakthrough:**
High volume ≠ High severity. Returns (93.5% negative) is emotionally devastating per-mention, but Quality (6.8% negative) affects more users because it represents diffuse, silent uncertainty. Themes with 0% negativity (Reviews, Styling, Comparison) are "invisible friction" — they prevent conversion without generating complaints.

**Channel Cross-Tab:**
- Returns = universal (all 3 complaint channels)
- Price = Reddit-specific (73%)
- Availability = Google Play-specific (80% — Tier 2/3 delivery)
- YouTube = zero friction — purely aspirational

**Repeat Signals:**
- "No return policy on bras and panties" — **7 repetitions**
- "None of the good items got any discounts" — **6 repetitions**

---
---

# PHASE C: THE VALIDATION (Slides 5–6)

---

## SLIDE 5

### Title: Price is the #1 Stated Barrier — But 11/12 Users Pay MORE When Confidence Signals Are Present

**How Our Thinking Evolved:**
Before research, we hypothesised Quality (14.1%) and Price (10.5%) were the dominant standalone blockers. Three rounds of primary research changed this:

**Survey (N = 36 wishlist users, from 39 responses) revealed five competing mechanisms:**

| Mechanism | Frequency | Implication |
|---|---|---|
| **Price / deals** | 44% | Strongest explicit barrier — but a **solution constraint**, not solution space |
| **Comparison / alternatives** | 36% | Wishlist = shortlist, not commitment. AI scored this at only 2.9% combined (Comparison 1.6% + Alternatives 1.3%) — a major detection gap |
| **Decision confidence** (fit/quality/style) | 28% explicit; 69% historical | **Strongest non-monetary signal** — the actionable opportunity |
| **External research** | 89% leave the app | Users are resolving decisions off-platform → competitor leakage |
| **Availability** | 11% | Low frequency but very high intent |

**The honest framing:** Price IS the biggest barrier. We don't pretend otherwise. But under the no-incentives constraint, decision confidence is the largest *solvable* friction. 42% of users bought something similar elsewhere — Myntra captures intent but loses control of the decision journey.

**25/36 wishlist users report having experienced visual/fit uncertainty as a reason for abandoning a fashion purchase at some point** (Q15, lifetime question).

**Live Interviews (12 respondents) — The "Confidence > Price" Pattern:**
11 out of 12 respondents described paying MORE for an item because the confidence signals were stronger:

| User | What Happened | Key Quote |
|---|---|---|
| Rishika (F23) | Two sellers, same shorts — bought the expensive one with reviews | *"Surety that it had to be the same"* |
| Aastha (F) | Same top — bought from Amazon at higher price because better reviews | *"It did have good reviews, so I got it from Amazon"* |
| Nandini (F) | Dress — paid 20–30% more for good reviews + buyer photos | *"Yes, absolutely"* |
| Umesh (M) | Pays more for Snitch over cheaper identical items on Amazon | *"I'm willing to pay more"* |
| Sia (F) | Party dress ~₹2000, chose better-reviewed option over cheaper | *"It was better reviewed, so I bought that"* |
| Tanej (M) | Zara sweatshirt at premium over identical cheaper brand | *"I purchased from Zara because of Zara"* |

**The 1 counter-example (Aziz, M):** Price is primary — has never paid more for reviews. He is a price-led cross-platform comparer. This is honest counter-evidence, not a flaw.

**Cross-interview tallies (all 12):**
- 11/12 (92%) paid more for confidence | 11/12 prefer buyer photos over model pics | 9/12 won't buy without reviews | 11/12 compare cross-platform

**Why users saved items to their wishlist (from 12 interviews):**
- "I liked it but I wasn't sure about the quality" — Rishika (Int 1)
- "Waiting for a price drop" — Stuti (Int 2), Aziz (Int 3)
- "I was comparing with similar items" — Aastha (Int 4), Nandini (Int 7)
- "I liked the style but wasn't sure it would suit me" — Prakhar (Int 11)
- "I save everything I like, then decide later" — Sia (Int 10), Himanshi (Int 8)

**What would make them purchase (unprompted answers from interviews):**
- Real buyer photos showing actual product — 11/12
- Enough reviews with detail about fit/quality — 9/12
- Confidence that product matches the listing — 11/12 ("Surety" — Rishika)
- Clear return policy upfront — 7/12
- Myntra quality check / verification — Tanej (Int 9): "quality check को pass कर रहे हैं, उसको label लगा दे"

**What information they still need before buying:**
- Real photos (not model shots) — 11/12
- Size/fit accuracy for specific brand — 9/12
- Other buyers' honest opinions — 9/12
- Return policy clarity — 7/12
- Whether the product is genuine — Nandini: checks if images are copied across platforms

**How users currently overcome uncertainty (existing workarounds):**
- Leave the app to check Amazon/AJIO/Flipkart reviews — 11/12
- Check YouTube videos for real product footage — 11/36 (survey)
- Check Instagram for styling inspiration — 13/36 (survey)
- Visit brand website directly — 11/36
- Order and return if wrong (costly fallback) — Yaakrati: "order kar leti hu, return kr dungi"
- Rely on brand trust as a proxy (Aziz, Umesh) — avoids research entirely

**The Confidence Gap Paradox:** We expected price to be the villain — and it IS the largest stated barrier (44%). But 11/12 interview users literally pay MORE for trust. Price is the socially acceptable excuse; confidence is the actual decision lever. Solving the confidence gap requires NO monetary incentives — which is exactly our constraint. The root cause for the solvable segment is information asymmetry, not price sensitivity.

---

## SLIDE 6

### Title: 56% of Wishlisted Intent Is Unresolved — and 89% of Users Leave the App to Try to Resolve It

**The Wishlist Is a Decision Workspace, Not a Purchase Queue**

Among 36 wishlist users, current intent toward their most recent wishlisted item:

| Intent | Count | % |
|---|---|---|
| Still want it, expect to buy | 11 | 31% |
| Still want it, don't know when | 9 | 25% |
| Still considering / uncertain | 12 | 33% |
| No longer want it | 3 | 8% |

**56% are still interested. 33% are actively evaluating.** Most non-conversion is unresolved intent, not forgetting.

**Behavioural Segments (derived from behaviour, not demographics — refined by 12 live interviews)**

| Segment | Survey % | Interview Refinement | Actionable? |
|---|---|---|---|
| **Confidence-arbitrage buyers** | ~28% explicit | 11/12 pay MORE for trust signals (Rishika, Aastha, Nandini, Sia, Umesh, Tanej) | ✅ **Primary target** |
| **Price-blocked** | ~44% | Stuti: self-regulation, not inability. But still overridden by confidence | ❌ **Constrained** (no-incentives rule) |
| **Comparison-stalled** | ~36% | 11/12 compare cross-platform — for price AND reviews, not just price | ✅ Partially addressable |
| **Brand-trust-substituters** | — | Aziz, Umesh, Yaakrati: brand replaces reviews | ⚠️ Solution less relevant |
| **Styling/versatility doubters** | — | Prakhar: "Will it go with my wardrobe?" — distinct mechanism | ✅ Addressable |
| Stock-out-blocked | ~11% | Yaakrati: boots went unavailable while comparing | ⚠️ Logistics |
| Passive decayers | Small | Prakhar: procrastination loop (20–30 day revisits) | ⚠️ Nudge only |

**Segment Selection:** Decision confidence is the **strongest non-monetary signal** (28% explicit, 69% historical). Price is honestly the largest barrier — but 11/12 interview respondents pay MORE when confidence signals are present. Price is a constraint, not solution space.

**89% of Users Leave the App — Here's Why:**

| What they're resolving | Where they go | Responses |
|---|---|---|
| "Is this actually good?" | Reviews elsewhere | 15/36 |
| "Is there something better?" | Similar products elsewhere | 13/36 |
| "Is this worth the price?" | Price comparison | 13/36 |
| "Will this look good?" | Instagram / social media | 13/36 |
| "Can I see it in real life?" | YouTube | 11/36 |
| "What does the brand say?" | Brand website | 11/36 |
| "Can I return it?" | Return policy | 8/36 |

**Root Cause — 5 Whys (with interview evidence)**

Why 1: Users hesitate to move wishlisted items to cart.
→ Because they feel uncertain about the purchase outcome.
*Evidence: 56% still want the item; Prakhar (Int 11) revisits every 20–30 days without resolving.*

Why 2: Why uncertain?
→ The product page doesn't give them enough real evidence to decide.
*Evidence: Aastha (Int 4): "Model pics से बिल्कुल ही अलग आता है." Steve (Int 6): "They never look exactly the way shown in the picture."*

Why 3: Why is the evidence insufficient?
→ Model photos are heavily edited, size charts are inconsistent, and no verified buyer photos exist. Some products have ZERO reviews.
*Evidence: 9/12 won't buy without reviews. Himanshi (Int 8): "ये तो देखना ही पड़ता है." Tanej (Int 9): "बिना reviews को confirm नहीं होता."*

Why 4: Why don't they just order and return if wrong?
→ Return process is stressful and unreliable (93.5% negativity in AI data).
*Evidence: Prakhar (Int 11): "That's like lots of hassle, like time." Counter: Yaakrati (Int 12) uses return as safety net.*

Why 5: So what do they do?
→ Leave the app to compare the same product's reviews on Amazon/AJIO/Flipkart. During that cross-platform comparison, they find better deals or more trusted listings and buy from the competitor.
*Evidence: 11/12 compare cross-platform. Aastha: bought same top from Amazon at HIGHER price for reviews.*

**Root Cause (The Confidence Gap Paradox):** Myntra captures purchase intent at the wishlist stage but loses control of the decision-making journey. Users compare CONFIDENCE LEVELS across platforms, not just prices — 11/12 pay MORE for trust. The information asymmetry on the product page forces comparison-shopping, creating competitor leakage. Price is the stated barrier; confidence is the actual lever.

**Target Segment:** Confidence-arbitrage buyers — users who have genuine purchase intent but cannot resolve uncertainty on-platform. ~28% explicit (survey), but 11/12 interview respondents exhibit this behaviour.

**Product Outcome We Intend to Influence:** Increase the rate at which wishlisted items move to cart by providing sufficient confidence signals on the wishlist page, eliminating the need for cross-platform research.

**Existing User Workarounds (and why they fail):**
- Leave Myntra to check reviews on Amazon/AJIO → 42% buy from competitor during this process (leakage)
- Check YouTube for real footage → time-consuming, not product-specific
- Rely on brand trust as proxy → only works for known brands (Aziz, Umesh); fails for unbranded/new sellers
- Order and return if wrong → stressful (93.5% negativity), Prakhar: "lots of hassle, like time"

**Why Solving This Creates User Value:** Users WANT to buy from Myntra — 56% still want the item. They're not leaving because they don't want the product. They're leaving because they can't TRUST the product information. Giving them verified confidence signals saves time (no cross-platform research), reduces return hassle, and helps them make better purchase decisions.

**Why Solving This Makes Business Sense:** Every user who leaves to compare on Amazon is a potential lost sale (42% leakage rate). Converting even a fraction of the 30.1% Stage 2 friction into purchases = material revenue uplift from existing traffic, with zero acquisition cost.

**How Our Thinking Evolved (the full chain):**
```
BUSINESS METRIC: 30-day wishlist → purchase conversion
    ↓
PRODUCT OUTCOMES: Decomposed into 4 conversion stages — Stage 2 = 30.1% friction
    ↓
AI DISCOVERY: Engine identified Quality (14.1%), Reviews (6.1%), Fit (4.5%) as top themes
    → BUT: Price appeared largest. Were we wrong about confidence?
    ↓
PRIMARY RESEARCH (Survey N=36): Price IS #1 (44%). But confidence = 28% explicit, 69% historical.
    → AI underdetected comparison (2.9% vs. actual 36%). 89% leave the app.
    ↓
PRIMARY RESEARCH (12 Interviews): The Confidence Gap Paradox discovered.
    → 11/12 pay MORE for confidence. Price is the excuse; trust is the lever.
    ↓
PROBLEM DEFINITION: Information asymmetry on the product page forces comparison-shopping,
    creating competitor leakage. Solvable WITHOUT monetary incentives.
```

**Emergent Insights from Live Interviews (12 respondents):**

1. **"Confidence Arbitrage"** — Users compare CONFIDENCE LEVELS across platforms, not just prices. Rishika (Int 1): bought MORE expensive shorts because that seller had reviews. Aastha (Int 4): bought same top from Amazon at higher price for better reviews.

2. **Return policy ≠ confidence solution** — Prakhar (Int 11): "That's like lots of hassle, like time." Users want confidence BEFORE buying, not the safety net of returns after.

3. **Brand trust can substitute for reviews** — Aziz (Int 3), Umesh (Int 5), Yaakrati (Int 12): If they trust the brand, reviews become optional. Solution must differentiate branded vs. unbranded.

4. **Styling/versatility is a distinct confidence type** — Prakhar (Int 11): "Will this go with my wardrobe?" Not fit, not quality — compatibility with existing clothes.

5. **Cross-Seller Review Bridge — validated but not universal** — Stuti, Nandini, Sia validated; Himanshi rejected: "1% भी doubt नहीं रखना चाहेंगे."

6. **Model pics are NOT trusted** — Aastha (Int 4): "Model pics से बिल्कुल ही अलग आता है." Steve (Int 6): "They never look exactly the way shown in the picture."

**Competitor Leakage Evidence (Survey + Interviews):**
- Survey: **42% bought something similar elsewhere**; **35% of high-intent users** leaked
- Rishika (Int 1): compares same product on Amazon
- Aastha (Int 4): bought same top from Amazon at higher price for reviews
- Nandini (Int 7): checks if product images are real or copied across platforms
- Yaakrati (Int 12): boots went out of stock while she was comparing — direct lost sale
- 11/12 interview respondents compare cross-platform

---
---

# PHASE D: THE SOLUTION (Slides 7–8)

---

## SLIDE 7

### Title: We Evaluated 6 Mechanisms — "Myntra Verified Confidence Layer" Wins on RICE and All 3 Creativity Levels

**How Might We** reduce the confidence gap on the wishlist page so that users can resolve their purchase decision without leaving to compare on Amazon, AJIO, or Instagram?

**Competitive Landscape (what already exists):**
- Myntra: MyFashionGPT, My Stylist, Mix & Match, Myntra Studio (influencer content)
- Amazon: AR Virtual Try-On (footwear, apparel), AI Shopping Guides, "customers say true to size"
- AJIO: Style Quiz, curated collections
- Flipkart: Flipkart Assured (delivery reliability, not quality verification)
- Meesho: Seller ratings (generic star rating, not quality-specific)

**6 Genuinely Different Mechanisms Evaluated:**

| # | Mechanism | Type |
|---|---|---|
| 1 | **Myntra Verified Confidence Layer** (buyer photos + Myntra Verified Badge + cross-seller review bridge + brand size intelligence + smart compare + post-purchase flywheel) | Platform-verified trust system |
| 2 | Moodboard / Pinterest-style Fashion Board | Inspiration tool |
| 3 | Virtual Try-On (AR superimpose) | Fit resolution |
| 4 | Smart Price Alert | Timing/nudge |
| 5 | Wishlist Reminder Notifications | Re-engagement |
| 6 | Influencer Social Proof | Social validation |

**RICE Prioritisation**

| # | Mechanism | Reach | Impact | Confidence | Effort | RICE | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | **Confidence Layer** | 60% (target segment) | High — directly resolves root cause | High — validated by AI + survey + 12 interviews | Medium | **90** | ✅ **WINNER** |
| 2 | Moodboard | 35% | Medium | Low | High | 25 | ❌ Myntra already has MyFashionGPT + Mix & Match |
| 3 | Virtual Try-On | 25% | High | Medium | Very High | 20 | ❌ Amazon already has AR try-on natively |
| 4 | Price Alert | 10% | Low | Medium | Low | 15 | ❌ Violates no-incentives constraint |
| 5 | Reminders | 5% | Low | Medium | Low | 10 | ❌ Every app does this — no differentiation |
| 6 | Influencer Proof | 20% | Low | Low | Medium | 18 | ❌ Myntra Studio already exists |

**Three-Level Creativity Test**

| Level | Test | Myntra Verified Confidence Layer |
|---|---|---|
| **1. Problem Fit** | Does it solve the validated root cause? | ✅ Provides the exact confidence signals users currently leave the app to find. 8 components addressing every friction mechanism from interviews. |
| **2. Differentiation** | Is it different from what exists? | ✅ **Myntra Verified Badge** — no fashion platform physically verifies product quality/fit and publishes results as a buyer-facing confidence signal. Amazon's Choice is delivery reliability. Flipkart Assured is authenticity. Neither is quality/fit verification. |
| **3. Defensibility** | Why is it hard to copy? | ✅ **Three moats:** (a) Post-Purchase Confidence Flywheel builds proprietary Brand Trust Index (photo accuracy rates, size intelligence) that compounds with every purchase. (b) Myntra Verified requires physical operations infrastructure. (c) Cross-Seller Review Bridge creates seller-product-review graph. Competitor needs Myntra's purchase data + warehouse operations + time to replicate. |

---

## SLIDE 8

### Title: Myntra Verified Confidence Layer — A Three-Layer Trust System That Gets Smarter With Every Purchase

**The Confidence Stack: 3 Layers, 8 Components**

**Layer 1 — User-Generated Trust (Baseline):**

| Component | What It Shows | Evidence |
|---|---|---|
| 📸 **Verified Buyer Photos** | Real customer photos surfaced ON the wishlist card | 11/12 prefer buyer photos; Aastha: "model pics से बिल्कुल ही अलग" |
| ⭐ **Top Reviews on Wishlist** | Most helpful reviews pulled directly onto wishlist — no need to navigate to product page | 9/12 won't buy without reviews; Tanej: "बिना reviews को confirm नहीं होता" |
| 🔄 **Return Clarity Badge** | "✅ Easy Return 15 days" or "⚠️ Non-returnable" — prominent, not buried | 7/12 check return policy; Aastha: no-return = "suspicious" |

**Layer 2 — Platform-Verified Trust (Differentiated — no competitor does this):**

| Component | What It Shows | Evidence |
|---|---|---|
| 🏅 **Myntra Verified Badge** | Myntra independently verifies quality, fit, photos — for zero-review AND reviewed products. Actual measurements, in-house photography, quality grade. | Tanej: "quality check को pass कर रहे हैं, उसको label लगा दे." Solves Himanshi's zero-tolerance too. |
| 🔗 **Cross-Seller Review Bridge** | Zero-review products → seller's other product reviews + seller trust score. Fallback for newer sellers. | 3/6 validated (Stuti, Nandini, Sia). 1/6 rejected (Himanshi). Honest limitation acknowledged. |
| 🔀 **Smart Compare** | Side-by-side comparison of 2-3 wishlisted items with all confidence signals | 3 users asked unprompted; Himanshi: "सब कुछ वहीं आ जाए" |

**Layer 3 — Data-Compounding Trust (Defensible moat — gets better over time):**

| Component | What It Shows | Evidence |
|---|---|---|
| 📏 **Brand-Level Size Intelligence** | "Roadster runs 1 size small based on 2,300 Myntra buyers" — not generic size chart, Myntra-specific | Tanej: XL vs XXL confusion. Post-purchase data creates proprietary asset. |
| 🔁 **Post-Purchase Confidence Flywheel** | After delivery: "Match photos? Size accurate? Quality?" → feeds Brand Trust Index per brand/seller | Creates: Photo Accuracy Rate ("92% match"), Size Intelligence, Seller Trust Score. Compounds with every purchase. |

**How They Work Together:**

```
PRODUCT HAS REVIEWS:
  → Buyer Photos + Top Reviews + Brand Size Intelligence
    + Return Badge + Brand Trust Index (from flywheel)
  → "Real photos look good, runs true to size, easy return. Buying."

PRODUCT HAS ZERO REVIEWS:
  → Myntra Verified Badge + Cross-Seller Review Bridge
    + Return Badge + Seller Trust Score
  → "Myntra verified this AND seller's other products rated 4.3★. Buying."

USER COMPARING ITEMS:
  → Smart Compare with all confidence signals side-by-side
  → "Item A: 94% photo match. Item B: unverified. Going with A."
```

**User Flow (3 steps)**
1. Open wishlist → see Confidence Layer on each item (buyer photos, reviews, badges, brand trust)
2. Tap compare → side-by-side view with all confidence data
3. Decision resolved on-platform → move to cart WITHOUT opening Amazon or AJIO

**Architecture**
```
Myntra Reviews DB + Seller Graph + Purchase/Return Data
    → AI Summariser + Quality Verification Pipeline
    → Brand Trust Index API + Myntra Verified Certification
    → Wishlist Confidence Layer UI
    → Post-Purchase Survey → feeds back into Brand Trust Index (FLYWHEEL)
```

**MVP proves the mechanism:** Can surfacing platform-verified confidence signals at the point of decision change user behaviour from "leave app to compare" to "buy here now"?

**Live MVP →** [ai-discovery-engine-rose.vercel.app/wishlist_mvp.html](https://ai-discovery-engine-rose.vercel.app/wishlist_mvp.html)

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
  • Myntra Verified Badge influence (conversion on verified vs. unverified items)
  • Cross-Seller Review Bridge engagement (for zero-review products)
  • Smart Compare usage rate
  • Post-Purchase Flywheel response rate (% answering micro-survey)
  • Reduced time: wishlist-add → cart-add
  • Decreased cross-platform exits
    ↓
LAGGING INDICATORS (does behaviour persist?)
  • 7-day repeat conversion rate
  • Brand Trust Index coverage (% of products with confidence data)
  • Wishlist-to-cart velocity trend over 30 days
    ↓
GUARDRAILS (must NOT worsen — kill feature if they do)
  • Core purchase conversion rate
  • Average order value
  • Wishlist addition rate (don't discourage wishlisting)
  • Return rate (better info should reduce returns, not increase them)
```

**Metric Definitions & Rationale:**

| Metric | Definition | Why We Chose It |
|---|---|---|
| **North Star: 30-day WL→Purchase %** | % of users who purchase ≥1 wishlisted item within 30 days of adding | Directly measures the business goal. 30-day window captures realistic decision cycles from our survey data. |
| **Solution Metric: CL view → cart %** | % of users who view the Confidence Layer on a wishlisted item and add it to cart | Isolates the causal mechanism — did the confidence signals actually drive the cart action? |
| **CL View Rate** | % of wishlist page visits where ≥1 Confidence Layer is expanded/viewed | If users don't see the confidence signals, they can't be influenced. Minimum adoption threshold. |
| **Buyer Photo CTR** | % of CL views that result in clicking a buyer photo | Buyer photos are the #1 requested signal (11/12). Click = engagement with the core trust signal. |
| **Myntra Verified influence** | Conversion rate on Verified items vs. non-Verified items (same category) | Tests whether platform-level verification (Layer 2) has incremental impact over user-generated signals. |
| **Cross-Seller Bridge engagement** | % of zero-review products where Bridge is viewed AND user proceeds to cart | Measures whether the Bridge solves the zero-review problem specifically. Limited validation (3/6). |
| **Smart Compare usage** | % of users with ≥2 wishlisted items who use the compare feature | Tests whether comparison friction (36% survey) is resolved on-platform. |
| **Flywheel response rate** | % of post-delivery users who complete the micro-survey | Determines whether the data flywheel is sustainable. Target ≥20%. |
| **Time: WL-add → cart-add** | Median hours between wishlisting and adding to cart | If confidence signals work, decision time should decrease. |
| **Cross-platform exit rate** | % of wishlist sessions where user leaves Myntra within 5 min | Measures whether the root behaviour ("leave to compare") is reduced. |
| **7-day repeat conversion** | % of users who convert a 2nd wishlisted item within 7 days of the 1st | Tests whether confidence-driven purchasing becomes habitual. |
| **Brand Trust Index coverage** | % of top-1000 wishlisted products with confidence data from flywheel | Measures data moat growth over time. |

**Guardrail Definitions:**

| Guardrail | Definition | Why It Matters |
|---|---|---|
| **Core purchase conversion** | Overall purchase conversion rate (not just wishlist) | Ensure we don't break the main funnel while optimising a sub-funnel |
| **Average order value** | Mean ₹ per order | Confidence signals shouldn't push users toward cheaper items |
| **Wishlist addition rate** | # of items wishlisted per user per week | More info upfront might discourage "save for later" — this must NOT drop |
| **Return rate** | % of orders returned within 15 days | Better info should REDUCE returns. If it increases them, the signals are misleading |

**Kill Criteria:** If leading indicators don't move within 14 days of A/B test launch, we stop the experiment and investigate.

---

## SLIDE 10

### Title: Here's How We Could Be Wrong — and the 60-Day Experiment to Find Out

**Top Risks**

| Risk | Why It Could Fail | Mitigation |
|---|---|---|
| **Wrong root cause** | Confidence may not be the real blocker at scale (survey N = 36). Price is 44% — confidence is 28% explicit | A/B test with kill switch at Day 14; measure behaviour, not self-report. Counter-evidence (Aziz = price-led) acknowledged |
| **Myntra Verified operational cost** | Physical quality verification doesn't scale to all products | Start with top-wishlisted zero-review products only (highest ROI). Expand based on conversion lift |
| **Post-Purchase Flywheel low adoption** | Users may not answer micro-survey after delivery | 10-second survey, in-app nudge, gamify ("help future buyers"). Target ≥20% response rate |
| **Cross-Seller Bridge rejection** | Himanshi rejected it; Tanej: seller self-reviews not trusted | Position as FALLBACK for zero-review only, not primary signal. Myntra Verified Badge is the primary trust for zero-review products |
| **AI summary errors** | Review digests could be misleading | Deterministic rules > LLM guesses; confidence thresholds; human review queue |
| **Info reduces intent** | More information sometimes kills a purchase (survey evidence) | Monitor Confidence Layer views → cart removal correlation |
| **Cannibalisation** | May shift purchases to wishlist flow without net new sales | Track total purchase volume as guardrail |

**60-Day Experiment Plan**

| Phase | Days | Action | Success Gate |
|---|---|---|---|
| Shadow | 0–14 | Show to 5% of users, engagement only | ≥15% view rate |
| A/B Test | 15–30 | 50/50 split on wishlist page | ≥5% conversion lift |
| Scale | 31–60 | 100% if gates pass | No guardrail violations |

**Beyond MVP**
- **Phase 2:** Expand Myntra Verified to top 1,000 wishlisted products; scale Post-Purchase Flywheel to all categories
- **Phase 3:** Personalised confidence — learn which trust layer matters most per user (some need photos, others need size data)
- **Long-term:** Proprietary Brand Trust Index across all sellers × products × categories — a compounding data moat that makes Myntra the most trusted fashion platform

---
---

# AUDIT CHECKLIST (v4 — Final)

**project.md Part Mapping (all 8 required sections covered):**

| project.md Requirement | Slide | Status |
|---|---|---|
| 1. Business metric decomposition | Slide 2 | ✅ |
| 2. Discovery engine findings | Slides 3–4 | ✅ |
| 3. Primary research | Slides 5–6 | ✅ |
| 4. Problem definition | Slide 6 (root cause chain) | ✅ |
| 5. Solution rationale | Slide 7 (RICE + 3-Level Test) | ✅ |
| 6. MVP | Slide 8 (3-layer Confidence Layer) | ✅ |
| 7. Success metrics | Slide 9 | ✅ |
| 8. Risks and mitigation | Slide 10 | ✅ |

**Arindam Feedback Compliance:**

| Requirement | Source | Status |
|---|---|---|
| RICE framework | framework.md Phase 7 | ✅ Slide 7 — with competitive rejections |
| 3-Level Creativity Test (L1+L2+L3) | arindam_feedback | ✅ Slide 7 — Myntra Verified = L2, Flywheel = L3 |
| "How Might We" statement | framework.md Phase 7 | ✅ Slide 7 |
| 5 Whys root cause with evidence | framework.md Phase 5 | ✅ Slide 6 — real quotes at every level |
| Behavioural segments (not demographics) | arindam_feedback Rule 1 | ✅ Slide 6 — interview-refined |
| AI findings as hypotheses, not conclusions | arindam_feedback | ✅ Slide 3 |
| Disconfirmation / evidence changed thinking | framework.md core philosophy | ✅ Slide 5 — Confidence Gap Paradox |
| "How thinking evolved" narrative | project.md Part 4 | ✅ Slide 5 — AI→Survey→Interview arc |
| Competitive analysis in rejections | 3-Level Test Level 2 | ✅ Slide 7 — Myntra/Amazon/AJIO/Flipkart/Meesho |
| Counter-evidence presented honestly | Anti-assumption mandate | ✅ Slide 5 (Aziz), Slide 8 (Himanshi) |

**Deliverable Links:**

| Link | Where Referenced | Status |
|---|---|---|
| AI Discovery Engine | Slides 1, 3 | ✅ |
| Deployed MVP | Slides 1, 8 | ✅ |
| Research Report | Slide 1 | ✅ |
| GitHub Source Code | Slide 1 | ✅ |

**Deck Constraints:**

| Constraint | Status |
|---|---|
| No Fellow name | ✅ |
| 10 slides max | ✅ (exactly 10) |
| Title = key takeaway | ✅ All slides |
| Min font 14 (Slides) / 22 (Canva) | ⬜ To verify in final deck |
| < 40 MB | ⬜ To verify |
| Color-blind-friendly | ⬜ To verify |
| File name: NL Myntra | ⬜ To set |
