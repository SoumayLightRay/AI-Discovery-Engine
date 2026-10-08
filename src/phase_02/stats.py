"""
Small, dependency-free statistics helpers for the analysis pipeline.

The analysis tags a *stratified* sample (an equal number of reviews per source),
so the raw sample percentages over-represent small sources such as Reddit and
under-represent Google Play. These helpers quantify that uncertainty instead of
presenting sample percentages as if they described the whole corpus.
"""
import math


def wilson_interval(successes: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """95% Wilson score interval for a proportion, as fractions in [0, 1].

    Preferred over the normal approximation because it behaves for small n and
    for proportions near 0 or 1 (many themes here have only a handful of hits).
    """
    if n <= 0:
        return (0.0, 0.0)
    p = successes / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def pct(x: float, digits: int = 1) -> float:
    return round(100 * x, digits)


def source_weighted_rate(per_source: dict[str, tuple[int, int]], corpus_counts: dict[str, int]) -> float | None:
    """Re-weight per-source rates to the corpus's real source mix.

    per_source:    {source: (events, sample_size)}
    corpus_counts: {source: number of records in the full corpus}
    Returns the estimated corpus-wide rate as a fraction, or None if no source
    has both a sample and a corpus count.
    """
    total = sum(corpus_counts.get(s, 0) for s, (_, n) in per_source.items() if n > 0)
    if total <= 0:
        return None
    return sum(
        corpus_counts[s] / total * (events / n)
        for s, (events, n) in per_source.items()
        if n > 0 and corpus_counts.get(s, 0) > 0
    )


def theme_statistics(tagged: list[dict]) -> dict[str, dict]:
    """Per-theme count, share of sample (with 95% CI) and friction count."""
    n = len(tagged)
    themes: dict[str, dict] = {}
    for r in tagged:
        t = themes.setdefault(r["primary_theme"], {"count": 0, "friction_count": 0})
        t["count"] += 1
        t["friction_count"] += 1 if r.get("friction_present") else 0
    for t in themes.values():
        lo, hi = wilson_interval(t["count"], n)
        t["share_pct"] = pct(t["count"] / n) if n else 0.0
        t["share_ci95_pct"] = [pct(lo), pct(hi)]
        t["friction_rate_pct"] = pct(t["friction_count"] / t["count"]) if t["count"] else 0.0
    return themes
