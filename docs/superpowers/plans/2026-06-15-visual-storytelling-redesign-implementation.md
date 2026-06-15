# Visual Storytelling Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the existing Optima Fide homepage into a calmer image-led story while preserving all working integrations.

**Architecture:** Keep the static single-file site and existing localization/interaction code. Add focused editorial sections and responsive CSS, consolidate repeated cards, and extend the validator with structural requirements.

**Tech Stack:** HTML, CSS, vanilla JavaScript, Python validator

---

### Task 1: Structural Contract

**Files:**
- Modify: `scripts/validate_site.py`

- [ ] Require the new life, recovery spaces, consolidated program, and day timeline sections.
- [ ] Run `python scripts/validate_site.py` and confirm it fails because the new markup is absent.

### Task 2: Visual Storytelling Sections

**Files:**
- Modify: `index.html`

- [ ] Add the life-in-center editorial section after consultation.
- [ ] Convert the center gallery to an asymmetric visual strip with lazy-loaded images.
- [ ] Replace eight repeated included cards with four thematic visual panels.
- [ ] Present the daily rhythm as a scene with one large photo and a responsive timeline.
- [ ] Add responsive styles for the required mobile widths.
- [ ] Run `python scripts/validate_site.py` and confirm it passes.

### Task 3: Browser Verification

**Files:**
- Verify: `index.html`

- [ ] Serve the site locally.
- [ ] Check desktop and mobile for overflow, menu, language switching, gallery, and console errors.
- [ ] Check PDF, PayPal, and Telegram destinations remain present.
- [ ] Commit and push the verified redesign.

