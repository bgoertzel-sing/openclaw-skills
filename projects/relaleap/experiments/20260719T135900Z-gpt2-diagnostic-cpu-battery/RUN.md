# Experiment: 20260719T135900Z-gpt2-diagnostic-cpu-battery

## Identity

- **Run ID:** `20260719T135900Z-gpt2-diagnostic-cpu-battery`
- **Project:** relaleap
- **Source commit:** `b58ba44` (branch `agent/tinyshakespeare-hdpc`)
- **Script:** `scripts/run_gpt2_diagnostic_cpu.py`
- **Device:** CPU (8 cores, 15 GB RAM)
- **Duration:** ~4 minutes
- **Cost:** USD 0 (local CPU)

## Purpose

Follow-up diagnostics addressing the "Plausible explanations" section of the
2026-07-19 six-layer outcome report. The report suggested: "hold the checkpoint
and downstream probe fixed while measuring layerwise teacher-logit/hidden-state
matching and gradient/activity scales across preregistered ePC hyperparameters."

Four hypotheses from the report:
1. Under-effective teacher transfer (KD gap ~880-893 nats)
2. Overly restrictive representation (ePC effective rank ~4-5 vs BP ~40-57)
3. Credit-assignment scale or optimization mismatch
4. Interaction with the fixed adapter rule

## Inputs

- **Checkpoints:** 9 saved safetensors checkpoints from Run 2
  (`experiments/20260718T073312Z-epc-outcome-6layer-run2/artifacts/results/checkpoints/`),
  3 seeds (1729, 3253, 6421) x 3 arms (bp_ce, bp_kd, epc_kd).
- **Probe:** Deterministic random-token batch (seed=42, seq_len=64, batch=2).
  No teacher model or dataset needed; all diagnostics use the saved weights
  and random-token forward passes.

## Diagnostics run

### D1: Weight-space spectral analysis (per layer, per checkpoint)

Per-layer singular value spectra for all weight matrices (c_attn, c_proj,
c_fc, c_proj in attention and MLP), plus layer-norm weight norms.

### D2: Representation geometry (per layer, per checkpoint)

Hidden-state activation statistics (mean, std, kurtosis, sparsity, effective
rank, participation ratio) on the fixed random-token probe.

### D3: Cross-checkpoint layerwise linear CKA

Pairwise linear CKA between all 9 checkpoints at each of 7 probe points
(input state + 6 hidden states).

### D4: ePC hyperparameter sweep (ePC checkpoints only)

Sweep over lambda_output {0.01, 0.05, 0.1, 0.3, 0.5}, relaxation_lr
{0.05, 0.1, 0.2, 0.4}, and steps {1, 2, 4, 8}. Measures energy, energy
history, accepted step sizes, and per-block gradient norms / credit ratios.

**Known limitation:** Used the model's own logits as a self-reference teacher
(since the real GPT-2 teacher is not cached locally). This makes the KD loss
trivially zero and all gradients vanish. D4 results are non-informative; the
diagnostic needs a real teacher or cross-checkpoint teacher to be meaningful.

### D5: Gradient flow comparison (per layer, per checkpoint)

Per-block gradient norms under cross-entropy loss on fixed random tokens.
Reveals whether ePC-trained models have different gradient flow properties.

## Key findings

### Finding 1: Representation collapse in ePC (supports hypothesis 2)

**ePC hidden states have effective rank ~1.0 in layers 1-5**, vs 1.5-4.5 for
BP controls:

| Layer | BP+CE | BP+KD | ePC+KD |
|-------|-------|-------|--------|
| 0     | 1.49  | 1.54  | 1.55   |
| 1     | 1.49  | 2.02  | 1.00   |
| 2     | 1.87  | 3.42  | 1.00   |
| 3     | 2.10  | 4.50  | 1.00   |
| 4     | 2.13  | 4.29  | 1.00   |
| 5     | 2.07  | 3.60  | 1.23   |

The ePC objective has collapsed the residual stream to a single dominant
direction in layers 1-5. A rank-1 representation cannot support meaningful
low-rank adaptation, which explains the outcome battery's finding that ePC
adaptation AUC is worse than both BP controls.

### Finding 2: Layer 5 weight explosion in ePC (supports hypothesis 3)

ePC's last layer has spectral norms **20-40x larger** than BP controls:

| Checkpoint            | attn_c_attn | mlp_c_fc | mlp_c_proj |
|-----------------------|-------------|----------|------------|
| seed1729_bp_ce        | 1.96        | 2.96     | 1.25       |
| seed1729_bp_kd        | 2.09        | 3.02     | 1.47       |
| seed1729_epc_kd       | 39.00       | 40.66    | 33.88      |
| seed3253_epc_kd       | 48.45       | 43.20    | 35.60      |
| seed6421_epc_kd       | 35.92       | 41.38    | 33.56      |

Condition numbers are 10-40x worse (e.g., mlp_c_proj condition ~207-217 for
ePC vs ~7.5-9.0 for BP). This suggests the ePC objective drives pathological
weight growth in the last layer, possibly because:
- The output_weight term (lambda_output=0.05) creates pressure only on the
  final layer's output.
- Local prediction errors in earlier layers are under-weighted relative to
  the output KD term.
- The last layer compensates for the collapsed representations below it by
  scaling up its weights to match teacher logits.

### Finding 3: Different gradient flow profile (supports hypothesis 3)

ePC models have a **U-shaped gradient profile** (high at layer 0 and 5, dip
in middle), while BP models show monotonic decay:

| Layer | BP+CE  | BP+KD  | ePC+KD |
|-------|--------|--------|--------|
| 0     | 30.33  | 17.60  | 26.22  |
| 1     | 13.51  | 9.97   | 14.55  |
| 2     | 9.84   | 7.57   | 14.84  |
| 3     | 8.40   | 5.80   | 13.77  |
| 4     | 7.82   | 4.59   | 11.68  |
| 5     | 8.60   | 4.33   | 26.31  |

The high layer-5 gradient norm (26.3 vs 4.3 for BP+KD) is consistent with
the weight explosion: the last layer receives large gradients that aren't
effectively distributed to earlier layers. The middle layers (2-4) have
higher gradients than BP+KD but lower than layer 5, suggesting the ePC
credit assignment is not effectively reaching the middle of the network.

### Finding 4: Low within-arm CKA (descriptive)

Within-arm CKA is very low for all arms (0.003-0.007), meaning different
seeds produce very different representations. Cross-arm CKA is also low, with
bp_ce_vs_bp_kd at 0.23 being the highest. This is expected for small models
trained from different initializations but confirms that the ePC
representation difference is not merely a seed effect.

### D4 limitation

The ePC hyperparameter sweep (D4) used the model's own logits as a
self-reference teacher, making the KD loss trivially zero and all gradients
vanish. D4 results are non-informative. To make this diagnostic meaningful,
it needs either:
- The real GPT-2 teacher model (requires internet or caching), or
- A cross-checkpoint teacher (e.g., use bp_kd checkpoint logits as teacher
  for the ePC checkpoint).

## Scientific interpretation

**Observed:**
1. ePC hidden states collapse to rank ~1 in layers 1-5.
2. ePC layer 5 weights explode (20-40x spectral norm increase).
3. ePC gradient flow is U-shaped with large layer-0 and layer-5 norms.
4. BP+KD has the healthiest representation geometry (effective rank 2-4.5).

**Inferred:**
The ePC objective as configured (lambda_output=0.05, steps=4,
relaxation_lr=0.2) creates a credit-assignment pathology: the output KD term
dominates, causing the last layer to compensate for collapsed middle-layer
representations by scaling up its weights. The local prediction errors in
earlier layers are too weak (relative to the output term) to maintain
representation diversity. This is a configuration/credit-assignment problem,
not necessarily a fundamental ePC scaling issue.

**Hypothesis:**
Increasing lambda_output (e.g., to 0.3-0.5) or decreasing the output_weight
relative to local prediction errors might prevent the representation collapse.
Alternatively, adding a hidden-state matching term (the existing
hidden_state_arm configuration) could maintain representation diversity.

**Decision implications:**
- The representation collapse and weight explosion are actionable: they
  suggest specific ePC hyperparameter changes that could be tested.
- A follow-up GPU run with revised hyperparameters (higher lambda_output,
  or enabled hidden-state matching) could test whether the collapse is
  preventable.
- The D4 diagnostic should be re-run with a real or cross-checkpoint teacher
  to complete the hyperparameter sensitivity analysis.

## Artifact map

- **Full results:** `diagnostic_results.json` (SHA-256 to be computed)
- **Summary:** `summary.json`
- **Script:** `scripts/run_gpt2_diagnostic_cpu.py` at commit `b58ba44`
- **Source checkpoints:** `experiments/20260718T073312Z-epc-outcome-6layer-run2/artifacts/results/checkpoints/`

## Exit status

Normal exit (code 0). All 5 diagnostics completed on all 9 checkpoints.
D4 results are non-informative due to the self-reference teacher design
limitation documented above.
