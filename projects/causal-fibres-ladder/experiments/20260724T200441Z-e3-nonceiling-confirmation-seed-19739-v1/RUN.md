# Run 20260724T200441Z-e3-nonceiling-confirmation-seed-19739-v1: e3-nonceiling-confirmation-seed-19739-v1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T20:04:41Z`
- Finished: `2026-07-24T20:04:50Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

On one disjoint confirmation seed, does supplied-fibre routing beat matched-budget DGC-20 on CS quality?

## Hypothesis or expected behavior

The supplied-fibre arm passes the programme bar only through a positive confirmation mean and at least four of five strict paired wins; this seed is read only as one frozen pair.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed is encoded in the run ID and command; this seed is disjoint from calibration.
- ID routing is reused on the held-out odd-parity CS split.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

All arms and meters completed. Across the five-seed set, supplied fibre had only 3/5 CS task-accuracy wins, 1/5 task-loss wins, and 0/5 factor-BCE wins, so the frozen bar fails. Aggregate metrics are in `../20260724T201046Z-e3-nonceiling-disposition-v1/RUN.md`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Retain this paired result; do not relax the failed confirmation bar.
