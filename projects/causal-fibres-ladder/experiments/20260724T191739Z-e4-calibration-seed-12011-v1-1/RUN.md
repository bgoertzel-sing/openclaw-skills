# Run 20260724T191739Z-e4-calibration-seed-12011-v1-1: e4-calibration-seed-12011-v1-1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T19:17:39Z`
- Finished: `2026-07-24T19:17:43Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Can observed-token or symbolic-constraint settlement recover material
16-class task headroom over FF?

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

TC exposes small CS headroom (`0.0781` to `0.0938` accuracy). OT, SC, and
OT+SC do not improve CS task accuracy. SC recovers `0.0743` of loss headroom
and `0.1111` of factor-bit headroom, below the material `0.2` bar.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up
