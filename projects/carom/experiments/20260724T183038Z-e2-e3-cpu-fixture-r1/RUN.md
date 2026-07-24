# Run 20260724T183038Z-e2-e3-cpu-fixture-r1: e2-e3-cpu-fixture-r1

- Project: `carom`
- Started: `2026-07-24T18:30:38Z`
- Finished: `2026-07-24T18:31:53Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/carom/repos/carom`

## Question

Does E2/E3 remain deterministic across five seeds, and what is its CPU cost?

## Hypothesis or expected behavior

All 25 arm/seed combinations should finish and repeat exactly.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: record here when relevant.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Passed operationally: 25/25 repeated exactly. Wall time 74.23 s; peak RSS
375,468 KB. Forty updates left arms near chance, so this does not disposition
E2/E3. Full naive scaling is multi-day CPU work; E4/E5 remain closed.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up
