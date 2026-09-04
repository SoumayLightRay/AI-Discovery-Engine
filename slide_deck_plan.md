# 10-Slide Deck — Full Text Content

> **File:** `NL Myntra` · 10 slides max · No Fellow name · Title = key takeaway

---
---

# PHASE A: THE PROBLEM (Slides 1–2)

---

## SLIDE 1

### Title: The Wishlist That Never Converts

Millions of Myntra users browse fashion products, save items they like, and add them to their wishlists every day. A wishlist is the strongest purchase-intent signal short of adding to cart — the user has explicitly said "I want this."

Yet only a small fraction of wishlisted items convert into purchases within 30 days. Over time, users accumulate dozens of wishlisted products while only a handful are ever bought.

**Strategic Goal**
Increase the percentage of users who purchase at least one item from their wishlist within 30 days of adding it.

**Why This Matters**
- Wishlisting = high-intent demand already on the platform
- Converting it increases purchase frequency from existing users
- No new user acquisition cost required
- Directly improves monetisation of existing traffic

**Constraint**
No monetary incentives (no discounts, no coupons, no cashback).

---

## SLIDE 2

### Title: The Wishlist-to-Purchase Journey Breaks at Stage 2 — Where Users Try to Build Confidence

We decomposed the wishlist-to-purchase journey into the stages where conversion is won or lost:

**Stage 1 — Discovery & Wishlisting**
User finds a product and saves it. Motivations vary: genuine purchase intent, aspirational bookmarking, waiting for a price drop.

**Stage 2 — Evaluation & Confidence Building → 30.1% OF ALL FRICTION**
The user returns to evaluate the item. This is where the journey breaks most often:
- Quality/Material doubt — 14.1%
- Reviews/Information gap — 6.1%
- Fit/Size uncertainty — 4.5%
- Styling/Occasion doubt — 3.5%
- Social validation seeking — 1.9%

**Stage 3 — Decision & Commitment → 27.1%**
The user tries to commit. Remaining barriers:
- Price & discount expectations — 10.5%
- Return/Exchange policy fear — 9.9%
- Availability/Delivery — 5.4%
- Alternative platform comparison — 1.3%

**Stage 4 — Conversion or Drop-off → 3.2%**
Forgetting, distraction, or permanent abandonment.

**Strategic Focus:** Stage 2 has the highest friction concentration AND is the most solvable without monetary incentives. Stage 3 friction (price, returns) is harder to address under the no-incentives constraint.

---
---

# PHASE B: THE INVESTIGATION (Slides 3–4)

---

## SLIDE 3

### Title: We Built an AI Engine That Analysed 1,367 Reviews and Produced 12 Friction Hypotheses — Not Conclusions

**The Pipeline**
Ingest → Analyse → Retrieve → Deliver

1. **Ingest:** Apify Cloud scraped 1,367 public reviews from 4 channels
2. **Analyse:** Groq LLaMA 3.3 70B classified each review on 5 dimensions (theme, sentiment, friction, verbatim, source)
3. **Retrieve:** BM25 + TF-IDF semantic search across the full corpus
4. **Deliver:** Interactive dashboard + chatbot on Vercel

**Data Sources (Balanced Sampling)**

| Channel | Reviews | What It Captures |
|---|---|---|
| Google Play | 78 (24.9%) | Delivery, returns, quality complaints |
| App Store | 77 (24.6%) | Returns, wrong products, customer service |
| YouTube | 79 (25.2%) | Aspirational, styling, social validation |
| Reddit | 79 (25.2%) | Price, fit, honest reviews, sizing complaints |

**Total Analysed:** 313 reviews deep-analysed · 70 friction-tagged (22.4%)

**Critical Framing:** These AI-generated themes are hypotheses that require human validation. The engine assists research — it does not replace the PM's thinking.

**Live links:** Dashboard · Full Report · GitHub

---

## SLIDE 4

### Title: The Engine Revealed That Severity ≠ Frequency — The Loudest Complaints Are Not the Biggest Blockers

**Top Friction Themes (from 313 analysed reviews)**

| Theme | Volume | Negativity Rate | What This Means |
|---|---|---|---|
| Quality/Material | 14.1% | 6.8% | Highest volume but low anger — diffuse uncertainty, not acute rage |
| Price | 10.5% | 36.4% | Only 1 in 3 mentions is a complaint; rest are neutral comparisons |
| Returns | 9.9% | 93.5% | Nearly every mention is toxic — but not top-of-mind for most users |
| Reviews/Info | 6.1% | 0.0% | "Invisible friction" — the absence of information kills silently |
| Fit/Size | 4.5% | 42.9% | All friction from Reddit — users research sizing offline and on YouTube |

**The Key Analytical Insight**
High volume ≠ High severity. Returns (31 mentions, 93.5% negative) is far more emotionally damaging per-mention than Quality (44 mentions, 6.8% negative). But Quality affects more users overall because it represents diffuse uncertainty — users aren't angry, they're unsure. And the themes with 0% negativity (Reviews, Styling, Comparison) represent "invisible friction" that silently prevents conversion without generating any complaints at all.

**Channel Cross-Tabulation**
- Returns is universal — appears across Google Play, App Store, AND Reddit
- Availability is a Google Play problem (80% of those complaints)
- Price frustration is a Reddit phenomenon (73%)
- Fit/Size is exclusively Reddit (100%)
- YouTube contributes zero friction — purely aspirational

**Strongest Repeat Signals**
- "No return policy on bras and panties" — appeared 7 times from different users
- "None of the good items got any discounts" — appeared 6 times

---
---

# PHASE C: THE VALIDATION (Slides 5–6)

---

## SLIDE 5

### Title: A Survey of 29 Users Confirmed Our Core Hypothesis — and Exposed a Major Gap in Our AI Data

**Survey:** Google Form, 31 submissions (effective N ≈ 29), Sep 4–5 2026.

**What the survey confirmed:**
- ✅ Quality/Confidence gap is the primary friction — users say "Will it be worth it!", "no reviews with pictures", "not sure how it fits"
- ✅ Fit/Size is highly prevalent — among the top 2 most-ticked reasons
- ✅ Users leave the app to research — YouTube, Instagram, competitor apps, brand websites, offline stores (4–6 actions per item)

**What the survey refined:**
- ⚠️ "Price" is NOT one problem — it's three: (a) waiting for a sale (unsolvable), (b) personal cash-flow timing (external), (c) value-unproven (solvable!). Pure price-only holdouts are a minority.
- ⚠️ Price is rarely ticked alone in multi-select — it almost always co-occurs with fit/comparison. Most users cite a bundle of blockers, not a single cause.

**What the survey revealed that the AI missed:**
- 🔄 Comparison is the #1 most-ticked multi-select reason — but the AI scored it at only 1.6%. Why? Because public reviews rarely discuss competitor behaviour. The AI detects complaints; the survey detects behaviour. This is a significant detection gap.

**The disconfirmation IS the credibility:** We expected Price to be the dominant standalone blocker. The survey showed it's a secondary justification layered on top of a primary confidence gap. If users were confident the product was worth it, the price wouldn't feel as high.

**Caution noted:** Q15 ("can't picture how it would look/fit") was a leading yes/no prompt — high agreement on a closed question is weaker evidence than the same theme appearing unprompted in open text (which it does, but less dominantly than Q15's raw percentage suggests).

---

## SLIDE 6

### Title: 60% of Stalled Users Are "Confidence-Starved Evaluators" — They Want to Buy but Can't Decide Without Leaving the App

**Behavioural Segments (derived from behaviour, not demographics)**

| Segment | % | Blocker | Actionable? |
|---|---|---|---|
| **Value-unproven evaluators** | ~35% | "Is it worth it?" — need evidence, not a lower price | ✅ Primary target |
| **Fit/style researchers** | ~25% | "Will it suit me?" — actively leaving app for YouTube/offline | ✅ Secondary target |
| Stock-out-blocked | ~15% | Size unavailable, often event-driven | ⚠️ Logistics problem |
| Cash-timing-blocked | ~10% | Waiting on salary/allowance, not price | ❌ External |
| Price-waiters | ~10% | Explicitly waiting for discount | ❌ No-incentives constraint |
| Passive decayers | ~5% | No blocker; item loses salience over time | ⚠️ Nudge only |

**Why We Chose This Segment:** Value-unproven + Fit/style researchers (combined ~60%) have the highest baseline intent, the pain is explicitly stated in their own words, and the blocker is solvable without monetary incentives.

**Root Cause Chain**

Symptom: Wishlisted items sit unconverted for weeks.
→ Behaviour: User wants the item but delays purchase.
→ Reason: "I'm not sure if it's worth it" / "not sure how it fits" / "no reviews with pictures"
→ Workaround: Leaves app → researches on YouTube, Instagram, competitor apps (4–6 actions per item)
→ Consequence: During off-platform research, finds alternative → buys from competitor → Myntra loses the sale
→ Root cause: Myntra's product page lacks real-world evidence (verified buyer photos, honest fit consensus, quality proof) to let the user decide without leaving the platform.

**Problem Statement**
Among high-intent users who wishlist fashion items, those who lack sufficient real-world evidence delay purchasing because Myntra's product page creates uncertainty about quality, fit, and value. They currently resolve this doubt by researching on YouTube and Instagram, which delays their decision and creates opportunities for competitors to intercept the purchase.

**Competitor leakage evidence:**
- "Found better design and branded stuff for same price"
- "Bought it from different site"
- "Got notification from Flipkart that prices gone down. Bought it cheaper from somewhere else."

---
---

# PHASE D: THE SOLUTION (Slides 7–8)

---

## SLIDE 7

### Title: We Evaluated 6 Mechanisms — the Wishlist Confidence Layer Wins Because It Directly Resolves the Root Cause Without Monetary Incentives

**The 6 mechanisms we considered:**

| # | Mechanism | Problem Fit | Differentiation | Defensibility | Verdict |
|---|---|---|---|---|---|
| 1 | **Wishlist Confidence Layer** | ✅ Directly resolves information asymmetry | ✅ No competitor does this on the wishlist page | ✅ Accumulates proprietary buyer data | **Winner** |
| 2 | AI Outfit Recommender | ⚠️ Addresses styling, not confidence | ❌ Multiple competitors have this | ❌ Easily copied | Rejected |
| 3 | Smart Price Alert | ❌ Requires monetary incentive logic | ⚠️ Flipkart already does this | ❌ No moat | Rejected |
| 4 | Social Proof Nudges | ⚠️ Partial — social signal, not product evidence | ❌ Amazon already does this | ❌ Trivial to copy | Rejected |
| 5 | Wishlist Reminder Notifications | ⚠️ Addresses forgetting (5%), not confidence (60%) | ❌ Every app does this | ❌ No moat | Rejected |
| 6 | AR Virtual Try-On | ✅ Great for fit doubt | ❌ Capital-intensive for MVP | ✅ Hard to copy | Too complex |

**Three-Level Creativity Test (per Arindam's framework)**

Level 1 — Problem Fit: Does it solve the validated root cause?
→ Yes. The Confidence Layer provides the exact evidence (verified photos, fit consensus, return clarity) that users currently leave the app to find on YouTube and Instagram.

Level 2 — Differentiation: Is it meaningfully different from competitors?
→ Yes. No fashion platform currently surfaces confidence evidence directly on the wishlist page. The wishlist is treated as a static list, not an active decision-support tool.

Level 3 — Defensibility: Why is it hard to copy?
→ The system accumulates proprietary verified-buyer photo and fit-consensus data over time. The more buyers contribute, the richer the confidence layer becomes. This creates a compounding data advantage.

---

## SLIDE 8

### Title: The Wishlist Confidence Layer — Bringing YouTube-Level Evidence Onto the Wishlist Page

**What the user sees on each wishlisted item:**

| Component | What It Shows | Friction Addressed |
|---|---|---|
| 📸 Verified Buyer Photos | Real photos from customers who purchased this item | Quality uncertainty (14.1%) |
| 📏 Fit Consensus | "85% of buyers say true to size" — aggregated from reviews | Fit/Size doubt (4.5%) |
| 🔄 Return Clarity Badge | "✅ Returnable within 15 days" or "⚠️ Non-returnable (intimates)" | Return anxiety (9.9%) |
| ⭐ AI Review Digest | 3-line summary: "Buyers love the fabric but say it runs small" | Information gap (6.1%) |

**User Flow**
1. User opens their wishlist → sees the Confidence Layer on each item
2. Taps an item → verified buyer photos, fit consensus percentage, return eligibility, AI review summary
3. Confidence resolved on-platform → moves to cart without needing to check YouTube or Instagram

**Why This Works**
The MVP replicates the exact information users currently seek outside the app (real photos on YouTube, honest sizing on Reddit, return policy confirmation) and brings it directly to the point of decision. It eliminates the off-platform research session that creates competitor leakage.

**Architecture**
Myntra Reviews Database → AI Summarisation Engine → Confidence Score API → Wishlist UI Overlay

**Live MVP:** [ai-discovery-engine-rose.vercel.app](https://ai-discovery-engine-rose.vercel.app/)

---
---

# PHASE E: THE MEASUREMENT (Slides 9–10)

---

## SLIDE 9

### Title: North Star — 30-Day Wishlist-to-Purchase Conversion. If Guardrails Break, We Kill the Feature.

**Metric Causal Chain**

North Star Metric
→ 30-day Wishlist → Purchase Conversion Rate
→ % of users who purchase ≥1 wishlisted item within 30 days of adding it

Solution Metric (what our feature directly changes)
→ % of users who view the Confidence Layer and then move an item to cart

Leading Indicators (does the mechanism fire?)
→ Confidence Layer view rate (target: ≥15% of wishlist visits)
→ Verified buyer photo click-through rate
→ Reduced time between wishlist-add and cart-add
→ Decreased off-platform exits during wishlist sessions

Lagging Indicators (does the behaviour persist?)
→ 7-day repeat conversion rate
→ Wishlist-to-cart velocity trend over 30 days

Guardrail Metrics (must NOT get worse — if they do, kill the feature)
→ Core purchase conversion rate
→ Average order value
→ Wishlist addition rate (don't accidentally discourage wishlisting)
→ Return rate (better upfront info should reduce returns, not increase them)

**Kill Criteria:** If leading indicators don't move within 14 days of A/B test launch, we stop the experiment and investigate.

---

## SLIDE 10

### Title: Here's How We Could Be Wrong — and the 60-Day Experiment to Find Out

**Top Risks**

| Risk | Why It Could Fail | Mitigation |
|---|---|---|
| Wrong root cause | Confidence may not be the real blocker at scale — survey N is small | A/B test with kill switch at Day 14; measure actual behaviour, not self-report |
| AI summary errors | Review digests could be inaccurate or misleading | Deterministic rules over LLM guesses; human review queue for edge cases; confidence thresholds |
| Data sparsity | New or niche products may have zero buyer photos | Graceful fallback to brand-provided content with clear "Brand photo" vs "Buyer photo" labelling |
| Cannibalisation | Feature may shift purchases from browse-to-buy to wishlist-to-buy without net new purchases | Track total purchase volume as guardrail metric, not just wishlist conversion |
| Information reduces intent | Survey found one case where more reviews killed a purchase ("after view reviews mind changes") | Monitor for cases where Confidence Layer engagement correlates with cart removal — investigate if pattern emerges |

**60-Day Experiment Plan**

| Phase | Days | Action | Success Gate |
|---|---|---|---|
| Shadow mode | 0–14 | Show to 5% of users, measure engagement only | ≥15% Confidence Layer view rate |
| A/B test | 15–30 | 50/50 split on wishlist page, measure conversion | ≥5% lift in wishlist-to-cart conversion |
| Scale | 31–60 | 100% rollout if both gates pass | No guardrail violations |

**Beyond MVP — What's Next**
- Phase 2: Expand Confidence Layer to cart page (pre-checkout confidence boost)
- Phase 3: Personalised confidence — learn which evidence type matters most per user (some care about fit, others about quality)
- Long-term: Build a proprietary "Trust Graph" across all products — a compounding data moat that improves with every purchase and every buyer photo uploaded
