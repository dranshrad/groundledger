---
name: editorial-pass
description: >-
  Groundledger SPARK multi-pass editor plus Tone Retarget, Locale Lock, Voice
  Specimens, Style Pattern Mine, and Voice Canon. Preserves author voice, never
  invents facts. Use when polishing drafts, retargeting tone, or building a
  style guide from samples.
license: MIT
compatibility: Claude Code, Cursor, Cowork (Agent Skills)
---

# Editorial Pass (SPARK Chain)

Groundledger multi-pass editor. The user chooses the locale. Never force one.

**Core laws:**
- Preserve the author's voice.
- Obey the Grounding Law (`../blog-engine/references/grounding.md`). Fact freeze means no new invented claims.

## Modes

| Mode | Job |
|------|-----|
| `spark` | Full or partial SPARK chain (default) |
| `tone` | **Tone Retarget** — new tone, same substance |
| `locale-lock` | **Locale Lock** — en-US / en-GB / custom glossary |
| `specimens` | **Voice Specimens** — annotated samples |
| `mine` | **Style Pattern Mine** — patterns from samples |
| `canon` | **Voice Canon** — synthesize `VOICE.md` |

## SPARK passes

| # | Pass | Does | Must not |
|---|------|------|----------|
| 1 | Sanitize | Typos, grammar, markdown, locale consistency | Rewrite voice |
| 2 | Pace | Rhythm, cuts throat-clearing | Add claims |
| 3 | Architecture | Headings, order, intent flags | Invent facts |
| 4 | Reference | Flag unsourced claims | Fabricate sources |
| 5 | Knife | Tighten; optional SEO on visible truth | Keyword stuffing |

You may skip, reorder or stop passes. For a full SPARK run, write the intermediates without pausing.

## Intermediates

Default `./editorial/<slug>/`:

```
00_original.md
01_sanitize.md … 05_knife.md
final.md
pass-log.md
```

**WARNING:** Never overwrite the source. Copy it to `00_original.md` first.

## Voice lock

1. Before pass 1, load [references/voice-lock.md](references/voice-lock.md).
2. Revert flattening edits.

## Tone Retarget (`tone`)

Inputs: draft + target tone (e.g. warmer, more formal, less hype).

Constraints:
- Add zero new claims.
- Preserve the meaning.
- Emit a diff summary of tone moves only.

## Locale Lock (`locale-lock`)

1. Apply the chosen locale + optional glossary.
2. If the user did not specify a locale, default to `keep-as-is`.
3. Never force en-GB.

## Voice Specimens → Mine → Canon

1. **specimens** — store annotated samples under `./voice/specimens/`
2. **mine** — extract recurring patterns (length, openers, humor, bans)
3. **canon** — write/update `VOICE.md` for suite-wide use

See [references/voice-canon.md](references/voice-canon.md).

## Fact freeze

Add no new stats/quotes/studies. Send publish-ready evidence work to `blog-engine` `verify`.

## Bridges

- After Knife → optional `blog-engine` `score` or `social-cast` `atomize`.
- YMYL → blog-engine intensifier (`ymyl`).
