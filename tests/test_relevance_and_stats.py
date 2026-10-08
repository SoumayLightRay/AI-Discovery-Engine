import math

from src.phase_01.relevance import has_fashion_signal, is_relevant
from src.phase_02.stats import source_weighted_rate, theme_statistics, wilson_interval


def test_gate_rejects_unrelated_youtube_comments():
    assert not is_relevant({"source": "YouTube", "text": "Watching this in 2017, the squirrel hides its nuts"})
    assert not is_relevant({"source": "YouTube", "text": "I think people seeing it by two to three phones"})


def test_gate_keeps_fashion_youtube_comments():
    assert is_relevant({"source": "YouTube", "text": "The kurta size chart was wrong and my return got rejected"})


def test_gate_does_not_touch_app_store_reviews():
    # On-topic by construction, even without a keyword.
    assert is_relevant({"source": "Google Play", "text": "everything was very smooth and great"})


def test_stop_is_not_a_top_signal():
    assert not has_fashion_signal("please stop by this video")


def test_wilson_interval_bounds_and_symmetry():
    lo, hi = wilson_interval(44, 313)
    assert 0.10 < lo < 44 / 313 < hi < 0.19
    assert wilson_interval(0, 0) == (0.0, 0.0)
    lo0, hi0 = wilson_interval(0, 50)
    assert lo0 == 0.0 and hi0 > 0  # zero hits is not "certainly zero"
    assert math.isclose(sum(wilson_interval(50, 100)) / 2, 0.5, abs_tol=0.01)


def test_source_weighting_uses_corpus_mix():
    # Reddit is 100% friction, Play 0%; corpus is 90% Play -> estimate 10%, not the 50% sample rate.
    rate = source_weighted_rate({"Reddit": (10, 10), "Play": (0, 10)}, {"Reddit": 10, "Play": 90})
    assert math.isclose(rate, 0.10)
    assert source_weighted_rate({"X": (1, 1)}, {}) is None


def test_theme_statistics():
    tagged = [
        {"primary_theme": "Price", "friction_present": True},
        {"primary_theme": "Price", "friction_present": False},
        {"primary_theme": "Returns", "friction_present": True},
        {"primary_theme": "Returns", "friction_present": True},
    ]
    st = theme_statistics(tagged)
    assert st["Price"]["count"] == 2 and st["Price"]["friction_rate_pct"] == 50.0
    assert st["Returns"]["friction_rate_pct"] == 100.0 and st["Returns"]["share_pct"] == 50.0
