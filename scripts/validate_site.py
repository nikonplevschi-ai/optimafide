from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
PRICE_LIST_PATH = "assets/docs/optima-fide-price-list-2026.docx"

QIWI_EXPLANATIONS = (
    "Pentru terminalul QIWI, continuați către fondurile de ajutor. Donația pentru Optima Fide este sprijin voluntar pentru centru.",
    "В терминале QIWI перейдите к фондам помощи. Пожертвование для Optima Fide является добровольной поддержкой центра.",
    "In the QIWI terminal, continue to Aid funds. A donation to Optima Fide is voluntary support for the center.",
)


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
            "https://wa.me/37378377337",
            "viber://chat?number=%2B37378377337",
            "https://www.facebook.com/profile.php?id=100064660152285",
            "https://www.paypal.com/ncp/payment/LP4324XXE6824",
            'class="section impact-section"',
            'data-i18n="impactTitle"',
            'data-i18n="impact1Number"',
            'data-i18n="impact2Number"',
            'data-i18n="impactNote"',
            "600+",
            "19 000+",
        ):
            if required not in html:
                errors.append(f"missing required site marker: {required}")

        for removed_marker in (
            "PDF materials",
            "Download the right material",
            "Family PDF",
            "Partner PDF",
            "Download PDF",
            "offersEyebrow",
            "offersTitle",
            "offersLead",
            "offerFamilyTitle",
            "offerPartnerTitle",
            "offerConsultTitle",
            "familyPdfCta",
            "partnerPdfCta",
            "assets/pdfs/optima-fide-family-offer-ru.pdf",
            "assets/pdfs/optima-fide-partner-offer-en.pdf",
        ):
            if removed_marker in html:
                errors.append(f"old PDF materials block marker remains: {removed_marker}")

        if PRICE_LIST_PATH in html or (ROOT / PRICE_LIST_PATH).exists():
            errors.append("service price list must not be published")

        for explanation in QIWI_EXPLANATIONS:
            if explanation not in html:
                errors.append("missing QIWI voluntary-support explanation")

        searchable = html.replace(
            "https://www.paypal.com/ncp/payment/LP4324XXE6824", ""
        )
        for explanation in QIWI_EXPLANATIONS:
            searchable = searchable.replace(explanation, "")
        forbidden_patterns = (
            r"\bprice(?:s|list|d)?\b",
            r"\bpricing\b",
            r"\bcost(?:s)?\b",
            r"\bfees?\b",
            r"\bpaid\b",
            r"\bpayment\b",
            r"\bpay\b",
            r"\bpreț(?:uri)?\b",
            r"\bpret(?:uri)?\b",
            r"\btarif(?:e)?\b",
            r"\bachit\w*\b",
            r"\bplăt\w*\b",
            r"\bplata\b",
            r"\bпрайс(?:-лист)?\b",
            r"\bстоимост\w*\b",
            r"\bцен[аы]\b",
            r"\bоплат\w*\b",
            r"\bплатн\w*\b",
        )
        for pattern in forbidden_patterns:
            if re.search(pattern, searchable, flags=re.IGNORECASE):
                errors.append(f"forbidden service-pricing wording remains: {pattern}")

    for required_file in ("robots.txt", "sitemap.xml"):
        if not (ROOT / required_file).exists():
            errors.append(f"{required_file} is missing")

    sitemap = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if re.search(r"price|pricing|pricelist|price-list|tarif|pret|прайс", sitemap, re.I):
        errors.append("sitemap contains a service-pricing URL")

    if errors:
        print("Site validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Site validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
