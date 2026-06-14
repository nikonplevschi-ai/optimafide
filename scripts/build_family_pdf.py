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
CACHE = ROOT / "work" / "family-pdf-images"
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
styles.add(ParagraphStyle(name="T", fontName="Arial-Bold", fontSize=23, leading=27, textColor=GREEN, spaceAfter=10))
styles.add(ParagraphStyle(name="H", fontName="Arial-Bold", fontSize=16, leading=19, textColor=GREEN, spaceBefore=8, spaceAfter=8))
styles.add(ParagraphStyle(name="B", fontName="Arial", fontSize=10.5, leading=14, textColor=INK, spaceAfter=7))
styles.add(ParagraphStyle(name="Small", fontName="Arial", fontSize=8.5, leading=11, textColor=MUTED, spaceAfter=5))
styles.add(ParagraphStyle(name="Center", parent=styles["Small"], alignment=TA_CENTER))
styles.add(ParagraphStyle(name="BulletX", parent=styles["B"], leftIndent=14, firstLineIndent=-8, bulletIndent=4))
styles.add(ParagraphStyle(name="TeamName", fontName="Arial-Bold", fontSize=9.4, leading=11.3, textColor=GREEN, spaceAfter=2))
styles.add(ParagraphStyle(name="TeamRole", fontName="Arial-Bold", fontSize=7.7, leading=9.2, textColor=GOLD, spaceAfter=3))
styles.add(ParagraphStyle(name="TeamDesc", fontName="Arial", fontSize=7.4, leading=9.1, textColor=INK, spaceAfter=0))


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
    gap = 6 * mm
    rows = [
        [team_card(*team[0], width=card_w), team_card(*team[1], width=card_w)],
        [team_card(*team[2], width=card_w), team_card(*team[3], width=card_w)],
        ["", team_card(*team[4], width=card_w), ""],
    ]
    grid = Table(rows[:2], colWidths=[card_w, card_w], hAlign="CENTER")
    grid.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    centered_last = Table([rows[2]], colWidths=[(170 * mm - card_w) / 2, card_w, (170 * mm - card_w) / 2], hAlign="CENTER")
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
    canvas.setFont("Arial", 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawCentredString(A4[0] / 2, 10 * mm, "Optima Fide  |  Goianul Nou, Stăuceni  |  +373 79 002 064  |  optimafide.info@gmail.com")
    canvas.restoreState()


story = [
    img("assets/images/hero-center.webp", 170 * mm), Spacer(1, 5 * mm),
    p("OPTIMA FIDE", "Small"), p("Optima Fide — программа восстановления с проживанием", "T"),
    p("Резиденциальная программа восстановления в аккредитованном центре в Молдове", "H"),
    p("Проживание, питание, ежедневный ритм, терапевтическое сообщество и поддержка семьи."),
    note("Первый шаг", "спокойный конфиденциальный разговор. Он не обязывает к поступлению в центр."),
    Spacer(1, 4 * mm), p("Резиденциальный центр Optima Fide, Гоянул Ноу, Стэучень", "Small"),
    PageBreak(),
    p("Когда программа может помочь", "T"),
    p("Без обещаний мгновенного результата и без давления", "Small"),
    *bullets(["Человек хочет выйти из зависимости, но одному не получается.", "После срыва нужен новый старт в безопасной среде.", "Дома много соблазнов, конфликтов или нестабильности.", "Нужно восстановить ответственность, труд, отношения и здоровый ритм.", "Семья ищет понятный и бережный способ помочь близкому."]),
    p("Что даёт резиденциальный формат", "H"),
    *bullets(["спокойное проживание и регулярное питание", "предсказуемый ежедневный ритм", "группы, личные беседы и общие обязанности", "поддержку семьи", "движение, общение и подготовку к возвращению в жизнь"]),
    note("Важно", "программа не заменяет неотложную медицинскую помощь, стационарную психиатрию или экстренную детоксикацию."),
    PageBreak(),
    p("Как проходит жизнь в центре", "T"), p("Порядок, общение, ответственность и восстановление", "Small"),
    img("assets/images/hero-center.webp", 120 * mm), Spacer(1, 3 * mm),
    *[p(f"<b>{a}.</b> {b}") for a, b in [("Утро", "порядок, личная гигиена, завтрак и настрой на день."), ("День", "группы, обязанности, индивидуальная работа и обучение."), ("После обеда", "активность, спорт, двор, прогулки и практические дела."), ("Вечер", "общение, тишина, молитва по желанию и подведение итогов."), ("Ночь", "отдых и восстановление сна.")]],
    p("Активности как часть восстановления", "H"),
    p("Бильярд развивает внимание и выдержку; пинг-понг поддерживает движение и реакцию; футбол помогает командности и дисциплине; общие трапезы и зона мангала создают простую семейную атмосферу."),
    PageBreak(),
    p("Люди, которые сопровождают процесс", "T"), p("В команде сочетаются организационный опыт, поддержка участников, связь с семьёй и ежедневное сопровождение в центре.", "Small"),
]

team = [
    ("assets/images/team/team-igor-owner.webp", "о. Игорь Плевский", "Президент фонда / духовное сопровождение", "Координирует миссию фонда, партнёрства и духовное измерение программы."),
    ("assets/images/team/team-anastasia-owner.webp", "Анастасия Плевская", "Сопровождение программы / поддержка участников", "Помогает участникам сохранять ежедневный ритм и включаться в процесс восстановления."),
    ("assets/images/team/team-ruslan-owner.webp", "Руслан Магари", "Менеджер центра / ежедневная организация", "Отвечает за порядок, условия проживания и практическую жизнь центра."),
    ("assets/images/team/team-oksana-owner.webp", "Оксана Харболинская", "Координатор программы / семья и коммуникация", "Помогает в коммуникации с участниками, семьями и в организации сопровождения."),
    ("assets/images/team/team-tudor-owner.webp", "Тудор Ротарь", "Консультант «равный равному»", "Поддерживает участников через личный опыт, общение и практическое сопровождение."),
]
story += [*team_grid(team), PageBreak(), p("Что входит и что оплачивается отдельно", "T"), p("Честное разделение базовой программы и дополнительных возможностей", "Small"), p("В базовую программу входит", "H"), *bullets(["проживание и питание", "ежедневный ритм, группы и сопровождение", "поддержка семьи и духовная поддержка по желанию", "активности на территории центра", "подготовка к реинтеграции"]), p("По согласованию и за отдельную плату", "H"), *bullets(["восстановительные поездки по Молдове", "массаж и парикмахер", "консультации профильных специалистов", "анализы и обследования через профильные учреждения", "индивидуальный транспорт, сопровождение и запись к специалистам"]), note("Важно", "восстановительные поездки и дополнительные услуги не являются обязательной частью программы. Они доступны по согласованию, с учётом состояния участника и правил центра, и оплачиваются отдельно."), PageBreak(), p("Спокойная смена обстановки", "T"), p("Восстановительные поездки по Молдове", "Small")]

for path, cap in [("assets/images/tourism/tourism-church-owner.webp", "Церкви и монастыри: тишина, молитва, внутреннее восстановление."), ("assets/images/tourism/tourism-park-lake-owner.webp", "Озеро и парк: отдых у воды и созерцание."), ("assets/images/tourism/tourism-forest-path-owner.webp", "Лесные тропы: прогулки и восстановление ритма.")]:
    story += [img(path, 95 * mm), p(cap, "Center")]
story += [note("Условие", "любые выезды организуются только по предварительному согласованию и за отдельную плату."), PageBreak(), p("Как начать", "T"), p("Простой путь от первого разговора до приезда", "Small")]
for n, text in enumerate(["Позвонить или написать в Telegram.", "Спокойно обсудить ситуацию, состояние и мотивацию.", "Согласовать условия, документы, необходимые вещи и дату приезда.", "Приехать в центр и пройти спокойную адаптацию первых дней."], 1):
    story.append(p(f"<b>{n}. {text}</b>"))
story += [p("Частые вопросы", "H")]
for q, a in [("Можно ли сначала просто поговорить?", "Да. Первый разговор конфиденциален и не обязывает к поступлению."), ("Есть ли проживание и питание?", "Да, они входят в резиденциальную программу."), ("Можно ли семье обратиться без самого человека?", "Да. Семья может получить ориентирование по возможным следующим шагам."), ("Есть ли медицинские консультации?", "При необходимости они организуются отдельно через профильных специалистов и учреждения.")]:
    story += [p(f"<b>{q}</b>"), p(a)]
story += [p("Контакты", "H"), p("<b>+373 79 002 064</b>"), p("optimafide.info@gmail.com  |  Telegram: @optimafide"), p("Goianul Nou, Stăuceni, Republica Moldova", "Small")]

SimpleDocTemplate(str(OUT / "optima-fide-family-offer-ru.pdf"), pagesize=A4, rightMargin=20 * mm, leftMargin=20 * mm, topMargin=17 * mm, bottomMargin=18 * mm, title="Optima Fide — программа восстановления с проживанием", author="Optima Fide").build(story, onFirstPage=footer, onLaterPages=footer)
print(OUT / "optima-fide-family-offer-ru.pdf")
