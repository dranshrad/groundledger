# Tech Review (pass 4)

Merged checklist: Systems Architect + Software Engineering Reviewer + Prompt
Engineering Specialist. Run in one context. Apply only the sections the article
touches; skip the rest silently.

**Output:** one findings table — no per-section reports.

| # | Location | Finding | Severity | Fix |
|---|----------|---------|----------|-----|

Severity: `blocker` (wrong / unsafe / broken) · `major` (misleading, weak
trade-off) · `minor` (style, polish). Blockers fail the quality gate.

## Architecture & systems

- Claims about architecture, scaling, performance, or security are correct and
  current — verify against official docs, not memory.
- Trade-offs stated, not hidden. Every "X is better" names the cost of X.
- Design patterns used where they fit, named correctly.
- Failure modes acknowledged: what breaks under load, partial failure, retries.
- A diagram (Mermaid) is suggested wherever prose describes a flow, topology,
  or decision tree of 3+ steps.

## Code examples

- Compiles / runs as shown (mentally trace it; run it if a runtime is at hand).
- Modern idiomatic syntax for the stated language/version.
- Readable: intention-revealing names, no dead code, minimal cleverness.
- Edge cases: what happens on empty input, error, timeout — handled or the
  omission is explicitly called out as simplification.
- Security: no injectable strings, hardcoded secrets, or unsafe defaults —
  even in "toy" examples (readers copy them).
- Production-inspired: an experienced engineer would not wince.
- Testing mentioned where the article's promise implies reliability.

## Prompts & LLM content

- Every prompt shown explains *why* it works (mechanism, not magic).
- Failure modes named: where the prompt breaks, degrades, or overfits to one
  model.
- Model-specific claims tagged with model + version; no timeless "LLMs always…".
- Prompt/technique comparisons are grounded (cited eval or reproducible
  example), never invented benchmark numbers.
- Evaluation guidance included when the article teaches a prompt pattern:
  how would a reader verify it works for them?

## Claims handoff

Any factual claim surfaced here that lacks support goes to `blog-engine`
`verify` (Claim Probe+) — do not adjudicate evidence in this file.
