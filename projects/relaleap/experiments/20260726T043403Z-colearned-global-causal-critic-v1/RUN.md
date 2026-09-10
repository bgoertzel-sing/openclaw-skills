# Run 20260726T043403Z-colearned-global-causal-critic-v1: preregistration

- Project: `relaleap`
- Started: `2026-07-26T04:34:03Z`
- Finished: `2026-07-26T05:53:00Z`
- Status: `implementation gate passed; scientific experiment not run`
- Local or remote: `local design only`

## Question

Can a co-learned critic estimate held-out intervention effects over the
network's module set and use conservative update routing to improve the
retention-plasticity tradeoff over ordinary ePC and support gating?

## Hypothesis

Randomized paired interventions will identify an action-relevant global causal
abstraction. A joint module-token critic will outperform local/support
baselines on downstream and synergistic fixtures, and its conservative policy
will improve forgetting at matched plasticity.

## Frozen protocol

See `../../docs/colearned_global_causal_critic_protocol_v1.md`.

This record freezes the conceptual experiment structure, not final numeric
configuration. Calibration may select only the explicitly listed horizon,
critic learning rate, Task-B utility weight, and decision interval. A
machine-readable configuration and untouched confirmation seeds must be
committed before confirmation execution.

## Provenance

- Predecessor implementation: commit `b490f52`,
  branch `agent/online-causal-epc-v3`.
- Predecessor evidence:
  `../20260726T025745Z-online-causal-epc-v3/RUN.md`.
- v3 observation: support AUC `1.0` and planted oracle benefit, followed by a
  negative Shakespeare promotion result.
- Implementation commit: `690c8f7e0d6bf8866dba6440574a94b74a1bbae4`
  on `agent/colearned-causal-critic-v1`.
- Worktree:
  `projects/relaleap/worktrees/colearned-causal-critic-v1`.
- No GPU, remote resource, or paid compute was used.

## Research-rule application

Rules 1, 2, 5, 6, and 7 are primary. The protocol validates estimation before
policy use, states intervention semantics before code, requires reproducible
counterfactual evidence, limits the causal claim to an action/outcome
projection, and defines modular implementation seams.

## Acceptance test

The implementation phase is complete only when:

- deterministic paired-rollout and gradient-boundary tests pass;
- all synthetic confirmation estimation and policy gates are evaluated without
  threshold revision;
- raw interventions, propensities, outcomes, predictions, confidence bounds,
  and seeds are preserved;
- Shakespeare is run only if every Phase-0 gate passes;
- `RUN.md` separates observations, inference, and alternative explanations.

## Implemented components

- `CausalFeatureExtractor` with future/oracle-feature rejection;
- `RandomizedInterventionPolicy` with exact logged propensities;
- `LearnerSnapshot` and `PairedRolloutOracle` restoring model, optimizer,
  Python, NumPy, Torch, and CUDA RNG state;
- `CriticReplay` with separate immutable randomized-audit storage;
- `GlobalCausalCritic` and equal-interface `IndependentModuleCritic`;
- ensemble mean/variance heads and Gaussian critic loss;
- conservative lower-confidence-bound action selection;
- counterfactual coverage, Spearman, AUROC, calibration, MSE, and false-benefit
  reporting;
- analytic local, downstream-chain, synergistic-pair, and null/harmful
  fixtures.

## Results

### Focused implementation verification

Command:

`PYTHONPATH=src python3 -m pytest tests/test_causal_critic.py -q`

Result: `16 passed in 2.01s`.

The tests cover exact paired restoration, common random numbers, nonfinite and
propensity refusal, selected-group-only gradient scaling, future/oracle leakage
rejection, behavior-policy frequencies, critic interfaces and gradients,
critic/learner parameter separation, conservative fallback, audit-buffer
separation, missing-cell refusal, shuffled-label gate failure, and all four
analytic fixtures.

### Full repository verification

Command:

`PYTHONPATH=src:. /home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python -m pytest tests/ -q`

Result: `448 passed, 1 skipped in 22.84s`.

An initial system-Python full-suite attempt stopped during collection because
the sibling `causal_fibres` package was absent from that interpreter. The
repository's established virtual environment resolved the dependency; no test
or implementation change was made in response.

Compilation and `git diff --check` passed. The worktree is clean after commit.

## Interpretation

**Observed:** The implementation satisfies its deterministic interface and
integration tests.

**Not yet observed:** held-out intervention prediction, global-vs-independent
critic advantage, calibrated policy value, or improved forgetting.

The protocol replaces “causal support determines protection” with an
identified intervention-utility model. Support and local curvature diagnostics
remain observable features, but the critic's labels come from randomized
paired update interventions. The global-causal claim remains deliberately
narrow: predictive and decision-useful structure over the frozen intervention
family and rollout horizon.

## Next command

Add a machine-readable Phase-0 calibration configuration and runner that
generates logged paired transitions on the four analytic/planted fixture
families. Run calibration seeds only; freeze hyperparameters and untouched
confirmation seeds before confirmation.
