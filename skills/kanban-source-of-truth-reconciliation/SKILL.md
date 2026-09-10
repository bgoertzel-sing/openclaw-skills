---
name: "kanban-source-of-truth-reconciliation"
description: "Add timestamped scoped-scheduler and same-day source-lag rules."
---

# Kanban source-of-truth reconciliation

## Purpose

Maintain `catalog/KANBAN.md` as a compact, pointer-rich cross-project index while treating each project `TASKS.md` as authoritative.

## When to use

Use before daily or global status summaries, and whenever a board entry, worker, or scheduled task appears stale or inconsistent.

## Procedure

1. Read `catalog/KANBAN.md` first, including active commitments and hygiene rules.
2. Capture a reconciliation timestamp, then list active and disabled cron jobs. Record visibility or permission limits explicitly.
3. List visible recent sessions and subagents. Do not infer absence from a visibility-restricted empty result.
4. Enumerate `projects/**/TASKS.md`; prioritize records changed after the board's `Last updated` timestamp plus every project named on the board.
5. Compare authoritative project states with board entries:
   - missing active/recent projects;
   - obsolete statuses, blockers, next actions, or approval boundaries;
   - scheduler claims that lack an active visible job;
   - duplicates or completed work still listed as running.
6. Treat the scheduler view as scoped evidence: retain project-recorded cron IDs when they are not visible, and label the scope/date rather than deleting or disabling them.
7. For same-day work that postdates the board, verify the project record before reporting it as a board delta; if the record itself has not caught up, label it a source-of-truth reconciliation task rather than promoting a session note.
8. Inspect `git status -- catalog/KANBAN.md` before editing. Preserve unrelated, uncommitted user changes.
9. If authorized to edit and a concrete delta is verified, make the smallest pointer-rich update, state its scope, and advance `Last updated`. Otherwise report exact proposed deltas and sources.
10. For paid, live, security, or access-sensitive work, keep the board at the approval/gate level; do not trigger or change such work during reconciliation.

## Output checklist

Report: board freshness; scheduler/session visibility limitations; proposed or applied board deltas; stale scheduled-task claims; unresolved ownership/approval blockers; and any project record needing reconciliation before the board can be updated.
