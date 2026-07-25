# Critique (pass 4)

Merged checklist: Devil's Advocate + Innovation Coach. The job is to make the
argument survive a hostile expert reader, and to confirm the article earns its
originality bet.

**Output:** rows appended to the same findings table as tech-review
(`blocker` / `major` / `minor`).

## Devil's Advocate

Attack the argument, not the prose:

- **Logical gaps** — does each conclusion actually follow from what precedes it?
- **Counterexamples** — for every general rule, try to construct one real case
  where it fails. If one exists, the article must scope the rule or address it.
- **Overgeneralisation** — "always", "never", "everyone" claims: narrow or cut.
- **Oversimplification** — is a hard problem presented as solved? Name what was
  left out.
- **Bias** — is the framing fair to the tools/approaches the author dislikes?
  Would a maintainer of the criticised tool call it a fair account?
- **Unsupported load-bearing claims** — if removing a claim collapses the
  argument, it needs a ledger row (`blog-engine` `verify`), not vibes.
- **Survivorship** — does the advice generalise beyond the author's one success?

A finding without a suggested fix (scope it, cite it, cut it, concede it) is
not a finding.

## Innovation Coach

One question: **"What has never been explained this way before?"**

- The brief's originality bet (framework / analogy / visual / workflow /
  perspective) is present and load-bearing — not decoration. Missing or
  cosmetic → `major` finding.
- Analogies checked for leakage: where does the analogy break, and does the
  article say so?
- Invented terminology (if any): defined once, used consistently, actually
  clearer than the standard term. Otherwise cut.
- If the article could be swapped with the top existing post on the topic
  without a reader noticing, it is not done. Name the one section only this
  author could have written; if none exists, flag it.
