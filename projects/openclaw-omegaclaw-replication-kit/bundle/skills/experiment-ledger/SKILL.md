---
name: experiment-ledger
description: Plan, execute, capture, and interpret reproducible software or scientific experiments. Use for ownerchmarks, stochastic runs, model evaluations, remote jobs, dependency-sensitive tests, performance comparisons, or any claim that needs recorded evidence.
---

# Experiment Ledger

A consequential run is not complete until another competent person can identify what ran, on which code and data, in which environment, with which result.

## Before execution

1. Identify the project and precise question.
2. Create a run directory with `~/research-agent/bin/new-experiment` or copy `templates/EXPERIMENT.md`.
3. Record repository remote, branch, commit, dirty status/diff pointer, input identifiers, data hashes, configuration, seeds, hardware, and expected outcome.
4. Put the exact command in `command.sh` before running it.
5. For paid remote compute, invoke `remote-compute-guardrails` first.

## Execute

- Prefer a deterministic script over a long interactive command.
- Capture stdout, stderr, exit status, wall time, and tool versions.
- Do not dump the full environment; it may contain secrets.
- Preserve raw metrics in machine-readable JSON/CSV and summarize them in `RUN.md`.
- For long runs, use a named `tmux` session and record its name.

## Interpret

Separate:

- direct output and measurements;
- reproducibility status;
- interpretation;
- alternative explanations;
- remaining uncertainty.

Do not call a run successful merely because it exited zero. Check the intended invariant, test, metric, or artifact.

## Finish

1. Set final status and timestamps.
2. Record result, limitations, artifacts, and reproduction steps.
3. Hash important artifacts when practical.
4. Link the run from `PROJECT.md` and update `TASKS.md`.
5. If the run changes a durable conclusion, add or revise a decision/result record.
6. Add a concise pointer to today's memory note.
