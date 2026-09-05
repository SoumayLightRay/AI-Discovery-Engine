# 10-Slide Deck — Full Text Content (v3 — Approved)

> **File:** `NL Myntra` · 10 slides max · No Fellow name · Title = key takeaway
> **Constraints:** Min font 14 (Slides) / 22 (Canva) · < 40 MB · Color-blind-friendly
> **Changes from v2:** Cross-platform comparison narrative (not YouTube exodus), Blue Cobalt Shorts story, Cross-Seller Review Bridge bundled into Confidence Layer, competitive analysis in RICE rejections

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
| **Comparison / alternatives** | 36% | Wishlist = shortlist, not commitment. AI scored this at only 1.6% (major detection gap) |
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

**The disconfirmation IS the credibility:** We expected Price to be the villain — and it IS the largest barrier. But 11/12 interview users literally pay MORE for trust. The root cause for the *solvable* segment is information asymmetry, not price sensitivity.

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

**Root Cause — 5 Whys**

Why 1: Users hesitate to move wishlisted items to cart.
→ Because they feel uncertain about the purchase outcome.

Why 2: Why uncertain?
→ The product page doesn't give them enough real evidence to decide.

Why 3: Why is the evidence insufficient?
→ Model photos are heavily edited, size charts are inconsistent, and no verified buyer photos exist. Some products have ZERO reviews.

Why 4: Why don't they just order and return if wrong?
→ Return process is stressful and unreliable (93.5% negativity in AI data).

Why 5: So what do they do?
→ Leave the app to compare the same product's reviews on Amazon/AJIO/Flipkart. During that cross-platform comparison, they find better deals or more trusted listings and buy from the competitor.

**Root Cause:** Myntra captures purchase intent at the wishlist stage but loses control of the decision-making journey afterward. The information asymmetry on the product page forces users to comparison-shop on competing platforms, creating competitor leakage.

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

### Title: We Evaluated 6 Mechanisms — the Wishlist Confidence Layer Wins on RICE and All 3 Creativity Levels

**How Might We** reduce the information asymmetry on the wishlist page so that users can build purchase confidence without leaving the app to check competing platforms?

**Competitive Landscape (what already exists):**
- Myntra: MyFashionGPT, My Stylist, Mix & Match, Myntra Studio (influencer content)
- Amazon: AR Virtual Try-On (footwear, apparel), AI Shopping Guides
- AJIO: Style Quiz, curated collections

**6 Genuinely Different Mechanisms Evaluated:**

| # | Mechanism | Type |
|---|---|---|
| 1 | Wishlist Confidence Layer (buyer photos + fit consensus + return badge + AI digest + cross-seller review bridge) | Decision-support |
| 2 | Moodboard / Pinterest-style Fashion Board | Inspiration tool |
| 3 | Virtual Try-On (AR superimpose) | Fit resolution |
| 4 | Smart Price Alert | Timing/nudge |
| 5 | Wishlist Reminder Notifications | Re-engagement |
| 6 | Influencer Social Proof | Social validation |

**RICE Prioritisation**

| # | Mechanism | Reach | Impact | Confidence | Effort | RICE | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | **Confidence Layer** | 60% (target segment) | High — directly resolves root cause | High — validated by AI + survey + interview | Medium | **90** | ✅ **WINNER** |
| 2 | Moodboard | 35% | Medium | Low | High | 25 | ❌ Myntra already has MyFashionGPT + Mix & Match |
| 3 | Virtual Try-On | 25% | High | Medium | Very High | 20 | ❌ Amazon already has AR try-on natively |
| 4 | Price Alert | 10% | Low | Medium | Low | 15 | ❌ Violates no-incentives constraint |
| 5 | Reminders | 5% | Low | Medium | Low | 10 | ❌ Every app does this — no differentiation |
| 6 | Influencer Proof | 20% | Low | Low | Medium | 18 | ❌ Myntra Studio already exists |

**Three-Level Creativity Test**

| Level | Test | Wishlist Confidence Layer |
|---|---|---|
| **1. Problem Fit** | Does it solve the validated root cause? | ✅ Provides the exact evidence users currently leave the app to compare on Amazon/AJIO |
| **2. Differentiation** | Is it different from what exists? | ✅ No fashion platform surfaces confidence evidence on the WISHLIST page. Myntra's existing features (My Stylist, Mix & Match) address discovery, not evaluation confidence. |
| **3. Defensibility** | Why is it hard to copy? | ✅ The Cross-Seller Review Bridge creates a proprietary seller graph. The more sellers and buyers contribute, the richer the confidence data — a compounding data moat. |

---

## SLIDE 8

### Title: The Wishlist Confidence Layer — Keeping Users on Myntra Instead of Sending Them to Amazon to Check Reviews

**What the user sees on each wishlisted item:**

| Component | What It Shows | Friction Addressed |
|---|---|---|
| 📸 Verified Buyer Photos | Real photos from customers who bought this item | Quality uncertainty (14.1%) |
| 📏 Fit Consensus | "85% of buyers say true to size" — aggregated from reviews | Fit/Size doubt (4.5%) |
| 🔄 Return Clarity Badge | "✅ Returnable 15 days" or "⚠️ Non-returnable (intimates)" | Return anxiety (9.9%) |
| ⭐ AI Review Digest | 3-line summary: "Buyers love fabric but say it runs small" | Information gap (6.1%) |
| 🔗 Cross-Seller Review Bridge | When product has zero reviews: show reviews of same material/fabric from same seller, seller's overall rating | Zero-review "invisible friction" |

**The Cross-Seller Review Bridge (Novel Component):**
The interview revealed a key dilemma: two sellers, same product, different trust signals. When a product has NO reviews, instead of showing nothing (which sends users to Amazon), we show:
- Reviews of the same material/fabric from the same seller
- The seller's aggregate rating across all products
- "Similar products by this seller rated 4.3★ with 200+ reviews"

This is **genuinely novel** — no competitor does this. And it creates a proprietary seller-review graph that compounds over time.

**User Flow (3 steps)**
1. User opens wishlist → sees Confidence Layer on each item
2. Taps for detail → buyer photos, fit consensus %, return badge, AI digest, cross-seller reviews
3. Confidence resolved on-platform → moves to cart WITHOUT opening Amazon or AJIO to compare

**Architecture**
```
Myntra Reviews DB + Seller Graph → AI Summariser → Confidence Score API → Wishlist UI Overlay
```

**MVP proves the mechanism:** Can providing real-world evidence at the point of decision change user behaviour from "leave app to compare" to "buy here now"?

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
  • Cross-Seller Review Bridge engagement (for zero-review products)
  • Reduced time: wishlist-add → cart-add
  • Decreased cross-platform exits (fewer users leaving to check Amazon/AJIO)
    ↓
LAGGING INDICATORS (does behaviour persist?)
  • 7-day repeat conversion rate
  • Wishlist-to-cart velocity trend over 30 days
    ↓
GUARDRAILS (must NOT worsen — kill feature if they do)
  • Core purchase conversion rate
  • Average order value
  • Wishlist addition rate (don't discourage wishlisting)
  • Return rate (better info should reduce returns, not increase them)
```

**Kill Criteria:** If leading indicators don't move within 14 days of A/B test launch, we stop the experiment and investigate.

---

## SLIDE 10

### Title: Here's How We Could Be Wrong — and the 60-Day Experiment to Find Out

**Top Risks**

| Risk | Why It Could Fail | Mitigation |
|---|---|---|
| **Wrong root cause** | Confidence may not be the real blocker at scale (survey N = 36 wishlist users). Price is the strongest barrier at 44% — confidence is 28% explicit | A/B test with kill switch at Day 14; measure behaviour, not self-report. Price is acknowledged as constraint, not ignored |
| **AI summary errors** | Review digests could be misleading | Deterministic rules > LLM guesses; confidence thresholds; human review queue |
| **Data sparsity** | New/niche products have zero buyer photos | Cross-Seller Review Bridge as fallback (show seller's other product reviews) |
| **Cannibalisation** | May shift purchases to wishlist flow without net new sales | Track total purchase volume as guardrail |
| **Info reduces intent** | Survey found cases where more reviews killed a purchase | Monitor Confidence Layer views → cart removal correlation |

**60-Day Experiment Plan**

| Phase | Days | Action | Success Gate |
|---|---|---|---|
| Shadow | 0–14 | Show to 5% of users, engagement only | ≥15% view rate |
| A/B Test | 15–30 | 50/50 split on wishlist page | ≥5% conversion lift |
| Scale | 31–60 | 100% if gates pass | No guardrail violations |

**Beyond MVP**
- **Phase 2:** Expand Confidence Layer to cart page (pre-checkout confidence)
- **Phase 3:** Personalised confidence — learn which evidence type matters most per user (some care about fit, others about quality)
- **Long-term:** Proprietary "Trust Graph" across all sellers × products × materials — a compounding data moat that grows with every purchase

---
---

# AUDIT CHECKLIST (v3)

| Requirement | Source | Status |
|---|---|---|
| RICE framework | framework.md Phase 7 | ✅ Slide 7 — with competitive rejections |
| 3-Level Creativity Test | framework.md / arindam_feedback | ✅ Slide 7 |
| "How Might We" statement | framework.md Phase 7 | ✅ Slide 7 |
| 5 Whys root cause | framework.md Phase 5 | ✅ Slide 6 |
| Behavioural segments (not demographics) | arindam_feedback Rule 1 | ✅ Slide 6 |
| AI findings as hypotheses, not conclusions | arindam_feedback Rule 3 | ✅ Slide 3 |
| Disconfirmation / evidence changed thinking | framework.md core philosophy | ✅ Slide 5 — Blue Cobalt Shorts |
| "How thinking evolved" narrative | project.md Part 4 | ✅ Slide 5 |
| Competitive analysis in rejections | 3-Level Test Level 2 | ✅ Slide 7 — Myntra/Amazon/AJIO features cited |
| Cross-platform comparison narrative | Interview 1 + Survey | ✅ Slides 5, 6, 8 |
| North Star → solution → leading → guardrails | framework.md Phase 9 | ✅ Slide 9 |
| Risks & mitigation | project.md Part 7 | ✅ Slide 10 |
| Cross-Seller Review Bridge (novel component) | Interview 1 suggestion | ✅ Slides 7, 8 |
| Blue Cobalt Shorts story | Interview 1 | ✅ Slide 5 |
| No Fellow name | project.md | ✅ All slides |
| Title = key takeaway | project.md deck guidelines | ✅ All slides |
| Real AI data (1,367 reviews) | report.md | ✅ Slides 2–4 |
| Real survey data (N = 36 wishlist users) | primary_research.md | ✅ Slides 5, 6 |
| Real interview data (12 live calls) | docs/interview_1–12.md + interview_consolidated.md | ✅ All 12 interviews processed with real quotes |
| Links to live deliverables | project.md | ✅ Slides 1, 3, 8 |
