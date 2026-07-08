#!/usr/bin/env python3
"""Generate application-ready CV PDFs."""

from __future__ import annotations

from pathlib import Path

from fpdf import FPDF

DIR = Path(__file__).parent
NAVY = (30, 58, 95)
TEXT = (26, 26, 26)
MUTED = (85, 85, 85)


def ascii_safe(text: str) -> str:
    return (
        text.replace("\u2014", " - ")
        .replace("\u2013", "-")
        .replace("\u00b7", " | ")
        .replace("\u2192", "->")
        .replace("\u2019", "'")
        .replace("\u2018", "'")
        .replace("\u201c", '"')
        .replace("\u201d", '"')
    )


class CVPDF(FPDF):
    def __init__(self, title: str) -> None:
        super().__init__()
        self.set_auto_page_break(auto=True, margin=12)
        self.set_margins(14, 12, 14)
        self.doc_title = title

    def _reset_x(self) -> None:
        self.set_x(self.l_margin)

    def header_block(self, name: str, contact: str) -> None:
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(*NAVY)
        self.cell(0, 9, name, align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "", 9)
        self.set_text_color(*MUTED)
        self.multi_cell(0, 4.2, contact, align="C")
        self.ln(1)
        self.set_draw_color(*NAVY)
        self.set_line_width(0.5)
        self.line(14, self.get_y(), 196, self.get_y())
        self.ln(4)

    def section(self, title: str) -> None:
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*NAVY)
        self.cell(0, 5, title.upper(), new_x="LMARGIN", new_y="NEXT")
        y = self.get_y()
        self.set_draw_color(197, 211, 224)
        self.set_line_width(0.2)
        self.line(14, y, 196, y)
        self.ln(3)

    def body_text(self, text: str, bold_phrases: list[str] | None = None) -> None:
        text = ascii_safe(text)
        self._reset_x()
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(*TEXT)
        if not bold_phrases:
            self.multi_cell(0, 4.3, text, new_x="LMARGIN", new_y="NEXT")
            self.ln(1)
            return
        # Simple bold segments
        self.write(4.3, "")
        parts = [text]
        for phrase in bold_phrases:
            new_parts = []
            for part in parts:
                if isinstance(part, tuple):
                    new_parts.append(part)
                    continue
                split = part.split(phrase)
                for i, seg in enumerate(split):
                    if seg:
                        new_parts.append(seg)
                    if i < len(split) - 1:
                        new_parts.append(("B", phrase))
            parts = new_parts
        for part in parts:
            if isinstance(part, tuple):
                self.set_font("Helvetica", "B", 9.5)
                self.write(4.3, part[1])
                self.set_font("Helvetica", "", 9.5)
            else:
                self.write(4.3, part)
        self.ln(4.3)

    def skill_line(self, label: str, value: str) -> None:
        text = ascii_safe(label + value)
        self._reset_x()
        self.set_font("Helvetica", "", 9.3)
        self.set_text_color(*TEXT)
        self.multi_cell(0, 4.2, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.3)

    def job(self, title: str, dates: str, bullets: list[str]) -> None:
        title, dates = ascii_safe(title), ascii_safe(dates)
        bullets = [ascii_safe(b) for b in bullets]
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(*TEXT)
        self.cell(0, 4.8, title, new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "I", 9)
        self.set_text_color(*MUTED)
        self.cell(0, 4.2, dates, new_x="LMARGIN", new_y="NEXT")
        self.ln(0.5)
        self.set_font("Helvetica", "", 9.3)
        self.set_text_color(*TEXT)
        for bullet in bullets:
            self._reset_x()
            self.set_x(self.l_margin + 2)
            self.cell(4, 4.1, "-")
            self.multi_cell(0, 4.1, bullet, new_x="LMARGIN", new_y="NEXT")
        self.ln(1.5)


def build_vip_pdf(path: Path) -> None:
    pdf = CVPDF("Samuli Lahtela CV")
    pdf.add_page()
    pdf.header_block(
        "Samuli Lahtela",
        "Malta, Gzira  |  +358 40 579 5752  |  slahtela98@gmail.com\n"
        "Open to Remote & Relocation",
    )

    pdf.section("Professional Summary")
    pdf.body_text(
        "iGaming professional with 4+ years across VIP player support, live casino operations, "
        "and CRM-driven retention in Malta's regulated market. Experienced in managing high-value "
        "player relationships, monitoring account activity for risk and compliance, and supporting "
        "retention campaigns across casino and sportsbook products."
    )
    pdf.body_text(
        "Fluent in Finnish and English, with a track record of calm escalation handling, cross-team "
        "coordination, and accurate player documentation. Seeking a VIP Account Manager, Player "
        "Retention, or CRM-focused role — remote or international."
    )

    pdf.section("Core Skills")
    pdf.skill_line("Player & CRM:", "VIP relationship management · Player retention & lifecycle · CRM documentation & follow-ups · Responsible gaming · KYC / compliance escalation · Promotions & campaign support")
    pdf.skill_line("Products:", "Online casino · Live casino · Sportsbook · Bonus & wagering workflows")
    pdf.skill_line("Languages:", "Finnish (native) · English (fluent)")

    pdf.section("Professional Experience")
    pdf.job(
        "Customer Relations — Glitnor, Malta",
        "August 2023 – Present",
        [
            "Manage day-to-day contact with players across casino and sportsbook, including VIP and high-value accounts, resolving payment, bonus, verification, and account queries end to end.",
            "Monitor player activity to identify at-risk behaviour, responsible gaming concerns, and compliance flags; escalate to risk, fraud, and management with clear case context.",
            "Support retention initiatives through promotions, campaigns, and personalised player outreach aligned with CRM workflows.",
            "Handle VIP-related queries and sensitive account issues, maintaining service quality under pressure in a fast-paced, regulated environment.",
            "Collaborate with internal teams (payments, compliance, product) to resolve complex cases efficiently and protect player trust and satisfaction.",
            "Maintain accurate interaction records to support handovers, audits, and continuity of high-value player relationships.",
        ],
    )
    pdf.job(
        "Game Presenter / Help Desk — Evolution, Malta",
        "June 2022 – July 2023",
        [
            "Hosted live casino games for an international audience, representing the brand with professionalism and adherence to studio standards.",
            "Built real-time rapport with high-value players at the table, supporting engagement while remaining alert to complaints and escalation needs.",
            "Provided help desk support alongside presenting duties, assisting players with technical and account-related queries between sessions.",
            "Coordinated with studio operations and support teams to resolve issues without disrupting the live player experience.",
        ],
    )

    pdf.section("Education")
    pdf.body_text("Kajaani University of Applied Sciences — 2020 – 2024")

    pdf.section("Additional Information")
    pdf.body_text("Work location: Malta (EU work rights) · Open to fully remote roles with EU time-zone overlap or relocation")
    pdf.body_text("Industry: Regulated iGaming (B2C casino & sportsbook)")

    pdf.output(path)


def build_data_pdf(path: Path) -> None:
    pdf = CVPDF("Samuli Lahtela CV Data CRM")
    pdf.add_page()
    pdf.header_block(
        "Samuli Lahtela",
        "Malta, Gzira  |  +358 40 579 5752  |  slahtela98@gmail.com\n"
        "Open to Remote & Relocation",
    )

    pdf.section("Professional Summary")
    pdf.body_text(
        "iGaming professional with 4+ years in player operations and VIP account handling, combining "
        "frontline CRM experience with data analysis skills to support retention, risk awareness, and "
        "player engagement across casino, sportsbook, and live casino in Malta's regulated market."
    )
    pdf.body_text(
        "Proficient in SQL, Python (Pandas, Matplotlib), and Tableau, with Microsoft Azure (AZ-900, SC-900) "
        "certifications. Fluent in Finnish and English. Targeting VIP Account Manager, CRM / Player Analytics, "
        "or Retention roles."
    )

    pdf.section("Core Skills")
    pdf.skill_line("CRM & Retention:", "VIP player management · Player behaviour analysis · Retention campaigns · RG & compliance escalation")
    pdf.skill_line("Data & Tools:", "SQL · Python (Pandas, Matplotlib) · Tableau · CRM platforms · Azure (AZ-900, SC-900)")
    pdf.skill_line("Products:", "Online casino · Live casino · Sportsbook")
    pdf.skill_line("Languages:", "Finnish (native) · English (fluent)")

    pdf.section("Professional Experience")
    pdf.job(
        "Customer Relations — Glitnor, Malta",
        "August 2023 – Present",
        [
            "Analyse player behaviour and betting patterns to support engagement, retention, and early identification of high-risk accounts.",
            "Monitor VIP player activity for compliance, responsible gaming, and fraud indicators; escalate with documented case history.",
            "Deliver data-informed input to support promotion targeting, risk mitigation, and customer journey improvements.",
            "Manage VIP and standard player queries across casino and sportsbook; support retention campaigns within CRM processes.",
            "Partner with payments, compliance, and product teams on complex escalations while maintaining accurate player records.",
        ],
    )
    pdf.job(
        "Game Presenter / Help Desk — Evolution, Malta",
        "June 2022 – July 2023",
        [
            "Hosted live casino presentations for international players, engaging high-value players in a regulated studio.",
            "Provided help desk support for technical and account queries during live operations.",
        ],
    )

    pdf.section("Education")
    pdf.body_text("Kajaani University of Applied Sciences — 2020 – 2024")

    pdf.section("Certifications")
    pdf.body_text("Microsoft Azure Fundamentals (AZ-900)")
    pdf.body_text("Microsoft Security, Compliance, and Identity Fundamentals (SC-900)")

    pdf.section("Additional Information")
    pdf.body_text("Work location: Malta (EU work rights) · Open to remote or relocation")
    pdf.body_text("Industry: Regulated iGaming (B2C casino & sportsbook)")

    pdf.output(path)


def build_casino_ops_pdf(path: Path) -> None:
    pdf = CVPDF("Samuli Lahtela CV Casino Operations")
    pdf.add_page()
    pdf.header_block(
        "Samuli Lahtela",
        "Malta, Gzira  |  +358 40 579 5752  |  slahtela98@gmail.com\n"
        "Open to Relocation: Limassol, Cyprus (full-time, office-based)",
    )

    pdf.section("Professional Summary")
    pdf.body_text(
        "iGaming operations professional with 4+ years across casino operations, promotion configuration, and "
        "cross-team product support across MGA, SGA (Sweden), Ontario, and Dutch (KSA) regulated markets. "
        "Strong hands-on understanding of registration, deposits, bonuses, gameplay, and withdrawals across "
        "casino and sportsbook products."
    )
    pdf.body_text(
        "Daily user of Jira, Intercom, and Confluence (with Zendesk experience). Experienced reviewing, setting "
        "up, and configuring promotions, escalating product bugs, and coordinating with CRM, VIP, payments, and "
        "compliance teams. Background includes live casino operations at Evolution. Fluent in English and Finnish."
    )

    pdf.section("Core Skills")
    pdf.skill_line("Casino Operations:", "Promotion setup & configuration · Player journey review · Multi-market regulatory awareness · Payment operations · Live casino")
    pdf.skill_line("Product & Cross-Team:", "Jira ticket management · Product bug reporting · Feature rollout validation · CRM / VIP / CS coordination · Confluence documentation")
    pdf.skill_line("Tools & Markets:", "Jira · Intercom · Confluence · Zendesk · MGA · SGA (Sweden) · Ontario · Dutch (KSA) · English (fluent) · Finnish (native)")

    pdf.section("Professional Experience")
    pdf.job(
        "Casino Operations & Product Support — Glitnor, Malta",
        "Senior Customer Agent | August 2023 – Present",
        [
            "Lead day-to-day casino and sportsbook operations across registration, deposits, bonuses, gameplay, and withdrawals across MGA, SGA, Ontario, and Dutch regulated markets.",
            "Review, set up, and configure promotions and bonus campaigns; monitor configurations and flag issues before and after go-live.",
            "Manage product requests, bugs, and improvement tickets in Jira daily; document processes in Confluence.",
            "Handle operational queries through Intercom (daily) and Zendesk; coordinate with CRM, VIP, and Customer Support.",
            "Apply market-specific regulatory knowledge (SGA, Ontario, KSA, MGA) for bonuses, RG, verification, and compliance escalations.",
            "Identify operational issues, escalate to payments, compliance, fraud, and product teams; validate flows during rollouts.",
        ],
    )
    pdf.job(
        "Game Presenter / Help Desk — Evolution, Malta",
        "June 2022 – July 2023",
        [
            "Supported live casino operations in a regulated studio environment for an international player base.",
            "Provided help desk support; escalated platform issues to studio and operations teams.",
            "Identified player experience pain points during live gameplay and coordinated cross-team resolution.",
        ],
    )

    pdf.section("Education")
    pdf.body_text("Kajaani University of Applied Sciences — 2020 – 2024")

    pdf.section("Additional Information")
    pdf.body_text("Relocation: Ready to relocate to Limassol, Cyprus for a full-time office-based role")
    pdf.body_text("Regulatory exposure: Malta (MGA), Sweden (SGA), Ontario (AGCO), Netherlands (KSA)")
    pdf.body_text("Work style: Organised, detail-oriented, comfortable in fast-paced environments")

    pdf.output(path)


def main() -> None:
    outputs = [
        (DIR / "Samuli-Lahtela-CV.pdf", build_vip_pdf),
        (DIR / "Samuli-Lahtela-CV-VIP-CRM.pdf", build_vip_pdf),
        (DIR / "Samuli-Lahtela-CV-Data-CRM.pdf", build_data_pdf),
        (DIR / "Samuli-Lahtela-CV-Casino-Operations-Limassol.pdf", build_casino_ops_pdf),
    ]
    for path, builder in outputs:
        builder(path)
        pages = __import__("pypdf").PdfReader(str(path))
        print(f"Created {path.name} — {len(pages.pages)} page(s), {path.stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
