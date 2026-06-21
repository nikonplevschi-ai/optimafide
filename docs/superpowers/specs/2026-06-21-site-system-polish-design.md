# Optima Fide Site System Polish Design

## Goal

Bring every section below the completed `hero--calm` into one premium ivory, sage, deep-green and muted-gold design system without removing sections, changing program meaning, or disrupting working integrations.

The completed hero remains the visual standard and is not redesigned in this stage. Its production commit is `007402f`.

## Scope And Constraints

- Preserve all existing sections, factual claims, program information, navigation targets and bank details.
- Preserve RO/RU/EN switching and equivalent meaning in all three languages.
- Preserve Telegram forms and Worker, `@optimafide_bot`, PayPal, PDF, Word, phone, Google verification, canonical, sitemap and robots.
- Do not merge or remove sections unless two adjacent fragments are exact presentational duplicates. No aggressive shortening or structural redesign.
- Keep the implementation in the existing static `index.html` and `scripts/validate_site.py` architecture.
- Treat `https://optimafide.pages.dev/` as the primary production URL.

## Design System

Use the existing `--of-*` hero tokens as the source of truth. Add focused aliases only when they clarify ownership, such as card radius, card padding, section spacing and interactive shadow.

### Approved Color Palette

The site must use these exact primary tokens:

```css
:root {
  --of-bg: #f5efe4;
  --of-surface: #fffaf1;
  --of-surface-soft: #f8f2e7;
  --of-green-deep: #06261f;
  --of-green-main: #0b372c;
  --of-green-soft: #dfe8dc;
  --of-sage: #8fa086;
  --of-sage-light: #eef3ea;
  --of-gold: #c99a3d;
  --of-gold-soft: #d9b86c;
  --of-gold-hover: #b8872f;
  --of-text: #10251f;
  --of-muted: #65736b;
  --of-border: rgba(16, 37, 31, .11);
  --of-shadow: 0 18px 55px rgba(18, 44, 36, .11);
}
```

Body uses `--of-bg`, cards use `--of-surface`, soft sections use `--of-surface-soft`, headings use `--of-green-deep`, body copy uses `--of-text`, muted copy uses `--of-muted`, primary CTA uses `--of-gold` with `--of-gold-hover`, badges use `--of-sage-light` or `--of-surface`, and borders/shadows use the approved tokens.

Remove accidental cold-gray and blue UI accents. Photography keeps realistic sky and environmental colors, but shared UI surfaces must remain warm, sage-toned and residential rather than clinical or office-like.

The hero mist is adjusted to the approved warmer blend:

```css
background:
  radial-gradient(circle at 12% 82%, rgba(143, 160, 134, .30), transparent 36%),
  radial-gradient(circle at 78% 18%, rgba(217, 184, 108, .18), transparent 32%),
  linear-gradient(90deg, rgba(255, 250, 241, .96), rgba(255, 250, 241, .48), rgba(223, 232, 220, .22));
```

### Surfaces

- Default card radius: 24px, with a permitted 22–28px range for component-specific proportions.
- Default desktop padding: 24–30px.
- Default mobile padding: 18–22px.
- Default surface: translucent warm white/cream.
- Border: one-pixel deep-green line at approximately ten percent opacity.
- Default shadow: restrained `--of-shadow-card`.
- Interactive shadow: slightly stronger, paired with a maximum three-pixel lift.
- Cards in the same grid row use equal-height grid behavior where their content model is comparable.

Shared rules are grouped by visual responsibility, but component-specific selectors retain image aspect ratios, special layouts and functional behavior. A blanket `.card` rule is not applied blindly.

### Typography

- Cormorant Garamond remains the section and card-heading font where already appropriate.
- Inter remains the body, navigation, label and control font.
- Card headings use consistent line-height and balanced wrapping.
- Body copy uses a calm readable line-height and muted deep-green color.
- Eyebrows, captions and metadata share a compact Inter treatment.

### Buttons And Links

- Primary: muted-gold pill, deep-green text.
- Secondary: cream/warm-white pill with subtle border.
- Dark primary remains available only where contrast requires it.
- Text links use deep green with a restrained underline or arrow only when useful.
- Minimum touch height is 44px, increasing to 48px for major mobile actions.
- All buttons use `max-width: 100%`, safe wrapping, consistent padding, visible focus styling and no overflow.

## Component Groups

### Resource Cards

The four document/consultation cards retain their content and destinations. They use equal-height rows, compact copy, aligned actions and short existing CTA labels. Buttons remain inside each card at every viewport.

### Team Cards

The five team cards retain current photos, roles, phone numbers and emails. Portrait frames use consistent aspect ratio, `object-fit: cover`, manually tuned object position where needed, equal card heights and quieter contact styling.

### Program, Conditions And Information Cards

Situation, activity, service, trust, admission, included and comparison cards share surface, border, radius, spacing and heading rhythm. Dense groups retain all facts but use more deliberate grids, consistent content alignment and less visual repetition.

### Photo And Story Sections

Story, visual-program, gallery and tourism imagery keeps its current semantic mapping. Crops and object positions are tuned per image. Adjacent duplicates are prohibited. A restrained common saturation/contrast treatment may be applied through CSS; source replacement occurs only when an image is objectively mismatched or unusable.

### Voices

Anonymous stories retain all names-as-changed notices and meaning. Cards receive consistent spacing, calmer quote styling, equal rhythm and no exaggerated hover.

### Donation And Bank Details

Donation copy, PayPal, Telegram and banking data remain unchanged in meaning. The visual hierarchy separates primary support actions from dense banking rows. Accordions keep stable opening behavior, readable labels and aligned copy controls.

### FAQ And Accordions

FAQ and bank accordions share border, radius, focus treatment and disclosure rhythm. Opening content must not visually jump or overflow. Motion remains subtle and accessible.

### Contact, Forms And Footer

Contact cards, Telegram CTA, forms and footer adopt the same surfaces, spacing and button system. Labels, status messages, consent and modal behavior remain intact.

## Copy Policy

- Remove only obvious repetition within the same card or adjacent heading/lead pair.
- Shorten buttons where needed for fit, while preserving action meaning.
- Do not introduce medical guarantees, cure claims, urgency pressure or unsupported metrics.
- Preserve calm, respectful and professional tone.
- Every copy change must be applied consistently to RO/RU/EN and covered by translation validation.

## Motion And Interaction

- Existing reveal behavior is retained and normalized to a soft opacity/vertical movement.
- Hover lift is applied only to interactive cards, links, buttons and clickable images.
- Static informational cards do not move merely because they look like cards.
- Focus-visible styles are present for links, buttons, summaries and form controls.
- `prefers-reduced-motion: reduce` disables animations and reduces transition duration to an effectively immediate value.

## Responsive System

- Required widths: 360, 375, 390, 414, 430, 768, 1024, 1280 and 1440px.
- Comparable cards stack to one column on mobile and preserve deliberate gaps.
- Tablet grids collapse before text becomes cramped.
- Buttons become full-width only when that improves touch usability and composition.
- No card, button, image, table-like bank row or translated text may create horizontal scrolling.
- Sticky CTA must not cover important content.

## Accessibility

- Preserve and validate image alt text, form labels, modal attributes and disclosure semantics.
- Add consistent focus-visible treatment.
- Maintain readable contrast across ivory, cream, sage, gold and green surfaces.
- Interactive and non-interactive cards remain visually distinguishable.

## Performance

- Retain WebP usage and lazy loading below the hero.
- Hero stays eager; below-fold images use lazy loading and async decoding where supported.
- Avoid introducing new large image assets unless required by a verified visual defect.
- Verify zero failed local asset requests and zero broken rendered images.

## Verification And Artifacts

Extend `scripts/validate_site.py` with regression checks for the shared card system, safe buttons, reduced motion and critical localized copy. Run it before commit and after all changes.

Browser verification covers RO/RU/EN and every required width. It checks horizontal overflow, card/button containment, broken images, header and sticky CTA behavior, console errors and interactive controls.

Functional verification covers family PDF, partner PDF, Word, PayPal, Telegram Worker submission, Telegram bot, phone link, forms, copy buttons, accordions, canonical, sitemap, robots and Google verification.

Save artifacts under `C:\Users\igor\Desktop\OptimaFide_site_work\`:

- `exports`: full-page 1440px, full-page 390px, 768px tablet, hero, resource cards, team and donation screenshots.
- `notes\card-polish-report.md`: component counts, concrete changes, copy changes, photo/crop changes, responsive evidence, functional evidence, deployment URL and commit hash.
- `backups`: pre-polish `index.html` and validation script.

## Delivery

Create two ordered stage-two commits:

1. Color palette and warm hero mist:

`Refine site color palette with premium sage tones`

2. Card, spacing, animation and copy system:

`Polish all site cards spacing animations and copy`

Push `main`, deploy Cloudflare Pages after both commits, verify `https://optimafide.pages.dev/`, and report both commit hashes. The completed hero stage remains a separate prior commit.
