# Run 20260724T210500Z-e4-channel-confirmation-3seed: e4-channel-confirmation-3seed

- Project: `causal-fibres-ladder`
- Started: `2026-07-24T21:05:00Z`
- Finished: `2026-07-24T21:12:00Z`
- Status: `succeeded`
- Local or remote: `local`
- Working directory: `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/projects/causal-fibres-ladder/repos/relaleap-e1`

## Question

Do the three qualitative findings from the E4 channel diagnostic
calibration (completeness, weight monotonicity, channel superiority) replicate
on disjoint confirmation seeds under frozen thresholds?

## Hypothesis or expected behavior

All five frozen thresholds should pass on three disjoint seeds:
- C1: full4 G > 1.5 × two-cap mean at every matched weight/channel
- C2: all 9 mask/channel series strictly increasing through 5×
- C3: logit G > 1.5 × hidden G for full4 at every weight
- C4: |both_G − logit_G| < 0.01 for all 12 conditions
- C5: full4/5×/both G > 1.0

## Inputs

- Git state: commit `daa06e9` on branch `agent/e1-guarded-homotopy`
- Base student: `configs/e3_partial_student_v1.json` (75 updates, frozen)
- Diagnostic config: `configs/e4_channel_confirmation_frozen_v1.json`
- Calibration reference: `experiments/20260724T202915Z-e4-channel-diagnostic-summary-v2/`
- Confirmation seeds: `20801, 21903, 23017` (disjoint from calibration `12011, 13121, 14251`)
- Grid: 3 masks × 4 weights × 3 channels + FF and TC baselines, ID and CS splits
- 128 evaluation examples per split
- Command per seed: `python scripts/run_e4_channel_diagnostic.py --base-config configs/e3_partial_student_v1.json --diagnostic configs/e4_channel_confirmation_frozen_v1.json --seed <SEED> --output <OUT>`
- Aggregate: `python scripts/summarize_e4_confirmation.py --inputs <seed_jsons> --thresholds configs/e4_channel_confirmation_frozen_v1.json --output <summary>`

## Results

- Exit status: 0 (all three seeds and summary)
- Artifacts: `artifacts/seed_20801.json`, `artifacts/seed_21903.json`, `artifacts/seed_23017.json`, `artifacts/result.json`
- Result SHA256: `7f67c9082e39be9fe7ed733a9973245830f8fa4a87184c8c90a5be2218cdc956`

### Confirmation baselines (CS, mean of 3 seeds)

| Condition | Task Loss | Task Accuracy | Factor Bit Acc |
|---|---|---|---|
| FF | 0.82555 ± 0.21791 | 0.97396 ± 0.03854 | 0.99479 |
| TC (diagnostic) | 0.81090 ± 0.21491 | 0.97656 ± 0.04059 | 0.99479 |

### Threshold checks

| Threshold | Description | Result |
|---|---|---|
| C1 | full4 G > 1.5 × two-cap mean (12 conditions) | ✅ PASSED (ratios 1.9994–2.0003) |
| C2 | Strictly increasing G through 5× (9 series) | ✅ PASSED (9/9) |
| C3 | logit G > 1.5 × hidden G for full4 (4 weights) | ✅ PASSED (ratios 2.1623–2.1781) |
| C4 | |both_G − logit_G| < 0.01 (12 conditions) | ✅ PASSED (max diff 1.482e-5) |
| C5 | full4/5×/both G > 1.0 | ✅ PASSED (G = 4.34430 ± 0.28271) |
| **All** | | **✅ PASSED** |

### Best CS condition

full4/5×/both: task loss `0.76171 ± 0.20429`, task accuracy `0.98438 ± 0.02706`,
factor-bit accuracy `0.99609`, G_task_loss `4.34430 ± 0.28271`.

### Calibration vs confirmation comparison

| Metric | Calibration (3 seeds) | Confirmation (3 seeds) |
|---|---|---|
| FF CS loss | 1.04947 | 0.82555 |
| TC CS loss | 1.03227 | 0.81090 |
| full4/1×/hidden G | 0.37686 | 0.40887 |
| full4/1×/logit G | 0.92634 | 0.88991 |
| full4/5×/both G | 4.55170 | 4.34430 |
| full4/two-cap ratio (1× hidden) | 2.001 | 2.000 |
| logit/hidden ratio (full4 1×) | 2.458 | 2.177 |

The confirmation seeds have lower baseline loss (higher starting accuracy),
yet all qualitative patterns replicate. The full4/two-cap ratio is remarkably
stable at exactly 2.0, consistent with the per-factor normalization: full4 has
twice as many factors at the same per-factor weight as each two-factor cap.

The logit/hidden ratio is slightly lower in confirmation (2.18 vs 2.46),
reflecting seed variation but remaining well above the 1.5 threshold.

## Interpretation

All five frozen confirmation thresholds passed. The three qualitative findings
are confirmed:

1. **Information completeness matters**: full4 produces approximately twice
   the recovery of the mean two-factor cap at every matched weight and channel,
   consistent with per-factor normalization (each additional factor contributes
   additively at matched per-factor force).

2. **Constraint weight matters**: recovery is strictly increasing through 5×
   for all nine mask/channel series with no saturation observed.

3. **Injection channel matters**: direct-logit injection provides approximately
   2.2× the recovery of hidden-state settlement. The combined channel is
   numerically indistinguishable from logit alone (max difference `1.5e-5`),
   confirming that hidden settlement adds no value once the logit bypass is
   available.

The frozen negative E4 gate remains unchanged. Full4 uniquely identifies the
16-way class on this synthetic grammar, so these results are diagnostic, not
deployability evidence. The confirmation sharpens the conclusion that the prior
weak E4 was a joint failure of incomplete information, insufficient constraint
weight, and a hidden-state injection bottleneck.

## Reproduction

Run the three seed commands listed in Inputs, then the summary command.
All configs are frozen in the repository.

## Follow-up

- E5 scope should prioritize a provenance-aware direct-logit constraint sink
  after the typed tensor adapter prerequisite (see `docs/e5_post_e4_scope.md`).
- A deployable source of complete constraints must be established separately;
  full4 is label-equivalent on this synthetic grammar only.
- The constraint weight sweep did not saturate at 5×; if a future deployable
  constraint source is found, a wider sweep may identify an optimal scale.
