# Remote Job Record: HDPC/ePC Grid Run 1

## Provider/account context
- Provider: Runpod
- Account: bengoertzel@gmail.com
- Created: 2026-07-11 03:44:41 UTC

## Resource
- Pod ID: `zivpxu06yhmx40`
- Pod name: `relaleap-hdpc-grid-run1`
- GPU: 1× RTX A6000-class GPU
- Price: $0.49/hr
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Volume: 30GB

## Approval / guardrail provenance
- Local heartbeat search did not find a pre-existing remote-job record for this exact pod.
- Closest planning note: `scratch/relaleap_omegasim_next_gpu_plans_20260710.md` listed HDPC/ePC grid as requiring explicit capped approval, expected 6-10h, hard cap 12h / $6.
- Current heartbeat status: active GPU process, not idle; not terminated because it is still doing work and appears within the draft cap window, but approval/guardrail provenance remains unresolved.

## Task observed on pod
`python3 run_grid.py --device cuda --epochs 5 --steps-per-epoch 200 --batch-size 128 --d-model 256 --nhead 4 --d-ff 1024 --num-layers 6 --seq-len 256`

## Status
- [x] Found running
- [x] Active GPU work observed at 2026-07-11 05:35 UTC
- [x] Completion observed at 2026-07-11 07:19 UTC
- [x] Artifacts retrieved
- [x] Pod terminated

## Heartbeat update — 2026-07-11 06:19 UTC

Pod remained active, not idle:

- Process: `python3 run_grid.py --device cuda --epochs 5 --steps-per-epoch 200 --batch-size 128 --d-model 256 --nhead 4 --d-ff 1024 --num-layers 6 --seq-len 256`
- Process elapsed: about 2h29m
- GPU: 100% utilization, about 4.3GB / 49GB VRAM used
- Latest observed artifact: `/workspace/relaleap/results/hdpc_grid/seed5678_lam0.01/hdpc_tinyshakespeare_smoke.pt` at 06:19 UTC
- Cleanup action: not terminated because it is actively producing artifacts and remains well inside the draft 12h/$6 cap window.
- Next check scheduled for 2026-07-11 07:30 UTC.

## Heartbeat check — 2026-07-11 06:49 UTC
- Pod still running active GPU work: `run_grid.py` elapsed ~2h59m, GPU utilization 100%, VRAM ~4264 MiB.
- Outputs observed through `seed5678_lam0.05`; no completion/idle state yet.
- Next follow-up scheduled for 2026-07-11 07:35 UTC.

## Completion note

2026-07-11 07:24 UTC: heartbeat found no active training process, idle GPU, and completed `grid_summary.json`. Artifacts were copied to `projects/relaleap/experiments/hdpc_epc_grid_run1/artifacts/`. `runpodctl pod delete zivpxu06yhmx40` returned deleted=true, and `runpodctl pod list` returned `[]`. See `hdpc_epc_grid_run1/RUN.md`.
