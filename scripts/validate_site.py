from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "index.html"
GOOGLE_VERIFICATION_PATH = ROOT / "google696019cf5de45d47.html"
GOOGLE_VERIFICATION_CONTENT = "google-site-verification: google696019cf5de45d47.html"
ROBOTS_PATH = ROOT / "robots.txt"
SITEMAP_PATH = ROOT / "sitemap.xml"
TELEGRAM_WORKER_PATH = ROOT / "cloudflare-worker" / "telegram-request-worker.js"
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
    "spaces-yard.webp",
    'data-i18n="illustrativeNote"',
    'id="group-support"',
    'id="personal-guidance"',
    'id="activity-movement"',
    'class="visual-story',
    'class="family-questions"',
    "life-center.webp",
    "spaces-group-room.webp",
    "spaces-yard.webp",
    "spaces-chapel.webp",
    "excursion-dendrarium.webp",
    "excursion-cascade-park.webp",
    "excursion-history-museum.webp",
    "excursion-ethnography-museum.webp",
    "excursion-water-tower.webp",
    "team/team-ruslan-owner-2026.png",
    "team/team-oksana-owner-2026.png",
    "visual/daily-rhythm-hq.png",
    "visual/group-support-owner.jpg",
    "visual/family-help-owner.jpg",
    "family-support.webp",
    "center-stairs.jpg",
    'class="hero hero--calm"',
    'class="hero-trust-line"',
    "assets/images/hero/hero-center-premium.webp",
    ".hero--family .hero-frame",
    ".hero--trust .hero-frame",
    "@media (prefers-reduced-motion: reduce)",
    '<meta name="google-site-verification" content="xZ_T9EjYJ_9vJWXbHZWo5uzpubsGZZ5qbSsYukcCPgQ">',
    '<link rel="canonical" href="https://optimafide.pages.dev/">',
    '<meta property="og:url" content="https://optimafide.pages.dev/">',
    '<title>Optima Fide — centru rezidențial de recuperare în Moldova</title>',
    '<meta name="description" content="Cazare, masă, program rezidențial de recuperare, sprijin pentru familie și acreditare de stat la centrul Optima Fide din Moldova.">',
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
    "+373 783 77337",
    "Din 2014",
    "Golanul Nou",
    "Clienți reabilitați",
    "Clienti reabilitati",
    "team-photo-anastasia",
    "assets/images/visual/spaces-main.webp",
    "assets/images/visual/spaces-dining.webp",
    "assets/images/visual/stairs.webp",
]

EXPECTED_RESOURCE_CTA = {
    "ro": {
        "familyPdfCta": "Descarcă PDF",
        "partnerPdfCta": "Descarcă PDF",
        "priceDocxCta": "Descarcă Word",
        "consultCta": "Contactează-ne",
    },
    "ru": {
        "familyPdfCta": "Скачать PDF",
        "partnerPdfCta": "Скачать PDF",
        "priceDocxCta": "Скачать Word",
        "consultCta": "Связаться",
    },
    "en": {
        "familyPdfCta": "Download PDF",
        "partnerPdfCta": "Download PDF",
        "priceDocxCta": "Download Word",
        "consultCta": "Contact us",
    },
}

EXPECTED_TRANSLATIONS = {
    "ro": {
        "badgeAccreditation": "Acreditare de stat",
        "badgeDuration": "Program 6–12 luni",
        "badgeBoard": "Cazare și masă",
        "badgeFamily": "20 locuri",
        "badgePlace": "Goianul Nou, Stăuceni",
        "heroTitle": "Un loc unde te poți opri și începe din nou",
        "heroLead": "Program rezidențial de recuperare: cazare, masă, ritm zilnic, comunitate terapeutică și sprijin pentru familie.",
        "heroConsult": "Solicită o consultație",
        "telegramCta": "Scrie în Telegram",
        "heroTrustLine": "Acreditare · 20 locuri · 500+ persoane sprijinite · confidențial",
        "hallwayCaption": "Spațiu pentru liniște și concentrare",
        "dayMorning": "Dimineața",
        "dayDay": "Ziua",
        "dayAfternoon": "După-amiaza",
        "dayEvening": "Seara",
    },
    "ru": {
        "badgeAccreditation": "Государственная аккредитация",
        "badgeDuration": "Программа 6–12 месяцев",
        "badgeBoard": "Проживание и питание",
        "badgeFamily": "20 мест",
        "badgePlace": "Goianul Nou, Stăuceni",
        "heroTitle": "Место, где можно остановиться и начать заново",
        "heroLead": "Резиденциальная программа восстановления: проживание, питание, ежедневный ритм, сообщество и поддержка семьи.",
        "heroConsult": "Запросить консультацию",
        "telegramCta": "Написать в Telegram",
        "heroTrustLine": "Аккредитация · 20 мест · 500+ человек получили помощь · конфиденциально",
        "hallwayCaption": "Пространство для тихого отдыха и концентрации",
        "dayMorning": "Утро",
        "dayDay": "День",
        "dayAfternoon": "После обеда",
        "dayEvening": "Вечер",
    },
    "en": {
        "badgeAccreditation": "State accreditation",
        "badgeDuration": "6–12 month program",
        "badgeBoard": "Accommodation and meals",
        "badgeFamily": "20 places",
        "badgePlace": "Goianul Nou, Stăuceni",
        "heroTitle": "A place to pause, recover and begin again",
        "heroLead": "A residential recovery program with accommodation, meals, daily rhythm, community support and family guidance.",
        "heroConsult": "Request a consultation",
        "telegramCta": "Write on Telegram",
        "heroTrustLine": "Accredited · 20 residential places · 500+ people supported · confidential",
        "hallwayCaption": "Space for quiet rest and concentration",
        "dayMorning": "Morning",
        "dayDay": "Day",
        "dayAfternoon": "Afternoon",
        "dayEvening": "Evening",
    },
}

EXPECTED_TEAM_CONTACTS = {
    "Igor Plevschi": ("+37378377337", "+373 78 377 337", "general.optimafide@gmail.com"),
    "Anastasia Plevscaia": ("+37360679547", "+373 60 679 547", "optimafide.psiholog@gmail.com"),
    "Ruslan Magari": ("+37379002064", "+373 79 002 064", "ruslanmagari@gmail.com"),
    "Oksana Harbolinscaia": ("+37378601352", "+373 78 601 352", "psyneverlie@gmail.com"),
    "Tudor Rotaru": ("+37362139361", "+373 62 139 361", "sofos82@mail.ru"),
}

DESIGN_SYSTEM_REQUIREMENTS = [
    "--of-bg: #f5efe4",
    "--of-surface: #fffaf1",
    "--of-surface-soft: #f8f2e7",
    "--of-surface-glass: rgba(255, 250, 241, 0.82)",
    "--of-green-deep: #06261f",
    "--of-green-main: #0b372c",
    "--of-green-soft: #dfe8dc",
    "--of-sage: #8fa086",
    "--of-sage-dark: #65785f",
    "--of-sage-light: #eef3ea",
    "--of-gold: #c99a3d",
    "--of-gold-soft: #d9b86c",
    "--of-gold-hover: #b8872f",
    "--of-text: #10251f",
    "--of-muted: #65736b",
    "--of-muted-soft: #87928b",
    "--of-border: rgba(16, 37, 31, 0.11)",
    "--of-border-strong: rgba(16, 37, 31, 0.18)",
    "--of-shadow-soft: 0 18px 55px rgba(18, 44, 36, 0.11)",
    "--of-shadow-card: 0 12px 34px rgba(18, 44, 36, 0.08)",
    "--of-shadow-hover: 0 22px 70px rgba(18, 44, 36, 0.14)",
    'class="mobile-cta-label"',
    'data-i18n="mobileMore"',
    'https://wa.me/37379002064',
    'https://www.facebook.com/profile.php?id=100064660152285',
    'https://t.me/optimafide_bot',
    'viber://chat?number=%2B37379002064',
    'class="intake-intro"',
    'class="brand-emblem"',
    'class="brand-emblem"><img src="logo.jpg"',
    'href="https://wa.me/37379002064"',
]


def main() -> int:
    html = HTML_PATH.read_text(encoding="utf-8")
    failures: list[str] = []

    for requirement in DESIGN_SYSTEM_REQUIREMENTS:
        if requirement not in html:
            failures.append(f"Missing design-system contract: {requirement}")

    confirmed_links = {
        "WhatsApp": ("https://wa.me/37379002064", 3),
        "Facebook": ("https://www.facebook.com/profile.php?id=100064660152285", 4),
        "Telegram": ("https://t.me/optimafide_bot", 6),
        "Viber": ("viber://chat?number=%2B37379002064", 3),
    }
    for channel, (url, minimum) in confirmed_links.items():
        if html.count(url) < minimum:
            failures.append(f"{channel} confirmed link is missing from required contact surfaces")

    system_layer = re.search(r"/\* Optima Fide design system \*/(.*?)/\* End Optima Fide design system \*/", html, re.DOTALL)
    if not system_layer:
        failures.append("Missing unified Optima Fide design-system CSS layer")
    else:
        layer = system_layer.group(1)
        for declaration in (
            "border-radius: 24px",
            "box-shadow: var(--of-shadow-card)",
            "padding-block: clamp(88px, 9vw, 128px)",
            "transition-duration: .001ms",
        ):
            if declaration not in layer:
                failures.append(f"Design-system CSS missing: {declaration}")

    v3_layer = re.search(r"/\* Premium visual redesign V3 \*/(.*?)/\* End premium visual redesign V3 \*/", html, re.DOTALL)
    if not v3_layer:
        failures.append("Missing premium visual redesign V3 CSS layer")
    else:
        v3_css = v3_layer.group(1)
        for declaration in (
            "width: min(1220px, 100%)",
            "border-radius: 36px",
            "linear-gradient(180deg, #dfbf72 0%, #c99a3d 58%, #b8872f 100%)",
            "margin: -56px auto 0",
            "linear-gradient(180deg, #06261f 0%, #041a16 100%)",
        ):
            if declaration not in v3_css:
                failures.append(f"Premium visual redesign V3 CSS missing: {declaration}")

    v4_layer = re.search(r"/\* Approved homepage V4 \*/(.*?)/\* End approved homepage V4 \*/", html, re.DOTALL)
    if not v4_layer:
        failures.append("Missing approved homepage V4 layout layer")
    else:
        v4_css = v4_layer.group(1)
        for declaration in ("main > .hero { order: 1", "#admission { order: 3", "#donatii { order: 9", "#faq { order: 10"):
            if declaration not in v4_css:
                failures.append(f"Approved homepage V4 CSS missing: {declaration}")

    if not GOOGLE_VERIFICATION_PATH.exists():
        failures.append("Missing Google verification file")
    elif GOOGLE_VERIFICATION_PATH.read_text(encoding="utf-8").strip() != GOOGLE_VERIFICATION_CONTENT:
        failures.append("Invalid Google verification file content")

    if not ROBOTS_PATH.exists() or "Sitemap: https://optimafide.pages.dev/sitemap.xml" not in ROBOTS_PATH.read_text(encoding="utf-8"):
        failures.append("Missing or invalid robots.txt")
    if not SITEMAP_PATH.exists() or "<loc>https://optimafide.pages.dev/</loc>" not in SITEMAP_PATH.read_text(encoding="utf-8"):
        failures.append("Missing or invalid sitemap.xml")

    worker = TELEGRAM_WORKER_PATH.read_text(encoding="utf-8")
    if 'request.method === "GET"' not in worker or 'service: "optima-fide-telegram-requests"' not in worker:
        failures.append("Telegram Worker must expose a GET health check")
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
        extensions = list(re.finditer(
            rf"Object\.assign\(translations\.{lang},\s*\{{(.*?)\n\s*\}}\);",
            html,
            re.DOTALL,
        ))
        for extension in extensions:
            available.update(re.findall(r"\b([A-Za-z][A-Za-z0-9]+)\s*:", extension.group(1)))
        missing = sorted(used_keys - available)
        if missing:
            failures.append(f"{lang} missing keys: {', '.join(missing)}")
        translation_source = match + "\n".join(extension.group(1) for extension in extensions)
        for key, expected in EXPECTED_RESOURCE_CTA[lang].items():
            if not re.search(rf'["\']?{key}["\']?\s*:\s*"{re.escape(expected)}"', translation_source):
                failures.append(f'{lang} {key} must be "{expected}"')
        for key, expected in EXPECTED_TRANSLATIONS[lang].items():
            if not re.search(rf'["\']?{key}["\']?\s*:\s*"{re.escape(expected)}"', translation_source):
                failures.append(f'{lang} {key} must be "{expected}"')

    offer_button_rule = re.search(r"\.offer-card\s+\.btn\s*\{([^}]*)\}", html, re.DOTALL)
    if not offer_button_rule:
        failures.append("Missing compact offer-card button rule")
    else:
        declarations = offer_button_rule.group(1)
        for required_declaration in ("max-width: 100%", "white-space: normal"):
            if required_declaration not in declarations:
                failures.append(f"Offer-card buttons missing: {required_declaration}")

    hero_layout_rule = re.search(r"\.hero-layout\s*\{([^}]*)\}", html, re.DOTALL)
    if not hero_layout_rule:
        failures.append("Missing hero layout rule")
    else:
        declarations = hero_layout_rule.group(1)
        for required_declaration in ("display: flex", "padding: clamp(30px, 5vw, 72px)"):
            if required_declaration not in declarations:
                failures.append(f"Hero layout missing safe badge spacing: {required_declaration}")

    hero_badge_rule = re.search(r"\.hero-badge\s*\{([^}]*)\}", html, re.DOTALL)
    if not hero_badge_rule:
        failures.append("Missing hero badge rule")
    else:
        declarations = hero_badge_rule.group(1)
        for required_declaration in ("max-width: 100%", "white-space: normal"):
            if required_declaration not in declarations:
                failures.append(f"Hero badges missing: {required_declaration}")

    team_photo_rule = re.search(r"\.team-photo,\s*\.team-placeholder\s*\{([^}]*)\}", html, re.DOTALL)
    if not team_photo_rule or "display: block" not in team_photo_rule.group(1):
        failures.append("Team photo containers must be block-level")
    if not team_photo_rule or "overflow: hidden" not in team_photo_rule.group(1):
        failures.append("Team photo containers must crop portrait images")

    team_grid_rule = re.search(r"\.team-grid\s*\{([^}]*)\}", html, re.DOTALL)
    if not team_grid_rule or "grid-auto-rows: 1fr" not in team_grid_rule.group(1):
        failures.append("Team grid rows must have equal height")

    for name, (phone_href, phone_text, email) in EXPECTED_TEAM_CONTACTS.items():
        card = re.search(
            rf'<article class="team-card".*?alt="{re.escape(name)}".*?</article>',
            html,
            re.DOTALL,
        )
        if not card:
            failures.append(f"Missing team card: {name}")
            continue
        for expected in (f'href="tel:{phone_href}"', phone_text, f'href="mailto:{email}"'):
            if expected not in card.group(0):
                failures.append(f"{name} missing contact: {expected}")

    expected_section_images = {
        "group-support": "assets/images/visual/group-support-owner.jpg",
        "familie": "assets/images/visual/family-help-owner.jpg",
    }
    for section_id, image_path in expected_section_images.items():
        section = re.search(
            rf'<section[^>]+id="{section_id}".*?</section>',
            html,
            re.DOTALL,
        )
        if not section or image_path not in section.group(0):
            failures.append(f"Section {section_id} must use {image_path}")

    img_sources = re.findall(r'<img[^>]+src="([^"]+)"', html)
    if img_sources.count("assets/images/visual/personal-consultation.webp") != 1:
        failures.append("Personal consultation photo must not be repeated")

    if html.count("fetch(TELEGRAM_WORKER_URL") < 2:
        failures.append("Both site request forms must submit to the Telegram Worker")

    day_line = re.search(r'<div class="day-line">(.*?)</div>', html, re.DOTALL)
    expected_day_line = ["dayMorning", "dayDay", "dayAfternoon", "dayEvening"]
    actual_day_line = re.findall(r'data-i18n="(day[A-Za-z]+)"', day_line.group(1) if day_line else "")
    if actual_day_line != expected_day_line:
        failures.append("Day line must show morning, day, afternoon and evening in order")

    for card in re.findall(r'<article class="team-card".*?</article>', html, re.DOTALL):
        if 'loading="lazy"' not in card:
            failures.append("Team photos below the fold must use lazy loading")
            break
    certificate = re.search(r'<button class="certificate-button".*?</button>', html, re.DOTALL)
    if not certificate or 'loading="lazy"' not in certificate.group(0):
        failures.append("Accreditation image below the fold must use lazy loading")
    for tile in re.findall(r'<button class="gallery-tile".*?</button>', html, re.DOTALL):
        if 'loading="lazy"' not in tile:
            failures.append("Gallery photos below the fold must use lazy loading")
            break

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
