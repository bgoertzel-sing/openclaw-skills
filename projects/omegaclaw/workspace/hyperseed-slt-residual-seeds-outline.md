# SLT-Guided Residual Seeds: Outline (Revised)

**Tentative title:** SLT-Guided Residual Seeds — Weakness, Evidence Geometry, and Refinement DAGs for Transformer Adaptation

**Status:** Revised outline incorporating Protocosmobot's five corrections. Drafting remains gated on review of this revision.
**Date:** 2026-07-28 (rev. 1)
**Author:** ProtomegaTron
**Reviewer:** Protocosmobot
**Imports from 0014:** Frozen interface (Def. 2.1), Evidence record (Def. 2.3), Counterfactual factor closure (Def. 2.5), Matched budget (Def. 2.2), H0–H6 hypothesis ladder. These are cited, not re-derived.

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

**Source claims:**
- "If the evidence factorizes across modules, the global LLC is the sum of module LLCs." — *Weakness as Local Evidence* (library/slt-hyperseed-synthesis/source/Weakness-Singular-Learning.pdf)
- "Do not promote a residual basis because it reconstructs well. Promote it because R is small." — *SLT and Residual Layers* (library/slt-residual-layers/extracted.txt)
- Evidence-ratio → soft-accuracy bridge, O(λ/n) correction: *SLT-accuracy-weakness_v1* (library/slt-hyperseed-synthesis/source/SLT-accuracy-weakness_v1.pdf, §1–2)

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

**Source claims:**
- I_λ > 0 / < 0 interpretation: *SLT for SubRep* (library/slt-hyperseed-synthesis/source/SLT-SubRep-v5.pdf)
- Computable surrogates via mixed-Hessian blocks and commutator diagnostics: *Weakness as Local Evidence* §appendix; *SLT and Residual Layers* §"Third, compute mixed-Hessian / commutator dominance"

**Formal objects:** InteractionInformation I_λ(a, b), CommutatorDominance Comm(a, b), MixedHessianNorm ‖H_{ab}‖, SurrogateAgreement δ(Comm, ‖H_{ab}‖, I_λ).

**Falsifiable prediction:** In a small transformer with known modular structure (e.g., two-task mixture), per-seed LLC estimates should yield I_λ ≈ 0 between task-specific seeds and I_λ > 0 between capacity-sharing seeds. Additionally, the surrogate measures should agree with direct LLC estimates to within stated tolerances (to be preregistered). Measurable with the `devinterp` LLC estimator. Surrogate-direct discrepancies, if found, would weaken the diagnostic taxonomy rather than the underlying SLT theory.

---

### Claim 3 — Refinement DAGs are the operational structure of seed ecology

Seeds do not exist in a fixed decomposition. They participate in a refinement DAG whose moves include split, merge, mediate, specialize, demote, and transfer. Each move is scored by the pregate objective:

> J(F) = n·L̂_F + λ̂_F·log n − log π(F) + α·Comm(F) + β·Leak(F) + γ·Regret(F) + δ·Interaction(F)

The structure controller selects refinement moves that decrease J with stable associative signatures (see Claim 4 for the distinction between association and causation here).

**Source claims:**
- Refinement-DAG structure with weakness/evidence scoring: *Weakness as Local Evidence* §refinement DAGs, quantale message-passing
- The seven-term pregate formula: *SLT and Residual Layers* (extracted.txt, §"Use an SLT-informed pregate")
- Regime-change detection via module-wise LLC signatures triggers refinement: *SLT for regime-change detection* (library/slt-hyperseed-synthesis/source/SLT-for-regime-change-detection.pdf)

**Formal objects:** RefinementMove m: F → F', PregateScore J(F, c), AssociativeSignature σ(r_i, c), RegimeSignature Σ(F, t).

**Connection to 0014:** 0014's H1 representation contest (Def. 2.8) compares arm classes at matched budget. Claim 3 extends this to a *dynamic* contest: the contest is not a one-shot comparison but a DAG of refinement moves, each subject to the same evidence gates 0014 defines.

---

### Claim 4 — Additivity deviation is a measurable proxy for compositional evidence leakage

**[Correction 3 applied: removed biconditional; replaced causal language with associative; added confidence-interval and intervention requirements.]**

**This is the single novel bridge claim.** SLT's RLCT decomposition across components predicts that deviations from LLC additivity signal geometric interactions between singular regions. In Hyperseed terms, these deviations are *associative signatures* of evidence leakage between refinement stages.

> Δ_add(F) = |λ_{joint} − Σ_c λ_c|

**Epistemic downgrade from earlier version:**

1. **No biconditional.** Δ_add > 0 is *necessary but not sufficient* evidence that factorization F fails to decompose the evidence geometry. Finite-sample bias in LLC estimation, prior misspecification, and MCMC mixing artifacts can all produce non-zero Δ_add even when the true singularity structure decomposes. The claim is: *Δ_add significantly exceeding zero, after accounting for estimator uncertainty, is evidence against clean factorization.* The converse (Δ_add ≈ 0 implies good factorization) is better supported but still conditional on the product-prior assumption from Claim 1.

2. **Association, not causation.** The prediction is that Δ_add *correlates with* graph-theoretic cross-stage dependency in the refinement DAG. This is an associative claim. Upgrading to causal language requires an intervention design: perturb cross-stage coupling (e.g., by ablating skip connections, freezing subsets of parameters, or injecting noise at stage boundaries) while controlling model complexity, and verify that Δ_add changes in the predicted direction. Until such an intervention experiment is designed and run, "Δ_add tracks cross-stage dependency" means association.

**Confidence-interval requirement:** All reported Δ_add values must include:
- Bootstrap or MCMC-derived confidence intervals on individual λ_c estimates.
- Propagated uncertainty on Δ_add itself (not just point estimates).
- A preregistered significance threshold for declaring Δ_add "meaningfully non-zero" (e.g., Δ_add > 2σ_Δ).

**Source claims:**
- LLC additivity and its failure: *Weakness as Local Evidence*; *SLT-SubRep-v5* §interaction complexity
- Cross-stage dependency → counterfactual factor closure: 0014 Def. 2.5
- The initial synthesis hypothesis: "deviations from additivity signal geometric interactions between singular regions" (library/slt-hyperseed-synthesis/INITIAL_SYNTHESIS.md)

**Rank-norm claim excised.** An earlier draft contained the unsupported claim Δ_add ∝ rank(W_mix)‖W_mix‖₂. This has been fully removed. Known rank and norm do not generally determine the SLT relationship without an explicit resolution of singularities under a specified model/prior. What remains is the preregistered prediction only: Δ_add is expected to be significantly nonzero (Holm-adjusted p < 0.05) on the positive control, with the effect size estimated from the pilot calibration set. No analytic proportionality is claimed.

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

**Source claims:**
- Regime-change detection and its limits: *SLT-Goal-Stability_v4* (library/slt-hyperseed-synthesis/source/SLT-Goal-Stability_v4.pdf)
- Semantics–geometry connection: *SLT-Semantics-v2* (library/slt-hyperseed-synthesis/source/SLT-Semantics-v2.pdf)
- SubRep interaction complexity: *SLT-SubRep-v5*
- Evolution/EDA free-energy geodesics: *SLT-Evolution* (library/slt-hyperseed-synthesis/source/SLT-Evolution.pdf)

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

### 2. Uncertainty Quantification
- **Per-component λ_c:** Bootstrap confidence intervals (B ≥ 1000 resamples) or MCMC posterior credible intervals (95%).
- **Δ_add:** Propagated via delta method or bootstrap on the sum; reported with 95% CI.
- **I_λ(a, b):** Same uncertainty propagation; reported with 95% CI.
- **Significance threshold:** Δ_add is declared "meaningfully non-zero" iff the 95% CI excludes zero.

### 3. Component-to-DAG Mapping
- **Component definition:** Each residual block (or attention head / MLP sublayer, depending on granularity — to be fixed before experiment) is one component c_i.
- **DAG construction:** Edges from c_i to c_j iff information flow exists (measured by gradient attribution or activation patching). Edge weights from mutual information or ablation impact.
- **Cross-stage dependency score:** Weighted edge density between non-adjacent DAG stages. Formal definition to be stated as a graph-theoretic formula before data collection.

### 4. Model and Data
- **Model:** To be selected from: (a) synthetic mixture-of-experts with known singular structure, or (b) small transformer (≤ 6 layers) trained on a two-task mixture.
- **Training data:** Fixed dataset, split specified before training.
- **Evaluation data:** Held-out split, not used for LLC estimation.

### 5. Synthetic Control Split (Pilot / Confirmation)

- **Split rule:** Before any outcome is inspected, all synthetic control instances are randomly assigned to **pilot** (50%) or **confirmation** (50%) sets using a preregistered random seed.
- **Pilot set purpose:** Used exactly once for threshold-setting (η for Claim 1, sign-accuracy baseline for Claim 2, Δ_add significance calibration for Claim 4). After calibration, thresholds are frozen.
- **Confirmation set purpose:** Reserved exclusively for all admission decisions and claim evaluations. Never examined during calibration.
- **No adaptive reallocation.** The 50/50 split is fixed. No CV-triggered or data-dependent reallocation is permitted. If pilot sample sizes prove insufficient, the experiment must be rerun with a larger total N (determined from pilot variance estimates), not by borrowing from the confirmation set.
- **Membership is preassigned and immutable.** The assignment vector is committed to the repository before any LLC estimation begins.

### 6. Analysis Plan

**Decision governance:** All significance decisions across the entire protocol are governed by **Holm-adjusted p-values** (FWER control at α = 0.05). Bonferroni-adjusted simultaneous CIs are reported for transparency but are conservative; the Holm procedure governs accept/reject decisions. Raw (unadjusted) p-values are reported alongside adjusted values but never used for decisions.

**Comparison family:** The family consists of exactly three preregistered comparisons:
1. Claim 4 primary test (Spearman ρ ≠ 0)
2. Claim 2 secondary test (sign accuracy > chance)
3. Claim 1 tertiary test (proportion R < η > 50%)

These are ordered by the Holm procedure (smallest raw p first). No post-hoc comparisons are added without a new preregistration.

- **Primary test (Claim 4):** Spearman correlation between per-component Δ_add and cross-stage dependency score. Report coefficient, Holm-adjusted p-value, raw p-value, and Bonferroni-adjusted CI.
- **Secondary test (Claim 2):** Agreement between sign(I_λ) and known modular structure. Report accuracy, Cohen's κ, Holm-adjusted p-value.
- **Tertiary test (Claim 1):** Fraction of components where R < η (η calibrated from pilot set, then frozen). Report proportion, bootstrap CI, Holm-adjusted p-value.
- **Falsification criteria:** Claim 4 is falsified if Holm-adjusted p > 0.05 for the Spearman test. Claim 2's taxonomy is weakened if sign accuracy < 70%. Claim 1's factorization hypothesis is weakened if R < η for fewer than 50% of components. All thresholds use Holm-adjusted p-values.
- **Intervention design (for eventual causal upgrade of Claim 4):** Ablate skip connections at selected stage boundaries; re-estimate Δ_add; test whether Δ_add changes in the predicted direction. This is planned as a follow-up, not part of the initial preregistration.

---

## Structure of the full note

1. **Introduction** — thesis and scope (½ page)
2. **Imports from 0014** — cite definitions, do not re-derive (¼ page)
3. **Claim 1: Seeds as evidence factors** — definitions, assumptions, proposition, epistemic caveats (1.5 pages)
4. **Claim 2: LLC interaction information** — proposed diagnostic taxonomy, surrogate limitations (1 page)
5. **Claim 3: Refinement DAGs** — definitions + connection to 0014's representation contest (1 page)
6. **Claim 4: Additivity deviation as evidence-leakage proxy** — the novel bridge claim, associative framing, confidence requirements, experimental design (2 pages)
7. **Claim 5: Restricted adaptation conjecture** — defined model class, explicit scope (1 page)
8. **Preregistered experimental protocol** — estimator, uncertainty, mapping, analysis plan (1.5 pages)
9. **Open questions** — what remains uncertain, what experiments decide (½ page)

**Estimated length:** ~9 pages LaTeX, plus bibliography.

## Source library citations

| Short key | Full path |
|---|---|
| Weakness-SL | library/slt-hyperseed-synthesis/source/Weakness-Singular-Learning.pdf |
| SLT-ResLayers | library/slt-residual-layers/SLT-and-Residual-Layers.pdf |
| SLT-Accuracy | library/slt-hyperseed-synthesis/source/SLT-accuracy-weakness_v1.pdf |
| SLT-SubRep | library/slt-hyperseed-synthesis/source/SLT-SubRep-v5.pdf |
| SLT-Regime | library/slt-hyperseed-synthesis/source/SLT-for-regime-change-detection.pdf |
| SLT-GoalStab | library/slt-hyperseed-synthesis/source/SLT-Goal-Stability_v4.pdf |
| SLT-Semantics | library/slt-hyperseed-synthesis/source/SLT-Semantics-v2.pdf |
| SLT-Evolution | library/slt-hyperseed-synthesis/source/SLT-Evolution.pdf |
| Paper-0014 | papers/0014-causal-fibres-hypothesis-ladder/main.tex |
| InitSynth | library/slt-hyperseed-synthesis/INITIAL_SYNTHESIS.md |

## Revision log

| Date | Change |
|---|---|
| 2026-07-28 | Initial five-claim outline |
| 2026-07-28 rev.1 | Applied Protocosmobot's five corrections: (1) Claim 1 conditional + assumptions + hypothesis status; (2) Claim 2 proposed diagnostic + surrogate≠estimator; (3) Claim 4 no biconditional + association not causation + CI requirement; (4) Claim 5 restricted model class; (5) Full preregistered experimental protocol |
| 2026-07-28 rev.2 | Gate closure revision: (1) Explicit Holm-adjusted p-value governance + defined comparison family of 3; (2) Preassigned 50/50 pilot/confirmation split, no adaptive reallocation; (3) Sources committed to git with SHA-256 verification; (4) Rank-norm claim (Δ_add ∝ rank·norm) fully excised from Claim 4 with rationale |
