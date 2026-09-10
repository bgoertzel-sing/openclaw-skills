# Run 20260725T015720Z-e4-cmcp-persistent-calibration: e4-cmcp-persistent-calibration

- Project: `causal-fibres-ladder`
- Started: `2026-07-25T01:57:20Z`
- Finished: `2026-07-25T01:57:40Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

On a stable identified 128-example compositional-shift cohort, does persistent
CMCP suppress recurring duplicate precision while retaining independently
seeded extractions across eight episodes?

## Hypothesis or expected behavior

CMCP should remain close to oracle precision and improve calibration relative
to naive counting. Naive precision should reach 26 and oracle precision 9 by
construction.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Calibration seeds: `61001, 62103, 63209`.
- Stable cohort identity is recorded separately in each seed artifact.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`

All three seeds completed with unchanged model weights and stable cohort
identity. At episode 8, mean effective precision was naive `26.0`, CMCP
`8.91091`, direction-only `1.0`, and oracle `9.0`. CMCP versus naive mean
accuracy was `0.84896` versus `0.76302`; ECE was `0.06525` versus `0.10568`;
and multiclass Brier was `0.24003` versus `0.32604`.

## Interpretation

**Observed:** CMCP tracked oracle precision closely on all calibration seeds
and improved all three predictive/calibration summaries relative to naive
counting.

**Boundary:** This is same-cohort frozen-model evidence accounting. It does
not measure continual-learning retention, forgetting, or cross-example
transfer. The earlier fresh-batch smoke was row-misaligned and is retained
only as implementation history, not scientific evidence.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Freeze conservative gates before opening the five reserved confirmation seeds.
