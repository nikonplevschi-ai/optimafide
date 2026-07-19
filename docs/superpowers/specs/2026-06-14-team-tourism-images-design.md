# Team and Tourism Images Design

## Goal

Improve trust and visual consistency in two areas:

1. make the team section accurate and complete;
2. make recovery outings calm and place-focused, without foreground people,
   while using real center activity photos when available.

## Team Section

- Remove Andrei Buhna completely, including initials, contacts, and translation
  keys.
- Keep five confirmed people: Igor Plevschi, Anastasia Plevscaia, Ruslan
  Magari, Oksana Harbolinscaia, and Tudor Rotaru.
- Use the matching real photos from `C:\Users\igor\Desktop\РєРѕРјР°РЅРґР°`.
- Do not add Ivan Kopciac because no confirmed role was provided.
- Preserve existing confirmed contacts. Tudor uses `078377337` and the
  existing project email `sofos82@mail.ru`.
- Every card contains a photo, localized name, localized role, one short
  localized function line, and available contacts.
- Cards have equal structure and height. Use a three-column desktop grid,
  two-column tablet grid, and one-column mobile grid.

## Recovery Outings

- Remove tourism images whose visual focus is a person, portrait, or horse.
- Use calm, warm, place-focused images: monasteries, Moldova landscapes,
  Dniester/water, walking areas, fishing/outdoor rest, and cultural/spiritual
  places.
- Prefer suitable existing project assets. For missing subjects, use only
  licensed Wikimedia Commons, Unsplash, or Pexels images and record source and
  license/attribution in `assets/images/tourism/CREDITS.md`.
- Store new optimized images as WebP under `assets/images/tourism/`.
- Use the owner-provided desktop image
  `465382576_27402833706026883_6960522537795147385_n.jpg` for walks and
  quiet rest.
- Use the owner-provided desktop image
  `652216466_34272583262385192_4894032945407263329_n.jpg` for spiritual and
  cultural places.
- Keep consistent image proportions, subtle hover zoom, and working lightbox.
- Keep all visible text and alt text localized through RO/RU/EN translations.

## Center Activities

- Search connected Google Drive for real Optima Fide photos of billiards,
  table tennis, and the football field.
- If confirmed real center photos are found, optimize them as WebP under
  `assets/images/activities/` and use them in the corresponding cards.
- If no confirmed photos are found, retain the current neutral cards. Do not
  introduce unrelated stock photos as center photos.

## Verification

- Andrei Buhna and initials `AB` are absent from source and production.
- Tudor Rotaru has a real photo and confirmed contact details.
- Every remaining team card has name, role, function line, and available
  contacts.
- Tourism section contains no foreground people or person-focused photos.
- RO/RU/EN switch all updated content and alt text.
- Desktop, tablet, and mobile have no overflow or broken layouts.
- No local image is broken; lightbox works; browser console has no errors.

## Commits

- `Fix team section and add Tudor Rotaru photo`
- `Replace tourism people photos and update activity images`
