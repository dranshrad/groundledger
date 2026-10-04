# Carousel Engine (Instagram 4:5)

Load only for `social-cast` `carousel` (or `atomize` when a carousel derivative is
requested). Produces a **slide script + optional HTML preview** that can be
exported as 1080×1350 PNGs. Not a separate agent — one pass, compact tables.

**Grounding:** numbers, benchmarks, “algorithm” claims, and testimonials need a
claim-ledger row or explicit author supply
([Grounding Law](../../blog-engine/references/grounding.md)). Prefer omitting a
stat over inventing one. Never invent engagement predictions.

## Brand intake (once)

Pull from `CAST.md` / `BRAND.md` / `VOICE.md` when present. Ask only for gaps:

| Field | Notes |
|-------|--------|
| Brand name | Display on hook / CTA slides |
| Handle | `@…` for caption + optional preview chrome |
| Primary hex | Single seed for the whole palette |
| Font mood | See type table; or named Google Font |
| Voice | bold · warm · minimal · playful · expert |
| Mark | Logo path, brand initial, or skip |
| Assets | Optional: product shot, screenshot (paths or URLs) |

If the user gives a brand URL, infer colour temperature and voice from visible styling.
Confirm the hex before locking. Store the answers in `CAST.md` under a `## Carousel`
block, so that later runs skip intake.

## Palette (from one hex)

| Token | Derivation |
|-------|------------|
| `CORE` | Given hex |
| `CORE_SOFT` | Lighten ~20% |
| `CORE_DEEP` | Darken ~30% |
| `PAPER` | Off-white tinted toward CORE (never `#FFFFFF`) |
| `EDGE` | PAPER one shade down (borders) |
| `INK` | Near-black with a trace of CORE (never `#000000`) |

Signature gradient: `linear-gradient(165deg, CORE_DEEP 0%, CORE 50%, CORE_SOFT 100%)`.

## Type

One heading face + one body face. Never a third.

| Mood | Headings | Body | Fits |
|------|----------|------|------|
| Editorial | Playfair Display | DM Sans | Coaching, lifestyle |
| Clean | Plus Jakarta Sans | (solo) | SaaS, minimal |
| Warm | Lora | Nunito Sans | Wellness, personal brands |
| Technical | Space Grotesk | (solo) | Dev tools, AI, data |
| Statement | Fraunces | Outfit | Agencies, bold creators |
| Formal | Libre Baskerville | Work Sans | Finance, consulting |
| Approachable | Bricolage Grotesque | (solo) | Education, community |

Size scale (at 420px layout width): headline 28–34 / 600 · body 14 / 400 ·
label pills 10 / 600 caps · step numerals 26 / 300 · fine print 11–12. Load from
Google Fonts when rendering HTML.

## Narrative spine

Default **7 slides**. Flex 5–10 when the topic demands. If you flex, redistribute the jobs, and keep
**hook first** and **CTA last**.

| # | Job | Background | One job |
|---|-----|------------|---------|
| 1 | Hook | PAPER | Stop the scroll — SNAP hook + mark; almost no body |
| 2 | Tension | INK | Name the frustration the reader already feels |
| 3 | Answer | gradient | Core idea in one quotable box |
| 4 | Payoff | PAPER | What they actually get |
| 5 | Depth | INK | Proof, detail, or the difference (ledgered if numeric) |
| 6 | Method | PAPER | Numbered steps — feels doable |
| 7 | Ask | gradient | One clear CTA; no swipe cue; bar at 100% |

**Swipe rhythm:** alternate PAPER / INK. Close on gradient. Reshape the order only if
the topic forces it. Never break the light/dark pulse without saying why.

Slide 1 is the only slide most people see:
1. Write 3 SNAP hook variants.
2. Pick one.
3. Keep the others as A/B notes in the script footer.

## Canvas chrome (every slide)

Ratio **4:5**. Each slide stands alone (no shared bleed).

1. **Progress bar** — bottom, 3px, fully rounded. Width = `(index+1)/total`.
   CORE on PAPER slides, white on INK. Never omit it.
2. **Swipe cue** — right edge, ~48px fade + chevron. Put it on every slide **except**
   the last (its removal signals “end”).
3. **Safe padding** — content clear of bar and cue.

## Component kit

Use only these. Keep them visually identical across slides.

| Component | Use |
|-----------|-----|
| Struck-through pill | Old way being replaced |
| Label pill | Feature / category tags (`CORE_SOFT`) |
| Quote box | Sample input, short proof line (INK ground, italic) |
| Feature row | Icon + label + one line; hairline dividers |
| Numbered step | Oversized numeral + title + detail (method slide) |
| CTA button | Final slide only: pill, PAPER fill, `CORE_DEEP` text |

## Output contract

Emit **one** of these. If unclear, ask. Default = script + HTML preview:

### A — Slide script (always)

```markdown
## Carousel — <slug>
- Platform: Instagram 4:5 · slides: N · mood: <font mood> · core: <#hex>
- Hook chosen: <SNAP line> · Alt hooks: …

| # | Job | BG | On-slide copy | Visual notes |
|---|-----|----|---------------|--------------|
| 1 | Hook | PAPER | … | mark top-left |

### Caption
- First line (grid): …
- Body: …
- CTA: …
- Hashtags: ≤ 5 or none

### Claims
| Claim on slide | Ledger / author-supplied / cut |
|----------------|--------------------------------|
```

### B — HTML preview (when design-in-chat is useful)

One self-contained HTML file: swipeable viewport, optional Instagram-style
chrome for judgement only. **Layout base width = 420px** (viewport 420×525).
Do not widen the frame by hand — export scales instead.

Optional chrome: avatar + handle, dots, action row, caption line. Hide chrome
before PNG capture.

### C — Export (when tooling is available)

Target: **1080×1350 PNG per slide**, no crop.

| Setting | Value |
|---------|--------|
| Layout width | 420px (unchanged) |
| Scale | `1080 / 420 ≈ 2.5714` (`device_scale_factor`) |
| Clip | Exact viewport; chrome hidden |
| Fonts | Wait until web fonts loaded (~3s) or text falls back |
| Motion | Disable transitions during capture |

Prefer a small Python capture script (Playwright/Puppeteer) over fragile shell
pipelines. Embed local images as base64, so that the HTML stays portable.

**CAUTION:** If no browser runtime is available, ship the script + HTML, and state that the PNGs need a
local export step. Do not fake binary files.

## Edit protocol

Never regenerate the whole deck to change one line.

| Intent | User says (examples) |
|--------|----------------------|
| One slide | “Change slide 1 hook to …” / “Make slide 3 darker; add a quote” |
| Structure | “Swap 4 and 5” / “Add a slide between 2 and 3 about …” / “Drop 6” |
| Feel | “Warmer” / “All dark backgrounds” / “Serif headings” |
| Brand | “Core is now #E63946 — rebuild palette only” |
| Ship | “Export PNGs” / “Raw HTML” / “Rewrite caption” |

## Atomize bridge

When `atomize` maps an atom to carousel, run this engine with that atom as the
spine seed. Prefer `steps`, `definition` (myth vs fact), and `proof`
(comparison) atoms. One atom → one carousel. Do not cram a whole article into
seven slides.

## Non-negotiables

1. Export-ready copy on first output — no “lorem” / placeholders.
2. Light/dark alternation + progress bar always.
3. Palette from one hex. Two typefaces max.
4. Last slide: no arrow, full bar, one ask.
5. No invented stats or algorithm lore.
6. Fix named slides. Do not full-regen for a one-line change.
