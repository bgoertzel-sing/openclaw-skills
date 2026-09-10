# CAROM compiled-channel GPT-2 multi-seed protocol

Status: blocked pending the Step-2 stable-schedule evidence and explicit paid
compute approval.

## Preconditions

1. Step 2 meets its warm-start stability gate and identifies a schedule that
   does not collapse by effective update 6,000.
2. The repaired v2/v3 constructed controls pass on the execution environment.
3. The frozen corpora, GPT-2 layer/tokenizer/span adapter, checkpoint format,
   and all numerical gates are hash-recorded before training.

## Proposed confirmation

- Seeds 0, 1, 2; frozen GPT-2-small final-layer span adapter.
- Stable Step-2 schedule; batch 64; matched update and evaluation cadence.
- L2--4 training; untouched L5 structural holdout.
- CPU-canonical paired validation/test corpora, evaluated once per checkpoint.
- Repaired endpoints: task/exact-workspace accuracy, example-paired bootstrap
  intervals, tie-correct edge AUROC/AUPRC and prevalence baselines, complete
  dwell-collapsed itinerary order, classified fraction, exposure/activity/
  workspace-update norms, forced-versus-shuffled matched trajectory contrast,
  and descriptive v3 swap/JVP/switching/coupling panel.

## Frozen promotion gates

- Mean L2--4 task accuracy at least 0.50 and no seed below 0.40.
- Mean L5 accuracy at least 0.30 and at least 0.03 above the matched fresh
  schedule control.
- Median classified itinerary coverage at least 0.70 and first-visit tau at
  least 0.70.
- Median forced-minus-shuffled accuracy at least 0.03 with an example-paired
  95% bootstrap interval excluding zero.
- No arm exceeds its matched control by more than 10% in integrated activity
  mass or workspace-update norm.

Small swap/JVP values are reported as sampled local/nonlinear measurements,
not proof of global commutation. Sampled product growth below one is not a
stability proof. The experiment is positive only if all accuracy,
generalization, trajectory, and exposure gates pass.

## Cost boundary

Prepare a separate `REMOTE_JOB.md` only after Step 2 reports measured H100
throughput. The remaining overall CAROM authorization cannot be inferred to
cover this confirmation; provision only after explicit approval of its exact
resource, duration, and hard cost cap.
