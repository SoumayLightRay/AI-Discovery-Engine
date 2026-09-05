# Product Manager Fellowship — Graduation Project (Aug 2026)

> **Submission Deadline: September 5, 2026, 3:59:00 PM IST**
> No submissions accepted after deadline, even by a few seconds.

---

## Product Chosen: **Myntra**

## Role: Product Manager, Growth Team

---

## Context

Millions of users browse fashion products, save items they like, and add products to their wishlists. A wishlist represents a particularly interesting signal: the user has expressed explicit interest in an item but has stopped short of purchasing it.

Over time, users can accumulate dozens—or even hundreds—of wishlisted products, while only a small proportion eventually translate into purchases.

**Strategic Goal:**
> Increase the percentage of users who purchase at least one item from their wishlist within 30 days of adding it.

Improving wishlist-to-purchase conversion could increase purchase frequency, improve monetization from existing users, and help the company extract greater value from high-intent demand already present on the platform.

**Key Constraints:**
- You are **NOT** given the underlying user problem — your task is to **discover** it.
- You **CANNOT** offer monetary incentives to users.

---

## Part 1: Build an AI-Powered Discovery Engine

Build an AI-powered system that analyzes user feedback at scale.

**AI Stack Options:** Claude, GPTs, Agents, Workflows, n8n, Zapier, Perplexity, or any AI-native stack.

**Data Sources:**
- App Store reviews
- Play Store reviews
- Reddit discussions
- Fashion and shopping communities
- Social media conversations
- YouTube comments
- Product reviews and Q&A
- Other publicly available conversations about online fashion shopping

**Research Questions the Engine Must Answer:**
1. Why do users add fashion products to their wishlist?
2. What prevents wishlisted products from eventually being purchased?
3. What uncertainties remain after users have identified a product they like?
4. What causes users to postpone a purchase?
5. How do users compare multiple shortlisted products?
6. What information do users seek outside Myntra/AJIO before purchasing?
7. What role do fit, size, styling, price, reviews, occasion and social validation play?
8. When do users use the wishlist as genuine purchase intent versus simply as a bookmarking mechanism?
9. How do these behaviors differ across user segments?
10. What unmet needs emerge consistently across user conversations?

**Requirements:**
- Go beyond summarizing reviews or performing sentiment analysis.
- Identify, quantify where possible, and compare potential opportunity areas that could influence the stated business metric.

---

## Part 2: Break Down the Business Metric

Break down: **Wishlist → Purchase Conversion**

Into the relevant product outcomes and user behaviors that could influence it.

- Think carefully about what needs to change for the business metric to improve.
- Use metric decomposition alongside the output of the AI discovery engine to determine where the highest-potential opportunities lie.

---

## Part 3: Validate the Opportunity Through User Research

AI-generated insights are only a starting point.

1. Choose a target user segment and opportunity area based on initial analysis.
2. Conduct **5–6 user interviews** with respondents belonging to the chosen segment.

**Understand:**
- Why they saved each item
- Whether they still intend to purchase it
- What is stopping them
- What would make them purchase it
- What information they still need
- Whether they are considering alternatives
- What happens outside the app before they decide
- How they currently overcome uncertainty

---

## Part 4: Define the Problem

Based on discovery and primary research, clearly articulate:
- The target user segment
- The product outcome you intend to influence
- The root cause preventing the desired behavior
- Existing user workarounds
- Why solving the problem creates meaningful user value
- Why solving the problem makes business sense

**Show how thinking evolved across:**
> Business Metric → Product Outcomes → AI Discovery → Primary Research → Problem Definition

---

## Part 5: Build an MVP

Design and build a functional MVP addressing the identified problem.

**May take the form of:**
- A feature within Myntra/AJIO
- An AI-powered workflow
- An AI agent
- A standalone experience connected to the shopping journey

**Must be deployed to production** so it can be interacted with and tested.

---

## Part 6: Define Success

- Start with the business metric
- Define the metrics the solution would influence
- Leading indicators, guardrail metrics
- Definition of each metric and rationale for choosing them

---

## Part 7: Risks & Mitigation Steps

- Why the solution might fail
- Most important risks for the specific solution
- Proposed mitigation plans

---

## Deliverables

### 1. [Link] AI Discovery Engine
- Link where the workflow can be tested
- A 1-slider within the final deck explaining how it works

### 2. [PDF] 10-Slide Deck
1. Business metric decomposition
2. Discovery engine findings
3. Primary research
4. Problem definition
5. Solution rationale
6. MVP
7. Success metrics
8. Risks and mitigation

### 3. [Link] Deployed MVP
- A publicly accessible prototype, workflow, or agent that can be tested

---

## Deck Guidelines

- **No Fellow name** anywhere in the slide deck
- **10 slides max** (title slide counts within 10)
- Slide title = **key message** of the slide (not just "Problem")
- Ensure text is readable on background colors
- Use color-blind-friendly colors
- Link supporting artifacts via hyperlinks (ensure reader has access)
- **Max file size:** < 40 MB
- **Naming:** e.g., `NL Myntra`
- **Min font size:** 14 (Google Slides / PPT), 26 (Figma 1920×1080), 22 (Canva 1920×1080)

---

## Our Live Deliverable Links

| Deliverable | Link | Status |
|---|---|---|
| **AI Discovery Engine** | [https://ai-discovery-engine-rose.vercel.app/](https://ai-discovery-engine-rose.vercel.app/) | ✅ Live |
| **Source Code** | [https://github.com/SoumayLightRay/AI-Discovery-Engine](https://github.com/SoumayLightRay/AI-Discovery-Engine) | ✅ Live |
| **Backend API** | [https://discovery-engine-api-mk0d.onrender.com](https://discovery-engine-api-mk0d.onrender.com) | ✅ Live |
| **Deployed MVP** | [https://ai-discovery-engine-rose.vercel.app/wishlist_mvp.html](https://ai-discovery-engine-rose.vercel.app/wishlist_mvp.html) | ✅ Live |
| **10-Slide Deck** | _To be created in Canva_ | ⬜ Pending |
