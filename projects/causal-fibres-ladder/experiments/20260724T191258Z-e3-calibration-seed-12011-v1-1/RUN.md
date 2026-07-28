# Run 20260724T191258Z-e3-calibration-seed-12011-v1-1: e3-calibration-seed-12011-v1-1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T19:12:58Z`
- Finished: `2026-07-24T19:13:00Z`
- Status: `failed`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Can the first frozen E3 calibration seed start on the local Torch build?

## Hypothesis or expected behavior

Fill in before interpreting the result.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Random seeds/data identifiers: record here when relevant.

## Results

- Exit status: 1
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

Failed before training because this Torch version has no `torch.flatnonzero`.
No scientific result was produced. The tested compatibility fix uses
`torch.nonzero(...).flatten()`; the corrected rerun is `../20260724T191338Z-e3-calibration-seed-12011-v1-1-rerun/`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up
