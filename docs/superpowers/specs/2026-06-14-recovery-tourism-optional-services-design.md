# Recovery Tourism and Optional Services Design

## Goal

Extend the Optima Fide landing page with three clearly separated sections that
support its residential rehabilitation positioning:

1. healthy activities available at the center;
2. optional recovery outings across Moldova;
3. optional personal-care, consultation, and practical services.

The additions must feel calm, trustworthy, and rehabilitation-focused rather
than like an entertainment resort or commercial medical clinic.

## Main Hero Image

Use the user-provided `D:\рабочая\1.webp` as the site's primary visual symbol
and save it as `assets/images/hero-center.webp`.

Use the image in three places:

1. the main hero;
2. the first center gallery tile;
3. the Open Graph `og:image` metadata.

On desktop, the hero fills the first viewport with the building kept almost
fully visible. A soft dark-green and milky overlay warms the visual appearance,
softens the sky, and gives the left-aligned text sufficient contrast while
leaving the building visible toward the right. The original image file is not
destructively edited.

On mobile, show the image as a substantial separate panel above the hero copy
on a light background. Do not reduce the building to a narrow strip or crop it
aggressively.

The hero uses the localized title and supporting copy for a residential
recovery center in Moldova. Beneath it, show five localized trust badges:
state accreditation, 6-12 month program, accommodation and meals, 20
residential places, and Goianul Nou/Stăuceni.

Add a localized image caption:

- RO: `Centrul rezidențial Optima Fide, Goianul Nou, Stăuceni`
- RU: `Резиденциальный центр Optima Fide, Гоянул Ноу, Стэучень`
- EN: `Optima Fide residential center, Goianul Nou, Stăuceni`

## Page Structure

### Accreditation Certificate

Replace the current certificate image with the user-provided PDF:
`C:\Users\igor\Desktop\Отправка по электронной почте IMG_0001_702ee374-40e9-449d-a99c-4ea800e95c99.pdf`.

The source is a single A4 page (`595.2 x 841.92 pt`) containing one
full-page image. Extract and optimize it as WebP/JPG assets while preserving
the exact A4 aspect ratio. The certificate must remain fully visible without
cropping in the accreditation section and lightbox.

### Center Activities

Extend the existing center-zones area after its photo gallery. Add a compact
five-card grid for billiards, table tennis, football field, barbecue/outdoor
meal area, and courtyard/outdoor rest.

Each card describes the activity through recovery-supporting qualities such as
movement, attention, communication, discipline, teamwork, and healthy rest.
The cards use the site's existing card styling and do not require unverified
photos.

### Recovery Outings Across Moldova

Replace the existing tourism presentation with a dedicated recovery-outings
section positioned after the center conditions/zones content and before the
trust/team/donation area.

The section contains:

- a large photographic feature using a suitable existing repository tourism
  image;
- an explicit localized label stating that outings are arranged by prior
  agreement and for an additional fee;
- six destination cards: monasteries, landscapes and nature, the Dniester
  River, fishing and outdoor rest, cultural and spiritual places, and
  individually agreed outings;
- a localized note explaining that outings depend on the participant's
  condition, program rules, weather, and prior agreement.

Existing repository WebP/JPG tourism images will be reused for the feature and
destination cards. No image with uncertain licensing will be introduced.

### Optional Services

Add a separate section immediately after recovery outings. Use a two-by-three
card grid on desktop and one column on mobile.

Cards cover massage, hairdresser, surgical doctor consultation, addiction
medicine consultants, tests and examinations, and individual practical
services. Every card displays a localized additional-fee badge.

A visible localized disclaimer states that medical consultations, tests, and
examinations are arranged through specialized professionals and institutions,
are not provided independently by the center, and are coordinated separately.

## Localization

All visible new content and image alternative text will use the existing
`translations` object in Romanian, Russian, and English. Existing language
switch behavior remains unchanged.

## Visual Direction

Follow the current warm off-white, green, and gold visual system. Reuse current
card shadows, reveal animation, and rounded corners. The recovery-outings
section gets stronger photographic hierarchy, while activities and services
remain compact enough to preserve the page rhythm.

No new navigation item is required because the current navigation is already
dense. The existing tourism link continues to target the redesigned outings
section.

## Safety and Legal Language

- Outings are always described as optional, arranged by agreement, and paid
  separately.
- Tourism is framed as calm recovery-supporting outings, not a required part
  of rehabilitation or an entertainment resort.
- No treatment, healing, or guaranteed-result claims are added.
- Medical consultations, tests, and examinations are described only as being
  arranged through specialized professionals and institutions.

## Verification

Verify locally at desktop (1440px), tablet (768px), and mobile (375px):

- Romanian, Russian, and English switching updates all new content;
- no horizontal scrolling or overlapping text;
- all images load and preserve aspect ratio;
- lightbox, sticky CTA, map, form, and IBAN copy behavior still work;
- browser console has no errors;
- prohibited legacy strings remain absent.

After implementation, commit with:

`Set center building as main hero image`

and then:

`Add recovery tourism and optional activity services`

Then push to `main` and verify the production HTML and rendered page.
