# CAROM GPT-2 low-peak schedule diagnostic

- Status: `completed; stability pass, promotion fail; artifacts verified; pod terminated`
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

## Results

The H100 run completed both arms in about 89 minutes of experiment time.

| arm/update | L2--4 acc. | L5 acc. | first-visit tau | coverage | classified frac. |
|---|---:|---:|---:|---:|---:|
| warm/start | 0.3288 | 0.2305 | 0.5898 | 0.6172 | 0.5635 |
| warm/500 | 0.3398 | 0.2422 | 0.8359 | 0.6908 | 0.6462 |
| warm/2000 (best) | 0.3535 | 0.2474 | 0.8516 | 0.6956 | 0.6500 |
| warm/3000 final | 0.3529 | 0.2396 | 0.8398 | 0.6921 | 0.6499 |
| fresh/start | 0.1354 | 0.1471 | 0.0000 | 0.1777 | 0.1237 |
| fresh/6000 final | 0.2122 | 0.1823 | 0.8750 | 0.6992 | 0.8130 |

The warm-start stability gate **passes**: final L2--4 exceeds 0.30, there are
no two consecutive declines below start minus 0.03, and final tau/classified
fraction exceed their starting values. The promotion gate **fails**: final
L2--4 is below 0.45 and L5 is below 0.25, despite a +0.0241 L2--4 improvement
and strong trajectory diagnostics. The low-peak fresh arm is stable but
underpowered, ending at only 0.2122 L2--4.

Tie-correct edge AUPRC was 0.4365 at warm start and 0.4414 final, but positive
recall at threshold 0.5 was zero throughout the warm arm. Raw edge accuracy
must not be interpreted as learned positive-edge recovery.

## Disposition

The `1e-4` warmup-cosine schedule prevents the archived effective-step-6000
collapse and preserves/improves useful step-3000 weights. This supports the
high-LR destabilization hypothesis but does not causally prove it because the
optimizer/scheduler state was reset and there was no matched high-LR rerun.
It is not an adequate fresh-training schedule and does not meet the accuracy
promotion gate.

Step 4 may use this result only as a stable warm-start schedule candidate; it
must not use `1e-4` as a fresh multi-seed schedule without another calibration.

## Retrieval and cleanup

- Retrieved complete JSON metrics, logs, frozen corpus, remote SHA manifest,
  and the state-complete warm/fresh endpoint checkpoints.
- All retrieved SHA-256 values matched the remote manifest.
- Intermediate state-complete checkpoints (653 MB total remotely) were not
  transferred because doing so would have breached the two-hour cap; their
  hashes and metrics remain in the retrieved manifest/summary.
- Pod `425j76ha3y9a4i` was deleted after verification. Running inventory and
  the task-specific all-status query were empty.
