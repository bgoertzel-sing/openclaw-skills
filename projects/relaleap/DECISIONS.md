# Decision Log

## D-20260728-v4-functional-result-accepted-for-v4-1

- Date: `2026-07-28`
- Status: `accepted for V4-1 substrate intake only`
- Decision owner: Benjamin Goertzel
- Evidence: `experiments/20260728T162149Z-v4-functional-gate-nonlinear-torch/`
- Execution contract: `docs/v4-1_asset_intake_contract_20260728.md`

Ben explicitly accepts the nonlinear paired-rollout result as sufficient to
advance. The evidence is strong for the narrow operational claim that
`approximate_full_state_AD` predicts local paired `torch.optim.Adam` responses
on the tested nonlinear fixtures and is materially better than frozen-D under
high-LR stress.

The original V4-0 preregistration remains accurately recorded as
**inconclusive**: B2 and high-LR B1 missed the 5-sigma fixture-admission
precheck. This decision is an authorized progression choice, not a post-hoc
claim that that preregistered criterion passed. It opens V4-1 asset intake and
the `T=1` adapter-validation work only. It does not admit exact-D, JAX
reproduction, transformer or policy efficacy, V4-2, V4-3, or paid compute.

## D-20260727-commutator-critic-v4-preliminary

- Date: `2026-07-27`
- Status: `revision required before integration`
- Evidence:
  `experiments/20260727T080552Z-commutator-critic-v1-1-audit/`
- Source: `../../library/commutator-critic-v1-1/`

The V4 pivot is better identified than V1--V3: it measures the local
gradient/curvature/optimizer-state response and learns only a residual, while
recomputing positive-control truth per state and treating late-trajectory
signal loss explicitly. The supplied quadratic sandbox reproduced
byte-for-byte, so these fixture-level mechanisms merit continued local work.

Do not integrate or execute C2/policy stages yet. JAX-dependent nonlinear
claims remain unreproduced, and the supplied PyTorch backend failed all four of
its own bit-exact optimizer-replica admission tests on the target host. First
repair or explicitly version the functional optimizer equivalence, then
reproduce exact-D in an isolated reviewed JAX environment, then implement only
the minimal C0/C1 slice on a fresh branch. HDC footprints may propose sparse
pair edges, but measured commutator/cross-curvature terms must determine their
causal weights.

## D-20260728-v4-empirical-torch-admission

- Date: `2026-07-28`
- Status: `accepted for local validation`
- Decision owner: Benjamin Goertzel
- Evidence: `docs/causal_critic_v4_c4prime_execution_plan_20260727.md` V4-0

### Decision

Treat the failed Torch bit-exact functional-optimizer replicas as a
conformance diagnostic, not the primary scientific blocker. Admit a clearly
labeled `approximate_full_state_AD` backend only if it predicts direct paired
CRN counterfactual rollouts of the actual `torch.optim` nonlinear learner under
the frozen V4-0 empirical gate. It must beat or match frozen-D as specified.

### Consequences

A pass establishes local empirical usefulness of a full-state tangent on the
planted nonlinear fixture, not exact-D implementation equivalence, JAX
reproduction, transformer validity, C2 validity, routing-policy value, or C4′
readiness. A failure remains scientifically informative and blocks downstream
work.

## D-20260726-colearned-critic-v3-fixture-audit-failed

- Date: `2026-07-26`
- Status: `fail-closed before calibration/confirmation`
- Evidence:
  `worktrees/colearned-causal-critic-v1/experiments/20260726T184000Z-colearned-causal-critic-v3-preconfirmation-audit/`
- Implementation: `agent/colearned-causal-critic-v1` commit `5eb57db`

The v3 trajectory audit retained the intended family ordering through 75% of
its 100-update trajectory, but every family violated it at the final
checkpoint. The null/harmful positive-utility proportion was 0%, satisfying
its one-class check, yet its intervention ordering also failed. Per the frozen
protocol, stop before calibration or confirmation; do not tune fixture
coefficients, re-anchoring, or thresholds against this audit. Any successor
requires a new protocol version, fresh audit seeds, and fresh confirmation
seeds.

## D-20260726-colearned-critic-v2-preregistered

- Date: `2026-07-26`
- Status: `accepted for local confirmation`
- Implementation branch: `agent/colearned-causal-critic-v1`
- Protocol: `docs/colearned_global_causal_critic_protocol_v2.md`

Replace the analytic response formula with a trainable planted modular learner
before another critic confirmation. Preserve randomized common-RNG paired
identification, logged propensities, replay boundaries, coverage gates, and
critic/learner gradient separation.

Use a two-part beneficial-sign/conditional-amount ensemble as the primary
uncertainty model, optionally isotonic-calibrated on calibration seeds only.
Apply AUROC only to two-class families and use false-beneficial rate for the
one-class null. Require critic MSE below constant and support-only baselines;
report local-linear but require dominance only on explicitly nonlinear
fixtures. Freeze confirmation choices before execution.

Observed v1 failures motivate these changes but do not constitute v2 evidence.
The implemented planted-fixture infrastructure passed the full local suite
(`459 passed, 1 skipped`); critic-v2 confirmation remains unrun.

## D-20260725-colearned-critic-phase0-failed: Block policy interpretation

- Date: `2026-07-25`
- Status: `accepted for local calibration`
- Evidence:
  `worktrees/colearned-causal-critic-v1/experiments/20260726T063000Z-colearned-causal-critic-phase0/`
- Implementation branch: `agent/colearned-causal-critic-v1`

The global critic Phase-0 estimation conjunction failed on untouched analytic
confirmation seeds. Preserve the positive ordering, coverage, synergy
pair-error, and null false-benefit results, but do not interpret policy-arm
summaries or run Shakespeare. ECE failed in all four families; synergy sign
AUROC failed; and exact linear baselines correctly dominated the neural critic
in local/null. The null fixture contains no beneficial class, so its AUROC gate
is not identified, while the analytic fixture cannot emit the credit-wavefront
or entropy-rank policy diagnostics.

Any retry must be a versioned protocol repair with newly frozen confirmation
seeds. Prespecify a one-class null metric, nontrivial baseline fixtures,
calibration-only probability calibration, and a trainable planted learner for
trajectory-level policy and representation gates. Do not revise v1 thresholds
against the observed confirmation set.

## D-20260726-online-support-v3-confirmed-no-shakespeare-promotion

- Date: `2026-07-26`
- Status: `accepted for local calibration`
- Evidence: `experiments/20260726T025745Z-online-causal-epc-v3/`
- Implementation: `agent/online-causal-epc-v3` commit `b490f52`

Use sign-insensitive squared Hutchinson overlap to gate nonzero curvature
interaction, retain signed trace only as cooperative/antagonistic
classification, and use the direct module-local vector
`H_B g_A - H_A g_B` for the theorem-relevant commutator condition. Judge
ablation load-bearing on each module's own task; report cross-task effects as
facilitative/suppressive without the old `.05` bound.

All revised planted gates passed on untouched seeds, confirming that v2's
failures were gate-specification errors. The contingent Shakespeare run failed
its separate promotion gate because full-causal forgetting and finite-update
commutator were worse than ordinary ePC. Do not scale or use paid compute.

## D-20260726-online-support-v2-failed: Stop before Shakespeare

- Date: `2026-07-26`
- Status: `accepted for local calibration`
- Evidence: `experiments/20260726T023651Z-online-causal-epc-v2/`
- Implementation branch: `agent/online-causal-epc-v2`

The overlapping-vocabulary 90/10 teacher fixture repaired the exact-zero
interaction defect and made the dominant pathways reliably load-bearing.
Nevertheless, Phase 0 failed: signed `tr(H_A H_B)` was negative for some
modules/seeds, so the positive-baseline and shrinkage gates failed, and the
minority block's Task-A ablation effect exceeded the .05-nat cross-effect
limit. Do not run Shakespeare. Any third fixture must use untouched
confirmation seeds and justify whether signed curvature overlap or a
sign-insensitive quantity is the theorem-relevant diagnostic.

## D-20260726-online-support-phase0-failed: Repair planted fixture

- Date: `2026-07-26`
- Status: `accepted for local calibration`
- Evidence: `experiments/20260726T080000Z-online-causal-epc/`
- Implementation: `agent/online-causal-epc` commit `83abac8`

Do not run the Shakespeare phase. The estimator recovered architectural routing
(AUC 1.0) and gates acted correctly, but exact disjoint routing made the
protected mixed-Hessian baseline zero, precluding strict shrinkage. More
importantly, signed block-zero ablations were not reliably harmful on their own
tasks. A replacement positive control must jointly guarantee trained
load-bearing pathways and nonzero controlled cross-task curvature.

## D-20260726-causal-coding-epc-negative: Require planted support validation

- Date: `2026-07-26`
- Status: `accepted for local calibration`
- Decision owner: research agent; pending Ben review
- Related evidence:
  `experiments/20260726T003000Z-causal-coding-epc-5arm/`
- Implementation: `agent/cmcp-epc-kd-bridge` commit `4b0a425`

### Decision

Do not promote or scale the five-arm causal-coding ePC configuration. Before
another Tiny Shakespeare causal-routing run, construct a planted modular task
with known architectural `S_A/S_B`, validate support recovery and gate action,
and require the oracle-support arm to demonstrate a functional
retention/plasticity benefit.

### Evidence and rationale

The preregistered local CPU run completed all 15 records. The full causal stack
passed Task-B tolerance, finite-commutator reduction, rank, and credit-wavefront
checks, but worsened mean Task-A forgetting (4.9536 versus 4.8678) and did not
reduce pre-gate off-support leakage (.8572 versus .8551). Estimated supports
were seed-unstable and contained no A-only module in one seed. The true-label
intervention oracle reduced leakage and commutator but worsened forgetting, so
the fixture did not provide the intended positive control.

This does not reject the causal-continuous-learning theorem. It rejects the
claim that the current estimator, two-block fixture, and frozen regularizers
realize its useful modularity conditions.

## D-20260725-cmcp-epc-cl-negative: Do not promote CMCP-ePC to GPT-2

- Date: `2026-07-25`
- Status: `accepted for local calibration`
- Decision owner: research agent; pending Ben review
- Related evidence: experiment
  `20260725T231807Z-cmcp-epc-cl-phase1`

### Decision

Do not start the contingent GPT-2 CMCP-ePC experiment. In the frozen local
gate, CMCP-ePC failed to beat CMCP-KD on any functional continual-learning
endpoint and worsened forgetting relative to ordinary ePC in every seed.

### Interpretation and revisit trigger

Response novelty identified difference, not task-conditional usefulness: it
assigned about half the normalized mass to the arithmetic teacher and improved
plasticity at a large retention cost. Revisit only with a packet utility or
maintenance criterion validated on a fixture where teacher evidence is
conditionally useful on the actual student inputs; retain normalized mass and
explicit wall-time accounting.

## D-20260725-cmcp-selector-calibration: Use response novelty and direct KD in the fast calibration loop

- Date: `2026-07-25`
- Status: `accepted for local calibration`
- Decision owner: research agent; pending Ben review
- Related evidence: experiments `20260725T222650Z-cmcp-mass-normalized`
  through `20260725T231500Z-cmcp-carom-bridge`

### Decision

For this toy complementary-teacher selector calibration, normalize applied KD
mass, use response-space conditional novelty, and use direct KD for the fast
loop. Preserve ePC as a separate settled-error routing hypothesis rather than
claiming it has no value. Do not claim a CMCP--CAROM unification until CAROM
implements and identifies a comparable marginal-novelty/maintenance ledger.

### Rationale

Mass normalization collapsed the old fixture. The redesigned fixture gave
independent evidence positive value. Response novelty beat gradient novelty
under the frozen calibration rule and nearly matched oracle Task-B loss on
disjoint seeds, although it worsened retention. ePC improved plasticity but
worsened retention and cost about 2.17x runtime, failing the frozen joint gate.
CAROM E2/E3 currently lacks both the shared ledger and a completed scientific
outcome needed for convergence evidence.

## D-20260719-diagnostic-findings: ePC representation collapse and weight explosion

- Date: `2026-07-19`
- Status: `accepted`
- Decision owner: Benjamin Goertzel (pending review)
- Related evidence: experiment `20260719T135900Z-gpt2-diagnostic-cpu-battery`;
  commit `ee77c3e`

### Findings

CPU diagnostic battery on the 9 saved Run-2 checkpoints revealed:
1. ePC hidden states collapse to effective rank ~1.0 in layers 1-5 (vs 1.5-4.5
   for BP controls).
2. ePC layer 5 spectral norms are 20-40x larger than BP controls, with
   condition numbers 10-40x worse.
3. ePC gradient flow is U-shaped (high L0 and L5, dip in middle) while BP
   shows monotonic decay.

### Interpretation

The ePC objective as configured (lambda_output=0.05, steps=4) creates a
credit-assignment pathology: the output KD term dominates, causing
representation collapse in middle layers and compensatory weight explosion
in the last layer. This supports hypotheses 2 (restrictive representation)
and 3 (credit-assignment mismatch) from the outcome report.

### Next step

Design a follow-up GPU experiment with revised ePC hyperparameters:
- Increase lambda_output (e.g., to 0.3-0.5) to strengthen local prediction
  errors relative to the output term.
- Or enable the hidden-state matching arm (already configured but disabled)
  to maintain representation diversity.
- Preregister the revised config, obtain explicit bounded approval, and run
  3-seed distillation + outcome battery on GPU.

## D-20260719-r5-negative-result: ePC_KD fails the GPT-2 six-layer distillation gate

- Date: `2026-07-19`
- Status: `accepted`
- Decision owner: Benjamin Goertzel (pending review)
- Related evidence: experiment `r5-runpod-20260719`; commit `dc61f31`;
  summary.json with promotion eval

### Outcome

The r5 Runpod distillation stage (3 seeds, GPT-2 six-layer student,
WikiText-103) completed validly, but its separately requested Stage-2 outcome
battery did not execute. ePC_KD failed all four distillation-promotion criteria:

- Update-matched gain: −0.52 nats (ePC_KD worse than BP+KD at 1000 updates)
- Wall-clock-matched gain: −1.56 nats (ePC_KD worse — BP+KD does ~4× updates)
- Per-seed regression: up to 0.569 nats worse
- ePC_KD (6.49–6.54) also worse than plain BP+CE (5.25–5.30)

One positive signal: activity_energy_monotone=true for all ePC_KD runs.
kd_gap_nats very high (~880–893), suggesting poor teacher→student learning
under ePC at this scale.

### Decision

The twelve-layer confirmation run is **not authorized**. The distillation gate
is a scientifically valid negative result, while the independently completed
outcome battery is recorded at
`experiments/20260718T223300Z-epc-outcome-6layer-battery/`. Before any further ePC
GPU work, diagnose whether the failure is:
1. A fundamental ePC scaling issue (energy relaxation doesn't help at GPT-2 scale),
2. A credit-assignment configuration problem (kd_gap too high), or
3. A hyperparameter/learning-rate issue specific to the ePC arm.

The activity_energy_monotone signal suggests the ePC mechanism itself is
functioning, but not translating into student improvement.

## D-20260717-six-then-twelve-epc-depth: Gate twelve layers on six

- Date: `2026-07-17`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related evidence: commit `7d4d4dc`; experiment
  `20260717T154506Z-epc-outcome-6layer-preflight`

### Decision

Run the scalable six-layer GPT-2-width ePC/BP/KD outcome comparison first, then
move to a twelve-layer student after the six-layer gate completes validly. Keep
the source/target domains, seeds, common low-rank adaptation rule, metrics, and
decision thresholds fixed across depths; only depth and the separately
approved resource envelope may change.

### Consequences

- Six layers is the immediate paid-compute gate and requires explicit approval
  of its recorded USD 7 total cap before provisioning.
- Twelve layers is preregistered as a contingent confirmation, not authorized
  by approval of the six-layer job.
- Invalid provenance, incomplete checkpoints, or a failed six-layer systems
  gate blocks the twelve-layer run. A scientifically negative but valid
  six-layer outcome is still reported before deciding whether the confirmation
  remains informative.

## D-20260717-evaluate-epc-network-outcomes: Test structural and adaptation outcomes

- Date: `2026-07-17`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related evidence: `docs/epc_outcome_probe_protocol.md`; experiment
  `20260717T145830Z-epc-outcome-probe-local-v1`; implementation `e398876`

### Decision

Because BP, KD, and ePC produced nearly equal loss in the corrected local gate,
evaluate whether ePC produces a network with other advantages. Start with a
small local instrument/effect-size pilot, then move quickly to a more scalable
and informative RunPod test after freezing the domain shift, checkpoints,
metrics, controls, runtime, and cost.

The primary endpoint is the adaptation/forgetting tradeoff under an identical
post-training update rule. Structural similarity, spectral rank, block-skip
sensitivity, and corruption/OOD robustness are secondary diagnostics. A
structural difference without functional benefit is descriptive, not grounds
for promotion.

### Consequences

- The prior perplexity comparison remains valid but is no longer the sole
  scientific question.
- The aborted July 17 GPU artifacts remain provenance-ineligible and cannot be
  reused as the checkpoint trio.
- Paid execution requires a new remote job record and explicit bounded approval.
- The local v1 run validates instrumentation only; its weak chronological split
  cannot support an ePC plasticity conclusion.

## D-20260714-sgld-pilot-before-production: Gate the next SGLD production run on a step-size pilot

- Date: `2026-07-14`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `docs/sgld_tuning_plan.md`; experiments `20260714T182809Z-sgld-step-size-sweep-targeted` and `20260714T182834Z-sgld-step-size-sweep-full-suite`

### Context

The prior A100 run had energy R-hat mean 2.0 and maximum 3.3 despite some ESS improvement, so increasing chain length without identifying a usable discretization regime would risk paying for autocorrelated or unstable samples.

### Decision

Before another production run, test about six step sizes with two 500-step chains. Reject divergence; require R-hat below 1.2 and mean ESS above 50 to proceed. If the best unpreconditioned candidate remains above R-hat 1.1, estimate a diagonal gradient-variance preconditioner and repeat the sweep.

### Consequences

- The approximately 6,000-step diagnostic is cheaper than another failed 8,000-step production configuration.
- A passing pilot permits a production attempt but does not replace full production convergence diagnostics.
- An all-high-R-hat sweep triggers preconditioning rather than a hopeful longer run.

### Revisit trigger

Revisit thresholds after empirical calibration against analytic benchmarks or if the short-chain R-hat estimate proves too noisy to rank candidates reliably.

## D-20260709-hdpc-before-slt-columnar-upgrades: Try HDPC/ePC Tiny Shakespeare first

- Date: `2026-07-09`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: HDPC working draft; Goemaere et al. 2026 ePC paper; planned branch `agent/tinyshakespeare-hdpc`

### Context

Ben supplied an HDPC working draft describing homotopy distillation from backprop-trained transformers into PC-consistent learners plus energy-coupled PC crowns, and the Goemaere et al. ePC paper as background. The prior RelaLeap sequence emphasized SLT estimator validation before SLT-guided residual-layer construction, while SLT measurement work is still running/concluding.

### Decision

Try the HDPC/ePC plan first on the Tiny Shakespeare corpus. Use a bounded Runpod GPU run only after explicit resource/time/cost approval and after local tests/smoke checks. Treat SLT inputs to the process and columnar residual-layer models as afterwards upgrades, not prerequisites for the first HDPC prototype.

### Consequences

- The immediate implementation target is technical viability of homotopy-distilled PC learners and identity-initialized PC crowns on Tiny Shakespeare.
- Initial tests must catch silent failure modes: ordinary-BP leakage from detach mistakes, dropout/KV-cache misuse, non-monotone relaxation, mixed-precision error decay, and loss of the pure-KD anchor.
- SLT/WBIC/LLC validation remains required before scientific promotion of causal residual columns or SLT-guided claims, but it no longer blocks the first HDPC/ePC engineering prototype.
- Runpod approval must specify provider/account context, GPU/resource/image/storage/region, current price source, expected duration, maximum cost/time, data upload scope, artifact retrieval, and termination/cleanup behavior.

### Revisit trigger

Revisit if the Tiny Shakespeare HDPC prototype fails the anchor/path/distinctness/crown-identity tests, if Runpod cost is unjustified after local smoke tests, or after baseline HDPC results are strong enough to justify adding SLT inputs and columnar residual structure.

## D-20260725-colearned-global-causal-critic-v1: Preregister an intervention-trained critic

- Date: `2026-07-25`
- Status: `protocol accepted for implementation; core implemented, experiment unrun`
- Decision owner: Benjamin Goertzel requested the concrete protocol
- Related task/run: `docs/colearned_global_causal_critic_protocol_v1.md`;
  `experiments/20260726T043403Z-colearned-global-causal-critic-v1/`

### Context

The v3 estimator recovered planted support with AUC 1.0 and the planted oracle
improved retention, but estimated and oracle support routing both failed to
improve the Shakespeare retention/plasticity tradeoff. Support identifies
participation; it does not identify which update intervention is useful.

### Proposed decision

Test a co-learned critic as an action-relevant abstraction of the learner's
global causal dynamics. Train it online from logged randomized, paired
interventions over module gradient-protection actions. Require held-out
counterfactual calibration before allowing its conservative policy to control
routing.

The v1 critic is model-based/bandit-style with a hard gradient boundary.
Differentiating through the learner is deferred until intervention prediction
and policy value are established.

### Rationale

Randomized intervention assignments identify the critic's targets while
co-learning keeps its model adapted to the moving learner. Joint attention
over module tokens can represent downstream and synergistic effects that an
independent support gate cannot. Local analytic diagnostics remain informative
features, but forcing critic predictions to agree with them would circularly
reinstate the failed support-routing assumption.

### Consequences

- No Shakespeare or paid compute until all synthetic estimation and policy
  gates pass.
- “Global causal structure” means the intervention/outcome projection defined
  by the protocol, not recovery of a complete causal graph.
- Utility and causal prediction are tested separately: good task utility alone
  may be a heuristic, while good prediction alone may not improve routing.
- All actions, propensities, paired snapshots, outcomes, and uncertainty
  estimates must be preserved.

### Implementation status

Core implementation landed locally at commit `690c8f7` on
`agent/colearned-causal-critic-v1`. Sixteen focused tests and the full suite
(`448 passed, 1 skipped`) passed. This does not adopt or validate the critic's
scientific hypothesis; calibration and confirmation remain gated.

### Revisit trigger

Revisit if the critic cannot predict held-out intervention effects, if a global
critic does not beat an equal-capacity independent critic on downstream or
synergy fixtures, or if calibrated prediction fails to yield policy value.

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
# D-20260715-epc-distillation-first

- Date: `2026-07-15`
- Status: `accepted`
- Decision owner: Benjamin Goertzel

Make effective ePC-based distillation of Tiny Shakespeare backprop transformers the immediate RelaLeap objective. Treat the columnar predictive-coding head with SLT guidance as the next stage, gated on a reproducible ePC distillation benefit. The first experiment must isolate relaxation depth from optimizer and stochastic-state drift, compare against matched BP and conventional KD, and fail closed unless a nontrivial `T>1` configuration improves held-out behavior across seeds while satisfying energy and gradient diagnostics.

## D-20260715-epc-gate-null: Do not promote the first block-state ePC objective

- Date: `2026-07-15`
- Status: `accepted result`
- Decision owner: Benjamin Goertzel's preregistered fail-closed gate
- Evidence: `experiments/20260715T153035Z-epc-distillation-gate-local-r2/RUN.md`; code commit `941b8b3`

The first matched-state three-seed diagnostic validated execution, exact
depth-one KD equivalence, monotone activity energy, and finite layerwise
gradients, but no genuine relaxation depth beat matched ordinary KD in every
seed. Do not scale this objective or begin columnar/crown/SLT-guided head work.
First determine whether output-KL/local-error scaling or layerwise credit
assignment explains the gap, and validate a revised mechanism on a synthetic
known-signal case under a newly frozen protocol.

### 2026-07-15 follow-up

The scaling defect was confirmed and corrected; synthetic local-credit tests
passed. A separately frozen v2 on untouched seeds materially increased deep
block credit but again failed to beat matched KD. This strengthens, rather than
relaxes, the decision: do not promote the current block-state objective. The
next run must test a distinct credit-assignment hypothesis, not another tuning
of lambda or relaxation depth.

## D-20260716-gpt2-small-pilot-protocol: Preregister the minimum GPT-2 pilot

- Date: `2026-07-16`
- Status: `proposed protocol; frozen before outcomes`
- Decision owner: Ben's GPT-2-small priority; numeric protocol drafted by the
  RelaLeap progress worker for Ben's review
- Contract: `worktrees/tinyshakespeare-hdpc/configs/gpt2_small_epc_pilot.json`

Do not iterate further on Tiny Shakespeare; it is below the scale needed to
resolve the hypothesis. Test a six-layer GPT-2-width student distilled from the
pinned 124M GPT-2 teacher on pinned WikiText-103. Keep hidden-state matching a
separate exploratory arm. Compare primary ePC against ordinary BP+KD under both
equal updates and equal elapsed time across three fixed seeds, and apply the
pre-run validation-loss/invariant criterion exactly. Passing promotes only a
larger confirmation. GPU execution remains separately gated on a successful
CPU dry-run and Ben's explicit bounded RunPod approval.
## D-20260727-c4prime-staged-execution: Admit the V4 bridge only through backend and substrate gates

- Date: `2026-07-27`
- Status: `accepted planning decision`
- Evidence: `docs/causal_critic_v4_c4prime_execution_plan_20260727.md`,
  `../../library/commutator-critic-c4prime-2026/SOURCE.md`, and
  `experiments/20260727T080552Z-commutator-critic-v1-1-audit/`.

The C4′ companion note gives the V4 critic a potentially valuable
function-pinned substrate, but it remains a proposed specification.  Sequence
the persistent work as V4-0 backend admission, V4-1 exact-asset/T=1 adapter
validation, V4-2 preregistration plus measured microprofile, and only then a
separately approved V4-3 deployment.

The Torch replica failures and absent JAX reproduction block exact-D admission.
Missing production checkpoints and settle code independently block substrate
validation.  Do not integrate the critic into RelaLeap, infer C2 validity,
open policy work, or spend on C4′ until the preceding gates pass.

Alternatives rejected: treating the quadratic sandbox as a transformer
validation; accepting a post-hoc tolerance as bit exactness; using reported
Mesto metrics without the pinned artifact bundle; and treating the proposed
45-A100-hour ceiling as authorization.
# 2026-07-28 — Label the GPU-ready transformer step as a clean-room hybrid

Decision: the locally validated GPT-2 PCStep seam is named
`clean_room_transformer_epc_v1`. It may support a bounded GPU engineering
smoke after separate costed approval, but it must not be described as Mesto
checkpoint-compatible or as a source-aligned transformer-local update.

Rationale: Mesto's public `metta-on-mork` `pcgraph` code fixes the
settle-then-update phase order and supplies checked XOR semantics, but it does
not specify attention, MLP, layer-normalization, tied-embedding, optimizer, or
transformer-local learning rules. The implemented seam therefore freezes
weights during block-state settlement and then uses explicit block gates with
ordinary autograd/AdamW. This is testable engineering progress while
preserving the production-asset boundary.

Evidence:
`experiments/20260728T184216Z-v4-1-gpt2-pcstep-preflight/` and
`experiments/20260728T184406Z-v4-1-gpt2-pcstep-full-suite/`.
