# CAROM E0/E1 Exposure-Controlled Experiment Specification

Date: 2026-07-20

## Question

Does the learned-free versus hand-engineered heteroclinic-controller accuracy
gap survive paired deterministic evaluation when controller activity mass,
integrated command exposure, and recurrent workspace-update magnitude are
measured and activity mixing is normalized?

## Frozen arms

Train four otherwise matched itinerant arms for each of five seeds:

1. `fixed_raw`: fixed inhibition chain, original unnormalized mixture.
2. `free_raw`: learned inhibition, original unnormalized mixture.
3. `fixed_norm`: fixed inhibition chain, activity-normalized mixture.
4. `free_norm`: learned inhibition, activity-normalized mixture.

The normalized mixture is

`beta = gain * sum_m(a_m rho(c_m)) / (epsilon + sum_m a_m)`.

Use gain 1.0 and epsilon 1e-6. Do not initialize the free matrix from the
fixed chain and do not add successor-labelled regularization.

## Invariants

- Training and evaluation use distinct Python RNGs.
- Every arm and seed is evaluated on the same serialized paired corpus.
- Evaluation is deterministic: model evaluation mode disables controller noise.
- Model initialization and training batches are identical within each seed,
  modulo parameters whose shapes/roles differ by arm.
- Evaluation must not mutate training RNG state.
- Raw and normalized arms differ only in activity normalization.
- The free inhibition matrix starts from the existing random symmetric-like
  initialization, never from the engineered successor chain.

## Training and evaluation

- Seeds: 7, 17, 27, 37, 47.
- Training: 3,000 updates, batch 128, AdamW, OneCycleLR, d=64, K=16.
- Controller: 70 steps, dt=.2, noise=.02 during training, fatigue tau=6,
  fatigue k=1.5, leak=.02.
- Paired evaluation corpus: 2,048 examples, balanced as nearly as possible
  across effective depths 2--5, generated once from evaluation seed 20260720.

## Required outputs

For every arm/seed and every evaluation example:

- slot accuracy and exact-workspace accuracy;
- program depth and command tokens;
- dominant-mode sequence and compressed transition sequence;
- per-mode dwell counts and integrated activity exposure;
- total activity mass, overlap count/fraction, skips, reversals, revisits,
  terminal trapping, and command-position exposure;
- integrated workspace-update norm.

Aggregate accuracy by depth and command, plus paired fixed-minus-free
differences with bootstrap 95% intervals. Preserve raw per-example JSONL.

## Primary contrasts and decisions

1. `fixed_raw - free_raw`: reproduce the original gap under repaired E0
   measurement. If the paired interval includes zero or the result is not
   reproducible across seeds, stop treating 13.1 points as established.
2. `fixed_norm - free_norm`: residual gap after activity normalization.
3. `free_norm - free_raw`: benefit or harm from normalization.

Normalization is the primary explanation if it removes at least half of the
paired raw gap while not increasing integrated workspace-update norm by more
than 10%. If a substantial gap remains, proceed to E2 mode-specific fitness.

## Validity gates

- All five seeds complete all four arms.
- Evaluation corpus hash is identical across arms and seeds.
- Repeated evaluation of one checkpoint is bitwise-identical.
- No non-finite loss, activity, exposure, or update norm.
- Report single-seed and across-seed uncertainty; do not pool examples as if
  seeds were independent.

## Research-rule focus

Rules 1, 2, 5, and 7: validate the measurement instrument, freeze behavior
before coding, preserve exact provenance, and keep controller normalization
behind a replaceable model interface.
