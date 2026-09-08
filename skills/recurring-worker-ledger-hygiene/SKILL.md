---
name: "recurring-worker-ledger-hygiene"
description: "Keep recurring TASKS concise; put unchanged blocked checks in NOTES, not duplicate open tasks."
---

# Recurring Worker Ledger Hygiene

## Purpose

Keep a project's `TASKS.md` useful as the authoritative action and gate ledger when recurring workers run frequently. Preserve detailed observations without accumulating duplicate open tasks.

## Procedure

1. Read the current `TASKS.md` and most recent `NOTES.md` before writing.
2. Identify whether a new observation changes any of: next action, approval requirement, experiment/gate state, blocker, artifact identity, or safety boundary.
3. If it does not change one of those, append the timestamped observation to `NOTES.md` (or the run's `RUN.md`/manifest) rather than adding a new `TASKS.md` item.
4. In `TASKS.md`, maintain one current task per active operation. Replace its status line atomically when meaningful state changes; retain the latest evidence path and precise next condition.
5. For an unchanged blocked or review-gated lane, keep exactly one unchecked task in `TASKS.md`; log each no-change check in `NOTES.md` and include its last-check timestamp in the single task only when it improves operator visibility. Do not create a new unchecked copy each run.
6. When a bounded operation completes or fails, move the detailed timeline to `NOTES.md` or the experiment record; set the task to its resulting next gate. Do not leave historical progress snapshots as unchecked tasks.
7. Update `catalog/KANBAN.md` only when its compact cross-project status or next action materially changes. Scheduler/session listings are scope-limited evidence, never proof that a named worker stopped.
8. Before reporting, check that the top of `TASKS.md` answers: what is active, what unblocks it, what action is permitted now, and which immutable evidence supports that answer.

## Boundaries

Do not erase provenance: preserve dated observations and hashes in `NOTES.md`, experiment ledgers, or manifests. Do not change remote, paid, live, or security scope merely while cleaning records.
