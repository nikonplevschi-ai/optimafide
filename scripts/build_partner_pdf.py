from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "documents"
CACHE = ROOT / "work" / "partner-pdf-images"
OUT.mkdir(parents=True, exist_ok=True)
CACHE.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(TTFont("Arial", "C:/Windows/Fonts/arial.ttf"))
pdfmetrics.registerFont(TTFont("Arial-Bold", "C:/Windows/Fonts/arialbd.ttf"))

GREEN = colors.HexColor("#173C32")
GOLD = colors.HexColor("#BA9148")
INK = colors.HexColor("#26312D")
MUTED = colors.HexColor("#5C6963")
SOFT = colors.HexColor("#EEF4F0")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="T", fontName="Arial-Bold", fontSize=22, leading=26, textColor=GREEN, spaceAfter=10))
styles.add(ParagraphStyle(name="H", fontName="Arial-Bold", fontSize=15, leading=18, textColor=GREEN, spaceBefore=8, spaceAfter=7))
styles.add(ParagraphStyle(name="B", fontName="Arial", fontSize=10.2, leading=13.5, textColor=INK, spaceAfter=7))
styles.add(ParagraphStyle(name="Small", fontName="Arial", fontSize=8.4, leading=10.5, textColor=MUTED, spaceAfter=5))
styles.add(ParagraphStyle(name="Center", parent=styles["Small"], alignment=TA_CENTER))
styles.add(ParagraphStyle(name="BulletX", parent=styles["B"], leftIndent=14, firstLineIndent=-8, bulletIndent=4))


def jpg(path):
    source = ROOT / path
    target = CACHE / f"{source.stem}.jpg"
    if not target.exists() or target.stat().st_mtime < source.stat().st_mtime:
        PILImage.open(source).convert("RGB").save(target, "JPEG", quality=91)
    return str(target)


def img(path, width=170 * mm, height=None):
    source = jpg(path)
    if height:
        return Image(source, width=width, height=height)
    im = PILImage.open(source)
    return Image(source, width=width, height=width * im.height / im.width)


def p(text, style="B"):
    return Paragraph(text, styles[style])


def bullets(items):
    return [p("• " + item, "BulletX") for item in items]


def note(label, text):
    table = Table([[Paragraph(f"<b>{label}:</b> {text}", styles["B"])]], colWidths=[170 * mm])
    table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), SOFT), ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D4E2DA")), ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return table


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Arial", 7.4)
    canvas.setFillColor(MUTED)
    canvas.drawCentredString(A4[0] / 2, 10 * mm, "Optima Fide  |  accredited residential recovery center in Moldova  |  optimafide.info@gmail.com")
    canvas.restoreState()


story = [
    img("assets/images/hero-center.webp", 170 * mm), Spacer(1, 5 * mm),
    p("OPTIMA FIDE", "Small"),
    p("Optima Fide — accredited residential recovery center in Moldova", "T"),
    p("A practical partner and donor brief about the mission, accreditation, residential program, infrastructure and ways to support the work.", "B"),
    note("Location", "Goianul Nou, Stăuceni, Republic of Moldova. Residential capacity: 20 places."),
    PageBreak(),
    p("Mission of the foundation", "T"),
    p("Optima Fide supports people and families affected by addiction through a structured residential recovery environment, daily rhythm, community support, spiritual accompaniment without pressure and practical reintegration work."),
    *bullets(["Provide a safe residential environment away from destructive habits.", "Support responsibility, work, family relationships and stable daily structure.", "Cooperate with families, churches, social services, specialists, donors and community partners."]),
    p("Accreditation", "H"),
    img("assets/images/accreditation-certificate-clean.webp", 82 * mm),
    p("The center presents a state accreditation certificate for rehabilitation through a therapeutic community for consumers of psychoactive substances and substitution therapy patients.", "Small"),
    PageBreak(),
    p("Residential recovery program", "T"),
    *bullets(["Accommodation, meals and a predictable daily rhythm.", "Group meetings, individual conversations, responsibilities and community life.", "Family orientation and support during the process.", "Optional spiritual support, prayer, silence and meaning without pressure.", "Preparation for reintegration into stable daily life."]),
    note("Medical boundary", "Medical consultations, tests and examinations are arranged through specialized professionals and institutions when needed. Optima Fide does not replace emergency medical care, inpatient psychiatry or emergency detoxification."),
    p("Infrastructure of the center", "H"),
    *bullets(["Residential building in Goianul Nou, Stăuceni.", "20 residential places.", "Dining and common spaces.", "Outdoor courtyard and activity areas.", "Spaces for group meetings and daily community rhythm."]),
    PageBreak(),
    p("Team", "T"),
]

team = [
    ("assets/images/team/team-igor-owner.webp", "Fr. Igor Plevschi", "Foundation president / spiritual accompaniment"),
    ("assets/images/team/team-anastasia-owner.webp", "Anastasia Plevscaia", "Program accompaniment / participant support"),
    ("assets/images/team/team-ruslan-owner.webp", "Ruslan Magari", "Center manager / daily organization"),
    ("assets/images/team/team-oksana-owner.webp", "Oksana Harbolinscaia", "Program coordinator / family and communication"),
    ("assets/images/team/team-tudor-owner.webp", "Tudor Rotaru", "Peer-to-peer consultant"),
]
cells = []
for path, name, role in team:
    cells.append([img(path, 28 * mm, 36 * mm), Paragraph(f"<b>{name}</b><br/>{role}", styles["Small"])])
team_table = Table(cells, colWidths=[34 * mm, 136 * mm])
team_table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F7FAF8")), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D4E2DA")), ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#D4E2DA")), ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
story += [
    team_table,
    PageBreak(),
    p("Results and current scale", "T"),
    *bullets(["19,000+ consultations provided over the years.", "500+ people received help.", "20 residential places in the center.", "State accreditation and a concrete residential location in Moldova."]),
    p("Partnership opportunities", "H"),
    *bullets(["Support residential places, meals, heating, utilities and daily operations.", "Partner on family support, reintegration, training and community outreach.", "Help improve infrastructure, equipment and transportation.", "Cooperate through churches, social services, foundations and professional networks."]),
    PageBreak(),
    p("Bank details and contacts", "T"),
    p("<b>Account name:</b> Fundatia Optima Fide"),
    p("<b>IBAN:</b> MD63VI000000002224729306"),
    p("<b>Bank:</b> B.C. Victoriabank S.A."),
    p("<b>SWIFT:</b> VICBMD2X"),
    p("<b>Fiscal code:</b> 1012620008338"),
    Spacer(1, 4 * mm),
    p("<b>Phone:</b> +373 79 002 064"),
    p("<b>Email:</b> optimafide.info@gmail.com"),
    p("<b>Website:</b> https://nikonplevschi-ai.github.io/optimafide/"),
    p("<b>Address:</b> str. Gloriei nr. 4, s. Goianul Nou, or. Stăuceni, Republic of Moldova", "Small"),
]

SimpleDocTemplate(str(OUT / "optima-fide-partner-offer-en.pdf"), pagesize=A4, rightMargin=20 * mm, leftMargin=20 * mm, topMargin=17 * mm, bottomMargin=18 * mm, title="Optima Fide — accredited residential recovery center in Moldova", author="Optima Fide").build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT / "optima-fide-partner-offer-en.pdf")
