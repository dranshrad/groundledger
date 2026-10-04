# Craft & Accessibility

## Voice

- Specific > grand
- Evidence before adjectives
- No fake intimacy (“let’s dive in”)
- Prefer verbs over noun stacks

Avoid hollow intensifiers unless earned by data: revolutionary, ultimate,
game-changing, seamless, robust, cutting-edge, delve, tapestry, landscape.

Do not use em dashes (U+2014). Use commas, hyphens, colons, or split sentences.

## Structure

- One H1
- Headings describe jobs, not keywords
- Never skip heading levels
- Open major sections with a declarative answer
- One idea per paragraph. Split the paragraph when comprehension drops.
- Summary boxes are optional. Use them only when they aid scanning.

## Visuals

Use a visual when it:

- proves a claim,
- compares options, or
- shows a UI/state the prose cannot.

Otherwise skip. Prefer original screenshots/diagrams. Stock images need license
notes. Alt text must describe function, not “image1”.

## Links

- Descriptive anchors (state the destination’s job)
- External links support claims. They are not decoration.
- Internal links only to intent-related URLs
- Link purpose must be clear out of context (accessibility)

## Schema policy

Add JSON-LD only when it mirrors visible content:

- `BlogPosting` / `Article`
- `Person` or `Organization` for accountability
- `BreadcrumbList` when breadcrumbs exist

Do **not** add FAQ/HowTo schema for invisible content or score games.
Schema is optional hygiene, not a citation cheat code.

## Accessibility checklist (blocking)

- [ ] Heading order is logical
- [ ] Every informative image has alt text
- [ ] Links make sense out of context
- [ ] Tables have header cells when used
- [ ] Language is plain enough for the stated audience
- [ ] No information conveyed by color alone in described charts

## Platform output

1. Detect project signals (Next/MDX, Hugo, Astro, WordPress, etc.).
2. Adapt the front matter / component constraints to them.

Default: portable markdown.
