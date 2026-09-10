# SLT Large Validation Run 1 — Remote Job Record

## Status: COMPLETE / TERMINATED

## Pod Details
- Pod ID: `pmqngq3cxcd5bw`
- GPU: A100 SXM (80GB)
- Cost: $1.49/hr
- SSH: `ssh -i ~/.runpod/ssh/runpodctl-ssh-key root@195.26.233.28 -p 37166`
- Started: 2026-07-11 16:59 UTC
- Auto-terminate: 2026-07-12T03:00:00Z

## Approval

- Approved by Benjamin Goertzel: 2026-07-11 09:51 PDT
- Approval scope: both R1 (HDPC grid v2) and R2 (SLT large run) in parallel, speed over cost

## Resource

- Provider: Runpod, bengoertzel@gmail.com
- Pod: pmqngq3cxcd5bw
- GPU: 1× A100-SXM4-80GB
- Price: ~$1.50/hr planning
- Image: runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404
- Storage: 50GB container disk + 50GB volume

## Source

- Repo: projects/relaleap/worktrees/slt-integration
- Branch: agent/slt-integration
- Commit: 52f5171

## Guardrail

- Hard cap: 16h / $24 compute
- Auto-terminate: 2026-07-12T03:00:00Z

## Command

```bash
cd /workspace/relaleap && PYTHONPATH=src python3 scripts/run_slt_tinyshakespeare.py \
  --device cuda --epochs 3 --n_chains 8 --n_samples 1000
```

## Justification

Previous run (4 chains × 200 samples) had R-hat 1.7-2.1 and ESS 2-12 — not converged.
This run uses 8 chains × 1000 samples (10× more) to target R-hat < 1.1 and ESS > 200.

## Cleanup

- Retrieve artifacts to projects/relaleap/experiments/slt_large_run1/artifacts/
- Verify report JSON parseability and diagnostics
- Terminate pod

## Completion note

2026-07-11 19:06 UTC heartbeat found the pod complete/idle with `slt_tinyshakespeare_report.json` present. Retrieved artifacts to `projects/relaleap/experiments/slt_large_run1/artifacts/`, verified JSON (`status=complete`, `device=cuda`, `epochs=3`, `n_chains=8`, `n_samples=1000`, `elapsed_seconds=3978.46`), and deleted pod `pmqngq3cxcd5bw` at 19:09 UTC. `runpodctl pod list` returned `[]`. See `RUN.md`.
