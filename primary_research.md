# Primary Research: Survey Analysis & AI Hypothesis Cross-Validation

> **Survey Source:** Google Form, 31 submissions (effective N ≈ 29), Sep 4–5 2026.  
> **AI Engine Source:** 1,367 reviews, 313 LLM-analysed, 70 friction-tagged, 12 themes.  
> **Purpose:** Execute the research loop — Discovery → Hypothesis → Research → **Confirm / Reject / Refine** → Problem.

---

## 1. Survey Design & Sample

- **31 submissions**, 2 duplicate resubmits → effective N ≈ 29–30.
- 2 respondents don't wishlist at all (screened out) → core analysis N ≈ 27–29.
- **Platform spread:** Myntra (most frequent), AJIO, Nykaa Fashion, Amazon Fashion, Flipkart, brand sites, smaller apps (Urbanic, Savana, Newme, Little Box). Most shop across 2+ platforms simultaneously.
- **Wishlist sizes:** Wide range from 0–5 items to 100+. Size alone does not correlate to any single behaviour pattern.
- **Methodological caution:** Self-report survey, not a behavioural observation. Every finding below is a *hypothesis to probe in live interviews*, not a validated root cause.

---

## 2. AI Hypothesis Cross-Validation: What the Survey Confirms, Rejects, and Refines

This is the most important section. The AI Discovery Engine produced 12 friction hypotheses. Here is what the primary research did to each one.

### ✅ CONFIRMED: Information Asymmetry / Confidence Gap (AI: 14.1% Quality + 6.1% Reviews)

**AI hypothesis:** Users doubt product quality because of edited photos and insufficient reviews.

**Survey evidence — STRONG confirmation, with critical nuance:**
- Open-text (unprompted): *"The product doesn't have many reviews"*, *"no reviews with pictures"*, *"Will it be worth it!"*, *"still unsure if it's worth the price and whether it will actually meet my expectations"*
- Multi-select (Q9): "Unsure about size or fit" and "unsure about quality/material" were among the most frequently ticked.
- Q15 (prompted): Large majority answered "Yes" to the fit-visualisation question.

**Critical nuance the AI missed:** The survey reveals that "quality doubt" and "value doubt" are **different frictions**. 
- *Quality doubt* = "Will the material match the photos?" (about product truth)
- *Value doubt* = "Is this product worth ANY price until I'm reassured?" (about purchase justification)
The AI engine lumped both under "Quality/Material." The interviews should separate them.

**Verdict: CONFIRMED and REFINED — split into Quality-truth and Value-justification.**

---

### ✅ CONFIRMED: Fit/Size Uncertainty (AI: 4.5%)

**AI hypothesis:** Users can't confidently predict whether the item will fit.

**Survey evidence — CONFIRMED, with behavioural detail:**
- Open-text: *"not sure how it fits"*, *"Don't know if it will suit me"*, *"Wasn't sure, if it will look good on me"*
- Behavioural: Multiple respondents report going to an **offline store** to check sizing before buying online, and searching **YouTube** for haul videos. This is active resolution behaviour — the doubt isn't passive, users are working on it, just not on Myntra's platform.
- Q9 multi-select: "Unsure about size or fit" is one of the two most-ticked reasons.

**New insight AI couldn't see:** Fit doubt often co-occurs with other blockers ("comparison" + "fit" + "price" ticked together by the same person). The friction is a **bundle**, not a single cause.

**Verdict: CONFIRMED — and revealed as part of a multi-cause bundle, not a standalone blocker.**

---

### ⚠️ REFINED: Price (AI: 10.5%) — Three Distinct Sub-Problems, Not One

**AI hypothesis:** Users are dissatisfied with pricing and wait for discounts.

**Survey evidence — CONFIRMED but must be decomposed into three distinct mechanisms:**

| Sub-problem | Survey evidence | Solvable without incentives? |
|---|---|---|
| **Waiting for a sale** | *"Waiting for prices to go down"*, *"waiting for sale and offers"* | ❌ No — this is learned platform behaviour |
| **Personal cash-flow timing** | *"Waiting to receive money from dad"*, *"my salary was higher... now lower"*, *"Because I don't earn"* | ❌ No — not a product problem |
| **Value unproven** | *"Will it be worth it!"*, *"unsure if it's worth the price and whether it will actually meet my expectations"* | ✅ **Yes** — this is confidence, not price |

**Critical finding:** "Waiting for a sale" is rarely ticked alone in Q9 — it almost always co-occurs with "comparison" or "fit." Pure price-only holdouts are a **minority**. This suggests that for many users, "price" is a secondary justification layered on top of a primary confidence gap. If they were confident the product was worth it, the price wouldn't feel as high.

**Verdict: REFINED — "Price" is actually 3 different problems. Only "Value unproven" is actionable.**

---

### ✅ CONFIRMED: Comparison / Alternatives (AI: 1.6% + 1.3%)

**AI hypothesis:** Users compare across platforms and sometimes buy elsewhere.

**Survey evidence — CONFIRMED and revealed as MORE important than the AI's low percentage suggested:**
- Q9: "Wanted to compare other options" was arguably the **single most-ticked reason** across all respondents.
- Q12 (abandonment): *"found better design and branded stuff for same price"*, *"Bought it from different site"*, *"Got a notification from Flipkart that prices have gone down. Bought it for cheaper from somewhere else."*
- Q13: 34.4% of respondents compare price elsewhere; 34.4% look for similar products on other apps.

**Critical finding the AI underweighted:** The AI engine scored Comparison at only 1.6% and Alternatives at 1.3% because public reviews rarely discuss competitor behaviour. But in the survey, comparison is the **#1 self-reported behaviour**. This is a significant gap between what users say in reviews (emotional complaints) vs. what they actually do (rational comparison). The AI engine detects complaints; the survey detects behaviour.

**Verdict: CONFIRMED — and revealed as far more prevalent than AI data suggested. The AI's 1.6% was a detection gap, not a reality gap.**

---

### ✅ CONFIRMED: Availability / Stock-Out (AI: 5.4%)

**AI hypothesis:** Items become unavailable, blocking purchase.

**Survey evidence — CONFIRMED as a distinct, high-intent segment:**
- Open-text (4+ mentions): *"My size is out of stock"*, *"Size unavailable"*, *"Not available in my size"*, *"Size not available"*
- Often tied to a **deadline** (event, occasion) — these users have the highest intent of anyone in the sample.
- Concentrated in **footwear** (heels, boots, sneakers) per Q9 cross-referencing.

**Verdict: CONFIRMED — distinct segment, but an inventory problem (not a PM/product problem).**

---

### ✅ CONFIRMED: Forgetting / Passive Decay (AI: 1.6%)

**AI hypothesis:** Some users simply forget about wishlisted items.

**Survey evidence — CONFIRMED as a real but distinct failure mode:**
- Open-text: *"I forgot"*, *"Got distracted or forgot"*
- Interest decay without new information: *"Did not find the product as appealing as it did before"*, *"I don't really want it anymore... Confusion"*
- Q5 (conversion triggers): Reminders work — *"saw it in an advertisement"*, *"was searching for something and remembered it was in my cart"*

**New insight:** This is a **different mechanism** from doubt. Nothing changed about the product — attention simply moved on. These users don't need more information; they need re-engagement triggers.

**Verdict: CONFIRMED — small but real. Distinct from confidence-gap users.**

---

### 🆕 NEW: Conscious Accumulation Control (AI: Not Detected)

**Survey found a behaviour the AI engine never saw:**
- One respondent: *"I don't want to keep creating more collections"*
- This is deliberate self-restraint — the user wants the item, can afford it, knows it fits, but is consciously curbing consumption.

**Verdict: NEW — too small to act on (N=1), but worth probing in interviews.**

---

### 🆕 NEW: Information Can REDUCE Intent (AI: Not Detected)

**Survey found a counter-intuitive signal:**
- One respondent abandoned a wishlisted item specifically **after reading more reviews**: *"after view reviews mind changes"*
- This means "more reviews" is not universally positive. For some users, additional information reveals problems they hadn't considered and kills the purchase.

**Verdict: NEW — challenges the assumption that "more information = more conversion." The interviews should probe this.**

---

## 3. What People Do Outside the App (The Research Exodus)

When users are stalled, they don't passively wait. They conduct a **multi-step research process entirely outside Myntra's ecosystem:**

| External Channel | Rough Prevalence | What They're Seeking |
|---|---|---|
| YouTube | Very common | Video hauls, real-world look, material check |
| Instagram / social media | Very common | Styling, outfit pairing, social validation |
| Other e-commerce apps | Very common | Price comparison, alternative products |
| Brand's own website | Moderate | Better product details, size guides |
| External review sites | Moderate | Honest quality/fit feedback |
| Friends/family | Moderate | Social validation, fit advice |
| Offline store visit | Small but notable | Physical try-on before online purchase |

**Key finding:** Several respondents do **4–6 of these actions for a single item**. This is not a quick Google search — it's a sustained research session happening entirely off-platform. Every minute spent on YouTube or Instagram is a minute where a competitor's ad, a better deal, or a "good enough" alternative can intercept the purchase.

---

## 4. Conversion Triggers: What Finally Breaks the Stall?

| Trigger Type | Survey Evidence | Implication |
|---|---|---|
| **Price/discount** | *"purchased at better price"*, *"prices gone down"* | Monetary lever — outside our constraint |
| **Cash availability** | *"when I got money"*, *"had enough money"* | External life event — can't influence |
| **Reminder/re-exposure** | *"saw it in an advertisement"*, *"remembered it was in my cart"* | Platform can engineer this ✅ |
| **Urgency/deadline** | *"delivery date was near"* (event-driven) | Platform can surface occasion relevance ✅ |
| **Doubt resolution** | One user tried the item in an offline store, then bought online | Platform can replicate this digitally ✅ |

**Strategic insight:** The three triggers we CAN influence (reminder, urgency, doubt resolution) all map to the confidence-gap and passive-decay segments. This validates our focus.

---

## 5. Abandonment Patterns: How Myntra Loses the Sale

| Abandonment Type | Evidence | Revenue Impact |
|---|---|---|
| **Leakage to competitor** | *"Bought from different site"*, *"found better design for same price"*, *"Flipkart notification"* | **Lost revenue** — user's need was met, just not by Myntra |
| **Need already met** | *"Realized I already own similar"* | No lost revenue |
| **Interest decay** | *"Not as appealing as before"*, *"lost interest"* | Forecasting error — was never real intent |
| **Information killed intent** | *"after view reviews mind changes"* | Actually a good outcome — user avoided a bad purchase |

**The competitor leakage pattern is the most dangerous.** Multiple respondents explicitly state they bought the same or similar product from a different platform. The wishlist-to-purchase pipeline is not just slow — it's **leaky**.

---

## 6. Behavioural Segments (Hypotheses for Interview Validation)

Based on observed behavioural clustering, not demographics:

| Segment | Behaviour | Blocker Type | Size in Sample | Actionable? |
|---|---|---|---|---|
| **Value-unproven evaluators** | Want the item, can't justify the spend without more evidence | Confidence gap | ~35% | ✅ **Primary target** |
| **Fit/style-doubtful researchers** | Actively leaving app to resolve doubt via YouTube/Instagram/offline | Information gap | ~25% | ✅ Secondary target |
| **Stock-out-blocked** | Want to buy, size/item unavailable, often event-driven | Inventory | ~15% | ⚠️ Logistics problem |
| **Cash-timing-blocked** | Want the item at current price, waiting on personal income | External life | ~10% | ❌ Not solvable |
| **Price-waiters** | Explicitly waiting for discount/sale event | Monetary | ~10% | ❌ Constrained |
| **Passive decayers** | No active blocker; item loses salience over time | Attention | ~5% | ⚠️ Nudge only |

**Target segment chosen: Value-unproven evaluators + Fit/style-doubtful researchers (combined ~60%)**

Rationale:
- **Meaningful population:** ~60% of the sample
- **Strong pain:** They explicitly describe the friction in their own words
- **High intent:** They *want* to buy — they're not browsing or bookmarking
- **Metric leverage:** Converting this group directly improves 30-day wishlist-to-purchase
- **Solvable without monetary incentives:** The blocker is confidence, not price

---

## 7. The AI ↔ Survey Convergence Map

| AI Engine Finding | Survey Finding | Status |
|---|---|---|
| Quality/Material = #1 theme (14.1%) | Confidence gap is the primary open-text signal | ✅ **Converged** |
| Returns = most toxic (93.5% negative) | Return/exchange policy checked externally; not top-of-mind blocker in survey | ⚠️ **Partially validated** — toxic when hit, but not the primary stall |
| Price = high volume (10.5%) | Price is rarely a standalone blocker; usually bundled with fit/comparison | ⚠️ **Refined** — decomposed into 3 sub-problems |
| Comparison = low (1.6%) | Comparison is the **#1 multi-select tick** | 🔄 **AI underweighted** — detection gap |
| Reviews/Info = invisible (0%, 6.1%) | "No reviews with pictures" cited explicitly | ✅ **Converged** |
| Availability = moderate (5.4%) | Stock-out is a real, distinct, high-intent blocker | ✅ **Converged** |
| Forgetting = low (1.6%) | Real but small; reminders work as conversion triggers | ✅ **Converged** |
| Fit/Size = watch (4.5%) | Among top 2 most-ticked multi-select reasons | ✅ **Converged — and more prevalent than AI suggested** |

---

## 8. Updated Root Cause Chain (Post-Survey)

```
SYMPTOM
  Wishlisted items sit unconverted for weeks.
    ↓
BEHAVIOUR (Survey Section 2)
  User wants the item but delays purchase.
    ↓
IMMEDIATE REASON (Survey Section 2, open-text)
  "I'm not sure if it's worth it" / "not sure how it fits" / "no reviews with pictures"
    ↓
WORKAROUND (Survey Section 4)
  User leaves the app to research on YouTube, Instagram, competitor apps (4–6 actions per item)
    ↓
CONSEQUENCE (Survey Section 6)
  During the off-platform research, user finds alternative → buys from competitor → Myntra loses the sale.
    ↓
ROOT CAUSE
  Myntra's product page does not provide sufficient real-world evidence
  (verified buyer photos, honest fit consensus, quality proof) to let the
  user make a confident decision without leaving the platform.
```

---

## 9. Gaps and What the Interviews Must Resolve

| Gap | Why the Survey Can't Answer It | Interview Probe |
|---|---|---|
| **Why do users compare?** | Multi-select can't distinguish price-comparison from fit-comparison from habitual browsing | "Walk me through what you're actually looking for when you check another app" |
| **Is "waiting for a sale" real price sensitivity or trained behaviour?** | Self-report can't separate genuine from learned | "If Myntra guaranteed no future discount on this item, would you buy it now?" |
| **Does more information always help?** | One respondent's intent dropped after reading reviews | "Has reading reviews ever made you NOT want something?" |
| **What specifically resolves the confidence gap?** | Survey shows they research, not what resolves it | "What was the specific moment you felt confident enough to click Buy?" |
| **Why do users trust YouTube over Myntra's product page?** | Survey says they go to YouTube but not why | "What does a YouTube haul video show you that the Myntra page doesn't?" |

---

*This document is the analytical bridge between AI Discovery (Phase 2) and Live Interviews (Phase 4). The survey has confirmed the core hypothesis — the friction is a confidence gap, not a price gap — but the precise mechanism ("what specifically makes a user feel confident enough to buy?") remains an interview question.*
