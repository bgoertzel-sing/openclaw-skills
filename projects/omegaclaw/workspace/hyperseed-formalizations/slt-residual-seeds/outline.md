# SLT-Guided Residual Seeds: Outline (Revised)

**Tentative title:** SLT-Guided Residual Seeds — Weakness, Evidence Geometry, and Refinement DAGs for Transformer Adaptation

**Status:** Revised outline incorporating Protocosmobot's five first-round corrections + three second-round checks + five third-round operational fixes + fourth-round gates + fifth-round citation/claim cleanup + sixth-round Holm family resolution + seventh-round commit-reference correction + eighth-round §6 consistency fix and main.tex quarantine + ninth-round exhaustive Holm enumeration + tenth-round per-test explicit family enumeration + eleventh-round unified Holm family (option a) + twelfth-round equivalence-test fix and α-sweep scope clarification. Claim 4 admitted; LaTeX may proceed.
**Date:** 2026-07-28 (rev. 16)
**Gate 3 verification record:** Rev. 9 (commit `b0e0465`), SOURCES.md fresh-clone transcript at commit `326d4f1`.
**main.tex status:** Provisional/unreviewed. Created during the drafting embargo (a process deviation). Claim 4 now admitted (rev. 15); LaTeX drafting may proceed.
**Author:** ProtomegaTron
**Reviewer:** Protocosmobot
**Location:** `hyperseed-formalizations/slt-residual-seeds/outline.md`
**Imports from 0014:** Frozen interface (Def. 2.1), Evidence record (Def. 2.3), Counterfactual factor closure (Def. 2.5), Matched budget (Def. 2.2), H0–H6 hypothesis ladder. These are cited, not re-derived.
**0014 citation source:** See `SOURCES.md` (co-located) for canonical retrieval paths. All citations resolve from the checked-out repository root via the source manifest, not from an agent workspace.

---

## Five claims

### Claim 1 — Residual seeds are local evidence factors, not activation features

**[Correction 1 applied: replaced biconditional with conditional; stated product-model/prior and asymptotic assumptions; interaction remainder treated as hypothesis.]**

A residual correction r_c attached to a frozen base model B decomposes the excess loss landscape *under the following assumptions:*

1. **Product-model assumption:** the parameter space admits a product factorization θ = (θ_1, …, θ_k) such that the prior π(θ) = Π_c π_c(θ_c), i.e., components are a priori independent.
2. **Asymptotic regime:** n is large enough relative to the singularity structure that the free-energy asymptotic F_n = nL̂_n + λ log n − (m−1) log log n + O(1) applies (Watanabe's main theorem).
3. **Dominated interaction remainder (hypothesis, not established fact):** the interaction term R(θ) in K(θ) = Σ_c K_c(θ_c) + R(θ) satisfies |R| < η for a threshold η to be empirically determined.

When these assumptions hold, the global LLC approximately equals the sum of per-seed LLCs; the Bayesian evidence approximately factorizes; and each seed has a quasi-independent evidence neighborhood.

**Epistemic status of the interaction remainder:** The smallness of R is a *testable hypothesis*, not a sufficient proof of factorization. Even if R is empirically small in a given model, this does not establish that the decomposition is coordinate-invariant or structure-revealing — it establishes only that the product-prior decomposition is a good approximation at the observed sample size. The decomposition could break under distribution shift, scale change, or different priors.

**Source claims:** (see `SOURCES.md` for retrieval paths)
- "If the evidence factorizes across modules, the global LLC is the sum of module LLCs." — [Weakness-SL]
- "Do not promote a residual basis because it reconstructs well. Promote it because R is small." — [SLT-ResLayers]
- Evidence-ratio → soft-accuracy bridge, O(λ/n) correction: [SLT-Accuracy] §1–2

**Formal objects:** ResidualSeed r_i, EvidenceNeighborhood W(r_i, c), LLC λ(r_i, c), Factorization F = {r_i}, InteractionRemainder R_F, DominatedInteractionHypothesis(F, c, η).

**Non-overlap with 0014:** 0014 defines frozen interfaces, teacher-gap closure, and representation contests. This claim adds the LLC-additivity criterion as the promotion gate *within* 0014's frozen-interface scaffold. It does not redefine the interface.

---

### Claim 2 — LLC interaction information as a proposed diagnostic for seed coupling type

**[Correction 2 applied: taxonomy labeled "proposed diagnostic"; surrogates distinguished from direct estimators.]**

The LLC interaction information between seeds a, b:

> I_λ(a; b) = λ_a + λ_b − λ_{ab}

**Proposed diagnostic taxonomy** (not established as proven classification):

| Sign of I_λ | Proposed interpretation | Status |
|---|---|---|
| I_λ > 0 | Redundant/shared singular structure → merge candidate | Hypothesis: plausible from SLT decomposition theory, not proven as a classification theorem |
| I_λ < 0 | Synergistic/emergent structure → assembly or mediator needed | Hypothesis: same status |
| I_λ ≈ 0 | Factorizable independence | Consistent with Claim 1's product-model assumption |

This taxonomy is a *proposed diagnostic framework*, not a proven classifier. The cited sources (*SLT-SubRep-v5*) suggest the sign interpretation but do not prove it as a general classification of coupling types.

**Surrogate estimators are not interchangeable with I_λ.** The mixed-Hessian norm ‖H_{ab}‖ and commutator dominance Comm(a, b) are computationally tractable surrogates that correlate with the true LLC interaction information under regularity conditions, but:
- They measure different geometric quantities (local curvature cross-terms vs. singularity-structure overlap).
- Their agreement with the true I_λ degrades near degenerate singularities.
- Discrepancies between surrogates should be reported as evidence of estimator limitations, not resolved by fiat.

**Source claims:** (see `SOURCES.md` for retrieval paths)
- I_λ > 0 / < 0 interpretation: [SLT-SubRep]
- Computable surrogates via mixed-Hessian blocks and commutator diagnostics: [Weakness-SL] §appendix; [SLT-ResLayers] §"Third, compute mixed-Hessian / commutator dominance"

**Formal objects:** InteractionInformation I_λ(a, b), CommutatorDominance Comm(a, b), MixedHessianNorm ‖H_{ab}‖, SurrogateAgreement δ(Comm, ‖H_{ab}‖, I_λ).

**Falsifiable prediction:** In a small transformer with known modular structure (e.g., two-task mixture), per-seed LLC estimates should yield I_λ ≈ 0 between task-specific seeds and I_λ > 0 between capacity-sharing seeds. Additionally, the surrogate measures should agree with direct LLC estimates to within stated tolerances (to be preregistered). Measurable with the `devinterp` LLC estimator. Surrogate-direct discrepancies, if found, would weaken the diagnostic taxonomy rather than the underlying SLT theory.

---

### Claim 3 — Refinement DAGs are the operational structure of seed ecology

Seeds do not exist in a fixed decomposition. They participate in a refinement DAG whose moves include split, merge, mediate, specialize, demote, and transfer. Each move is scored by the pregate objective:

> J(F) = n·L̂_F + λ̂_F·log n − log π(F) + α·Comm(F) + β·Leak(F) + γ·Regret(F) + δ·Interaction(F)

The structure controller selects refinement moves that decrease J with stable associative signatures (see Claim 4 for the distinction between association and causation here).

**Source claims:** (see `SOURCES.md` for retrieval paths)
- Refinement-DAG structure with weakness/evidence scoring: [Weakness-SL] §refinement DAGs, quantale message-passing
- The seven-term pregate formula: [SLT-ResLayers] §"Use an SLT-informed pregate"
- Regime-change detection via module-wise LLC signatures triggers refinement: [SLT-Regime]

**Formal objects:** RefinementMove m: F → F', PregateScore J(F, c), AssociativeSignature σ(r_i, c), RegimeSignature Σ(F, t).

**Connection to 0014:** 0014's H1 representation contest (Def. 2.8) compares arm classes at matched budget. Claim 3 extends this to a *dynamic* contest: the contest is not a one-shot comparison but a DAG of refinement moves, each subject to the same evidence gates 0014 defines.

---

### Claim 4 — Additivity deviation is a measurable proxy for compositional evidence leakage

**[Correction 3 applied: removed biconditional; replaced causal language with associative; added confidence-interval and intervention requirements.]**

**This is the single novel bridge claim.** SLT's RLCT decomposition across components predicts that deviations from LLC additivity signal geometric interactions between singular regions. In Hyperseed terms, these deviations are *associative signatures* of evidence leakage between refinement stages.

> Δ_add(F) = |λ_{joint} − Σ_c λ_c|

**Epistemic downgrade from earlier version:**

1. **No biconditional.** Δ_add > 0 is *necessary but not sufficient* evidence that factorization F fails to decompose the evidence geometry. Finite-sample bias in LLC estimation, prior misspecification, and MCMC mixing artifacts can all produce non-zero Δ_add even when the true singularity structure decomposes. The claim is: *Δ_add significantly exceeding zero, after accounting for estimator uncertainty, is evidence against clean factorization.* The converse (Δ_add ≈ 0 implies good factorization) is better supported but still conditional on the product-prior assumption from Claim 1.

2. **Association, not causation.** The prediction is that Δ_add *correlates with* graph-theoretic cross-stage dependency in the refinement DAG. This is an associative claim. Upgrading to causal language requires an intervention that varies cross-stage coupling while **preserving parameter count and component decomposition**. Three candidate interventions, ordered by preference:
   - **(a) Coupling-strength interpolation.** Parameterize cross-stage connections with a scalar α ∈ [0,1]. At α=1 the architecture is unchanged; at α=0 cross-stage information flow is severed. Crucially, all parameters remain in the model (zeroed weights are frozen, not removed), so total parameter count, component count, and decomposition structure are preserved. Predict: Δ_add decreases monotonically as α → 0.
   - **(b) Calibrated noise injection at stage boundaries (secondary/optional).** Add i.i.d. Gaussian noise ε ~ N(0, σ²) to activations at inter-stage boundaries, sweeping σ from 0 (original) to a level that effectively decorrelates stages. Architecture and parameter count are exactly preserved. **Additional matching requirements (if used):** at each noise level σ, the injected model must be retrained or fine-tuned until (i) marginal activation variance at each layer matches the α-sweep baseline to within 5%, and (ii) predictive loss on the evaluation split matches the α-sweep baseline at the corresponding effective coupling strength to within 5%. Without these calibrations, noise injection changes activation statistics and is a confound, not a clean intervention. Predict: Δ_add decreases as σ increases, conditional on variance and loss matching.
   - **(c) Matched-complexity control (if architectural changes are unavoidable).** If a structural ablation (e.g. skip-connection removal) is used, it must be paired with a control condition: the same architectural change but with re-initialized (random) weights in the modified pathway, matching parameter count and decomposition. The difference in Δ_add between the ablation and the matched control isolates the coupling effect from the complexity-change confound.
   Until such an intervention is run, "Δ_add tracks cross-stage dependency" means association.

**Confidence-interval requirement:** All reported Δ_add values must include:
- Bootstrap or MCMC-derived confidence intervals on individual λ_c estimates.
- Propagated uncertainty on Δ_add itself (not just point estimates).
- Multiplicity-corrected significance: Δ_add is declared “meaningfully non-zero” iff its Holm-adjusted p-value < 0.05 across the unified confirmatory family of N = 5 + k(k+1)/2 tests (see §2 and §6 of the preregistered protocol).

**Source claims:** (see `SOURCES.md` for retrieval paths)
- LLC additivity and its failure: [Weakness-SL]; [SLT-SubRep] §interaction complexity
- Cross-stage dependency → counterfactual factor closure: [CausalFibres] Def. 2.5
- The initial synthesis hypothesis: "deviations from additivity signal geometric interactions between singular regions" [InitSynth]

**Falsifiable experimental check (revised):** Take a small transformer (or synthetic model with known singular structure). Compute per-layer LLC estimates via the `devinterp` local learning coefficient estimator with stated hyperparameters. Report Δ_add with confidence intervals. Independently compute a graph-theoretic cross-stage dependency score on the refinement DAG. Test for statistically significant correlation. If Δ_add is significantly elevated but the DAG shows clean stage separation, the associative claim is falsified. If they correlate, the Hyperseed–SLT bridge has non-trivial empirical support — but *not* causal evidence unless an intervention experiment (described above) is also run.

**Why novel:** The individual pieces (LLC decomposition, refinement DAGs, counterfactual factor closure) exist in the source papers. The novel claim is that Δ_add is the *quantitative observable* that connects SLT geometry to Hyperseed compositional structure — as a measurable, falsifiable associative bridge.

---

### Claim 5 — SLT-guided residual learning as a prototype for evidence-based adaptation in LLC-estimable systems

**[Correction 4 applied: restricted universality conjecture to defined model class.]**

The seed ecology pattern — base process + controlled corrective factors, scored by evidence geometry, refined through a DAG of structural moves, monitored for regime change — extends beyond residual layers to a defined class of systems.

**Required model class for the universality conjecture:**

A system belongs to the *LLC-estimable component-decomposable* class iff:
1. It admits a finite parametric description θ ∈ Θ ⊂ ℝ^d.
2. Its loss function L(θ) is real-analytic (or admits a resolution of singularities).
3. Local learning coefficients are estimable at each component (the posterior concentrates sufficiently for MCMC-based LLC estimation to converge).
4. It has an explicit component decomposition F = {c_1, …, c_k} with defined parameter subspaces θ_{c_i} and a product-prior factorization.
5. The interaction remainder R(θ) from Claim 1 is well-defined and estimable.

**Within this class**, the seed-ecology dynamics are conjectured to hold:

- **Incremental compression:** corrective components are compression features for the base model's error stream.
- **Evidence gating:** promotion/demotion is governed by LLC-additivity checks, not reconstruction error alone.
- **Regime detection:** LLC/signature shifts trigger structural revision (*SLT for regime-change detection*).
- **Interaction diagnostics:** coupling type is diagnosed via I_λ (Claim 2's proposed taxonomy).
- **Goal stability limits:** SLT diagnostics detect structural shifts but not semantic truth; the semantics route via distinctions → partitions → symmetries → singularities adds the missing layer (*SLT-Goal-Stability_v4*, *SLT-Semantics-v2*).

**Explicitly excluded from the conjecture:** non-parametric models, models where LLC estimation does not converge, systems without a natural component decomposition, and infinite-dimensional parameter spaces (unless a finite-dimensional effective description exists).

**Source claims:** (see `SOURCES.md` for retrieval paths)
- Regime-change detection and its limits: [SLT-GoalStab]
- Semantics–geometry connection: [SLT-Semantics]
- SubRep interaction complexity: [SLT-SubRep]
- Evolution/EDA free-energy geodesics: [SLT-Evolution]

**Formal objects:** LLCEstimableSystem, ComponentDecomposableModel, AdaptationProtocol (parameterized by evidence gates, refinement moves, regime monitors, semantic registration).

**Conjecture (restricted AGI adaptation):** Any system in the LLC-estimable component-decomposable class that maintains a base predictive process, an ecology of modular corrective seeds scored by local evidence, and a refinement DAG over candidate factorizations will exhibit the same LLC-additivity / interaction-information / regime-signature dynamics described in Claims 1–4. This is the restricted Hyperseed universality claim for evidence-based adaptation.

---

## Preregistered Experimental Protocol

**[Correction 5 applied: explicit preregistration of estimator, uncertainty method, component-to-DAG mapping, and analysis plan.]**

Before running the falsification experiment for Claims 1, 2, and 4, the following must be preregistered:

### 1. LLC Estimator Specification
- **Estimator:** `devinterp` local learning coefficient estimator (citation: Lau et al., 2024).
- **MCMC method:** SGLD with specified step size schedule, number of chains, burn-in length, and thinning interval.
- **Convergence diagnostic:** R̂ < 1.05 across chains; effective sample size ≥ 200 per component.
- **Hyperparameters to fix before data collection:** learning rate, temperature schedule, number of posterior samples.

### 2. Uncertainty Quantification and Multiplicity Correction
- **Per-component λ_c:** Bootstrap confidence intervals (B ≥ 1000 resamples) or MCMC posterior credible intervals (95%).
- **Δ_add:** Propagated via delta method or bootstrap on the sum; reported with 95% CI.
- **I_λ(a, b):** Same uncertainty propagation; reported with 95% CI.
- **Significance threshold (unadjusted):** Δ_add is declared "meaningfully non-zero" iff the 95% CI excludes zero.

**Multiplicity correction (preregistered):**

The experiment involves simultaneous statistical tests across multiple comparisons. **Option (a) is adopted:** one unified confirmatory family containing every control-admission test, every headline claim test, every per-component Δ_add test, and every per-pair I_λ test. The **confirmatory comparison family** consists of:

| Group | Tests | Supports | H₀ | Count |
|-------|-------|----------|-----|-------|
| A1 | Null control Δ_add | Calibration gate | |Δ_add| ≥ ε (equivalence, TOST) | 1 |
| A1 | Positive control Δ_add | Power gate | Δ_add = 0 | 1 |
| A2 | Spearman ρ(Δ_add, dependency) | Claim 4 | ρ = 0 | 1 |
| A2 | Sign accuracy of I_λ vs structure | Claim 2 | Accuracy ≤ chance | 1 |
| A2 | Prevalence of R < η | Claim 1 | Prevalence ≤ threshold | 1 |
| A3 | Δ_add(c_i) per component | Claim 4 | Δ_add(c_i) = 0 | k |
| A4 | I_λ(c_i, c_j) per pair | Claim 2 | I_λ(c_i, c_j) = 0 | k(k−1)/2 |

**Total confirmatory family size:** N = 5 + k + k(k−1)/2 = 5 + k(k+1)/2, where k is the number of components in the test model (fixed before data collection per §3). This family is fixed before data collection.

**Instantiated membership (k = 6):** N = 5 + 6·7/2 = 26. For k = 12: N = 5 + 12·13/2 = 83.

**Holm sequential rejection thresholds (general, α_family = 0.05):**

The Holm procedure orders all N raw p-values smallest to largest and tests sequentially. For ordered position j ∈ {1, …, N}:

> Rejection threshold at position j: α/(N − j + 1)

Rejection stops at the first j where p_(j) > α/(N − j + 1); all subsequent hypotheses are retained regardless of their raw p-values.

**Example thresholds (k = 6, N = 26):**

| Ordered position j | Threshold α/(N−j+1) |
|---|---|
| 1 (smallest p) | 0.05/26 ≈ 0.00192 |
| 2 | 0.05/25 = 0.00200 |
| … | … |
| 13 (midpoint) | 0.05/14 ≈ 0.00357 |
| … | … |
| 25 | 0.05/2 = 0.02500 |
| 26 (largest p) | 0.05/1 = 0.05000 |

**Exhaustive inventory of all statistical comparisons in this protocol:**

Every statistical comparison mentioned anywhere in this document is classified below. No comparison exists outside this inventory. Let k denote the number of components in the test model (fixed before data collection per §3).

**A. Confirmatory family (N = 5 + k(k+1)/2, decision-governing).**
These are the only tests whose outcomes can support or falsify any claim. All use Holm-adjusted p-values at FWER α = 0.05. Option (a) is adopted: one unified family containing every control-admission test, every headline claim test, every per-component Δ_add test, and every per-pair I_λ test.

**A1. Control-admission tests (2 tests):**

| # | Test | H₀ | Supports / falsifies | Count |
|---|------|-----|----------------------|-------|
| A1.1 | Null control: aggregate Δ_add on null-control confirmation set (equivalence test) | |Δ_add| ≥ ε (TOST; ε = preregistered practical-equivalence margin) | Estimator calibration gate | 1 |
| A1.2 | Positive control: aggregate Δ_add on positive-control confirmation set | Δ_add = 0 (one-sided) | Estimator power gate | 1 |

**A2. Headline claim tests (3 tests):**

| # | Test | H₀ | Supports / falsifies | Count |
|---|------|-----|----------------------|-------|
| A2.1 | Spearman ρ(Δ_add, cross-stage dependency) | ρ = 0 | Claim 4 (primary bridge test) | 1 |
| A2.2 | Sign accuracy of I_λ vs known modular structure | Accuracy ≤ chance | Claim 2 (diagnostic taxonomy) | 1 |
| A2.3 | Prevalence of R < η across components | Prevalence ≤ pilot-calibrated threshold | Claim 1 (factorization hypothesis) | 1 |

**A3. Per-component Δ_add tests (k tests):**

| # | Test | H₀ | Supports / falsifies | Count |
|---|------|-----|----------------------|-------|
| A3.i (i = 1, …, k) | Δ_add(c_i) for component c_i | Δ_add(c_i) = 0 | Claim 4 (per-component additivity deviation) | k |

Each per-component Δ_add(c_i) is individually tested for significance within the Holm family. These values also serve as data points for the Spearman ρ headline test (A2.1); the two uses address different questions (individual non-zero deviation vs. correlation with dependency structure).

**A4. Per-pair I_λ tests (k(k−1)/2 tests):**

| # | Test | H₀ | Supports / falsifies | Count |
|---|------|-----|----------------------|-------|
| A4.ij (i < j) | I_λ(c_i, c_j) for component pair (c_i, c_j) | I_λ(c_i, c_j) = 0 | Claim 2 (per-pair interaction information) | k(k−1)/2 |

Each per-pair I_λ(c_i, c_j) is individually tested for significance within the Holm family. The signs of significant pairs also feed into the sign-accuracy headline test (A2.2); the two uses address different questions (individual non-zero interaction vs. aggregate taxonomic accuracy).

**Total confirmatory tests: N = 2 + 3 + k + k(k−1)/2 = 5 + k(k+1)/2.**

**B. Descriptive / intermediate statistics (no claim-bearing capacity).**
Each statistic below is reported for transparency with unadjusted CIs. None enters the confirmatory family. None can independently support or falsify any claim. Cherry-picking individual values as evidence for or against a claim is prohibited.

*Note: Per-component Δ_add(c_i) and per-pair I_λ(c_i, c_j) were classified as descriptive in rev. 14. Under option (a) (rev. 15), they are promoted to the confirmatory family (A3, A4). The remaining descriptive statistics are:*

| # | Statistic | Count | Role | Reporting | Claim-bearing capacity |
|---|-----------|-------|------|-----------|------------------------|
| B1 | R(c_i) for each component c_i, i = 1, …, k | k | Data points aggregated into prevalence fraction (test A2.3); each R(c_i) is compared against η = 0.1 × λ_max to compute the fraction | Unadjusted 95% CI per value | **None.** Individual R(c_i) < η classifications are inputs to the prevalence test; no single classification is tested for significance. |
| B2 | λ_{c_i} for each component c_i, i = 1, …, k | k | Building blocks for computing Δ_add(c_i) = |λ_{joint} − Σ_j λ_{c_j}| at each component | Bootstrap/MCMC posterior CI per value | **None.** Individual λ estimates are inputs to Δ_add, not tested independently. |
| B3 | Surrogate agreement δ(Comm(c_i, c_j), ‖H_{c_i c_j}‖, I_λ(c_i, c_j)) for each pair (i < j) | k(k−1)/2 | Estimator-quality diagnostic: checks whether the computationally tractable surrogates agree with direct LLC interaction estimates | Unadjusted 95% CI per pair | **None.** No claim depends on surrogate agreement; discrepancies are noted as estimator limitations. |

**Total descriptive statistics: 2k + k(k−1)/2 values.** For a k = 6 component model, this is 27 values. For k = 12, this is 90 values. None is tested for significance; none bears on any claim.

**C. Separate preregistered family (α-coupling sweep, follow-up causal-upgrade experiment only).**
This family is not part of the confirmatory N = 5 + k(k+1)/2 and is registered before the intervention experiment begins.

Let k_α = 11 (α-levels: 1.0, 0.9, 0.8, …, 0.1, 0.0) and m = number of components in the intervention model.

| # | Test | Count | Description |
|---|------|-------|-------------|
| C1 | Δ_add(c_i; α_j) for each component c_i at each coupling level α_j | k_α × m = 11m | Per-component additivity deviation measured at each of 11 α-levels |
| C2 | Monotonicity of Δ_add(c_i; ·) vs α for each component c_i | m | One-sided Jonckheere–Terpstra trend test (or Page's test) per component: H₀ is that Δ_add does not decrease as α → 0 |

**Total intervention family size: N_intervention = 11m + m = 12m tests,** Holm-corrected at FWER α = 0.05. This family is frozen before the intervention experiment begins and does not overlap with the confirmatory N = 5 + k(k+1)/2.

**Scope limitation:** The α-sweep intervention family (C) is designed exclusively for a follow-up causal-upgrade experiment. **It cannot support Claims 1–4 of this paper.** Claims 1–4 are associative claims whose evidence comes solely from the confirmatory family (A). The α-sweep, if it yields positive results, would upgrade Claim 4's associative language to causal language in a subsequent paper or revision — but it is neither necessary for nor capable of establishing the present claims.

**D. Completeness guarantee.**
The three categories above (A, B, C) exhaust every statistical comparison mentioned anywhere in this document. Any future analysis not listed in A, B, or C must be preregistered as a new family or explicitly classified as descriptive/exploratory before data collection. Post hoc additions to the confirmatory family (A) are prohibited. Post hoc additions to the intervention family (C) must be preregistered before intervention data collection. Any statistic not in A or C is descriptive by default and cannot bear on any claim.

**Correction method:** Holm–Bonferroni sequential rejection procedure (Holm, 1979). This controls the family-wise error rate (FWER) at α_family = 0.05 while being uniformly more powerful than Bonferroni.
- Order all N p-values: p_(1) ≤ p_(2) ≤ … ≤ p_(N).
- Reject H₀_(j) iff p_(j) ≤ α_family / (N − j + 1) for all j′ ≤ j.
- Equivalently, report Holm-adjusted p-values: p̃_(j) = max_{j′≤j} { (N − j′ + 1) · p_(j′) }.
- An individual comparison is declared significant iff its Holm-adjusted p-value < 0.05.

**Adjusted confidence intervals:** Where CIs are reported alongside Holm-corrected tests, use Bonferroni-adjusted CIs at level 1 − α_family/N per comparison (conservative but consistent with the FWER control). These replace the unadjusted 95% CIs in all multi-comparison contexts.

**Rationale for Holm over alternatives:** Holm–Bonferroni controls FWER (appropriate here because a single false positive about coupling structure would undermine the bridge claim) while being strictly more powerful than Bonferroni. FDR-controlling methods (Benjamini–Hochberg) would be appropriate if the goal were screening many components for follow-up, but here each comparison bears directly on the claim; FWER control is the correct standard.

### 3. Component-to-DAG Mapping
- **Component definition:** Each residual block (or attention head / MLP sublayer, depending on granularity — to be fixed before experiment) is one component c_i.
- **DAG construction:** Edges from c_i to c_j iff information flow exists (measured by gradient attribution or activation patching). Edge weights from mutual information or ablation impact.
- **Cross-stage dependency score:** Weighted edge density between non-adjacent DAG stages. Formal definition to be stated as a graph-theoretic formula before data collection.

### 4. Synthetic Controls (Pilot / Confirmation Split)

**Split design to prevent calibration circularity:**

Synthetic control data is generated once and split into two disjoint sets before any analysis:

- **Pilot calibration set (50% of synthetic control runs).** Used *exactly once* for threshold calibration (§6). After calibration thresholds are frozen, this data is permanently set aside and never used for any admission decision, significance test, or claim evaluation. The pilot is consumed by threshold-setting.
- **Held-out confirmation set (remaining 50% of synthetic control runs).** Reserved exclusively for the admission tests described below. Never examined during calibration. All control-pass/fail decisions use only this set.
- **Split ratio:** 50/50, preregistered and fixed. Membership is assigned via a preregistered random seed before any outcome inspection; the assignment vector is committed to the repository before LLC estimation begins.
- **No adaptive reallocation.** If the pilot set is too small for stable threshold estimation (coefficient of variation of threshold estimates across bootstrap resamples > 0.2), do not borrow from the confirmation set. Instead, increase the total sample size N using variance estimates from the pilot, generate new synthetic controls at the larger N, re-split 50/50 with a fresh preregistered seed, and repeat calibration. The confirmation set is never examined during calibration under any circumstance.

**Controls (evaluated on confirmation set only):**

- **Null/negative control (no coupling by construction).** Two independent MLPs sharing no parameters, trained on disjoint tasks from the same data distribution. Components are a priori independent by construction. Expected result: Δ_add within the practical-equivalence margin ε, I_λ ≈ 0 between the two networks, R < η. **Admission criterion:** The null control passes via a preregistered TOST (Two One-Sided Tests) equivalence test — we must positively reject H₀: |Δ_add| ≥ ε at Holm-adjusted p < 0.05, establishing that Δ_add is practically equivalent to zero. Mere failure to reject H₀: Δ_add = 0 is not sufficient for control admission, because absence of evidence against zero is not evidence of equivalence. If the equivalence test fails (i.e., we cannot positively establish |Δ_add| < ε), the estimator or its hyperparameters are miscalibrated or the equivalence margin is too tight; do not proceed to the test model.
- **Positive control (known coupling, explicit decomposition).** Two MLPs (component₁, component₂) connected by a fixed linear coupling layer W_mix of known rank r, trained jointly on the same task mixture. The component decomposition is defined a priori: component₁ = MLP₁ parameters, component₂ = MLP₂ parameters, coupling = W_mix. Because W_mix introduces an explicit cross-component coupling, we *preregister the expectation* that Δ_add > 0. The preregistered prediction is: *Δ_add is expected to be significantly nonzero (Holm-adjusted p < 0.05) on the positive control, with the effect size estimated from the pilot calibration set.* No analytic proportionality between Δ_add and rank/norm of W_mix is claimed—computing the RLCT contribution of the coupling would require a resolution of singularities for the specific loss surface under the chosen prior, which has not been performed. This positive control has both known non-zero coupling and an explicit component decomposition — a single dense MLP would not qualify because its component decomposition is not defined a priori. Expected result: Δ_add >> 0, |I_λ| >> 0, R > η. If the estimator fails to detect non-factorizability on this positive control, the estimator lacks power; do not proceed.
- **Decision rule for controls (applied to confirmation set only):** Both controls must pass before any claims about the test model are made. Null control: TOST equivalence test rejects H₀: |Δ_add| ≥ ε at Holm-adjusted p < 0.05 (positively establishing practical equivalence to zero). Positive control: Holm-adjusted p < 0.05 for H₀: Δ_add = 0 (establishing that the estimator detects known coupling).

### 5. Model and Data
- **Test model:** Small transformer (≤ 6 layers) trained on a two-task mixture.
- **Held-out model:** A second, architecturally distinct model (e.g. a 4-layer transformer if the test model is 6 layers, or a convolutional residual network) trained on the same data. Predictions for this held-out model are registered before fitting. If Claims 1–4 hold on the test model but fail on the held-out model, the claims are model-specific, not general.
- **Training data:** Fixed dataset, split specified before training.
- **LLC estimation data:** Training split (for loss landscape exploration).
- **Evaluation data:** Held-out split, not used for LLC estimation or estimator tuning.

### 6. Numerical Decision Thresholds (preregistered)

**Decision governance (binding):** All significance decisions in this protocol—control admission, claim evaluation, per-component Δ_add tests, and per-pair I_λ tests—use Holm-adjusted p-values (FWER α = 0.05) within the unified confirmatory family of N = 5 + k(k+1)/2 tests defined in §2. Unadjusted p-values and unadjusted CIs are reported for transparency only and never govern any decision. Bonferroni simultaneous CIs are reported alongside Holm-adjusted tests; they are conservative but consistent with FWER control. The remaining descriptive statistics (individual R(c), λ_{c}, surrogate agreement δ) are reported with unadjusted CIs for transparency and cannot independently support any claim.

**Multiplicity handling:** The unified confirmatory Holm family (N = 5 + k(k+1)/2, option (a)) and correction method are frozen before data collection (§2). The α-coupling sweep, if executed as a follow-up, has its own separately preregistered family (§2).

- **Δ_add significance (controls and per-component):** Control-admission Δ_add tests use Holm-adjusted p-values within the unified N = 5 + k(k+1)/2 family. Null control: TOST equivalence test, H₀: |Δ_add| ≥ ε, passes iff Holm-adjusted p < 0.05 (positive establishment of practical equivalence to zero; mere failure to reject zero does not suffice). Positive control: H₀: Δ_add = 0, passes iff Holm-adjusted p < 0.05. Per-component Δ_add(c_i) tests (H₀: Δ_add(c_i) = 0) also use Holm-adjusted p-values within the same family. All reported with Bonferroni-adjusted CI at level 1 − 0.05/N.
- **Practical-equivalence margin ε (null control):** ε is calibrated from the pilot calibration set (§4) using the observed Δ_add variability on the null-control pilot runs. Specifically: ε = max(2 × SD_pilot(Δ_add), 0.05 × λ_max), where SD_pilot is the standard deviation of Δ_add across pilot null-control runs and λ_max is the largest per-component LLC. The margin is frozen after pilot calibration and before any confirmation-set data is examined. If the pilot yields unstable ε estimates (bootstrap CV > 0.2), increase total sample size as specified in §4.
- **Interaction remainder threshold:** η = 0.1 × λ_max, where λ_max is the largest per-component LLC. R/λ_max < 0.1 counts as "dominated."
- **I_λ magnitude (confirmatory):** Individual I_λ(c_i, c_j) values are tested for significance (H₀: I_λ(c_i, c_j) = 0) within the unified Holm family (A4). Reported with Bonferroni-adjusted CI at level 1 − 0.05/N. An individual I_λ is classified as “significant” iff its Holm-adjusted p-value < 0.05 within the unified family. The signs of significant pairs feed into the sign-accuracy headline test (A2.2).
- **Correlation threshold (Claim 4 primary test):** Spearman ρ with Holm-adjusted p < 0.05 (one-tailed). **Threshold calibration:** The minimum detectable ρ is set using the pilot calibration set (§4), targeting ≥ 80% power at the pilot-observed effect size. The procedure: (1) compute observed Δ_add–dependency correlations on the pilot positive-control data, (2) estimate the effect size, (3) compute the required ρ threshold for 80% power at that effect size and the confirmation-set sample size, (4) freeze that threshold. If the pilot effect is too small for 80% power at the confirmation-set size, report the achieved power honestly and note the study is underpowered for this effect. **The pilot calibration set is consumed by this step and never reused for confirmation tests.**
- **Sign accuracy (Claim 2):** Agreement between sign(I_λ) and known modular structure. **Threshold calibration:** Using the pilot calibration set, compute the null-distribution sign accuracy (random assignment baseline) and set the threshold at 2σ above null expectation. Freeze Cohen's κ threshold accordingly. **Pilot set consumed.**
- **Factorization prevalence (Claim 1):** R < η for a preregistered fraction of components. **Threshold calibration:** Using the pilot calibration set, compute R for all components in both positive and null controls, then set the prevalence threshold at the ROC-optimal discrimination point. If controls show perfect separation, use 80% (conservative). Freeze before examining confirmation data. **Pilot set consumed.**

**Circularity prevention:** The three calibration steps above each consume the pilot set. Once thresholds are frozen after step (3) of each calibration, the pilot data is set aside. All subsequent control-pass/fail decisions and claim evaluations use only the held-out confirmation set (§4). No threshold is revised after examining confirmation data.

### 7. Analysis Plan

**Decision governance (restated from §6):** Holm-adjusted p-values within the unified confirmatory family (N = 5 + k(k+1)/2, defined in §2) govern all accept/reject decisions throughout this analysis plan. Bonferroni-adjusted simultaneous CIs are reported for descriptive transparency; they do not govern decisions. Raw (unadjusted) p-values are reported alongside adjusted values but never used for decisions.

- **A1 — Control admission (2 tests):**
  - **A1.1 — Null control (equivalence test):** TOST on Δ_add for null control (confirmation set). H₀: |Δ_add| ≥ ε, where ε is the preregistered practical-equivalence margin frozen after pilot calibration (§6). Holm-adjusted p < 0.05 required — i.e., we must positively reject the hypothesis that Δ_add is outside the equivalence margin. Mere failure to reject Δ_add = 0 is not control admission.
  - **A1.2 — Positive control:** Δ_add > 0 on positive control (confirmation set). Holm-adjusted p < 0.05 required.
  - **Sequencing:** Both controls must pass before any other tests are evaluated. If either fails, the estimator is miscalibrated and no claim tests are run.
- **A2 — Headline claim tests (3 tests):**
  - **A2.1 — Primary (Claim 4):** Spearman correlation between per-component Δ_add and cross-stage dependency score. Report coefficient, Holm-adjusted p-value, raw p-value, and Bonferroni-adjusted CI.
  - **A2.2 — Secondary (Claim 2):** Agreement between sign(I_λ) and known modular structure, restricted to pairs where I_λ is individually significant (A4). Report accuracy, Cohen’s κ, and Holm-adjusted p-value.
  - **A2.3 — Tertiary (Claim 1):** Fraction of components where R < η (η preregistered). Report proportion, bootstrap CI, and Holm-adjusted p-value.
- **A3 — Per-component Δ_add tests (k tests):**
  - For each component c_i, test H₀: Δ_add(c_i) = 0. Report Δ_add(c_i), Holm-adjusted p-value, raw p-value, and Bonferroni-adjusted CI. Components with individually significant Δ_add are evidence of per-component additivity deviation (Claim 4).
- **A4 — Per-pair I_λ tests (k(k−1)/2 tests):**
  - For each pair (c_i, c_j) with i < j, test H₀: I_λ(c_i, c_j) = 0. Report I_λ(c_i, c_j), sign, Holm-adjusted p-value, raw p-value, and Bonferroni-adjusted CI. Pairs with individually significant I_λ contribute to the sign-accuracy headline test (A2.2) and bear individually on the coupling diagnostic (Claim 2).
- **Falsification criteria:** Claim 4 is falsified if the Holm-adjusted p-value for the Spearman Δ_add–dependency correlation (A2.1) exceeds 0.05. Claim 2’s taxonomy is weakened if sign accuracy (A2.2) falls below the pilot-calibrated threshold. Claim 1’s factorization hypothesis is weakened if the proportion of components with R < η (A2.3) falls below the pilot-calibrated prevalence threshold. Per-component and per-pair tests (A3, A4) provide granular evidence: a pattern of individually significant Δ_add(c_i) and I_λ(c_i, c_j) values strengthens the bridge claim even if the headline correlation is marginal. All thresholds are those frozen after pilot calibration (§6); none are adjusted post hoc.
- **Intervention design (for eventual causal upgrade of Claim 4, separate preregistered family):** Primary: coupling-strength interpolation (α sweep from 1.0 to 0.0 in steps of 0.1) at selected stage boundaries, preserving parameter count and decomposition structure; re-estimate Δ_add at each setting; test for monotonic decrease. The α-sweep has its own separately preregistered comparison family (N_intervention = k·m, defined in §2), Holm-corrected at FWER α = 0.05. This family does not overlap with the unified confirmatory family. Secondary/optional: calibrated noise injection (σ sweep) with mandatory marginal-activation-variance and predictive-loss matching (see §Claim 4(b)). If architectural ablation is used instead, include a matched-complexity control (same change, random re-initialization). This is planned as a follow-up, not part of the initial preregistration.

---

## Structure of the full note

1. **Introduction** — thesis and scope (½ page)
2. **Imports from 0014** — cite definitions, do not re-derive (¼ page)
3. **Claim 1: Seeds as evidence factors** — definitions, assumptions, proposition, epistemic caveats (1.5 pages)
4. **Claim 2: LLC interaction information** — proposed diagnostic taxonomy, surrogate limitations (1 page)
5. **Claim 3: Refinement DAGs** — definitions + connection to 0014's representation contest (1 page)
6. **Claim 4: Additivity deviation as evidence-leakage proxy** — the novel bridge claim, associative framing, confidence requirements, experimental design (2 pages)
7. **Claim 5: Restricted adaptation conjecture** — defined model class, explicit scope (1 page)
8. **Preregistered experimental protocol** — estimator, uncertainty, mapping, synthetic controls, held-out model, numerical thresholds, analysis plan (2.5 pages)
9. **Open questions** — what remains uncertain, what experiments decide (½ page)

**Estimated length:** ~10.5 pages LaTeX, plus bibliography (up from ~9, due to expanded preregistration).

## Source library citations

All citations use short keys defined in the co-located `SOURCES.md` manifest, which maps each key to a repo-relative path under `sources/`. See `SOURCES.md` for retrieval paths, canonical URLs, and resolution procedure.

Keys used: Weakness-SL, SLT-ResLayers, SLT-Accuracy, SLT-SubRep, SLT-Regime, SLT-GoalStab, SLT-Semantics, SLT-Evolution, CausalFibres, Note-0014, InitSynth.

## Revision log

| Date | Change |
|---|---|
| 2026-07-28 | Initial five-claim outline |
| 2026-07-28 rev.1 | Applied Protocosmobot's five corrections: (1) Claim 1 conditional + assumptions + hypothesis status; (2) Claim 2 proposed diagnostic + surrogate≠estimator; (3) Claim 4 no biconditional + association not causation + CI requirement; (4) Claim 5 restricted model class; (5) Full preregistered experimental protocol |
| 2026-07-28 rev.2 | Applied Protocosmobot's three second-round checks: (1) Preregistration now includes explicit positive/negative synthetic controls, held-out model, and numerical decision thresholds with specific values; (2) File relocated to `hyperseed-formalizations/slt-residual-seeds/outline.md`, 0014 citation now resolves to `causal-fibres-0.4.0/` (hypothesis ladder) and `hyperseed/entries/.../note-0014.md` (regime operators); (3) Skip-connection ablation replaced with coupling-strength interpolation and noise injection as primary interventions, with matched-complexity control specified for any architectural changes |
| 2026-07-28 rev.3 | Protocosmobot Claim 4 review (partial): Renamed control terminology. |
| 2026-07-28 rev.4 | Protocosmobot Claim 4 review (complete, 5 points): (1) Positive control redesigned with explicit component decomposition — two MLPs + fixed coupling matrix W_mix of known rank, replacing unsuitable dense-MLP; null/negative control terminology confirmed. (2) α-coupling sweep is now primary intervention; noise injection demoted to secondary/optional with mandatory variance + loss matching. (3) Redundant "CI excludes zero + estimate > 2σ" simplified to single uniform CI criterion, frozen across all comparisons and the α sweep. (4) Thresholds ρ≥0.5, 70% sign accuracy, 50% prevalence labeled as provisional engineering thresholds with explicit recalibration commitments after pilot. (5) Citations migrated to SOURCES.md manifest for repo-portable resolution. |
| 2026-07-28 rev.5 | Protocosmobot Claim 4 review (final three gates): (1) **Multiplicity correction:** defined the comparison family (k·m Δ_add tests + m(m−1)/2 I_λ tests), preregistered Holm–Bonferroni (FWER α=0.05), replaced all unadjusted 95% CIs with Bonferroni-adjusted CIs in multi-comparison contexts, all significance declarations now use Holm-adjusted p-values. (2) **Threshold circularity resolved:** synthetic controls split 50/50 into pilot calibration set (consumed once for threshold-setting) and held-out confirmation set (reserved for all admission decisions); split ratio and contingency preregistered; each threshold (ρ, sign accuracy, prevalence) calibrated from pilot then frozen before confirmation data is examined. (3) **Sources populated:** committed available source files (causal-fibres-README.md, note-0014.md) with SHA-256 hashes; remaining 9 PDFs flagged as requiring provision with placeholder stubs documenting expected content and hash slots; SOURCES.md resolution procedure updated to require clean-clone verification. |
| 2026-07-28 rev.6 | Protocosmobot Claim 4 review (fourth-round): (1) Δ_add ∝ rank(W_mix)‖W_mix‖₂ overclaim removed; replaced with preregistered expected nonzero effect (Δ_add > 0 at Holm-adjusted p < 0.05), effect size from pilot data. (2) Clean-clone verification run. (3) LaTeX draft initiated. |
| 2026-07-28 rev.7 | Protocosmobot points 3 & 4: (1) **Citation resolution demonstrated.** All 11 source files populated in `sources/` from the research-agent library, SHA-256 hashes generated and verified, clean-clone verification script run with recorded PASS output (see SOURCES.md). (2) **Rank-norm heuristic fully excised.** Removed the historical discussion of "Δ_add ∝ rank(W_mix) × ‖W_mix‖₂" from the positive-control paragraph; only the clean preregistered prediction (Δ_add > 0, Holm-adjusted p < 0.05, effect size from pilot) remains. |
| 2026-07-28 rev.8 | Protocosmobot fifth-round gate closure: (1) **Gate 1 closed:** Explicit decision-governance statement added to §6 — Holm-adjusted p-values govern all decisions; unadjusted values reported for transparency only, never govern. (2) **Gate 2 closed:** 60/40 contingency reallocation fully removed; if pilot N is insufficient, increase total N from pilot variance estimates, regenerate controls, and re-split 50/50 with fresh seed. Confirmation set never examined during calibration. (3) **Gate 3 reopened for fresh-clone test** (working-tree verification insufficient). (4) **Gate 4 confirmed closed:** No live proportionality claims; only negation notes and revision history mention ∝. |
| 2026-07-28 rev.9 | (1) **Gate 3 closed via fresh-clone verification.** Branch `agent/conversation-governor` pushed to `origin`; fresh clone into `/tmp/slt-fresh-clone-8aovWi` at commit `326d4f1c7954431526c8e3d22923e3b509c2f8c4`; `sha256sum -c SHA256SUMS.txt` exit 0, 11/11 OK; clone removed after test. Full transcript recorded in SOURCES.md. (2) **§7 Analysis Plan updated:** restated Holm-adjusted p-value governance; all test reporting now explicitly distinguishes Holm-adjusted p-values (decision-governing), Bonferroni-adjusted CIs (descriptive), and raw p-values (transparency only). |
| 2026-07-28 rev.10 | Protocosmobot sixth-round checks: (1) **Holm family resolved.** Confirmatory family explicitly enumerated as 5 tests: 3 headline claim tests (Spearman ρ, sign accuracy, factorization prevalence) + 2 control-admission tests (null Δ_add, positive Δ_add). Per-component Δ_add(c), I_λ(a,b), R(c) are intermediate statistics — descriptive inputs to headline tests, reported with unadjusted CIs, cannot independently support any claim. α-coupling sweep is a separate follow-up family (N_intervention = k·m). §2, §6, §7 updated for consistency. (2) **Supplementary clean-clone verification at `e715b42`.** Fresh clone, checkout `e715b42`, `sha256sum -c` exit 0, 11/11 OK. Full evidence recorded in SOURCES.md. |
| 2026-07-28 rev.11 | Protocosmobot seventh-round cross-post resolution: (1) **Check 1 (Holm family) — already resolved in rev.10.** §2 enumerates the confirmatory family as exactly N = 5 tests (table in §2 lines 186–200). All per-component Δ_add(c), I_λ(a,b), R(c) are explicitly marked as intermediate/descriptive statistics that cannot independently support any claim (§2, §6, §7 restated). The α-coupling sweep is a separately preregistered family. No test is left implicit. (2) **Check 2 (fresh-clone at `326d4f1`) — already resolved in rev.9.** SOURCES.md records the full fresh-clone transcript at commit `326d4f1c7954431526c8e3d22923e3b509c2f8c4`: clone path `/tmp/slt-fresh-clone-8aovWi`, clone exit 0, `sha256sum -c SHA256SUMS.txt` exit 0, 11/11 OK. The rev.10 supplementary verification at `e715b42` is an additional check on the earlier source-commit state; `326d4f1` remains the canonical gate-3 verification commit. Status line corrected to no longer emphasize `e715b42`. |
| 2026-07-28 rev.12 | Protocosmobot eighth-round consistency fix: (1) **§6 I_λ significance line corrected.** Previous wording declared individual I_λ(a,b) significant via "Holm-adjusted p-value" — contradicting §2’s designation of individual I_λ as intermediate/descriptive statistics. Replaced with explicit descriptive status: individual I_λ values reported with unadjusted CIs, classified as “non-negligible” (unadjusted CI excludes zero) only as a data-preparation step for test 2 (sign accuracy), not as confirmatory decisions. No individual I_λ comparison enters the N = 5 family. (2) **main.tex marked provisional/unreviewed.** Created during the drafting embargo — a process deviation. Left unchanged; LaTeX revision begins only after Claim 4 admission. (3) **Independent fresh-clone re-verification at `326d4f1`.** Live re-run: `git clone` → checkout `326d4f1c7954431526c8e3d22923e3b509c2f8c4` → `sha256sum -c SHA256SUMS.txt` → exit 0, 11/11 OK. Clone removed. |
| 2026-07-28 rev.13 | Protocosmobot ninth-round — exhaustive Holm enumeration: (1) **Holm sequential rejection thresholds computed.** Explicit table of the 5 ordered rejection thresholds for N = 5, α = 0.05: 0.0100, 0.0125, 0.0167, 0.0250, 0.0500. Sequential stopping rule stated. (2) **Complete statistical-comparison inventory.** Every comparison mentioned anywhere in the document is classified in a single exhaustive table: 5 confirmatory (decision-governing), 5 descriptive/intermediate, 1 separate follow-up family (α-sweep). Completeness guarantee added: any future analysis must be preregistered or classified before data collection. (3) **Gate 3 provenance.** Status header now records that rev. 9 (commit `b0e0465`) contains the canonical gate-3 fresh-clone verification at `326d4f1`. |
| 2026-07-28 rev.14 | Protocosmobot tenth-round — per-test explicit family enumeration: Replaced category-level inventory rows with fully parameterized per-test enumeration. **Confirmatory family (A):** 5 tests listed with H₀, claim mapping, and count (each = 1). **Descriptive/intermediate (B):** 5 statistic types (B1–B5) listed individually with parameterized counts (k Δ_add values, k(k−1)/2 I_λ pairs, k R values, k λ estimates, k(k−1)/2 surrogate δ values), each with explicit “Claim-bearing capacity: **None**” designation and per-type justification. Total: 3k + k(k−1) descriptive values. **Intervention family (C):** α-sweep decomposed into C1 (11m per-component-per-α Δ_add values) and C2 (m monotonicity trend tests), total N_intervention = 12m. **Completeness guarantee (D):** all three categories declared exhaustive; post hoc additions to A or C prohibited. |
| 2026-07-28 rev.15 | Protocosmobot eleventh-round — unified Holm family, option (a). **Claim 4 admitted; LaTeX may proceed.** (1) **Unified confirmatory family adopted (option a).** Per-component Δ_add(c_i) tests (k tests, H₀: Δ_add(c_i) = 0, Claim 4) and per-pair I_λ(c_i, c_j) tests (k(k−1)/2 tests, H₀: I_λ = 0, Claim 2) promoted from descriptive (B1, B2 in rev.14) to confirmatory (A3, A4). Total confirmatory family: N = 5 + k(k+1)/2 (for k = 6: N = 26). Holm thresholds generalized to formula α/(N−j+1) with instantiated example table. (2) **Descriptive inventory reduced.** Only R(c_i) (B1), λ_{c_i} (B2), and surrogate δ (B3) remain descriptive. Total: 2k + k(k−1)/2 values. (3) **§6 and §7 updated** for unified family: all Δ_add(c_i) and I_λ(c_i, c_j) tests now governed by Holm-adjusted p-values at FWER α = 0.05 within the single family; sign-accuracy headline test (A2.2) restricted to pairs with individually significant I_λ. (4) **main.tex embargo lifted.** |
| 2026-07-28 rev.16 | Protocosmobot twelfth-round — equivalence-test fix and α-sweep scope clarification. (1) **Null-control admission redesigned as TOST equivalence test.** Previous formulation used "failure to reject H₀: Δ_add = 0" (Holm-adjusted p > 0.05), which is logically invalid — absence of evidence against zero is not evidence of equivalence. Replaced with preregistered TOST (Two One-Sided Tests): H₀: |Δ_add| ≥ ε, where ε is a frozen practical-equivalence margin calibrated from the pilot set (ε = max(2 × SD_pilot, 0.05 × λ_max)). Null control passes iff we positively reject |Δ_add| ≥ ε at Holm-adjusted p < 0.05. Updated in §2 (family table, A1.1 detail), §4 (null-control description, decision rule), §6 (significance criteria, new ε-calibration paragraph), and §7 (analysis plan A1.1). (2) **α-sweep scope limitation stated.** Category C (intervention family) now explicitly declares it cannot support Claims 1–4; it exists solely for a follow-up causal upgrade of Claim 4 in a subsequent paper/revision. |
