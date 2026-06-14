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
OUT = ROOT / "assets" / "pdfs"
CACHE = ROOT / "work" / "partner-pdf-images"
PDF_TEAM_DIR = ROOT / "assets" / "images" / "team" / "pdf"
OUT.mkdir(parents=True, exist_ok=True)
CACHE.mkdir(parents=True, exist_ok=True)
PDF_TEAM_DIR.mkdir(parents=True, exist_ok=True)

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
styles.add(ParagraphStyle(name="TeamName", fontName="Arial-Bold", fontSize=9.2, leading=11, textColor=GREEN, spaceAfter=2))
styles.add(ParagraphStyle(name="TeamRole", fontName="Arial-Bold", fontSize=7.6, leading=9, textColor=GOLD, spaceAfter=3))
styles.add(ParagraphStyle(name="TeamDesc", fontName="Arial", fontSize=7.3, leading=9, textColor=INK, spaceAfter=0))


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


def team_photo(path):
    source = ROOT / path
    target = PDF_TEAM_DIR / f"{source.stem}-4x5.jpg"
    updated_after = max(source.stat().st_mtime, Path(__file__).stat().st_mtime)
    if not target.exists() or target.stat().st_mtime < updated_after:
        with PILImage.open(source).convert("RGB") as im:
            ratio = 4 / 5
            width, height = im.size
            if width / height > ratio:
                crop_height = int(height * 0.68)
                new_width = int(crop_height * ratio)
                left = max(0, (width - new_width) // 2)
                top = max(0, int((height - crop_height) * 0.15))
                box = (left, top, left + new_width, top + crop_height)
            else:
                new_height = int(width / ratio)
                top = max(0, min(height - new_height, int((height - new_height) * 0.18)))
                box = (0, top, width, top + new_height)
            im.crop(box).resize((800, 1000), PILImage.LANCZOS).save(target, "JPEG", quality=92)
    return Image(str(target), width=30 * mm, height=37.5 * mm)


def p(text, style="B"):
    return Paragraph(text, styles[style])


def bullets(items):
    return [p("• " + item, "BulletX") for item in items]


def note(label, text):
    table = Table([[Paragraph(f"<b>{label}:</b> {text}", styles["B"])]], colWidths=[170 * mm])
    table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), SOFT), ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D4E2DA")), ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    return table


def team_card(path, name, role, description, width=82 * mm):
    text = [Paragraph(name, styles["TeamName"]), Paragraph(role, styles["TeamRole"]), Paragraph(description, styles["TeamDesc"])]
    card = Table([[team_photo(path), text]], colWidths=[34 * mm, width - 34 * mm])
    card.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F7FAF8")),
        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D4E2DA")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return card


def team_grid(team):
    card_w = 82 * mm
    grid = Table([
        [team_card(*team[0], width=card_w), team_card(*team[1], width=card_w)],
        [team_card(*team[2], width=card_w), team_card(*team[3], width=card_w)],
    ], colWidths=[card_w, card_w], hAlign="CENTER")
    grid.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    centered_last = Table([["", team_card(*team[4], width=card_w), ""]], colWidths=[(170 * mm - card_w) / 2, card_w, (170 * mm - card_w) / 2], hAlign="CENTER")
    centered_last.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))
    return [grid, centered_last]


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
    p("The team combines organizational experience, participant support, family communication and daily accompaniment.", "Small"),
]

team = [
    ("assets/images/team/team-igor-owner.webp", "Fr. Igor Plevschi", "Foundation president / spiritual accompaniment", "Coordinates the mission, partnerships and the spiritual dimension of the program."),
    ("assets/images/team/team-anastasia-owner.webp", "Anastasia Plevscaia", "Program accompaniment / participant support", "Supports participants in daily rhythm and engagement in the recovery process."),
    ("assets/images/team/team-ruslan-owner.webp", "Ruslan Magari", "Center manager / daily organization", "Responsible for order, stay conditions and practical daily life in the center."),
    ("assets/images/team/team-oksana-owner.webp", "Oksana Harbolinscaia", "Program coordinator / family communication", "Supports communication with participants, families and the accompaniment process."),
    ("assets/images/team/team-tudor-owner.webp", "Tudor Rotaru", "Peer-to-peer consultant", "Supports participants through personal experience, communication and practical accompaniment."),
]
story += [
    *team_grid(team),
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
