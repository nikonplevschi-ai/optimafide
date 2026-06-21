# Premium Calm Hero Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the existing dark photo-banner hero with the approved light, green-toned `hero--calm` composition while preserving all site functionality and SEO signals.

**Architecture:** Keep the established single-file site structure. Add semantic hero mode classes and a dedicated processed image asset, extend `scripts/validate_site.py` with structural/content regressions, and verify rendered geometry through Chromium at every required viewport and language. Store non-production work files under `C:\Users\igor\Desktop\OptimaFide_site_work\`.

**Tech Stack:** Static HTML/CSS/JavaScript, Python validation, Cloudflare Pages, Chromium DevTools Protocol, image generation/editing tool for the premium building variant.

---

### Task 1: Prepare Work Files And Regression Contract

**Files:**
- Modify: `scripts/validate_site.py`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\{mockups,hero-variants,processed-images,backups,exports,notes}`

- [ ] **Step 1: Create the desktop project structure and backups**

Create the six required directories. Copy `index.html`, the current building source image, the approved reference screenshot, and existing visual mockup into the matching backup/source folders without altering repository files.

- [ ] **Step 2: Add failing structural regressions**

Extend `scripts/validate_site.py` to require:

```python
EXPECTED_HERO_TRANSLATIONS = {
    "ro": {
        "heroTitle": "Un loc unde te poți opri și începe din nou",
        "heroLead": "Program rezidențial de recuperare: cazare, masă, ritm zilnic, comunitate terapeutică și sprijin pentru familie.",
        "heroTrustLine": "Acreditare · 20 locuri · 500+ persoane sprijinite · confidențial",
    },
    "ru": {
        "heroTitle": "Место, где можно остановиться и начать заново",
        "heroLead": "Резиденциальная программа восстановления: проживание, питание, ежедневный ритм, сообщество и поддержка семьи.",
        "heroTrustLine": "Аккредитация · 20 мест · 500+ человек получили помощь · конфиденциально",
    },
    "en": {
        "heroTitle": "A place to pause, recover and begin again",
        "heroLead": "A residential recovery program with accommodation, meals, daily rhythm, community support and family guidance.",
        "heroTrustLine": "Accredited · 20 residential places · 500+ people supported · confidential",
    },
}
```

Also require `class="hero hero--calm"`, `hero--family`, `hero--trust`, `class="hero-trust-line"`, `assets/images/hero/hero-center-premium.webp`, and reduced-motion rules.

- [ ] **Step 3: Run the validator and confirm the expected failure**

Run:

```powershell
$env:PYTHONUTF8='1'; python scripts\validate_site.py
```

Expected: failures for the missing hero mode, trust line, processed asset, exact translations, and alternative classes.

### Task 2: Produce The Premium Building Asset

**Files:**
- Source: `assets/images/center-building.webp`
- Create: `assets/images/hero/hero-center-premium.webp`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\processed-images\hero-center-premium-v1.webp`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\processed-images\hero-center-final.webp`

- [ ] **Step 1: Inspect the source image at original resolution**

Confirm dimensions, roof/facade visibility, and color cast. Record the source dimensions in `notes\hero-image-notes.txt`.

- [ ] **Step 2: Generate an architecture-preserving premium edit**

Use the image editing tool with the source image and this constraint:

```text
Preserve the exact building architecture, windows, balconies, roofline, proportions, camera position, and realistic surroundings. Improve exposure and white balance, reduce the cold blue cast, keep the facade clean white, soften contrast, and introduce restrained warm ivory and natural sage-green tones. Do not add or remove structures, trees, roads, windows, people, signage, or landscaping. Avoid HDR and artificial saturation. Produce a calm premium architectural photograph suitable for a wellness residence hero.
```

- [ ] **Step 3: Compare the edit against the source**

Reject any version that changes architecture. Select the most faithful version and export it as WebP for the site and desktop work folder.

- [ ] **Step 4: Confirm the asset exists and loads**

Run:

```powershell
Get-Item assets\images\hero\hero-center-premium.webp
```

Expected: one non-empty WebP file.

### Task 3: Implement Header And Hero Structure

**Files:**
- Modify: `index.html`

- [ ] **Step 1: Add the active hero mode and semantic layers**

Change the hero markup to the following ownership structure while preserving existing link destinations and modal hooks:

```html
<section class="hero hero--calm" aria-labelledby="hero-title">
  <div class="hero-frame">
    <div class="hero-media">
      <img src="assets/images/hero/hero-center-premium.webp" data-i18n-alt="heroImageAlt" alt="Centrul rezidențial Optima Fide">
    </div>
    <div class="hero-layout">
      <div class="hero-copy">
        <div class="hero-badges">
          <span class="hero-badge" data-i18n="badgeAccreditation"></span>
          <span class="hero-badge" data-i18n="badgeDuration"></span>
          <span class="hero-badge" data-i18n="badgeBoard"></span>
          <span class="hero-badge" data-i18n="badgeFamily"></span>
          <span class="hero-badge" data-i18n="badgePlace"></span>
        </div>
        <h1 class="hero-title" id="hero-title" data-i18n="heroTitle"></h1>
        <p class="hero-subtitle" data-i18n="heroLead"></p>
        <div class="hero-actions">
          <a class="btn hero-primary" href="#consultatie" data-i18n="heroConsult"></a>
          <a class="btn hero-secondary" href="#" data-contact-modal data-i18n="telegramCta"></a>
        </div>
      </div>
      <div class="hero-trust-line" data-i18n="heroTrustLine"></div>
    </div>
  </div>
</section>
```

Keep exactly two primary hero actions: consultation and Telegram. Phone remains available in the header and sticky mobile CTA.

- [ ] **Step 2: Add the approved tokens and typography**

Add `--font-heading`, `--font-body`, the approved `--of-*` colors/shadows, and use the existing Google Fonts request if it already includes the required weights. Set the title maximum to 5.8rem to keep Russian line breaks controlled.

- [ ] **Step 3: Implement the blended calm composition**

Use one rounded frame with a light gradient surface, absolute right-side image layer, left content layer, thin border, and soft shadow. Blend content into the photo using ivory/sage gradients; do not introduce a hard dividing edge.

- [ ] **Step 4: Add mist and entrance motion**

Implement 16–19 second low-opacity mist animations and short initial content reveal. Add:

```css
@media (prefers-reduced-motion: reduce) {
  .hero-frame::before,
  .hero-frame::after,
  .hero-frame,
  .hero-badge,
  .hero-title,
  .hero-subtitle,
  .hero-actions {
    animation: none !important;
  }
}
```

- [ ] **Step 5: Refine the header without changing behavior**

Keep the brand left, navigation centered, and phone plus gold consultation CTA right at desktop. Do not add hours. Preserve mobile menu and language switching.

### Task 4: Add Exact Copy And Alternative Modes

**Files:**
- Modify: `index.html`
- Modify: `scripts/validate_site.py`

- [ ] **Step 1: Replace hero translations**

Set the approved RO/RU/EN headline, subtitle, two CTA labels, five short badges, image alt, and trust line in the active translation extensions. Remove the obsolete long accreditation badge text from the rendered hero.

- [ ] **Step 2: Add inactive alternative CSS modes**

Add scoped rules only:

```css
.hero--family .hero-frame {
  background: linear-gradient(105deg, rgba(255,253,247,.98), rgba(247,242,232,.78)), var(--of-cream);
}
.hero--family .hero-frame::before { opacity: .82; }
.hero--trust .hero-frame {
  background: linear-gradient(105deg, rgba(255,253,247,.96), rgba(143,160,134,.36)), var(--of-cream);
}
.hero--trust .hero-badge { border-color: rgba(11,55,44,.2); }
```

Do not add a switcher and do not render multiple heroes.

- [ ] **Step 3: Implement mobile flow**

At 768px and below, set the media layer to normal document flow first, content second, trust line third. Use `object-fit: contain`, full-width CTA buttons, compact wrapped badges, and no trust-line bullets.

- [ ] **Step 4: Run the validator until green**

Run:

```powershell
$env:PYTHONUTF8='1'; python scripts\validate_site.py
git diff --check
```

Expected: `Site validation passed`, exit code 0, and no whitespace errors.

### Task 5: Rendered Visual And Functional Verification

**Files:**
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\mockups\hero-desktop-final.png`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\mockups\hero-mobile-final.png`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\exports\full-page-desktop.png`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\exports\full-page-mobile.png`

- [ ] **Step 1: Serve the local site and run the viewport-language matrix**

For widths 360, 375, 390, 414, 430, 768, 1024, and 1280 and languages RO/RU/EN, assert:

```javascript
document.documentElement.scrollWidth <= innerWidth
badges.every(rect => rect is inside heroFrame)
heroTitleRect does not overlap heroActionsRect
heroImage.complete && heroImage.naturalWidth > 0
getComputedStyle(heroImage).objectFit === "contain"
```

Expected: 24 checks, zero failures, zero console errors.

- [ ] **Step 2: Visually inspect desktop and mobile**

Confirm the building architecture is unchanged, roof and facade are visible, left gradients read as intentional atmosphere, gold is restrained, and mobile has no excessive gap between image and text.

- [ ] **Step 3: Capture required screenshots**

Save desktop/mobile hero and full-page screenshots to the desktop project folders. Create a before/after comparison in `mockups`.

- [ ] **Step 4: Verify unchanged functionality locally**

Check language switch, mobile menu, PDF, Word, PayPal URL, Telegram modal, Worker health, Google verification, sitemap, robots, and local image references.

### Task 6: Commit, Deploy, And Audit Production

**Files:**
- Modify outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\notes\implementation-report.md`

- [ ] **Step 1: Run fresh pre-commit verification**

Run:

```powershell
$env:PYTHONUTF8='1'; python scripts\validate_site.py
git diff --check
git status --short
```

Expected: validation pass and only intended repository changes.

- [ ] **Step 2: Commit and push**

Run:

```powershell
git add .
git commit -m "Refine premium green-toned hero to match approved concept"
git push origin main
```

- [ ] **Step 3: Deploy Cloudflare Pages**

Run:

```powershell
npx --yes wrangler@latest pages deploy . --project-name optimafide --branch main
```

Expected: deployment URL under `optimafide.pages.dev`.

- [ ] **Step 4: Verify production**

Confirm HTTP 200 and correct canonical on `https://optimafide.pages.dev/`; validate sitemap XML, robots, Google verification, PDF, Word, PayPal, Telegram bot, Worker health and one clearly labeled test form submission. Repeat the 24 rendered checks against production and confirm zero console errors/broken images.

- [ ] **Step 5: Write the desktop report**

Record the photo treatment, tokens, typography, responsive results, functional checks, deployment URL, and commit hash in `notes\implementation-report.md`.
