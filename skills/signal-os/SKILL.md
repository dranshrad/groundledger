---
name: signal-os
description: >-
  Signal Over Noise OS: lean editorial conductor for world-class software, AI,
  and prompt-engineering writing. Runs a 6-pass pipeline (Discover, Brief,
  Draft, Review, Polish, Ship) by routing to Groundledger skills, adding
  technical review and adversarial critique. Use for a full article pipeline,
  flagship technical article, tech/code review of a draft, devil's advocate
  critique, or a post-publish retrospective.
license: MIT
compatibility: Claude Code, Cursor, Cowork (Agent Skills)
---

# Signal Over Noise OS (Conductor)

A boutique editorial studio in one skill. It is not a chatbot. It is a pipeline.

The goal: writing that an experienced engineer would recognise by its clarity,
originality, and human voice, even with the byline removed.

**Shared laws (never restate, always obey):**
`../blog-engine/references/grounding.md` (no invented facts) ·
`VOICE.md` / `BRAND.md` (voice and brand, enforced by editorial-pass voice lock).

## Pipeline

```
Discover → Brief → Draft → Review → Polish → Ship
                     ▲         │
                     └─ fail (max 2 loops)
```

| # | Pass | Routes to | Compact output |
|---|------|-----------|----------------|
| 1 | `discover` | `orbit-discovery` `field` + `spray` + `triage` | ≤ 10 scored ideas, one-line timing rationale each |
| 2 | `brief` | `orbit-discovery` `shelf` + `blog-engine` `brief` / `spine` | Evidence table, angle, spine, story arc, one originality bet |
| 3 | `draft` | `blog-engine` `draft` | Article + claim ledger + Q-tests + CLEAR scorecard |
| 4 | `review` | [references/tech-review.md](references/tech-review.md) + [references/critique.md](references/critique.md) + `blog-engine` `verify` | Single findings table (severity-tagged) |
| 5 | `polish` | `editorial-pass` `spark` | Humanised final draft, voice locked |
| 6 | `ship` | `blog-engine` `ship-scan` + `frame` · `social-cast` `atomize` · `studio-desk` `ship` | Article + default pack + retro |

When to run:
- Run any single pass on request.
- Run the full pipeline only when the user asks for it ("full pipeline", "flagship article", "new article end to end").
- Never trigger the pipeline for small pieces (a post, a fix, a rewrite).

## Quality gate (pass 4 → 5)

Pass all three:
- Claim ledger clean (no `blocked` material rows)
- CLEAR ≥ 85 · Q-tests 5/5
- No unresolved `blocker` findings from review

If the gate fails, return to Draft with a diff contract.

**CAUTION:** **Hard cap: 2 loops.** After 2 loops, either ship with the residual risks listed, or stop and ask the user.

Use no second scoring system. CLEAR + stress tests are the only gate.

## Originality bet (pass 2, mandatory)

Every article commits to exactly one bet, named in the brief:
- new framework
- new analogy
- new visual explanation
- better workflow
- fresh perspective

Pass 4 checks that the bet was delivered ([references/critique.md](references/critique.md)).

## Default publishing pack (pass 6)

- Default: Article + **X thread + LinkedIn post + newsletter edition** via `social-cast` `atomize`.
- All other derivatives (Medium, Substack, Dev.to, Reddit, HN, YouTube script, podcast outline, carousel, FAQ, glossary…): make them only on explicit per-platform request, via `social-cast` or `blog-engine` `adapt`.

## Token economy rules

1. Use one context per pass. Specialists are checklist lines, never separate agents.
2. Output tables and ledgers, not narrative reports.
3. Load a reference file only in the pass that uses it.
4. Never restate grounding, voice, or brand rules. Link them.
5. Prefer omitting a number over fabricating one.
6. Give no predicted virality or engagement scores. Post-publish analysis goes to `social-cast` `readout`.

## Retrospective (`retro`)

After publishing, append ≤ 12 lines to a running `RETRO.md`:

```
## <slug> — <date>
- Worked:
- Weakest section:
- Too complex:
- Most original insight:
- Open questions:
- Follow-up articles:
```

Before the next `brief` pass, read the last 2 entries. Nothing else carries over.

## Bridges

- Strategy / surfaces → `orbit-discovery` · Long-form craft → `blog-engine`
- Voice polish → `editorial-pass` · Social → `social-cast` · Ops → `studio-desk`
- Suite router → `../groundledger/SKILL.md`
