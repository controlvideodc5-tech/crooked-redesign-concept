**Less doom. More doing.** This system covers the Crooked homepage redesign concept and everything made from it: the site, posters, socials, the newsletter header, stickers and merch. It is an unofficial design exploration, not affiliated with or endorsed by Crooked Media. Show names, show art and marks belong to their owners. Every piece carries the `UnofficialMark`.

Read in this order: this page for the visual rules, **Voice and tone** for how it sounds, **Putting it into practice** for how a brief becomes a poster, a post or a product.

## The idea in one line

Navy carries the brand, yellow does the work, and every piece ends with something to do: **Listen. Show up. Organize.** Keep that order whenever the three appear together.

## Color

- Ground everything in `c-navy-900` (screens use `bg-inverse` for bands) or paper `bg-page`. Paper is blue-biased `c-slate-50`; never pure white for the page. White (`bg-surface`) is for cards and boxes sitting on paper.
- Use `accent-default` (yellow) for the one thing to click, the thing that's playing, focus and progress. If three things on screen are yellow, two of them are wrong.
- Use `status-live` (red 500) as a fill only: live pill, live dot, strike bars, calendar strips. For red text use `status-live-text` (red 700 light, red 300 dark).
- Put the player and nav on `bg-chrome` so tools read apart from editorial.
- Keep `con-*` sky, cream and butter inside Crooked Con placements. Two sanctioned exceptions in collateral: the climate poster sky and the "Hope is a verb" sticker.
- Pink `c-pink-300` is a collateral ground (reproductive freedom, stickers) with navy type. It never appears in product UI.
- Screen proportion: about 45 navy, 35 paper, 10 white, 7 yellow, 3 red.
- Collateral uses the `c-*` primitives directly because print and social art keep fixed colors in either theme. Product UI uses semantic tokens only (`bg-*`, `fg-*`, `border-*`, `accent-*`, `status-*`) so it follows light and dark.

### Contrast, checked (WCAG 2.1)

| Pair | Ratio | Rule |
| --- | --- | --- |
| `fg-default` on `bg-page` | 15.3:1 | Body and headings. |
| `fg-muted` on `bg-page` | 5.5:1 | Secondary text. |
| yellow on navy / navy on yellow | 11.8:1 | Display, links, CTAs, button labels. |
| `c-slate-300` on navy | 8.6:1 | Labels on navy. |
| navy on pink | 10.1:1 | Pink collateral. |
| cream on sky 700 | 4.9:1 | Con headline, upper band only. |
| butter on sky 600 | 3.7:1 | Display size only. |
| white on red 500 | 4.2:1 | 12px bold minimum in UI; display size in collateral. |
| red 700 on paper / on yellow | 5.9:1 / 4.6:1 | Red text. |
| butter or cream on sky 300 | 2.4–2.7:1 | Fails. No type in the lower sky. |
| yellow on white | 1.4:1 | Never. |

Focus: `focus-ring` (yellow) is 1.4:1 on white by itself, so every focus state pairs the 3px yellow outline with a 2px `fg-default` ring. Together they clear 3:1 on paper, white, navy and yellow.

## Type

Three faces, three jobs. Never swap them.

- **Big Shoulders Display 900** for headlines and big numbers: `display-xl` hero, `display-l` section, `display-m` panel, `display-s` sub-head, `display-poster` for collateral. Caps by CSS, written in sentence case so they read right in feeds and screen readers. Leading `.92` on screen, `.86` in collateral.
- **Public Sans** for reading: `lede` 19px, `title` 16–20px bold, `body` 16px, `body-s` 14px, `button` 15px bold.
- **IBM Plex Mono 500** for metadata only: `eyebrow` 12px and `label-s` 11px, caps, tracking `f-track-label`. Show names, times, dates, counts. Tabular numerals for clocks, durations and prices.
- Nothing a person must read goes below 11px. Body copy and buttons are never in display caps. One eyebrow per block, only when it adds a fact.

## Layout, space and shape

- The homepage reads like a rundown: today's lineup first, the player always in reach, one band for the ways to act. Order sections by what a listener does next, not by org chart.
- Max width `layout-max` (1240), gutter `layout-gutter` (16–48). Show grid 4 → 3 at 1000 → 2 at 720. Hero splits 1.25 : 1 and stacks at 860. Sections breathe `space-16` top and bottom.
- Spacing steps: `space-1` 4 through `space-16` 64. Card padding `space-6`; grid gaps `space-5`.
- `radius-pill` for every button, chip, tag and live pill. `radius-lg` (12) for art and cards, `radius-xl` (14) for lineup rows and the player, `radius-2xl` (16) for panels.
- Show art is always 1:1. Floating UI (previews, queues, checklists) gets a 2px `border-strong`.
- Depth: `shadow-card` on hovered cards over navy, `shadow-lift` for popovers and the player, `shadow-art` for fanned art and the email calendar.

## Motion

Move like a broadcast, not a slot machine. 150ms for hovers, 200ms for lifts and toggles, 500ms for slide changes, all on `cubic-bezier(.16, .8, .24, 1)`. The hero dwells 8s with a visible progress bar and a pause button. Ambient motion lives in three places only (the On Crooked drift, the Con sky, the credits roll) and pauses on hover or focus. Under `prefers-reduced-motion` all of it stops: the drift becomes a scroll row and the credits a static list. Motion has no tokens; these values are the rule.

## Imagery, marks and icons

- Each show's own 1:1 art, never recolored or cropped off-square. Fanned stacks rotate in 4° steps, five cards maximum. Host photography for live events, warm and candid.
- The "CROOKED" in this system is Big Shoulders set as a stand-in (`wm`: 34px, 900, tracking .02em). No official logo was supplied and none is drawn here. Production must use Crooked Media's wordmark files. Vote Save America and Friends of the Pod keep their own marks; don't rebuild them in type.
- The halo (a repeating radial ring in 13% yellow on navy) is the only decorative pattern. Collateral adds a small set of flat illustrative devices built from shapes: the sun disc, grass edge, record, calendar, checklist, scoreboard.
- Icons: the concept uses a single inline play triangle and the live dot. There is no icon set yet; when one is needed, use simple 2px-stroke glyphs in `currentColor` and add them under an Icons asset group. No emoji in brand voice; emoji appear only inside quoted chat bubbles.

## Tokens

`tokens.json` keeps the concept's three tiers and names. Primitives are `c-*`, semantic tokens are `bg-*`, `fg-*`, `border-*`, `accent-*`, `status-*`, `focus-ring` and `con-*`, and component tokens are `button-*`, `play-*`, `chip-*`. Components read semantic or component tokens, never primitives; collateral is the one exception, as above. Font families compile to `--font-display`, `--font-body` and `--font-mono`; `bundle.css` maps the concept's `--f-display`, `--f-body` and `--f-mono` to them so the concept's `index.html` keeps working.

Fixes this system makes to the concept:

- Red eyebrow text (3.9:1) now uses `status-live-text`.
- The 9px now-playing pill is 12px bold.
- Con type stays above the gradient midpoint.
- Preview and queue borders use `border-strong`, which flips to slate in dark mode.
- About 20 hard-coded hex values outside `:root` now have token names. In collateral, `#9AA3C0` became `c-slate-400`, `#33406B` became `c-navy-600` and `#262A35` became `c-chrome-800`.
- The "Early-bird ends Oct 6" line is past due; replace it with the current ticket tier or drop it.
