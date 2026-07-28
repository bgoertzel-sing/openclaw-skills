# HDPC/ePC Extended Grid V2 — Remote Job Record

## Status: FAILED / TERMINATED

## Pod Details
- Pod ID: `tb09sv8ocb8qgv`
- GPU: L40S (48GB)
- Cost: $0.99/hr
- SSH: `ssh -i ~/.runpod/ssh/runpodctl-ssh-key root@64.247.206.229 -p 18870`
- Started: 2026-07-11 16:59 UTC
- Auto-terminate: 2026-07-12T00:00:00Z

## Approval

- Approved by Benjamin Goertzel: 2026-07-11 09:51 PDT
- Approval scope: both R1 (HDPC grid v2) and R2 (SLT large run) in parallel, speed over cost

## Resource

- Provider: Runpod, bengoertzel@gmail.com
- Pod: tb09sv8ocb8qgv
- GPU: 1× L40S (48GB)
- Price: $0.99/hr
- Image: runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404
- Storage: 50GB container disk + 20GB volume

## Source

- Repo: projects/relaleap/worktrees/tinyshakespeare-hdpc
- Branch: agent/tinyshakespeare-hdpc
- Commit: 0803a37

## Guardrail

- Hard cap: 12h / $6 compute
- Auto-terminate: 2026-07-12T00:00:00Z

## Command

```bash
cd /workspace/relaleap && PYTHONPATH=src python3 scripts/run_grid_v2.py \
  --device cuda --epochs 5 --steps-per-epoch 200 --batch-size 128 \
  --d-model 256 --nhead 4 --d-ff 1024 --num-layers 6 --seq-len 256 \
  --artifact-dir results/hdpc_grid_v2
```

## Conditions (4)

1. teacher_only — no student/crown
2. student_no_crown — plain KD, no PC crown
3. detached_crown — HDPC student with detached crown
4. coupled_crown — HDPC student with coupled crown

Seeds: [42, 1234, 5678], λ_kd: [0.01, 0.05, 0.10]
Total runs: 3 teacher_only + 3×3×3 = 30 student conditions = 33 total

## Cleanup

- Retrieve artifacts to projects/relaleap/experiments/hdpc_epc_grid_v2/artifacts/
- Verify grid_v2_summary.json
- Terminate pod

## Failure / cleanup note

2026-07-11 17:36 UTC heartbeat found the pod idle and `hdpc_grid_v2.log` showing `TypeError: estimate_perplexity() got an unexpected keyword argument 'eval_batches'` on the first teacher-only condition. Retrieved the log to `artifacts/hdpc_grid_v2.log` and deleted pod `tb09sv8ocb8qgv` at 17:39 UTC. No `grid_v2_summary.json` was produced.
