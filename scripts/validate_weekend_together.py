from pathlib import Path
import re


html = (Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8")

required = {
    'id="weekend-together"': "section",
    'data-i18n="weekendTitle"': "localized title",
    'data-i18n="supportWeekend"': "form option",
    'href="https://t.me/optimafide_bot"': "Telegram CTA",
    'weekendBook: "Discută formatul"': "Romanian discuss-format CTA",
    'weekendBook: "Обсудить формат"': "Russian discuss-format CTA",
    'weekendBook: "Discuss the format"': "English discuss-format CTA",
    'data-i18n="faqWeekend1Q"': "weekend FAQ 1",
    'data-i18n="faqWeekend2Q"': "weekend FAQ 2",
    'data-i18n="faqWeekend3Q"': "weekend FAQ 3",
    ".hero::before": "full-width hero mist",
    "object-position: 44% center": "building shift",
    "aspect-ratio: 595 / 842": "upright certificate frame",
    ".weekend-media img { position: absolute; inset: 0;": "full-height weekend image",
}

missing = [label for marker, label in required.items() if marker not in html]
assert not missing, "Missing Weekend Together contract: " + ", ".join(missing)

translation_keys = (
    "weekendTitle",
    "weekendSubtitle",
    "supportWeekend",
    "faqWeekend1Q",
    "faqWeekend3A",
)
for language in ("ro", "ru", "en"):
    blocks = re.findall(
        rf"Object\.assign\(translations\.{language},\s*\{{(.*?)\n\s*\}}\);",
        html,
        flags=re.DOTALL,
    )
    combined = "\n".join(blocks)
    for key in translation_keys:
        assert re.search(rf"\b{key}\s*:", combined), f"{key} missing from {language}"

section_start = html.index('id="weekend-together"')
section_end = html.find("</section>", section_start)
section = html[section_start:section_end]
for forbidden in (
    "4 900 MDL",
    "3 500 MDL",
    "+1 400 MDL",
    "1 000 MDL",
    "weekend-pricing",
    "weekend-price",
):
    assert forbidden not in section

assert "MDL" not in section, "Weekend section must not display service amounts"

print("Weekend Together contract: OK")
