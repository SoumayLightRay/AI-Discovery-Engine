# Arindam Mukherjee Feedback & NextLeap Grading Blueprint

*Source: Graduation Project Feedback Call (August 21, 2026) led by Arindam Mukherjee (Head of Product).*

---

## 1. Evaluation Context & Blind Scoring Rules
- **Triple-Blind Evaluation:** Submissions are scored independently by three mentors. All personal identifiers (names, emails, LinkedIn links) must be completely redacted.
- **Grading Threshold:** 15 parameters grouped into 4 categories. An aggregate normalized score **≥ 70%** earns "Top Fellow" honors.
- **Zero-Tolerance Red Flags (Score = 0):**
  1. *Uncritical AI Generation:* Submitting generic, hallucinated, or unedited AI outputs with no original human thinking.
  2. *Plagiarism or Template Copying:* Direct reproduction of common framework templates without contextual customization.
  3. *Failure to follow presentation constraints:* Font size below minimums, broken links, unreadable wireframes.

---

## 2. Core Feedback: "The Anti-Assumption Mandate"

Arindam specifically emphasized that the #1 reason fellow submissions fail is **making assumptions instead of grounding conclusions in primary evidence**:

### Rule 1: No Pre-Determined Personas or Demographic Stereotyping
- **The Mistake:** Stating *"Our target user is Priya, 24, living in Bengaluru, shopping on weekends"* without any empirical data proving this demographic is the one facing the drop-off.
- **The Correct Approach:** Derive user archetypes **behaviorally from the data**:
  - What was the user trying to accomplish?
  - Where in the journey did they abandon?
  - What is the friction trigger?

### Rule 2: Root Cause Analysis ("5 Whys") vs. Symptom Treating
- **The Mistake:** Seeing "wishlist items are not bought" and jumping immediately to *"Let's add an AI outfit generator or discount notification!"* (Solution-first thinking).
- **The Correct Approach:** Ask "Why?" at least 3-5 times to uncover the psychological barrier:
  - *Why do users abandon?* Because they aren't confident the dress will look good on them.
  - *Why aren't they confident?* Because model photos are heavily edited and size charts are inconsistent across brands.
  - *Why don't they just order and return?* Because Myntra added return pickup convenience fees and return windows are stressful.
  - *Root Cause:* Low upfront certainty creates high downstream perceived risk.

### Rule 3: The Three-Level Creativity Framework
When proposing solutions based on discovered themes:
1. **Level 1 (Table Stakes):** Does the feature directly solve the user friction?
2. **Level 2 (Differentiation):** Is the UX or mechanism novel compared to competitors (e.g., Meesho, Ajio, Amazon)?
3. **Level 3 (Defensibility / Moat):** Does it create network effects, proprietary data assets, or a structural barrier that cannot be cloned overnight?

---

## 3. Strict AI Tooling Guardrails

| Permitted AI Usage (The "Discovery Engine") | Strictly Prohibited AI Usage |
| :--- | :--- |
| ✅ Scraping public community reviews & comments | ❌ Asking AI to "invent" user pain points |
| ✅ Deduplication, PII stripping, text cleaning | ❌ Relying on AI for problem selection |
| ✅ First-pass thematic clustering & quote extraction | ❌ Letting AI decide product roadmap bets |
| ✅ Drafting interview probing questions | ❌ Copy-pasting AI summaries into final decks |

---

## 4. Strict Data-Driven Segmentation (Friction-Based, Not Persona-Based)

*Crucial Correction:* We cannot invent user personas (like "The Passive Hoarder" or "The Cautious Shopper") because we cannot observe user intent or emotional state from app reviews. We can only observe **what they explicitly complain about**. 

Therefore, we segment the **Friction Points (The Problems)**, not the users. Based on the 1,367 reviews, the drop-off friction falls into these strictly observable categories:

1. **Late-Stage Pricing Friction (Checkout Blockers)**
   - *Observable Data:* Users explicitly state they abandoned the cart at the final step due to added charges.
   - *Verbatim Evidence Examples:* Complaints about "Platform Fee," "Convenience Fee," "Delivery Surge," or prices changing between the wishlist and the cart.
2. **Pre-Purchase Confidence Friction (Product Representation)**
   - *Observable Data:* Users express inability to choose a product.
   - *Verbatim Evidence Examples:* "Size chart is completely wrong for this brand," "Material looks different in real life," "No reviews with photos to check the real fit."
3. **Post-Purchase Risk Friction (Return Policy Anxiety)**
   - *Observable Data:* Users explicitly state they are afraid to order because of return issues.
   - *Verbatim Evidence Examples:* "Return pickup was rejected," "Takes 15 days to get a refund," "Charged me for returning the item."
4. **Technical / UI Friction (App Mechanics)**
   - *Observable Data:* Bug reports preventing conversion.
   - *Verbatim Evidence Examples:* "Wishlist disappeared," "App crashes on payment page," "OTP not coming."

By segmenting the *problems* rather than assuming *user archetypes*, we remain 100% grounded in primary evidence and avoid AI-generated persona hallucinations.
