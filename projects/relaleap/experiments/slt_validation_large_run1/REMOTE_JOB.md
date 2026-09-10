# Remote Job Record: RelaLeap SLT Validation Large Run 1

## Provider/account context
- Provider: Runpod
- Account: bengoertzel@gmail.com
- Created: 2026-07-11 03:44:42 UTC

## Resource
- Pod ID: `kfzk2c2pwp8rlk`
- Pod name: `relaleap-slt-large-run1`
- GPU: 1× A100-class 80GB GPU (Runpod listing price observed through pod metadata)
- Price: $1.49/hr
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Volume: 50GB

## Approval / guardrail provenance
- Local heartbeat search did not find a pre-existing remote-job record for this exact pod.
- Closest planning note: `scratch/relaleap_omegasim_next_gpu_plans_20260710.md` listed larger SLT validation as requiring explicit capped approval, expected 8-14h, hard cap 16h / $24.
- Because the pod was complete/idle at heartbeat check time, artifacts were retrieved and the pod was terminated to stop spend.

## Task observed on pod
`python3 run_slt_large.py --device cuda --epochs 3 --n-chains 8 --n-samples 1000`

## Status
- [x] Found running
- [x] Completion observed
- [x] Artifacts retrieved
- [x] Pod terminated

## Completion note
2026-07-11 05:35 UTC: heartbeat found no active training process, idle GPU, and completed `slt_tinyshakespeare_report.json`. Artifacts were copied to `projects/relaleap/experiments/slt_validation_large_run1/artifacts/`. `runpodctl pod delete kfzk2c2pwp8rlk` returned deleted=true.
