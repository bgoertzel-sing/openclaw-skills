# Train-Time Causal Factor Learner Preregistration

- Project: RelaLeap SLT residual-layer causal factors
- Date: 2026-07-03
- Status: preregistered design; no implementation yet
- Directive: Ben asked to try a genuinely new train-time causal factor approach after v0 posthoc pregate and v2 cached-residual fitted arms failed promotion.
- Source context: `library/slt-residual-layers/SOURCE.md`; `scratch/relaleap_gpt55_pro_final_plan.md`

## 1. Hypothesis

A residual-layer learner can discover useful causal columns **during task training** if the residual mechanism is parameterized as a sparse set of trainable local interventions and is regularized by SLT/causal modularity signals, rather than by reconstruction alone.

The core hypothesis is:

> Jointly training a sparse residual-column adapter with SLT-informed additivity, commutator, exact-ablation, and interaction-remainder penalties will recover column structures that pass synthetic causal ground-truth regimes and matched null controls more reliably than posthoc bases fit to frozen residual caches.

The target validation signal is **local evidence/free-energy additivity and causal modularity**, not residual reconstruction quality. Reconstruction may be useful as a weak auxiliary stabilizer, but it is not sufficient evidence for columnar causal structure.

## 2. Architecture: Train-Time Residual Causal Column Learner

### 2.1 Insertion site and task objective

For a frozen or trainable base transformer with hidden state `h_l` at an insertion site, insert a residual adapter:

```text
h'_l = h_l + r_theta(h_l, c_l)
```

where `c_l` contains local context features available at train time: token identity, position, local activations, optional gradient/Fisher summaries, and task metadata for synthetic regimes.

The learner is trained with the ordinary task loss through the frozen suffix or full model, depending on the benchmark:

```text
L_task = CE(y, Tail(h_l + r_theta(h_l, c_l)))
```

The first implementation should prefer a frozen base and frozen suffix so exact ablations and commutator audits are interpretable.

### 2.2 Minimal parameterization

The minimal mechanism is a sparse mixture of rank-one residual atoms grouped into columns:

```text
atom g:       A_g(h) = beta_g * b_g * phi(a_g^T h + u_g^T c)
column k:    C_k(h,c) = sum_g q_{kg} z_g(h,c) A_g(h)
residual:    r_theta(h,c) = sum_k m_k(h,c) alpha_k(h,c) C_k(h,c)
```

Parameters:

- `a_g`: input direction for atom `g`
- `b_g`: output residual direction for atom `g`
- `beta_g`: learned scalar amplitude, initialized at zero
- `q_{kg}`: soft membership of atom `g` in column `k`
- `z_g(h,c)`: atom gate/activation
- `m_k(h,c)`: sparse column mask, implemented with top-k, hard concrete, or straight-through sparsemax
- `alpha_k(h,c)`: column coefficient
- optional `s_k`: low-dimensional column state or centroid used for split/merge decisions

Identity initialization is mandatory:

```text
beta_g = 0  =>  r_theta = 0 at initialization
```

This prevents early task degradation and makes growth events auditable.

### 2.3 Column initialization and growth

Training starts with a conservative seed set:

- `K0` columns, e.g. 4 or 8
- `G0` atoms per column, e.g. 2
- all output amplitudes zero or near-zero
- gates initialized to low entropy but not hard one-hot

Columns are grown online by auditing residual/task-error structure during training. Every `T_audit` steps, compute per-example weakness records:

```text
w_i = {
  task_loss_i,
  delta_loss_i under current adapter,
  gradient g_i = d CE / d h_i,
  approximate Fisher/GN metric G_i,
  active column support S_i,
  exact ablation losses for small audited supports,
  column contribution vectors delta h_{ik}
}
```

Growth rules are preregistered and deterministic given metrics and seeds:

1. **Spawn column** when a cluster of high-loss/high-gradient examples is poorly explained by all active columns and shows coherent residual direction under gradient/Fisher geometry.
2. **Spawn atom inside a column** when the column has high within-column reconstruction/task residual but low off-support leakage.
3. **Freeze growth** when null controls or low-rank controls explain the same residual structure as well as the proposed new column.
4. **Kill/deactivate column** when usage remains below a minimum threshold or exact ablations show no positive singleton gain.

A new column must begin with zero output amplitude and earn activation through task loss plus gates; it is not allowed to copy a fitted posthoc residual vector from heldout data.

## 3. SLT-Informed Training Objective

The train-time objective is multi-term, but promotion decisions will report panels separately rather than a single handcrafted score.

```text
L_total =
  L_task
  + lambda_sparse L_sparse
  + lambda_usage L_usage
  + lambda_comm L_comm_proxy
  + lambda_rem L_interaction_remainder
  + lambda_leak L_off_support_leakage
  + lambda_ablate L_ablation_calibration
  + lambda_prior L_structure_prior
  + lambda_rec L_aux_reconstruction_optional
```

### 3.1 Sparsity and usage

- Per-token sparse active columns: `|S_i| <= k`, usually `k in {1,2,3}`.
- Penalize diffuse support entropy.
- Penalize dead columns and column collapse using a weak usage prior, not forced equal usage.
- Track active rank, active parameters per token, residual norm, and support frequency.

### 3.2 Commutator regularization

Approximate during training with mini-task/microcontext updates. For contexts `A` and `B`:

```text
Comm(A,B) = E_x || logits_{U_B(U_A(theta))}(x) - logits_{U_A(U_B(theta))}(x) ||^2
```

The train-time proxy may use first-order mixed-Hessian/HVP approximations, but preregistered audit gates must include finite-update commutators on heldout audit slices.

### 3.3 Interaction remainder regularization

Let `delta h_a` and `delta h_b` be column contributions. Penalize diffuse pairwise coupling under the local Fisher/GN metric:

```text
sigma_ab = delta h_a^T G delta h_b
```

The goal is not to force all interactions to zero. The goal is to concentrate nonzero interactions into sparse, interpretable pairs and to preserve regimes where synergy is genuinely present.

### 3.4 LLC additivity and interaction information

The learner periodically estimates module-wise local evidence proxies over actual trainable parameter blocks:

```text
I_lambda(a;b) = lambda_a + lambda_b - lambda_ab
```

Interpretation:

- `I_lambda ~= 0`: approximately independent columns
- `I_lambda > 0`: redundant/shared singular structure
- `I_lambda < 0`: synergistic/emergent joint singular structure

The interaction regularizer only penalizes **unstructured diffuse interaction**, not preregistered synergistic pairs in synthetic regimes. LLC estimates are reported as finite-sample WBIC/SGLD proxies, not exact RLCTs.

### 3.4.1 Mandatory SLT-estimation validity contract

Because earlier RelaLeap work used a handcrafted LLC proxy and a tiny frozen-parameter WBIC table, this version treats SLT parameters as **not meaningfully estimated** unless all of the following are true:

1. **Actual trainable blocks**: WBIC/SGLD probes are run over the adapter's real trained parameter blocks: column amplitudes, gates/router parameters, atom directions, shared-core parameters, and declared joint blocks. Frozen output amplitudes or posthoc scalar knobs are insufficient.
2. **Known-SLT calibration suite**: before interpreting RelaLeap estimates, the estimator must pass benchmark models with known or analytically checkable behavior: a regular identifiable linear model, a rank-deficient linear model, an overparameterized mixture/symmetry toy, independent two-module composition, redundant/shared-core composition, and synergistic two-module composition.
3. **Temperature and sampler diagnostics**: WBIC temperature, SGLD step size, burn-in, chain count, effective sample size proxy, seed sensitivity, and posterior-energy trace stability must be reported. A single chain or a single temperature is diagnostic only.
4. **Input coverage and inference budget**: every estimate must report the number of input examples used, the sampling/stratification scheme over regimes, labels, router supports, loss quantiles, and active-column supports, plus the total inference budget. The intended advantage here is that RelaLeap can run the network on many inputs; the bottleneck is inference time, not conceptual unobservability. Claims are blocked until sample-size sensitivity curves show the WBIC/SGLD proxy and `I_lambda` signs/margins stabilize as the input count grows.
5. **Module-vs-joint estimates**: every reported interaction value must include separate estimates for `lambda_a`, `lambda_b`, and `lambda_ab`, with identical data splits, sampler settings, parameter masks, priors, and input batches unless a preregistered sensitivity run says otherwise.
6. **Null-normalized uncertainty**: `I_lambda` sign and magnitude must beat matched nulls and bootstrap/seed/input-resample uncertainty. If the confidence interval crosses the matched-null margin, the SLT interpretation is blocked.
7. **Finite-sample wording**: reports must call these `finite-sample WBIC/SGLD proxies for RLCT/LLC`, not exact RLCT estimates.
8. **Promotion guardrail**: scientific promotion is impossible if the SLT evidence panel lacks estimator type, estimated parameter blocks, WBIC temperature schedule, calibration status, calibration benchmark names, input sample size, input coverage report, inference budget report, sample-size sensitivity report, null-normalized margin, and finite-sample caveat.

If any item fails, the decision report must say `slt_evidence_status = uncalibrated` and `scientific_status = fail_closed`, even if task loss, reconstruction, and causal audits look good.

### 3.5 Exact ablation calibration

During training and validation, audit small supports exactly:

```text
L(S) = CE(y, Tail(h + sum_{k in S} r_k(h,c)))
G_a = L(empty) - L({a})
Syn_ab = [L(empty)-L({a,b})] - G_a - G_b
Regret(S) = L(S) - min_{S' in one-swap-neighborhood(S)} L(S')
```

Information-geometric surrogates must be calibrated against exact ablations and may not be treated as causal evidence without calibration.

## 4. Split / Merge / Transfer Policy

All structural changes occur only at audit intervals and are logged.

### 4.1 Split column

Split column `k` into `k1,k2` when all hold:

- high within-column pair synergy or high within-column Fisher coupling variance;
- active examples form two stable clusters in gradient/Fisher/residual contribution space;
- exact one-swap support regret improves after provisional split;
- split beats support-frequency-matched random split on validation audit slices;
- the added parameter cost is justified by lower local evidence/free-energy proxy.

### 4.2 Merge columns

Merge `a,b` when all hold:

- supports are highly co-active and ablation fingerprints are redundant;
- `I_lambda(a;b) > 0` persistently indicates shared/redundant singular structure;
- merged candidate preserves CE and exact ablation gains;
- commutator and leakage do not worsen beyond budget.

### 4.3 Transfer atoms across columns

Transfer atom `g` from column `a` to `b`, or share it through a marked shared-core node, when:

- `g` contributes more singleton gain under `b`'s audited support;
- transfer reduces off-support leakage;
- transfer does not hide a synergistic pair as a false singleton;
- the event is stable across at least two audit windows.

### 4.4 Add shared core / mediator

When two columns have positive `I_lambda` and redundant ablation fingerprints but should not simply merge because they serve distinct contexts, create a shared-core atom group and mark both columns as dependents. This is the expected behavior in `shared_core_redundant`.

### 4.5 Fail-closed structural policy

If split/merge/transfer criteria conflict, keep the previous simpler structure. If SVD/low-rank or flat same-router controls match the proposed structural update, block the columnar interpretation.

## 5. How This Differs from End-to-End Sparse Dictionary Training

This is not merely a sparse dictionary trained end-to-end because:

1. **Columns are causal intervention modules**, not just basis vectors. They must have exact ablation gains, calibrated support regret, commutator behavior, and stable causal fingerprints.
2. **Structure is grown and revised during task training** using preregistered split/merge/transfer rules, not selected posthoc from residual caches.
3. **Validation is SLT/free-energy additivity**, including module LLC and `I_lambda`, not reconstruction error or sparse coding loss.
4. **Matched controls are mandatory**: same-router flat values, SVD/low-rank, parameter-matched dense adapters, support-frequency nulls, and dependency-aware shuffles.
5. **Interactions are interpreted, not erased**: redundant and synergistic regimes must be detected rather than regularized away.
6. **Identity initialization and fail-closed promotion** prevent claiming causal factors from capacity, initialization, or leakage artifacts.

## 6. Training Procedure

### Stage 0: deterministic setup

- Fix seeds and log all configs.
- Use synthetic regimes first; no GPU or paid compute required.
- Use train/validation/test splits with no heldout teacher retraining.
- Report exact parameter counts and active-rank budgets.

### Stage 1: warmup

- Train task model or residual adapter from identity initialization.
- Activate sparsity gradually.
- Disable structural growth until the adapter has nonzero but stable contribution.

### Stage 2: audited growth

At every audit interval:

1. compute weakness records;
2. evaluate exact ablations on sampled supports;
3. compute null-control metrics for declared dependencies;
4. propose split/merge/transfer/spawn/kill actions;
5. accept only if validation metrics and fail-closed criteria pass;
6. log rejected proposals.

### Stage 3: freeze structure and fit coefficients

- Freeze the learned structural graph (`columns`, `atoms`, shared cores, allowed supports).
- Continue short training of amplitudes/gates only.
- Run heldout causal audits and SLT/WBIC proxies over actual parameter blocks.

### Stage 4: decision report

Report separate panels:

- prediction metrics;
- reconstruction metrics;
- causal modularity metrics;
- SLT/evidence metrics;
- null-normalized margins;
- structural event log.

No single weighted score may determine promotion.

## 7. Synthetic Ground-Truth Test Plan

The train-time learner must be evaluated before any real transformer claim on these regimes:

### 7.1 `exact_factorized`

Expected pass:

- recovers true active supports above preregistered threshold;
- low off-support leakage;
- low commutator;
- `I_lambda` near zero except noise;
- beats same-router flat and low-rank controls on causal modularity while matching task loss.

### 7.2 `shared_core_redundant`

Expected pass:

- detects shared/redundant structure using positive `I_lambda`;
- either merges columns or creates a marked shared core;
- does not falsely report independent columns.

### 7.3 `synergistic_pair`

Expected pass:

- preserves a sparse pair interaction;
- pair synergy is positive under exact ablation;
- `I_lambda` is nonzero with the preregistered sign pattern for the generator;
- does not split the pair into two falsely independent singletons.

### 7.4 `low_rank_trap`

Expected pass:

- SVD/low-rank control wins or ties;
- learner blocks columnar causal claim;
- decision report says fail-closed for columnar interpretation.

### 7.5 `oblique_dictionary`

Expected pass:

- nonorthogonal/rank-one column learner beats orthogonal sparse diagnostic;
- learned directions are not reducible to train-only SVD rotation;
- exact ablations validate column supports.

### 7.6 `random_null`

Expected pass:

- no non-null causal factor claim;
- real learner does not beat dependency-aware nulls with confidence;
- promotion is blocked.

## 8. Causal Audit Gates

A candidate train-time factorization passes only if all gates pass on validation and remain non-contradictory on test.

1. **Prediction gate**: matches or improves task loss relative to matched controls without excessive KL/logit drift.
2. **Exact ablation gate**: singleton gains, pair synergies, and one-swap regret support the learned supports.
3. **Commutator gate**: finite-update order effects remain below budget for independent columns; declared synergistic/shared-core exceptions must be sparse and stable.
4. **Leakage gate**: off-support gradient/Fisher leakage remains below budget.
5. **Support regret gate**: selected supports are locally competitive under one-swap neighborhoods.
6. **Ablation calibration gate**: information-geometric surrogate has bounded MAE, sign accuracy, and rank correlation against exact ablations.
7. **LLC additivity gate**: module-wise LLC additivity has the expected sparse interaction pattern for the regime.
8. **Null margin gate**: real metrics beat all applicable dependency-aware nulls by bootstrap margin.

## 9. Null Controls

Every arm/learner must declare its information dependencies. Nulls must perturb every declared channel.

Required nulls:

- target shuffle;
- teacher residual shuffle if teacher residuals are used in auxiliary losses;
- hidden shuffle;
- hidden/residual misalignment;
- context shuffle;
- router support shuffle;
- support-frequency-matched random supports;
- gradient shuffle and gradient sign flip;
- Fisher/GN metric shuffle;
- token identity shuffle;
- position shuffle;
- mechanism-preserving control;
- mechanism-violating control.

Matched controls:

- same-router flat value residual adapter;
- SVD/low-rank dense control fit train-only;
- parameter-matched dense adapter;
- active-rank-matched sparse dictionary;
- residual-norm-matched control;
- oracle diagnostic modes marked non-promotable.

Exact ties with nulls are failures unless the null is declared non-applicable before running.

## 10. Success Criteria

A train-time causal factor learner is considered a preregistered success only if:

1. It passes all six synthetic regimes with expected behavior, including fail-closed behavior on `low_rank_trap` and `random_null`.
2. It beats or ties matched controls on task loss while beating them on causal modularity.
3. It beats all applicable dependency-aware nulls with bootstrap confidence.
4. It reports calibrated exact ablation and information-geometric audits.
5. It reports module-wise WBIC/LLC proxies over actual trainable parameters, with calibration benchmarks passing.
6. Its learned `I_lambda` structure is sparse and interpretable rather than diffuse all-to-all coupling.
7. Structural events are reproducible from logged metrics, configs, and seeds.

Only after these conditions pass may a later implementation consider GPU validation on real transformer residual caches.

## 11. Fail-Closed Criteria

The claim must be blocked if any of the following occur:

- SVD/low-rank control wins in regimes other than expected low-rank traps.
- Same-router flat value control matches the learner on causal metrics.
- Null controls tie or beat the learner.
- LLC estimates fail calibration benchmarks.
- Exact ablations contradict surrogate audits.
- Support regret or commutator leakage is high.
- Interactions are diffuse all-to-all rather than sparse.
- Column growth is unstable across seeds.
- Learned factors depend on heldout residuals or posthoc cache fitting.
- The result is explainable by parameter count, active rank, residual norm, or router frequency.

The correct report in these cases is `scientific_status = fail_closed`, not partial promotion.

## 12. What Is NOT Being Claimed

This preregistration does **not** claim:

- that the proposed learner is implemented;
- that RelaLeap has already discovered causal transformer residual columns;
- that finite-sample WBIC/SGLD estimates are exact RLCTs;
- that reconstruction quality implies causal factorization;
- that sparse dictionary atoms are automatically semantic features;
- that low commutator alone proves modularity;
- that synthetic success transfers to real transformers;
- that a GPU-scale run is justified before the synthetic gates pass;
- that interactions should always be zero; synergistic and shared-core regimes are expected and must be detected.

## 13. First Implementation Slice, Later

No code is implemented in this preregistration. The first later coding slice should implement only:

1. synthetic regime generators;
2. identity-initialized rank-one column learner;
3. same-router flat and SVD controls;
4. exact ablation auditor;
5. null dependency contracts;
6. structured event log;
7. fail-closed report.

WBIC/LLC proxies can be added only after calibration benchmarks are in place.
