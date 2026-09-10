# Run 20260724T061200Z-e1-posthoc-m0-v1-1-corrected: e1-posthoc-m0-v1-1-corrected

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T06:12:00Z`
- Finished: `2026-07-24T06:12:03Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

On the reduced six-block terminal homotopy student, do one matched KD and one
teacher-free CE re-settle pass produce Mesto-like early/middle top-5% field
mass, and does the settled error field agree with the negative BP adjoint under
the v1.1 M0 metrics?

## Hypothesis or expected behavior

The instrumentation should preserve weights, emit both substrates in one
schema, distinguish exact identity from a deterministic random-field null, and
report the six-block depth profile. This reduced eight-step run is not expected
to reproduce the 124M result by assumption.

## Inputs

- Git state: `git.txt`
- Environment: `env.txt`
- Command: `command.sh`
- Config: `configs/e1_homotopy_smoke.json`, seed `1729`, terminal settlement
  depth `8`.
- Criteria: `configs/e1_e2_acceptance_v1_1.json`, including Prediction 2 frozen
  before any M3/M4 unblinding.
- Source revision SHA-256:
  `fcf44a4dcf83b3c0bdca3edf67a7ab138f04bf4ad17f531b13b2344e7b40537b`.

## Results

- Exit status: 0
- Standard output: `stdout.log`
- Standard error: `stderr.log`
- Machine status: `status.json`
- Artifacts: `artifacts/`
- Focused regression: 12 tests passed.
- Results JSON SHA-256:
  `369bf6829fd851c6c8be5bff3dc796690221e26706c13c46a6b1de326155ca85`.
- Field NPZ SHA-256:
  `92c2a8c264a1c0b5d8013319ca666e152c5ab94385a9220e576475b4bc6ea141`.
- All model weights remained unchanged during KD and CE settlement.
- KD and CE both assigned `100%` of global top-5% settled-field mass to block
  6. Mesto's supplied twelve-to-six rescaled KD profile is approximately
  `[0.298, 0.320, 0.266, 0.100, 0.016, 0.001]`.
- Blocks 1--3 had numerically zero settled error after eight steps. Block 4
  cosine to the BP descent field was `0.173` KD / `0.187` CE. Blocks 5 and 6
  were strongly direction-aligned (`0.9989/1.0000` KD;
  `0.9993/1.0000` CE), with top-5% support Jaccard
  `0.962/0.987` KD and `0.987/0.987` CE. Deterministic random-field Jaccards
  were `0.013--0.037`.

## Interpretation

**Observed:** the reduced eight-step settle is readout-local and does not
reproduce the supplied early/middle Mesto depth profile. Upstream M0 cannot be
meaningfully interpreted where the settled field is exactly zero.

**Inferred:** the current reduced settle depth/dynamics do not propagate the
task signal far enough upstream for a valid six-block M0 reproduction.
Near-perfect block-5/6 alignment is expected from local descent and is not a
whole-model adjoint-identification result.

**Decision:** retain this as a negative instrument result. Before E2 compares
substrates, run a preregistered settlement-depth sweep through `T=128` (and
check the precise error-field convention against the R8/R9 implementation).
Do not unblind M3/M4 or interpret this run as refuting the supplied 124M claim.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.

## Follow-up

Implement the depth sweep with fixed terminal weights and probe set, reporting
energy, per-block field norm, P1 profile, and M0 at each depth. Proceed to the
dual-substrate E2 battery only if nonzero upstream fields make M0 identifiable;
otherwise record an observability/settlement-depth blocker.
