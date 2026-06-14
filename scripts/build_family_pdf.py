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
CACHE = ROOT / "work" / "family-pdf-images"
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
styles.add(ParagraphStyle(name="T", fontName="Arial-Bold", fontSize=23, leading=27, textColor=GREEN, spaceAfter=10))
styles.add(ParagraphStyle(name="H", fontName="Arial-Bold", fontSize=16, leading=19, textColor=GREEN, spaceBefore=8, spaceAfter=8))
styles.add(ParagraphStyle(name="B", fontName="Arial", fontSize=10.5, leading=14, textColor=INK, spaceAfter=7))
styles.add(ParagraphStyle(name="Small", fontName="Arial", fontSize=8.5, leading=11, textColor=MUTED, spaceAfter=5))
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
    p("Люди, которые сопровождают процесс", "T"), p("Организационный опыт, поддержка участников и связь с семьёй", "Small"),
]

team = [
    ("assets/images/team/team-igor-owner.webp", "о. Игорь Плевский", "Президент фонда / духовное сопровождение"),
    ("assets/images/team/team-anastasia-owner.webp", "Анастасия Плевская", "Сопровождение программы / поддержка участников"),
    ("assets/images/team/team-ruslan-owner.webp", "Руслан Магари", "Менеджер центра / ежедневная организация"),
    ("assets/images/team/team-oksana-owner.webp", "Оксана Харболинская", "Координатор программы / семья и коммуникация"),
    ("assets/images/team/team-tudor-owner.webp", "Тудор Ротарь", "Консультант «равный равному»"),
]
cells = []
for path, name, role in team:
    cells.append([img(path, 28 * mm, 36 * mm), Paragraph(f"<b>{name}</b><br/>{role}", styles["Small"])])
team_table = Table(cells, colWidths=[34 * mm, 136 * mm])
team_table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F7FAF8")), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D4E2DA")), ("INNERGRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#D4E2DA")), ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
story += [team_table, PageBreak(), p("Что входит и что оплачивается отдельно", "T"), p("Честное разделение базовой программы и дополнительных возможностей", "Small"), p("В базовую программу входит", "H"), *bullets(["проживание и питание", "ежедневный ритм, группы и сопровождение", "поддержка семьи и духовная поддержка по желанию", "активности на территории центра", "подготовка к реинтеграции"]), p("По согласованию и за отдельную плату", "H"), *bullets(["восстановительные поездки по Молдове", "массаж и парикмахер", "консультации профильных специалистов", "анализы и обследования через профильные учреждения", "индивидуальный транспорт, сопровождение и запись к специалистам"]), note("Важно", "восстановительные поездки и дополнительные услуги не являются обязательной частью программы. Они доступны по согласованию, с учётом состояния участника и правил центра, и оплачиваются отдельно."), PageBreak(), p("Спокойная смена обстановки", "T"), p("Восстановительные поездки по Молдове", "Small")]

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
