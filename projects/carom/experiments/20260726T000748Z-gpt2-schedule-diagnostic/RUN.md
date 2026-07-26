# CAROM GPT-2 low-peak schedule diagnostic

- Status: `preregistered; local implementation complete; awaiting paid-compute approval`
- Started: `2026-07-26T00:07:48Z`
- Project: `carom`

## Question

Does a peak learning rate of `1e-4`, with short linear warmup and cosine decay,
avoid the endpoint and itinerary collapse observed near the original
OneCycleLR peak of `2e-3`?

## Interpretation boundary

The retained `step_3000.pt` contains model weights and Python batch-generator
state, but no AdamW or scheduler state. The warm arm therefore resets the
optimizer and is a **warm start, not an exact continuation**. It can establish
whether useful step-3000 weights can be maintained or improved under a
conservative schedule. The matched fresh arm describes learning under the same
normalized low-peak schedule but does not alone causally isolate LR from
optimizer-state reset.

## Frozen protocol

- Seed: 0.
- Frozen GPT-2-small final-layer span adapter.
- Warm arm: step-3000 weights and saved Python RNG; reset AdamW; 3,000 updates.
- Fresh arm: seed-0 initialization; reset AdamW; 6,000 updates.
- Both: batch 64, AdamW weight decay `1e-4`, clip 1.0, peak LR `1e-4`,
  5% linear warmup then cosine decay to `1e-5`.
- Checkpoints/evaluation every 500 updates on CPU-canonical frozen validation
  corpora: L2--4 seed 20260726 (`n=256`) and L5 (`n=128`).
- Every checkpoint preserves model, optimizer, scheduler, Python/Torch/CUDA
  RNG state, config, and SHA-256.
- Measurements: L2--4 and L5 task accuracy, tie-correct edge metrics,
  full dwell-collapsed itinerary metrics including first-visit tau,
  dominance/classified fraction, and elapsed time.

## Frozen diagnostic gates

- Operational: finite values, all planned checkpoints, frozen corpus hash,
  checkpoint hashes, and artifact manifest.
- Warm-start stability: final L2--4 accuracy at least `0.30`, no two
  consecutive post-start evaluations more than `0.03` below the starting
  accuracy, and final classified fraction/tau no more than `0.10` below start.
- Promotion: L2--4 accuracy at least `0.45`, improvement over the starting
  checkpoint, L5 accuracy at least `0.25`, and no material itinerary decline.
- LR-destabilization support: the warm arm avoids the historical collapse by
  effective update 6,000 while the archived original schedule does not.
  This is supportive, not a clean matched causal contrast.

## Evidence

- Runner: `repos/carom/run_carom_gpt2_schedule_diagnostic.py`
- Tests: `repos/carom/test_gpt2_schedule_diagnostic.py`,
  repaired harness constructed controls.
- Exact remote command will be frozen in `command.sh`.
