# Co-learned Global Causal Critic v1

## Status and question

This is a preregistered local-CPU protocol. It is a strategic pivot motivated
by the v3 result: planted causal support was recovered exactly, but neither
estimated nor oracle support produced retention-useful routing on Shakespeare.

The question is:

> Can a critic co-learn a compact, action-relevant model of the network's
> global intervention structure and use it to choose module update gates that
> improve the retention-plasticity tradeoff over ordinary ePC?

The critic is not claimed to recover the complete structural causal model of
the learner. It estimates the projection of that moving causal system onto a
specified intervention set, observation history, rollout horizon, and outcome
vector.

## Research rules

Rules 1, 2, 5, 6, and 7 are primary.

- Validate the intervention-utility estimator before trusting its policy.
- Freeze causal semantics and behavioral invariants before implementation.
- Preserve exact intervention assignments, propensities, paired states, and
  outcomes.
- Interpret the critic as a task-relative causal abstraction, not a universal
  causal graph.
- Keep feature extraction, critic, policy, interventions, and auditing behind
  replaceable interfaces.

## Hypotheses

### H1: intervention identification

On a planted modular learner with known intervention-response structure, a
critic trained online from randomized interventions predicts held-out
advantages of update actions better than constant, support-only, and
local-diagnostic baselines.

### H2: global composition

A critic that jointly attends over all module states predicts multi-module
intervention outcomes better than an equal-capacity independent per-module
critic when the fixture contains downstream and synergistic effects.

### H3: policy value

Conservative critic routing improves retained-task loss at matched incoming-task
loss relative to ordinary ePC and fixed support gating on untouched seeds.

### H4: real-text contingency

Only if H1-H3 pass, the same frozen critic mechanism improves Shakespeare
forgetting without violating Task-B tolerance or representation/credit gates.

## Causal estimand

Let `S_t` be the observable learner state, `A_t` a vector of module update
actions, and `Y_{t+h}` the outcome vector after a fixed `h`-update rollout.
For action vector `a` relative to ordinary ePC action `a0`, estimate

`tau_h(S_t, a) = E[Y_{t+h}(a) - Y_{t+h}(a0) | S_t]`.

The primary scalar advantage is

`U_h = -(Delta L_retain(a) - Delta L_retain(a0))
       - lambda_B * max(0, Delta L_new(a) - Delta L_new(a0))
       - lambda_C * intervention_cost(a)`.

The critic also predicts the unscalarized vector:

- retained-task loss change;
- incoming-task loss change;
- finite-update commutator change;
- off-support leakage change;
- per-module state displacement.

`lambda_B` is chosen on calibration seeds to express a fixed Task-B tolerance,
then frozen. Scientific conclusions must also report the Pareto frontier and
must not depend only on this scalarization.

## Intervention family

For v1, retain the existing soft-gradient semantics. For each module `m`,
action `g_m` is its protected gradient fraction:

- `0.0`: ordinary ePC update;
- `0.5`: half-protected update;
- `0.9`: strongly protected update.

The optimizer, learning rate, minibatches, replay samples, ePC relaxation, and
supervised/KD mass remain identical. Only the post-backward module-gradient
multiplier `1 - g_m` changes.

To control combinatorics, exploratory interventions alter either one module or
one predeclared interacting pair per rollout. Joint policy actions may affect
all modules after the critic passes the pairwise calibration gate.

## Observable critic state

At every decision point, construct one token per module containing:

- module type/depth and normalized parameter count;
- EMA Task-A and Task-B gradient norms and squared norms;
- gradient cosine and norm ratio;
- online support score and uncertainty;
- activation mean/variance, centered effective rank, and Task-A/Task-B CKA;
- weight norm, update norm, optimizer moments, and recent gate history;
- signed and sign-insensitive curvature overlap when scheduled;
- `||H_B g_A - H_A g_B||` when scheduled;
- recent local ablation/probe effects when available;
- exponentially discounted retention and plasticity outcome history.

A global token contains task phase, update fraction, current retained/new
validation losses, aggregate gradient statistics, previous policy value, and
an encoded history of recent interventions and outcomes.

All features are computed from information available at decision time. Future
validation outcomes and oracle support labels are prohibited inputs.

## Critic architecture

The primary critic is a small permutation-equivariant module-token transformer:

- shared module encoder MLP;
- two self-attention blocks over module tokens plus one global token;
- GRU state on the global token to represent recent learning dynamics;
- action embedding for the proposed single-module or pair intervention;
- ensemble of five independently initialized outcome heads.

Each head predicts means and log variances for the outcome vector and scalar
advantage. The ensemble supplies epistemic uncertainty. Module type/depth
features preserve meaningful ordering while the shared encoder avoids a
separate unconstrained network per module.

Capacity must be below 5% of main-network trainable parameters. An
equal-parameter independent-module MLP is the principal architectural control.

## Co-learning and gradient boundary

The critic learns online throughout Task B, but v1 uses a strict causal
boundary:

1. Snapshot the learner and optimizer at a scheduled audit point.
2. Generate a paired ordinary/intervention rollout from the identical
   snapshot, batches, replay samples, and RNG stream.
3. Record the realized outcome difference and behavior-policy propensity.
4. Add the transition to a bounded, recency-weighted critic replay buffer.
5. Update the critic from this buffer.
6. Restore the live learner; only the selected live action changes its
   trajectory.

No critic gradient flows through main-network optimization, and no main loss
updates critic parameters. This is still co-learning: critic data and policy
evolve with the live learner, but labels remain identifiable intervention
outcomes rather than gradients through a learned optimizer.

A differentiable meta-gradient critic is explicitly deferred until this
bandit/model-based version passes calibration.

## Exploration and causal identification

During the identification phase, interventions are assigned by a logged
randomized behavior policy:

- 50% ordinary;
- 25% randomly selected single-module `g=0.5`;
- 15% randomly selected single-module `g=0.9`;
- 10% randomly selected predeclared module-pair intervention.

Every action probability is stored. Module selection is uniform within the
eligible set. Common-random-number paired rollouts provide the primary labels;
inverse-propensity and doubly robust estimates provide a secondary audit
against selection or missing-rollout bias.

After calibration, the live policy uses a conservative lower-confidence bound:
choose a nonordinary action only when its 10th-percentile predicted advantage
is positive and its predicted Task-B penalty remains within tolerance.
Otherwise choose ordinary ePC. Ten percent of decision points remain
randomized and are reserved as an online audit stream; these samples are not
used for same-step policy selection.

## Preventing self-confirming behavior

- Never train or evaluate solely on actions chosen greedily by the critic.
- Log behavior propensities and retain randomized exploration throughout.
- Maintain a chronological held-out intervention buffer that is never used for
  critic fitting or early stopping.
- Evaluate calibration both on-policy and under the fixed randomized audit
  policy.
- Report effective sample size by action and module.
- Fail closed if any action/module cell lacks the frozen minimum coverage.

## Phase 0 fixtures

Use four synthetic families, each with train/calibration/confirmation seeds:

1. `local_specific`: intervention effects are primarily module-local.
2. `downstream_chain`: protecting an upstream module changes downstream
   representations and delayed retention.
3. `synergistic_pair`: neither single protection is useful but a specified
   pair is useful.
4. `null_or_harmful`: protection has zero or negative utility.

The existing overlapping-vocabulary planted fixture supplies task support and
load-bearing paths. Additional teacher/coupling settings create the known
downstream, pair-synergy, and null regimes. Ground truth is defined by
exhaustive paired rollouts over the finite v1 intervention family, not by
architectural labels alone.

Use calibration seeds to select only:

- rollout horizon from `{5, 20, 50}`;
- critic learning rate from `{1e-4, 3e-4}`;
- `lambda_B` consistent with the frozen Task-B tolerance;
- decision interval from `{10, 25}` updates.

Then freeze configuration and confirmation seeds before inspecting their
outcomes.

## Arms

All arms share initialization, batches, replay, optimizer, total main-network
updates, and supervised/KD mass.

1. `ordinary_epc`: no protection.
2. `support_gate`: existing online support score drives the soft gate.
3. `local_linear`: ridge model using local diagnostics only.
4. `independent_critic`: equal-capacity per-module critic without cross-module
   attention.
5. `global_critic_no_analytics`: global critic without support, Hessian, or
   commutator inputs.
6. `global_critic`: full proposed critic.
7. `exhaustive_oracle`: selects the best measured action from paired rollouts;
   synthetic upper bound only.
8. `random_policy`: same action-frequency budget as the critic policy.

## Primary critic-estimation gates

All must pass on every untouched confirmation fixture unless stated otherwise:

1. Held-out scalar-advantage Spearman correlation at least `0.50`.
2. Held-out advantage-sign AUROC at least `0.75`.
3. Expected calibration error of predicted beneficial-action probability at
   most `0.10`.
4. Mean squared outcome error strictly below constant, support-only, and
   local-linear baselines.
5. In `synergistic_pair`, the global critic's pair-action advantage error is
   at least 20% below the independent critic's.
6. In `null_or_harmful`, false beneficial-action rate at the conservative
   decision threshold is at most 5%.
7. Randomized-audit effective sample size is at least 50 for every action class
   and at least 20 for every module/action marginal.

Thresholds are initial protocol values and must be frozen in machine-readable
configuration before confirmation execution.

## Primary policy gates

On untouched seeds:

1. The global critic has lower mean retained-task forgetting than
   `ordinary_epc` and `support_gate`.
2. Its incoming-task final loss is no worse than `ordinary_epc + 0.02` nat.
3. Its paired scalar utility exceeds `ordinary_epc` with a 95% paired bootstrap
   confidence interval excluding zero.
4. It beats `random_policy` at the same nonordinary-action frequency.
5. It attains at least 50% of the exhaustive oracle's utility improvement over
   ordinary ePC in `local_specific` and `downstream_chain`.
6. Credit wavefront and entropy-rank ratios remain at least 0.90 of ordinary
   ePC; no nonfinite gradients, losses, or critic predictions occur.

Failure of any estimation gate blocks policy interpretation. Failure of any
policy gate blocks Shakespeare.

## Ablations and interpretation

Required ablations:

- remove support features;
- remove curvature/commutator features;
- remove recurrent history;
- replace global attention with independent module heads;
- replace randomized exploration with logged greedy data only, diagnostic
  arm only;
- permute module identities at evaluation;
- shuffle intervention outcomes within learner-state strata.

Analytic causal diagnostics are inputs and explanatory probes, not consistency
targets. A near-zero local commutator does not prove zero global utility, and a
large commutator does not determine intervention sign. Penalizing the critic
for disagreeing with these diagnostics is prohibited in v1.

Evidence for “capturing global causal structure” requires all of:

- held-out intervention prediction;
- cross-module architectural advantage over the independent critic;
- successful pair-synergy prediction;
- degradation under intervention-outcome shuffling;
- policy value on untouched learner trajectories.

Good utility alone is insufficient because it may arise from a task-phase
heuristic; good prediction alone is insufficient because it may not improve
routing.

## Contingent Shakespeare phase

Run only after all Phase-0 gates pass. Freeze the critic architecture,
hyperparameters, intervention family, horizon, utility weights, and policy
thresholds. Do not use synthetic oracle labels.

Use five untouched seeds and compare:

- ordinary ePC;
- support gate;
- local-linear critic;
- global critic;
- random policy matched for intervention frequency.

Primary endpoint: Task-A forgetting at matched Task-B tolerance. Secondary
endpoints: finite-update commutator, leakage, effective rank, credit wavefront,
critic held-out intervention calibration, action distribution, and overhead.

Promotion requires:

- global-critic mean forgetting at least `0.05` nat lower than ordinary ePC;
- improvement in at least four of five seeds;
- Task-B mean final loss no worse than ordinary `+0.02` nat;
- held-out intervention sign AUROC at least `0.65`;
- paired bootstrap 95% interval for scalar utility above zero;
- credit/rank gates at least 0.90;
- runtime overhead at most 2x ordinary ePC excluding explicitly reported audit
  rollouts.

No paid compute follows automatically. A successful local Shakespeare phase
would justify only a separately costed proposal.

## Stop conditions

Stop fail-closed if:

- paired rollouts are not bitwise state/batch/RNG matched before intervention;
- critic features contain future or oracle information;
- action propensities are absent or inconsistent;
- outcome labels cannot be reproduced from saved snapshots;
- critic/main gradients cross the frozen boundary;
- coverage or calibration gates fail;
- utility improves only by violating Task-B tolerance;
- results depend on post-confirmation threshold changes.

## Implementation seams and tests

Define:

- `CausalFeatureExtractor`;
- `InterventionPolicy`;
- `PairedRolloutOracle`;
- `GlobalCausalCritic`;
- `CriticReplay`;
- `CounterfactualAuditor`;
- `CriticDecisionReport`.

Minimum tests before any scientific run:

- exact snapshot/optimizer/RNG restoration;
- only selected gradient groups differ across paired arms;
- propensity probabilities sum to one and match empirical frequencies;
- no future outcome appears in features;
- critic and learner parameter sets are disjoint under backward;
- deterministic replay labels;
- synthetic positive, synergy, null, and harmful fixtures;
- confidence-bound fallback to ordinary ePC;
- shuffled-label critic fails;
- report refuses promotion with missing action cells or failed gates.

## Expected interpretation

A pass would show that an online critic can learn an action-relevant global
causal abstraction of a moving learner sufficiently well to improve routing.
It would not show recovery of the learner's complete causal graph.

A failure with good intervention prediction but poor policy value would
indicate that the intervention family or scalarized objective is inadequate.
A failure of held-out prediction would indicate insufficient observability,
coverage, horizon choice, or critic capacity. A global critic no better than
the independent critic would reject the claim that cross-module structure is
needed in this fixture.
