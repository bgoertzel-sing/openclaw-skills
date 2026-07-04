# A6 Matched Excess-over-Control Gate Preregistration

Date: 2026-07-02
Project: OmegaSim thresholded-appraisal reboot

## Scientific intent

The A6 functional candidate gate remains insufficient because linear controls can pass absolute movement criteria as often as, or more often than, appraisal runs. This gate requires each appraisal run to beat matched controls with the same seed, gain, coupling, delay, and noise/model settings available in the current sweep.

## Matching rule

For each appraisal row, compare only with controls sharing the exact `(seed, gain, delay, coupling)` tuple in the same sweep output:

- `linear` control;
- `shuffled` control.

If either matched control is missing, the appraisal row is not a candidate.

## Excess metrics

For a matched appraisal run, compute excess over the strongest matched control for:

- `functional_tail_range` = combined artifact/provenance-debt/risk/prediction-error tail movement;
- `artifact_range_tail`;
- `role_entropy_bits`;
- `debt_range_tail`;
- `risk_range_tail`;
- `prediction_error_range_tail`;
- switch-rate relation to the matched control band.

## Candidate criterion

An appraisal run is an A6 matched excess-over-control candidate only if all conditions hold:

1. matched `linear` and `shuffled` controls exist;
2. appraisal and matched controls are bounded;
3. appraisal passes the absolute A6 functional candidate gate;
4. appraisal tail has no short period under the current detector;
5. `functional_tail_range_excess_over_control >= 0.05`;
6. `artifact_range_tail_excess_over_control >= 0.005`;
7. at least two of artifact/debt/risk/prediction-error tail ranges exceed the matched-control maxima;
8. `role_entropy_bits_excess_over_control >= -0.10`;
9. appraisal switching remains nontrivial and not fully noisy (`0.03 <= switch_rate <= 0.85`);
10. no trivial flat artifact tail (`artifact_range_tail >= 0.03`);
11. no risk collapse (`0.02 < risk_mean_tail < 0.95`).

A simple `matched_excess_score` may be reported for ranking non-candidates, but candidate status is determined by the boolean gate above.

## Fail-closed interpretation

If no appraisal rows pass this matched gate, do not run a denser phase diagram as if the previous absolute candidates were appraisal-specific. The next step should adjust the model or metrics, especially residual-state/lobe discovery beyond role argmax and/or explicit costly prediction actions.
