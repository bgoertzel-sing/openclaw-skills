# CAROM GPT-2 piecewise schedule experiment

- Status: `invalidated during execution; stopped; pod terminated`
- Run-record ID: `20260726T100000Z-gpt2-piecewise-schedule`
- Actual remote start: `2026-07-26T02:35:49Z`
- Project: `carom`

## Execution disposition

The approved H100 attempt started at `2026-07-26T02:35:49Z` on RunPod pod
`xyaed6b5s9q99g` and was stopped at approximately `2026-07-26T02:48:00Z`
after a protocol-invalid learning-rate trace was observed. The pod was
deleted after all partial artifacts were retrieved and hash-verified. The
final inventory query returned `[]`.

This attempt is **not a scientific result** and no frozen endpoint gate is
evaluable. A corrected runner and new approval are required before rerunning.

## Observations

- Local preflight: `python3 -m pytest test_gpt2_piecewise_schedule.py -v`
  passed all 12 tests in 33.56 seconds.
- Allocation: one H100 SXM 80 GB in Canada, USD 2.99/hour, 50 GB container
  disk, no persistent/network volume, SSH only.
- The remote process produced the frozen corpus plus piecewise checkpoints at
  updates 0, 500, and 1000. The logged optimizer learning rates were
  `2.6667e-8`, `3.8602e-6`, and `3.2247e-6`, respectively.
- The preregistration requires a phase-1 peak learning rate of `2e-3`, but the
  maximum possible optimizer rate in the implementation is `4e-6`.
- The implementation evaluates every 500 updates, while the frozen protocol
  specifies every 1000 updates.
- All 13 retrieved partial evidence files passed
  `sha256sum -c remote_sha256_manifest.txt`.
- The run used about 12.8 wall minutes. At USD 2.99/hour, the estimated
  compute charge is approximately USD 0.64; provider billing detail had not
  populated immediately after deletion.

## Cause

Direct code inspection shows that `piecewise_lr()` and
`original_onecycle_lr()` return absolute learning rates, but their return
values are supplied to `torch.optim.lr_scheduler.LambdaLR`. `LambdaLR`
interprets the function value as a multiplier on the optimizer base learning
rate (`2e-3`). Thus an intended `2e-3` peak becomes `2e-3 × 2e-3 = 4e-6`.
The unit tests validate the schedule functions in isolation and do not test
the optimizer's realized learning rate. Separately, `main()` sets
`eval_interval = 500`.

## Interpretation

- **Inference:** Continuing would have tested a roughly 500-fold lower
  learning-rate schedule with twice the preregistered evaluation cadence, not
  the approved piecewise-vs-OneCycle comparison.
- **Hypothesis:** An optimizer-level schedule test that asserts realized
  rates at warmup peak, phase boundary, and final update would have caught
  this defect before provisioning.
- **Remaining uncertainty:** No conclusion can be drawn about stability,
  promotion, or schedule superiority from the partial metrics.

## Frozen-gate disposition

- Operational: **FAIL / incomplete** (intentional stop; only three partial
  checkpoints from one arm; no `summary.json`).
- Stability: **not evaluable**.
- Promotion: **not evaluable**.
- Schedule comparison: **not evaluable**.

## Reproduction evidence

- Exact approved source: commit `14cbb91`.
- Remote command: `command.sh`.
- Environment and source hashes: `artifacts/env.txt`, `artifacts/git.txt`.
- Raw partial logs and checkpoints: `artifacts/`.
- Verification:
  `cd artifacts && sha256sum -c remote_sha256_manifest.txt`
  (13/13 `OK`).

## Question

Does a piecewise learning rate schedule — high LR (peak 2e-3) for the first
3,000 updates followed by low LR (peak 1e-4) for the remaining 9,000 — achieve
higher final accuracy than the original OneCycleLR (peak 2e-3 over 12,000)
without the collapse observed in the archived run?

## Motivation

- The archived 12k run peaked at L2-4 0.3268 at step 3000, then collapsed to
  0.1888 by step 12000. OneCycleLR peak occurred near step 3600.
- The low-peak diagnostic (peak 1e-4) was stable but underpowered for fresh
  training (L2-4 0.2122 at 6000 updates).
- The warm-start diagnostic confirmed that 1e-4 maintains and slightly improves
  step-3000 weights (L2-4 0.3288 → 0.3529 over 3000 updates).
- Hypothesis: the high LR is needed for fast learning in phase 1, and the low
  LR is needed for stable consolidation in phase 2.

## Frozen protocol

- Seed: 0.
- Frozen base: GPT-2-small, 124M parameters, final hidden layer, width 768.
- CAROM architecture/losses: unchanged from the 12k run.
- Two arms:
  1. **Piecewise**: Phase 1 (0-3000): peak LR 2e-3, 5% linear warmup, cosine
     decay from 2e-3 to 1e-4. Phase 2 (3000-12000): cosine decay from 1e-4 to
     1e-5, no warmup.
  2. **OneCycleLR control**: peak LR 2e-3, 5% warmup, cosine decay to 2e-4
     over 12,000 updates (replicates the original schedule).
- Batch size: 64.
- AdamW weight decay: 1e-4. Gradient clip: 1.0.
- Checkpoints/evaluation every 1,000 updates on frozen validation corpora:
  L2-4 (n=256, seed 20260726) and L5 (n=128).
- Every checkpoint preserves model, optimizer, scheduler, Python/Torch/CUDA
  RNG state, config, and SHA-256.
- Measurements: L2-4 and L5 task accuracy, tie-correct edge metrics,
  full dwell-collapsed itinerary metrics including first-visit tau,
  dominance/classified fraction, coverage, and elapsed time.

## Frozen diagnostic gates

- Operational: finite values, all 13 planned checkpoints (0, 1000, ...,
  12000), frozen corpus hash, checkpoint hashes, and artifact manifest.
- Stability: piecewise arm final L2-4 accuracy ≥ 0.30; no two consecutive
  evaluations more than 0.05 below the peak L2-4 accuracy.
- Promotion: piecewise final L2-4 ≥ 0.40 (improvement over archived 0.3268
  peak and 0.1888 final); L5 ≥ 0.25; piecewise final tau ≥ 0.50.
- Schedule comparison: piecewise final L2-4 exceeds OneCycleLR control final
  L2-4 by at least 0.05.

## Interpretation boundaries

- The piecewise arm tests whether combining the proven fast-learning phase
  with the proven stable phase avoids collapse. It is a clean within-run
  comparison because both arms share initialization, data, and evaluation.
- The OneCycleLR control arm replicates the original schedule but with the
  repaired instruments and frozen corpora, providing a contemporaneous
  baseline rather than relying on the archived run's metrics.
- If the piecewise arm collapses too, the problem is not solely LR schedule
  but something structural (e.g., Layer 5 weight explosion).

## Evidence

- Runner: `repos/carom/run_carom_gpt2_piecewise_schedule.py`
- Tests: `repos/carom/test_gpt2_piecewise_schedule.py` (12 passed)
- Commit: `14cbb91` on `agent/conversation-governor`
- Exact remote command: `command.sh`.
