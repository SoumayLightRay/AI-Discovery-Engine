# Primary Research: Survey Analysis & AI Hypothesis Cross-Validation

> **Survey Source:** Google Form, 39 submissions (38 online fashion shoppers, 36 wishlist users), Sep 4–5 2026.  
> **AI Engine Source:** 1,367 reviews, 313 LLM-analysed, 70 friction-tagged, 12 themes.  
> **Purpose:** Execute the research loop — Discovery → Hypothesis → Research → **Confirm / Reject / Refine** → Problem.

---

## 1. Survey Design & Sample

- **39 submissions**, of which **38** are online fashion shoppers and **36** report using a wishlist/save/heart feature.
- **Platform spread:** Myntra (most frequent), AJIO, Nykaa Fashion, Amazon Fashion, Flipkart, brand sites, smaller apps (Urbanic, Savana, Newme, Little Box). Most shop across 2+ platforms simultaneously.
- **Wishlist sizes:** Wide range from 0–5 items to 100+. Size alone does not correlate to any single behaviour pattern.

**Data-quality caveat:** Several respondents answered with non-fashion items (iPad, Dyson, lip balm/cosmetics). The dataset is used for **directional behavioural discovery**, not as a claim that every response represents Myntra-fashion behaviour specifically.

**Methodological caution:** Self-report survey, not a behavioural observation. Every finding below is a *hypothesis to probe in live interviews*, not a validated root cause.

---

## 2. The Biggest Insight: Wishlist ≠ Purchase Queue

Among 36 wishlist users, current intent toward their most recently wishlisted item:

| Intent Level | Count | % |
|---|---|---|
| Still want it, expect to buy | 11 | 31% |
| Still want it, don't know when | 9 | 25% |
| Still considering / uncertain | 12 | 33% |
| No longer want it | 3 | 8% |
| Don't remember | 1 | 3% |

**20/36 (~56%) are clearly still interested in the item**, while another 12 are actively evaluating it.

> **Most wishlist non-purchases are not simply "users forgot about the product." A large portion represents unresolved purchase intent.**

This is important because it tells us the opportunity isn't necessarily to make people open their wishlist more often. The more interesting question is:

> **What prevents an interested user from moving from "I want this" to "I'm confident enough to buy this"?**

---

## 3. Five Competing Friction Mechanisms

The updated data reveals five distinct mechanisms that prevent wishlist conversion. They are listed in order of observed frequency.

---

### A. Economic Friction — Price / Sale / Affordability (44%)

**Strongest explicit barrier in the dataset.**

Across the 36 wishlist users:

- **14/36 (39%)** mention waiting for a sale/discount
- **12/36 (33%)** mention price being too high
- Combined, **16/36 (44%)** have a price/deal-related signal

Among the **20 high-intent users**, price/deal appears in **12/20 (60%)**.

Examples include users explicitly waiting for: a sale, a lower price, a credit-card offer, enough money, a price drop. Several successful purchases happened after a discount or better price became available.

**Framing:**

> **Price is unquestionably a research finding. But because the assignment prohibits monetary incentives, price is a solution constraint rather than the chosen solution space.**

This makes the research more credible — we acknowledge price honestly rather than pretending it isn't important, while focusing our solution on the non-monetary mechanisms below.

---

### B. Decision Friction — Comparison / Alternatives (36%)

**Almost as important as price.**

**13/36 (36%)** explicitly mention wanting to compare other options:

- *"Still comparing among other organizers"*
- *"Maybe I'll find a better alternate"*
- *"Still looking for other options"*
- *"To verify that it's the best option"*
- *"I'm looking for some other options"*

This behaviour often continues outside the app.

> **The wishlist frequently functions as a shortlist, not a commitment.**

Users don't necessarily save one product and wait to buy it. They save several candidates and then evaluate:

**Product A vs Product B vs Product C → price → reviews → fit → quality → style → decision**

This is arguably more interesting for the discovery engine than simply "users need reminders."

---

### C. Confidence Friction — Fit / Quality / Style / Visual Certainty (28%)

**Strongest non-monetary signal.**

When we combine fit/size, quality/material, style suitability, and social opinion:

**10/36 (~28%)** have at least one explicit confidence-related blocker.

Individually:

| Confidence Blocker | Count |
|---|---|
| Fit/size uncertainty | 6 |
| Quality/material doubt | 5 |
| Style suitability | 5 |
| Someone else's opinion | 1 |

**The Q15 evidence is particularly strong:**

**25/36 respondents said they have at some point decided not to buy a wishlisted fashion item because they couldn't confidently picture how it would look or fit on them.**

**Important caveat:** Q15 is a **historical/lifetime question**, so the correct statement is:

> **25/36 wishlist users report having experienced visual/fit uncertainty as a reason for abandoning a fashion purchase at some point.**

NOT: "25 users didn't buy their current wishlist item because of fit." That would be wrong.

---

### D. Product Availability Friction — Size / Stock (11%)

**Lower frequency but very high intent.**

Only **4/36 (~11%)** explicitly mention stock/size availability. But the **quality of the evidence is strong:**

- *"My size is out of stock."*
- *"Size unavailable."*
- *"Not available in my size."*

One user explicitly said they would buy as soon as the product came back in stock. Another wanted heels for an event but couldn't get their size.

**PM interpretation:** Availability has **low-to-moderate frequency + extremely high intent.** It could be a valuable **segment-specific opportunity**, even though it isn't the overall dominant problem.

---

### E. Intent / Context Decay

**Explains why some wishlist items shouldn't be converted at all.**

Several users describe: forgetting the item, losing interest, deciding they didn't need it, already owning something similar, questioning whether the purchase was necessary, finding a better option, saving multiple similar products and eventually buying one.

The 100+ wishlist respondent gives a particularly useful explanation: they often wishlist several similar items, eventually buy one, and then remove/ignore the others because they no longer need them.

> **Some non-conversion is healthy behaviour, not a product failure.**

This is critical for metric thinking. Myntra shouldn't necessarily try to force every wishlist item into a purchase. The valuable population is **high-intent + stalled** rather than **every wishlist user**.

---

## 4. Users Are Doing Significant Research Outside the Shopping App

This is probably the **most strategically interesting finding** in the new data.

Among wishlist users, **32/36 (~89%)** reported some form of activity outside the shopping app rather than "nothing extra."

| External Behaviour | Responses |
|---|---|
| Read reviews elsewhere | **15** |
| Instagram / social media | **13** |
| Compared price elsewhere | **13** |
| Looked for similar products elsewhere | **13** |
| YouTube | **11** |
| Brand website | **11** |
| Friends / family | **8** |
| Return / exchange policy | **8** |
| Offline sizing / trying | **3** |

This is much more interesting than "users browse other apps." The behaviour tells us *why* they leave — **they are trying to resolve a decision:**

| Decision they're resolving | Where they go |
|---|---|
| "Will this look good?" | Instagram / YouTube |
| "Is this actually good?" | Reviews elsewhere |
| "Is this worth the price?" | Price comparison |
| "Is there something better?" | Alternative products |
| "Will it fit?" | Offline store |
| "Can I return it?" | Return policy |

---

## 5. Evidence of Leakage After Myntra Captures Intent

This is particularly important for the business problem.

**15/36 (~42%)** said they ended up buying something similar instead.

Among high-intent users, **7/20 (35%)** reported buying something similar instead.

Some responses explicitly describe buying: the same product from another site, a cheaper alternative, a better design, a different fit, a comparable product with better perceived value.

One respondent saved a product, researched it elsewhere, and ultimately bought the **same product from another site**. Another found a better design/brand for the same price.

**This gives us a potential funnel failure:**

```
Myntra captures discovery + wishlist intent
    ↓
User starts evaluating
    ↓
User leaves Myntra
    ↓
User compares / researches
    ↓
User may return OR purchase elsewhere
```

---

## 6. Successful Conversion Reveals the Missing Trigger

The successful-purchase stories show several different triggers:

- Price dropped
- Sale appeared
- Product came back in stock
- Money became available
- Need / occasion became more urgent
- Delivery date became relevant
- User saw the product again
- User tried it offline
- Another option became less attractive

One particularly interesting example: a user forgot a wishlisted sneaker, then saw it again in an advertisement and eventually bought it. Another bought after physically trying a similar product in-store. Another bought once the price became acceptable.

> **Wishlist conversion is often triggered by a change in context, not simply by repeated exposure to the wishlist.**

---

## 7. The AI ↔ Survey Convergence Map (Updated)

| AI Engine Finding | Survey Finding | Status |
|---|---|---|
| Quality/Material = #1 theme (14.1%) | Confidence gap is a meaningful non-monetary signal (28%) | ✅ **Converged** |
| Returns = most toxic (93.5% negative) | Return/exchange policy checked by 8/36 externally; not a primary blocker | ⚠️ **Weak signal** — toxic when hit, but not top-of-mind |
| Price = high volume (10.5%) | Price is the **strongest explicit barrier** (44%) | ✅ **Converged — even stronger than AI suggested** |
| Comparison = low (1.6%) | Comparison is the **second strongest signal** (36%) | 🔄 **AI underweighted** — major detection gap |
| Reviews/Info = invisible (0%, 6.1%) | 15/36 read reviews elsewhere; "no reviews with pictures" cited | ✅ **Converged** |
| Availability = moderate (5.4%) | 4/36 (11%) explicit blocker, very high intent | ✅ **Converged** |
| Forgetting = low (1.6%) | Real but some non-conversion is healthy behaviour | ⚠️ **Refined** — don't try to convert everything |
| Fit/Size = watch (4.5%) | 6/36 explicit; 25/36 report historical fit/visual uncertainty | ✅ **Converged — more prevalent than AI suggested** |
| Social validation = low (1.9%) | Limited direct evidence (1/36) | ⚠️ **Weak signal** |

**Key detection gap:** The AI engine scored Comparison at only 1.6% because public reviews rarely discuss competitor behaviour. But in the survey, comparison is the **#2 self-reported behaviour** (36%). This is a significant gap between what users say in reviews (emotional complaints) vs. what they actually do (rational comparison). The AI engine detects complaints; the survey detects behaviour.

---

## 8. Competing Opportunity Areas for the AI Discovery Engine

| Opportunity | Evidence | Frequency | Status |
|---|---|---|---|
| Price / value | Strongest explicit blocker | 44% | **Observed — constrained** |
| Comparison / alternatives | Very frequent | 36% | **Observed** |
| Decision confidence | Strong non-monetary signal | 28% explicit; 69% historical | **Observed** |
| External research | Extremely prevalent | 89% | **Observed** |
| Availability | Lower frequency, high-intent | 11% | **Observed** |
| Intent decay | Explains some non-conversion | — | **Observed** |
| Returns | Limited evidence | 22% check externally | **Weak signal** |
| Social validation | Limited direct evidence | 3% | **Weak signal** |

The engine should ask:

> **Which mechanism is most strongly associated with high-intent users who remain stalled?**

---

## 9. Updated Behavioural Model

The survey evidence supports a richer model than simple "Wishlist → Purchase":

```
DISCOVER
   ↓
SAVE / WISHLIST
   ↓
WHAT KIND OF INTENT?
   ├── Bookmark / inspiration
   ├── Comparison / shortlist
   └── Genuine purchase intent
             ↓
       DECISION PROCESS
             ↓
   ┌─────────┼──────────┐
   ↓         ↓          ↓
 Price    Confidence  Availability
   ↓         ↓          ↓
   └────── Comparison ──┘
             ↓
      External Research
             ↓
       ┌─────┴─────┐
       ↓           ↓
     BUY       DELAY / ABANDON
       ↓           ↓
  Myntra /     Alternative /
  elsewhere    lose interest
```

---

## 10. Updated Root Cause Chain (Post-Survey)

```
SYMPTOM
  Wishlisted items sit unconverted for weeks.
    ↓
BEHAVIOUR (Section 2)
  56% still want the item; 33% are actively evaluating.
  Most non-conversion is unresolved intent, not forgetting.
    ↓
FRICTION BUNDLE (Section 3)
  Price (44%) + Comparison (36%) + Confidence (28%) + Availability (11%)
  These co-occur — users face multiple blockers simultaneously.
    ↓
WORKAROUND (Section 4)
  89% leave the app to research: reviews, social media, price comparison,
  alternatives, YouTube, brand sites, friends, return policies (4–6 actions per item).
    ↓
CONSEQUENCE (Section 5)
  42% bought something similar elsewhere. 35% of high-intent users leaked.
  Myntra captures intent but loses control of the decision-making journey.
    ↓
ROOT CAUSE
  Myntra's product page does not provide sufficient evidence
  (verified buyer photos, fit consensus, quality proof, competitive context)
  to let users resolve their decision without leaving the platform —
  and once they leave, competitor leakage occurs.
```

---

## 11. The Most Important Insight

> **Wishlist users are not simply waiting to buy. They are often using the wishlist as a decision workspace — saving candidates, comparing alternatives, researching externally and trying to resolve price, fit, quality, style or availability uncertainty before committing.**

**Business implication:**

> **Myntra may capture purchase intent at the wishlist stage but lose control of the decision-making journey afterward.**

---

## 12. Live Interview Findings (12 Respondents)

> **Method:** Live phone calls, 3–10 minutes each, rapid-fire + probing.
> **Respondents:** Rishika, Stuti, Aziz, Aastha, Umesh, Steve, Nandini, Himanshi, Tanej, Sia, Prakhar, Yaakrati + 1 screened out (Dimple, non-online-shopper).

### 12.1 The Headline: Confidence > Price (11/12 = 92%)

The single most important finding across all interviews:

| # | Name | Paid more for confidence? | Example |
|---|---|---|---|
| 1 | Rishika (F23) | ✅ | Blue Cobalt Shorts — bought expensive seller with reviews |
| 2 | Stuti (F) | ✅ | Tripod — chose reviewed over unreviewed |
| 3 | Aziz (M) | ❌ | Only counter-example — price is primary |
| 4 | Aastha (F) | ✅ | Same top — bought Amazon at higher price for reviews |
| 5 | Umesh (M) | ✅ | Snitch/Bewakoof over cheaper identical items |
| 6 | Steve (M) | ✅ | Phone cover — chose reviewed over unreviewed |
| 7 | Nandini (F) | ✅ | Dress — paid 20–30% more for reviews + photos |
| 8 | Himanshi (F) | ✅ | Chooses expensive Urbanic for quality |
| 9 | Tanej (M) | ✅ | Zara sweatshirt at premium over identical brand |
| 10 | Sia (F) | ✅ | Party dress ~₹2000 — better-reviewed option |
| 11 | Prakhar (M) | ✅ | Would choose reviewed seller for same product |
| 12 | Yaakrati (F) | ✅ | Suspects cheap = fake; chooses pricier |

> **The survey said price is the #1 barrier (44%). The interviews reveal that 11/12 users pay MORE when confidence signals are present. Price is the stated excuse; confidence is the actual lever.**

### 12.2 Cross-Interview Tallies

| Pattern | Score | Implication |
|---|---|---|
| Confidence > Price | **11/12 (92%)** | Confidence overrides price for nearly all users |
| Buyer photos > model pics | **11/12** | "Model pics से बिल्कुल ही अलग आता है" |
| Zero reviews = no buy | **9/12** | Reviews are the #1 confidence signal |
| Cross-platform comparison | **11/12** | Myntra captures intent, loses the decision journey |
| Return policy as trust signal | **7/12** | No return = "suspicious" |

### 12.3 Survey Gap Resolution

| Gap (from Section 12, pre-interview) | Interview Answer |
|---|---|
| **Why do users compare?** | Price AND reviews — not just price. Aastha: "For price comparison and quality comparison by reviews" |
| **Is "waiting for a sale" real?** | Mixed. Stuti: it's deliberate financial self-regulation, not inability. But 11/12 will pay more for confidence regardless |
| **Does more info always help?** | No — Himanshi rejected Cross-Seller Review Bridge: "1% भी doubt नहीं रखना चाहेंगे" |
| **What resolves the confidence gap?** | Buyer photos + review depth + brand trust + return policy. NOT model pics, NOT seller self-reviews |
| **Why trust YouTube over Myntra?** | Not all do — Rishika doesn't use YouTube for fashion. Cross-platform review comparison is more common |
| **What triggers context change?** | Sale appeared, price dropped, money became available, saw product again, or item went out of stock |

### 12.4 Cross-Seller Review Bridge Validation

| Name | Response | Verdict |
|---|---|---|
| Stuti | "Yeah, then maybe I would buy it" | ✅ Validated |
| Nandini | "Then I'll go ahead and buy it" | ✅ Validated |
| Sia | "Yeah. I do that." (already does this naturally) | ✅ Validated |
| Tanej | "Maybe yes... that will give me the real picture" | ⚠️ Partial |
| Umesh | Would check seller + return policy | ⚠️ Partial |
| Himanshi | "हम still नहीं खरीदेंगे... 1% भी doubt नहीं रखना चाहेंगे" | ❌ Rejected |

**Result: 3 validated, 2 partial, 1 rejected.** The concept works for most but is not universal. Himanshi's rejection is important counter-evidence.

### 12.5 New Insights from Interviews (Not in Survey or AI Data)

| Insight | Source | Implication |
|---|---|---|
| Wishlist as financial self-regulation | Stuti | Some delay is intentional — not a product failure |
| Brand trust substitutes for reviews | Aziz, Umesh, Yaakrati | Solution must differentiate branded vs. unbranded products |
| Styling/versatility doubt | Prakhar | "Will this go with my wardrobe?" is a distinct mechanism |
| Image duplication across platforms | Nandini | Users verify if photos are even real |
| Myntra Quality Check badge | Tanej | Platform-verified quality for zero-review products |
| Purchase velocity as social proof | Umesh | "Recently a lot of people started buying" — dynamic signal |
| Procrastination loop (20–30 day revisits) | Prakhar | Information needed to decide isn't changing between visits |
| Offline retail as competing channel | Steve | Leakage isn't only digital-to-digital |
| Wishlist clutter with unavailable products | Yaakrati | Greyed-out items create noise |
| Return policy = hassle, not solution | Prakhar | Users want confidence BEFORE buying, not returns after |
| Virtual try-on only for wishlisted items | Rishika | Limiting scope prevents decision paralysis |
| Seller self-reviews not trusted | Tanej | "He wants to sell his item" — need independent verification |

---

## 13. Final Root Cause Chain (Post-Survey + Post-Interview)

```
SYMPTOM
  Wishlisted items sit unconverted for weeks.
    ↓
BEHAVIOUR (Survey, Section 2)
  56% still want the item; 33% are actively evaluating.
  Most non-conversion is unresolved intent, not forgetting.
    ↓
FRICTION BUNDLE (Survey, Section 3)
  Price (44%) + Comparison (36%) + Confidence (28%) + Availability (11%)
  These co-occur — users face multiple blockers simultaneously.
    ↓
THE PARADOX (Interviews, Section 12)
  Price is the stated #1 barrier — but 11/12 users PAY MORE
  when confidence signals are present. Price is the excuse;
  confidence is the actual decision lever.
    ↓
WORKAROUND (Survey + Interviews)
  89% leave the app. 11/12 compare cross-platform.
  They check reviews, price, return policy, buyer photos,
  Instagram, YouTube, brand websites, friends, offline stores.
    ↓
CONSEQUENCE (Survey + Interviews)
  42% bought something similar elsewhere. 35% of high-intent users leaked.
  Myntra captures intent but loses control of the decision-making journey.
    ↓
ROOT CAUSE
  Myntra's product page does not provide sufficient evidence
  (verified buyer photos, fit consensus, quality proof, return clarity)
  to let users resolve their decision without leaving the platform —
  and once they leave, competitor leakage occurs.
```

---

## 14. The Most Important Insight (Final)

> **Wishlist users are not simply waiting to buy. They are using the wishlist as a decision workspace — saving candidates, comparing alternatives, and researching externally to resolve confidence uncertainty. Price is the stated barrier, but 92% of interview respondents have paid MORE for products with stronger confidence signals. The opportunity is not to lower prices — it's to raise confidence.**

**Business implication:**

> **Myntra captures purchase intent at the wishlist stage but loses control of the decision-making journey afterward. The Confidence Layer addresses this by bringing decision-resolution information (buyer photos, review summaries, fit consensus, return clarity, seller trust signals) directly onto the wishlist page — eliminating the need to leave the platform.**

---

*This document is the analytical bridge between AI Discovery (Phase 2), Survey (39 responses), and Live Interviews (12 respondents). Three rounds of research converge on the same root cause: information asymmetry on the product page forces users off-platform, where competitor leakage occurs. The solution space is confidence, not price.*

