---
name: blog-engine
description: >-
  Groundledger long-form skill: CLEAR rubric, claim ledgers, adversarial Q-tests,
  grounding law (no fabricated stats), YMYL, Ship Scan, Cite Surface Audit,
  Freshness Drift, Graph Runner, Locale Lattice, Release Latch. Use for blog
  drafts, rewrites, SEO audits, citation checks, clusters, multilingual plans,
  or publish readiness on Claude Code, Cursor, or Cowork.
license: MIT
compatibility: Claude Code, Cursor, Cowork (Agent Skills)
---

# Blog Engine (CLEAR Editorial System)

Groundledger long-form skill for grounded, publish-ready articles.

**Ship rule:** ship only when all of these are true:
- CLEAR ≥ 85
- claim ledger clean
- Q-tests pass
- residual risk accepted
- Grounding Law satisfied
- (when requested) Ship Scan + Release Latch green

**Grounding Law:** [references/grounding.md](references/grounding.md). It is binding.

## Modes

| Mode | Goal |
|------|------|
| `draft` | New article from JTBD + Spine Picker |
| `improve` | Rewrite under a diff contract |
| `score` | CLEAR + ledger + residual risks |
| `brief` | Competitive teardown + evidence plan |
| `horizon` | **Horizon Brief** — 90-day intent + surface bets |
| `spine` | **Spine Picker** — form from JTBD + competitive gaps |
| `map` | Reader-journey outline |
| `verify` | Claim audit (**Claim Probe+**) |
| `cite-probe` | 5 AI-style extractability questions |
| `cite-surface` | **Cite Surface Audit** — full citation readiness |
| `ship-scan` | **Ship Scan** — SEO + extractability checklist |
| `collision` | **Job Collision Map** — overlapping URL jobs |
| `cluster` | Intent-pure graph |
| `graph-run` | **Graph Runner** — plan → spoke briefs → ship order |
| `freshness` | **Freshness Drift** — refresh/consolidate/prune |
| `mirror` | **Mirror Markup** — schema from visible truth |
| `locale` | **Locale Lattice** — translate/localize/hreflang plan |
| `frame` | **Frame & Tone Kit** — visual/chart/TTS briefs |
| `signal-bridge` | **Signal Bridge** — CWV/GSC/GA adapter checklist |
| `release` | **Release Latch** — packaging before handoff |
| `adapt` | Channel packs (prefer `social-cast` `atomize` for depth) |
| `ymyl` | YMYL intensifier |
| `calendar` | Cadence + update triggers |

For a bare topic, default to `draft` after one JTBD question.

## CLEAR rubric (100)

See [references/clear-rubric.md](references/clear-rubric.md): Claim 25 · Lexical 15 · Entity 15 · Answer 25 · Reader-job 20. Ship at ≥ 85.

## Core draft artifacts

Every `draft` / `improve` emits: article, claim ledger, adversarial Q-test,
residual risks, CLEAR scorecard. Templates: [references/artifacts.md](references/artifacts.md).

## Draft pipeline (summary)

1. Lock the JTBD.
2. Check intent purity.
3. Write the evidence plan.
4. Run the Spine Picker + journey map.
5. Write extractable answers.
6. Run the stress tests.
7. Deliver or block.

Full craft: [references/craft.md](references/craft.md) · forms: [references/forms.md](references/forms.md) · evidence: [references/evidence.md](references/evidence.md).

### Stress tests (blocking)

| # | Test | Pass |
|---|------|------|
| 1 | Claim ledger | No `blocked` material rows |
| 2 | Contradiction hunt | No internal conflicts |
| 3 | Q-test | 5/5 extractable |
| 4 | CLEAR | ≥ 85 |
| 5 | YMYL | Intensifier green if triggered |
| 6 | Accessibility | Alt, links, heading order |

## Extended modes (quick contracts)

### Horizon Brief (`horizon`)

1. Write a 90-day plan: ICP jobs, surface bets, hub/spoke candidates, evidence gaps, KPI per asset.
2. Hand production to `draft` / `graph-run`.

### Spine Picker (`spine`)

1. Pick a form from [references/forms.md](references/forms.md) using the JTBD + competitor spine gaps.
2. Output: chosen form + rejected forms + why.

### Ship Scan (`ship-scan`)

Owned SEO + extractability checklist (titles, meta, headings, links, OG, schema mirror, extractable opens). See [references/ship-scan.md](references/ship-scan.md). It is separate from CLEAR.

### Job Collision Map (`collision`)

1. Given a corpus (paths or titles+jobs), flag overlapping JTBDs.
2. Recommend merge, differentiate, or prune.

### Cite Surface Audit (`cite-surface`)

Full citation readiness beyond `cite-probe`: entity stability, passage inventory, crawler access notes, structure for extraction. See [references/cite-surface.md](references/cite-surface.md).

### Claim Probe+ (`verify`)

For each claim, report:
- support status
- confidence (`high`/`med`/`low`)
- echo risk (the same claim repeated without new evidence)
- fix action

### Freshness Drift (`freshness`)

1. From traffic/export deltas or stale dates, classify each page: refresh / consolidate / prune.
2. Attach update triggers.

See [references/freshness.md](references/freshness.md).

### Graph Runner (`graph-run`)

1. Turn the cluster plan into ordered spoke briefs.
2. Set the ship sequence with dependencies.
3. Reject duplicate jobs.

### Mirror Markup (`mirror`)

Emit JSON-LD only where it mirrors visible content (`BlogPosting`/`Article`, `Person`/`Organization`, `BreadcrumbList`). Play no invisible FAQ games.

### Locale Lattice (`locale`)

Plan the locales, adaptation depth (translate vs cultural), hreflang pairs, and parity checklist. See [references/locale-lattice.md](references/locale-lattice.md).

### Frame & Tone Kit (`frame`)

Tool-agnostic briefs: hero brief, chart-from-ledger, optional TTS narration brief. See [references/frame-tone.md](references/frame-tone.md).

### Signal Bridge (`signal-bridge`)

Checklist for plugging in CWV, Search Console, analytics, keyword exports. No vendor lock-in. See [references/signal-bridge.md](references/signal-bridge.md).

### Release Latch (`release`)

Before handoff, check: required artifacts present, links resolve policy, hero/social image notes, review.md summary. See [references/release-latch.md](references/release-latch.md).

## YMYL

See [references/ymyl.md](references/ymyl.md).

## Works with (sister tools)

- Voice drafts: [voice-notes-to-anthropic-artifacts](https://github.com/dranshrad/voice-notes-to-anthropic-artifacts)
- Self-heal loops (code parallel): [automated-self-correction-loop](https://github.com/dranshrad/automated-self-correction-loop)
- Suite hub: [docs/ECOSYSTEM.md](https://github.com/dranshrad/groundledger/blob/master/docs/ECOSYSTEM.md)

## Progressive disclosure

| File | When |
|------|------|
| [grounding.md](references/grounding.md) | Anti-hallucination (always) |
| [clear-rubric.md](references/clear-rubric.md) | Scoring |
| [artifacts.md](references/artifacts.md) | Ledgers / Q-tests |
| [evidence.md](references/evidence.md) | Sourcing |
| [craft.md](references/craft.md) | Prose / a11y |
| [forms.md](references/forms.md) | Spines |
| [ship-scan.md](references/ship-scan.md) | SEO checklist |
| [cite-surface.md](references/cite-surface.md) | Citation audit |
| [freshness.md](references/freshness.md) | Decay |
| [locale-lattice.md](references/locale-lattice.md) | i18n |
| [frame-tone.md](references/frame-tone.md) | Media briefs |
| [signal-bridge.md](references/signal-bridge.md) | Analytics adapters |
| [release-latch.md](references/release-latch.md) | Packaging |
| [ymyl.md](references/ymyl.md) | High-stakes |
