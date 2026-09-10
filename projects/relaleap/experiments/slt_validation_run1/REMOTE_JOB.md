# Remote Job Record: SLT Estimator Validation Run 1

## Provider/account context
- Provider: Runpod
- Account: bengoertzel@gmail.com
- Created: 2026-07-10

## Approved resource
- GPU: 1× NVIDIA A100-SXM4-80GB (250GB RAM, 16 vCPU)
- Price: $1.49/hr on-demand
- Image: runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404
- Region: US

## Cost guardrail
- Expected duration: 4-8 hours
- Expected cost: $5.96–$11.92
- Max guardrail: 10 hours / $14.90 (auto-terminate 2026-07-11T12:00:00Z)
- Approved by: Benjamin Goertzel (2026-07-10 18:50 PDT)

## Upload plan
- Source: `projects/relaleap/worktrees/slt-integration/src/relaleap/` (3,577 lines SLT + 56K HDPC)
- Data: Tiny Shakespeare corpus (downloaded on-pod)
- Privacy: no credentials, secrets, or private data uploaded

## Task
SLT estimator validation on Tiny Shakespeare: train char-transformer (3 epochs), extract parameter blocks, run SGLD/WBIC chains per block (4 chains, 200 samples each), calibration check on product_singularity_ab2, block-wise lambda estimates with ESS and R-hat diagnostics, full JSON report.

## Source commit
- Worktree: `projects/relaleap/worktrees/slt-integration`
- Branch: `agent/slt-integration`
- Commit: `6dca8eb`

## Pod
- ID: `2ce6onegfua6nc`
- Name: `relaleap-slt-validation-run1`

## Status
- [x] Provisioned
- [x] Code uploaded
- [x] Job running
- [x] Artifacts retrieved
- [x] Pod terminated

## Completion note

2026-07-11 02:50 UTC: heartbeat follow-up found the job complete (`slt_tinyshakespeare_report.json` status `complete`), retrieved artifacts under `artifacts/`, and deleted pod `2ce6onegfua6nc` before the cost guardrail. See `RUN.md`.
