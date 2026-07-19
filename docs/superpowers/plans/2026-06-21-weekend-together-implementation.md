# Weekend Together Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a localized, responsive Weekend Together offer with weekend-only pricing, direct contact actions, form integration, FAQ coverage, and the approved hero and certificate alignment polish.

**Architecture:** Keep the static single-page architecture. Add one semantic section and its component-scoped CSS to `index.html`, extend the three existing translation dictionaries, and add a focused Python validator that reads the real HTML and asserts the public contract.

**Tech Stack:** HTML, CSS, vanilla JavaScript i18n dictionaries, Python standard library, Chrome responsive checks, Cloudflare Pages.

---

### Task 1: Define The Weekend Offer Contract

**Files:**
- Create: `scripts/validate_weekend_together.py`
- Test: `scripts/validate_weekend_together.py`

- [ ] **Step 1: Write the failing validator**

```python
from pathlib import Path

html = (Path(__file__).resolve().parents[1] / "index.html").read_text(encoding="utf-8")

required = {
    'id="weekend-together"': "section",
    'data-i18n="weekendTitle"': "localized title",
    'data-i18n="supportWeekend"': "form option",
    'href="https://t.me/optimafide_bot"': "Telegram CTA",
    "4 900 MDL": "pair price",
    "3 500 MDL": "single price",
    "+1 400 MDL": "extra companion price",
    "1 000 MDL": "reservation price",
    'data-i18n="faqWeekend1Q"': "weekend FAQ 1",
    'data-i18n="faqWeekend2Q"': "weekend FAQ 2",
    'data-i18n="faqWeekend3Q"': "weekend FAQ 3",
    ".hero::before": "full-width hero mist",
    "object-position: 56% center": "building shift",
    "aspect-ratio: 595 / 842": "upright certificate frame",
}

missing = [label for marker, label in required.items() if marker not in html]
assert not missing, "Missing Weekend Together contract: " + ", ".join(missing)

for dictionary_marker in ('const ro = {', 'const ru = {', 'const en = {'):
    start = html.index(dictionary_marker)
    end = html.index('\n    };', start)
    block = html[start:end]
    for key in ("weekendTitle", "weekendSubtitle", "supportWeekend", "faqWeekend1Q", "faqWeekend3A"):
        assert key in block, f"{key} missing from {dictionary_marker}"

for forbidden in ("1 week", "2 weeks", "1 month", "3 months", "6 months"):
    assert forbidden not in html[html.index('id="weekend-together"'):html.index('id="weekend-together"') + 15000]

print("Weekend Together contract: OK")
```

- [ ] **Step 2: Run the validator and confirm RED**

Run: `python scripts/validate_weekend_together.py`
Expected: FAIL with `Missing Weekend Together contract` because the section does not exist.

- [ ] **Step 3: Commit the failing contract test**

```powershell
git add -- scripts/validate_weekend_together.py
git commit -m "Test Weekend Together service contract"
```

### Task 2: Build The Localized Premium Section

**Files:**
- Modify: `index.html`
- Test: `scripts/validate_weekend_together.py`

- [ ] **Step 1: Add component-scoped styling**

Add `.weekend-offer`, `.weekend-layout`, `.weekend-media`, `.weekend-copy`, `.weekend-includes`, `.weekend-pricing`, `.weekend-price-featured`, `.weekend-price-row`, `.weekend-notice`, and `.weekend-actions` rules using existing ivory, sage, gold, typography, shadow, and radius variables. Add mobile rules that collapse the grid to one column and keep buttons and long translated strings inside the viewport.

- [ ] **Step 2: Add the section between consultation and admission**

```html
<section class="section weekend-offer" id="weekend-together" aria-labelledby="weekend-title">
  <div class="container weekend-shell" data-reveal>
    <figure class="weekend-media"><img src="assets/images/visual/family-support.webp" alt="" loading="lazy" decoding="async"></figure>
    <div class="weekend-copy">
      <div class="eyebrow" data-i18n="weekendEyebrow"></div>
      <h2 id="weekend-title" data-i18n="weekendTitle"></h2>
      <p class="weekend-subtitle" data-i18n="weekendSubtitle"></p>
      <p data-i18n="weekendText"></p>
      <h3 data-i18n="weekendIncludesTitle"></h3>
      <ul class="weekend-includes">
        <li data-i18n="weekendInclude1"></li><li data-i18n="weekendInclude2"></li>
        <li data-i18n="weekendInclude3"></li><li data-i18n="weekendInclude4"></li>
        <li data-i18n="weekendInclude5"></li><li data-i18n="weekendInclude6"></li>
        <li data-i18n="weekendInclude7"></li>
      </ul>
      <div class="weekend-pricing">
        <div class="weekend-price-featured"><span data-i18n="weekendPair"></span><strong>4 900 MDL</strong></div>
        <div class="weekend-price-row"><span data-i18n="weekendSingle"></span><strong>3 500 MDL</strong></div>
        <div class="weekend-price-row"><span data-i18n="weekendExtra"></span><strong>+1 400 MDL</strong></div>
        <div class="weekend-price-row"><span data-i18n="weekendReservation"></span><strong>1 000 MDL</strong></div>
      </div>
      <p class="weekend-continuation" data-i18n="weekendContinuation"></p>
      <p class="weekend-notice" data-i18n="weekendSafety"></p>
      <div class="weekend-actions">
        <a class="btn primary" href="https://t.me/optimafide_bot" target="_blank" rel="noopener noreferrer" data-i18n="weekendBook"></a>
        <a class="btn outline" href="https://wa.me/37378377337" target="_blank" rel="noopener noreferrer" data-i18n="weekendWhatsapp"></a>
        <a class="btn outline" href="tel:+37378377337" data-i18n="weekendCall"></a>
      </div>
    </div>
  </div>
</section>
```

- [ ] **Step 3: Integrate form, FAQ, and RO/RU/EN dictionaries**

Add `<option data-i18n="supportWeekend">Weekend împreună</option>` to `#support`. Add three `<details>` entries keyed `faqWeekend1Q/A` through `faqWeekend3Q/A`. Add complete, natural Romanian, Russian, and English values for every `weekend*`, `supportWeekend`, and FAQ key, preserving the supplied meaning and safety language.

- [ ] **Step 4: Run the focused validator and confirm GREEN**

Run: `python scripts/validate_weekend_together.py`
Expected: `Weekend Together contract: OK`

- [ ] **Step 5: Commit the feature**

```powershell
git add -- index.html scripts/validate_weekend_together.py
git commit -m "Add Weekend Together service"
```

### Task 3: Polish Hero And Certificate Presentation

**Files:**
- Modify: `index.html`
- Test: `scripts/validate_weekend_together.py`

- [ ] **Step 1: Extend the hero mist to viewport edges**

Add a non-interactive `.hero::before` layer spanning the hero section with soft ivory/sage radial and linear gradients. Keep `.hero-frame` above it and avoid changing the approved content, dimensions, or actions.

- [ ] **Step 2: Shift the building slightly left**

Set the desktop hero image to `object-position: 56% center`, preserving the existing mobile composition and cover behavior.

- [ ] **Step 3: Present the full certificate upright**

Give `.certificate-button picture` an upright `aspect-ratio: 595 / 842`, center it, and render `.certificate-button img` at `width: 100%`, `height: 100%`, `object-fit: contain`, and `transform: none`. Preserve both the current JPEG/WebP sources and lightbox target.

- [ ] **Step 4: Run the focused validator**

Run: `python scripts/validate_weekend_together.py`
Expected: `Weekend Together contract: OK`

### Task 4: Responsive And Functional Verification

**Files:**
- Modify if needed: `index.html`
- Create: `C:/Users/igor/Desktop/OptimaFide_site_work/notes/weekend-together-report.md`

- [ ] **Step 1: Run repository validators**

Run: `python scripts/validate_weekend_together.py`, `python scripts/validate_site.py`, and `git diff --check HEAD^`.
Expected: all commands exit 0 with no whitespace errors.

- [ ] **Step 2: Verify the page in RO, RU, and EN**

Use browser automation against the local server to set `localStorage.optimaLang` to each language. Confirm the section title, subtitle, price labels, safety note, form option, and FAQ entries change language and remain non-empty.

- [ ] **Step 3: Verify responsive behavior**

At widths `360`, `375`, `390`, `414`, `430`, `768`, `1024`, `1280`, and `1440`, assert `document.documentElement.scrollWidth <= document.documentElement.clientWidth`, all images have `naturalWidth > 0`, and no console errors occur.

- [ ] **Step 4: Verify protected integrations**

Check Telegram Worker, Telegram bot, WhatsApp, Facebook, Viber, PayPal, PDF, Word, `sitemap.xml`, and `robots.txt` using the existing URLs and validation script. Record results without editing unrelated integrations.

- [ ] **Step 5: Write the report**

Record the implemented placement, four permitted weekend prices, absence of longer-stay prices, translations, responsive results, link checks, validator output, screenshots, commit, and deployment URLs in `C:/Users/igor/Desktop/OptimaFide_site_work/notes/weekend-together-report.md`.

### Task 5: Screenshots And Deployment

**Files:**
- Create: `C:/Users/igor/Desktop/OptimaFide_site_work/exports/weekend-together-desktop.png`
- Create: `C:/Users/igor/Desktop/OptimaFide_site_work/exports/weekend-together-mobile.png`
- Create: `C:/Users/igor/Desktop/OptimaFide_site_work/exports/weekend-together-price-card.png`

- [ ] **Step 1: Capture requested screenshots**

Capture the full new section at desktop and 390px mobile sizes, plus a focused desktop crop of the price panel. Confirm each PNG exists and is non-empty.

- [ ] **Step 2: Push main**

Integrate the verified feature commit into `main` without staging or reverting unrelated user files, then run `git push origin main`.

- [ ] **Step 3: Deploy a clean commit archive to Cloudflare Pages**

Export the verified commit with `git archive`, deploy that clean directory using `npx wrangler pages deploy <archive-dir> --project-name optimafide --branch main --commit-hash <hash> --commit-message "Add Weekend Together service"`, and save the returned deployment URL.

- [ ] **Step 4: Verify production**

Open `https://optimafide.pages.dev/` with a cache-busting query, confirm `#weekend-together`, the four prices, translations, working image and CTA targets, and re-run the no-scroll/error checks against production.
