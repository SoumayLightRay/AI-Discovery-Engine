# PM Fellowship — Master Framework & 10-Slide Architecture

> Synthesised from: top-scoring deck teardowns (Zepto, Blinkit), NextLeap/Arindam Mukherjee feedback, project.md requirements, and our AI Discovery Engine findings.
>
> **Core philosophy:** The story is not "I had an idea → research agreed → I built it."
> The story is "We started with a metric → decomposed behaviour → investigated without assuming → evidence changed our hypotheses → primary research narrowed the problem → we found a specific root cause → several solutions were considered → one mechanism won → we built the smallest thing that could test it."

---

## The Master Chain

```
BUSINESS GOAL
    ↓
METRIC DECOMPOSITION
    ↓
BEHAVIOURAL FUNNEL
    ↓
AI DISCOVERY (Hypotheses, NOT conclusions)
    ↓
    ┌──────────────────────────────────────┐
    │  RESEARCH LOOP                       │
    │  Discovery → Hypothesis → Research   │
    │  → Confirm / Reject / Refine         │
    │  → Problem                           │
    └──────────────────────────────────────┘
    ↓
PRIMARY RESEARCH (5–6 interviews)
    ↓
SEGMENT (derived from behaviour, NOT demographics)
    ↓
ROOT CAUSE (5 Whys — not symptom-level)
    ↓
PROBLEM DEFINITION (customer-centred)
    ↓
OPPORTUNITY (what Myntra can realistically change)
    ↓
IDEATION (4–6 genuinely different mechanisms)
    ↓
PRIORITISATION (Impact × Reach × Confidence × Effort)
    ↓
MVP (proves the mechanism, not the whole product)
    ↓
MEASUREMENT (North Star → solution metric → leading → guardrails)
    ↓
RISKS & EXPERIMENT DESIGN
```

---

## Phase 1 — Business Goal & Metric Decomposition

### Business Goal

> Increase the percentage of users who purchase at least one item from their wishlist within 30 days of adding it.

**Constraint:** No monetary incentives.

### Why This Metric Matters

Wishlist addition is NOT the goal. The goal is:

> A user who expresses interest by wishlisting eventually converts that interest into a purchase within 30 days.

Improving this metric increases purchase frequency, improves monetisation from existing users, and extracts value from high-intent demand already on the platform — without needing to acquire new users.

### Metric Decomposition — The Diagnostic Map

Don't just decompose into "Wishlist → Purchase." Ask *where the conversion can fail* at each stage:

#### Stage 1 — Is the wishlist item genuine purchase intent?

Users wishlist because they:
- Genuinely intend to buy (our data: Intent/Bookmarking = 4.2%)
- Are waiting for a price drop (Price = 10.5%)
- Are comparing across platforms (Comparison = 1.6%)
- Want inspiration / aspirational bookmarking
- Like the product but aren't ready

This creates an **intent ceiling**. Not all wishlists are purchase signals.

#### Stage 2 — Does intent survive?

The user must return to the item. Potential failures:
- Forgot about the item (our data: Forgetting = 1.6%)
- No longer relevant / occasion passed
- Found alternative on another platform (Alternatives = 1.3%)
- Distracted by new arrivals

#### Stage 3 — Can the user make a confident decision?

This is where **30.1% of all friction clusters** in our data. Potential failures:
- Quality/material doubt (our data: **14.1%** — highest volume)
- Fit/size uncertainty (4.5%)
- Review/information insufficiency (6.1%)
- Styling/occasion doubt (3.5%)
- Social validation seeking (1.9%)

#### Stage 4 — Is the item actually purchasable?

Potential failures:
- Out of stock / size unavailable (our data: Availability = 5.4%)
- Price changed since wishlisting
- Delivery issues — especially Tier 2/3 cities (88.2% negativity rate on availability mentions)
- Return/exchange policy fear (our data: **9.9%**, 93.5% negativity rate)

#### Stage 5 — Does checkout complete?

Potential failures:
- Cart abandonment at payment
- Last-minute hesitation
- Platform fee surprise (verbatim: "additional platform fee on every order feels unnecessary")

**This gives us a neutral diagnostic framework.** We are NOT saying "Quality is the problem." We are saying "Here are all the places the behaviour can break. Now let's find out which ones actually do."

---

## Phase 2 — AI Discovery Engine (Hypotheses, NOT Conclusions)

### What the Engine Does

```
COLLECT → CODE → QUANTIFY → COMPARE → FALSIFY → OUTPUT
```

| Step | What It Does | Our Implementation |
|---|---|---|
| **Collect** | Scrape public Myntra conversations | Apify (4 channels: Google Play, App Store, YouTube, Reddit) |
| **Code** | Classify each review on 5 dimensions | Groq LLaMA 3.3 70B — theme, sentiment, friction, verbatim, source |
| **Quantify** | Count themes, cross-tabulate | 13-theme taxonomy, channel × sentiment × theme matrices |
| **Compare** | Rank by frequency, severity, solvability | Opportunity scoring with composite F×S×S metric |
| **Falsify** | Ask "What evidence would make this hypothesis weaker?" | Negativity rates reveal "invisible friction" vs. acute complaints |
| **Output** | An Opportunity Map — NOT a conclusion | Ranked hypotheses with status labels |

### The Opportunity Map (from our data)

| Opportunity | Evidence Volume | Negativity Rate | Sources | Conversion Stage | Status |
|---|---|---|---|---|---|
| Quality/Material | 44 (14.1%) | 6.8% (diffuse uncertainty) | GP, Reddit | Stage 3: Evaluation | **Hypothesis** |
| Price | 33 (10.5%) | 36.4% | Reddit, GP | Stage 3: Decision | **Hypothesis** — constrained by no-incentives rule |
| Returns | 31 (9.9%) | **93.5%** (toxic) | All 3 complaint channels | Stage 4: Risk | **Hypothesis** |
| Reviews/Info | 19 (6.1%) | 0.0% (invisible friction) | All | Stage 3: Evaluation | **Hypothesis** |
| Availability | 17 (5.4%) | 88.2% | Google Play (12/15) | Stage 4: Purchasability | **Hypothesis** |
| Fit/Size | 14 (4.5%) | 42.9% | Reddit only (5/5) | Stage 3: Evaluation | **Hypothesis** |
| Intent/Bookmarking | 13 (4.2%) | 0.0% | All | Stage 1: Intent | Behavioural signal |
| Styling/Occasion | 11 (3.5%) | 0.0% | YouTube | Stage 3: Evaluation | **Hypothesis** |
| Social Validation | 6 (1.9%) | 0.0% | YouTube | Stage 3: Evaluation | Weak signal |
| Comparison | 5 (1.6%) | 0.0% | All | Stage 3: Decision | Weak signal |
| Forgetting | 5 (1.6%) | 0.0% | All | Stage 2: Retention | Weak signal |
| Alternatives | 4 (1.3%) | 0.0% | Reddit | Stage 2: Retention | Weak signal |

**Critical insight from Arindam's feedback:**

> These AI findings are **hypotheses that require human validation**, not absolute facts. The engine assists research — it does not replace the PM's thinking. (NextLeap Zero-Tolerance Rule #1)

### Key Discovery the Engine Surfaced

**"Price" is NOT necessarily the real problem.** Even though Price has 33 mentions, its negativity rate is only 36.4%. Many price mentions are neutral comparisons. Meanwhile, **Returns (31 mentions, 93.5% negative)** is far more emotionally toxic per-mention. And **Quality (44 mentions, 6.8% negative)** is the highest-volume theme but its friction is diffuse *uncertainty*, not acute anger.

This distinction — high volume ≠ high severity — is exactly the kind of nuance the engine reveals that a simple "what's mentioned most?" approach would miss.

---

## Phase 3 — The Critical Transition: Discovery → Primary Research

This is where most decks become weak. They do:

> AI says X → survey says X → therefore X is the problem.

We must do something more intellectually honest.

### Example: "Price is the largest theme" does NOT mean "Price is the problem"

Price could mean:
- Genuinely unaffordable
- Waiting for a specific sale event
- Uncertain whether price is fair for the quality
- Comparing with AJIO/Amazon Fashion
- Purchase isn't urgent enough to justify the price
- Wants to spend money elsewhere this month

**These are different problems with different solutions.**

### Example: "Quality doubt" does NOT automatically mean "show more photos"

Quality doubt could mean:
- Doesn't trust heavily edited model photos
- Material looks different in real life
- Brand is unknown → no quality baseline
- No verified buyer photos exist
- Previous bad experience → generalised distrust

**The interviews must discover WHICH specific sub-problem is driving the friction.**

### Interview Framework (12 Respondents Completed)

| Case | Respondents | What We Learned |
|---|---|---|
| High-intent stalled users | Rishika, Aastha, Nandini, Sia | Confidence is the blocker — they pay MORE for trust |
| Price-led delayers | Aziz, Stuti | Aziz: pure price. Stuti: self-regulation, not inability |
| Fit/uncertainty-led hesitators | Tanej, Prakhar | Tanej: XL vs XXL. Prakhar: styling/versatility doubt |
| Availability-frustrated users | Yaakrati | Boots went out of stock during comparison — lost sale |
| Heavy external researchers | Nandini, Himanshi | Nandini: checks if images are real. Himanshi: zero tolerance for unreviewed |
| Brand-trust substituters | Umesh, Yaakrati, Aziz | Brand replaces reviews entirely for this segment |
| Platform-loyal users | Stuti | Myntra-loyal — doesn't compare cross-platform |
| Offline-preferring | Steve | Physical retail competes with e-commerce |

### Interview Protocol (Actual — Rapid-Fire Format)

1. "Think about the last fashion item you saved or wishlisted but didn't buy immediately. Why?"
2. "Have you ever bought something more expensive just because it had better reviews or buyer photos?"
3. "If a product has zero reviews, would you still buy it? What if the seller’s other products have great reviews?"
4. "Do you check anywhere else before deciding — another app, website, social media?"
5. "What information, if any, would make you more confident about buying?"
6. "Any feature you’d want added to the wishlist page?"

### The Confidence Gap Paradox (Key Interview Discovery)

The critical transition from AI → Survey → Interviews:

```
AI ENGINE:     Quality is the #1 theme (14.1%). Price is #2 (10.5%).
                → Hypothesis: Quality doubt is the root cause.

SURVEY:        Price is actually #1 (44%). Comparison is #2 (36%).
                → Hypothesis refined: Price is the biggest barrier.

INTERVIEWS:    11/12 users PAY MORE for confidence signals.
                → Discovery: Price is the STATED barrier;
                   confidence is the ACTUAL decision lever.
```

This is the anti-assumption story Arindam’s framework demands.

---

## Phase 4 — Segment (Derived from Behaviour, NOT Demographics)

**Per Arindam's feedback:** Do NOT create "Priya, 24, Bengaluru" personas. Derive segments behaviourally.

**Updated segments (post-interview, behaviour-derived):**

| Segment | Observable Behaviour | Interview Evidence | Size |
|---|---|---|---|
| **A. Confidence-arbitrage buyers** | Compare confidence levels across platforms; pay more for trust | Rishika, Aastha, Nandini, Sia, Umesh, Tanej, Steve, Himanshi, Prakhar, Stuti, Yaakrati | 11/12 |
| **B. Brand-trust-substituters** | Brand replaces reviews as confidence signal | Aziz, Umesh, Yaakrati | 3/12 |
| **C. Styling/versatility doubters** | "Will this go with my wardrobe?" — distinct from fit/quality | Prakhar | 1/12 |
| **D. Wishlist self-regulators** | Deliberately delay as financial cooling-off | Stuti | 1/12 |
| **E. Availability-blocked** | Item went out of stock during comparison delay | Yaakrati, Aastha | 2/12 |
| **F. Price-led cross-platform** | Pure price comparison drives decisions | Aziz | 1/12 |

**Note:** These segments overlap — most users exhibit multiple behaviours. The dominant pattern (Confidence-arbitrage, 11/12) is the target.

Chosen segment based on:

> **Meaningful population (11/12) × Strong pain (can't decide) × High intent (still want item) × Metric leverage (42% leak) × Solvability (no monetary incentives needed)**

---

## Phase 5 — Root Cause (The 5 Whys — Updated with Interview Evidence)

### The Chain (validated across AI Engine + Survey + 12 Interviews)

```
WHY 1: Why do wishlisted items sit unconverted?
  → Users feel uncertain about the purchase outcome.
  EVIDENCE: 56% still want the item; 33% actively evaluating (Survey)
  EVIDENCE: Prakhar — revisits every 20-30 days, same uncertainty each time

WHY 2: Why are they uncertain?
  → The product page doesn't give them enough real-world evidence to decide.
  EVIDENCE: Aastha — "Model pics से बिल्कुल ही अलग आता है"
  EVIDENCE: Steve — "They never look exactly the way shown in the picture"
  EVIDENCE: 11/12 prefer buyer photos over model pics

WHY 3: Why is the evidence insufficient?
  → Model photos are edited, reviews are sparse or absent, no verified
    buyer photos exist. Some products have ZERO reviews.
  EVIDENCE: 9/12 won't buy without reviews
  EVIDENCE: Himanshi — "ये तो देखना ही पड़ता है" (no exceptions)
  EVIDENCE: Tanej — "बिना reviews को confirm नहीं होता"

WHY 4: Why don't they just order and return if wrong?
  → Return process is seen as hassle, not solution.
  EVIDENCE: Prakhar — "That's like lots of hassle, like time"
  EVIDENCE: Aastha — "I find it very suspicious if they don't offer return option"
  COUNTER: Yaakrati uses return as safety net for unknown products

WHY 5: So what do they actually do?
  → Leave the app to compare on Amazon, AJIO, Instagram, YouTube, brand websites.
    During this journey, 42% buy from competitors.
  EVIDENCE: 11/12 compare cross-platform
  EVIDENCE: Aastha — bought same top from Amazon at HIGHER price for reviews
  EVIDENCE: Nandini — checks if product images are real or copied
```

**Root Cause Statement (Post-Interview):**

> Myntra captures purchase intent at the wishlist stage but provides insufficient real-world evidence (verified buyer photos, fit consensus, quality proof) on the product page. This forces users to comparison-shop on competing platforms — where they compare CONFIDENCE LEVELS, not just prices — creating competitor leakage. 11/12 users have paid MORE for products with better confidence signals, proving that the solvable barrier is information asymmetry, not price sensitivity.

This aligns with Arindam's feedback AND extends it: the root cause is not just quality doubt — it's the broader **Confidence Gap Paradox** where price is the stated barrier but confidence is the actual lever.

---

## Phase 6 — Problem Definition (Customer-Centred)

Format from Arindam's rules — **friction-based, not persona-based:**

> Among **[behavioural segment]** who add items to their Myntra wishlist, users who **[specific behaviour]** delay purchasing because **[validated root cause]**. They currently **[workaround]**, which **[consequence for user and for Myntra]**.

### Final Problem Definition (Post-Interview):

> Among **confidence-arbitrage buyers** (11/12 interview respondents) who save fashion items to their wishlist and still want them (56% of wishlisters), users who **cannot verify product quality, fit, or styling compatibility from the product page** delay purchasing because **model photos don't match reality, reviews are sparse or absent, and there is no verified buyer evidence**. They currently **compare the same product's reviews, photos, and trust signals across 2–3 competing platforms** (11/12 do this), which **delays their decision by days or weeks and causes 42% to buy from competitors**. Even users who cite price as their primary barrier will **pay 20–30% more when confidence signals are present** (11/12 confirmed), revealing that the solvable root cause is **information asymmetry, not price sensitivity**.

### What Changed from the Draft:
- "High-intent users" → **"Confidence-arbitrage buyers"** (behaviour-derived from interviews)
- "Lack sufficient evidence of quality" → **"Cannot verify quality, fit, or styling compatibility"** (Prakhar added styling; Tanej added fit)
- "Search YouTube/Reddit" → **"Compare across 2–3 competing platforms"** (interviews showed cross-platform comparison is more common than YouTube)
- Added the paradox: **"Even price-sensitive users pay more for confidence"** — this is the key discovery

---

## Phase 7 — Ideation (4–6 Genuinely Different Mechanisms)

NOT "Feature A, Feature A with AI, Feature A with chatbot." Actual different mechanisms:

| # | Mechanism Type | Example | Addresses |
|---|---|---|---|
| 1 | **Decision-support** | AI Confidence Score on each wishlisted item (quality + fit + return clarity) | Quality uncertainty |
| 2 | **Information enrichment** | Verified buyer photos + AI-summarised review highlights | Review gap |
| 3 | **Social proof** | "X people bought this from their wishlist this week" | Social validation |
| 4 | **Risk reduction** | Category-specific return guarantee badges (prominently on wishlist page) | Return anxiety |
| 5 | **Timing/nudge** | Smart wishlist reminders when price drops or stock changes | Forgetting + price |
| 6 | **Comparison simplification** | Side-by-side comparison tool for wishlisted items | Comparison friction |

### Three-Level Creativity Test (from Arindam's feedback)

Each solution MUST pass:

| Level | Test | Question |
|---|---|---|
| **1. Problem Fit** | Does it solve the validated root cause? | Does this directly address the information asymmetry? |
| **2. Differentiation** | Is this meaningfully different from what Myntra/competitors already do? | Does AJIO or Amazon Fashion already do this? |
| **3. Defensibility** | Why is this difficult to copy? | Does it create proprietary data, network effects, or a structural moat? |

---

## Phase 8 — MVP (Proves the Mechanism)

> **MVP ≠ "I built an AI app."**
>
> MVP = "Can I demonstrate that this intervention changes the behaviour we're trying to change?"

If the problem is decision uncertainty, the MVP should let someone experience the **decision-resolution moment**. Not build all of Myntra.

### MVP Checklist
- [ ] Deployed to production (per project.md: "Must be deployed so it can be interacted with and tested")
- [ ] Demonstrates the core mechanism
- [ ] Fits into the existing user journey
- [ ] Can be tested by the evaluator
- [ ] Shows architecture + user flow + fallback behaviour

---

## Phase 9 — Measurement (Causal Chain)

### North Star
**30-day Wishlist → Purchase Conversion Rate**

↓

### Solution Metric
The behaviour our solution directly changes (e.g., "% of users who view the Confidence Score and then move item to cart")

↓

### Leading Indicators
Does the mechanism actually fire? (e.g., Confidence Score view rate, buyer photo engagement)

↓

### Lagging Indicators
Does the behaviour persist? (e.g., 7-day repeat conversion, wishlist-to-cart velocity)

↓

### Guardrails (MUST NOT get worse)
- Core purchase conversion rate
- Average order value
- Wishlist addition rate (don't accidentally discourage wishlisting)
- Return rate (if we reduce uncertainty, returns should not increase)

---

## Phase 10 — Risks & Experiment Design

### Risk Framework

| Risk | Why It Could Fail | Mitigation |
|---|---|---|
| **Wrong root cause** | Primary research may disconfirm quality as the key blocker | Run A/B test before full rollout; kill feature if leading metrics don't move in 14 days |
| **AI-generated content errors** | Confidence scores or summaries could be wrong | Deterministic rules over LLM guesses; confidence thresholds; human review queue |
| **User distrust** | New UI elements may feel intrusive or spammy | Opt-in first; test with power users; gradual rollout |
| **Cannibalisation** | Solution may shift purchases from non-wishlist to wishlist flow without net new purchases | Track total purchase volume as guardrail, not just wishlist conversion |

### Experiment Design

- **Phase 1 (Days 0–14):** Shadow mode — show to 5% of users, measure engagement
- **Phase 2 (Days 15–30):** A/B test — 50/50 split on wishlist page, measure conversion lift
- **Phase 3 (Days 31–60):** Scale to 100% if conversion lift ≥ X% with no guardrail violations

---

## The 10-Slide Architecture

| Slide | Job | Key Message (Title = Takeaway) |
|---|---|---|
| **1** | Business problem | "Myntra's biggest untapped growth lever is the 70%+ of wishlisted items that never convert" |
| **2** | Metric decomposition | "The wishlist-to-purchase journey breaks at 5 stages — Stage 3 (Confidence) has the highest friction" |
| **3** | AI Discovery Engine | "We built an engine that analysed 1,367 reviews and identified 12 friction themes as hypotheses" |
| **4** | Evidence: competing opportunities | "Quality doubt (14.1%), Return fear (9.9%), and Price (10.5%) are the top 3 — but severity ≠ frequency" |
| **5** | Primary research | "5 interviews confirmed that [X] — and disconfirmed our assumption about [Y]" |
| **6** | Validated segment + root cause | "The core problem: information asymmetry creates perceived risk that makes wishlists stagnate" |
| **7** | Solution alternatives + why one wins | "We evaluated 6 mechanisms — [Winner] scores highest on Impact × Reach × Confidence × Effort" |
| **8** | MVP: how it works in the real journey | Live demo + screenshots + architecture |
| **9** | Measurement: North Star → guardrails | Causal chain from solution metric to business metric |
| **10** | Risks + experiment + what's next | "Here's how we'd be wrong, and here's the 60-day experiment to find out" |

**The key difference:** Slides 3–6 tell an **evidence story**, not a research summary. The disconfirmation IS the credibility.

---

## Anti-Patterns to Avoid (from Arindam's Feedback)

| ❌ Don't Do This | ✅ Do This Instead |
|---|---|
| "Our target is Priya, 24, Bengaluru" | Derive segments from observed behaviour |
| "AI found that quality is the #1 issue → let's fix quality" | AI found quality is a hypothesis → interviews confirmed/rejected it |
| "Here's our feature" (slide 2) | Problem framing comes before solution (slide 7+) |
| Copy-paste AI summaries into slides | Use AI as input; all analysis and decisions are human-authored |
| RICE table because other decks have one | Prioritise IF it makes sense for your choices |
| "I had an idea → research agreed → I built it" | "We investigated without assuming → evidence changed us" |

---

## Presentation Constraints (from project.md)

- **No Fellow name** anywhere in the slide deck
- **10 slides max** (title slide counts)
- Slide title = **key message** (not "Problem" — instead: "Users shop by mission, not category")
- Text readable on background colors
- Color-blind-friendly colors
- Link supporting artifacts via hyperlinks
- **Max file size:** < 40 MB
- **Naming:** `NL Myntra`
- **Min font size:** 14 (Google Slides/PPT), 26 (Figma 1920×1080), 22 (Canva 1920×1080)
