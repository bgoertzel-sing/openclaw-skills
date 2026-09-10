# Run 20260724T234609Z-e4-textlike-calibration-channel-matched

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T23:46:09Z`
- Finished: `2026-07-24T23:46:42Z`
- Status: `succeeded`
- Local or remote: `local CPU`

## Question

With the accepted 75-update non-ceiling student and a channel-matched
label-equivalent direct-logit TC anchor, which ≤92%-fidelity subset source
should be frozen for disjoint confirmation?

## Inputs

- Calibration seeds: `42013,43117,44221`.
- Reserved untouched confirmation seeds:
  `45329,46433,47543,48649,49757`.
- Config: `configs/e4_textlike_bridge_calibration_v1.json`.
- Focused validation: `18 passed`; compileall and diff checks passed.
- The prior amended calibration established mean CS FF accuracy `0.85938` but
  its hidden-state TC loss shift (`0.00810`) was below the frozen denominator
  floor. This run changes only the diagnostic TC anchor to the same direct-
  logit schedule as the symbolic source.

## Expected behavior

All G denominators should be defined. Freeze the highest mean-G eligible
subset primary, with mean extraction fidelity no greater than 92%, before
running any reserved seed.

## Results

- Exit status: `0`.
- Raw artifacts: `artifacts/`.

## Interpretation

All G denominators were defined. Mean CS FF/TC loss was
`0.42516/0.37652`, FF accuracy was `85.94%`, and natural-surface extraction
fidelity was `96.09%`. The natural-surface subset gave mean `G=0.20470`; the
5%-error source gave `0.20485` at `92.84%` extraction, while 10% added errors
fell to `G=-0.02051` at `86.26%`. The natural surface was frozen as the
deployment primary at commit `154e5cf` before reserved seeds ran.

Aggregate SHA-256:
`4486bd3405112a156e85494f2268ad8a7c99b684c865e81435624607eb164d87`.

## Reproduction

Run `command.sh` in the recorded environment after reviewing it.
