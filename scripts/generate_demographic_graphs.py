#!/usr/bin/env python3
"""Generate the five-page focus-group demographic dashboard PDF.

Install the only dependency and run:

    python -m pip install reportlab
    python scripts/generate_demographic_graphs.py

Use ``--output`` to choose a different destination.
"""

from argparse import ArgumentParser
from pathlib import Path

from reportlab.lib.colors import Color, HexColor
from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas


PAGE_W, PAGE_H = landscape(letter)
INK = HexColor("#17324D")
MUTED = HexColor("#617487")
GRID = HexColor("#DDE5EB")
PAPER = HexColor("#F7F9FB")
TEAL = HexColor("#008C95")
GREEN = HexColor("#67A33F")
PURPLE = HexColor("#6B4FB3")
PINK = HexColor("#D0447A")

COUNTRY_COLORS = {
    "United States": HexColor("#0072B2"),
    "Germany": HexColor("#E69F00"),
    "China": HexColor("#D55E00"),
    "Australia": HexColor("#009E73"),
    "Philippines": HexColor("#CC79A7"),
    "South Korea": HexColor("#56B4E9"),
    "Scotland (UK)": HexColor("#6F4E9C"),
}

COUNTRIES = [
    ("United States", -100.0, 39.0),
    ("Germany", 10.4, 51.2),
    ("China", 104.2, 35.9),
    ("Australia", 133.8, -25.3),
    ("Philippines", 121.8, 12.9),
    ("South Korea", 127.8, 36.5),
    ("Scotland (UK)", -4.2, 56.5),
]

TEAMS = [
    "Global HR Business Partners", "Process Solutions", "Discovery Research",
    "Communications & Branding", "Advanced Solutions", "Research & Development",
    "Learning & Development", "Compliance", "Global Belonging & Inclusion", "Sales",
]

ROLES = [
    "Marketing", "AI Solutions", "Supply Chain Management", "Data Analytics",
    "Healthcare Administration", "Life Science Sales", "Capital Expenditure Management",
    "Corporate Affairs", "Medical Affairs", "Mechanical Engineer", "Process Engineer",
    "Scientist", "Strategy Realization",
]


def page_base(pdf, number, title, subtitle):
    pdf.setFillColor(PAPER)
    pdf.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 23)
    pdf.drawString(42, PAGE_H - 52, title)
    pdf.setFillColor(MUTED)
    pdf.setFont("Helvetica", 10)
    pdf.drawString(42, PAGE_H - 69, subtitle)
    pdf.setStrokeColor(GRID)
    pdf.line(42, PAGE_H - 82, PAGE_W - 42, PAGE_H - 82)
    pdf.setFillColor(MUTED)
    pdf.setFont("Helvetica", 8)
    pdf.drawString(42, 24, "FOCUS GROUP DEMOGRAPHIC COVERAGE")
    pdf.drawRightString(PAGE_W - 42, 24, f"{number} / 5")


def dot(pdf, x, y, radius, color, stroke=None):
    pdf.setFillColor(color)
    pdf.setStrokeColor(stroke or color)
    pdf.circle(x, y, radius, fill=1, stroke=1 if stroke else 0)


def study_scale(pdf):
    page_base(pdf, 1, "Study scale", "Participation and session structure")
    for i in range(35):
        row, col = divmod(i, 10)
        dot(pdf, 52 + col * 27, PAGE_H - 135 - row * 27, 7.2, TEAL)
    pdf.setFillColor(MUTED)
    pdf.setFont("Helvetica", 9)
    pdf.drawString(52, PAGE_H - 253, "Each dot represents one participant")
    for idx, (value, label) in enumerate([("35", "participants"), ("5", "sessions"), ("40", "minutes each")]):
        y = PAGE_H - 155 - idx * 90
        pdf.setFillColor(INK)
        pdf.setFont("Helvetica-Bold", 38)
        pdf.drawString(410, y, value)
        pdf.setFillColor(MUTED)
        pdf.setFont("Helvetica", 13)
        pdf.drawString(487, y + 7, label)
    colors = [TEAL, GREEN, PURPLE, PINK, HexColor("#E69F00")]
    for i, color in enumerate(colors):
        x = 52 + i * 134
        pdf.setStrokeColor(color)
        pdf.setLineWidth(10)
        pdf.line(x, 130, x + 115, 130)
        pdf.setFillColor(MUTED)
        pdf.setFont("Helvetica", 8)
        pdf.drawCentredString(x + 57.5, 112, f"SESSION {i + 1}")
    pdf.showPage()


def demographic_breadth(pdf):
    page_base(pdf, 2, "Demographic breadth", "Distinct categories represented in the provided demographic notes")
    rows = [("Countries", 7), ("Cities", 17), ("Sectors", 3), ("Teams", 10), ("Roles", 13)]
    for index, (label, value) in enumerate(rows):
        y = PAGE_H - 135 - index * 66
        pdf.setFillColor(INK)
        pdf.setFont("Helvetica", 12)
        pdf.drawRightString(167, y - 4, label)
        pdf.setFillColor(GRID)
        pdf.roundRect(185, y - 10, 500, 20, 10, fill=1, stroke=0)
        pdf.setFillColor(TEAL)
        pdf.roundRect(185, y - 10, 500 * value / 17, 20, 10, fill=1, stroke=0)
        pdf.setFillColor(INK)
        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(698, y - 5, str(value))
    pdf.setFillColor(MUTED)
    pdf.setFont("Helvetica-Oblique", 9)
    pdf.drawString(185, 105, "Bars compare category counts, not participant distribution.")
    pdf.showPage()


def career_span(pdf):
    page_base(pdf, 3, "Career and age span", "Approximate participant coverage from internship through early professional experience")
    x0, x1, y = 95, PAGE_W - 95, 300
    for i in range(140):
        t = i / 139
        color = Color(GREEN.red * (1 - t) + TEAL.red * t, GREEN.green * (1 - t) + TEAL.green * t, GREEN.blue * (1 - t) + TEAL.blue * t)
        pdf.setStrokeColor(color)
        pdf.setLineWidth(12)
        pdf.line(x0 + (x1 - x0) * i / 140, y, x0 + (x1 - x0) * (i + 1) / 140, y)
    for x in (x0, x1):
        dot(pdf, x, y, 11, PAPER, TEAL)
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawString(x0, y + 62, "Approx. age 20")
    pdf.drawRightString(x1, y + 62, "Approx. age 30")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(x0, y + 38, "Rising sophomore intern")
    pdf.drawRightString(x1, y + 38, "Working professional")
    pdf.setFillColor(MUTED)
    pdf.setFont("Helvetica", 11)
    pdf.drawRightString(x1, y - 44, "Up to 7 years of experience")
    for label, t in [("Intern", 0.05), ("Early career", 0.5), ("Working professional", 0.95)]:
        x = x0 + (x1 - x0) * t
        pdf.setStrokeColor(GRID)
        pdf.setLineWidth(1)
        pdf.line(x, y - 12, x, y - 68)
        pdf.setFillColor(MUTED)
        pdf.setFont("Helvetica", 9)
        pdf.drawCentredString(x, y - 83, label)
    pdf.showPage()


def project(lon, lat, x, y, width, height):
    return x + (lon + 180) / 360 * width, y + (lat + 90) / 180 * height


def global_footprint(pdf):
    page_base(pdf, 4, "Global footprint", "Seven countries represented - colors indicate location, not participant volume")
    gx, gy, gw, gh = 55, 140, 510, 285
    pdf.setFillColor(HexColor("#EDF2F5"))
    pdf.roundRect(gx, gy, gw, gh, 18, fill=1, stroke=0)
    for lon in range(-120, 181, 60):
        x, _ = project(lon, 0, gx, gy, gw, gh)
        pdf.setStrokeColor(GRID)
        pdf.line(x, gy + 10, x, gy + gh - 10)
    for lat in range(-60, 61, 30):
        _, y = project(0, lat, gx, gy, gw, gh)
        pdf.setStrokeColor(GRID)
        pdf.line(gx + 10, y, gx + gw - 10, y)
    for name, lon, lat in COUNTRIES:
        x, y = project(lon, lat, gx, gy, gw, gh)
        dot(pdf, x, y, 8, COUNTRY_COLORS[name], PAPER)
    pdf.setFillColor(MUTED)
    pdf.setFont("Helvetica", 8)
    pdf.drawString(gx, gy - 17, "Geographic position is approximate; this is a coverage plot rather than a participant-density map.")
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(605, PAGE_H - 130, "COUNTRIES")
    for index, (name, _, _) in enumerate(COUNTRIES):
        y = PAGE_H - 162 - index * 38
        dot(pdf, 612, y + 3, 6, COUNTRY_COLORS[name])
        pdf.setFillColor(INK)
        pdf.setFont("Helvetica", 10)
        pdf.drawString(628, y, name)
    pdf.showPage()


def inventory(pdf, title, items, x, y, width, color):
    pdf.setFillColor(INK)
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(x, y, f"{title}  {len(items)}")
    y -= 30
    for item in items:
        dot(pdf, x + 5, y + 3, 4.2, color)
        pdf.setFillColor(INK)
        pdf.setFont("Helvetica", 9.5)
        if stringWidth(item, "Helvetica", 9.5) > width - 22:
            words = item.split()
            middle = max(1, len(words) // 2)
            pdf.drawString(x + 18, y, " ".join(words[:middle]))
            y -= 12
            pdf.drawString(x + 18, y, " ".join(words[middle:]))
        else:
            pdf.drawString(x + 18, y, item)
        y -= 27


def professional_perspectives(pdf):
    page_base(pdf, 5, "Professional perspectives", "Team and role coverage; no team-to-role relationship or frequency was provided")
    inventory(pdf, "TEAMS", TEAMS, 55, PAGE_H - 120, 310, GREEN)
    inventory(pdf, "ROLES", ROLES, 420, PAGE_H - 120, 320, PURPLE)
    pdf.showPage()


def build(output):
    output.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    pdf.setTitle("Focus Group Demographic Coverage Dashboard")
    for render in (study_scale, demographic_breadth, career_span, global_footprint, professional_perspectives):
        render(pdf)
    pdf.save()


if __name__ == "__main__":
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("focus-group-demographic-dashboard.pdf"))
    args = parser.parse_args()
    build(args.output.resolve())
    print(args.output.resolve())
