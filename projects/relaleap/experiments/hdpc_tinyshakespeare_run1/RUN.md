# HDPC/ePC Tiny Shakespeare Run 1

## Date
2026-07-10 12:20-12:26 PDT

## Provider
Runpod, account bengoertzel@gmail.com

## Resource
- Pod ID: `06ufjerd1zjvey` (terminated)
- GPU: 1× NVIDIA RTX 4090 (25.3 GB VRAM)
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Cost: $0.69/hr (includes disk/volume)
- Actual runtime: ~6 minutes
- Actual cost: ~$0.07

## Source commit
- Worktree: `projects/relaleap/worktrees/tinyshakespeare-hdpc`
- Branch: `agent/tinyshakespeare-hdpc`
- Commit: `fc5efa9`

## Config
- epochs=2, steps_per_epoch=50, batch_size=64
- d_model=128, nhead=4, d_ff=512, num_layers=4, seq_len=128
- learning_rate=3e-4, lambda_kd=0.05, temperatures=(1,2,4,8)
- seed=1234

## Results
- Teacher parameters: 826,433
- Student parameters: 835,013 (crown adds 8,580)
- Teacher perplexity: 10.75
- Student perplexity: 11.46
- Perplexity delta: +0.71 (student slightly worse, expected since crown is identity-initialized and barely trained)
- Energy profile: 400 steps recorded
- Update sparsity histogram (zero/tiny/small/large): (21, 1078, 686677, 147237)
- Gradient diagnostics: 58 parameter groups, BP vs PC gradient cosine similarities mostly 0.4-0.88

## Interpretation
- First GPU run of HDPC/ePC pipeline on Tiny Shakespeare. Pipeline executes end-to-end on CUDA without errors.
- Teacher and student are structurally identical at init (student backbone = teacher weights); perplexity gap reflects minimal crown training, not a mechanism failure.
- PC gradients are systematically larger than BP gradients (consistent with ePC scaling), and cosine similarities are positive across all layers (0.40-0.88), indicating PC gradients are directionally aligned with BP gradients.
- This is a smoke/feasibility run, not evidence of HDPC efficacy. Longer training with coupled crown is needed.

## Artifacts
- `artifacts/hdpc_tinyshakespeare/hdpc_tinyshakespeare_smoke.pt` (6.7 MB, model checkpoint)
- `artifacts/hdpc_tinyshakespeare/summary.json` (14 KB, full metrics + gradient diagnostics)
- `run_gpu.py` (runner script)

## Cleanup
- Pod terminated, no persistent storage retained.
- Verified: `runpodctl pod list` shows no active pods.

## Exit status: 0 (success)
