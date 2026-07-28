# Run 20260724T140951Z-e2-dual-m1-m5-v1-1-fixed: e2-dual-m1-m5-v1-1-fixed

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T14:09:51Z`
- Finished: `2026-07-24T14:10:02Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Do context-stable supports/subspaces, JBD factor alignment, intervention
selectivity, and factor observability exceed shuffled-context/random-cell
nulls on settled-error and adjoint fields after Prediction 2 is frozen?

## Hypothesis or expected behavior

Observable blocks should exceed nulls across M1--M5. If factor structure is
causally coherent, M3/M4 should also co-locate with each track's frozen P1
home blocks.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Seed `1729`; 128 shared probes, 16 contexts, eight do-pairs per factor.
- Prediction 2: `configs/e2_prediction_2_frozen_v1_1.json`, frozen before
  this run unblinded M3/M4.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifact: `artifacts/e2_dual_m1_m5_v1_1.json`, SHA-256
  `4aa579a557bd72ca9e38904fb05424c74e36bf4efe62ad0c4979e06f1505f6e0`.
- Focused estimator/harness tests: 18 passed.
- All 12 robust JBD fits converged.

## Interpretation

**Observed:** settled support stability exceeds null from blocks 2--6, but M5
is at chance through block 5 and reaches `0.793` only at block 6. Adjoint
support/subspace stability exceeds null throughout; M5 decreases from `0.859`
at block 1 to `0.691` at block 6, versus shuffled values near `0.47`.
M3 factor-alignment and M4 intervention-dominance scores generally exceed
their nulls on the adjoint track and in settled block 6.

**Observed:** the strongest adjoint M3/M4 scores occur in blocks 3 and 5, not
the frozen adjoint home blocks 1--2. Settled M3 co-locates with block 6, while
its strongest M4 score occurs in block 4.

**Inferred:** the estimator battery is operational and finds non-null
structure, but the pre-registered co-location prediction is not cleanly
confirmed. This single-seed reduced run has no frozen M1--M5 quantitative
acceptance envelope, so it cannot honestly classify confirmatory E2-A/B.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Do not select recovered fibres for E3 from this uncalibrated run. Freeze
M1--M5 acceptance thresholds from constructed/pathology/null controls and run
the required disjoint `n>=3` calibration/confirmation replicates first.
