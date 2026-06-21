from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")

required_markup = (
    "assets/images/accreditation-certificate-from-pdf.webp",
    "assets/images/accreditation-certificate-from-pdf.jpg",
    "object-position: 44% center",
    'class="app-icon" src="assets/icons/phone.svg"',
    'class="app-icon" src="assets/icons/telegram.svg"',
    'class="app-icon" src="assets/icons/whatsapp.svg"',
    ".nav-actions > .btn.gold { white-space: nowrap; min-width: 132px;",
)

for marker in required_markup:
    assert marker in HTML, f"missing markup: {marker}"

required_files = (
    "assets/images/accreditation-certificate-from-pdf.webp",
    "assets/images/accreditation-certificate-from-pdf.jpg",
    "assets/images/accreditation-certificate-from-pdf.sha256",
    "assets/icons/phone.svg",
    "assets/icons/telegram.svg",
    "assets/icons/whatsapp.svg",
)

for relative_path in required_files:
    path = ROOT / relative_path
    assert path.exists() and path.stat().st_size > 0, f"missing asset: {relative_path}"

print("PDF certificate, hero position and app icons: OK")
