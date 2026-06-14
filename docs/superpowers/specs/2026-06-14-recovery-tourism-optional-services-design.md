# Recovery Tourism and Optional Services Design

## Goal

Extend the Optima Fide landing page with three clearly separated sections that
support its residential rehabilitation positioning:

1. healthy activities available at the center;
2. optional recovery outings across Moldova;
3. optional personal-care, consultation, and practical services.

The additions must feel calm, trustworthy, and rehabilitation-focused rather
than like an entertainment resort or commercial medical clinic.

## Page Structure

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

- a large photographic feature using the user-provided `1.webp` image of the
  Optima Fide center as the main image;
- an explicit localized label stating that outings are arranged by prior
  agreement and for an additional fee;
- six destination cards: monasteries, landscapes and nature, the Dniester
  River, fishing and outdoor rest, cultural and spiritual places, and
  individually agreed outings;
- a localized note explaining that outings depend on the participant's
  condition, program rules, weather, and prior agreement.

Existing repository WebP/JPG tourism images will be reused for the destination
cards. The main image is supplied by the project owner. No image with uncertain
licensing will be introduced.

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

`Add recovery tourism and optional activity services`

Then push to `main` and verify the production HTML and rendered page.
