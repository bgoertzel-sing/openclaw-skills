# Run 20260724T191437Z-e3-calibration-seed-14251-v1-1: e3-calibration-seed-14251-v1-1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T19:14:37Z`
- Finished: `2026-07-24T19:14:45Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does the third frozen E3 calibration seed provide enough CS headroom for
confirmation?

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

No. The no-update interface is 100% exact on ID and 99.22% exact on CS.
Across all three calibration seeds the no-update CS mean is 99.74%, so E3
confirmation would be ceiling-limited and was not launched.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up
