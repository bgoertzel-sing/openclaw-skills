# CAROM Interventions — Pod tcni7iyd48kcpe

## Date
2026-07-21

## Pod
- **ID:** `tcni7iyd48kcpe`
- **GPU:** A100 80GB PCIe, $1.49/hr
- **Image:** `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- **Provisioned:** ~11:59 PDT (18:59 UTC)
- **Status on discovery:** Idle (no training processes), interventions completed

## Context

This pod was provisioned after the previous pods (`sgmngeyziytvbv` and `pyqw9l1inspotx`) died due to RunPod community cloud reclamation. Ben approved a new pod at ~09:28 PDT. The pod was used for CAROM intervention experiments using the repaired `r9_carom_interventions.py` script.

## What ran

1. **TinyLM retraining** with checkpointing every 500 steps (9 checkpoints: step_0000 through step_4000)
2. **CAROM interventions** on each checkpoint:
   - τ-decline curve with repaired itinerary metrics (revisit-erasure fixed)
   - Trajectory intervention (forced/shuffled/smeared/natural)
   - L=5 inference-budget sweep (S=72, 100, 120)
3. Frozen evaluation corpora built at L2-4 (512 examples) and L5 (256 examples)

## Harness fixes applied

- Revisit-erasure in exact-order scoring fixed
- Tie-biased AUROC fixed (now properly 0.5 for tied logits)
- Hardcoded TinyLM span extraction path replaced with adapter-compatible extraction

## Key results

### τ-decline curve (repaired itinerary)
| Step | L24_acc | L24_tau | L24_cov | L24_rev | L5_acc | L5_tau |
|------|---------|---------|---------|---------|--------|--------|
| 0    | 0.138   | 0.236   | 0.490   | 0.0     | 0.135  | 0.245  |
| 500  | 0.278   | 0.982   | 0.821   | 0.0     | 0.192  | 0.914  |
| 1000 | 0.417   | 0.911   | 0.927   | 0.3     | 0.206  | 0.821  |
| 1500 | 0.536   | 0.783   | 0.936   | 0.9     | 0.227  | 0.607  |
| 2000 | 0.627   | 0.801   | 0.927   | 1.0     | 0.270  | 0.558  |
| 2500 | 0.680   | 0.807   | 0.922   | 1.3     | 0.333  | 0.641  |
| 3000 | 0.697   | 0.819   | 0.915   | 1.2     | 0.349  | 0.631  |
| 3500 | 0.708   | 0.828   | 0.910   | 1.2     | 0.346  | 0.636  |
| 4000 | 0.709   | 0.825   | 0.911   | 1.2     | 0.356  | 0.642  |

### Trajectory intervention
| Step | Natural | Forced | Shuffled | Smeared | Causal | Nat-Shuf |
|------|---------|--------|----------|---------|--------|----------|
| 0    | 0.138   | 0.138  | 0.138    | 0.138   | 0.000  | 0.000    |
| 500  | 0.278   | 0.280  | 0.244    | 0.261   | 0.036  | 0.034    |
| 1000 | 0.417   | 0.393  | 0.365    | 0.399   | 0.028  | 0.052    |
| 1500 | 0.536   | 0.462  | 0.436    | 0.505   | 0.025  | 0.100    |
| 2000 | 0.627   | 0.504  | 0.459    | 0.572   | 0.045  | 0.168    |
| 2500 | 0.680   | 0.544  | 0.473    | 0.661   | 0.070  | 0.207    |
| 3000 | 0.697   | 0.519  | 0.475    | 0.651   | 0.044  | 0.222    |
| 3500 | 0.708   | 0.526  | 0.478    | 0.671   | 0.048  | 0.229    |
| 4000 | 0.709   | 0.534  | 0.483    | 0.679   | 0.052  | 0.227    |

### L=5 budget sweep
| Step | S=72 | S=100 | S=120 |
|------|------|-------|-------|
| 0    | 0.135| 0.135 | 0.135 |
| 500  | 0.192| 0.200 | 0.200 |
| 1000 | 0.206| 0.206 | 0.214 |
| 1500 | 0.227| 0.230 | 0.241 |
| 2000 | 0.270| 0.275 | 0.278 |
| 2500 | 0.333| 0.333 | 0.329 |
| 3000 | 0.349| 0.343 | 0.343 |
| 3500 | 0.346| 0.349 | 0.346 |
| 4000 | 0.356| 0.357 | 0.362 |

## Interpretation

- **L2-4 task accuracy** plateaus at ~0.71 by step 3000, with itinerary τ stabilizing ~0.82 and coverage ~0.91.
- **L5 task accuracy** remains low (~0.36), confirming the structural-generalization gap from the original exp2.
- **Trajectory intervention** shows a growing natural-vs-shuffled gap (0 → 0.227), indicating the model develops increasing sensitivity to itinerary ordering. Causal selectivity (natural-forced gap) is modest (~0.05) but present in later checkpoints.
- **L5 budget sweep** shows marginal improvement from S=72 to S=120, suggesting inference budget is not the primary bottleneck for L5 performance.
- **Revisits** emerge at step 1000+ and stabilize ~1.2, indicating non-trivial cyclic behavior in the itinerary.

## Artifacts

- `artifacts/summary.json` — 9-record full results
- `artifacts/result_step_*.json` — per-checkpoint detailed metrics (9 files)
- `artifacts/frozen_L24.pt` — frozen L2-4 evaluation corpus
- `artifacts/frozen_L5.pt` — frozen L5 evaluation corpus
- `artifacts/run_logs.txt` — combined training and intervention logs

## Pod status

Pod is idle. Interventions completed. **Terminating to stop spend.**

## Next steps

- Retrieve/terminate confirmed done
- Compare repaired vs original harness metrics (revisit erasure fix impact)
- Feed results into CAROM project tasks for Ben's review
- R9 Stage A (collapse audit / factor probes) still pending — requires R8 checkpoints which were lost on previous pod death
