# Run 20260728T184406Z-v4-1-gpt2-pcstep-full-suite: v4-1-gpt2-pcstep-full-suite

- Project: `relaleap`
- Started: `2026-07-28T18:44:06Z`
- Finished: `2026-07-28T18:44:23Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/worktrees/v4-gpt2-pcstep`

## Question

Does the completed transformer PCStep preflight preserve all existing RelaLeap
tests?

## Hypothesis or expected behavior

The focused adapter change should introduce no regressions in the current
RelaLeap worktree.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: repository test fixtures only; no external
  data or model download.
- Source branch: `agent/v4-gpt2-pcstep`.
- Completed implementation commit: `19e1022`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Complete result: 155 tests passed in 15.51 seconds.

## Interpretation

**Observed:** the full local suite passed 155/155.

**Interpretation:** the clean-room transformer PCStep seam is locally
integration-safe at this branch state. This is engineering evidence, not
Mesto checkpoint compatibility or evidence for transformer-local predictive
coding.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Freeze a bounded GPU smoke proposal only after reviewing the implementation
boundary and current provider pricing.
