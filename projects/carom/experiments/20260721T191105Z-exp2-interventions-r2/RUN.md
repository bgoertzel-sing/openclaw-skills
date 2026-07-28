# Run 20260721T191105Z-exp2-interventions-r2: Exp2 checkpoint interventions

- Project: `carom`
- Started: `2026-07-21T19:11:05Z`
- Finished: 2026-07-21T20:18Z (UTC) (13:18 PDT)
- Status: `completed`
- Operator/agent: `ZeroBot`
- Local or remote: `RunPod/tcni7iyd48kcpe`

## Question

Does the observed itinerary-tau decline reflect genuine mechanistic drift or a
metric artifact; is the compiled channel causally load-bearing; and is held-out
L=5 failure explained by the `S=72` inference budget?

## Hypothesis or expected behavior

No directional outcome is assumed. Forced-correct versus shuffled control is
the primary causal contrast. L=5 is evaluated at `S={72,100,120}`. Repaired
metrics must fail the revisit, smeared-state, and tied-AUROC counterexamples.

## Inputs

- Source: unversioned CAROM import; `exp2_compiled_channel.py` SHA-256
  `9171bcd065226d3f5ca96d7bb8f9f20d9f144a11f251923382cbefb7be112223`.
- Harness SHA-256:
  `35adda3b1ca918febdf72af117f2309c6c713c3f489f6709e50d010e6890be56`.
- Configuration: TinyLM 1,500 pretraining steps; compiler-supervised Exp2
  4,000 steps; checkpoints every 500 steps; frozen L2--4 corpus `n=512` seed
  1234; frozen L5 corpus `n=256` seed 5678; trajectory clamp seed 7.
- Random training seed: 0. Training and quick-evaluation RNG streams are
  separated.

## Environment

- RunPod pod: `tcni7iyd48kcpe`, created manually by Ben through web UI.
- GPU: NVIDIA A100-SXM4-80GB; 16 vCPUs; 125 GB RAM.
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`.
- Storage: 50 GB container disk; `/workspace` network mount. Durable run root:
  `/workspace/zerobot-runs/carom`.

## Command

See `command.sh`.

## Results

- Exit status: 0 (success)
- Initial run (`run.log`) crashed at Step 4 due to corpus unpacking mismatch
  (expected 8 keys, got 5). A repaired r3 harness run (`run_interventions_r3.log`)
  completed all 9 checkpoints successfully.
- Artifacts retrieved to `artifacts/results/` with SHA-256 hashes in
  `artifacts/artifact_hashes.txt`.

### τ-decline curve (repaired itinerary metrics)

| Step | L24_acc | L24_tau | L24_cov | L24_rev | L5_acc | L5_tau |
|------|---------|---------|---------|---------|--------|--------|
|    0 |   0.138 |   0.236 |   0.490 |     0.0 |  0.135 |  0.245 |
|  500 |   0.278 |   0.982 |   0.821 |     0.0 |  0.192 |  0.914 |
| 1000 |   0.417 |   0.911 |   0.927 |     0.3 |  0.206 |  0.821 |
| 1500 |   0.536 |   0.783 |   0.936 |     0.9 |  0.227 |  0.607 |
| 2000 |   0.627 |   0.801 |   0.927 |     1.0 |  0.270 |  0.558 |
| 2500 |   0.680 |   0.807 |   0.922 |     1.3 |  0.333 |  0.641 |
| 3000 |   0.697 |   0.819 |   0.915 |     1.2 |  0.349 |  0.631 |
| 3500 |   0.708 |   0.828 |   0.910 |     1.2 |  0.346 |  0.636 |
| 4000 |   0.709 |   0.825 |   0.911 |     1.2 |  0.356 |  0.642 |

### Trajectory intervention

| Step | Natural | Forced | Shuffled | Smeared | Causal | Nat-Shuf |
|------|---------|--------|----------|---------|--------|----------|
|    0 |   0.138 |  0.138 |    0.138 |   0.138 |  0.000 |    0.000 |
|  500 |   0.278 |  0.280 |    0.244 |   0.261 |  0.036 |    0.034 |
| 1000 |   0.417 |  0.393 |    0.365 |   0.399 |  0.028 |    0.052 |
| 1500 |   0.536 |  0.462 |    0.436 |   0.505 |  0.025 |    0.100 |
| 2000 |   0.627 |  0.504 |    0.459 |   0.572 |  0.045 |    0.168 |
| 2500 |   0.680 |  0.544 |    0.473 |   0.661 |  0.070 |    0.207 |
| 3000 |   0.697 |  0.519 |    0.475 |   0.651 |  0.044 |    0.222 |
| 3500 |   0.708 |  0.526 |    0.478 |   0.671 |  0.048 |    0.229 |
| 4000 |   0.709 |  0.534 |    0.483 |   0.679 |  0.052 |    0.227 |

### L=5 inference-budget sweep

| Step |  S=72 | S=100 | S=120 |
|------|-------|-------|-------|
|    0 | 0.135 | 0.135 | 0.135 |
|  500 | 0.192 | 0.200 | 0.200 |
| 1000 | 0.206 | 0.206 | 0.214 |
| 1500 | 0.227 | 0.230 | 0.241 |
| 2000 | 0.270 | 0.275 | 0.278 |
| 2500 | 0.333 | 0.333 | 0.329 |
| 3000 | 0.349 | 0.343 | 0.343 |
| 3500 | 0.346 | 0.349 | 0.346 |
| 4000 | 0.356 | 0.357 | 0.362 |

### Artifacts

- 9 per-step JSON result files (`result_step_0000.json` through `result_step_4000.json`)
- `summary.json` (30 KB, aggregated results)
- `frozen_L24.pt` (578 KB, 512 examples)
- `frozen_L5.pt` (291 KB, 256 examples)
- `run.log` (initial run, crashed at Step 4)
- `run_interventions_r3.log` (repaired r3 run, completed successfully)
- `artifact_hashes.txt` (SHA-256 for all artifacts)

## Interpretation

- **τ-decline:** L2-4 accuracy plateaus ~0.71 and tau stabilizes ~0.82,
  consistent with the earlier pod's findings. L5 accuracy remains low (~0.36),
  confirming held-out layer failure is not resolved by training duration alone.
- **Trajectory intervention:** Natural-vs-shuffled gap grows from 0 to 0.227,
  showing the compiled channel carries trajectory-dependent information.
  Causal selectivity (forced-natural) is modest (~0.05), suggesting the channel
  is partly load-bearing but not strongly causal in the forced-correct sense.
- **L=5 budget sweep:** Marginal improvement from S=72 to S=120
  (0.356 → 0.362 at step 4000), insufficient to explain the L=5 gap.
  The held-out layer failure is architectural/generalization, not inference-budget
  limited.
- These r2 results are consistent with the earlier r1 run from pod
  `tcni7iyd48kcpe` (same pod, separate experiment record at
  `20260721T195900Z-carom-interventions-pod-tcni7iyd48kcpe`).

## Reproduction

Deploy the two hash-pinned Python files to the run root and execute
`command.sh` as a background process with PID and log captured in the run root.

## Follow-up

- Pod `tcni7iyd48kcpe` was stopped (not terminated) by Ben via web UI.
- All artifacts retrieved and hash-verified locally.
- Monitor cron job removed (was stale, pod no longer reachable).
