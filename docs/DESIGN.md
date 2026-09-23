# Design system

*Owner: M09 (tokens shared with M10).* Tokens live in `web/static/css/tokens.css`.

## Direction

Liquid Glass, Apple-like. Security blue + green on white; dark mode with deep navy.
Clean, stable, systematic. **No emoji** — all icons are 24×24 stroke SVGs.

## Material

- `.glass`: `background: var(--glass)`, `backdrop-filter: var(--blur)`, 1px `var(--stroke)` border,
  inset top highlight `var(--hi)`, soft shadow, radius `var(--r-lg)` (22px).
- Ambient background: three large blurred blobs (blue, green, light blue) floating slowly (26–38 s).

## Spacing (exactly two gaps)

| Token | Value | Use |
|---|---|---|
| `--gap-section` | 40px (30px mobile) | between major blocks A / B / C |
| `--gap-card` | 20px (14px mobile) | between cards inside a block |

Panel header padding 16×22, body 22×26. Each page: eyebrow (`01 · Data Masking`), large title, lede,
then section labels **A · B · C** with a hairline to the right.

## Sizing follows content

- Source log textarea: min 300px (220 mobile), grows with its content, max 72vh then scrolls.
- Before/after panes: min 260px, max 72vh. Try-it box: min 110px, max 40vh.
- Stat cards are compact so the log stays visually dominant.

## Colour meaning

| Token | Meaning |
|---|---|
| `--blue` | primary action, selection, progress through the DFA |
| `--green` | safe / passed / accepting state / switches on |
| `--bad` | failed / dead state / high risk |
| `--c-card` `--c-email` `--c-phone` `--c-dob` `--c-address` | one colour per data type, everywhere |

## Motion

Spring easing `var(--spring)`. Tab enter: rise + un-blur. Masking: blue bar wipes over each masked span
(staggered 50 ms). Numbers count up. DFA: edges draw, token slides, ACCEPT pulses, REJECT shakes.
Language switch: short blur-fade. Everything off under `prefers-reduced-motion`.

## i18n

Default Thai; TH/EN segmented control in the sidebar; choice stored in `localStorage`.
Every visible string goes through `t(key)`. Server strings arrive in both languages (`label`/`label_en`, …).
Log content itself is never translated.
