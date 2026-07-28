# Run 20260724T194500Z-e2-e3-gpu-r1

- Project: `carom`
- Started: `2026-07-24T19:45:00Z`
- Status: `preregistered`
- Local or remote: `RunPod Secure Cloud`
- Working directory: `/workspace/carom-e2-e3`

## Question

Do mode-specific E2 fitness and generic direction-free E3 regularization improve
held-out accuracy and order/dwell trajectories across five paired seeds,
without excess total exposure or successor-pair encoding?

## Frozen protocol

- Arms: E2 full; no-workspace, no-command, and no-position feature ablations;
  E3 generic regularization applied to E2 full.
- Seeds: 7, 17, 27, 37, 47.
- Fixed evaluation corpus: 2,048 examples generated with evaluation seed
  20260720 and shared across all arms/seeds.
- Training: 3,000 updates, batch 128, AdamW, maximum OneCycleLR 0.002,
  `d=64`, `K=16`, 70 controller steps, training noise 0.02.
- Evaluation: deterministic, batch 256, repeated exactly per arm/seed.
- CUDA determinism: deterministic PyTorch algorithms with
  `CUBLAS_WORKSPACE_CONFIG=:4096:8`.
- RNG: paired model/training seeds; separate Python training stream and frozen
  evaluation corpus generator.
- Direction-free penalties: overlap 2e-4, switching/progress 2e-3, revisit
  2e-4, terminal trapping 1e-6, activity mass 2e-4.
- No term names or encodes a successor pair.

## Frozen numerical gates (amended before r2 provisioning)

The original qualitative scientific selection language was insufficient for a
five-seed GPU disposition.  The following thresholds are frozen prospectively
for r2; they do not alter the executable, seeds, corpus, or model settings.

- **E2 feature gate:** `e2_full` must exceed *each* of the three feature
  ablations by at least `0.010` in mean held-out slot accuracy, and the paired
  difference must be non-negative on at least 4/5 seeds for each ablation.
- **E3 safety/trajectory gate:** `e3_generic_regularized` must lose no more
  than `0.010` mean slot accuracy versus `e2_full`; its mean terminal-trapping
  fraction and mean revisit fraction must each be no greater than `e2_full`;
  and its mean integrated activity mass must be at most `1.10 × e2_full`.
- **Disposition:** E4 opens only if both gates pass.  Otherwise this is a
  bounded negative/diagnostic result, with the raw paired values retained.

## Gates

Operational gates are finite output, exact repeated evaluation, all 25
arm/seed results present, corpus hash agreement, and complete artifact hashes.
Any non-finite output or deterministic mismatch aborts the process and triggers
immediate artifact retrieval and pod termination.

Scientific selection applies the frozen numerical gates above. E4 remains
closed unless this joint gate passes.

## Approved remote bound

See `REMOTE_JOB.md`. Exact invocation is frozen in `command.sh`.

## Results

No scientific result was produced. Two boot-stuck RTX 4090 allocations were
deleted before execution. An A40 attempt ran the first arm for more than 17.5
minutes without completing, projecting beyond its provider deadline. An H100
SXM attempt then ran the identical first arm for more than 10.8 minutes without
completion. With 25 arm/seed combinations, the observed H100 lower-bound
projects beyond 4.5 hours and USD 13.45 at USD 2.99/hour, exceeding Ben's
USD 10 approval.

Both partial logs were retrieved and both pods terminated. Because neither
attempt completed even one arm, no endpoint or scientific comparison is
reported. The bottleneck is the 70-step Python recurrence over small GPU
kernels; a full run needs either a separately validated compiled/vectorized
runner or a larger explicit compute bound.
