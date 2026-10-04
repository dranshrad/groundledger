# PROBE contract (examples)

Reject incomplete recommendations at delivery.

## Complete example

```text
P Proof: Homepage title is "Welcome" (fetched 2026-07-25); H1 repeats brand only.
R Relies-on: Keyword map for primary service page (user to confirm).
O Overturn: If GSC (user export) shows brand queries dominate non-brand intent after 60d, type-in win — keep soft title.
B Beacon: Non-brand impressions on /services/ in next Search Console export.
E Effort: now
```

## Incomplete (do not ship)

```text
"Improve meta titles for SEO."
```

Missing Proof, Overturn, Beacon.

## Parallel specialist fan-out

When running `audit`, specialists may fail independently. Report:

```text
Completed: technical, page-fit
Failed / skipped: links (no export), cite-ai (timeout)
Coverage: 4/7 dial axes
```
