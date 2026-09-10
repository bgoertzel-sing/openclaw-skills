---
name: "scheduler-kanban-reconciliation"
description: "Add scoped-run diagnostics and freshness checks to prevent stale board claims and silent cron failures."
---

# Scheduler–Kanban Reconciliation

## Purpose

Keep `catalog/KANBAN.md` a truthful compact index of authoritative project work without treating a scope-limited scheduler or session listing as globally complete.

## Procedure

1. Read `catalog/KANBAN.md` first. Treat each referenced `projects/<slug>/TASKS.md` as the source of truth for that lane.
2. List available cron jobs (including disabled when permitted) and visible sessions/subagents. Record returned visibility scope and the observed time. Do not infer that unlisted workers are absent when the tool reports restricted or self-only visibility.
3. Review available job diagnostics: `lastRunStatus`, error, delivery status, and next run. Treat a job as healthy only when those fields are observed in an appropriately scoped listing.
4. Compare the board's `Last updated` date with the reflection date. For each operationally consequential entry (blocked/running/completed or a named next gate), read its authoritative `TASKS.md` if it has changed since the prior reconciliation or the board is older than one day.
5. Classify discrepancies as:
   - board stale: project source contradicts board;
   - scheduler unverified: board lists a job outside visible scheduler scope;
   - scheduler alert gap: authoritative record documents missing failure delivery;
   - project stale: board/source agree but no authoritative update is available;
   - no discrepancy.
6. Recommend edits to the authoritative project record first when it is incomplete; otherwise recommend a minimal board edit. Do not make the board a duplicate task ledger.
7. Propose scheduler repairs only when a job is demonstrably absent from an appropriately scoped listing. Never infer absence from restricted visibility. Escalate documented failure-alert gaps as operator-approved changes.
8. State proposed changes with evidence paths and dates. Never promote a failed, interrupted, or authorization-gated experiment to running/passed.

## Output

Produce a compact report with:
- observed scheduler jobs and visibility limitations;
- fresh board/source discrepancies;
- known run/delivery failure gaps;
- suggested recurring work;
- source-of-truth cleanup; and
- whether operator authorization is required.

## Boundaries

Read-only reconciliation by default. Do not change cron, access, security, paid compute, or live services without explicit approval.
