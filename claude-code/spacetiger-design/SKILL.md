---
name: spacetiger-design
description: Space Tiger AI Systems' brand design system — colors, type, buttons, cards, forms, and voice — extracted directly from spacetiger-site.hasnat-68e.workers.dev. Use whenever building a new document, deck, artifact, landing page, or mockup that should carry Space Tiger's look. Trigger on "Space Tiger," "our brand," "make it look like the website," "use our design system," or any Space Tiger-branded deliverable.
---

# Space Tiger design system

Source: live inspection (computed styles + DOM) of `spacetiger-site.hasnat-68e.workers.dev`
across `/`, `/what-we-build`, `/contact`, captured 2026-08-20. Every value below is a
real computed style pulled from the site, not a guess.

## Voice & feel

Retro sci-fi poster meets plain-spoken operator. A painterly astronaut-tiger mascot and
nebula/moon illustrations sit against otherwise flat, high-contrast, almost brutalist UI
type. Copy is short and second-person ("Book a free 30 min call," "Tell us what is
taking too much time") — never corporate throat-clearing. Don't reproduce the actual
mascot/illustration artwork (it's the site's copyrighted art); it's fine to describe the
style (painterly, sci-fi, warm nebula palette) when a new piece wants that same feel.

## Color tokens

| Token | Hex | Use |
|---|---|---|
| Paper | `#f1eada` | primary light background; also text-on-dark |
| Ink | `#000000` | primary text on light backgrounds |
| Brand purple | `#461d7c` | primary action color, links, borders, inline headline emphasis |
| Hero purple | `#291244` | hero section background |
| Void purple | `#1e0a3c` | alternate dark section background |
| Card purple-black | `#130624` | card/tile fill sitting on a dark section |
| Signal gold | `#f7c52d` | sparing accent only — step numerals, one emphasized word in a dark hero |

Pattern: alternate full-bleed sections between **Paper** and one of the dark purples for
rhythm. Inside an otherwise-Ink headline, recolor one word/phrase Brand purple (on light)
or leave it Paper/Gold (on dark) for emphasis — never recolor the whole headline. Gold is
a hit, not a fill: never use it as a background or for body text.

## Type

- **Display face:** `"Bebas Neue"` — every heading. Always uppercase, weight 700, tight/
  neutral tracking. Scales from ~90px (desktop h1/h2) down to ~19px (card titles).
- **Body/UI face:** `"Oswald"`, weights 400/500/600/700 — paragraphs, nav, buttons,
  labels, form fields. Contact-page body copy is actually weight 700 at 14px — this
  brand leans heavier than typical body text, don't default to 400 everywhere.
- Google Fonts import:
  `https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Oswald:wght@400;500;600;700&display=swap`
- **Eyebrow/label pattern:** Oswald 700, 10–13px, uppercase, letter-spacing ~0.6–1.95px,
  Brand purple on light backgrounds / Paper on dark backgrounds. Sits above every
  headline and above every form field.

## Shape language — this contrast is deliberate, keep it

| Element | Radius |
|---|---|
| Buttons | `99px` (full pill) |
| Form inputs | `3px` (sharp, minimal) |
| Cards / sections | `0px` (square, no shadow) |

Interactive controls are round; containers are square. Don't blur this line by giving
cards rounded corners or buttons sharp ones.

## Components

**Primary button (filled):** bg Brand purple, text Paper, 1px solid border (same
purple), radius 99px, padding ~13–20px vertical / 18–36px horizontal (bigger for hero
CTAs, smaller for nav), Oswald 600–700, trailing arrow glyph (↗ for external actions/
booking, → for in-page actions), label in normal case (not all-caps).

**Secondary button (outline):** transparent bg, 2px solid Brand purple border, Brand
purple text, same radius/padding/font as primary.

**Nav links:** plain text, Ink, Oswald 600, no background, no underline.

**Form field:**
- Label: Oswald 700, 10px, uppercase, Brand purple, letter-spacing 0.6px, above the field.
- Input/textarea: bg Paper at ~52% opacity (`rgba(241,234,218,0.52)`), border 1px solid
  Brand purple at 25% opacity (`rgba(70,29,124,0.25)`), radius 3px, padding 13px 14px,
  Oswald 14px, Ink text.
- Submit button: same spec as the primary button.

**Feature card / tile:** bg Card purple-black (`#130624`) on a dark section, radius 0,
no shadow, no border, generous padding (~40px 32px 36px). Title in Bebas Neue uppercase
Paper text (~19px); supporting list in Oswald.

**Section rhythm:** full-bleed sections alternating Paper → dark purple → Paper. Each
section carries one eyebrow label, one Bebas Neue headline, short Oswald body copy, and
one or two pill CTAs.

## How to apply this to a new document/deck/page

1. Load Bebas Neue (display) + Oswald 400/500/600/700 (body/UI) via the Google Fonts
   link above, or the closest system fallback (bold condensed sans for display, mid-
   weight grotesque/condensed sans for body) if Google Fonts isn't available.
2. Default background is Paper (`#f1eada`). Reach for Hero purple or Void purple only
   for a deliberate hero/emphasis moment, not as a general background.
3. Headlines: Bebas Neue, uppercase, Ink by default, with exactly one emphasized
   word/phrase recolored per the color table above.
4. Any CTA: pill radius 99px, filled or outline Brand purple — don't invent a third
   button style.
5. Any input-like element: 3px radius, translucent Paper fill, thin Brand-purple-25%
   border — keep it visually quieter than buttons.
6. Any card/tile: square corners, no shadow; use Card purple-black fill if it sits on a
   dark section, otherwise Paper.
7. Copy: short, second-person, plainly worded — cut anything that reads like corporate
   boilerplate.
