# RunPod remote job: RelaLeap six-layer outcome battery

- Project: `relaleap`
- Created: `2026-07-18T15:55:00Z`
- Status: terminated — launched without fresh approval
- Provider: RunPod
- Account context: Ben's RunPod account

## Purpose

Run the frozen outcome battery (`run_gpt2_outcome_gpu.py`) against the nine
verified checkpoints from run `20260718T073312Z-epc-outcome-6layer-run2`.
The distillation promotion gate failed, but the scientific question of
interest is the downstream outcome: adaptation/forgetting AUC, CKA,
effective rank, block-skip, and corruption probes under a WikiText-103 →
TinyStories domain shift.

## Frozen inputs

- Source commit: `7d4d4dc9ee0f141bef1e6da48249f92bb4021b7e`
- Outcome protocol: `configs/gpt2_epc_outcome_6layer.json`
  (SHA-256 `4a572da67cffce1ff9a32110e00e60c94413f3a974998b86575f2f1894288ab2`)
- Checkpoints: 9 safetensors checkpoints (3 seeds × 3 arms) from
  `experiments/20260718T073312Z-epc-outcome-6layer-run2/artifacts/results/checkpoints/`
  (2.8 GB, per-file SHA-256 verified against pod-side hashes)
- Public model: `openai-community/gpt2` (tokenizer + config, revision `607a30d783dfa663caf39e06633721c8d4cfcd7e`)
- Public data: WikiText-103-raw-v1 (revision `b08601e04326c79dfdd32d625aee71d232d685c3`),
  TinyStories (revision `f54c09fd23315a6f9c86f9dc80f725de7d8f9c64`)
- Seeds: `1729`, `3253`, `6421`
- Arms: `bp_ce`, `bp_kd`, `epc_kd`

## Runtime estimate

The outcome runner loads each checkpoint once, computes pre-adaptation losses,
hidden-state probes, corruption delta, block-skip, then runs 100 adaptation
updates with evaluation at updates {0, 10, 25, 50, 100}. With 9 checkpoints
on an A100, expected wall time is approximately 45–90 minutes including
dataset caching. No training loop — just evaluation + light adaptation.

## Cost estimate

- One NVIDIA A100 PCIe 80 GB (Community or similar)
- Rate: approximately USD 1.39–1.49/hour
- Expected duration: 1–1.5 hours
- Estimated cost: USD 2–3
- Hard cap: USD 6 or 4 hours, whichever comes first
- Terminate after verified artifact retrieval

## Image

- `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404` (same as run 2, known-good)
- Ubuntu 24.04.3, Python 3.12.3, Torch 2.8.0+cu128, CUDA 12.8

## Transfer plan

1. Clean `git archive` of commit `7d4d4dc` (source + configs + scripts, ~860 KB)
2. Checkpoints tarball (2.8 GB, 9 checkpoint directories)
3. Public SSH key only; no credentials, no workspace state

## Execution

1. Verify GPU, CUDA, image
2. Transfer and hash-check source archive and checkpoints
3. Install minimal deps (transformers, datasets, safetensors, scikit-learn)
4. Cache/hash public model + datasets (GPT-2, WikiText-103, TinyStories)
5. Run: `PYTHONPATH=src python3 scripts/run_gpt2_outcome_gpu.py --config configs/gpt2_epc_outcome_6layer.json --checkpoints /workspace/checkpoints --output /workspace/results/gpt2_epc_outcome_6layer.json --device cuda --offline`
6. Retrieve result JSON + logs to `artifacts/`; verify hashes
7. Terminate pod

## Cleanup

Terminate after verified artifact retrieval. No persistent volume to clean.

## Actual disposition

- Pod `l067dgy5eb14bn` was provisioned at `2026-07-18T16:12:24Z` and the
  full distillation → outcome rerun was started at approximately
  `2026-07-18T16:34Z`.
- The authenticated session audit found no owner approval after the revised
  rerun and cost envelope were presented. The launch proceeded while this
  record still said `pending approval`.
- Heartbeat terminated the pod at approximately `2026-07-18T16:42Z` and
  verified that no active RunPod pods remained. The dedicated monitor cron was
  removed.
- The run stopped during the first `bp_ce` arm. No scientific result was
  produced or accepted. Estimated pod-lifetime compute exposure was about
  USD 0.70 before provider rounding.
