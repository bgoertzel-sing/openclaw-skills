# Remote Job Record: HDPC/ePC Tiny Shakespeare Run 1

## Provider/account context
- Provider: Runpod
- Account: bengoertzel@gmail.com
- Created: 2026-07-10

## Approved resource
- GPU: 1× NVIDIA RTX 4090 (31GB VRAM, 8 vCPU)
- Price: $0.34/hr on-demand
- Image: runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404 (or equivalent PyTorch 2.x CUDA 12.x)
- Region: best available

## Cost guardrail
- Expected duration: 4-6 hours
- Expected cost: $1.36–$2.04
- Max guardrail: 8 hours / $2.72
- Approved by: Benjamin Goertzel (2026-07-10 12:20 PDT)

## Upload plan
- Source: `projects/relaleap/worktrees/tinyshakespeare-hdpc/src/relaleap/hdpc/` + `tests/test_hdpc*`
- Data: Tiny Shakespeare corpus (downloaded on-pod from public source, no local upload needed)
- Privacy: no credentials, secrets, or private data uploaded

## Task
Train tiny BP char-transformer teacher on Tiny Shakespeare, run student=teacher homotopy KD with λ=0.05 and T={1,2,4,8}, PC-gradient/BP-gradient diagnostics, held-out perplexity delta, energy profiles, update-sparsity histograms, detached crown.

## Artifact return
- Destination: `projects/relaleap/experiments/hdpc_tinyshakespeare_run1/`
- Contents: metrics JSON, loss curves, energy profiles, gradient diagnostics, smoke test results

## Stop/terminate
- Terminate pod after artifacts retrieved
- No persistent storage needed

## Source commit
- Worktree: `projects/relaleap/worktrees/tinyshakespeare-hdpc`
- Branch: `agent/tinyshakespeare-hdpc`
- Commit: `fc5efa9`

## Status
- [x] Provisioned
- [x] Code uploaded
- [x] Job running
- [x] Artifacts retrieved
- [x] Pod terminated
