# Weekend Together Design

## Goal

Add a new three-day, two-night "Weekend Together" introductory service without changing the approved premium sage, ivory, and gold design direction or the existing homepage structure.

## Placement And Composition

The new `#weekend-together` section sits immediately after the confidential consultation block and before the admission section. It is a self-contained premium offer: a calm existing support image on the left, concise service copy on the right, and a distinct price panel that remains visually warm rather than resembling a price table.

On narrow screens the content becomes one column in this order: heading, image, description, included items, prices, safety note, continuation note, and calls to action. The section must not introduce horizontal scrolling at any supported viewport.

## Content

All visible content is available in Romanian, Russian, and English through the site's existing `data-i18n` dictionary pattern. The language uses "participant", "person who needs support", and "loved one" equivalents and avoids promises of treatment, guaranteed outcomes, or rapid recovery.

The section explains that the format is for a participant with a relative, friend, or other loved one to see the center, experience its rhythm, speak with the team, and understand a possible next step. It lists accommodation for three days and two nights, meals, orientation, participation in the center's calm routine, a consultation, a conversation with the accompanying person, and help understanding possible next steps.

## Pricing

Only these weekend prices are displayed:

- Participant plus one loved one: `4 900 MDL`
- Participant arriving alone: `3 500 MDL`
- Additional accompanying person: `+1 400 MDL`
- Reservation: `1 000 MDL`, included in the total weekend price

No prices for one week, two weeks, one month, three months, six months, or any longer residential program are added. A localized note states that options and conditions for a longer stay are discussed individually after consultation.

## Actions And Form

The primary booking action opens `https://t.me/optimafide_bot` directly. Secondary actions open WhatsApp and the phone link. The existing consultation form receives one localized support-type option for Weekend Together; its current submission behavior remains unchanged.

## FAQ And Safety

Three localized FAQ entries cover leaving after the weekend, having a loved one present for all three days, and discussing a longer stay. A localized safety note clearly states that Weekend Together is not medical detoxification, does not replace emergency medical care, and requires a preliminary conversation to confirm that the format is safe for everyone involved.

## Assets And Boundaries

Reuse an existing calm family-support image already shipped with the site, avoiding a new generated or stock asset. Do not alter the accreditation presentation, payment links, downloadable PDF or Word files, social links, Telegram Worker behavior, existing contact flows, sitemap, or robots rules except where verification reveals a direct regression caused by this feature.

## Verification And Delivery

Add a focused validation test that initially fails because the new section, translations, prices, support option, and FAQ entries are absent. After implementation, run the focused test, `python scripts/validate_site.py`, and `git diff --check`. Verify RO/RU/EN, supported responsive widths, images, console, links, downloads, sitemap, robots, and production deployment. Save the requested desktop, mobile, and price-card screenshots plus the report, then commit with `Add Weekend Together service`, push `main`, and deploy Cloudflare Pages.
