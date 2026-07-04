# OmegaSim A6 run

## Status

completed

## Question

Can a single-hive role-coupled motivational model produce bounded, structured residual dynamics under condition 1 (`no_cross_role_coupling`)?

## Command

```bash
python3 run_a6.py --condition 1 --timesteps 120 --seed 20260701 --noise 0.01 --outdir runs/condition-1-smoke
```

## Environment

- Python: `3.10.12`
- Platform: `Linux-7.0.11-76070011-generic-x86_64-with-glibc2.35`
- NumPy: `2.2.6`
- Git: `{
  "repo": "/home/openclaw/research-agent/projects/hyperseed-formalizations/repos/hyperseed-formalizations",
  "commit": "99a62789152deec88b0f5b660754472e4268487d",
  "branch": "agent/protomegatron-formalization-0002",
  "status_short": "?? papers/0005-plain-metta-rholang-spec-compiler/\n?? substack/"
}`

## Configuration

```json
{
  "config": {
    "condition_id": 1,
    "timesteps": 120,
    "seed": 20260701,
    "field_dim": 8,
    "coupling_slope_k": 2.0,
    "threshold_percentile_theta": 50.0,
    "delay_tau": null,
    "memory_rho": null,
    "fatigue_gain": 0.03,
    "prediction_cost": 0.03,
    "noise": 0.01,
    "coupling_gain": 0.35,
    "field_leak": 0.08,
    "role_decay": 0.05,
    "temperature": 0.28
  },
  "condition": {
    "id": 1,
    "name": "no_cross_role_coupling",
    "description": "Roles evolve only from shared field, noise, and self-state.",
    "coupling_mode": "none",
    "coupling_gain": 1.0,
    "logistic_slope": 2.0,
    "delay_tau": 0,
    "hysteresis_rho": 0.0,
    "adaptive_thresholds": false,
    "costly_prediction": false
  },
  "roles": [
    "explorer",
    "synthesizer",
    "formalizer",
    "implementer",
    "reviewer",
    "coordinator",
    "maintainer",
    "communicator"
  ],
  "actions": [
    "explore",
    "message",
    "create_task",
    "work_task",
    "synthesize",
    "review",
    "formalize",
    "delegate",
    "predict",
    "escalate",
    "maintain",
    "pause"
  ]
}
```

## Results

```json
{
  "artifact_final": [
    1.0,
    1.0,
    0.9230625301525311
  ],
  "compression_ratio": 0.13617021276595745,
  "embedded_shape": [
    118,
    87
  ],
  "field_minmax": [
    0.0,
    0.7643792434795807
  ],
  "field_shape": [
    120,
    8
  ],
  "latent_shape": [
    120,
    8,
    8
  ],
  "mean_fatigue_final": 1.0,
  "mean_threshold_final": 0.4179393080137578,
  "n_lobes": 4,
  "nonlinear_forecastability": 0.6210536766646134,
  "observable_shape": [
    120,
    29
  ],
  "pca_explained": [
    0.6173311157473748,
    0.07469476033265196,
    0.05734835971851626
  ],
  "perturbation_recovery_proxy": 1.0,
  "recurrence": 0.07943119793162884,
  "residual_shape": [
    120,
    29
  ],
  "timesteps": 120,
  "transition_grammar": {
    "0->1": 2,
    "1->0": 2,
    "1->3": 2,
    "2->3": 1,
    "3->1": 2
  }
}
```

## Interpretation

This short run is a smoke/verification run, not evidence for a strange attractor.
It verifies bounded semantic fields, valid role actions, full latent-state output,
residual delay embedding, and preliminary lobe/recurrence metrics.

## Artifacts

- `result.npz`: raw arrays
- `metadata.json`: roles, fields, actions, condition, config
- `metrics.json`: analysis metrics
- `observable.npy`, `residuals.npy`, `embedding.npy`, `pca_scores.npy`, `lobe_labels.npy`
- `timeseries.png`, `pca_lobes.png` when matplotlib is available
- `stdout.log`, `stderr.log`, `command.sh`

## Timing

Wall time seconds: 1.566
