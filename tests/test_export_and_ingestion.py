import pytest

from src.phase_03.export_report import generate_html_report


def test_report_escapes_llm_text():
    data = {
        "metadata": {"analysis_model": "<b>m</b>", "theme_distribution": {"<script>x</script>": 3}, "sample_analyzed_size": 10},
        "synthesis": {
            "executive_summary": "<img src=x onerror=alert(1)>",
            "opportunities": [{"theme": "<i>t</i>", "rigorous_problem_statement": "<u>p</u>", "grounded_quote": "<s>q</s>"}],
            "root_cause_analysis": [{"level": "Why 1", "cause": "<svg onload=1>"}],
            "primary_research_interview_guide": ["<a href=javascript:1>q</a>"],
        },
    }
    html = generate_html_report(data)
    for raw in ("<script>x", "<img src=x", "<svg onload", "<a href=javascript", "<u>p</u>"):
        assert raw not in html
    assert "&lt;img src=x" in html


def test_clean_text_keeps_rupee_decodes_entities_drops_emoji():
    pytest.importorskip("google_play_scraper")
    pytest.importorskip("apify_client")
    from src.phase_01.ingestion import clean_text

    out = clean_text("It&#39;s only ₹499 \U0001F600 see https://x.co @bob great")
    assert "It's" in out and "₹499" in out and "\U0001F600" not in out and "http" not in out and "@bob" not in out
