# OmegaSim A6 experiment build and smoke verification

## Status

Completed initial A6 implementation and smoke verification on 2026-07-01 PDT.

## Objective

Build the first OmegaSim A6 experiment: a single-hive role-coupled motivational model simulation with thresholded logistic appraisal, delayed cross-role influence, hysteresis/adaptive-threshold/prediction conditions, and a lightweight analysis pipeline.

## Files

- `omegasim_a6.py` — main simulation
- `conditions.py` — seven A6 conditions
- `sweeps.py` — sweep grid from ProtomegaTron's feedback
- `analysis.py` — residualization, delay embedding, PCA/lobes, recurrence/compression/forecastability/recovery metrics
- `run_a6.py` — ledger-style runner
- `test_a6.py` — smoke tests
- `.venv/` — local Python 3.10 environment with numpy/scipy/matplotlib
- `runs/condition-1-smoke/` — no-coupling smoke run
- `runs/condition-5-smoke/` — delayed logistic + hysteresis smoke run

## Environment

- Python: `Python 3.10.12`
- Virtualenv: `projects/hyperseed-formalizations/experiments/omegasim-a6/.venv`
- Installed packages: numpy 2.2.6, scipy 1.15.3, matplotlib 3.10.9
- Repository commit observed before run: `99a6278` in `projects/hyperseed-formalizations/repos/hyperseed-formalizations/`; repo had pre-existing untracked `papers/0005-plain-metta-rholang-spec-compiler/` and `substack/` entries.

## Commands run

```bash
python3 -m venv projects/hyperseed-formalizations/experiments/omegasim-a6/.venv
projects/hyperseed-formalizations/experiments/omegasim-a6/.venv/bin/python -m pip install --upgrade pip numpy scipy matplotlib
cd projects/hyperseed-formalizations/experiments/omegasim-a6
.venv/bin/python test_a6.py
.venv/bin/python run_a6.py --condition 1 --timesteps 120 --seed 20260701 --noise 0.01 --outdir runs/condition-1-smoke
.venv/bin/python run_a6.py --condition 5 --timesteps 120 --seed 20260701 --noise 0.01 --outdir runs/condition-5-smoke
.venv/bin/python -m py_compile omegasim_a6.py conditions.py sweeps.py analysis.py run_a6.py test_a6.py
```

## Verification results

`test_a6.py` passed all smoke tests:

- simulation runs;
- latent state shape is `(timesteps, 8 roles, 8 state vars)`;
- action indices/names are valid;
- semantic field and latent state remain bounded in `[0, 1]`;
- residualization and analysis produce finite outputs;
- condition 1 and condition 5 produce different dynamics.

Short-run comparison, same seed/noise/timesteps:

| Metric | Condition 1 | Condition 5 |
|---|---:|---:|
| field min/max | `[0.0, 0.7643792434795807]` | `[0.0, 1.0]` |
| detected lobes | 4 | 4 |
| recurrence | 0.07943119793162884 | 0.07943119793162884 |
| final artifact maturity | 1.0 | 1.0 |
| final artifact utility | 1.0 | 1.0 |
| final queue health | 0.9230625301525311 | 0.2813038027607335 |

Cross-condition array differences:

- mean absolute field difference: `0.1033780502359527`
- mean absolute latent-state difference: `0.019685818052375886`

## Interpretation

This is a smoke run only. It confirms the A6 implementation emits the expected latent-state/action/field artifacts, keeps fields bounded, and differentiates uncoupled from delayed-logistic+hysteretic dynamics. It does **not** establish a strange attractor; longer sweeps and shuffled/linearized controls are still needed.
