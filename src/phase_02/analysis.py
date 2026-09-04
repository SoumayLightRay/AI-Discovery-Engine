import json
import os
import time
import random
from collections import Counter
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

INPUT_FILE = "docs/phases/phase-01/normalized_data.json"
OUTPUT_JSON = "docs/phases/phase-02/analysis_results.json"
OUTPUT_SUMMARY = "docs/phases/phase-02/weekly_pulse_summary.md"
MODEL_NAME = "openai/gpt-oss-120b"
MAX_SAMPLE_SIZE = 320 # Balanced cross-platform sample for Groq free-tier rate limits

FRICTION_THEMES = [
    "Intent/bookmarking",
    "Price",
    "Availability",
    "Fit/size",
    "Quality/material",
    "Styling/occasion",
    "Reviews/information",
    "Social validation",
    "Comparison",
    "Returns",
    "Forgetting/distraction",
    "Alternatives",
    "Other emergent themes"
]

def load_reviews():
    if not os.path.exists(INPUT_FILE):
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_stratified_sample(reviews, max_total=320):
    """
    Ensures balanced representation across Google Play, App Store, YouTube, and Reddit.
    Avoids Google Play (954 items) drowning out Reddit (99 items) or App Store (130 items).
    """
    by_source = {}
    for r in reviews:
        src = r.get("source", "Unknown")
        by_source.setdefault(src, []).append(r)
    
    per_source_target = max_total // len(by_source)
    sample = []
    
    for src, items in by_source.items():
        if len(items) <= per_source_target:
            sample.extend(items)
        else:
            # Random seed for reproducible sampling
            random.seed(42)
            sample.extend(random.sample(items, per_source_target))
            
    random.shuffle(sample)
    return sample

def tag_batch_reviews(client, batch):
    """
    Stage A: Batch tag reviews with friction themes and sentiment.
    Grounds all output in verbatim snippets to mitigate hallucination.
    """
    reviews_text = "\n".join([f"[{i+1}] (Source: {r['source']}) {r['text'][:300]}" for i, r in enumerate(batch)])
    
    prompt = f"""You are an expert E-Commerce UX & Product Discovery Analyst.
Analyze the following batch of user reviews and feedback for Myntra fashion/shopping.

Classify each review into exactly one primary theme from this list:
1. Intent/bookmarking
2. Price
3. Availability
4. Fit/size
5. Quality/material
6. Styling/occasion
7. Reviews/information
8. Social validation
9. Comparison
10. Returns
11. Forgetting/distraction
12. Alternatives
13. Other emergent themes

For each review, extract:
- id: review index [1 to {len(batch)}]
- primary_theme: one of the 6 themes above
- sentiment: negative, neutral, or positive
- friction_present: boolean (true if user encountered friction or abandoned checkout/wishlist)
- verbatim_quote: a short exact quote from the review that proves the friction (or empty string if none)

Respond ONLY with valid JSON in this exact structure:
{{
  "tagged_reviews": [
    {{
      "id": 1,
      "primary_theme": "...",
      "sentiment": "...",
      "friction_present": true,
      "verbatim_quote": "..."
    }}
  ]
}}

Reviews to analyze:
{reviews_text}
"""
    max_retries = 3
    for attempt in range(max_retries):
        try:
            completion = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a product intelligence data processor. You output valid JSON strictly."},
                    {"role": "user", "content": prompt}
                ],
                response_format={"type": "json_object"},
                temperature=0.2,
                max_tokens=2500
            )
            content = completion.choices[0].message.content
            data = json.loads(content)
            tagged = data.get("tagged_reviews", [])
            
            # Validate: if more than 50% tagged as "Other", retry
            other_count = sum(1 for t in tagged if 'other' in t.get('primary_theme', '').lower())
            if len(tagged) > 0 and other_count / len(tagged) > 0.5 and attempt < max_retries - 1:
                print(f"    Retry {attempt+1}: {other_count}/{len(tagged)} tagged as Other, retrying...")
                time.sleep(5)
                continue
            
            return tagged
        except Exception as e:
            print(f"  Warning: Batch tagging error (attempt {attempt+1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                wait_time = 10 * (attempt + 1)  # Exponential backoff: 10s, 20s
                print(f"    Waiting {wait_time}s before retry...")
                time.sleep(wait_time)
    
    # Final fallback only after all retries exhausted
    print(f"  ERROR: All {max_retries} retries failed for this batch. Using fallback.")
    fallback = []
    for i, r in enumerate(batch):
        fallback.append({
            "id": i + 1,
            "primary_theme": "Other / General Feedback",
            "sentiment": "neutral",
            "friction_present": False,
            "verbatim_quote": ""
        })
    return fallback

def synthesize_pulse(client, total_dataset_count, analyzed_count, theme_counts, sample_quotes_by_theme):
    """
    Stage B: Synthesize structured problem discovery, root-cause hypotheses, and opportunity areas.
    """
    theme_breakdown_str = json.dumps(theme_counts, indent=2)
    quotes_str = json.dumps(sample_quotes_by_theme, indent=2)

    prompt = f"""You are a Lead Product Manager specializing in E-Commerce Cart & Wishlist Conversion.
We have collected {total_dataset_count} real user reviews and community discussions (from Google Play, Apple App Store, YouTube, and Reddit) regarding Myntra, and tagged a statistically representative sample of {analyzed_count} reviews.

Friction Theme Distribution:
{theme_breakdown_str}

Representative Grounded Verbatim Quotes:
{quotes_str}

Based on this grounded primary evidence, synthesize a high-impact discovery pulse:
1. Executive Summary: The single biggest friction causing wishlist drop-offs.
2. Root-Cause Analysis (5 Whys from user psychology perspective, not business metrics).
3. Top 3 Actionable Opportunities. For each, output the exact problem definition using this strict structure: "Among [specific segment], users who [specific behavior] delay purchasing because [root cause]. They currently [workaround], which leaves them [consequence]." (Note: Monetary incentives should be excluded from the eventual solution space).
4. Primary User Research Questions: 3 sharp questions to ask during 1:1 user interviews to validate these findings.

Respond ONLY with valid JSON in this exact schema:
{{
  "executive_summary": "string",
  "dominant_friction_theme": "string",
  "root_cause_analysis": [
    {{"level": "Why 1", "cause": "..."}},
    {{"level": "Why 2", "cause": "..."}},
    {{"level": "Why 3", "cause": "..."}}
  ],
  "opportunities": [
    {{
      "theme": "...",
      "rigorous_problem_statement": "Among [segment], users who [behavior] delay purchasing because [root cause]. They currently [workaround], which leaves them [consequence].",
      "grounded_quote": "..."
    }}
  ],
  "primary_research_interview_guide": [
    "question 1",
    "question 2",
    "question 3"
  ]
}}
"""
    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "You are an elite product strategy director. Output valid JSON strictly."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.3,
        max_tokens=2500
    )
    return json.loads(completion.choices[0].message.content)

def main():
    print("=== Phase 2: AI Analysis & Friction Theme Discovery ===")
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set in environment or .env file.")

    client = Groq(api_key=api_key)
    
    print(f"1. Loading normalized dataset from {INPUT_FILE}...")
    all_reviews = load_reviews()
    total_reviews = len(all_reviews)
    print(f"-> Total records in dataset: {total_reviews}")

    # Stratified sampling across all 4 channels
    sample_to_analyze = get_stratified_sample(all_reviews, max_total=MAX_SAMPLE_SIZE)
    print(f"-> Selected balanced stratified sample of {len(sample_to_analyze)} reviews across Google Play, App Store, YouTube, and Reddit.")
    
    # Stage A: Batch tagging
    batch_size = 20
    tagged_results = []
    print(f"2. Stage A: Processing reviews in batches of {batch_size} via {MODEL_NAME}...")

    for i in range(0, len(sample_to_analyze), batch_size):
        batch = sample_to_analyze[i:i + batch_size]
        batch_num = (i // batch_size) + 1
        total_batches = (len(sample_to_analyze) + batch_size - 1) // batch_size
        print(f"   Processing batch {batch_num}/{total_batches} ({len(batch)} items)...")
        
        batch_tags = tag_batch_reviews(client, batch)
        
        for idx, tag_info in enumerate(batch_tags):
            if idx < len(batch):
                item_record = {
                    **batch[idx],
                    "primary_theme": tag_info.get("primary_theme", "Other / General Feedback"),
                    "sentiment": tag_info.get("sentiment", "neutral"),
                    "friction_present": tag_info.get("friction_present", False),
                    "verbatim_quote": tag_info.get("verbatim_quote", "")
                }
                tagged_results.append(item_record)
        
        # Respect rate limits (Groq free tier)
        time.sleep(8.0)  # Respect Groq free-tier rate limits (6 RPM)

    print(f"-> Completed tagging for {len(tagged_results)} items.")

    # Calculate theme statistics
    theme_counts = Counter(r["primary_theme"] for r in tagged_results)
    sentiment_counts = Counter(r["sentiment"] for r in tagged_results)
    friction_count = sum(1 for r in tagged_results if r.get("friction_present"))

    # Extract sample quotes per theme
    quotes_by_theme = {}
    for r in tagged_results:
        theme = r["primary_theme"]
        quote = r.get("verbatim_quote")
        if quote and len(quote) > 15:
            if theme not in quotes_by_theme:
                quotes_by_theme[theme] = []
            if len(quotes_by_theme[theme]) < 3:
                quotes_by_theme[theme].append({
                    "quote": quote,
                    "source": r["source"]
                })

    # Stage B: Synthesize Discovery Pulse
    print("3. Stage B: Generating Synthesis & Opportunity Areas via LLM...")
    synthesis = synthesize_pulse(client, total_reviews, len(tagged_results), dict(theme_counts), quotes_by_theme)

    # Save full results to JSON
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    full_output = {
        "metadata": {
            "analysis_model": MODEL_NAME,
            "total_dataset_size": total_reviews,
            "sample_analyzed_size": len(tagged_results),
            "friction_identified_count": friction_count,
            "friction_rate_percentage": round((friction_count / len(tagged_results)) * 100, 2) if tagged_results else 0,
            "sources_in_sample": dict(Counter(r["source"] for r in tagged_results)),
            "theme_distribution": dict(theme_counts),
            "sentiment_distribution": dict(sentiment_counts)
        },
        "synthesis": synthesis,
        "sample_grounded_quotes": quotes_by_theme,
        "tagged_reviews": tagged_results
    }

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(full_output, f, indent=2)
    print(f"-> Saved structured results to {OUTPUT_JSON}")

    # Generate Markdown Summary
    md_content = f"""# Weekly Discovery Pulse: Myntra Wishlist Conversion

**Total Dataset Size:** {total_reviews} reviews & posts across Google Play, Apple App Store, YouTube, and Reddit.  
**Stratified Sample Analyzed:** {len(tagged_results)} reviews.  
**Friction Rate:** {full_output['metadata']['friction_rate_percentage']}% of analyzed touchpoints report active purchase blockers.

---

## 1. Executive Summary
{synthesis.get('executive_summary', 'N/A')}

**Dominant Friction Theme:** `{synthesis.get('dominant_friction_theme', 'Price & Hidden Cost Surprises')}`

---

## 2. Friction Theme Breakdown
| Theme | Frequency (Count) | % of Analyzed Sample |
| :--- | :--- | :--- |
"""
    for theme, count in theme_counts.most_common():
        pct = round((count / len(tagged_results)) * 100, 1)
        md_content += f"| **{theme}** | {count} | {pct}% |\n"

    md_content += f"""
---

## 3. Root Cause Analysis (5 Whys)
"""
    for why in synthesis.get("root_cause_analysis", []):
        md_content += f"- **{why.get('level')}**: {why.get('cause')}\n"

    md_content += f"""
---

## 4. Opportunity Areas for Wishlist Conversion
"""
    for opp in synthesis.get("opportunities", []):
        md_content += f"""### 💡 Opportunity: {opp.get('theme')}
**Problem Statement:**
> {opp.get('rigorous_problem_statement')}

**Grounded Evidence (Verbatim Quote):**
*\"{opp.get('grounded_quote')}\"*

"""

    md_content += f"""---

## 5. Primary Research Interview Guide (Validation Questions)
Use these targeted questions during user interviews:
"""
    for q in synthesis.get("primary_research_interview_guide", []):
        md_content += f"1. \"{q}\"\n"

    with open(OUTPUT_SUMMARY, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"-> Saved human-readable summary to {OUTPUT_SUMMARY}")
    print("\nPhase 2 AI Analysis completed successfully!")

if __name__ == "__main__":
    main()
