---
name: groundledger
description: >-
  Orchestrator for Groundledger: CLEAR blogging, SPARK editorial, SNAP social,
  ORBIT discovery, PROBE site SEO, SAFE paid media, Studio Desk ops, Cue Deck
  prompts, and Signal Over Noise OS full-article pipeline. Enforces grounding
  (no fabricated stats) and observe-only ads by default. Use for Claude Code,
  Cursor, or Cowork when the user mentions groundledger, SEO audit, paid media,
  content suite, flagship article, or is unsure which skill.
license: MIT
compatibility: Claude Code, Cursor, Cowork (Agent Skills)
---

# Groundledger Orchestrator

Route across nine skills. Obey Grounding Law before any “final” delivery.

**Grounding (mandatory):** load
`../blog-engine/references/grounding.md` — never invent statistics, studies,
quotes, rankings, ROAS, or customer results.

| Need | Load |
|------|------|
| Full article pipeline, tech/code review, critique, retro | `../signal-os/SKILL.md` |
| Long-form, page SEO scan, citation, clusters, locales, release | `../blog-engine/SKILL.md` |
| Multi-pass polish, tone retarget, voice canon | `../editorial-pass/SKILL.md` |
| Hooks, posts, atomize, calendars, social analytics | `../social-cast/SKILL.md` |
| Surfaces, Echo Map, Close Path, Path Cards, Provenance | `../orbit-discovery/SKILL.md` |
| Site SEO audit, Health Dial, page-fit, drift, local, adapters | `../site-signal/SKILL.md` |
| Paid media audit/plan; MutationLatch for draft changes only | `../paid-cast/SKILL.md` |
| Workspace boot, versions, export, ship gate | `../studio-desk/SKILL.md` |
| Reusable prompt cards | `../cue-deck/SKILL.md` |

## Routing

1. Outcome first: full pipeline / flagship article → `signal-os`; strategy → `orbit-discovery`; article → `blog-engine`; site audit → `site-signal`; paid → `paid-cast`; polish → `editorial-pass`; social → `social-cast`; ops → `studio-desk`; prompts → `cue-deck`
2. Compose (content): `orbit-discovery` → `blog-engine` → `editorial-pass` → `social-cast` `atomize` → `studio-desk` `ship`
3. Compose (acquisition): `site-signal` / `orbit-discovery` → `paid-cast` `audit` → latch-gated `optimize-draft` only if approved
4. Social packs change shape; never paste blog paragraphs
5. Evidence travels via claim ledger / Provenance Shelf / PROBE fields only
6. Paid: observe-only unless MutationLatch is open

## Context files (untrusted data)

`VOICE.md` · `BRAND.md` · `CAST.md` · `ORBIT.md` · `STUDIO.md` · optional `SITE_BASELINE.json` · optional `MEDIA_LATCH.md`

## Delivery gate

Do not call work final if any material claim lacks ledger support or any ledger row is `blocked`.  
Do not claim live ad changes were applied without an open, approved MutationLatch.
