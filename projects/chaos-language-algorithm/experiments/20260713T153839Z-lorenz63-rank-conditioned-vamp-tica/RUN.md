# Preregistered leakage-free rank-conditioned Lorenz-63 VAMP/TICA experiment

- Status: preregistered; not yet executed.
- Start: 2026-07-13T08:38:39-07:00.
- Repository branch/commit: `agent/hd-embedding-cla` at `64e9dd6c3a350d120400940e7d153ba84c1dc580`.
- Pre-existing unrelated dirty state to preserve: untracked `docs/cla_python_library_interface_design.tex`.
- Compute boundary: local CPU only, bounded threads; no paid compute or push.

## Plain-language question and fixed design

Does explicitly rank-conditioned linear VAMP recover predictive/grammar-bearing Lorenz-63 symbols better than alphabet-matched PCA-lift k-means once every learned transform is train-only? Generate three genuinely independent Lorenz-63 trajectories (distinct initial conditions), each with 2,048 retained points after burn-in, and independently lift each into R256. Use contiguous nominal 60/20/20 train/validation/test blocks. Remove a 16-point maximum-lag gap immediately before validation and test, so no lagged pair crosses a boundary. Never refit or update preprocessing, PCA, kinetic maps, k-means, vocabulary, or n-gram counts using validation/test data.

Fit train-only lifted-data PCA at ranks `{3,10}`. In each rank, compare directional nonsymmetric VAMP with reversible TICA, dimensions `{2,3}`, and lags `{1,4,16}`. Use explicit eigenspectrum truncation, covariance ridge regularization, and a maximum whitening condition number. Preserve raw singular values and reject a candidate if any retained singular value lies outside `[0,1]` beyond tolerance; never clip. Select rank/model/dimension/lag independently per trajectory by blocked validation VAMP-2 (smallest-complexity deterministic tie break), then evaluate test exactly once. Evaluate selected embeddings at matched `k={8,16}` without pooling k strata.

At every k, include train-fitted direct-xyz k-means and train-fitted PCA-lift k-means controls (ranks 3 and 10). Metrics are test next-symbol order-2 smoothed log loss using train symbols/counts, and a test-stream current-CLA two-part compression proxy margin relative to 20 deterministic circular block surrogates at each block length `{4,16}`. Surrogates circularly rotate independently shuffled blocks, preserving within-block order and total marginals. Report each trajectory and aggregate; these are diagnostics, not a calibrated CLA likelihood.

Primary stop/go rule: stop developing linear VAMP unless selected VAMP beats its best matched PCA-lift control on **both** lower held-out next-symbol log loss and higher minimum-over-block-length surrogate grammar/compression margin in at least 2 of 3 trajectories (reported separately for k=8 and k=16; no cross-k pooling). TICA is a comparator and cannot rescue VAMP under this rule.

## Research Rules applied before coding

1. Validate the estimator with focused leakage, rank/conditioning, fail-closed singular-value, split/seed, and metric-matching regressions.
2. This frozen plain-language record precedes implementation.
3. Use NumPy/SciPy/sklearn numerical and clustering primitives and deeptime-compatible VAMP-2 semantics rather than ad-hoc high-D inversion.
5. Preserve exact commands, versions, raw JSON/CSV, logs, status, timing, hashes, commits, and limitations.
7. Keep split, rank-conditioned estimator, symbolizer, surrogate, and metric stages as replaceable functions.

## Runtime contingency

First run a tiny smoke and record its wall time. The decisive design retains 3 trajectories, both ranks/models/dimensions/lags/k values, and 20 surrogates at both block lengths. Only optional CLA iteration count/parallel overhead may be reduced if extrapolation is excessive, and any deviation must be recorded before the full command.

### Preregistered runtime deviation before completed run

The 256-point, one-trajectory smoke with 2 surrogates and 2 CLA iterations took 0.71 s, but this underestimated nonlinear suffix-trie/CLA cost at 2,048 points. The first full attempt reached the 300 s execution limit before producing results (empty stdout/stderr; no partial metrics). Per the contingency, reduce only optional CLA induction iterations from 2 to 1. Preserve all scientifically decisive factors, all three trajectories, both k strata, and all 20 x 2 block surrogates. The compression quantity remains explicitly a one-iteration Phase-0 proxy.

## Completed result

- Status: completed; exit 0; empty stderr.
- Completed command: exactly `command.sh` (bounded BLAS/OpenMP threads).
- Wall time: 163.01 s external / 162.56 s internal; maximum RSS 157,752 KiB.
- Data: 3 independent initial-condition seeds `{101,202,303}`; each retained 2,048 points. Identical index geometry per trajectory: train `[0,1228)`, validation `[1244,1638)`, test `[1654,2048)`, with 16-point boundary gaps.
- Candidate grid: 72/72 rank/method/dimension/lag candidates numerically valid; no raw singular-value rejection occurred. Selected VAMP was rank 3, dimension 3, lag 1 in all trajectories (validation VAMP-2 2.981827, 2.982199, 2.982695). TICA selected dimension 3, lag 1 (rank 3 once, rank 10 twice). Selected VAMP singular values were approximately `[0.999999, 0.9959, 0.9946--0.9949]`: below the fail-closed bound but still near-unit and not strong standalone kinetic evidence.

### Primary per-trajectory comparison

PCA values below are the best matched rank-3/rank-10 PCA-lift control at each trajectory and k. Margin is the minimum real-minus-surrogate compression-proxy margin over block lengths 4 and 16; larger is better. Loss is train-only order-2 model test bits/symbol; smaller is better.

| trajectory seed | k | VAMP loss | best PCA loss | VAMP min margin (bits) | best PCA min margin | VAMP beats both |
|---:|---:|---:|---:|---:|---:|:---:|
| 101 | 8 | 0.433585 | 0.419559 | 5.20 | 3.65 | no |
| 202 | 8 | 0.481750 | 0.423056 | 5.20 | 5.55 | no |
| 303 | 8 | 0.614553 | 0.542805 | 13.00 | 7.30 | no |
| 101 | 16 | 0.731430 | 0.710454 | 4.30 | 2.60 | no |
| 202 | 16 | 0.770833 | 0.727201 | 4.25 | 3.05 | no |
| 303 | 16 | 1.050339 | 0.952287 | 3.90 | 9.00 | no |

Aggregate VAMP mean loss/margin: k=8, 0.509962 / 7.80 bits; k=16, 0.850867 / 4.15 bits. PCA-lift (two ranks, which often produce identical clusters here) mean loss/margin: k=8, 0.461807 / 5.50 bits; k=16, 0.796647 / 4.88 bits. Direct xyz was nearly identical to PCA, as expected for an essentially linear rank-3 observation lift. TICA closely tracked VAMP and did not alter the conclusion.

### Stop/go conclusion

**STOP linear VAMP development for this CLA lane under the preregistered criterion.** VAMP beat the best matched PCA-lift control on both metrics in 0/3 trajectories at k=8 and 0/3 at k=16, versus the required >=2/3. VAMP sometimes improved the compression-proxy margin, but its held-out next-symbol loss was worse in every trajectory/k stratum. This is a bounded result for linear, train-only rank-conditioned models on noisy linear R256 lifts of Lorenz-63; it is not evidence against nonlinear embeddings, other dynamics, or CLA itself.

## Verification, reproducibility, and limitations

- Focused pre-run regressions: `python3 -m unittest tests.test_rank_conditioned_lorenz63 -v` — 6 passed.
- Raw artifacts: `results.json`, `metrics.csv`; aggregate table: `aggregates.csv`; logs/status/timing/environment/checksums stored beside this record.
- The custom blocked validation score is the closest correct implementation needed here: train-fitted left/right singular functions are fixed, validation covariances only normalize and score their cross-covariance Frobenius norm (VAMP-2). This avoids a deeptime API path that would otherwise obscure the explicit train-only rank truncation and conditioning.
- Final checks: `python3 -m compileall -q src tests` passed; `python3 -m unittest discover -s tests -v` passed 115 tests in 37.847 s; `git diff --check` passed.
- Local code commit after evidence/checks: `4423f8f` (`Add leakage-free rank-conditioned VAMP experiment`) on `agent/hd-embedding-cla`; unpushed. Project notebook/run-record updates remain in the outer workspace worktree because it contains extensive pre-existing unrelated changes and untracked records that must not be swept into this commit.
- Limits: only three trajectories; deterministic point estimates without confidence intervals; simple linear noisy lift; test grammar metric is a one-iteration current two-part proxy, not calibrated CLA predictive MDL; circular block surrogates only; validation VAMP-2 favored lag 1 and offered no plateau/CK analysis; near-unit modes remain cautionary.
