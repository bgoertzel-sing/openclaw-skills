---
name: "recurring-worker-preflight"
description: "Preflight recurrent research-worker commands, evidence gates, and task-ledger updates before substantive execution."
---

# Recurring Worker Preflight

## Purpose

Use before a recurring research worker changes code, runs a costly experiment, or reports an evidence-gate outcome.

## Procedure

1. Read the project `TASKS.md` and the most recent dated `NOTES.md` entry. Treat `TASKS.md` as authoritative for scope, approval, and next action.
2. Identify the single intended action and its gate: local-only, explicit approval, external transport, remote compute, or human decision.
3. Validate command anchors before execution:
   - resolve the test target from the repository (`rg`, test discovery, or declared runner);
   - resolve the Git ref with `git rev-parse --verify` before ancestry/range checks;
   - verify any required artifact, manifest, or transfer harness is present and locally executable.
4. If a gate is not met, do not substitute an adjacent task or silently choose scientific parameters. Record the precise blocker and the smallest next command or human decision in `TASKS.md`/`NOTES.md` as appropriate.
5. On completion, record observed commands/tests, immutable artifact or commit identifiers, scope boundaries, and the next gate. Update the cross-project Kanban only when its compact status or next action materially changes.
6. For scheduler review, query visible cron/session state but label it as scoped; reconcile recurring-lane truth from project records rather than treating an empty listing as inactivity.

## Checklist

- [ ] Authoritative task scope read
- [ ] Approval/transport/decision gate checked
- [ ] Test target and Git ref resolved
- [ ] No unauthorized remote, paid, or live action
- [ ] Result and next gate recorded in project ledger
