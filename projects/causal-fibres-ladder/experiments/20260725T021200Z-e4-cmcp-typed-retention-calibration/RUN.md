# E4/CMCP Typed Retention Calibration

- Project: `causal-fibres-ladder`
- Status: complete; confirmation not justified
- Started: 2026-07-25T02:12:00Z
- Local or remote: local CPU
- Seeds: `61001, 62119, 63241`

## Question

Does the one-constrained-factor curriculum reversal provide a stable
non-ceiling regime in which CMCP tracks oracle retention/plasticity and avoids
naive duplicate-driven interference?

## Boundary

This run selects validity ranges and determines whether confirmation is
justified. It is not confirmation evidence.

## Command

See `command.sh`, frozen before execution.

## Results

All runs exited zero. Every arm began from the identical model hash, performed
48 optimizer updates, saw the identical ordered Task-B batches, and retained
one verified cohort/example ordering.

At episode 6:

| Seed | CMCP precision | Oracle precision | Naive precision | A acc CMCP/naive | B acc CMCP/naive |
|---|---:|---:|---:|---:|---:|
| 61001 | 7.9343 | 7.5 | 21.0 | 0.7734 / 0.8516 | 0.8438 / 0.8281 |
| 62119 | 6.8364 | 7.5 | 21.0 | 0.6094 / 0.8750 | 0.8203 / 0.7422 |
| 63241 | 7.3588 | 7.5 | 21.0 | 0.8281 / 0.8906 | 0.8828 / 0.8828 |

CMCP closely tracked oracle and substantially reduced forgetting relative to
no-ledger and direction-only controls. It did not beat naive accumulation:
naive retained Task A better on all three seeds and matched or nearly matched
Task-B accuracy on two. Combined Task-A/Task-B losses likewise favored naive.

## Disposition

Do not open the five reserved confirmation seeds. This calibration validates
the typed identity/provenance boundary and the matched parameter-learning
harness, but the tested duplicate burst does not cause the predicted naive
interference. A new confirmation would require a newly motivated source of
correlated, systematically biased evidence or a longer nonstationary task
sequence—not post-hoc threshold selection.
