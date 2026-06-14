# Team and Tourism Images Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Correct the team section and replace person-focused tourism imagery while using confirmed real activity photos when available.

**Architecture:** Preserve the static single-page structure and current translations. Prepare optimized assets in focused image directories, update only the team/activity/tourism components, and extend validation for removed content and image integrity.

**Tech Stack:** Static HTML/CSS/JavaScript, Pillow image processing, Google Drive connector, browser verification, Git/GitHub Pages.

---

### Task 1: Prepare and Integrate Team Photos

**Files:**
- Modify: `index.html`
- Create/Replace: `assets/images/team-*.webp`
- Modify: `scripts/validate_site.py`

- [ ] Optimize the five confirmed desktop-folder photos to WebP.
- [ ] Remove Andrei Buhna card and translation keys.
- [ ] Replace all five remaining team images with confirmed photos.
- [ ] Add localized one-line function text to every card.
- [ ] Make cards equal-height with consistent photo aspect ratio.
- [ ] Validate source contains no Andrei/AB and commit.

### Task 2: Search for Real Activity Photos

**Files:**
- Modify if photos found: `index.html`
- Create if photos found: `assets/images/activities/*.webp`

- [ ] Search Google Drive for billiards, table tennis, and football field.
- [ ] Use only confirmed Optima Fide center photos.
- [ ] If not found, leave current neutral cards unchanged and record this fact.

### Task 3: Replace Tourism People Photos

**Files:**
- Modify: `index.html`
- Create: `assets/images/tourism/*.webp`
- Create: `assets/images/tourism/CREDITS.md`

- [ ] Audit current tourism assets for foreground people/person focus.
- [ ] Prefer suitable person-free existing assets.
- [ ] Find licensed person-free images only for missing themes and document sources.
- [ ] Update cards, localized alt text, hover zoom, and lightbox.
- [ ] Validate and commit.

### Task 4: Verify and Publish

**Files:**
- Modify if findings require: `index.html`
- Modify if findings require: `scripts/validate_site.py`

- [ ] Run local validation and JavaScript syntax checks.
- [ ] Verify desktop/tablet/mobile, languages, images, lightbox, and console.
- [ ] Push `main`.
- [ ] Verify production HTML and rendered production page.

