"""
Topical-relevance gate for ingested records.

Why this exists: sources such as YouTube comments are collected per *video*, so
a single wrongly-chosen video can flood the corpus with comments that have
nothing to do with fashion or shopping (the committed dataset contains 190
YouTube comments from unrelated viral videos). App-store reviews are on-topic
by construction, so the gate is only applied to the sources in GATED_SOURCES.

The check is deliberately cheap and transparent (a keyword allow-list) so that
it can be audited, unit-tested and tuned without calling an LLM.
"""
import re

# Sources whose records are NOT guaranteed on-topic by how they are collected.
GATED_SOURCES = {"YouTube"}

_SIGNAL = re.compile(
    r"myntra|mytra|ajio|nykaa|flipkart|amazon|meesho|tata\s*cliq|h&m|zara|"
    r"wishlist|wish\s*list|\bcart\b|checkout|\border(?:ed|s|ing)?\b|deliver|"
    r"\breturn|refund|exchange|\bsize|\bsizing\b|\bfit(?:s|ting)?\b|"
    r"cloth|apparel|dress|shirt|kurt[ai]|saree|lehenga|jeans|"
    r"trouser|shorts|jacket|hoodie|sweater|shoe|sneaker|footwear|"
    r"fashion|outfit|styling|haul|try-?on|"
    r"price|discount|coupon|\bsale\b|offer|\bbuy|bought|purchase|shopping|shop\b|"
    r"fabric|material|quality|stitch|brand",
    re.IGNORECASE,
)


def has_fashion_signal(text: str) -> bool:
    """True if the text contains at least one fashion/shopping/app-commerce cue."""
    return bool(text and _SIGNAL.search(text))


def is_relevant(record: dict) -> bool:
    """Return True if a normalized record should be kept for analysis/retrieval."""
    if record.get("source") not in GATED_SOURCES:
        return True
    return has_fashion_signal(record.get("text", ""))
