# CAROM frozen-GPT-2 12k review synthesis

Date: 2026-07-22

Sources:

- `2026-07-22-carom-gpt2-12k-fable.md`
- `2026-07-22-carom-gpt2-12k-sol.md`
- `../carom_gpt2_12k_detailed_results_2026-07-22.pdf`

## Consensus

Both independent reviews agree on the following.

1. The degradation between steps 3,000 and 5,000 is real. Endpoint accuracy,
   training loss, itinerary completeness/order, and intervention effects fail
   together while the stretched OneCycle schedule is near its peak LR.
2. High-LR displacement is the leading causal hypothesis, not an established
   cause. A single seed, changed schedule, changed checkpoint cadence, and a
   changed training-data stream prevent causal attribution.
3. Raw edge accuracy near 0.70 is not evidence that graph compilation survived.
   For short chains it is compatible with a majority-negative predictor.
4. The cleaner order contrast is forced-minus-shuffled (0.0306 at step 3,000),
   not natural-minus-shuffled (0.0801), because the latter also changes dwell,
   amplitude, smoothness, and exposure.
5. More inference steps do not rescue the retained models. This disfavors a
   simple insufficient-settling explanation.
6. The economical optimization path is a bounded low-LR warm start from the
   earlier 4k checkpoint (accuracy 0.412), while fresh matched runs are needed
   to test the LR hypothesis scientifically.

## Important newly identified confounds

- Training and online checkpoint evaluation share one Python RNG. Evaluation
  therefore changes subsequent training batches, and the 4k/12k cadence
  difference changes the training stream.
- The masked edge BCE uses default mean reduction over the padded matrix, so
  its effective scale depends on live length and padding.
- Checkpoints do not preserve enough optimizer/scheduler/RNG state for an exact
  continuation; using them is a warm start with reset optimizer state.
- The repeatedly inspected fixed corpus is now a validation set, not an
  unbiased final test set.

## Differences in recommended retry details

The reviews agree on ordering but differ slightly on the first warm-start
configuration. Fable proposes parameter-group LRs of 1e-4 for core/output and
5e-5 for routing/GLV-sensitive groups, with the edge head initially frozen if
checkpoint diagnostics validate it. Sol proposes a simpler uniform 1e-4 LR
for the first 2,000-update probe and defers module-specific rates/freezing until
the edge metrics are repaired.

Decision: adopt Sol's conservative sequencing. Do not freeze or privilege an
edge head whose learning has not been established. First repair diagnostics,
then run a uniform-LR warm-start probe; parameter-group localization follows
only if the probe is stable but inadequate.

## Ordered next-experiment ladder

### Stage 0: checkpoint-only forensics (no paid training)

Evaluate the earlier 4k final checkpoint and 12k steps 3k, 4k, 5k, and 12k on
new, versioned validation corpora. Separate RNGs for training, monitoring,
validation, and interventions. Report per-length and exact-program endpoint
accuracy with program-level paired bootstrap intervals; edge prevalence,
predicted-positive rate, precision, recall, balanced accuracy, MCC, PR-AUC,
tie-correct ROC-AUC, calibration, and exact-chain recovery; entry/router
entropy; activity mass, dwell, clamp rates, operator exposure, workspace-update
norms, rho distributions, and invasion margins. Add all-negative/all-positive
baselines.

Gate: if edge positive recall <0.20 or PR-AUC is not at least prevalence+0.05,
stop interpreting raw edge accuracy and repair/reweight the loss before any
longer run.

### Stage 1: economical warm-start probe

- Start from the earlier 4k-final model weights; explicitly call this a warm
  start because Adam/scheduler state is reset.
- AdamW, LR 1e-4, weight decay 1e-4, batch 64, clip 1.0.
- Maximum 2,000 updates; validation/checkpoint every 100; full interventions
  every 500.
- Preserve optimizer, scheduler, Python/Torch/CUDA RNG states and configuration
  hashes in every checkpoint.
- Early stop after three consecutive validations >=0.03 below best-so-far
  without >=0.01 improvement over the preceding 500 updates; immediate stop
  for nonfinite values, extreme gradients, or two validations below 0.30.
- Minimum success: accuracy >=0.45 with paired improvement over the starting
  checkpoint and no material mechanism degradation. Promotion target: >=0.50,
  coverage >=0.70, forced-minus-shuffled >=0.03. The original substantive
  target remains >0.55.

### Stage 2: local LR bracket from identical warm-start weights

Run 500-update arms at 3e-5, 1e-4, and 3e-4 with identical batch/RNG streams,
validation every 50, and checkpoints every 100. Continue only the stable winner
for at most 1,500 additional updates.

### Stage 3: fresh schedule discriminator

Use identical initialization, pre-generated/hash-checked batches, and cadence:

- reproduced 4k OneCycle control: max LR 2e-3, 4,000 updates, pct_start 0.3;
- lower-peak 4k control: max LR 5e-4, otherwise identical;
- capped continuation: warm up 4e-5 to 5e-4 over 600 updates, cosine decay to
  5e-5 by step 6,000.

The high-LR hypothesis gains strong support only if the 2e-3 arm reproduces
collapse while one or both conservative arms avoid it under matched streams.

### Stage 4: module/loss localization

Only after calibrated edge diagnostics exist, compare uniform LR against a
0.3x LR for routing/GLV-sensitive modules, and compare normalized live-pair
edge BCE weights (control 1.0 versus 0.25). Do not freeze the edge head based
on raw accuracy alone.

### Stage 5: replication and confirmation

Promote one configuration to seeds 0, 1, and 2, adding 3 and 4 if uncertainty
is large. Select on validation only, then evaluate once on an untouched test
corpus. Require paired improvement over the matched control, mean L2--4 >=0.50
as a promotion gate, no seed below 0.40, median coverage >=0.70, and median
forced-minus-shuffled >=0.03. Retain >0.55 as the substantive target and 0.65
as aspirational until replicated.

## Mechanistic claim boundary

Licensed: a modest useful state appeared and was destroyed; endpoint and
trajectory organization degraded together; additional inference steps did not
rescue these checkpoints; the frozen GPT-2 weights themselves did not change.

Not licensed: preserved dependency compilation; learned commutation; an
order-specific 0.0801 causal effect; a formally stable heteroclinic channel;
general compositional extrapolation; or a claim that high LR caused the failure
without matched controls.
