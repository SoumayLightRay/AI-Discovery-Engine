"""
Google Docs Report Exporter for the AI Discovery Engine.
Reads the weekly pulse summary and analysis results, then formats them
into a clean Google Docs-compatible document or exports as a standalone HTML report.

Usage:
    python src/phase_03/export_report.py          # Export as HTML
    python src/phase_03/export_report.py --gdocs   # Push to Google Docs (requires credentials)
"""
import json
import os
import sys
from datetime import datetime

ANALYSIS_PATH = "docs/phases/phase-02/analysis_results.json"
SUMMARY_PATH = "docs/phases/phase-02/weekly_pulse_summary.md"
OUTPUT_HTML = "docs/phases/phase-03/discovery_report.html"


def load_analysis():
    with open(ANALYSIS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_html_report(data):
    """Generate a polished HTML report suitable for Google Docs import or standalone viewing."""
    meta = data.get("metadata", {})
    synthesis = data.get("synthesis", {})
    quotes = data.get("sample_grounded_quotes", {})

    theme_rows = ""
    for theme, count in sorted(meta.get("theme_distribution", {}).items(), key=lambda x: -x[1]):
        if "other" in theme.lower():
            continue
        pct = round((count / meta.get("sample_analyzed_size", 1)) * 100, 1)
        theme_rows += f"<tr><td><strong>{theme}</strong></td><td>{count}</td><td>{pct}%</td></tr>\n"

    opp_blocks = ""
    for i, opp in enumerate(synthesis.get("opportunities", []), 1):
        opp_blocks += f"""
        <div style="background:#f8f9fa;border-left:4px solid #7c3aed;padding:16px;margin:16px 0;border-radius:4px;">
            <h3 style="color:#7c3aed;margin-top:0;">Opportunity {i}: {opp.get('theme', '')}</h3>
            <p><strong>Problem Statement:</strong><br>{opp.get('rigorous_problem_statement', '')}</p>
            <blockquote style="border-left:3px solid #38bdf8;padding-left:12px;color:#475569;font-style:italic;">
                "{opp.get('grounded_quote', '')}"
            </blockquote>
        </div>"""

    root_cause_items = ""
    for why in synthesis.get("root_cause_analysis", []):
        root_cause_items += f"<li><strong>{why.get('level')}:</strong> {why.get('cause')}</li>\n"

    interview_items = ""
    for q in synthesis.get("primary_research_interview_guide", []):
        interview_items += f'<li>"{q}"</li>\n'

    report_date = datetime.now().strftime("%B %d, %Y")

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>AI Discovery Engine — Weekly Pulse Report</title>
    <style>
        body {{ font-family: 'Google Sans', Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 40px; color: #1e293b; line-height: 1.7; }}
        h1 {{ color: #0f172a; border-bottom: 3px solid #7c3aed; padding-bottom: 8px; }}
        h2 {{ color: #334155; margin-top: 32px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 16px 0; }}
        th {{ background: #7c3aed; color: white; padding: 10px 14px; text-align: left; }}
        td {{ padding: 8px 14px; border-bottom: 1px solid #e2e8f0; }}
        tr:nth-child(even) {{ background: #f8fafc; }}
        .metric {{ display: inline-block; background: #f1f5f9; padding: 12px 20px; border-radius: 8px; margin: 8px 8px 8px 0; text-align: center; }}
        .metric .value {{ font-size: 24px; font-weight: 700; color: #7c3aed; }}
        .metric .label {{ font-size: 12px; color: #64748b; text-transform: uppercase; }}
        .footer {{ margin-top: 40px; padding-top: 16px; border-top: 1px solid #e2e8f0; font-size: 12px; color: #94a3b8; }}
    </style>
</head>
<body>
    <h1>🔮 AI Discovery Engine — Weekly Pulse Report</h1>
    <p style="color:#64748b;">Generated: {report_date} | Model: {meta.get('analysis_model', 'N/A')} | Cohort: Apparel & Intimates</p>

    <div>
        <div class="metric"><div class="value">{meta.get('total_dataset_size', 0):,}</div><div class="label">Total Reviews</div></div>
        <div class="metric"><div class="value">{meta.get('sample_analyzed_size', 0)}</div><div class="label">Sample Analyzed</div></div>
        <div class="metric"><div class="value">{meta.get('friction_rate_percentage', 0)}%</div><div class="label">Friction Rate</div></div>
    </div>

    <h2>Executive Summary</h2>
    <p>{synthesis.get('executive_summary', 'N/A')}</p>
    <p><strong>Dominant Friction Theme:</strong> {synthesis.get('dominant_friction_theme', 'N/A')}</p>

    <h2>Friction Theme Distribution</h2>
    <table>
        <tr><th>Theme</th><th>Count</th><th>% of Sample</th></tr>
        {theme_rows}
    </table>

    <h2>Root Cause Analysis (5 Whys)</h2>
    <ol>{root_cause_items}</ol>

    <h2>Synthesized Opportunities</h2>
    {opp_blocks}

    <h2>Primary Research Interview Guide</h2>
    <p>Use these targeted questions during 1:1 user interviews to validate findings:</p>
    <ol>{interview_items}</ol>

    <div class="footer">
        <p>AI Discovery Engine v2.4 · Data sourced from Google Play, Apple App Store, YouTube, Reddit</p>
        <p>⚠️ This report is generated by AI analysis of user reviews. Core synthesis and problem structuring remain human-driven.</p>
    </div>
</body>
</html>"""
    return html


def main():
    print("=== Exporting Discovery Engine Report ===")

    data = load_analysis()
    html = generate_html_report(data)

    os.makedirs(os.path.dirname(OUTPUT_HTML), exist_ok=True)
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Report exported to {OUTPUT_HTML}")
    print(f"   You can open this in your browser or import directly into Google Docs.")
    print(f"   Google Docs: File > Open > Upload the HTML file")


if __name__ == "__main__":
    main()
