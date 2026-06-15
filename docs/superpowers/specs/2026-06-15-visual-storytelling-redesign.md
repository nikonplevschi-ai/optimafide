# Optima Fide Visual Storytelling Redesign

## Goal

Rework the existing single-page Optima Fide website from a long sequence of similar cards into a warm, clear visual story. Keep the current static architecture, three languages, content, forms, documents, and external links working.

## Direction

The page will use large editorial sections inspired by Apple's presentation principles without copying its visual identity. Each viewport should communicate one main idea through a strong image, a short headline, concise supporting copy, and no more than two primary actions.

The visual tone remains calm, trustworthy, residential, and human. Photography should emphasize light, order, home, shared spaces, recovery, and dignity. Recognizable people must only appear where their use is already approved, such as the team section.

## Page Structure

The hero remains the opening section, followed by:

1. Compact confidential consultation block.
2. New two-column "Life in the center" section with a large photograph and three short ideas.
3. "Recovery spaces" editorial gallery: one dominant image, two supporting images, and a horizontal strip.
4. "Who the program is for" expressed as large visual panels or concise icon pills.
5. "What is included" reduced from eight cards to four large thematic blocks:
   - accommodation and meals;
   - daily rhythm;
   - group and individual support;
   - family and reintegration.
6. "A day at the center" as a visual timeline beside one large image.
7. Short "First days" visual section.
8. Team.
9. Recovery voices.
10. PDF materials and donations.
11. FAQ.
12. Contacts.

Existing content that remains useful but interrupts the main story may be consolidated into larger panels, shortened, moved into accordions, or placed later in the page. No working user journey may be removed.

## Components

### Life In The Center

Desktop uses a two-column composition with a large center photograph on the left and title, short copy, three concise points, and two actions on the right. Mobile stacks the photograph above the copy.

### Recovery Spaces

Desktop uses an asymmetric editorial grid and a secondary horizontal visual strip. Mobile becomes a horizontal snap-scrolling gallery with large images and short captions. Images retain their natural proportions through `object-fit: cover`.

### Included Program

The current eight equal cards become four large blocks. Each block combines related existing content and uses a photograph or restrained visual marker. The blocks vary in composition so the section does not read like a table.

### Daily Timeline

Desktop shows morning, day, evening, and quiet/rest on a horizontal line next to a large image. Mobile switches to a vertical line. Copy stays short and avoids schedule-table styling.

### Family And Donations

The family section becomes an emotional image-led section with three soft question rows instead of cards. Donations lead with purpose and show PayPal and Telegram actions first; bank details remain available in an accordion below.

## Content And Localization

Romanian remains the default language. Every new visible string must have Romanian, Russian, and English translations and use the existing `data-i18n` mechanism. Existing phone, Telegram, PayPal, PDF, and contact destinations must remain unchanged.

## Images

Prefer existing approved center images already in the repository. Additional approved Drive images may be selected when accessible and useful. New optimized files belong in `assets/images/visual/` as WebP:

- large images: approximately 1800-2200 px wide;
- medium images: approximately 1200 px wide;
- mobile variants only when they materially improve loading or crop quality.

All below-hero images use `loading="lazy"`. The hero remains eager-loaded.

## Motion

Keep the existing restrained reveal behavior, smooth anchor scrolling, and mobile menu transitions. Hover lift applies only to interactive elements. Respect reduced-motion preferences and avoid decorative motion that delays reading.

## Responsive Behavior

The layout must work at 360, 375, 390, 414, 430, and 768 px widths without page-level horizontal overflow. The gallery may scroll horizontally inside its own bounded area. Language controls, navigation, buttons, PDFs, PayPal, Telegram form, and Telegram modal must remain usable.

## Technical Approach

Keep the website static and preserve the single-file `index.html` architecture because the existing localization and interaction code are tightly integrated there. Add focused CSS classes and replace the relevant HTML section markup. Extend translations only for new strings. Update `scripts/validate_site.py` with structural checks for the new visual sections and retained integrations.

## Verification

Run `python scripts/validate_site.py`, then serve the site locally and inspect desktop and required mobile widths. Confirm:

- Romanian, Russian, and English switch correctly;
- no missing local images or translation keys;
- no page-level horizontal overflow;
- mobile menu and gallery work;
- PDFs, PayPal, Telegram bot link, Telegram request form, and modal remain reachable;
- browser console has no errors.

