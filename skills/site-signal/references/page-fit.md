# Page-fit (SERP shape vs page)

Goal: detect when the target URL’s **page type** fights the SERP’s dominant job.

## Page-type vocabulary

| Type | Typical job |
|------|-------------|
| Guide / explainer | Teach; long-form or modular FAQ |
| Category / hub | Navigate a set; comparison rails |
| Product detail (PDP) | Decide + buy / trial |
| Local / store | Visit / call / direction |
| Tool / calculator | Do a task in-page |
| Landing (campaign) | Convert one offer |
| Support / docs | Resolve a task |

## Method

1. Infer query cluster (user-supplied keywords or page topic).
2. Sketch expected SERP shapes from public knowledge + any SERP export the user provides — **do not invent rank positions**.
3. Classify target URL type from structure (nav, H1, CTA, schema, length).
4. Score gaps 0–5 on: type match, depth, UX friction, schema honesty, media, freshness cues.
5. Emit PROBE items for the largest gaps first.

## Common mismatches

- Thin landing page ranking intent that wants a guide
- Blog post trying to win transactional “buy X” SERPs
- City page that is a thin template with no local proof
- Category page with no filters / uniqueness vs facet spam

## Handoff

- Structural rewrite → `blog-engine`.
- Multi-URL cluster → `orbit-discovery`.
- Paid tests on fixed landing → `paid-cast`.
