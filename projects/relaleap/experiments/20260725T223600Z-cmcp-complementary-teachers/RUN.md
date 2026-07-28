# CMCP bridge Step 2: complementary-teacher fixture

- Status: complete
- Project: `relaleap`
- Started: 2026-07-25T22:36:00Z
- Execution: local CPU
- Seeds: `101, 211, 307`

## Question

Can the fixture give genuinely independent second-teacher evidence positive
measurable value, while retaining the old contradictory Task B as a separate
plasticity stress test?

## Frozen design

Use two teachers with complementary knowledge:

1. Teacher A is trained on the existing forward modular-sequence domain.
2. Teacher B is independently trained on a reverse modular-sequence domain.
3. Task A uses the forward domain. Task B uses the reverse domain without a
   contradictory label permutation.
4. During Task B, the packet cohort contains Teacher A's base response, its
   exact duplicate, its temperature descendant, and Teacher B's response as
   the genuinely independent packet.
5. Ordinary selects Teacher A only; naive counts every packet; CMCP estimates
   novelty; oracle assigns one unit to Teacher A and one to Teacher B.
6. Applied weights are normalized to total mass 1.0 in every arm, using the
   Step-1 implementation, so outcome differences can identify selection rather
   than total mass.
7. The original half-vocabulary-permuted contradictory fixture remains
   selectable as `contradictory` and is not used to choose the new design.

## Frozen prediction and success signal

Teacher B must itself have lower Task-B evaluation loss than Teacher A before
student outcomes are interpreted. If that fixture validity check passes,
ordinary's under-crediting of Teacher B should cost Task-B loss. Oracle should
beat ordinary on mean Task-B loss; this is the minimum positive-value signal.
CMCP is measured but not required to win in Step 2 because estimator choice is
reserved for Step 3.

Exact commands will be frozen in `command.sh` before execution.

## Results

The run completed locally with exit status 0. Three-seed means:

| Arm | Raw precision | A retention increase | B loss | B accuracy |
|---|---:|---:|---:|---:|
| ordinary | 1.000000 | 0.36879758 | 2.18521064 | 0.22656250 |
| naive | 4.000000 | 0.37241875 | 2.18260275 | 0.22916667 |
| CMCP | 1.665758 | 0.37579525 | 2.18027197 | 0.22786458 |
| oracle | 2.000000 | 0.37582134 | 2.18023286 | 0.22743056 |

Teacher fixture validity passed: Teacher B's mean Task-B loss was `2.09986468`
versus Teacher A's `2.80148311`. Oracle beat ordinary by `0.00497778` mean
Task-B loss, satisfying the frozen minimum positive-value signal.

**Observation:** complementary evidence had positive measurable value under
fixed total KD mass. CMCP nearly matched oracle in Task-B loss, but estimator
selection is deferred to Step 3 as preregistered.

**Limitation:** the effect is small and these seeds are calibration seeds, not
disjoint confirmation.

Focused fixture tests: `2 passed in 2.17s`. Artifact SHA-256:

- seed 101: `10326dafd84d7bf7384309f725d881b3af89a254110a23761dc2d3a1cf1dccc0`
- seed 211: `6cf1abe1ac1170028f76d04cd0132adb2ba513360e462120658321d2cc2a59ad`
- seed 307: `89ed5beef42b0b552d31a30a494a01cf7dcc1897f2213a2c12f8716e5d522103`
