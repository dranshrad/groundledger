# MutationLatch

Paid Cast never mutates live spend by default.

## Closed (default)

Allowed: read exports, summarize UI dumps, draft plans, draft change packs marked `DRAFT — NOT APPLIED`.

**WARNING:** Forbidden:
- claiming that a bid/budget/status change happened;
- pasting “I updated your campaign” without user confirmation.

## Opening the latch

Collect in `MEDIA_LATCH.md` or the chat:

```text
scope: …
max_daily_delta_usd: …
max_budget_move_pct: …
geo_fence: …
audience_fence: …
creative_fence: …
kill_date: …
idempotency_key: …
rollback_cue: …
user_approval: pending | approved
```

Latch opens only when `user_approval: approved` and ceilings are numeric (or explicitly `unlimited` with user typing that word).

## Change pack format

Each mutation item:

1. Platform + object id/name  
2. Before → after  
3. Why (claim + evidence)  
4. Ceiling check  
5. Rollback step  

Ship as a checklist the human (or their API) applies. Groundledger does not hold ad-account credentials as canon.

## Idempotency / rollback

- Prefer named keys so re-running a pack does not double-spend intent  
- Every increase has a decrease path  
- Kill date auto-reminds: after kill_date, re-close latch  
