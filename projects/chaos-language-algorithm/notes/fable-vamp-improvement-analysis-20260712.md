# Fable VAMP Improvement Analysis
**Date:** 2026-07-12
**Source:** Claude Fable (via subagent), prompted with full CLA/VAMP codebase context
**Status:** Recommendation — not yet implemented

## Core recommendation

Use **regularized, cross-validated VAMP-2 with explicit rank truncation**, not raw covariance inversion and not singular-value clipping. For D=200–300, first reduce the observation space to a statistically supportable rank, then estimate the kinetic map there.

The immediate scientific priority is not a more elaborate VAMP model. It is a longer, leakage-free lifted-Lorenz experiment with direct grammar-recovery metrics and alphabet-matched controls. The completed short sweep already shows that VAMP has not beaten direct xyz k-means, and its near-unit singular values are not reliable kinetic evidence at the current sample size.

---

## 1. Which VAMP variant

### Use VAMP-2 for model selection

Estimate the usual whitened Koopman matrix K_τ = (C00+λ0 I)^{-1/2} C0τ (Cττ+λτ I)^{-1/2}, and retain its singular functions. Select lag, regularization, feature rank, and embedding dimension using a **held-out VAMP-2 score** R2 = Σ σi², computed on validation covariance matrices with singular functions fitted only on training data.

- VAMP-2 is the standard variational score for comparing learned kinetic subspaces.
- Squaring singular values gives a stable additive measure of captured kinetic variance.
- It supports cross-validation without needing reversibility.
- VAMP-1 (R1 = Σ σi) can be a secondary diagnostic but should not drive selection — it weights weak modes more strongly.

### Preserve nonreversibility by default

Keep nonsymmetrized C0τ. TICA/reversible estimates should remain a comparator, not the default. Fit the left singular-function map z(x) = U_d^T (C00+λI)^{-1/2} (x−μ0) and apply that same map to every time point.

---

## 2. Make D=200–300 estimation reliable

### Replace full-space whitening with rank-restricted whitening

With n≈D, the covariance spectrum near zero is mostly estimation noise.

1. Fit centering and all transforms on training blocks only.
2. Compute a thin SVD of the centered snapshot matrices.
3. Restrict covariance calculations to rank r satisfying: retained variance criterion + conservative sample support (r ≤ n_eff/10, capped ~20–40).
4. Perform VAMP whitening and SVD in this r-dimensional space.
5. Map learned singular functions back only when needed.

### Estimate effective, not nominal, sample size

n_eff ≈ (n−τ) / (1 + 2 Σk ρ(k)). Use n_eff, not n, to cap rank. Initial target: at least 5,000 retained points; repeat at 10k and 20k; multiple independently initialized trajectories.

### Regularization hierarchy

A. **Mandatory spectral truncation** — discard eigenmodes below λi/λmax < ε.
B. **Data-adaptive shrinkage** — Ledoit-Wolf or OAS independently for C00 and Cττ. Ridge grid: λ ∈ 10^{−8..−1} × tr(C)/r.
C. **Condition-number constraint** — bounded whitening condition number (~10^6).
D. **Optional dual estimator** — compute in snapshot/Gram space for D≫n.

### Remove singular-value clipping

Do not silently clip σi into [0,1]. Preserve raw values, flag violations, reject/refit. The current blanket "near 1 = invalid" rule is too strong — distinguish constant mode, credible slow modes, and numerical artifacts.

---

## 3. Principled lag selection

Blocked out-of-sample validation, not best in-sample timescale.

Candidate lags on logarithmic grid: τ ∈ {1,2,4,8,16,32,64}.

For every lag:
1. Train/validation blocks with gap ≥ τ.
2. Fit all transforms on training only.
3. Evaluate validation VAMP-2 score at fixed d.
4. Compute implied timescales.
5. Bootstrap for uncertainty.
6. Compare singular subspaces across adjacent lags (principal angles).
7. Test Chapman-Kolmogorov at 2τ, 3τ, ...

Select smallest lag where: implied timescales plateau, subspace stable, validation VAMP-2 near plateau, CK error acceptable, grammar preservation not degrading.

**Separate dynamical and grammatical lag criteria** — optimal Markov lag need not be optimal grammar-preserving lag. Report a Pareto curve.

---

## 4. Direct grammar-preservation diagnostics

### A. Reference-partition agreement

Fit reference symbolization on original xyz. Align labels (Hungarian matching). Measure: AMI, variation of information, transition-matrix divergence, dwell-time distribution distance, n-gram JS divergence (n=2..6), motif precision/recall.

### B. Grammar transfer tests

1. Learn CLA grammar on reference symbols, evaluate codelength on embedded symbols.
2. Learn on embedded, evaluate reference.
3. Compare induced rule expansions and occurrence sets.
4. Compare category memberships.

Primary metric: normalized transfer regret G_regret = [L(S_emb|G_ref) − L(S_emb|G_emb)] / |S_emb|.

### C. Invariance under observation lift

Many lifts of same latent trajectory (orthogonal, anisotropic, nonlinear, noise levels). Recovered grammars should be more similar across observation maps of same latent dynamics than across distinct dynamics.

### D. Better nulls

Block shuffles, phase-randomized surrogates, transition-preserving first-order Markov surrogates, IAAFT surrogates, time-reversed trajectories, parameter-matched nonchaotic/stochastic controls.

### E. Nested validation

Inner blocks for hyperparameter selection; outer blocks for final grammar-preservation claim.

---

## 5. Embedding dimension and microstates

Select d jointly from: cross-validated VAMP-2 increments, bootstrap stability, implied-timescale gaps, downstream grammar transfer regret. Use smallest d within 1 SE of best.

Treat k as rate-distortion parameter. Sweep k at matched alphabet size across VAMP, PCA, random projection, raw-state controls. Compare on Pareto fronts.

---

## 6. Multilag and multiscale VAMP

Only after single-lag pipeline passes ground-truth test. Shared encoder W optimized over several lags: max_W Σ wτ R2(W;τ). Or simpler: concatenate short-lag and plateau-lag normalized coordinates. Only adopt if it reduces grammar transfer regret.

---

## 7. PCCA+ integration into CLA

PCCA+ memberships as **proposal priors**, not forced categories.

1. Cluster VAMP embedding into microstates.
2. Estimate regularized transition model.
3. Apply PCCA+ (or nonreversible coherent-set clustering for strongly nonreversible dynamics).
4. For each macrostate a, generate candidate CLA category: M_a = {i : χ_ia > θ}.
5. Construct membership-weighted CLA context histogram.
6. Rank proposals by membership coherence + contextual JS similarity + expected MDL gain.
7. Submit to normal CLA edit/MDL machinery.
8. Accept only if exact reconstruction retained and MDL improves.

---

## 8. Priority order

### P0 — Correct scientific validation (highest impact)
1. Increase trajectories to 5k/10k/20k points.
2. Add matched PCA, random projection, raw xyz, no-embedding k-means controls.
3. Implement reference-symbol and bidirectional grammar-transfer metrics.
4. Use nested blocked validation and multiple lifts/noise seeds.

### P1 — Repair numerical estimation
5. Add preliminary rank truncation.
6. Add adaptive/tuned regularization.
7. Remove singular-value clipping.
8. Separate trivial stationary modes from nontrivial kinetic modes.
9. Record condition numbers and train-vs-validation singular values.

### P2 — Lag and dimension selection
10. Implement lag grids, blocked cross-validated VAMP-2, bootstrap IT plateaus, subspace stability, CK tests.
11. Jointly select d and k by rate-distortion/grammar-preservation Pareto.

### P3 — CLA integration
12. Add PCCA/coherent-set memberships as soft category proposal seeds.
13. Score proposals through contextual JS and exact MDL acceptance.
14. Add grammar-transfer regret and rule/category stability to experiment outputs.

### P4 — Multiscale models
15. Only if short- and long-lag objectives conflict after P0–P3.
16. Consider nonlinear VAMPnets only after linear regularized baseline is validated and data volume is much larger.

---

## Key insight

The decisive change is conceptual: VAMP should be treated as a **cross-validated kinetic estimator inside a paired grammar-preservation experiment**, not merely as a preprocessing transform whose success is inferred from compressibility.
