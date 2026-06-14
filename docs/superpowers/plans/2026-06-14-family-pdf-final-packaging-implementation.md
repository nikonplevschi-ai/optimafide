# Family PDF And Final Packaging Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Finalize the family-facing site copy and publish a visually verified Russian family PDF.

**Architecture:** Keep the static multilingual site architecture and extend its translation overrides. Generate a branded DOCX with python-docx, render it through the bundled document renderer, and publish the resulting PDF as a static asset.

**Tech Stack:** HTML/CSS/JavaScript, Python, python-docx, LibreOffice renderer, GitHub Pages.

---

### Task 1: Finalize Website Copy
- [ ] Update team roles/functions and Oksana's name in RO/RU/EN.
- [ ] Align tourism captions with the photographs.
- [ ] Add the multilingual important notice and PDF download CTA.
- [ ] Run `python scripts/validate_site.py`.

### Task 2: Build Family PDF
- [ ] Create the Russian family packet generator.
- [ ] Generate DOCX and PDF using real project assets.
- [ ] Render and inspect every page, then correct layout defects.

### Task 3: Publish And Verify
- [ ] Verify local desktop/mobile, languages, download, images, overflow, and console.
- [ ] Commit and push.
- [ ] Verify production HTML and PDF download.
