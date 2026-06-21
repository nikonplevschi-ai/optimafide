# Optima Fide Premium Calm Hero Design

## Goal

Replace the current photo-banner hero with a light, premium `hero--calm` composition matching the approved reference. The primary production and SEO URL is `https://optimafide.pages.dev/`.

## Visual Direction

- Use a single rounded hero card rather than two rigid split rectangles.
- Keep an ivory, cream, sage, muted-gold palette with soft layered mist.
- Place text on the left and the real Optima Fide building on the right, blending both areas with gradients instead of a hard divider.
- Preserve the building architecture and realistic surroundings. Photo processing may improve exposure, white balance, blue cast, contrast, and warmth, but must not invent structural details.
- Keep the entire roof and facade readable.

## Header

- Retain the existing functional header and language/mobile navigation behavior.
- Refine it to the approved light premium composition: brand left, navigation centered, phone and consultation CTA right when space permits.
- Use `Cormorant Garamond` for the brand and `Inter` for navigation and actions.
- Do not add unconfirmed opening hours.

## Hero Structure

The active section class is `hero hero--calm` and contains:

1. A rounded light hero frame with thin border and soft shadow.
2. A separate building image layer on the right.
3. A content layer on the left with short badges, headline, subtitle, and two CTAs.
4. A compact trust line at the bottom.
5. Very slow decorative sage/ivory/gold mist layers with reduced-motion support.

The primary CTA opens the consultation path. The secondary CTA opens the existing Telegram contact flow. Existing phone, modal, Worker, and downstream sections remain functional.

## Copy

### Romanian

- Headline: `Un loc unde te poți opri și începe din nou`
- Subtitle: `Program rezidențial de recuperare: cazare, masă, ritm zilnic, comunitate terapeutică și sprijin pentru familie.`
- CTAs: `Solicită o consultație`, `Scrie în Telegram`
- Badges: `Acreditare de stat`, `Program 6–12 luni`, `Cazare și masă`, `20 locuri`, `Goianul Nou, Stăuceni`
- Trust line: `Acreditare · 20 locuri · 500+ persoane sprijinite · confidențial`

### Russian

- Headline: `Место, где можно остановиться и начать заново`
- Subtitle: `Резиденциальная программа восстановления: проживание, питание, ежедневный ритм, сообщество и поддержка семьи.`
- CTAs: `Запросить консультацию`, `Написать в Telegram`
- Badges: `Государственная аккредитация`, `Программа 6–12 месяцев`, `Проживание и питание`, `20 мест`, `Goianul Nou, Stăuceni`
- Trust line: `Аккредитация · 20 мест · 500+ человек получили помощь · конфиденциально`

### English

- Headline: `A place to pause, recover and begin again`
- Subtitle: `A residential recovery program with accommodation, meals, daily rhythm, community support and family guidance.`
- CTAs: `Request a consultation`, `Write on Telegram`
- Badges: `State accreditation`, `6–12 month program`, `Accommodation and meals`, `20 places`, `Goianul Nou, Stăuceni`
- Trust line: `Accredited · 20 residential places · 500+ people supported · confidential`

## Typography And Tokens

- Heading font: `Cormorant Garamond`, weights 500, 600, 700.
- Body font: `Inter`, weights 400 through 800.
- Hero title: weight 700, line-height 0.96, letter-spacing -0.035em, desktop clamp up to 5.8rem for safe Russian wrapping.
- Subtitle: weight 500, line-height 1.55, maximum width about 580px.
- Buttons: 0.96rem, weight 800, pill shape, minimum height about 52px.
- Badges: compact pill shape, roughly 0.72rem to 0.84rem.
- Colors and shadows follow the approved `--of-*` ivory, cream, deep green, sage, muted gold, border, and shadow tokens.

## Motion

- Mist movement is almost static, with 16–19 second alternate animations.
- Hero and content use a short, soft initial reveal.
- `prefers-reduced-motion: reduce` disables all hero and mist animation.

## Responsive Behavior

- Desktop and tablet retain the blended left-content/right-building composition.
- At 768px and below, the hero becomes a vertical flow: building image first, content second, trust line last.
- The mobile image uses `object-fit: contain` and does not crop the roof or facade.
- Badges wrap naturally, CTAs become full-width, and trust separators are removed when needed.
- Required viewport checks: 360, 375, 390, 414, 430, 768, 1024, and 1280px.
- No horizontal scrolling, overflow, badge/title overlap, or excessive empty vertical space is allowed.

## Alternative Modes

- Prepare inactive `hero--family` and `hero--trust` classes as styling modes only.
- `hero--family` is warmer and more supportive.
- `hero--trust` is more formal and green-toned.
- Neither alternative is rendered simultaneously or exposed as a user-facing switch.

## Assets And Work Files

Create and maintain:

`C:\Users\igor\Desktop\OptimaFide_site_work\`

with `mockups`, `hero-variants`, `processed-images`, `backups`, `exports`, and `notes` subdirectories. Store the source building image, processed variants, final hero image, desktop/mobile screenshots, before/after comparison, backups of important edits, and the final report there.

## Compatibility And Verification

- Preserve RO/RU/EN switching, mobile menu, Telegram form and Worker, Telegram bot, PayPal, PDF, Word, Google verification, canonical, sitemap, robots, and all sections below the hero.
- Keep the canonical, Open Graph URL, sitemap, and robots aligned to `https://optimafide.pages.dev/`.
- Run `python scripts/validate_site.py`.
- Run npm build/lint only if matching scripts exist.
- Verify both site URLs return HTTP 200, while treating `optimafide.pages.dev` as primary.
- Verify all required viewports, languages, local assets, console errors, broken images, downloads, PayPal, Telegram Worker submission, sitemap, and robots.

## Delivery

Commit implementation as `Refine premium green-toned hero to match approved concept`, push `main`, deploy Cloudflare Pages, verify production, and report the commit hash and evidence.
