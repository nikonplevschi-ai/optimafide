# Premium Typography Pass Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refine Optima Fide typography and spacing so the existing site feels lighter, more premium, and more readable without changing structure or content.

**Architecture:** Keep the current static single-file site. Add a final typography refinement layer near the end of the existing `index.html` stylesheet so it overrides earlier heavier rules while preserving existing layout, integrations, translations, and dirty worktree state.

**Tech Stack:** Static HTML/CSS/JavaScript in `index.html`, existing Python validator, local browser screenshots.

---

### Task 1: Typography CSS Layer

**Files:**
- Modify: `C:\Users\igor\Desktop\optimafide\index.html`

- [x] Update the Google Fonts URL to include Cormorant Garamond weights `400;500;600;700`.
- [x] Add `.editorial-text` and `.text-accent-gold` utilities.
- [x] Add a final CSS layer that sets hero title weight to `500`, large section headings to `500`, card headings to `600`, body copy to Inter with calm line-height, and softer spacing around headings, leads, CTAs, cards, FAQ, donation, footer, and mobile.
- [x] Use `.editorial-text` only on one or two existing strong headings without changing their text.

### Task 2: Static Validation

**Files:**
- Read: `C:\Users\igor\Desktop\optimafide\scripts\validate_site.py`
- Verify: `C:\Users\igor\Desktop\optimafide\index.html`

- [x] Run `python scripts/validate_site.py`.
- [x] Run `git diff --check`.
- [x] Inspect the diff to confirm no sections or content were removed.

### Task 3: Browser QA And Screenshots

**Files:**
- Create screenshots under `C:\Users\igor\Desktop\OptimaFide_site_work\exports\`

- [x] Start a local static server for the repo.
- [x] Open the page at desktop `1440px` and mobile `390px`.
- [x] Check console errors, horizontal scroll, broken images, key outbound/file links, language buttons, contact modal, and forms at a non-destructive level.
- [x] Save `typography-pass-desktop.png`, `typography-pass-mobile-390.png`, `typography-pass-hero.png`, and `typography-pass-key-sections.png`.

### Task 4: Commit And Push

**Files:**
- Commit only intentional files.

- [x] Stage `index.html` and the plan document.
- [ ] Commit with `Refine premium typography and spacing`.
- [ ] Push `main`.
- [ ] Report production URL, deployment URL if available, commit hash, changed files, screenshots, validation results, and functional preservation notes.
