# Run 20260724T200720Z-e3-v4-continual-seed-15313-v1: e3-v4-continual-seed-15313-v1

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T20:07:20Z`
- Finished: `2026-07-24T20:07:25Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Does one V4 sequential factor-stream seed support Prediction 1 under matched selected-scalar work?

## Hypothesis or expected behavior

Dense ungated settlement should match raw BP beyond noise; any protection should be confined to support-restricted arms or track proximal trajectory divergence.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed is encoded in the run ID and command.
- Stream order: subject number, object number, tense, negation; inactive factors are fixed to zero.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

## Interpretation

All five arms completed with dense/BP selected-scalar ratio 1.00599. The five-seed aggregate shows lower dense than BP drift on three seeds but no positive covariance with proximal divergence, so Prediction 1 is not cleanly supported. See `../20260724T201046Z-e3-nonceiling-disposition-v1/RUN.md`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Treat effective-step matching as the unresolved alternative explanation.
