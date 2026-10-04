---
name: studio-desk
description: >-
  Groundledger workspace ops: Workspace Boot, studios (Longform, Blog Desk, Op-Ed
  Shelf, Doc Templates), Draft Lineage, Version Vault, Cast Desk Status, Export
  Pack, Ship Gate, Collection Index. Use when scaffolding a writing workspace,
  versioning drafts, exporting, or preparing CMS handoff.
license: MIT
compatibility: Claude Code, Cursor, Cowork (Agent Skills)
---

# Studio Desk

Groundledger workspace and publishing-ops skill.

**Grounding:** the [Grounding Law](../blog-engine/references/grounding.md) is binding at `ship`.

**CAUTION:** Do not pass the Ship Gate in either of these cases:
- any claim-ledger row is `blocked`;
- a paid change pack claims writes that no approved MutationLatch authorised.

## Modes

| Mode | Job |
|------|-----|
| `boot` | **Workspace Boot** + studio variant |
| `lineage` | **Draft Lineage** — next version with targeted edits |
| `vault` | **Version Vault** — archive old versions |
| `status` | **Cast Desk Status** — drafts / versions / shipped |
| `export` | **Export Pack** — md bundle / HTML / plain text notes |
| `ship` | **Ship Gate** — CMS/handoff checklist |
| `index` | **Collection Index** — TOC for a posts folder |

## Workspace Boot (`boot`)

Ask for: studio variant + name + local path.

### Studios

| Studio | Layout |
|--------|--------|
| **Longform** | `drafts/` `research/` `notes/` `images/` `archive/` |
| **Blog Desk** | `drafting/` `published/` `briefs/` `archive/` |
| **Op-Ed Shelf** | `posts/<topic>/` `drafts/` `archive/` |
| **Doc Templates** | `templates/` `exports/` `archive/` |

Then:
1. Write a short `STUDIO.md` that describes the conventions.
2. Do not create secrets.
3. Optional: remind the user that they can `git init`.

**WARNING:** Do not force public GitHub creation.

Folder rules: [references/studio-layout.md](references/studio-layout.md).

## Draft Lineage (`lineage`)

1. Copy the current draft to `vN+1` (or a dated stamp).
2. Require a **diff contract** (KEEP/CHANGE/DELETE).
3. Never overwrite `vN` in place.

## Version Vault (`vault`)

Move superseded versions into `archive/YYYY-MM/`, with a one-line reason log.

## Cast Desk Status (`status`)

Scan the workspace. Summarize:
- active drafts
- latest versions
- published count
- stale (>N days) items

N is the user's threshold. If the user gave no N, report each draft's age in days and do not label any item stale.

## Export Pack (`export`)

From a draft path, produce:

- Combined markdown (front matter + body)
- Optional HTML sketch (semantic article wrapper)
- Plain-text stripped copy
- Manifest listing files

Do not claim pixel-perfect PDF. Note that the user may print the HTML to PDF.

## Ship Gate (`ship`)

Handoff checklist:
- final path
- CLEAR/Ship Scan status, if blog
- cast pack, if social
- CMS fields
- URL slug
- OG image
- owner

Pair it with the blog-engine **Release Latch**.

## Collection Index (`index`)

Generate `INDEX.md` for a posts directory. List titles, dates, jobs and paths.

## Bridges

- Writing → `blog-engine` / `editorial-pass`
- Social → `social-cast`
- Strategy → `orbit-discovery`
