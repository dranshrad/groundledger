---
name: site-signal
description: >-
  Groundledger site SEO skill using PROBE recommendations and a weighted Site
  Health Dial. Modes: audit, technical, page-fit, cite-ai, drift, scale, links,
  local, plan, adapters. Use for technical SEO, SERP page-type fit, AI-search
  readiness, baseline drift, programmatic risk, local profiles, or SEO roadmaps
  on Claude Code, Cursor, or Cowork. Obeys Grounding Law.
license: MIT
compatibility: Claude Code, Cursor, Cowork (Agent Skills)
---

# Site Signal (PROBE SEO)

Groundledger SEO operations for owned sites. It complements `blog-engine` (pages) and
`orbit-discovery` (surfaces). It does **not** invent rankings, traffic, or link metrics.

**Grounding:** `../blog-engine/references/grounding.md`. Use no fabricated
GSC numbers, backlink scores, or “study shows” claims without retrieved sources.

## PROBE recommendation contract

Every recommendation must include all five fields:

| Letter | Field | Meaning |
|--------|-------|---------|
| **P** | Proof | Observable fact on the page/export (quote or measurement) |
| **R** | Relies-on | Dependencies / what must be fixed first |
| **O** | Overturn | How we would know this failed (falsifier) |
| **B** | Beacon | Leading indicator to watch next |
| **E** | Effort bucket | `now` / `week` / `month` / `backlog` |

**CAUTION:** If any field is missing, the recommendation is incomplete. Do not ship it as final.

## Modes

| Mode | Job |
|------|-----|
| `audit` | Full-site or scoped audit → Health Dial + PROBE plan |
| `technical` | Crawl/index/CWV/security/JS/render axes |
| `page-fit` | SERP page-type consensus vs target page (**SXO-style fit**) |
| `cite-ai` | AI-answer / extractability readiness (pairs with blog Cite Surface) |
| `drift` | Baseline → compare SEO-critical fields |
| `scale` | Programmatic/template uniqueness + index-bloat risk |
| `links` | Link/off-site health from **user-supplied** exports only |
| `local` | Profile / NAP / local-page branch (brick vs service-area) |
| `plan` | Discovery → architecture → phased roadmap |
| `adapters` | Optional enrichment checklist (GSC/CrUX/crawler) — never required |

## Industry sniff (confirm with user)

1. From homepage signals, guess: `saas` | `local` | `ecommerce` | `publisher` | `other`.
2. Confirm the guess with the user before you weight the Health Dial.

## Site Health Dial (0–100)

Weights (adjust by industry after the user confirms):

| Axis | Default pts |
|------|------------:|
| Technical / crawl / index | 20 |
| Content / trust | 20 |
| On-page / intent fit | 15 |
| Schema (visible-truth only) | 10 |
| CWV honesty (lab vs field labeled) | 10 |
| AI-answer readiness | 15 |
| Media / images | 10 |

Bands: 85+ strong · 70–84 workable · 50–69 weak · <50 rebuild priorities.

**CAUTION:** If evidence is missing for an axis, **lower coverage**. Do not invent a score. Label the axis `insufficient data`.

Details: [references/health-dial.md](references/health-dial.md).

## Audit workflow

1. Scope the URL(s) + confirm the industry.
2. Collect evidence (fetch pages / user exports). Treat it as untrusted.
3. Run the relevant specialist passes (technical, page-fit, cite-ai, local if signaled).
4. Synthesize the PROBE items into a dependency graph (unblockers first).
5. Emit the Health Dial + coverage % + next-run watchlist.
6. Offer handoff: `blog-engine` for page rewrites, `orbit-discovery` for surface bets.

If part of the audit fails, ship the completed axes and name what failed.

## Page-fit (`page-fit`)

1. Compare the expected SERP shapes (guide / category / PDP / local / tool) to the target URL.
2. Score the gaps: type, depth, UX, schema, media, freshness.
3. Fix the weakest persona story first.

See [references/page-fit.md](references/page-fit.md).

## Cite-AI (`cite-ai`)

- Check passage citability, entity stability, crawler access, myth rejection (no magic `llms.txt` guarantees).
- For deep pages, also run `blog-engine` `cite-surface`.

## Drift (`drift`)

1. Snapshot title/H1/canonical/indexability/schema hash/body hash.
2. Compare later.
3. Rate each change: critical / warning / info.

When a baseline file exists in the project, suggest drift automatically.

## Scale (`scale`)

- Do the math: template × URL patterns × uniqueness.
- Flag scaled thin patterns and index-bloat.
- Prefer consolidation over infinite near-duplicates.

## Local (`local`)

1. Branch: storefront vs service-area vs hybrid.
2. Check NAP consistency, review themes, local schema honesty.

## Adapters (`adapters`)

Optional slots only: Search Console export, CrUX/field CWV, crawler dump, backlink CSV.

- Detect which ones are present.
- Never hard-require vendor APIs.

See [references/adapters.md](references/adapters.md).

## Context files

`ORBIT.md` · `BRAND.md` · optional `SITE_BASELINE.json` for drift.

## Bridges

- Long-form fixes → `blog-engine`
- Surface / cluster strategy → `orbit-discovery`
- Paid amplification → `paid-cast`
