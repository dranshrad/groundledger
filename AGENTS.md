# Agent conventions (Groundledger)

## Skill layout

Each skill is `skills/<name>/SKILL.md` with optional `references/`.

Frontmatter: `name`, `description`, `license` (MIT). Keep `name` = directory name.

## Grounding

All agents must follow `skills/blog-engine/references/grounding.md`.  
Paid media: observe-only unless MutationLatch is open (`skills/paid-cast/`).  
Site SEO recommendations must be PROBE-complete (`skills/site-signal/`).  
Full article pipelines run through `skills/signal-os/` (6 passes, max 2 review loops).

## Clients

| Client | Skills path |
|--------|-------------|
| Claude Code | `~/.claude/skills/` or plugin |
| Cursor | `~/.cursor/skills/` |
| Cowork | per-skill zip upload |

## Paths

Cross-skill references must be sibling-relative: `../blog-engine/references/grounding.md`.
Repo-root paths (`skills/blog-engine/...`) resolve here and break after install.

## Size

Prefer SKILL.md under ~500 lines; put depth in `references/`.

## Before committing

```bash
python3 scripts/validate.py     # structure, frontmatter, links, dual-layout paths
python3 evals/check.py --lint   # eval fixtures well-formed
```
