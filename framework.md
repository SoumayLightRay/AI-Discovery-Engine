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

### Interview Framework (5–6 Respondents for Contrast)

| Case | Why This Case | What We Learn |
|---|---|---|
| High-intent stalled user | Core target candidate | What specific blocker stops purchase? |
| Price-led delayer | Understand constraint | Is this solvable without incentives? |
| Fit/uncertainty-led hesitator | Understand confidence gap | What information would resolve it? |
| Availability-frustrated user | Test product constraint | Is this a PM problem or logistics? |
| Heavy external researcher | Understand workaround | What does Myntra lack that YouTube/Reddit provides? |
| Successful converter | Learn what actually worked | What tipped them from wishlist → purchase? |

### Interview Protocol

For each respondent:
1. "Show me your Myntra wishlist right now. Pick 3 items."
2. For each: "Why did you save this? Do you still want it? What's stopping you?"
3. "Walk me through the last time you moved something from wishlist to cart. What changed?"
4. "Have you ever decided NOT to buy something specifically because of the return policy?"
5. "When you research a Myntra product on YouTube or Reddit, what are you looking for that isn't on the product page?"
6. "How do you decide between Myntra vs. AJIO vs. Amazon for the same type of product?"

---

## Phase 4 — Segment (Derived from Behaviour, NOT Demographics)

**Per Arindam's feedback:** Do NOT create "Priya, 24, Bengaluru" personas. Derive segments behaviourally.

**Per our data, candidate segments:**

| Segment | Observable Behaviour | Data Signal |
|---|---|---|
| **A. Genuine high-intent stalled** | Wishlisted recently, revisited, haven't purchased, specific unresolved blocker | Quality + Returns + Fit themes |
| **B. Passive bookmarkers** | Large wishlist, rarely revisit, no real purchase intent | Intent/Bookmarking (4.2%, 0% negativity) |
| **C. Deal-timers** | Wishlisted to wait for price drop, explicitly monitoring | Price theme (10.5%) — "none of my wishlist items got discounts" |
| **D. Comparison shoppers** | Wishlist as cross-platform comparison tool | Comparison + Alternatives themes |
| **E. Availability-constrained** | Want item, can't purchase because size/stock unavailable | Availability (5.4%, 88.2% negative) |

Choose ONE based on:

> **Meaningful population × Strong pain × High intent × Metric leverage × Solvability (without monetary incentives)**

---

## Phase 5 — Root Cause (The 5 Whys)

### The Chain (from our data)

```
SYMPTOM
  Wishlist items aren't being purchased within 30 days.
    ↓
BEHAVIOUR
  User saves product but delays or abandons purchase.
    ↓
IMMEDIATE REASON (Why 1)
  "I'm not sure whether the quality/fit/return will be acceptable."
    ↓
DEEPER REASON (Why 2)
  "The product page doesn't give me enough real evidence to decide."
    ↓
ROOT CAUSE (Why 3)
  "Model photos are heavily edited, size charts are inconsistent across brands,
   and I can't see what real buyers received."
    ↓
COMPOUNDING FACTOR (Why 4)
  "Even if I order and it's wrong, the return process is stressful and unreliable."
    ↓
CONSEQUENCE (Why 5)
  "So I keep it in my wishlist as a safety net, procrastinate, and eventually
   forget or find it on another platform."
```

**Root Cause Statement:**

> Low upfront certainty creates high downstream perceived risk. The information asymmetry between what the product page shows and what the user actually receives is the fundamental driver of wishlist stagnation.

This aligns directly with Arindam's feedback: *"Why aren't they confident? Because model photos are heavily edited and size charts are inconsistent across brands."*

---

## Phase 6 — Problem Definition (Customer-Centred)

Format from Arindam's rules — **friction-based, not persona-based:**

> Among **[behavioural segment]** who add items to their Myntra wishlist, users who **[specific behaviour]** delay purchasing because **[validated root cause]**. They currently **[workaround]**, which **[consequence for user and for Myntra]**.

### Our Draft (to be refined after interviews):

> Among **high-intent users who add items to their wishlist and revisit them**, users who **lack sufficient evidence of real product quality** delay purchasing because **heavily edited product imagery and inconsistent size charts create uncertainty about what they will actually receive**. They currently **search YouTube hauls and Reddit threads for honest reviews**, which **delays their decision and increases the chance of finding alternatives on competing platforms**.

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
