# Phase-1 lifted Lorenz-63 benchmark

- Status: completed, exit 0
- Question: Does dependency-free kinetic embedding plus adaptive microstates retain more temporal structure than matched raw M1 on the same deterministic noisy R256 lift?
- Relevant research rules: 1 (validate detector), 3 (production backend exists; bounded run uses dependency-free reference), 5 (reproducible report), 7 (backend seam).
- Repository: `https://github.com/bgoertzel-sing/chaos-language-algorithm`
- Branch/start commit: `agent/hd-embedding-cla` / `71bdcab79592772fda91cff0dc2a94f133e25454`
- Start state: untracked `docs/cla_python_library_interface_design.tex`; benchmark/test additions were also dirty for this run. Full status is in `environment.txt`.
- Exact command: `command.sh`
- Configuration: Lorenz-63, 256 retained samples after 64 discarded; deterministic orthonormal lift to R256; Gaussian noise 0.001; seed 20260712; pure kinetic map d=3, lag=2; k=12; matched lifted raw-M1 with 2 bins/axis; 4 CLA iterations; 3 shuffles.
- Host/tools: local CPU, Python/OS/CPU and optional deeptime version in `environment.txt`.
- Wall time: 13 seconds (`/usr/bin/time`: real 13.22 s). Raw stdout/stderr and exit code are preserved.

## Direct results

| diagnostic | adaptive kinetic + k-means | matched raw M1 |
|---|---:|---:|
| symbols / unique | 254 / 12 | 256 / 209 |
| CLA chunk rules / categories | 4 / 0 | 1 / 0 |
| exact symbolic reconstruction | yes | yes |
| real-minus-shuffled proxy bits | 39.3333 | 2.1000 |
| held-out order-2 n-gram perplexity | 3.4202 | 433.1849 |
| scorer total (proxy units) | 205.6 | 253.9 |

Intrinsic spectral participation ratio was 3.4499, while the 95%-variance suggested dimension was 141. The pure-map singular values were all clipped to 1.0, a warning that this dependency-free high-D whitening path is numerically saturated. Lifted trajectory SHA-256 (big-endian float64 serialization): `36ded3c1df542e082948014970f1b28d7de14efee4d83457287cb514a1680a1b`.

## Interpretation and limits

This single bounded seed supports proceeding: adaptive symbols show a much larger real-minus-shuffled proxy and far lower n-gram holdout perplexity than raw M1. It does **not** establish grammar preservation. Compression values use the current approximate two-part score against an empirical iid baseline, not calibrated CLA MDL; holdout is a smoothed order-2 n-gram, not CLA predictive likelihood. M1 has a radically larger alphabet, so the held-out comparison is diagnostic rather than a fully rate-matched predictive test. No categories were learned. Production `deeptime` 0.4.5 is installed but was not used in this primary reference run.

## Verification

`python3 -m unittest tests.test_phase1_lorenz63 tests.test_hd_embedding` passed 19 tests in 3.189 s. Important artifacts are hashed in `SHA256SUMS`.

## Recommendation

Run a preregistered multi-seed d/k/lag sweep using the deeptime backend, add rate/alphabet-matched controls, and report intervals. Prioritize a genuine CLA predictive code or calibrated MDL before making scientific grammar-preservation claims.
