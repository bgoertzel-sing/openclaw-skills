# Remote Job Record: HDPC/ePC Tiny Shakespeare Run 2 (Non-Smoke)

## Provider/account context
- Provider: Runpod
- Account: bengoertzel@gmail.com
- Created: 2026-07-10

## Approved resource
- GPU: 1× NVIDIA RTX A6000 (48GB VRAM, 18 vCPU) — RTX 4090 unavailable
- Price: $0.49/hr on-demand
- Image: runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404
- Region: US

## Cost guardrail
- Expected duration: 2-4 hours
- Expected cost: $0.98–$1.96
- Max guardrail: 6 hours / $2.94 (auto-terminate 2026-07-11T04:00:00Z)
- Approved by: Benjamin Goertzel (2026-07-10 18:50 PDT)

## Upload plan
- Source: `projects/relaleap/worktrees/tinyshakespeare-hdpc/src/relaleap/hdpc/` + tests
- Data: Tiny Shakespeare corpus (downloaded on-pod)
- Privacy: no credentials, secrets, or private data uploaded

## Task
Non-smoke HDPC/ePC training: 5 epochs, 200 steps/epoch, batch=128, d_model=256, 4 heads, 6 layers, d_ff=1024, seq_len=256. Full homotopy KD with λ=0.05, T={1,2,4,8}. PC-gradient/BP-gradient diagnostics, held-out perplexity, energy profiles, update sparsity, detached crown.

## Source commit
- Worktree: `projects/relaleap/worktrees/tinyshakespeare-hdpc`
- Branch: `agent/tinyshakespeare-hdpc`
- Commit: `fc5efa9`

## Pod
- ID: `j0xlf52ahsoqa7`
- Name: `relaleap-hdpc-ts-run2`

## Status
- [x] Provisioned
- [x] Code uploaded
- [x] Job running
- [x] Artifacts retrieved
- [x] Pod terminated

## Completion note

2026-07-11 02:52 UTC: heartbeat follow-up found the job complete/idle, retrieved artifacts under `hdpc_tinyshakespeare_run2/artifacts/`, and deleted pod `j0xlf52ahsoqa7` before the 04:00Z cost guardrail. `runpodctl pod list` returned no remaining pods after cleanup. See `hdpc_tinyshakespeare_run2/RUN.md`.
