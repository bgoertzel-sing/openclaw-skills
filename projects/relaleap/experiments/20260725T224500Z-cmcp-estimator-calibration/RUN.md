# CMCP bridge Step 3: response versus gradient novelty

- Status: complete
- Project: `relaleap`
- Started: 2026-07-25T22:45:00Z
- Execution: local CPU

## Question

On the complementary-teacher fixture, does response-space conditional novelty
or student parameter-gradient conditional novelty better approximate useful
independent teacher credit?

## Frozen calibration and evaluation protocol

1. Retain fixed applied KD mass 1.0 and the Step-2 fixture.
2. Calibration seeds are `101,211,307`; these may choose exactly one estimator.
3. Response novelty uses standardized teacher probability responses.
4. Gradient novelty uses the flattened gradient of each packet's
   temperature-2 KL objective with respect to all trainable student parameters.
5. Exact duplicates and temperature descendants are judged by the estimator's
   conditional geometry, not zeroed by innovation type. The existing type
   identity remains only for the oracle and provenance audit.
6. Select the estimator with the lower mean Task-B loss on calibration seeds;
   break an exact tie in favor of response novelty for lower computation.
7. Freeze the selected estimator in `selected-estimator.json` before evaluating
   disjoint seeds `401,503,607`.
8. The evaluation criterion is descriptive: compare selected CMCP with
   ordinary and oracle on mean Task-B loss and Task-A retention. No estimator
   switch is allowed after seeing evaluation outcomes.

This is also the frozen descendant policy: descendants receive only the
conditional residual credit measured by the calibrated estimator, rather than
a type-rule temperature policy.

Exact commands will be placed in `command.sh` before execution.

## Results

Calibration selected response novelty exactly according to the frozen rule:

| Estimator | CMCP B loss | Raw precision | A retention increase |
|---|---:|---:|---:|
| response | 2.18031792 | 1.682258 | 0.37571948 |
| gradient | 2.18241845 | 1.360432 | 0.37275377 |

`selected-estimator.json` froze response novelty and evaluation seeds before
evaluation (SHA-256
`1eae0a0d92847b7213c3c36b38dc2f9ff66ad466ad4c7881feeb799dfe75addf`).

Disjoint evaluation means:

| Arm | B loss | B accuracy | A retention increase | Raw precision |
|---|---:|---:|---:|---:|
| ordinary | 2.13274304 | 0.25303820 | 0.42592634 | 1.000000 |
| naive | 2.13078655 | 0.25217014 | 0.42918581 | 4.000000 |
| CMCP-response | 2.12871956 | 0.25217014 | 0.43270205 | 1.705121 |
| oracle | 2.12868345 | 0.25130208 | 0.43275521 | 2.000000 |

**Observation:** selected response CMCP replicated a Task-B loss advantage over
ordinary (`0.00402349`) and nearly matched oracle (`0.00003611` gap), while
incurring a larger Task-A retention-loss increase (`+0.00677571` versus
ordinary). Accuracy did not improve.

**Inference:** response novelty is the better of the two tested selectors for
plastic Task-B loss on this fixture; the evidence is not a general
retention/plasticity win.

Focused tests after estimator implementation: `7 passed in 2.43s`. All raw
artifacts, stdout/stderr, exit status, and SHA-256 values are retained.
