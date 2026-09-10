# RUN: ePC Mechanism Screen (r6)

**Experiment ID:** `20260719T202100Z-epc-mechanism-screen-r6`
**Status:** failed; partial artifacts retrieved; pod deleted
**Pod ID:** `oq7laxlq83hqol`
**Pod provisioned:** 2026-07-19 20:23 PDT
**GPU:** A100 SXM4 80GB (Secure Cloud)
**Rate:** $1.49/hr
**Image:** `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
**Created:** 2026-07-19 20:21 PDT
**Approved by:** Ben Goertzel (Telegram, 2026-07-19 20:21 PDT)
**Cost bound:** USD 10.00 maximum incremental spend

## Objective

One-seed (3253) 200-update mechanism screen to determine whether ePC
representation collapse (rank loss) precedes or follows last-layer weight
norm growth, and to measure clipping/Adam/update dynamics across arms.

This is the Fable/Sol-recommended experiment B from the 2026-07-19
diagnostic battery, preceding any larger three-seed decisive run.

## Arms

| Arm | Description |
|---|---|
| `bp_ce` | BP with cross-entropy only |
| `bp_kd` | Update-matched BP with KD (T=2, CE/KD weights 0.5/0.5) |
| `epc_original` | ePC with historical config (T=4, lambda=0.05, steps=4, step_size=0.2) |
| `epc_calibrated` | ePC with deeper inference (T=12, lambda=0.05, steps=12) |
| `bp_kd_wallclock` | Wall-clock-matched BP with KD |

## Checkpoints

Updates: 0, 1, 10, 50, 100, 200

## Per-update telemetry

- Loss
- Pre-clip and post-clip gradient norm
- Clip fraction (fraction of params clipped)
- Adam m/v L2 norms
- Update/weight ratio (Adam step L2 / param L2)
- Elapsed seconds

## Configuration

- Seed: 3253
- Updates: 200
- Context length: 256
- Micro batch: 4, gradient accumulation: 8 (effective batch 32)
- Optimizer: AdamW, lr=1e-4, wd=0.01, warmup=50
- Gradient clip: 1.0
- Precision: bf16
- KD temperature: 2.0, CE/KD weights: 0.5/0.5
- Student: GPT-2 6-layer (d=768, 12 heads, d_ff=3072)
- Teacher: GPT-2 12-layer (openai-community/gpt2)
- Dataset: WikiText-103-raw-v1 (200 train documents, 64 eval segments)
- Source commit: `f73add7`

## Remote job

- Provider: RunPod
- Account: bengoertzel@gmail.com
- GPU: 1× A100 SXM 80GB Secure Cloud
- Price: $1.49/hour
- Expected duration: ~4 hours (5 arms × ~200 updates each, ePC ~4× slower)
- Hard time limit: 7 hours
- Hard cost cap: $10.00
- Image: runpod/pytorch:2.1.0-cuda12.1.1-devel-ubuntu22.4
- Storage: no persistent volume
- Data classification: public (GPT-2, WikiText-103)
- Stop/terminate: terminate after artifact retrieval
- Artifact return path: `projects/relaleap/experiments/20260719T202100Z-epc-mechanism-screen-r6/artifacts/`

## Stop conditions

- Non-finite loss
- Cost approaching $10 cap
- Pod unresponsive for >15 minutes
- Completion of all 5 arms with artifact retrieval

## Result and cleanup

- **Observed:** the process exited with code 1 after completing only `bp_ce`
  and `bp_kd`; no ePC arm or wall-clock control result was produced. This is
  not a completed ePC mechanism screen and supports no ePC conclusion.
- The launcher retained only `EXIT_CODE=1` in `mechanism_screen.log`, so the
  immediate exception was not preserved. Root cause is therefore unknown.
- Both completed JSON records parse successfully and contain 200 telemetry
  rows plus checkpoint metadata at updates 0, 1, 10, 50, 100, and 200.
- `bp_ce`: final validation loss 8.439046; elapsed 67.17 seconds.
- `bp_kd`: final validation loss 7.627799; elapsed 68.99 seconds.
- Artifact SHA-256:
  - `bp_ce.json`: `d2d8563e824110db73614516026b3d9620e7244f856bdfded20b3e2ba1192e0e`
  - `bp_kd.json`: `de9d5e199a13fc08b7463729c83ac665ab739f196ca0a9101370e9c2b8e02dbc`
  - `mechanism_screen.log`: `0aac2256ca135e9e2ce682d26e680d8ec767e0c2897215d636113386fbc768af`
- The interrupted local checkpoint transfer was removed because it was
  incomplete; the verified JSON telemetry was retained.
- Pod `oq7laxlq83hqol` was deleted at 2026-07-19 23:10 PDT. A subsequent
  `runpodctl pod list -o json` returned `[]`.
- Approximate upper-bound pod-lifetime cost is USD 5.62 (3.77 hours at
  USD 1.49/hour), before provider rounding; the provider invoice was not read.

## Open loop

Before any rerun, reproduce or expose the first ePC-arm failure locally or in
a same-process smoke, and repair logging so Python's exit status and stderr are
preserved (including pipeline failure via `pipefail`). A new paid resource
requires a fresh bounded approval.

## Evidence to collect

- Per-arm JSON with per-update metrics
- Intermediate checkpoints (6 per arm × 5 arms = 30 checkpoints)
- Summary JSON
- Stdout/stderr logs
- `nvidia-smi` output
- Python/torch/transformers versions
