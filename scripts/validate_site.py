from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "index.html"
REQUIRED = [
    "hero-center.webp",
    "team/team-tudor-owner.webp",
    "tourism/tourism-forest-path-owner.webp",
    "assets/pdfs/optima-fide-family-offer-ru.pdf",
    "assets/pdfs/optima-fide-partner-offer-en.pdf",
    'id="activities"',
    'id="optional-services"',
    'id="faq"',
    "additionalFee",
    "firstDaysTitle",
    'id="life-center"',
    'id="recovery-spaces"',
    'class="visual-program-grid"',
    'class="day-scene"',
    'class="day-line"',
    'data-visual-program',
    'data-i18n="dayMorning"',
    'data-i18n="dayDay"',
    'data-i18n="dayAfternoon"',
    'data-i18n="dayEvening"',
    'data-i18n="dayNight"',
    "group-session.webp",
    "personal-consultation.webp",
    "wellness-activity.webp",
    "community-life.webp",
    "outdoor-recovery.webp",
    'data-i18n="illustrativeNote"',
    "excursion-dendrarium.webp",
    "excursion-cascade-park.webp",
    "excursion-history-museum.webp",
    "excursion-ethnography-museum.webp",
    "excursion-water-tower.webp",
]
PROHIBITED = [
    "Andrei Buhna",
    "Андрей Бухна",
    ">AB<",
    "tourism-horse.webp",
    "tourism-orhei.webp",
    "Garbolinskaia",
    "Гарболинская",
    "therapy-session-blurred",
    "community-prayer-blurred",
    "community-celebration-blurred",
    "+373 78 377 337",
    "+373 783 77337",
    "Din 2014",
    "Golanul Nou",
    "Clienți reabilitați",
    "Clienti reabilitati",
    "https://recovery.optimafide.md/",
]


def main() -> int:
    html = HTML_PATH.read_text(encoding="utf-8")
    failures: list[str] = []
    used_keys = set(re.findall(r'data-i18n(?:-alt)?="([^"]+)"', html))

    for lang in ("ro", "ru", "en"):
        start = html.find(f'"{lang}": {{')
        next_starts = [html.find(f'"{other}": {{', start + 1) for other in ("ro", "ru", "en")]
        next_starts = [position for position in next_starts if position > start]
        end = min(next_starts) if next_starts else html.find("const translatable", start)
        match = html[start:end] if start >= 0 and end > start else ""
        if not match:
            failures.append(f"Missing translation dictionary: {lang}")
            continue
        available = set(re.findall(r'"([^"]+)"\s*:', match))
        extensions = re.finditer(
            rf"Object\.assign\(translations\.{lang},\s*\{{(.*?)\n\s*\}}\);",
            html,
            re.DOTALL,
        )
        for extension in extensions:
            available.update(re.findall(r"\b([A-Za-z][A-Za-z0-9]+)\s*:", extension.group(1)))
        missing = sorted(used_keys - available)
        if missing:
            failures.append(f"{lang} missing keys: {', '.join(missing)}")

    refs = re.findall(
        r'(?:src|data-lightbox|content)="((?!https?:|data:|#|mailto:|tel:)[^"]+\.(?:jpg|jpeg|png|webp|pdf))"',
        html,
        re.IGNORECASE,
    )
    refs += re.findall(r'srcset="([^"]+\.(?:jpg|jpeg|png|webp))"', html, re.IGNORECASE)
    for ref in sorted(set(refs)):
        if not (ROOT / ref).exists():
            failures.append(f"Missing local asset: {ref}")

    for item in REQUIRED:
        if item not in html:
            failures.append(f"Missing required content: {item}")
    for item in PROHIBITED:
        if item in html:
            failures.append(f"Prohibited legacy content found: {item}")

    if failures:
        print("\n".join(f"FAIL: {failure}" for failure in failures))
        return 1
    print("Site validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
