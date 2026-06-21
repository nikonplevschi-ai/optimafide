# Site System Polish Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply the approved warm sage palette and unify all cards, buttons, spacing, imagery, copy and motion without removing sections or changing program meaning.

**Architecture:** Keep production code in `index.html` and regression coverage in `scripts/validate_site.py`. Add a token-driven visual layer with component-specific selectors, then verify rendered layout through Chromium across RO/RU/EN and nine required widths. Preserve all external integrations and save audit artifacts under `C:\Users\igor\Desktop\OptimaFide_site_work\`.

**Tech Stack:** Static HTML/CSS/JavaScript, Python validation, Chromium DevTools Protocol, Cloudflare Pages.

---

### Task 1: Baseline And Palette Contract

**Files:**
- Modify: `scripts/validate_site.py`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\backups\index-before-card-polish.html`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\backups\validate-site-before-card-polish.py`

- [ ] **Step 1: Save baseline files and screenshots**

Copy the current production files into `backups` and capture before screenshots for 1440, 768 and 390px into `exports`.

- [ ] **Step 2: Add exact palette regressions**

Extend `REQUIRED` in `scripts/validate_site.py` with:

```python
PALETTE_REQUIRED = [
    "--of-bg: #f5efe4",
    "--of-surface: #fffaf1",
    "--of-surface-soft: #f8f2e7",
    "--of-green-deep: #06261f",
    "--of-green-main: #0b372c",
    "--of-green-soft: #dfe8dc",
    "--of-sage-light: #eef3ea",
    "--of-gold: #c99a3d",
    "--of-gold-hover: #b8872f",
    "--of-muted: #65736b",
    "--of-shadow: 0 18px 55px rgba(18, 44, 36, .11)",
]
```

Fail when any token is missing or when `body` does not use `var(--of-bg)`.

- [ ] **Step 3: Run and confirm RED**

Run:

```powershell
$env:PYTHONUTF8='1'; python scripts\validate_site.py
```

Expected: failures for the missing approved palette tokens and body assignment.

### Task 2: Apply Premium Sage Palette

**Files:**
- Modify: `index.html`
- Modify: `scripts/validate_site.py`

- [ ] **Step 1: Add the exact root tokens**

Add the approved palette verbatim and map legacy aliases to it:

```css
--bg: var(--of-bg);
--soft: var(--of-surface-soft);
--card: var(--of-surface);
--green: var(--of-green-main);
--gold: var(--of-gold);
--text: var(--of-text);
--muted: var(--of-muted);
--line: var(--of-border);
```

- [ ] **Step 2: Apply tokens to global surfaces and controls**

Set body, soft sections, cards, headings, body copy, badges, borders, shadows and primary CTA states to their approved token. Replace cold-gray UI surfaces while retaining realistic photo colors.

- [ ] **Step 3: Warm the hero mist**

Use the approved layered background:

```css
background:
  radial-gradient(circle at 12% 82%, rgba(143,160,134,.30), transparent 36%),
  radial-gradient(circle at 78% 18%, rgba(217,184,108,.18), transparent 32%),
  linear-gradient(90deg, rgba(255,250,241,.96), rgba(255,250,241,.48), rgba(223,232,220,.22));
```

- [ ] **Step 4: Run and confirm GREEN**

Run:

```powershell
$env:PYTHONUTF8='1'; python scripts\validate_site.py
git diff --check
```

Expected: validator passes and no whitespace errors.

- [ ] **Step 5: Commit palette separately**

```powershell
git add index.html scripts/validate_site.py
git commit -m "Refine site color palette with premium sage tones"
```

### Task 3: Card, Button And Motion Contract

**Files:**
- Modify: `scripts/validate_site.py`

- [ ] **Step 1: Add failing card-system regressions**

Require the following declarations in the new `.surface-card-system` selector group or equivalent component group:

```python
CARD_DECLARATIONS = [
    "border-radius: 24px",
    "border: 1px solid var(--of-border)",
    "background: var(--of-surface)",
    "box-shadow: var(--of-shadow-card)",
]
BUTTON_DECLARATIONS = [
    "max-width: 100%",
    "min-height: 44px",
    "white-space: normal",
]
```

Require `:focus-visible`, `@media (hover: hover) and (pointer: fine)` and reduced-motion `transition-duration: .001ms`.

- [ ] **Step 2: Run and confirm RED**

Expected: failures for missing shared card, button, focus, hover capability and reduced-motion contracts.

### Task 4: Implement System Polish

**Files:**
- Modify: `index.html`
- Modify: `scripts/validate_site.py`

- [ ] **Step 1: Normalize card surfaces by component family**

Group existing selectors without changing markup ownership:

```css
.included-card,
.situation-card,
.activity-card,
.service-card,
.trust-card,
.admission-card,
.offer-card,
.team-card,
.tourism-card,
.voice-card,
.family-card,
.soft-card,
.contact-card,
.donation-card,
.notice-panel,
.comparison-panel {
  border: 1px solid var(--of-border);
  border-radius: 24px;
  background: var(--of-surface);
  box-shadow: var(--of-shadow-card);
}
```

Use 24–30px desktop and 18–22px mobile padding only on components whose image wrapper does not own padding.

- [ ] **Step 2: Normalize equal-height grids**

Apply `grid-auto-rows: 1fr` and card `height: 100%` to resource, team, voice, tourism, included, activity, service, trust and admission grids where comparable cards share rows.

- [ ] **Step 3: Normalize buttons and focus**

Apply safe wrapping, 44px minimum height, consistent padding and visible focus rings. Keep primary gold, secondary cream and dark-primary variants distinct.

- [ ] **Step 4: Restrict hover and normalize reveal motion**

Use capability-gated hover only for clickable cards/buttons and a maximum 3px lift. Keep static cards stationary. Set reveal movement to 14px and support reduced motion with `.001ms` transitions.

- [ ] **Step 5: Tune photo crops and palette**

Use consistent object-fit, warm restrained saturation/contrast, and component-specific object-position. Do not replace images unless a rendered semantic/crop defect is verified.

- [ ] **Step 6: Apply conservative copy corrections**

Change only visibly repetitive or overflowing strings. Every changed key must have equivalent RO/RU/EN values and retain factual meaning.

- [ ] **Step 7: Implement responsive rules**

At mobile widths, use one-column cards, 18–22px padding, deliberate gaps and full-width major CTAs. At tablet widths, collapse grids before text becomes cramped. Preserve the completed hero behavior.

- [ ] **Step 8: Run and confirm GREEN**

Run validator and `git diff --check`; expected zero failures.

- [ ] **Step 9: Commit system polish separately**

```powershell
git add index.html scripts/validate_site.py
git commit -m "Polish all site cards spacing animations and copy"
```

### Task 5: Rendered And Functional Audit

**Files:**
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\exports\cards-full-1440.png`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\exports\cards-tablet-768.png`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\exports\cards-mobile-390.png`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\exports\resource-cards.png`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\exports\team-section.png`
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\exports\donation-section.png`

- [ ] **Step 1: Run the 27-case viewport-language matrix**

Test RO/RU/EN at 360, 375, 390, 414, 430, 768, 1024, 1280 and 1440px. Assert no horizontal overflow, no button/card overflow, no broken images, no empty translations and valid header/sticky behavior.

- [ ] **Step 2: Inspect every component family**

Measure rendered card counts, equal-height rows and button containment for resource, team, tourism, voice, activity, service, trust, admission and donation sections.

- [ ] **Step 3: Test interactions**

Verify menu, modal, forms, FAQ, bank accordions and copy buttons. Confirm zero console errors.

- [ ] **Step 4: Test external functionality**

Confirm HTTP 200 for PDFs, Word, PayPal, Telegram bot, Worker health, sitemap and robots. Send one clearly labeled production Telegram test only after deployment.

- [ ] **Step 5: Capture required screenshots**

Save full-page and section screenshots to `exports` and visually inspect them for spacing, crop, palette and hierarchy.

### Task 6: Push, Deploy And Report

**Files:**
- Create outside repository: `C:\Users\igor\Desktop\OptimaFide_site_work\notes\card-polish-report.md`

- [ ] **Step 1: Run fresh verification**

Run validator, XML parse, `git diff --check`, Git status and rendered audit. Do not proceed on failure.

- [ ] **Step 2: Push both commits**

```powershell
git push origin main
```

- [ ] **Step 3: Deploy Cloudflare Pages**

```powershell
npx --yes wrangler@latest pages deploy . --project-name optimafide --branch main
```

- [ ] **Step 4: Repeat production audit**

Repeat the 27 rendered checks and all functional endpoints on `https://optimafide.pages.dev/`.

- [ ] **Step 5: Write the report**

Record card/section counts, changes by component, copy/photo changes, responsive results, functional results, screenshot paths, deployment URL and both commit hashes.
