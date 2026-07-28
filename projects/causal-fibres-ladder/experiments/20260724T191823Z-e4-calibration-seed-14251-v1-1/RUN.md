# Run 20260724T191823Z-e4-calibration-seed-14251-v1-1: e4-calibration-seed-14251-v1-1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T19:18:23Z`
- Finished: `2026-07-24T19:18:27Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the third E4 calibration seed justify confirmation?

## Hypothesis or expected behavior

Fill in before interpreting the result.

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

No. SC recovers `0.0980` of CS loss headroom and no CS task-accuracy
headroom. Across all three seeds SC remains below `0.2`; confirmation was not
launched.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up
