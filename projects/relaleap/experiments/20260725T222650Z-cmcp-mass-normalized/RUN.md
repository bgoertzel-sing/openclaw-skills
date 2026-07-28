# CMCP bridge Step 1: mass-normalized rerun

- Status: complete
- Project: `relaleap`
- Started: 2026-07-25T22:26:50Z
- Execution: local CPU
- Repository: `projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`
- Branch/base commit: `agent/cmcp-epc-kd-bridge` / `1afb6e1`
- Seeds: `101, 211, 307`
- Updates: 160 per seed (80 Task A, 80 contradictory Task B)

## Question

Do the previously observed arm differences survive when every arm's accepted
packet weights are rescaled to exactly the same total KD mass (1.0) on every
update?

## Frozen prediction

**Arms collapse to within noise of each other when total KD mass is held
fixed.**

This prediction is frozen before implementing the normalization flag or
executing any normalized run. The decisive observation is whether ordinary,
naive, CMCP, and oracle outcome differences become negligible relative to the
prior unnormalized run. No post-run threshold is being used to promote a
selection-quality claim.

## Protocol

Add `--normalize-weights` to the existing runner. After each arm computes its
accepted packet weights, divide every nonzero weight by their sum, requiring a
finite positive sum. Preserve the original effective precision as an
accounting diagnostic while recording applied KD mass separately. All other
code, data generation, seeds, update count, initialization, and hyperparameters
remain unchanged from the valid prior v4 calibration.

## Inputs and comparison

Prior artifacts:
`../20260725T161000Z-cmcp-epc-kd-bridge/artifacts/calibration-seed{101,211,307}-u160-contradictory-v4.json`.

Exact execution command is frozen in `command.sh`.

## Results

Execution completed with exit status 0 in 43.46 seconds wall time. All arms had
mean applied KD mass exactly 1.0. Three-seed means:

| Arm | Applied mass | A retention increase | B loss | B accuracy | B ECE |
|---|---:|---:|---:|---:|---:|
| ordinary | 1.000000 | 0.16394022 | 2.30898352 | 0.14887153 | 0.01092225 |
| naive | 1.000000 | 0.16459763 | 2.30811343 | 0.14887153 | 0.01159942 |
| CMCP | 1.000000 | 0.16394173 | 2.30901640 | 0.14887153 | 0.01090665 |
| oracle | 1.000000 | 0.16398119 | 2.30902976 | 0.14887153 | 0.01090013 |

The largest between-arm mean Task-B loss difference was `0.00091633`; all
Task-B mean accuracies were exactly equal at displayed precision.

For comparison, the unnormalized run had applied/raw masses
`1.0/4.0/1.354120/2.0` for ordinary/naive/CMCP/oracle and a largest Task-B
mean-loss difference of approximately `0.02241`.

## Interpretation

**Observation:** the four arms collapsed when KD mass was fixed, matching the
frozen prediction.

**Inference:** the prior fixture did not identify packet selection quality;
its measurable arm differences were overwhelmingly driven by total KD mass.

**Limitation:** equality on this contradictory toy fixture does not show that
all selectors are equivalent on a fixture where independent evidence has
positive value.

## Reproducibility

- Focused tests: `5 passed in 1.90s`.
- Exit status: `exit-status.txt` (`0`).
- Stdout/stderr and GNU time resource statistics are retained.
- Artifact SHA-256:
  - seed 101: `38c861899a95e1311d1513b0e383f4e1aadb7d99d7d53219f585b096af93ba66`
  - seed 211: `f8b9e98a7d4ba99841acdc9a79f628ab71bdf9e58d8005a8763c6eca86b6726b`
  - seed 307: `b2508b8fc0f17b4d69dd41ec227cff9b8c3706ca1db3746ca89c479bbfb3bf53`
