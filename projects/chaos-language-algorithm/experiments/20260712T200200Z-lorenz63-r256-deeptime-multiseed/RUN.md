# Preregistered lifted Lorenz-63 R256 deeptime multi-seed sweep

- Status: completed, exit 0 (raw artifacts preserved under their recorded SHA-256 hashes)
- Question: Across seeds and a bounded d/k/lag grid, does deeptime VAMP + low-cardinality microstates yield positive real-minus-shuffled compression proxy and stable held-out order-2 n-gram perplexity, relative to alphabet-matched direct/raw controls?
- Start commit: `3d227b1b5486eed451fb53af2bfd9c3a96219975` on `agent/hd-embedding-cla`.
- Existing unrelated work to preserve: untracked `docs/cla_python_library_interface_design.tex`.
- Relevant research rules: 1 (validate detector), 2 (preregister spec), 3 (deeptime backend), 5 (reproducible evidence), 7 (backend seam).

## Fixed design before execution

Lorenz-63: 192 retained points after 64 discarded; deterministic noisy orthonormal lift to R256, noise=0.001. Seeds: 101, 202, 303. Deeptime non-reversible VAMP grid: d={3,5}, k={8,16,24}, lag={1,3}; 36 primary runs. CLA suffix-trie/JS, 2 induction iterations, 2 shuffled marginal-preserving surrogates, 70/30 held-out smoothed order-2 n-gram diagnostic.

Controls per seed: (1) `direct_raw_kmeans`, sklearn k-means directly on raw Lorenz-63 xyz with k=16 (roughly alphabet-matched); (2) `raw_compound_m1`, 2 bins on each of R256 (documented alphabet-explosion failure mode); (3) dependency-free pure kinetic map at d=3,k=16,lag=1. Controls total 9; total configurations 45.

Primary metrics: exact reconstruction, symbol count, unique symbols, rules/categories, current scorer total, real and shuffled gains and real-minus-shuffled proxy bits, held-out order-2 n-gram log-loss/perplexity. Embedding diagnostics: singular values, timescales, cumulative kinetic variance, finite-value warnings. All compression metrics are proxy/non-calibrated MDL; held-out metric is an n-gram diagnostic and **not CLA predictive likelihood**.

Aggregation: by method and by deeptime d/k/lag setting; report n, mean, sample SD, min/max, and normal 95% interval `mean +/- 1.96*SD/sqrt(n)` for real-minus-shuffled proxy and perplexity. Also overall deeptime aggregation. No hypothesis-test p-values. Robustness means all three seeds positive real-minus-shuffled for a setting; comparisons remain descriptive due to metric/alphabet limitations.

Artifacts: `results.json`, `runs.csv`, `aggregates.csv`, stdout/stderr, environment, timing, hashes, exit status. Exact command is frozen in `command.sh`. Tests for deterministic reduced sweep, schema, and aggregation run before full execution. Bounded local CPU only; no push/paid compute.

## Completed results

- Status: completed, exit 0
- Full sweep: 45 configurations in 62.22 s elapsed (61.80 s measured internally); 36 deeptime grid runs plus 9 controls.
- Exact reconstruction: 45/45. Categories: 0 in all runs. Deeptime symbols matched requested k (8--24); raw compound M1 had 150--164 unique symbols.
- Numerical warnings recorded by the original writer: 0. This was a diagnostics defect: deeptime leading singular values extremely near/slightly above 1 produced nonpositive or implausibly large implied timescales (up to about 1.35e16 in magnitude), but the old finite-only check did not flag them. The raw values and hashes remain unchanged. The repaired writer now preserves raw values while marking these diagnostics invalid with explicit status/warning fields. Pure-reference values [1,1,1] are likewise invalid as timescale evidence near lambda=1.

### Aggregate diagnostics

All compression values below are current two-part **proxy** bits, not calibrated CLA MDL. Perplexity is a smoothed order-2 n-gram diagnostic, **not CLA predictive likelihood**. Intervals in `aggregates.csv` are mean +/- 1.96 SE.

| method/setting | n | proxy mean ± SD | perplexity mean ± SD | all seeds proxy > 0 |
|---|---:|---:|---:|:---:|
| deeptime d=3 k=16 lag=1 | 3 | 9.500 ± 1.000 | 8.826 ± 3.883 | yes |
| deeptime d=3 k=16 lag=3 | 3 | 6.333 ± 1.756 | 12.300 ± 3.062 | yes |
| deeptime d=3 k=24 lag=1 | 3 | 5.000 ± 1.000 | 16.505 ± 4.484 | yes |
| deeptime d=3 k=24 lag=3 | 3 | 3.167 ± 1.258 | 20.287 ± 4.029 | yes |
| deeptime d=3 k=8 lag=1 | 3 | 17.000 ± 6.946 | 3.724 ± 2.079 | yes |
| deeptime d=3 k=8 lag=3 | 3 | 9.833 ± 5.132 | 4.835 ± 1.386 | yes |
| deeptime d=5 k=16 lag=1 | 3 | 3.667 ± 1.258 | 11.735 ± 0.569 | yes |
| deeptime d=5 k=16 lag=3 | 3 | 5.167 ± 1.258 | 11.992 ± 0.750 | yes |
| deeptime d=5 k=24 lag=1 | 3 | 5.017 ± 2.674 | 19.970 ± 3.662 | yes |
| deeptime d=5 k=24 lag=3 | 3 | 6.333 ± 1.528 | 20.694 ± 1.382 | yes |
| deeptime d=5 k=8 lag=1 | 3 | 11.167 ± 5.033 | 4.203 ± 0.368 | yes |
| deeptime d=5 k=8 lag=3 | 3 | 14.833 ± 5.346 | 4.470 ± 0.663 | yes |
| deeptime overall | 36 | 8.085 ± 5.200 | 11.628 ± 6.739 | yes |
| direct_raw_kmeans | 3 | 12.200 ± 0.500 | 3.697 ± 0.034 | yes |
| pure_reference | 3 | 15.167 ± 1.607 | 4.151 ± 0.148 | yes |
| raw_compound_m1 | 3 | 1.867 ± 1.528 | 257.769 ± 26.743 | yes |

## Interpretation

The positive real-minus-shuffled proxy is robust in the narrow preregistered sense: every deeptime run and every control was positive across all seeds/settings. It is not uniquely favorable to deeptime. Direct raw xyz k-means (k=16) had a higher proxy mean (12.2) and much lower perplexity (3.70) than deeptime overall (8.09 and 11.63); the dependency-free reference was also strong (15.17, 4.15). The best deeptime rate point was k=8 (proxy means 9.83--17.0; perplexity 3.72--4.84), while k=16/24 increased perplexity substantially. Raw compound M1 retained the expected alphabet-mismatch failure mode: 150--164 unique symbols and perplexity 257.77, despite a small positive proxy. No categories emerged.

Thus this sweep supports low-cardinality symbolization and rejects raw compound M1 as a fair predictive comparator, but does not show that VAMP improves upon a direct low-cardinality raw baseline for Lorenz-63. Near-unit singular values also limit kinetic-map interpretation at this short sample size.

## Verification and artifacts

- Focused tests: `python3 -m unittest tests.test_phase1_sweep tests.test_phase1_lorenz63 -v` — 5 passed.
- Full suite: `python3 -m unittest discover -s tests -v` — 107 passed in 41.081 s.
- `git diff --check` passed.
- Raw per-run and aggregate records: `results.json`, `runs.csv`, `aggregates.csv`; environment, stdout/stderr, timing, exit status, and hashes preserved alongside.
- Artifact formatting note: the already-hashed CSV files use the platform-default CSV CRLF record terminator. They were not rewritten. Future sweep CSV writers explicitly use LF, avoiding spurious `git diff --check` whitespace reports.

## Recommended next agenda step

Use the alphabet-matched direct xyz k-means baseline as the benchmark to beat. Increase trajectory length and choose lag via implied-timescale stability before another VAMP sweep; evaluate temporal-block surrogates and a genuinely calibrated CLA predictive/MDL code. Add category-seeding evaluation only after the embedding clears those controls.
