# HDPC/ePC Extended Grid V2 Run 2 — Remote Job Record

## Status: COMPLETE — pod auto-terminated, artifacts retrieved, RUN.md updated

## Pod Details
- Pod ID: `5j7sdm2b08oil9`
- GPU: RTX A6000 (48GB)
- Cost: $0.49/hr
- SSH: `ssh -i ~/.runpod/ssh/runpodctl-ssh-key root@38.147.83.27 -p 12114`
- Started: 2026-07-12 02:11 UTC
- Auto-terminate: 2026-07-12T12:00:00Z

## Approval
- Approved by Benjamin Goertzel: 2026-07-11 09:51 PDT
- This is a relaunch of the failed first attempt (call signature bug fixed)

## Source
- Repo: projects/relaleap/worktrees/tinyshakespeare-hdpc
- Branch: agent/tinyshakespeare-hdpc
- Commit: 3a6c733

## Guardrail
- Hard cap: 12h / $6 compute
- Auto-terminate: 2026-07-12T12:00:00Z

## Command
```bash
cd /workspace/relaleap && PYTHONPATH=src python3 scripts/run_grid_v2.py \
  --device cuda --epochs 5 --steps-per-epoch 200 --batch-size 128 \
  --d-model 256 --nhead 4 --d-ff 1024 --num-layers 6 --seq-len 256 \
  --artifact-dir results/hdpc_grid_v2
```

## Conditions (4)
1. teacher_only
2. student_no_crown
3. detached_crown
4. coupled_crown

Seeds: [42, 1234, 5678], λ_kd: [0.01, 0.05, 0.10]
Total runs: 3 teacher_only + 3×3×3 = 30 student conditions = 33 total

## Cleanup
- Retrieve artifacts to projects/relaleap/experiments/hdpc_epc_grid_v2/artifacts/
- Verify grid_v2_summary.json
- Terminate pod
