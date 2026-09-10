# P1A full-grid metrics pipeline smoke

- Date: 2026-07-27T23:58Z
- Repository commit: `e4e1d65`
- Scope: CPU implementation/replay smoke; not scientific-gate eligible
- Command: `OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 -m pytest`, followed
  twice by `python3 scripts/run_p1a_calibration.py --trials 32 --seeds 12011
  --dimensions 64 96 128 --loads 4 8 --output <artifact>`

Result: 18 tests passed. Both 30-cell/10-curve payloads are byte-identical,
SHA-256 `dba950b8250ccaef6876092a59b8da1ac5528e5ba2eb7d9fea74de6faca7c5bb`.
They exercise Wilson U95, grid censoring, deterministic binomial-logistic
interpolation, Spearman and resolved-decrease diagnostics, isotonic deviation,
WLS scaling, coherence alpha, and all-distance F3 bipolar/linear geometry.

The runner marks this reduced smoke `scientific_gate_eligible=false`. The
frozen 2,048-trial, 17-dimension, five-load, three-seed invocation remains the
next P1A execution; no P1A criteria have been changed or inferred from smoke.
