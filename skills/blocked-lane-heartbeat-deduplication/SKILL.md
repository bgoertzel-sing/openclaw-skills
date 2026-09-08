---
name: "blocked-lane-heartbeat-deduplication"
description: "Stop repetitive work on blocked or terminal lanes while preserving bounded change detection and audit evidence."
---

# Blocked-lane and terminal-lane heartbeat deduplication

## Purpose

Use for recurring workers whose next action is blocked on approval, an external condition, or a deliberately frozen gate, and for terminal lanes whose experiment has closed. Preserve necessary safety evidence without repeated identical suites, absence checks, artifact proliferation, or task-ledger churn.

## Procedure

1. Read authoritative project `TASKS.md` and the latest relevant run record. Classify the lane as `active`, `blocked`, `terminal_failed`, `terminal_complete`, or `paused`. Record the blocker/terminal condition, last verified commit or configuration digest, authorization boundary, and exact admissible unblock signals.
2. Before substantive work, inspect only cheap change signals: approval/decision record, task/source revision, relevant manifest transition, explicit unblock message, or permitted resource-state transition.
3. Maintain a compact dedup state keyed by lane and blocker digest: last check time, unchanged count, last emitted receipt, next eligible check, and expiry/owner.
4. If no signal changed:
   - first occurrence: emit one compact `unchanged_blocked` receipt without rerunning suites;
   - second consecutive occurrence with the same blocker digest: suppress detailed evidence creation and request scheduler pause/disable or convert to a low-frequency/event-triggered check;
   - later occurrences: emit nothing unless the declared safety cadence is due.
5. For `terminal_failed` or `terminal_complete`, perform at most one closure validation, then recommend disabling/removing the recurring worker through an authorized scheduler owner. Do not replay a terminal suite merely to demonstrate stability.
6. One successful resource-absence confirmation after deletion/termination is closure unless the run contract predeclares a delayed second check. Never poll a permanently deleted resource merely to reconfirm irretrievability.
7. Periodic revalidation requires a concrete risk. Record cadence, expiry, exact state change sought, and why an event-trigger cannot cover it. Default maximum cadence for unchanged approval/external blockers is daily.
8. If a change signal appears, run the predeclared provider-free validation once, record the transition and evidence, then proceed only within existing authority or return to blocked.
9. If the blocker persists to its horizon, create one owner decision request. Do not accumulate equivalent checks while awaiting it.
10. Keep one current-state line and a roll-up count. Preserve detailed repeats only when they add distinct diagnostic evidence.

## Scheduler/source-of-truth cleanup

- Project `TASKS.md` is authoritative for lane state.
- Kanban is a compact index and must not describe a terminal lane as an active continuation.
- When scheduler visibility is scoped, never infer that absent jobs do not exist. Record exact known job IDs and send cleanup to a main-session/gateway-authorized owner.
- Avoid replacement jobs for unchanged blocked state unless a documented cadence and expiry justify them.
- Independent status reporting is appropriate for genuinely long active cycles; it is not a substitute for suppressing blocked-lane churn.

## Guardrails

- Unchanged state is never authorization.
- Do not start paid, remote, live, access, or security-sensitive work from a heartbeat.
- Keep failed scientific gates, instrument failures, blocked work, and terminal closure distinct.
- Do not overwrite unique forensic evidence while deduplicating logs.

## Output

Report: lane classification; blocker/terminal condition and digest; cheap change signals checked; unchanged count; whether validation ran; next event/cadence; scheduler cleanup needed; and owner action required.
