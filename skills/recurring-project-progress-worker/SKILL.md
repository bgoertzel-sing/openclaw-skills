---
name: "recurring-project-progress-worker"
description: "Run safe scheduled project progress workers with provenance, gates, and handoffs."
---

# Recurring Project Progress Worker

Use when creating, auditing, or running a scheduled/background project worker that advances an ongoing research or engineering project without direct human supervision.

Do not use for paid remote compute, destructive cleanup, access-control/security changes, release publication, or default-branch pushes unless Benjamin has explicitly approved that specific action under the normal project policy.

## Preconditions

1. Identify the active project and read its project record:
   - `projects/<slug>/PROJECT.md`
   - `projects/<slug>/TASKS.md`
   - `projects/<slug>/DECISIONS.md`
   - recent `NOTES.md`, experiment records, and relevant repository instructions.
2. Inspect current mutable state before changing anything:
   - repository branch and `git status`;
   - current task status;
   - recent worker outputs or cron run history when applicable.
3. Choose a narrow, reversible slice from the project task list.
4. If the slice involves experiments, benchmarks, stochastic behavior, model evaluation, remote jobs, or dependency-sensitive results, use the experiment-ledger workflow.

## Worker discipline

1. Prefer local, low-cost, reversible actions.
2. Make progress in small coherent slices:
   - inspect first;
   - edit only targeted files;
   - run the narrowest meaningful verification;
   - broaden checks only when warranted.
3. Preserve provenance:
   - exact command lines;
   - repository path and commit/branch;
   - generated artifact paths;
   - exit status and important logs;
   - limits, skipped checks, or known uncertainty.
4. Fail closed on scientific claims:
   - do not promote estimates, benchmarks, detector outputs, or model-evaluation results without calibration/diagnostics appropriate to the project;
   - label engineering pass/fail separately from scientific validity.
5. Keep project records current:
   - update `TASKS.md` when task status changes;
   - update `DECISIONS.md` only for durable decisions and rationale;
   - update `NOTES.md` for working observations;
   - add experiment `RUN.md` conclusions when an experiment was run.
6. Back up coherent tested slices with local commits when appropriate and safe; push only under the project/GitHub policy already approved for that repository.

## Communication and routing

1. Send user-visible updates only for material progress, failures, blockers, unexpected cost/security risk, or requested completion notices.
2. Avoid boilerplate acknowledgement messages. If work will take more than about 10-15 seconds to frame, send a brief context-specific note, then continue.
3. Scheduled/progress updates should go to the dedicated scheduled-updates channel unless the project has a more specific approved route. The single daily 7AM Pacific summary remains in the main Protobots channel.
4. For project-level bot-bot discussion, use the dedicated ProtoBots-BotBotChats channel and suppress a scheduled duplicate if a substantive discussion occurred within the previous 24 hours.

## End-of-run checklist

Before declaring completion:

1. Run the smallest meaningful gate: test, lint, build, typecheck, command smoke test, artifact inspection, or documented blocker.
2. Check `git status` and note changed/untracked files.
3. Record durable project changes in the project notebook and daily memory with pointers, not duplicated prose.
4. Report:
   - what changed;
   - evidence/checks run;
   - artifacts or commits;
   - remaining risks or next unresolved item.

## Cron job guidance

When scheduling a recurring worker:

1. Use OpenClaw cron rather than shell sleeps or polling loops.
2. Prefer isolated `agentTurn` jobs for project workers.
3. Include a concrete prompt with:
   - project slug;
   - current objective;
   - allowed write scope;
   - approval boundaries;
   - required verification;
   - required project-record and memory updates.
4. Do not create duplicate recurring jobs for the same lane without inspecting existing cron jobs first.
5. Disable or remove obsolete jobs when the project closes or the cadence is superseded.
