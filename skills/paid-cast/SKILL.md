---
name: paid-cast
description: >-
  Groundledger paid-media skill with SAFE defaults (Snapshot → Advise → Fence →
  Experiment). Observe-only unless MutationLatch opens. Modes: audit, plan,
  math, brand, budget, trial, attrib, landing, creative, pace, optimize-draft.
  Use for Google/Meta/LinkedIn/Microsoft-style account reviews, unit economics,
  brand safety lattices, experiment decks, and draft change packs — not live
  spend edits without explicit approval. Claude Code, Cursor, Cowork.
license: MIT
compatibility: Claude Code, Cursor, Cowork (Agent Skills)
---

# Paid Cast (SAFE media)

Groundledger paid acquisition desk. It complements `orbit-discovery` (organic surfaces),
`site-signal` (landing SEO), and `social-cast` (organic social).

**WARNING:** **Default: observe-only.** Make no platform mutations, no budget edits and no status flips
unless the **MutationLatch** is open. A live change spends real money.

**Grounding:** `../blog-engine/references/grounding.md`. Use no invented ROAS,
CPAs, or “industry benchmarks” without a cited source that the user accepts.

## SAFE loop

| Step | Name | Rule |
|------|------|------|
| **S** | Snapshot | Read exports / UI dumps; claim + evidence + confidence |
| **A** | Advise | Ranked actions with unit-econ impact hypotheses |
| **F** | Fence | Ceilings: budget delta, geo, audience, creative, date |
| **E** | Experiment | Prefer trials over permanent flips |

## MutationLatch (writes)

The latch stays **closed** until all of these are true:

1. The user explicitly asks to draft or apply a change pack.
2. The scope is listed (accounts / campaigns / ad sets).
3. Ceilings are set (max daily $, max % budget move, kill date). Ceilings must be numeric, or explicitly `unlimited` with the user typing that word.
4. An idempotency key or rollback cue is recorded.
5. The user says **approve** on the exact draft.

Without the latch:
- Deliver the audit + draft-only recommendations. Mark each draft change pack `DRAFT — NOT APPLIED`.
- Never pretend that a change was applied in-platform.

## Claim / evidence / confidence

Write every material finding in this form:

```
Claim: …
Evidence: … (export row, screenshot note, UI path)
Confidence: high | medium | low
```

If confidence is low, ask or mark the finding unknown. Do not bluff attribution.

## Modes

| Mode | Job |
|------|-----|
| `audit` | Account / campaign health Snapshot |
| `plan` | Channel mix + phased media plan |
| `math` | Unit economics (CAC, payback, contribution) |
| `brand` | Brand Lattice (claims, exclusions, tone) |
| `budget` | Budget Lattice (caps, pacing, reserves) |
| `trial` | Experiment deck (hypotheses, metrics, stop rules) |
| `attrib` | Attribution comparability gate |
| `landing` | Post-click landing audit (pairs with `site-signal`) |
| `creative` | Fatigue / variant gaps |
| `pace` | Delivery / spend pace vs plan |
| `optimize-draft` | Change pack under MutationLatch |

Platform packs (Google / Meta / LinkedIn / Microsoft-style) are **draft mutation
templates** only. Never auto-execute them. See [references/mutation-latch.md](references/mutation-latch.md).

## Unit economics (`math`)

1. Require inputs that the user can supply: AOV/LTV proxy, margin, target CAC or payback.
2. If inputs are missing, compute scenarios labeled `assumption`, not facts.

See [references/unit-economics.md](references/unit-economics.md).

## Brand Lattice (`brand`)

Allowed claims · banned claims · competitor rules · sensitive topics · offer
language.

Creative and landing copy must pass the lattice before scale.

## Budget Lattice (`budget`)

Daily/monthly caps · channel reserves · test budget slice · emergency kill.

Pace mode watches spend vs plan. It does not change bids.

## Trial Deck (`trial`)

Hypothesis · primary metric · guardrails · sample / time stop · rollback.

Use one primary metric per trial. No “test everything.”

## Attribution gate (`attrib`)

Before you compare channels, require: same window, same conversion def, same currency,
same inclusion rules.

If the channels are incomparable, say so. Do not crown a winner.

## Landing (`landing`)

Check: message match, offer clarity, speed honesty, form friction, proof proximity.

- Deep SEO issues → hand off to `site-signal`.
- Copy rewrites → `blog-engine` / `editorial-pass`.

## Creative (`creative`)

- Take fatigue signals from user data only.
- Variant matrix: angle × format × offer.
- Respect the Brand Lattice.

## Context files

`BRAND.md` · `ORBIT.md` · optional `MEDIA_LATCH.md` (ceilings + approvals).

## Bridges

- Landing SEO → `site-signal`
- Organic social → `social-cast`
- Long-form proof pages → `blog-engine`
- Surface strategy → `orbit-discovery`
