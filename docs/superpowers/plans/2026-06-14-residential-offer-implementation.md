# Residential Offer Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the Optima Fide landing page into a warm, clear residential rehabilitation offer with a building-led hero, practical trust content, recovery outings, center activities, optional services, accurate accreditation, and full RO/RU/EN localization.

**Architecture:** Preserve the existing static single-page architecture and its `translations` object, language switcher, reveal behavior, lightbox, forms, and navigation. Add focused CSS component families and semantic HTML sections inside `index.html`, prepare owner-provided image assets under `assets/images`, and add a standalone Python validation script for repeatable structural checks.

**Tech Stack:** Static HTML/CSS/JavaScript, Python 3 with `pypdf` and Pillow for asset preparation/validation, local HTTP server, browser/Playwright verification, GitHub Pages.

---

## File Structure

- Modify: `index.html` - metadata, responsive visual system, all new sections, localized content, and interactions.
- Create: `assets/images/hero-center.webp` - owner-provided center building image used by hero, gallery, and Open Graph.
- Replace: `assets/images/accreditation-certificate-clean.webp` - exact certificate extracted from the provided PDF.
- Replace: `assets/images/accreditation-certificate-clean.jpg` - JPG fallback for the exact certificate.
- Create: `scripts/validate_site.py` - repeatable validation of translations, local image references, required content, and prohibited legacy strings.
- Modify: `README.md` - local preview and validation commands.

### Task 1: Add Repeatable Site Validation

**Files:**
- Create: `scripts/validate_site.py`
- Modify: `README.md`

- [ ] **Step 1: Write the failing validation script**

Create a script that parses `index.html`, collects `data-i18n` keys, extracts the three translation dictionaries, checks every used key in RO/RU/EN, verifies every local `src`, `srcset`, `data-lightbox`, and `og:image` target exists, and rejects:

```python
PROHIBITED = [
    "+373 78 377 337",
    "+373 783 77337",
    "Din 2014",
    "Golanul Nou",
    "Clienți reabilitați",
    "Clienti reabilitati",
]
```

The script must print each failure and exit `1`, or print `Site validation passed` and exit `0`.

- [ ] **Step 2: Run validation and confirm it fails before assets/content exist**

Run:

```powershell
python scripts/validate_site.py
```

Expected: non-zero exit caused by missing required hero/section keys or assets.

- [ ] **Step 3: Document local commands**

Add to `README.md`:

```markdown
## Local verification

```powershell
python -m http.server 8080
python scripts/validate_site.py
```
```

- [ ] **Step 4: Commit validation scaffold**

```powershell
git add scripts/validate_site.py README.md
git commit -m "Add repeatable landing page validation"
```

### Task 2: Prepare Hero and Exact Certificate Assets

**Files:**
- Create: `assets/images/hero-center.webp`
- Replace: `assets/images/accreditation-certificate-clean.webp`
- Replace: `assets/images/accreditation-certificate-clean.jpg`

- [ ] **Step 1: Copy the owner-provided hero image**

Copy `D:\рабочая\1.webp` to `assets/images/hero-center.webp` without destructive editing. Confirm it opens and its dimensions are non-zero.

- [ ] **Step 2: Extract the full-page certificate image**

Use `pypdf` to extract the single image from:

`C:\Users\igor\Desktop\Отправка по электронной почте IMG_0001_702ee374-40e9-449d-a99c-4ea800e95c99.pdf`

Save optimized JPG and WebP versions while preserving the A4 portrait ratio and without cropping.

- [ ] **Step 3: Validate prepared assets**

Run a Pillow check that prints dimensions and asserts:

```python
assert hero.width > 0 and hero.height > 0
assert abs((certificate.width / certificate.height) - (595.2 / 841.92)) < 0.02
```

Expected: both assertions pass.

- [ ] **Step 4: Commit hero/certificate assets**

```powershell
git add assets/images/hero-center.webp assets/images/accreditation-certificate-clean.webp assets/images/accreditation-certificate-clean.jpg
git commit -m "Set center building as main hero image"
```

### Task 3: Rebuild Hero and First-Step Offer

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add metadata and hero structure**

Set:

```html
<meta property="og:image" content="assets/images/hero-center.webp">
```

Rebuild the hero with a desktop full-bleed image background, readable left copy, three actions, five trust badges, and localized caption. On mobile, render a substantial image panel above a light-background copy panel.

- [ ] **Step 2: Add localized hero and first-step copy**

Add complete RO/RU/EN keys for:

- warm hero title and lead;
- request consultation, view stay conditions, and call now;
- five trust badges;
- hero image caption;
- first-step title, reassurance text, call, Telegram, and consultation actions.
- confidentiality and no-pressure reassurance;
- five quick-situation cards, each linking to the consultation form.

- [ ] **Step 3: Implement responsive hero CSS**

Ensure desktop preserves almost the whole building using a non-aggressive background position and green/milky overlays. Ensure mobile does not use the desktop background crop and has no text over the image.

- [ ] **Step 4: Verify hero and first-step behavior**

Run:

```powershell
python scripts/validate_site.py
```

Expected: no missing hero/first-step translation keys and `hero-center.webp` resolves.

- [ ] **Step 5: Commit hero implementation**

```powershell
git add index.html
git commit -m "Build welcoming residential center hero"
```

### Task 4: Build the Core Trust Offer

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Refine included-program cards**

Replace the current eight included-program cards with concise RO/RU/EN offer content for accommodation, meals, daily rhythm, groups, family, spirituality without pressure, activities, and reintegration.

- [ ] **Step 2: Add who-the-program-is-for cards**

Add six localized cards covering inability to stop alone, family seeking help, restart after relapse, unsafe home triggers/conflict, need for stable environment, and rebuilding responsibility/work/relationships.

- [ ] **Step 3: Add the verified trust section**

Present accreditation, residential format, 20 places, `500+` people helped, `19 000+` consultations, Goianul Nou, family support, spiritual support without pressure, and recovery experience without introducing new numerical claims.

- [ ] **Step 4: Rewrite family support section**

Turn the existing family section into a direct, warm message for relatives with one localized contact action.

- [ ] **Step 5: Run structural validation and commit**

```powershell
python scripts/validate_site.py
git add index.html
git commit -m "Strengthen residential program trust offer"
```

Expected: validation passes for all newly used translation keys.

### Task 5: Add Daily Rhythm and Admission Guidance

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Replace generic recovery timeline**

Replace the existing six-step timeline with a localized five-part example day: morning, daytime meetings/work, afternoon activity/learning, evening reflection/quiet, and night rest. Clearly label it as an example rhythm.

- [ ] **Step 2: Add admission steps**

Add the seven localized admission steps from first call/message through first-days adaptation.

- [ ] **Step 3: Add what-to-bring list**

Add identity document, comfortable daily clothes, hygiene items, seasonal
shoes, necessary personal belongings without excess, and medicines only by
prior agreement. Note that the full list can be clarified during consultation.

- [ ] **Step 4: Add first-three-days and calm rules blocks**

Explain arrival/orientation, restoring a stable basic rhythm, and creating an
initial accompaniment plan. Add respectful rules for daily rhythm, no alcohol
or narcotic substances, shared responsibilities, and care for people/place.

- [ ] **Step 5: Validate and commit**

```powershell
python scripts/validate_site.py
git add index.html
git commit -m "Add daily rhythm and admission guidance"
```

Expected: all new keys exist in RO/RU/EN.

### Task 6: Add Center Activities

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add a compact activities subsection after the center gallery**

Create five localized cards for billiards, table tennis, football field, barbecue/outdoor meals, and courtyard/outdoor rest. Use simple visual icons or numbered marks consistent with the current site.

- [ ] **Step 2: Frame every activity around recovery**

Keep descriptions focused on movement, communication, attention, discipline, teamwork, and healthy rest. Do not use resort or entertainment language.

- [ ] **Step 3: Validate and commit**

```powershell
python scripts/validate_site.py
git add index.html
git commit -m "Add healthy center activities"
```

### Task 7: Rebuild Recovery Outings

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Replace the current tourism section**

Create a large photographic feature using a suitable existing tourism WebP, followed by six cards: monasteries, landscapes/nature, Dniester, fishing/outdoor rest, cultural/spiritual places, and individual outings.

- [ ] **Step 2: Add fee and conditions language**

Add a prominent localized additional-fee label and note stating that outings depend on participant condition, program rules, weather, prior agreement, and separate cost.

- [ ] **Step 3: Localize image alt text**

Ensure all tourism images have localized `alt` values updated by the existing language switcher, using a small `data-i18n-alt` extension if needed.

- [ ] **Step 4: Validate and commit**

```powershell
python scripts/validate_site.py
git add index.html
git commit -m "Add recovery outings across Moldova"
```

### Task 8: Add Honest Included/Paid Comparison and Optional Services

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add included-versus-separate comparison**

Create a clear two-column comparison for base-program inclusions and separately paid options, without prices or commercial checkout styling.

- [ ] **Step 2: Add six optional-service cards**

Add massage, hairdresser, surgical doctor consultation, addiction medicine consultants, tests/examinations, and individual transport/accompaniment/appointments. Put a localized additional-fee badge on each.

- [ ] **Step 3: Add legal disclaimers**

State in the section and near the page footer that medical consultations, tests, and examinations are arranged through specialized professionals and institutions; the program does not replace emergency medical care.

Also state that the center does not replace inpatient psychiatry or emergency
detoxification.

- [ ] **Step 4: Validate and commit**

```powershell
python scripts/validate_site.py
git add index.html
git commit -m "Add recovery tourism and optional activity services"
```

### Task 9: Add FAQ and Final Content Polish

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add accessible FAQ accordion**

Use native `<details>` elements for ten localized questions: first conversation, duration, accommodation/meals, family contact, travel from elsewhere, what to bring, separately paid services, medical consultations, visits, and how to begin/confidentiality/location.

- [ ] **Step 2: Ensure accurate certificate display**

Confirm the accreditation section and lightbox use the replaced exact certificate assets with `object-fit: contain` and no crop.

- [ ] **Step 3: Review page length and remove duplicate copy**

Shorten or remove content that repeats the same offer, especially duplicated package/timeline text, while preserving all agreed information and existing contact/donation behavior.

- [ ] **Step 4: Strengthen partner/donor message**

Add a concise localized partnership message to the existing donation section
for church communities, social services, foundations, specialists, and donors.
Do not add testimonials or PDF download buttons without approved source files.

- [ ] **Step 5: Run validation and commit**

```powershell
python scripts/validate_site.py
git diff --check
git add index.html
git commit -m "Add FAQ and polish residential offer"
```

Expected: validation and diff check pass.

### Task 10: Browser Verification and Production Publication

**Files:**
- Modify if required by findings: `index.html`
- Modify if required by findings: `scripts/validate_site.py`

- [ ] **Step 1: Start local server**

Run:

```powershell
python -m http.server 8080
```

Expected: site available at `http://localhost:8080`.

- [ ] **Step 2: Verify responsive layouts**

Use browser automation at `1440px`, `768px`, and `375px`. Confirm no horizontal scroll, hero building remains visible, text does not overlap, grids collapse correctly, and certificate/tourism images are not distorted.

- [ ] **Step 3: Verify interactions and languages**

Switch RO/RU/EN and confirm all new content and alt text update. Test navigation, call/Telegram links, lightbox, FAQ, sticky CTA, form, map, and IBAN copy. Confirm console has no errors and network has no failed local assets.

- [ ] **Step 4: Run final local checks**

```powershell
python scripts/validate_site.py
git diff --check
git status --short
```

Expected: validation passes, no whitespace errors, and only intended changes remain.

- [ ] **Step 5: Push and verify GitHub Pages**

```powershell
git push origin main
```

Open `https://nikonplevschi-ai.github.io/optimafide/`, verify the deployed HTML contains `assets/images/hero-center.webp`, and repeat key desktop/mobile/language/console checks.
