from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"


def local_refs(html: str) -> set[str]:
    attr_refs = re.findall(
        r'(?:src|srcset|href|data-lightbox)="([^"]+\.(?:jpg|jpeg|png|webp|avif|pdf|docx|doc|ico|xml|txt))"',
        html,
        flags=re.IGNORECASE,
    )
    css_refs = re.findall(r"url\([\"']?([^\"')]+)[\"']?\)", html)
    refs = set()
    for ref in [*attr_refs, *css_refs]:
        if ref.startswith(("http://", "https://", "mailto:", "tel:", "viber:")):
            continue
        refs.add(ref.split("#", 1)[0])
    return refs


def main() -> int:
    errors: list[str] = []
    if not INDEX.exists():
        errors.append("index.html is missing")
    else:
        html = INDEX.read_text(encoding="utf-8")
        for ref in sorted(local_refs(html)):
            if not (ROOT / ref).exists():
                errors.append(f"missing referenced file: {ref}")

        for lang in ('"ro":', '"ru":', '"en":'):
            if lang not in html:
                errors.append(f"missing translation block: {lang}")

        for required in (
            "https://t.me/optimafide_bot",
            "https://wa.me/37379002064",
            "viber://chat?number=%2B37379002064",
            "https://www.facebook.com/profile.php?id=100064660152285",
            "https://www.paypal.com/ncp/payment/LP4324XXE6824",
            "assets/pdfs/optima-fide-family-offer-ru.pdf",
            "assets/pdfs/optima-fide-partner-offer-en.pdf",
            "assets/docs/optima-fide-price-list-2026.docx",
        ):
            if required not in html:
                errors.append(f"missing required link: {required}")

    for required_file in ("robots.txt", "sitemap.xml"):
        if not (ROOT / required_file).exists():
            errors.append(f"{required_file} is missing")

    if errors:
        print("Site validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Site validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
