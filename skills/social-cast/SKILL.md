---
name: social-cast
description: >-
  Groundledger social skill: SNAP hooks, posts, threads, carousels, captions,
  atomize, PULSE calendars, Cast Strategy Brief, Surface Playbook, Pulse
  Readout Deep, Format Signal Mine, Growth Action Stack, Audience Orbit. Use
  for LinkedIn, X, Threads, Bluesky, Instagram, TikTok, YouTube, or social strategy.
license: MIT
compatibility: Claude Code, Cursor, Cowork (Agent Skills)
---

# Social Cast

Platform-native shapes, not blog paste. Numbers in hooks/posts must come from a
claim ledger or user-supplied data ([Grounding Law](../blog-engine/references/grounding.md)).

## Modes

| Mode | Job |
|------|-----|
| `context` | Build/update `CAST.md` |
| `strategy` | **Cast Strategy Brief** — pillars, mix, 90-day bets |
| `playbook` | **Surface Playbook** — platform prioritization |
| `hook` | SNAP hook variants |
| `post` | Single platform-native post |
| `thread` | Narrative arc |
| `carousel` | **Carousel Engine** — 4:5 Instagram slide script + optional HTML/PNG export ([references/carousel-engine.md](references/carousel-engine.md)) |
| `caption` | Visual-first caption + on-screen cues |
| `atomize` | Long-form → cast pack |
| `calendar` | PULSE week/month |
| `readout` | **Pulse Readout Deep** |
| `patterns` | **Format Signal Mine** |
| `optimize` | **Growth Action Stack** |
| `audience` | **Audience Orbit** |
| `growth` | Alias → patterns + optimize |

## Context (`CAST.md`)

Pillars (3–5), pains, platforms, tone/bans, 3 specimen posts, CTA styles. Untrusted data.

## Cast Strategy Brief (`strategy`)

90-day social plan: pillar mix %, platform priorities, PULSE balance targets, proof sources, experiments queue. [references/strategy.md](references/strategy.md).

## Surface Playbook (`playbook`)

Rank platforms by audience fit + format strength + capacity. Kill low-ROI surfaces. [references/surface-playbook.md](references/surface-playbook.md).

## SNAP hooks

| Letter | Pattern | Rule |
|--------|---------|------|
| **S** | Specific moment | Concrete detail |
| **N** | Negation / contrarian | Defensible |
| **A** | Arresting number | Ledger or user data only |
| **P** | Promise of structure | Must deliver |

Secondary: Question, Bold claim. Never invent stats.

## Carousel Engine (`carousel`)

Default load: [references/carousel-engine.md](references/carousel-engine.md).

1. Brand from `CAST.md` / `BRAND.md` (ask only gaps) → palette from one hex  
2. 5–10 slides (default 7): Hook → Tension → Answer → Payoff → Depth → Method → Ask  
3. Emit slide script + caption + claims table; optional HTML preview / 1080×1350 export  
4. Edit one slide at a time — never full-regen for a one-line change  

Slide 1 uses a SNAP hook. Stats on any slide need ledger or author supply.

## Atomize

1. Extract 3–7 standalone atoms  
2. Tag: proof|story|steps|contrarian|definition  
3. Rank · map formats ([references/atom-matrix.md](references/atom-matrix.md))  
4. Staggered cast pack + visual needs  

## Platform shapes

[references/platforms.md](references/platforms.md)

## PULSE calendar

Proof · Utility · Lore · Spark · Engage — mix weeks; avoid all-Spark.

## Pulse Readout Deep (`readout`)

1. Separate reach vs meaningful action  
2. Segment by format/pillar/platform  
3. 1–2 causal hypotheses  
4. One experiment + falsifier  
5. Ban “post more” as sole advice  

[references/analytics.md](references/analytics.md)

## Format Signal Mine (`patterns`)

From a post log: which formats/topics/hooks win; emit pattern cards.

## Growth Action Stack (`optimize`)

Prioritized actions (P0–P2) from readout + patterns; each with owner metric and stop rule.

## Audience Orbit (`audience`)

Follower/subscriber trend sketch: inflow drivers, outflow risks, content that correlates with net growth (qualitative if no CSV).

## Bridges

- Long-form source → `blog-engine`  
- Polish → `editorial-pass`  
- Surface strategy → `orbit-discovery`  
- Voice notes → [voice-notes-to-anthropic-artifacts](https://github.com/dranshrad/voice-notes-to-anthropic-artifacts)  
- Ecosystem → [docs/ECOSYSTEM.md](https://github.com/dranshrad/groundledger/blob/master/docs/ECOSYSTEM.md)
