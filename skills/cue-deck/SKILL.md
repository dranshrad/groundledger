---
name: cue-deck
description: >-
  Groundledger Cue Deck: original prompt cards keyed to ORBIT stages and CLEAR
  modes (When, Inputs, Prompt, Output, Risks). Use when the user wants a
  reusable prompt, strategy cue, or agent instruction for content work.
license: MIT
compatibility: Claude Code, Cursor, Cowork (Agent Skills)
---

# Cue Deck

Groundledger prompt cards.

Every card that asks for facts inherits the
[Grounding Law](../blog-engine/references/grounding.md). A drawn card never
licenses an unledgered number.

## Modes

| Mode | Job |
|------|-----|
| `list` | Show card index |
| `draw` | Emit one card by id or stage |
| `custom` | Build a new card from a user goal |

## Card schema

Every card uses this schema:

```markdown
## Cue — [id]
**When:** …
**Inputs:** …
**Prompt:**
> …
**Output:** …
**Risks:** …
**Next skill:** blog-engine | orbit-discovery | site-signal | paid-cast | social-cast | editorial-pass | studio-desk
```

## Index

Load the full text from [references/cards.md](references/cards.md):

| ID | Stage / mode |
|----|----------------|
| `O-jobs` | Observe — JTBD spray |
| `R-echo` | Reinforce — Echo Map |
| `B-brief` | Build — asset brief |
| `I-kpi` | Instrument — measurement |
| `T-retro` | Transmit — learnings |
| `C-draft` | CLEAR draft kickoff |
| `C-verify` | Claim Probe+ |
| `C-cite` | Cite Surface |
| `S-atom` | Social atomize |
| `S-readout` | Pulse readout |
| `E-spark` | SPARK kickoff |
| `D-ship` | Ship Gate |
| `P-audit` | PROBE site audit |
| `P-fit` | Page-fit check |
| `A-snap` | Paid Snapshot (observe-only) |
| `A-latch` | MutationLatch checklist |

When you draw a card:
1. Copy the prompt block verbatim into the agent turn.
2. Execute it via the **Next skill**.
