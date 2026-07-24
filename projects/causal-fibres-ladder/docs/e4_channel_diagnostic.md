# E4 completeness, weight, and channel diagnostic

Date: 2026-07-24

## Design

The frozen 75-update student was evaluated on three calibration seeds with a
`3 masks × 4 weights × 3 channels` exploratory grid:

- masks: factor caps `0--1`, `2--3`, and full four-factor information;
- weights: `0.5x, 1x, 2x, 5x`;
- channels: hidden-state settlement, direct-logit injection, and both.

FF and the existing hidden-state TC settle remained the common baseline and
diagnostic anchor. The v1 run used mean BCE and was found to dilute each
full4 factor by half relative to a two-factor cap. Those runs are retained,
but completeness conclusions use v2, which sums per-factor BCE and divides by
the two-factor reference width.

This protocol is exploratory. It does not revise the frozen negative E4 gate.

## Results

Across seeds `12011,13121,14251`, CS FF loss/accuracy was
`1.04947/0.95052`; diagnostic TC was `1.03227/0.96094`.

At matched weight and channel, full4 task-loss G was almost exactly twice the
mean of the two caps after per-factor normalization. At 1x hidden,
full4 G=`0.37686` versus cap mean `0.18833`.

All nine mask/channel series increased strictly through 5x. Full4 hidden G
rose from `0.1887` at 0.5x to `1.8635` at 5x. The current 1x setting was
therefore too weak relative to the state-consistency penalty; no saturation
was observed in the tested range.

The direct-logit channel materially exceeded hidden settlement. For full4,
logit/hidden G was `2.458` at 1x and `2.443` at 5x. The combined channel was
numerically indistinguishable from logit alone (maximum absolute G difference
`1.16e-5`), so hidden settlement adds no measurable value once the logit
bypass is available.

The best CS condition was full4/5x/both:

- task loss `0.97079`;
- task accuracy `0.98438`;
- factor-bit accuracy `0.98893`;
- task-loss G `4.55170`.

G exceeds one because this condition beats the hidden-state TC diagnostic
anchor. All four synthetic factors uniquely identify the 16-way class, so
this is a diagnostic upper case and not evidence that equivalent information
is deployably available.

## Interpretation

The prior weak E4 result was not evidence that constraints are intrinsically
ineffective. It combined incomplete information, a low constraint-to-penalty
ratio, and a bottlenecked hidden-state channel. The strongest effect is the
direct-logit bypass, followed by weight; completeness contributes additively
when per-factor force is held constant.

A prospective E4 redesign should prioritize a direct-logit constraint adapter
and explicitly calibrate constraint versus anchor scale. It must separately
establish a deployable source of complete constraints. Deeper hidden
settlement alone is not the next experiment.

## Confirmation

Three disjoint confirmation seeds (`20801, 21903, 23017`) were run
under five frozen thresholds (C1--C5) before unblinding. All five passed:

- C1 (completeness): full4/two-cap ratio `1.9994--2.0003` across 12 conditions
  (threshold `1.5`).
- C2 (weight monotone): `9/9` series strictly increasing through 5×.
- C3 (logit > hidden): ratio `2.1623--2.1781` for full4 across 4 weights
  (threshold `1.5`).
- C4 (both ≈ logit): max `|both−logit|` `1.482e-5` across 12 conditions
  (threshold `0.01`).
- C5 (positive recovery): full4/5×/both G `4.34430 ± 0.28271` (threshold `1.0`).

The confirmation seeds have lower baseline loss (FF CS loss `0.82555` vs
calibration `1.04947`), yet all qualitative patterns replicate. The
full4/two-cap ratio is exactly `2.0`, consistent with per-factor
normalization. The logit/hidden ratio is slightly lower (`2.18` vs `2.46`)
but well above threshold.

## Evidence

### Calibration
- Aggregate:
  `experiments/20260724T202915Z-e4-channel-diagnostic-summary-v2/`
- Corrected seed runs:
  `experiments/20260724T202640Z-e4-channel-diagnostic-seed-12011-v2/`,
  `experiments/20260724T202651Z-e4-channel-diagnostic-seed-13121-v2/`,
  `experiments/20260724T202703Z-e4-channel-diagnostic-seed-14251-v2/`.

### Confirmation
- Aggregate:
  `experiments/20260724T210500Z-e4-channel-confirmation-3seed/`
- Seed runs: `artifacts/seed_20801.json`, `artifacts/seed_21903.json`,
  `artifacts/seed_23017.json`.
- Frozen thresholds: `configs/e4_channel_confirmation_frozen_v1.json`.

