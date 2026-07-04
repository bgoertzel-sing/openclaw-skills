# Decision Log

## D-20260703-train-time-causal-factor-approach: Try train-time causal factor learning

- Date: `2026-07-03`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `projects/relaleap/docs/train_time_causal_factor_preregistration.md`

### Context

RelaLeap has passed through two inadequate phases:

1. `v0` seven-arm posthoc pregate: useful as a smoke scaffold, but fail-closed, with handcrafted LLC proxy and no arm beating required null controls.
2. `v2` parameterized arms fitted to cached residuals: deployable mechanisms failed winner recovery, lost to controls, and failed null specificity.

Both phases learned or selected residual bases after freezing residual caches. The SLT residual-layer direction instead treats residual columns as local charts on transformer failure modes and validates factorization by local evidence/free-energy additivity, causal audits, and LLC interaction information.

### Decision

Try a genuinely new **train-time causal factor learner** in which residual columns are discovered jointly during task training. The approach must be preregistered before implementation and must be evaluated first on synthetic ground-truth regimes with strict fail-closed controls.

### Alternatives considered

- Continue scaling v0 posthoc pregate: rejected because v0 was only a smoke harness and no arm beat nulls.
- Continue v2 cached-residual fitting: rejected as insufficient because deployable mechanisms failed controls/null specificity.
- Train a generic sparse dictionary end-to-end: insufficient unless causal audits, SLT additivity, split/merge/transfer rules, and matched null controls are built in.

### Rationale and evidence

The guiding SLT residual-layer source says residual columns should be validated by decomposition of local evidence/free energy and dominated interaction remainder, not raw reconstruction. The GPT-5.5 Pro v2 plan recommends fail-closed matched controls, synthetic ground-truth regimes, exact ablation calibration, commutator audits, and LLC interaction information.

### Consequences

- No GPU or paid compute is justified before synthetic gates pass.
- No implementation claim should be made from reconstruction quality alone.
- Promotion requires matched-control wins, dependency-aware null wins, calibrated causal audits, and interpretable sparse LLC interaction structure.
- `low_rank_trap` and `random_null` success means blocking the columnar claim, not forcing a positive result.

### Revisit trigger

Revisit if synthetic regimes show the train-time learner cannot separate exact factorized, shared-core, synergistic, low-rank, oblique, and null cases under matched controls, or if LLC/WBIC calibration fails.

### Supersedes or superseded by

Supersedes reliance on v0/v2 posthoc cached-residual basis fitting as the next scientific step.

## D-20260704-slt-estimator-validation-current-focus: Gate residual-layer work on Tiny Shakespeare estimator validation

- Date: `2026-07-04`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `docs/relaleap_slt_estimator_validation_plan.pdf`; `docs/slt_estimator_validation_plan_summary.md`

### Context

Ben directed that the new SLT estimator validation plan should become the current focus for RelaLeap. The prior residual-layer idea remains important, but the weak link is whether WBIC/SGLD/LLC estimators are meaningful enough to guide residual-layer construction rather than repeating the earlier handcrafted-proxy failure mode.

### Decision

Make SLT estimator validation the active RelaLeap focus. Proceed to SLT-guided residual-layer construction on top of the transformer only after all relevant estimators pass calibration and validation on a Tiny Shakespeare level corpus.

### Consequences

- Wave 0 interface/report-schema freeze and estimator validation work outrank new residual-layer mechanism development.
- Tiny Shakespeare is the first real-text validation target after analytic/synthetic calibration.
- Residual-layer guidance should consume validated estimator outputs, not uncalibrated or clipped proxy numbers.
- Failures in calibration, sampler diagnostics, MAP/prior/gauge checks, sample-size sensitivity, or Tiny Shakespeare validation block scientific promotion and keep residual-layer use gated.

### Revisit trigger

Revisit if Tiny Shakespeare-level validation is too expensive or inconclusive after analytic benchmarks pass, or if a smaller real-text proxy is explicitly chosen as an equivalent validation gate.

### Supersedes or superseded by

Temporarily prioritizes estimator validation over the 2026-07-03 train-time residual-column implementation path; it does not reject that path.

## D-20260704-controlled-frontier-model-routing: Treat Fable/GPT-5.6 throttling as an empirical operations risk

- Date: `2026-07-04`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `MEMORY.md`; `projects/relaleap/PROJECT.md`

### Context

Ben noted that Claude Fable may throttle or degrade work on certain topics, including advanced neural-network AI development, and that similar strategies may be needed for other controlled frontier models such as GPT-5.6-class systems. RelaLeap may be more likely to trigger this than symbolic-AI-heavy projects such as `petta-memory` or `petta-chem`, although properly framed SLT estimator validation may be less likely to trigger throttling because the immediate focus is estimator calibration rather than frontier-model optimization.

### Decision

When using Fable or similar controlled frontier models for RelaLeap, treat model throttling, downgrade, rerouting, refusal, or invisible quality degradation as an empirical operations risk. Keep prompts factually accurate while deliberately framing work by the real immediate research subgoal and nearest truthful low-friction category, record observed behavior by task type, compare outputs against other models or local methods, and keep estimator/core code and tests model-portable. Treat frontier-dev safeguards as ethically contested: they may have a coherent safety rationale, but are structurally entangled with competitive moat protection unless classifier scope, vetting criteria, and appeals are externally auditable.

### Consequences

- Do not depend on a single proprietary model for critical RelaLeap estimator, architecture, or scientific decisions.
- Do not lie or misrepresent tasks. It is acceptable to work around overly broad/sloppy provider filters by using accurate phrasing and legitimate “spin,” such as analytic SLT calibration, WBIC/SGLD estimator validation, or Tiny Shakespeare-level validation when that is the actual work.
- Record signs of degradation or model switching when Fable/GPT-5.6-class systems become available; hidden degradation is especially harmful because it corrupts research evidence.
- Prefer local/open-model/decentralized verification paths where possible, especially if RelaLeap succeeds in making open LLMs more capable.

### Revisit trigger

Revisit after empirical Fable/GPT-5.6-class usage data exists across RelaLeap, `petta-memory`, `petta-chem`, and other projects, or if provider policies/tooling become clearer.

## D-20260703-meaningful-slt-estimation-contract: Require calibrated SLT evidence before promotion

- Date: `2026-07-03`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `docs/train_time_causal_factor_preregistration.md`; `repos/relaleap/src/relaleap/reporting.py`

### Context

Ben emphasized that RelaLeap should be very sure it is estimating SLT parameters meaningfully this time. Earlier work failed this standard: the main LLC term was a handcrafted complexity proxy, and WBIC/LLC was a tiny frozen-parameter diagnostic rather than an estimate over the learner's actual trainable singular structure.

### Decision

Scientific promotion now requires a mandatory SLT-estimation validity contract. WBIC/SGLD/LLC panels must be finite-sample proxies over actual trained parameter blocks, calibrated on known-SLT benchmarks, accompanied by sampler/temperature diagnostics and explicit input coverage/inference-budget accounting, and interpreted through module-vs-joint estimates with sample-size sensitivity and null-normalized uncertainty.

### Consequences

- Task loss, reconstruction, causal ablations, and null wins are still insufficient if the SLT evidence panel is uncalibrated.
- Reports must use finite-sample language and must not claim exact RLCT estimation.
- Reports must show enough input coverage to make the estimator meaningful: input counts, stratification/coverage, inference budget, and sensitivity as input count increases.
- Code-level reporting now rejects `scientific_status=pass` unless required calibrated SLT evidence fields are present.
- If calibration or uncertainty fails, the correct status is `scientific_status = fail_closed`.

### Revisit trigger

Revisit only after the known-SLT calibration suite demonstrates stable, null-normalized recovery of expected regular, singular, independent, redundant, and synergistic behavior across seeds, input-count sweeps, and WBIC/SGLD settings.
