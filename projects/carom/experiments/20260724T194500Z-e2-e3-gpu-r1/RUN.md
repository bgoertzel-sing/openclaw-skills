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
- RNG: paired model/training seeds; separate Python training stream and frozen
  evaluation corpus generator.
- Direction-free penalties: overlap 2e-4, switching/progress 2e-3, revisit
  2e-4, terminal trapping 1e-6, activity mass 2e-4.
- No term names or encodes a successor pair.

## Gates

Operational gates are finite output, exact repeated evaluation, all 25
arm/seed results present, corpus hash agreement, and complete artifact hashes.
Any non-finite output or deterministic mismatch aborts the process and triggers
immediate artifact retrieval and pod termination.

Scientific selection requires paired improvement in held-out slot/exact
accuracy and trajectory order/dwell metrics without materially increasing
integrated activity exposure. E4 remains closed unless this joint gate passes.

## Approved remote bound

See `REMOTE_JOB.md`. Exact invocation is frozen in `command.sh`.

## Results

Pending.

