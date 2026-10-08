from src.phase_02.analysis import FRICTION_THEMES, align_tags, get_stratified_sample, normalize_theme


def test_normalize_theme_variants():
    assert normalize_theme("fit / size") == "Fit/size"
    assert normalize_theme("PRICE") == "Price"
    assert normalize_theme("Returns (policy)") == "Returns"
    assert normalize_theme("Other / General Feedback") == "Other emergent themes"
    assert normalize_theme(None) == "Other emergent themes"
    assert all(normalize_theme(t) == t for t in FRICTION_THEMES)


def test_align_tags_matches_on_id_not_position():
    batch = [{"text": "a"}, {"text": "b"}, {"text": "c"}]
    tags = [{"id": 3, "primary_theme": "Price"}, {"id": 1, "primary_theme": "Returns"}]
    assert [(i, t["primary_theme"]) for i, t in align_tags(batch, tags)] == [(2, "Price"), (0, "Returns")]


def test_align_tags_falls_back_to_position_and_ignores_duplicates():
    batch = [{"text": "a"}, {"text": "b"}]
    tags = [{"primary_theme": "Price"}, {"id": 1, "primary_theme": "Dup"}, {"id": 99, "primary_theme": "X"}]
    out = list(align_tags(batch, tags))
    assert out[0][0] == 0 and len({i for i, _ in out}) == len(out)


def test_stratified_sample_is_balanced_and_reproducible():
    reviews = [{"source": "A", "text": str(i)} for i in range(100)] + [{"source": "B", "text": str(i)} for i in range(10)]
    s1 = get_stratified_sample(reviews, max_total=20)
    s2 = get_stratified_sample(reviews, max_total=20)
    assert s1 == s2
    assert sum(r["source"] == "A" for r in s1) == 10 and sum(r["source"] == "B" for r in s1) == 10
    assert get_stratified_sample([], 10) == []


def test_main_end_to_end_with_fake_llm(monkeypatch, tmp_path):
    """Runs the whole pipeline against the committed corpus with a stubbed LLM and temp outputs."""
    import json

    from src.phase_02 import analysis

    out_json, out_md = tmp_path / "a.json", tmp_path / "a.md"
    monkeypatch.setattr(analysis, "OUTPUT_JSON", str(out_json))
    monkeypatch.setattr(analysis, "OUTPUT_SUMMARY", str(out_md))
    monkeypatch.setattr(analysis, "MAX_SAMPLE_SIZE", 40)
    monkeypatch.setattr(analysis.time, "sleep", lambda *_: None)
    monkeypatch.setenv("GROQ_API_KEY", "fake")
    monkeypatch.setattr(analysis, "Groq", lambda api_key: object())

    def fake_tags(_client, batch):
        # Reverse order + variant spelling: id alignment and normalisation must cope.
        return [
            {"id": i + 1, "primary_theme": "returns" if i % 2 else "fit / size", "sentiment": "negative",
             "friction_present": bool(i % 2), "verbatim_quote": "a long enough verbatim quote"}
            for i in reversed(range(len(batch)))
        ]

    monkeypatch.setattr(analysis, "tag_batch_reviews", fake_tags)
    monkeypatch.setattr(analysis, "synthesize_pulse", lambda *a, **k: {
        "executive_summary": "x", "dominant_friction_theme": "Returns", "root_cause_analysis": [],
        "opportunities": [], "primary_research_interview_guide": []})
    analysis.main()

    res = json.loads(out_json.read_text())
    meta = res["metadata"]
    assert meta["off_topic_excluded"] > 0 and meta["total_dataset_size"] > meta["on_topic_dataset_size"]
    assert set(meta["theme_distribution"]) <= set(FRICTION_THEMES)
    # the gate removed the off-topic YouTube comments (only 2 genuine keyword hits survive)
    assert meta["sources_in_sample"].get("YouTube", 0) <= 2
    assert len(meta["friction_rate_ci95_percentage"]) == 2 and meta["friction_rate_corpus_weighted_percentage"] is not None
    assert "95% CI" in out_md.read_text()
