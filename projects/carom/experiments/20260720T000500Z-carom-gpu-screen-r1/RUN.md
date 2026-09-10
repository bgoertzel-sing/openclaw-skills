# RUN: CAROM GPU Mechanism Screen (r1)

**Experiment ID:** `20260720T000500Z-carom-gpu-screen-r1`
**Status:** completed; all four arms finished with exit code 0; artifacts retrieved
**Created:** 2026-07-20 00:05 PDT
**Pod provisioned:** 2026-07-20 00:09 PDT
**Approved by:** Ben Goertzel (Telegram, 2026-07-19, up to USD 10)
**Cost bound:** USD 10.00 maximum incremental spend
**Pod ID:** `00e42nckt4vm1v`
**GPU:** A100 SXM4 80GB (Secure Cloud)
**Rate:** $1.49/hr
**Image:** `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
**SSH:** `root@154.54.102.25 -p 16074`
**SSH key:** `/home/openclaw/.runpod/ssh/runpodctl-ssh-key`

## Objective

Run all four CAROM execution semantics (scheduled, fixed-point, fixed-chain
itinerant, free-rho itinerant) at GPU scale with common task, common operator
core, and shared seed. Collect per-step loss, accuracy, gradient norms,
fixed-point residuals, itinerant trajectories, and routing diagnostics.

This is a one-off bounded mechanism screen. It does not claim broad
algorithmic superiority. Validity gates: fixed-point residuals must decrease
across sweeps; hand-built chain itinerancy must be distinct from free-rho.

## Arms

| Arm | Description |
|---|---|
| `scheduled` | External clock, T=5 steps |
| `fixedpoint` | Deep equilibrium, 8 sweeps, alpha=0.5, contraction pressure |
| `itinerant-fixed` | GLV competition, hand-built successor chain, 70 dynamics steps |
| `itinerant-free` | GLV competition, free inhibition matrix, 70 dynamics steps |

## Configuration

- Seed: 7
- Steps: 4000
- Batch size: 128
- Model dimension: d=64, K=16 operators
- Optimizer: AdamW, lr=2e-3, weight_decay=1e-4, OneCycleLR
- Gradient clip: 1.0
- Eval every: 100 steps
- Checkpoint every: 1000 steps
- Dataset: procedural Z_8 composition task (6 slots, 5 commands, 10-token vocab)
- Source: `projects/carom/repos/carom/{task,model,train,run_carom_gpu_screen.py}`

## Remote job

- Provider: RunPod
- Account: bengoertzel@gmail.com
- GPU: 1× A100 SXM 80GB Secure Cloud (or RTX 4090 if A100 unavailable)
- Price: $1.49/hr (A100) or $0.69/hr (4090)
- Expected duration: ~1-2 hours
- Hard cost cap: $10.00
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Storage: no persistent volume
- Data classification: public (procedural synthetic task, no private data)
- Stop/terminate: terminate after artifact retrieval
- Artifact return path: `projects/carom/experiments/20260720T000500Z-carom-gpu-screen-r1/artifacts/`

## Stop conditions

- Non-finite loss
- Cost approaching $10 cap
- Pod unresponsive for >15 minutes
- Completion of all 4 variants with artifact retrieval

## Evidence to collect

- Per-variant JSON with per-step telemetry (loss, grad_norm, eval_acc, residuals, trajectories)
- Checkpoints at steps 0, 1000, 2000, 3000, 3999
- Summary JSON
- Stdout/stderr logs
- `nvidia-smi` output
- Python/torch versions

## Final Results

| Variant | Final Accuracy | Time (s) | Parameters |
|---|---|---|---|
| scheduled | 0.771 | 82 | 1,322,472 |
| fixedpoint | 0.560 | 203 | 1,322,792 |
| itinerant-fixed | 0.996 | 1,403 | 1,326,925 |
| itinerant-free | 0.865 | 1,417 | 1,326,925 |

Exit code: 0. All artifacts retrieved and verified (SHA-256 in REPORT.md).

## Interpretation

- **Observed:** Itinerant-fixed (hand-built GLV chain) achieves near-perfect
  accuracy (99.6%), dramatically outperforming scheduled (77.1%) and
  fixed-point (56.0%).
- **Observed:** Free-rho (learned inhibition) reaches 86.5%, confirming
  that learned GLV dynamics can produce useful heteroclinic channels without
  a hand-built chain, though with more overlap and dwell time.
- **Observed:** Fixed-point residuals decrease monotonically across sweeps
  (contraction confirmed) but stabilize at ~0.051, indicating incomplete
  convergence within 8 sweeps.
- **Inferred:** Temporal ordering via heteroclinic channels is the key
  mechanism for compositional generalization in this task.
- **Hypothesis:** Stronger inhibition or adaptive dynamics could close the
  free-rho gap to fixed-chain.

## Reports

- `REPORT.md`: full ASCII report with provenance
- `REPORT.tex` / `REPORT.pdf`: LaTeX/PDF version
- `artifacts/carom_screen/`: raw JSON telemetry, checkpoints, logs
