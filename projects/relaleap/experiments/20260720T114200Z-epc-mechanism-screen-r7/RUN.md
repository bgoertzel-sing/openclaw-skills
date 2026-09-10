# RUN: ePC Mechanism Screen (r7)

**Experiment ID:** `20260720T114200Z-epc-mechanism-screen-r7`
**Status:** complete; artifacts retrieved and pod deleted
**Pod provisioned:** 2026-07-20 04:46 PDT
**GPU:** A100 SXM4 80GB (Secure Cloud)
**Rate:** $1.49/hr
**Image:** `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
**SSH:** `root@154.54.102.45 -p 10426`
**SSH key:** `/home/openclaw/.runpod/ssh/runpodctl-ssh-key`
**Created:** 2026-07-20 04:44 PDT
**Approved by:** Ben Goertzel (Telegram, 2026-07-20 04:42 PDT)
**Cost bound:** USD 10.00 maximum incremental spend

## Objective

Rerun of the r6 mechanism screen with the crash fix (commit `e50ed24`).
The r6 run completed only `bp_ce` and `bp_kd` before crashing on the first
ePC arm. The fix removes a `del student_template` from inside the arm loop
and adds traceback logging. This run should complete all five arms.

## Arms

| Arm | Description |
|---|---|
| `bp_ce` | BP with cross-entropy only |
| `bp_kd` | Update-matched BP with KD (T=2, CE/KD weights 0.5/0.5) |
| `epc_original` | ePC with historical config (T=4, lambda=0.05, steps=4, step_size=0.2) |
| `epc_calibrated` | ePC with deeper inference (T=12, lambda=0.05, steps=12) |
| `bp_kd_wallclock` | Wall-clock-matched BP with KD |

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
- Source commit: `e50ed24` (branch `agent/epc-outcome-probes`)

## Checkpoints

Updates: 0, 1, 10, 50, 100, 200

## Remote job

- Provider: RunPod
- Account: bengoertzel@gmail.com
- GPU: 1× A100 SXM 80GB Secure Cloud
- Price: $1.49/hour
- Expected duration: ~4 hours (5 arms × ~200 updates each, ePC ~4× slower)
- Hard time limit: 7 hours
- Hard cost cap: $10.00
- Image: runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404
- Storage: no persistent volume
- Data classification: public (GPT-2, WikiText-103)
- Stop/terminate: terminate after artifact retrieval
- Artifact return path: `projects/relaleap/experiments/20260720T114200Z-epc-mechanism-screen-r7/artifacts/`

## Stop conditions

- Non-finite loss
- Cost approaching $10 cap
- Pod unresponsive for >15 minutes
- Completion of all 5 arms with artifact retrieval

## r6 → r7 fix

Commit `e50ed24` on branch `agent/epc-outcome-probes`:
- Removed `del student_template` from inside the arm loop (was causing
  `NameError` on second ePC arm).
- Removed redundant `GPT2BlockStateAdapter(student)` instantiations.
- Added `try/except` with `traceback.format_exc()` and `{arm}_ERROR.txt`
  output so any future crash preserves the traceback.
- `del student_init, student_template` moved before the arm loop.

## Live status

- `bp_ce`: completed (exit 0)
- `bp_kd`: completed (exit 0)
- `epc_original`: running (update 20+ as of 04:50 PDT)

## Final retrieval and cleanup

- All five arm JSON files, summary JSON, and the full log were retrieved to
  `artifacts/`; the summary parses and lists all five arms.
- Final validation losses: BP-CE 8.4390; BP-KD 7.6278; ePC-original 7.5672;
  ePC-calibrated 7.5836; BP-KD-wallclock 7.6278.
- Pod `s0zct9nfbax0b1` was deleted after artifact verification on 2026-07-20.
