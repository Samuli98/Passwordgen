#!/usr/bin/env python3
"""Generate HTML CVs (open in browser) and Chrome-printed PDFs (application-ready)."""

from __future__ import annotations

import subprocess
from pathlib import Path

DIR = Path(__file__).parent
HTML_DIR = DIR / "html"
ARTIFACTS = Path("/opt/cursor/artifacts")

CSS = """
@page { size: A4; margin: 12mm 14mm; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: Calibri, 'Segoe UI', Arial, sans-serif;
  font-size: 10pt;
  line-height: 1.35;
  color: #1a1a1a;
  max-width: 800px;
  margin: 0 auto;
  padding: 24px;
}
.header {
  text-align: center;
  border-bottom: 2px solid #1e3a5f;
  padding-bottom: 8px;
  margin-bottom: 12px;
}
.name { font-size: 22pt; font-weight: 700; color: #1e3a5f; }
.contact { font-size: 9.5pt; color: #444; margin-top: 4px; }
.section { margin-top: 12px; }
.section-title {
  font-size: 10.5pt;
  font-weight: 700;
  color: #1e3a5f;
  text-transform: uppercase;
  letter-spacing: 0.6px;
  border-bottom: 1px solid #c5d3e0;
  padding-bottom: 2px;
  margin-bottom: 6px;
}
p { margin-bottom: 6px; text-align: justify; }
.skill { margin-bottom: 3px; }
.skill strong { color: #1e3a5f; }
.job { margin-bottom: 10px; }
.job-title { font-weight: 700; font-size: 10.5pt; }
.job-meta { font-style: italic; color: #555; font-size: 9.5pt; margin-bottom: 4px; }
ul { margin-left: 18px; }
li { margin-bottom: 3px; }
@media print {
  body { padding: 0; max-width: none; }
}
"""


def wrap(title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>
{body}
</body>
</html>
"""


AFFILIATE = wrap(
    "Samuli Lahtela - CV Affiliate Executive",
    """
<div class="header">
  <div class="name">Samuli Lahtela</div>
  <div class="contact">Malta, Gzira | +358 40 579 5752 | slahtela98@gmail.com<br>Open to Relocation</div>
</div>

<div class="section">
  <div class="section-title">Professional Summary</div>
  <p>iGaming professional with <strong>4+ years</strong> across <strong>partner-facing operations</strong>, <strong>campaign and promotion support</strong>, and <strong>performance-aware player acquisition journeys</strong> in regulated markets (<strong>MGA, SGA, Ontario, Dutch KSA</strong>). Experienced coordinating with marketing, CRM, and commercial teams on <strong>promotions, exclusive offers, and player-facing campaigns</strong>, while monitoring conversion-critical flows from registration to first deposit and beyond.</p>
  <p>Hands-on with <strong>Jira, Intercom, Confluence, and Zendesk</strong>. Strong communicator in <strong>English and Finnish</strong>, detail-oriented, and comfortable working with data patterns, compliance rules, and multiple stakeholders. Seeking an <strong>Affiliate Executive</strong> role where relationship management, campaign optimisation, and regulated-market awareness drive high-quality player acquisition.</p>
</div>

<div class="section">
  <div class="section-title">Core Skills</div>
  <div class="skill"><strong>Partnerships &amp; Acquisition:</strong> Stakeholder relationship management · Campaign &amp; promotion coordination · Player acquisition journey (registration → FTD) · Multi-market acquisition context</div>
  <div class="skill"><strong>Performance &amp; Operations:</strong> KPI monitoring · Data pattern spotting · Campaign QA &amp; go-live checks · Compliance &amp; responsible gaming · Issue ownership</div>
  <div class="skill"><strong>Tools &amp; Markets:</strong> Jira · Intercom · Confluence · Zendesk · <strong>MGA · SGA (Sweden) · Ontario · Dutch (KSA)</strong> · English (fluent) · Finnish (native)</div>
</div>

<div class="section">
  <div class="section-title">Professional Experience</div>
  <div class="job">
    <div class="job-title">Senior Customer Operations — Glitnor, Malta</div>
    <div class="job-meta">August 2023 – Present</div>
    <ul>
      <li>Manage relationships with players and commercial stakeholders across casino and sportsbook; support acquisition journeys: <strong>registration, deposits (FTD), bonuses, gameplay, and withdrawals</strong>.</li>
      <li><strong>Coordinate promotional campaigns and exclusive offers</strong> with CRM and marketing; review, set up, and configure promotions and monitor performance after go-live.</li>
      <li>Spot conversion and quality issues early and take ownership via <strong>Jira</strong> with clear <strong>Confluence</strong> documentation.</li>
      <li>Work across <strong>MGA, SGA, Ontario, and KSA</strong> markets ensuring campaigns comply with market rules and responsible gaming requirements.</li>
      <li>Analyse campaign-related signals daily — conversion drop-offs, traffic quality indicators, bonus abuse patterns — and recommend improvements.</li>
      <li>Communicate with CRM, VIP, payments, compliance, and product; use <strong>Intercom</strong> (daily) and <strong>Zendesk</strong>.</li>
    </ul>
  </div>
  <div class="job">
    <div class="job-title">Game Presenter / Help Desk — Evolution, Malta</div>
    <div class="job-meta">June 2022 – July 2023</div>
    <ul>
      <li>Represented the brand in live casino operations for an international audience; identified player experience issues affecting acquisition quality.</li>
      <li>Supported help desk escalations and coordinated with operations under pressure in a regulated environment.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Education</div>
  <p><strong>Kajaani University of Applied Sciences</strong> — 2020 – 2024</p>
</div>

<div class="section">
  <div class="section-title">Additional Information</div>
  <ul>
    <li><strong>Relocation:</strong> Open to relocation</li>
    <li><strong>Regulatory markets:</strong> Malta (MGA), Sweden (SGA), Ontario (AGCO), Netherlands (KSA)</li>
    <li><strong>Learning focus:</strong> Affiliate platforms (Cellxpert, Income Access, NetRefer) and CPA / Rev Share / Hybrid models</li>
  </ul>
</div>
""",
)

CASINO = wrap(
    "Samuli Lahtela - CV Casino Operations",
    """
<div class="header">
  <div class="name">Samuli Lahtela</div>
  <div class="contact">Malta, Gzira | +358 40 579 5752 | slahtela98@gmail.com<br>Open to Relocation</div>
</div>

<div class="section">
  <div class="section-title">Professional Summary</div>
  <p>iGaming operations professional with <strong>4+ years</strong> across <strong>casino operations</strong>, <strong>promotion configuration</strong>, and <strong>cross-team product support</strong> across <strong>MGA, SGA (Sweden), Ontario, and Dutch (KSA)</strong> regulated markets. Strong hands-on understanding of registration, deposits, bonuses, gameplay, and withdrawals across casino and sportsbook products.</p>
  <p>Daily user of <strong>Jira, Intercom, and Confluence</strong> (with Zendesk experience). Experienced reviewing, setting up, and configuring promotions, escalating product bugs, and coordinating with CRM, VIP, payments, and compliance teams. Background includes live casino operations at Evolution. Fluent in English and Finnish.</p>
</div>

<div class="section">
  <div class="section-title">Core Skills</div>
  <div class="skill"><strong>Casino Operations:</strong> Promotion setup &amp; configuration · Player journey review · Multi-market regulatory awareness · Payment operations · Live casino</div>
  <div class="skill"><strong>Product &amp; Cross-Team:</strong> Jira ticket management · Product bug reporting · Feature rollout validation · CRM / VIP / CS coordination · Confluence documentation</div>
  <div class="skill"><strong>Tools &amp; Markets:</strong> Jira · Intercom · Confluence · Zendesk · MGA · SGA (Sweden) · Ontario · Dutch (KSA) · English (fluent) · Finnish (native)</div>
</div>

<div class="section">
  <div class="section-title">Professional Experience</div>
  <div class="job">
    <div class="job-title">Casino Operations &amp; Product Support — Glitnor, Malta</div>
    <div class="job-meta">Senior Customer Operations | August 2023 – Present</div>
    <ul>
      <li>Lead day-to-day casino and sportsbook operations across registration, deposits, bonuses, gameplay, and withdrawals across MGA, SGA, Ontario, and Dutch regulated markets.</li>
      <li>Review, set up, and configure promotions and bonus campaigns; monitor configurations and flag issues before and after go-live.</li>
      <li>Manage product requests, bugs, and improvement tickets in <strong>Jira</strong> daily; document processes in <strong>Confluence</strong>.</li>
      <li>Handle operational queries through <strong>Intercom</strong> (daily) and <strong>Zendesk</strong>; coordinate with CRM, VIP, and Customer Support.</li>
      <li>Apply market-specific regulatory knowledge (SGA, Ontario, KSA, MGA) for bonuses, RG, verification, and compliance escalations.</li>
      <li>Identify operational issues, escalate to payments, compliance, fraud, and product teams; validate flows during rollouts.</li>
    </ul>
  </div>
  <div class="job">
    <div class="job-title">Game Presenter / Help Desk — Evolution, Malta</div>
    <div class="job-meta">June 2022 – July 2023</div>
    <ul>
      <li>Supported live casino operations in a regulated studio environment for an international player base.</li>
      <li>Provided help desk support; escalated platform issues to studio and operations teams.</li>
      <li>Identified player experience pain points during live gameplay and coordinated cross-team resolution.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Education</div>
  <p><strong>Kajaani University of Applied Sciences</strong> — 2020 – 2024</p>
</div>

<div class="section">
  <div class="section-title">Additional Information</div>
  <ul>
    <li><strong>Relocation:</strong> Open to relocation</li>
    <li><strong>Regulatory exposure:</strong> Malta (MGA), Sweden (SGA), Ontario (AGCO), Netherlands (KSA)</li>
    <li><strong>Work style:</strong> Organised, detail-oriented, comfortable in fast-paced environments</li>
  </ul>
</div>
""",
)

VIP = wrap(
    "Samuli Lahtela - CV VIP CRM",
    """
<div class="header">
  <div class="name">Samuli Lahtela</div>
  <div class="contact">Malta, Gzira | +358 40 579 5752 | slahtela98@gmail.com<br>Open to Remote &amp; Relocation</div>
</div>

<div class="section">
  <div class="section-title">Professional Summary</div>
  <p>iGaming professional with <strong>4+ years</strong> across <strong>VIP player support</strong>, <strong>live casino operations</strong>, and <strong>CRM-driven retention</strong> in Malta's regulated market. Experienced in managing high-value player relationships, monitoring account activity for risk and compliance, and supporting retention campaigns across casino and sportsbook products.</p>
  <p>Fluent in <strong>Finnish and English</strong>. Seeking a <strong>VIP Account Manager</strong>, <strong>Player Retention</strong>, or <strong>CRM-focused</strong> role — remote or international.</p>
</div>

<div class="section">
  <div class="section-title">Core Skills</div>
  <div class="skill"><strong>Player &amp; CRM:</strong> VIP relationship management · Player retention &amp; lifecycle · CRM documentation · Responsible gaming · KYC / compliance escalation · Campaign support</div>
  <div class="skill"><strong>Products:</strong> Online casino · Live casino · Sportsbook · Bonus &amp; wagering workflows</div>
  <div class="skill"><strong>Languages:</strong> Finnish (native) · English (fluent)</div>
</div>

<div class="section">
  <div class="section-title">Professional Experience</div>
  <div class="job">
    <div class="job-title">Customer Relations — Glitnor, Malta</div>
    <div class="job-meta">August 2023 – Present</div>
    <ul>
      <li>Manage day-to-day contact with players across casino and sportsbook, including VIP and high-value accounts; resolve payment, bonus, verification, and account queries end to end.</li>
      <li>Monitor player activity for at-risk behaviour, responsible gaming concerns, and compliance flags; escalate with clear case context.</li>
      <li>Support retention initiatives through promotions, campaigns, and personalised outreach aligned with CRM workflows.</li>
      <li>Handle VIP-related queries and sensitive account issues in a fast-paced, regulated environment.</li>
      <li>Collaborate with payments, compliance, and product teams; maintain accurate records for handovers and VIP continuity.</li>
    </ul>
  </div>
  <div class="job">
    <div class="job-title">Game Presenter / Help Desk — Evolution, Malta</div>
    <div class="job-meta">June 2022 – July 2023</div>
    <ul>
      <li>Hosted live casino games for an international audience with professionalism and adherence to studio standards.</li>
      <li>Built real-time rapport with high-value players; remained alert to complaints and escalation needs.</li>
      <li>Provided help desk support for technical and account queries between presenting sessions.</li>
      <li>Coordinated with studio operations and support teams without disrupting the live player experience.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Education</div>
  <p><strong>Kajaani University of Applied Sciences</strong> — 2020 – 2024</p>
</div>

<div class="section">
  <div class="section-title">Additional Information</div>
  <ul>
    <li><strong>Work location:</strong> Malta (EU work rights) · Open to remote roles or relocation</li>
    <li><strong>Industry:</strong> Regulated iGaming (B2C casino &amp; sportsbook)</li>
  </ul>
</div>
""",
)


def html_to_pdf(html_path: Path, pdf_path: Path) -> None:
    user_data = Path(f"/tmp/chrome-cv-{pdf_path.stem}")
    user_data.mkdir(parents=True, exist_ok=True)
    cmd = [
        "google-chrome",
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--disable-dev-shm-usage",
        f"--user-data-dir={user_data}",
        "--no-pdf-header-footer",
        f"--print-to-pdf={pdf_path}",
        f"file://{html_path.resolve()}",
    ]
    # Chrome often stays running; use timeout and ignore nonzero if PDF exists
    try:
        subprocess.run(cmd, capture_output=True, timeout=45)
    except subprocess.TimeoutExpired:
        pass
    if not pdf_path.exists() or pdf_path.stat().st_size < 1000:
        raise RuntimeError(f"PDF not created: {pdf_path}")


def main() -> None:
    HTML_DIR.mkdir(parents=True, exist_ok=True)
    ARTIFACTS.mkdir(parents=True, exist_ok=True)

    files = {
        "Samuli-Lahtela-CV-Affiliate-Executive": AFFILIATE,
        "Samuli-Lahtela-CV-Casino-Operations-Limassol": CASINO,
        "Samuli-Lahtela-CV": VIP,
    }

    for name, html in files.items():
        html_path = HTML_DIR / f"{name}.html"
        html_path.write_text(html, encoding="utf-8")
        print(f"HTML: {html_path}")

        pdf_career = DIR / f"{name}.pdf"
        pdf_art = ARTIFACTS / f"{name}.pdf"
        html_to_pdf(html_path, pdf_career)
        # copy to artifacts
        pdf_art.write_bytes(pdf_career.read_bytes())
        print(f"PDF:  {pdf_career} ({pdf_career.stat().st_size // 1024} KB)")
        print(f"ART:  {pdf_art}")


if __name__ == "__main__":
    main()
