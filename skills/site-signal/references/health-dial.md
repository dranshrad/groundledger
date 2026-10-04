# Site Health Dial

Composite 0–100 score for Groundledger Site Signal audits. Every axis needs **evidence**. Missing evidence → reduce coverage, do not invent points.

## Default weights

| Axis | Points | What “good” looks like |
|------|-------:|------------------------|
| Technical / crawl / index | 20 | Indexable, sane robots/sitemap, no blocking render walls for critical content |
| Content / trust | 20 | Clear purpose, author/org signals, no hollow filler |
| On-page / intent fit | 15 | Title/H1/body match query job; internal links make sense |
| Schema | 10 | Matches visible truth only; no fantasy Product/FAQ markup |
| CWV honesty | 10 | Lab and field labeled separately; no fake “all green” without data |
| AI-answer readiness | 15 | Extractable passages, stable entities, cite-friendly structure |
| Media | 10 | Meaningful alts, reasonable weight, hero not a black hole |

Sum of awarded points = dial. Report **coverage** = (axes with real evidence) / 7.

**Always report the dial with its coverage.** A 78 at 3/7 coverage and a 78 at
7/7 coverage are not the same finding, and the number alone hides which one it
is. Never present a dial score without coverage attached, and never compare two
sites' dials measured at different coverage.

## Industry remaps (after user confirm)

| Industry | Bias |
|----------|------|
| `local` | Boost NAP/local schema; de-emphasize programmatic scale |
| `ecommerce` | Boost PDP uniqueness, faceted index control, product schema honesty |
| `saas` | Boost intent fit + cite-AI; technical still high |
| `publisher` | Boost content freshness + author; schema Article honesty |
| `other` | Keep defaults |

## Bands

| Score | Label | Action bias |
|------:|-------|-------------|
| 85–100 | Strong | Maintain + selective bets |
| 70–84 | Workable | Fix top PROBE `now` items |
| 50–69 | Weak | Unblock technical + intent before content volume |
| 0–49 | Rebuild | Dependency graph first; pause vanity publishing |

## Scoring rules

1. Cap any axis at its max weight. No bonus stacking.
2. Partial evidence → half credit max on that axis. Note the gap.
3. Contradictions (e.g. schema says InStock, page says sold out) → zero that schema slice + PROBE critical.
4. Never average competitor scores you did not measure.
