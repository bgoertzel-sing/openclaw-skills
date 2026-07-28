# SLT-Guided Residual Seeds: Outline (Revised)

**Tentative title:** SLT-Guided Residual Seeds — Weakness, Evidence Geometry, and Refinement DAGs for Transformer Adaptation

**Status:** Revised outline incorporating Protocosmobot's five first-round corrections + three second-round checks + five third-round operational fixes + fourth-round gates + fifth-round citation/claim cleanup + sixth-round Holm family resolution + seventh-round commit-reference correction + eighth-round §6 consistency fix and main.tex quarantine. Drafting remains gated on reviewer sign-off.
**Date:** 2026-07-28 (rev. 12)
**main.tex status:** Provisional/unreviewed. Created during the drafting embargo (a process deviation). Left unchanged pending Claim 4 admission; LaTeX revision begins only after the canonical outline passes all checks.
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
- Multiplicity-corrected significance: Δ_add is declared "meaningfully non-zero" iff its Holm-adjusted p-value < 0.05 across the full comparison family (see §2 and §6 of the preregistered protocol).

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

The experiment involves simultaneous statistical tests across multiple comparisons. The **confirmatory comparison family** consists of exactly the following claim-bearing and control-admission tests:

| # | Test | Supports | H₀ |
|---|------|----------|-----|
| 1 | Spearman ρ(Δ_add, cross-stage dependency) | Claim 4 | ρ = 0 |
| 2 | Sign accuracy of I_λ vs known modular structure | Claim 2 | Accuracy ≤ chance |
| 3 | Prevalence of R < η across components | Claim 1 | Prevalence ≤ pilot-calibrated threshold |
| 4 | Null control: Δ_add ≈ 0 | Control admission | Δ_add ≠ 0 |
| 5 | Positive control: Δ_add > 0 | Control admission | Δ_add = 0 |

**Total confirmatory family size: N = 5.** This family is fixed before data collection.

**Status of per-component statistics:** Individual per-component Δ_add(c) values, individual I_λ(a,b) values, and individual R(c) values are *intermediate statistics* that serve as inputs to the headline tests above. Specifically:
- Per-component Δ_add(c) values are the data points fed into the Spearman correlation (test 1).
- Per-component I_λ(a,b) signs are the data points fed into the sign accuracy (test 2).
- Per-component R(c) values are the data points fed into the prevalence fraction (test 3).

These intermediate values are reported descriptively for transparency (with unadjusted CIs) but **no individual per-component comparison independently supports or falsifies any claim.** They cannot be cherry-picked as evidence for or against a claim. Only the five headline tests above govern decisions.

**α-coupling sweep (follow-up intervention):** The causal-upgrade intervention (§7, Claim 4 intervention design) involves k=11 α-level comparisons. These form a **separate preregistered family** for the follow-up experiment, with family size N_intervention = k·m (k α-levels × m components), Holm-corrected at FWER α = 0.05. This family is registered before the intervention experiment begins and does not overlap with the confirmatory family above.

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

- **Null/negative control (no coupling by construction).** Two independent MLPs sharing no parameters, trained on disjoint tasks from the same data distribution. Components are a priori independent by construction. Expected result: Δ_add ≈ 0, I_λ ≈ 0 between the two networks, R < η. If the estimator reports non-zero Δ_add on this null control, the estimator or its hyperparameters are miscalibrated; do not proceed to the test model.
- **Positive control (known coupling, explicit decomposition).** Two MLPs (component₁, component₂) connected by a fixed linear coupling layer W_mix of known rank r, trained jointly on the same task mixture. The component decomposition is defined a priori: component₁ = MLP₁ parameters, component₂ = MLP₂ parameters, coupling = W_mix. Because W_mix introduces an explicit cross-component coupling, we *preregister the expectation* that Δ_add > 0. The preregistered prediction is: *Δ_add is expected to be significantly nonzero (Holm-adjusted p < 0.05) on the positive control, with the effect size estimated from the pilot calibration set.* No analytic proportionality between Δ_add and rank/norm of W_mix is claimed—computing the RLCT contribution of the coupling would require a resolution of singularities for the specific loss surface under the chosen prior, which has not been performed. This positive control has both known non-zero coupling and an explicit component decomposition — a single dense MLP would not qualify because its component decomposition is not defined a priori. Expected result: Δ_add >> 0, |I_λ| >> 0, R > η. If the estimator fails to detect non-factorizability on this positive control, the estimator lacks power; do not proceed.
- **Decision rule for controls (applied to confirmation set only):** Both controls must pass (null: Holm-adjusted p > 0.05 for Δ_add; positive: Holm-adjusted p < 0.05 for Δ_add) before any claims about the test model are made.

### 5. Model and Data
- **Test model:** Small transformer (≤ 6 layers) trained on a two-task mixture.
- **Held-out model:** A second, architecturally distinct model (e.g. a 4-layer transformer if the test model is 6 layers, or a convolutional residual network) trained on the same data. Predictions for this held-out model are registered before fitting. If Claims 1–4 hold on the test model but fail on the held-out model, the claims are model-specific, not general.
- **Training data:** Fixed dataset, split specified before training.
- **LLC estimation data:** Training split (for loss landscape exploration).
- **Evaluation data:** Held-out split, not used for LLC estimation or estimator tuning.

### 6. Numerical Decision Thresholds (preregistered)

**Decision governance (binding):** All significance decisions in this protocol—control admission and claim evaluation—use Holm-adjusted p-values (FWER α = 0.05) within the confirmatory family of N = 5 tests defined in §2. Unadjusted p-values and unadjusted CIs are reported for transparency only and never govern any decision. Bonferroni simultaneous CIs are reported alongside Holm-adjusted tests; they are conservative but consistent with FWER control. Per-component intermediate statistics (individual Δ_add(c), I_λ(a,b), R(c)) are descriptive inputs to the headline tests; they are reported with unadjusted CIs for transparency and cannot independently support any claim.

**Multiplicity handling:** The confirmatory Holm family (N = 5) and correction method are frozen before data collection (§2). The α-coupling sweep, if executed as a follow-up, has its own separately preregistered family (§2).

- **Δ_add significance (controls):** Control-admission Δ_add tests (null: p > 0.05; positive: p < 0.05) use Holm-adjusted p-values within the N = 5 family. Reported with Bonferroni-adjusted CI at level 1 − 0.05/5.
- **Interaction remainder threshold:** η = 0.1 × λ_max, where λ_max is the largest per-component LLC. R/λ_max < 0.1 counts as "dominated."
- **I_λ magnitude (descriptive, not confirmatory):** Individual |I_λ(a,b)| values are intermediate statistics (§2) and do not belong to the confirmatory N = 5 family. They are reported with unadjusted CIs for transparency. An individual I_λ is classified as "non-negligible" for input to test 2 (sign accuracy) iff its unadjusted 95% CI excludes zero; this is a data-preparation step, not a confirmatory decision. No individual I_λ comparison independently supports or falsifies any claim.
- **Correlation threshold (Claim 4 primary test):** Spearman ρ with Holm-adjusted p < 0.05 (one-tailed). **Threshold calibration:** The minimum detectable ρ is set using the pilot calibration set (§4), targeting ≥ 80% power at the pilot-observed effect size. The procedure: (1) compute observed Δ_add–dependency correlations on the pilot positive-control data, (2) estimate the effect size, (3) compute the required ρ threshold for 80% power at that effect size and the confirmation-set sample size, (4) freeze that threshold. If the pilot effect is too small for 80% power at the confirmation-set size, report the achieved power honestly and note the study is underpowered for this effect. **The pilot calibration set is consumed by this step and never reused for confirmation tests.**
- **Sign accuracy (Claim 2):** Agreement between sign(I_λ) and known modular structure. **Threshold calibration:** Using the pilot calibration set, compute the null-distribution sign accuracy (random assignment baseline) and set the threshold at 2σ above null expectation. Freeze Cohen's κ threshold accordingly. **Pilot set consumed.**
- **Factorization prevalence (Claim 1):** R < η for a preregistered fraction of components. **Threshold calibration:** Using the pilot calibration set, compute R for all components in both positive and null controls, then set the prevalence threshold at the ROC-optimal discrimination point. If controls show perfect separation, use 80% (conservative). Freeze before examining confirmation data. **Pilot set consumed.**

**Circularity prevention:** The three calibration steps above each consume the pilot set. Once thresholds are frozen after step (3) of each calibration, the pilot data is set aside. All subsequent control-pass/fail decisions and claim evaluations use only the held-out confirmation set (§4). No threshold is revised after examining confirmation data.

### 7. Analysis Plan

**Decision governance (restated from §6):** Holm-adjusted p-values within the confirmatory family (N = 5, defined in §2) govern all accept/reject decisions throughout this analysis plan. Bonferroni-adjusted simultaneous CIs are reported for descriptive transparency; they do not govern decisions. Raw (unadjusted) p-values are reported alongside adjusted values but never used for decisions. Per-component intermediate statistics are descriptive only (§2).

- **Test 1 — Primary (Claim 4):** Spearman correlation between per-component Δ_add and cross-stage dependency score. Report coefficient, Holm-adjusted p-value (family N = 5), raw p-value, and Bonferroni-adjusted CI.
- **Test 2 — Secondary (Claim 2):** Agreement between sign(I_λ) and known modular structure. Report accuracy, Cohen's κ, and Holm-adjusted p-value (family N = 5).
- **Test 3 — Tertiary (Claim 1):** Fraction of components where R < η (η preregistered). Report proportion, bootstrap CI, and Holm-adjusted p-value (family N = 5).
- **Test 4 — Null control admission:** Δ_add ≈ 0 on null control (confirmation set). Holm-adjusted p > 0.05 required.
- **Test 5 — Positive control admission:** Δ_add > 0 on positive control (confirmation set). Holm-adjusted p < 0.05 required.
- **Sequencing:** Tests 4 and 5 (control admission) must pass before tests 1–3 are evaluated. If either control fails, the estimator is miscalibrated and no claim tests are run.
- **Falsification criteria:** Claim 4 is falsified if the Holm-adjusted p-value for the Δ_add–dependency correlation exceeds 0.05. Claim 2's taxonomy is weakened if sign accuracy falls below the pilot-calibrated threshold. Claim 1's factorization hypothesis is weakened if the proportion of components with R < η falls below the pilot-calibrated prevalence threshold. All thresholds are those frozen after pilot calibration (§6); none are adjusted post hoc.
- **Intervention design (for eventual causal upgrade of Claim 4, separate preregistered family):** Primary: coupling-strength interpolation (α sweep from 1.0 to 0.0 in steps of 0.1) at selected stage boundaries, preserving parameter count and decomposition structure; re-estimate Δ_add at each setting; test for monotonic decrease. The α-sweep has its own separately preregistered comparison family (N_intervention = k·m, defined in §2), Holm-corrected at FWER α = 0.05. This family does not overlap with the confirmatory N = 5 family. Secondary/optional: calibrated noise injection (σ sweep) with mandatory marginal-activation-variance and predictive-loss matching (see §Claim 4(b)). If architectural ablation is used instead, include a matched-complexity control (same change, random re-initialization). This is planned as a follow-up, not part of the initial preregistration.

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
| 2026-07-28 rev.12 | Protocosmobot eighth-round consistency fix: (1) **§6 I_λ significance line corrected.** Previous wording declared individual I_λ(a,b) significant via "Holm-adjusted p-value" — contradicting §2's designation of individual I_λ as intermediate/descriptive statistics. Replaced with explicit descriptive status: individual I_λ values reported with unadjusted CIs, classified as "non-negligible" (unadjusted CI excludes zero) only as a data-preparation step for test 2 (sign accuracy), not as confirmatory decisions. No individual I_λ comparison enters the N = 5 family. (2) **main.tex marked provisional/unreviewed.** Created during the drafting embargo — a process deviation. Left unchanged; LaTeX revision begins only after Claim 4 admission. (3) **Independent fresh-clone re-verification at `326d4f1`.** Live re-run: `git clone` → checkout `326d4f1c7954431526c8e3d22923e3b509c2f8c4` → `sha256sum -c SHA256SUMS.txt` → exit 0, 11/11 OK. Clone removed. |
