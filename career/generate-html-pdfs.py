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
.doc-title {
  font-size: 11pt;
  font-weight: 600;
  color: #1e3a5f;
  text-transform: uppercase;
  letter-spacing: 1.2px;
  margin-bottom: 2px;
}
table.lang { width: 100%; border-collapse: collapse; font-size: 9.5pt; margin-top: 4px; }
table.lang th, table.lang td { border: 1px solid #c5d3e0; padding: 4px 8px; text-align: left; }
table.lang th { background: #f4f7fa; color: #1e3a5f; }
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
    "Samuli Lahtela - CV",
    """
<div class="header">
  <div class="name">Samuli Lahtela</div>
  <div class="contact">Malta, Gzira | +358 40 579 5752 | slahtela98@gmail.com<br>Open to Relocation</div>
</div>

<div class="section">
  <div class="section-title">Professional Summary</div>
  <p>iGaming professional with 4+ years in casino and sportsbook operations across regulated markets (MGA, SGA, Ontario, Dutch KSA). Experienced with promotions, player journeys, and day-to-day coordination with CRM, marketing, and commercial teams. Used to working in English and Finnish, spotting issues early, and following them through in Jira, Intercom, and Confluence.</p>
</div>

<div class="section">
  <div class="section-title">Core Skills</div>
  <div class="skill"><strong>Operations:</strong> Promotion setup &amp; configuration · Player journey support · Campaign coordination · Multi-market compliance · Responsible gaming</div>
  <div class="skill"><strong>Tools:</strong> Jira · Intercom · Confluence · Zendesk</div>
  <div class="skill"><strong>Markets &amp; Languages:</strong> MGA · SGA (Sweden) · Ontario · Dutch (KSA) · English (fluent) · Finnish (native)</div>
</div>

<div class="section">
  <div class="section-title">Professional Experience</div>
  <div class="job">
    <div class="job-title">Senior Customer Operations — Glitnor, Malta</div>
    <div class="job-meta">August 2023 – Present</div>
    <ul>
      <li>Support casino and sportsbook operations across registration, deposits, bonuses, gameplay, and withdrawals.</li>
      <li>Review, set up, and configure promotions; coordinate campaign launches with CRM and marketing.</li>
      <li>Work across MGA, SGA, Ontario, and Dutch regulated markets, applying the right market rules and RG requirements.</li>
      <li>Raise and track issues in Jira daily; document processes in Confluence.</li>
      <li>Handle player and internal queries through Intercom and Zendesk; work with payments, compliance, VIP, and product when cases need escalation.</li>
      <li>Flag configuration or player-flow problems early and follow them through to resolution.</li>
    </ul>
  </div>
  <div class="job">
    <div class="job-title">Game Presenter / Help Desk — Evolution, Malta</div>
    <div class="job-meta">June 2022 – July 2023</div>
    <ul>
      <li>Hosted live casino games for an international player base in a regulated studio environment.</li>
      <li>Supported help desk queries and escalated technical or account issues to operations.</li>
      <li>Worked under pressure with clear communication across studio and support teams.</li>
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
    <li>Open to relocation</li>
    <li>Regulatory markets: Malta (MGA), Sweden (SGA), Ontario (AGCO), Netherlands (KSA)</li>
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

CS_AGENT = wrap(
    "Samuli Lahtela - CV CS Agent",
    """
<div class="header">
  <div class="doc-title">Curriculum Vitae</div>
  <div class="name">Samuli Lahtela</div>
  <div class="contact">Tallinn, Estonia | +358 40 579 5752 | slahtela98@gmail.com</div>
</div>

<div class="section">
  <div class="section-title">Professional Summary</div>
  <p>Customer service professional with 4+ years in iGaming and customer-facing roles. Experienced handling player queries, payments, bonuses, and account issues. Clear communicator in English and Finnish.</p>
</div>

<div class="section">
  <div class="section-title">Core Skills</div>
  <div class="skill"><strong>Customer Service:</strong> Player support · Account queries · Payments &amp; bonuses · KYC / verification · Responsible gaming · Complaint handling</div>
  <div class="skill"><strong>Tools:</strong> Intercom · Zendesk · Jira · Confluence</div>
  <div class="skill"><strong>Work style:</strong> Calm under pressure · Accurate record-keeping · Team collaboration · Quick to learn new systems</div>
</div>

<div class="section">
  <div class="section-title">Work Experience</div>
  <div class="job">
    <div class="job-title">Customer Relations — Glitnor, Malta</div>
    <div class="job-meta">August 2023 – Present</div>
    <ul>
      <li>Handle player contact across casino and sportsbook; resolve payment, bonus, verification, and account queries.</li>
      <li>Escalate responsible gaming, risk, and compliance issues when needed.</li>
      <li>Work with internal teams to close cases quickly and keep clear notes on interactions.</li>
    </ul>
  </div>
  <div class="job">
    <div class="job-title">Game Presenter / Help Desk — Evolution, Malta</div>
    <div class="job-meta">June 2022 – July 2023</div>
    <ul>
      <li>Hosted live casino games for international players in a regulated studio.</li>
      <li>Provided help desk support for technical and account-related queries.</li>
      <li>Stayed professional under pressure and worked well with studio and support teams.</li>
    </ul>
  </div>
  <div class="job">
    <div class="job-title">Courier — DHL, Finland</div>
    <div class="job-meta">2018 – 2022</div>
    <ul>
      <li>Delivered parcels on scheduled routes; worked independently and met daily targets.</li>
      <li>Handled customer contact and resolved delivery issues on the spot.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Education</div>
  <p><strong>Kajaani University of Applied Sciences</strong> — 2020 – 2024</p>
</div>

<div class="section">
  <div class="section-title">Languages</div>
  <table class="lang">
    <tr><th>Language</th><th>Understanding</th><th>Speaking</th><th>Writing</th></tr>
    <tr><td><strong>Finnish</strong></td><td>E — Mother tongue</td><td>E — Mother tongue</td><td>E — Mother tongue</td></tr>
    <tr><td><strong>English</strong></td><td>A — Excellent</td><td>A — Excellent</td><td>A — Excellent</td></tr>
    <tr><td><strong>Swedish</strong></td><td>C — Okay</td><td>D — Little</td><td>D — Little</td></tr>
  </table>
</div>

<div class="section">
  <div class="section-title">Social Skills</div>
  <p>Good at working independently and as part of a team. Comfortable talking to customers and colleagues in different situations. Happy to learn new skills and pick up new tools quickly.</p>
</div>

<div class="section">
  <div class="section-title">Hobbies</div>
  <p>In my free time I go to the gym and take part in sports activities. I try to live a healthy, active lifestyle.</p>
</div>
""",
)

BOLT = wrap(
    "Samuli Lahtela - CV",
    """
<div class="header">
  <div class="name">Samuli Lahtela</div>
  <div class="contact">Tallinn, Estonia | +358 40 579 5752 | slahtela98@gmail.com<br>Open to Relocation / Tallinn-based roles</div>
</div>

<div class="section">
  <div class="section-title">Professional Summary</div>
  <p>Support and operations professional with 4+ years in high-volume customer-facing environments. Strong understanding of how users get help, describe issues, and move through chat, self-serve, and human-assisted flows. Worked closely with the Customer Support manager on process improvements, tooling feedback, and player journey fixes across regulated markets.</p>
  <p>Daily user of Intercom, Zendesk, Jira, and Confluence. Used to balancing quality of support with speed and operational efficiency. Fluent in English and Finnish.</p>
</div>

<div class="section">
  <div class="section-title">Core Skills</div>
  <div class="skill"><strong>Support experience:</strong> Help &amp; intake flows · Live chat · Case escalation · Self-serve awareness · Player journey mapping · Quality vs efficiency trade-offs</div>
  <div class="skill"><strong>Cross-team delivery:</strong> Collaboration with CS management · Product / ops feedback loops · Jira tickets &amp; bug reports · Process documentation · Stakeholder updates</div>
  <div class="skill"><strong>Tools:</strong> Intercom · Zendesk · Jira · Confluence</div>
</div>

<div class="section">
  <div class="section-title">Work Experience</div>
  <div class="job">
    <div class="job-title">Senior Customer Operations — Glitnor, Malta</div>
    <div class="job-meta">August 2023 – Present</div>
    <ul>
      <li>Work in a high-volume support environment covering registration, payments, bonuses, account access, and withdrawals across multiple markets.</li>
      <li>Partner closely with the Customer Support manager on day-to-day operations, process gaps, and improvements to how cases are handled and escalated.</li>
      <li>Map and improve player journeys when something breaks — from how the issue is raised to how it gets routed and resolved.</li>
      <li>Raise product and tooling feedback in Jira and follow cases through with clear Confluence notes.</li>
      <li>Use Intercom and Zendesk daily; feed real agent and user pain points back to management and related teams.</li>
      <li>Balance user experience with operational reality — spotting where clearer routing or self-serve would reduce repeat contacts and cost to serve.</li>
      <li>Coordinate with payments, compliance, CRM, VIP, and product when support issues need a cross-team fix.</li>
    </ul>
  </div>
  <div class="job">
    <div class="job-title">Game Presenter / Help Desk — Evolution, Malta</div>
    <div class="job-meta">June 2022 – July 2023</div>
    <ul>
      <li>Supported live casino users under pressure; handled help desk queries and escalations.</li>
      <li>Flagged recurring experience issues to operations and support teams.</li>
    </ul>
  </div>
  <div class="job">
    <div class="job-title">Courier — DHL, Finland</div>
    <div class="job-meta">2018 – 2022</div>
    <ul>
      <li>Customer-facing delivery role with independent ownership of daily targets and on-the-spot problem solving.</li>
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
    <li>Based in Tallinn, Estonia</li>
    <li>Languages: Finnish (native), English (excellent)</li>
    <li>Markets worked: MGA, SGA (Sweden), Ontario, Dutch (KSA)</li>
  </ul>
</div>
""",
)

HIGH_VOLUME = wrap(
    "Samuli Lahtela - CV",
    """
<div class="header">
  <div class="name">Samuli Lahtela</div>
  <div class="contact">Tallinn, Estonia | +358 40 579 5752 | slahtela98@gmail.com<br>Open to Relocation</div>
</div>

<div class="section">
  <div class="section-title">Professional Summary</div>
  <p>Customer support specialist with 4+ years in high-volume, regulated environments. Used to owning cases end to end — from first contact through resolution — including payments, account access, KYC, and compliance-related issues. Experienced supporting high-value customers where clear communication, calm ownership, and retention matter.</p>
  <p>Worked across live chat and written channels with Intercom, Zendesk, Jira, and Confluence. Comfortable escalating to KYC, risk, and compliance with the right context, while staying the customer’s main point of contact. Fluent in Finnish and English.</p>
</div>

<div class="section">
  <div class="section-title">Core Skills</div>
  <div class="skill"><strong>Case ownership:</strong> Cradle-to-grave support · First contact resolution focus · Multi-channel workflow · Clear updates · Internal coordination</div>
  <div class="skill"><strong>Retention &amp; high-value support:</strong> High-touch service · De-escalation · At-risk customer awareness · Loyalty-focused communication</div>
  <div class="skill"><strong>Compliance &amp; complexity:</strong> KYC / verification · Responsible gaming · Risk &amp; fraud escalation · Explaining difficult decisions simply</div>
  <div class="skill"><strong>Tools:</strong> Intercom · Zendesk · Jira · Confluence</div>
</div>

<div class="section">
  <div class="section-title">Work Experience</div>
  <div class="job">
    <div class="job-title">Senior Customer Operations — Glitnor, Malta</div>
    <div class="job-meta">August 2023 – Present</div>
    <ul>
      <li>Own player enquiries end to end across casino and sportsbook — payments, bonuses, account access, verification, and withdrawals — without passing the buck.</li>
      <li>Support high-value and VIP players where trust, speed, and clear ownership matter; keep the customer updated until the issue is closed.</li>
      <li>Work closely with KYC, compliance, risk, and payments teams; escalate with full context while remaining the customer’s single point of contact.</li>
      <li>Spot at-risk behaviour and friction early; use high-touch service and clear communication to protect retention.</li>
      <li>De-escalate tense situations with empathy and transparency, including when delivering difficult news around limits, verification, or account restrictions.</li>
      <li>Raise recurring issues, process gaps, and product bugs to management via Jira; document fixes in Confluence for the wider team.</li>
      <li>Manage a high volume of cases across live and written channels without dropping quality.</li>
    </ul>
  </div>
  <div class="job">
    <div class="job-title">Game Presenter / Help Desk — Evolution, Malta</div>
    <div class="job-meta">June 2022 – July 2023</div>
    <ul>
      <li>Supported international players in a fast, high-pressure live environment.</li>
      <li>Handled help desk queries and escalations; stayed accountable until issues were resolved with operations.</li>
    </ul>
  </div>
  <div class="job">
    <div class="job-title">Courier — DHL, Finland</div>
    <div class="job-meta">2018 – 2022</div>
    <ul>
      <li>Customer-facing role with daily ownership of targets and on-the-spot problem solving with frustrated customers.</li>
    </ul>
  </div>
</div>

<div class="section">
  <div class="section-title">Education</div>
  <p><strong>Kajaani University of Applied Sciences</strong> — 2020 – 2024</p>
</div>

<div class="section">
  <div class="section-title">Languages</div>
  <ul>
    <li><strong>Finnish</strong> — Native</li>
    <li><strong>English</strong> — Excellent</li>
    <li><strong>Swedish</strong> — Understanding okay; speaking and writing limited</li>
  </ul>
</div>

<div class="section">
  <div class="section-title">Additional Information</div>
  <ul>
    <li>Based in Tallinn, Estonia · Open to relocation</li>
    <li>Markets worked: MGA, SGA (Sweden), Ontario, Dutch (KSA)</li>
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
        "Samuli-Lahtela-CV-CS-Agent": CS_AGENT,
        "Samuli-Lahtela-CV-Bolt-Support-Experience": BOLT,
        "Samuli-Lahtela-CV-High-Volume-Support": HIGH_VOLUME,
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
