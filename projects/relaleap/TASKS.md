# Tasks

- [ ] Freeze and CPU-validate the clean-room multi-step GPT-2 ePC experiment
  runner requested by Ben on 2026-07-28. Deliverable: exact seeded batch-plan,
  paired ordinary-KD/ePC arms, periodic snapshot/replay checks, structured
  metrics/checkpoints, fixed stop/failure conditions, and a costed RunPod
  launch record. Acceptance: narrow CPU fixture proves multi-step exact replay
  and no settle-time parameter mutation; all expected arm records validate;
  focused tests and `git diff --check` pass. Next command: inspect the frozen
  pilot runner/data contract and implement a clean-room runner that invokes
  `PCStepAdapter` at every ePC update. Evidence path:
  `experiments/20260728T*-clean-room-transformer-epc-multistep-preflight/`.

- [x] Execute the approved bounded GPU engineering smoke for
  `clean_room_transformer_epc_v1`. Acceptance: a six-layer GPT-2 student and
  frozen GPT-2 teacher complete one CUDA T=1 step with frozen settlement and
  byte-exact replay; artifacts are returned/hashed and the pod is terminated.
  Completed 2026-07-28 at source commit `b86e156`: all execution invariants
  passed on an RTX 4090 with 3.14 GB peak allocation. The RunPod pod was
  deleted after hash-verified retrieval. Evidence:
  `experiments/20260728T195248Z-clean-room-transformer-epc-gpu-smoke/`.

- [x] Complete the V4-1 transformer-scale `PCStepAdapter` GPU-preflight seam.
  Deliverable: a pure, gated GPT-2 block-state settlement/local-update step
  built on the existing Hugging Face GPT-2 adapter, with explicit separation
  between source-aligned `pcgraph` semantics and our transformer
  generalization. Acceptance: a tiny GPT-2 CPU fixture proves frozen weights
  during settlement, finite local gradients, deterministic replay, exact
  snapshot/restore, fail-closed gates, and `T=1` KD-endpoint compatibility;
  focused and full relevant tests plus `git diff --check` pass. Next command:
  create an isolated `agent/v4-gpt2-pcstep` worktree and run the focused GPT-2
  adapter tests. Evidence:
  Completed 2026-07-28 at local commit `19e1022` on
  `agent/v4-gpt2-pcstep`: 11 focused adapter tests,
  30 broader GPT-2/pilot tests, and the complete 155-test suite passed;
  compilation and `git diff --check` passed. The implementation is explicitly
  `clean_room_transformer_epc_v1`, using frozen block-state settlement followed
  by gated global autograd/AdamW; it is not represented as Mesto's unpublished
  transformer-local rule. Evidence:
  `experiments/20260728T184216Z-v4-1-gpt2-pcstep-preflight/` and
  `experiments/20260728T184406Z-v4-1-gpt2-pcstep-full-suite/`.

- [x] Align the V4-1 `T=1` adapter with Mesto's public `metta-on-mork`
  `demos/pcgraph` implementation at commit
  `45a0b51dce76fd8d620984e812317f6ed3a01204`, with Claude Fable as delegated
  designer/reviewer. Deliverable: a provenance-explicit adapter or translation
  seam plus deterministic tests against the checked `pcgraph` one-tick oracle;
  identify exactly which GPT-2 homotopy components and checkpoints remain
  absent. Acceptance: source equations/sign conventions/state cells are mapped;
  one-tick settlement and local update agree within the source's stated fp32
  tolerance; frozen-weight and exact snapshot/restore invariants remain; GPL
  code is not copied without attribution/licence handling; focused tests and
  scoped `git diff --check` pass. Completed 2026-07-28: five tests pass against
  the checked one-tick and end-of-settle m1 records, plus compilation,
  whitespace, and credential checks. This validates only the public XOR seam;
  observed GPT-2 trainer/checkpoints/config/data/transformer rules/telemetry
  remain absent. Evidence:
  `experiments/20260728T181641Z-v4-1-pcgraph-source-alignment-fable/`.

- [x] Build a clean-room V4-1 `T=1` PC--GPT-2 adapter prototype from the
  supplied Mesto paper, with Claude Fable as the delegated designer.
  Deliverable: reviewable local code implementing the paper-derived settlement
  and local-update seam, an explicit assumptions/deviations document, and
  deterministic unit tests. Acceptance: the adapter has a pure
  `(theta, optimizer_state, batch, t, gate) -> state` boundary; asserts weights
  remain frozen during settlement; snapshot/restore is exact on the synthetic
  test fixture; `T=1` matches the defined reference update; focused tests and
  `git diff --check` pass. This is a clean-room executable hypothesis, not a
  reproduction of Mesto's unpublished code or checkpoints. Completed
  2026-07-28: five focused deterministic tests, compilation, and scoped
  `git diff --check` pass. The production V4-1 intake remains separately
  blocked on exact assets and licence terms. Evidence:
  `experiments/20260728T181111Z-v4-1-clean-room-pcstep-fable/`.

- [ ] Execute the evidence-gated V4 / C4′ causal-critic plan.
  Deliverable: a versioned backend-admission record; a pure T=1
  `PCStepAdapter` only after exact Mesto assets arrive; and a frozen C4′
  bridge preregistration before any E-line outcome or remote run. Acceptance:
  V4-0 empirical result is explicitly accepted for V4-1 progression by Ben;
  V4-1 proves exact
  state restoration, frozen settle weights, and the C4-class T=1 anchor; V4-2
  freezes the estimand/floors/action table/budget cut before an E-line seed;
  C4′ itself remains conditional on explicit resource approval. Ben amended
  V4-0 on 2026-07-28: Torch bit-exactness is diagnostic rather than the
  scientific admission gate. Next command: implement the frozen empirical
  nonlinear-tangent validation against direct paired CRN `torch.optim`
  rollouts, while retaining the mismatch record and JAX reproduction as
  separate work; do not integrate, claim C2 validity, start policy work, or
  request GPU resources. Evidence:
  `docs/causal_critic_v4_c4prime_execution_plan_20260727.md`,
  `../../library/commutator-critic-c4prime-2026/SOURCE.md`, and
  `experiments/20260727T080552Z-commutator-critic-v1-1-audit/`.
  Result 2026-07-28: the nonlinear float64 CPU run is INCONCLUSIVE because
  the frozen >=5-sigma admission precheck passed B1 (5.741) but not B2
  (3.033) or high-LR B1 (0.868). Descriptively, full-state Spearman remained
  .969-.9999 and was non-inferior to frozen-D in all cells; at high LR/h25 it
  was .969 versus .196. The aligned no-signal control had 0% false
  beneficials. Ben then explicitly accepted the result as sufficient to
  proceed to V4-1, without
  reclassifying the preregistered result as a statistical pass. Next command:
  receive and hash the exact Mesto asset bundle, then perform the V4-1
  import/snapshot-restore/T=1 adapter checks; no substitute substrate or
  remote run. Acceptance: the complete receipt and V4-1 adapter gates in
  `docs/v4-1_asset_intake_contract_20260728.md` pass. Evidence:
  `experiments/20260728T162149Z-v4-functional-gate-nonlinear-torch/`.
- [ ] Audit and reproduce the supplied RelaLeap V4 commutator-critic package.
  Deliverable: preserve the PDF and three archives with hashes; inspect the
  sandbox, skeleton, and patch set; rerun the available CPU checks without
  installing unreviewed dependencies; compare the measured claims with the
  V1--V3 negative evidence; and record a go/revise/stop recommendation for
  C0/C1. Acceptance: quadratic results are independently reproduced or any
  mismatch is localized; the packaged `comcrit` tests and patch-application
  state are checked; JAX-dependent claims are explicitly marked supplied-only
  if JAX remains unavailable; project and experiment records point to raw
  evidence. Next command: create the source-library item and local audit ledger,
  then run the quadratic demo and packaged tests. Evidence:
  `../../library/commutator-critic-v1-1/` and
  `experiments/20260727T*-commutator-critic-v1-1-audit/`.
  Partial result 2026-07-27: quadratic output reproduced byte-for-byte and
  built-in NumPy selftest passed. Packaged suite is `5 passed, 4 failed,
  1 skipped`; every failure is a PyTorch optimizer-replica bit-exactness gate.
  JAX claims remain unrun because JAX is absent. Next command: diagnose the
  functional optimizer operation-order/version mismatch in an isolated copy;
  do not integrate into RelaLeap until the backend gate passes.

- [x] Run the frozen co-learned global causal critic v1 Phase-0 calibration
  and confirmation locally. Deliverable: deterministic runner, frozen
  machine-readable calibration choice and disjoint seeds, raw logged paired
  transitions/predictions/confidence bounds, estimation and (only if
  unblocked) policy gate results, full-suite verification, and a fail-closed
  experiment record. Acceptance test: every frozen Phase-0 gate is evaluated
  without post-confirmation threshold changes; coverage reaches 50 per action
  class and 20 per module/action marginal; policy interpretation occurs only
  after every estimation gate passes; raw JSON and exact reproduction command
  are retained. Next command: implement and test
  `scripts/run_causal_critic_phase0.py` against the four analytic fixtures.
  Evidence:
  `experiments/20260726T*-colearned-causal-critic-phase0/`.
  Completed locally on 2026-07-25: 18 focused and 450 full tests passed
  (1 skipped). Confirmation failed ECE in all four families, synergy AUROC,
  and strict baseline dominance in local/null. Estimation passed Spearman,
  synergy global-vs-independent error, null false-benefit, and coverage.
  Policy interpretation and Shakespeare are blocked. Next command: draft a
  versioned repair protocol with a prespecified one-class null metric,
  nontrivially nonlinear local/null fixtures, probability calibration learned
  only on calibration seeds, and a trainable fixture exposing credit/rank
  diagnostics; allocate fresh confirmation seeds before implementation.

- [x] Implement the co-learned global causal critic v1 locally.
  Deliverable: modular feature extractor, randomized intervention policy,
  exact paired-rollout oracle, bounded critic replay, global and independent
  critics, uncertainty-aware decision policy, counterfactual auditor, planted
  local/downstream/synergy/null fixtures, and deterministic tests. Acceptance
  test: paired learner/optimizer/RNG restoration is exact; only selected
  gradient groups differ; propensities are valid; future/oracle leakage is
  rejected; critic/learner gradients are disjoint; replay labels reproduce;
  shuffled labels and missing action cells fail closed; focused and full test
  suites pass. Next command: create
  `projects/relaleap/worktrees/colearned-causal-critic-v1` from `b490f52` and
  add deterministic paired-rollout tests before critic training. Evidence:
  `experiments/20260726T043403Z-colearned-global-causal-critic-v1/RUN.md`.
  Completed at commit `690c8f7` on
  `agent/colearned-causal-critic-v1`: 16 focused tests passed; the full suite
  passed 448 with 1 skipped. This closes the implementation gate only. The
  preregistered calibration and untouched confirmation remain unrun.

- [x] Draft the co-learned global causal critic v1 experiment protocol.
  Deliverable: preregistered architecture, intervention-based identification
  scheme, online learning rule, planted calibration, matched controls,
  ablations, frozen promotion gates, stop conditions, and implementation
  seams. Acceptance test: the protocol distinguishes support from intervention
  utility; obtains critic labels from randomized paired interventions; measures
  held-out counterfactual calibration and policy value; prevents critic/main
  gradient leakage; and blocks Shakespeare unless all synthetic gates pass.
  Next command: implement the critic and counterfactual audit API in a fresh
  worktree from `b490f52`, beginning with deterministic paired-rollout tests.
  Evidence:
  `docs/colearned_global_causal_critic_protocol_v1.md` and
  `experiments/20260726T043403Z-colearned-global-causal-critic-v1/RUN.md`.

- [x] Confirm the online causal-support estimator with sign-insensitive
  curvature diagnostics (v3). Deliverable: add Hutchinson/Frobenius interaction
  magnitude, curvature-sign classification, per-module
  `H_B g_A - H_A g_B`, and facilitative/suppressive ablation reporting on
  branch `agent/online-causal-epc-v3`; run three untouched frozen Phase-0 seeds
  locally and run Shakespeare only if every revised gate passes. Acceptance
  test: focused diagnostics tests and the full existing suite pass; Phase 0
  emits finite per-module overlap and commutator metrics, AUC >= .85, oracle
  specificity >= .8, own-task ablations >= .1 nat, and lower oracle forgetting;
  the durable run record reports the fail-closed decision. Next command: create
  a clean v3 worktree at commit `4ca1b5e`, freeze confirmation seeds in the run
  record/config, then implement focused tests. Evidence path:
  `experiments/20260726T025745Z-online-causal-epc-v3/`.
  Completed on frozen seeds `8147, 12289, 24593`: all seven revised Phase-0
  gates passed, focused tests passed 8/8, and the full suite passed 432 with 1
  skipped. The contingent 15-arm Shakespeare run completed but failed its
  existing promotion gate on forgetting and finite-update commutator. Do not
  scale. Implementation commit: `b490f52` on
  `agent/online-causal-epc-v3`.

- [x] Redesign and rerun the online causal-ePC planted positive control (v2).
  Deliverable: overlapping-vocabulary teacher fixture with controlled nonzero
  cross-path coupling, updated tests/runner, three-seed five-arm Phase 0, and
  fail-closed experiment record. Acceptance: support AUC >= .85; oracle gate
  specificity >= .8; every ordinary module has positive mixed-Hessian trace;
  protected trace shrinks >=10%; own-task block ablations cost >=.1 nat with
  cross-task effects <=.05 nat; oracle forgetting is strictly below ordinary;
  focused and full suites pass; Shakespeare runs only if all gates pass.
  Next command: `PYTHONPATH=src:. ../../../../../../.venv/bin/python -m pytest
  tests/test_online_support.py -q`. Evidence:
  `experiments/20260726T023651Z-online-causal-epc-v2/`. Completed fail-closed:
  430 tests passed (1 skipped); support, gate action, dominant pathway
  load-bearing effects, and oracle advantage passed, but signed mixed-Hessian
  positivity failed and the minority-path Task-A cross-effect exceeded .05
  nat. Shakespeare was not run.

- [x] Implement and run the online multi-signal causal-support + soft-gating
  ePC experiment requested 2026-07-25. Deliverable: planted modular fixture,
  online gradient-ratio/cosine/Fisher/CKA estimator, soft gates, mixed-Hessian
  diagnostic, five matched arms, and conditional Shakespeare phase. Acceptance:
  focused estimator/fixture tests and full suite pass; three-seed Phase 0
  reports support AUC >= .90, correct gate action, mixed-Hessian shrinkage, and
  oracle retention benefit; Phase 1 runs only if every Phase 0 gate passes;
  frozen protocol, raw metrics, hashes, interpretation, and commits are
  durable. Next command: create `agent/online-causal-epc` at `4b0a425`, freeze
  the run record, then implement `online_support.py` and
  `planted_modular.py`. Evidence:
  `experiments/20260726T080000Z-online-causal-epc/`. Completed fail-closed:
  15/15 Phase-0 records and 429 full tests passed; support AUC and gate action
  passed, but mixed-Hessian shrinkage was impossible from an identically zero
  baseline and the ablation audit found the planted paths not reliably
  load-bearing. Shakespeare was not run. Implementation commit `83abac8`.

- [x] Implement and run the preregistered five-arm causal-coding ePC local CPU
  experiment requested 2026-07-25. Deliverable: ordinary ePC, gated ePC,
  gated+clarity, gated+clarity+commutator, and oracle-support ePC across seeds
  1729/3253/6421 with matched KD mass, initialization, batches, optimizer, and
  schedule; retain raw metrics and a conclusion against the frozen joint gate.
  Acceptance: support-estimator fixtures and mechanism tests pass; 15/15
  records contain the complete CL/representation/robustness/commutator/leakage
  battery; the full repository suite passes; protocol and result are recorded
  in a timestamped experiment directory; implementation and records are
  committed on `agent/cmcp-epc-kd-bridge`. Completed 2026-07-26: 15/15 records,
  exact KD mass, monotone ePC, full credit wavefront, and 424 post-run tests
  passed. The full arm reduced the finite commutator but worsened forgetting
  and failed to reduce pre-gate leakage, so the frozen 6/6 joint gate failed
  4/6. The true-label oracle also lacked a functional advantage. Next command:
  design a planted modular fixture with known architectural supports and verify
  support recovery/oracle benefit before revisiting Shakespeare. Evidence:
  `experiments/20260726T003000Z-causal-coding-epc-5arm/`.

- [x] Ingest and theorem-audit Ben's `Causal Coding and the General
  Causal-Continual-Learning Theorem` v1 manuscript. Deliverable: preserved PDF
  and searchable text, provenance sidecar, links to the current RelaLeap
  evidence, and explicit validity gaps. Acceptance: source hash is recorded;
  continuous, discrete, and categorical claims are checked separately; the
  result distinguishes path dependence from functional forgetting. Next
  command: use the corrected theorem conditions to design a constructed
  commutator/locality control before new training. Evidence:
  `../../library/causal-continual-learning-theorem-v1/SOURCE.md`. Completed
  2026-07-25.

- [x] Obtain independent Fable and Sol recommendations for an R9 battery aimed
  at possible ePC advantages beyond perplexity, especially whether internal
  representations are less excessively entangled without merely collapsing.
  Deliverable: preserved prompts/replies and a synthesized, ranked R9 design
  with metrics, matched controls, falsifiers, checkpoint-only probes versus new
  training needs, and a bounded compute ladder. Acceptance: both reviewers see
  the five-seed R8 results plus prior corrected rank evidence and explicitly
  distinguish disentanglement, sparsity/modularity, low rank, robustness, and
  functional benefit. Next command: send the frozen review brief to the prior
  RelaLeap Fable and Sol review sessions. Evidence:
  `docs/reviews/2026-07-21-r9-representation-battery-*`. Completed 2026-07-21:
  both reviews converged on a fail-closed checkpoint audit, rank-matched/
  collapsed BP controls, factor-labelled conditional leakage, causal
  interventions, and mandatory paired functional benefit. Synthesis:
  `docs/reviews/2026-07-21-r9-representation-battery-synthesis.md`.

## Active user commitment — ePC r8 broad outcome battery

- [x] Run a matched-budget CMCP-guided KD/ePC evidence-packet test, approved
  by Ben on 2026-07-25. Deliverable: ordinary KD/ePC, naive multi-view,
  CMCP-weighted, and oracle-deduplicated arms sharing initialization, batches,
  optimizer updates, teacher calls, and evaluation; packet provenance covers
  exact duplicates, deterministic descendants, and independent teacher views.
  Acceptance: typed identity guards and weight fixtures pass; all arms have
  equal update budgets; calibration and disjoint confirmation seeds report
  perplexity, calibration, retention/curriculum reversal, effective precision,
  and ePC energy monotonicity. Next command: implement the local reduced
  CMCP-KD/ePC harness and focused tests. Evidence:
  `experiments/20260725T161000Z-cmcp-epc-kd-bridge/`. Completed as a
  principled calibration stop: three valid 80+80 contradictory-curriculum
  seeds had equal updates/packets and monotone ePC energy. CMCP precision was
  `1.3541` versus naive `4.0` and oracle `2.0`; CMCP improved mean Task-B loss
  over naive (`2.31240` versus `2.33139`) but did not consistently beat
  ordinary KD/ePC on retention or plasticity. Confirmation remains sealed.

- [x] Complete the five-step CMCP/ePC identification repair requested
  2026-07-25. Deliverable: mass-normalized rerun; complementary-teacher
  positive-value fixture; response-versus-gradient novelty calibration with
  frozen disjoint evaluation; ePC ablation; evidence-based E2/E3/CAROM bridge
  audit. Acceptance: every step is preregistered before execution, raw
  artifacts and hashes are retained, focused/full tests pass, code is
  committed, and claims separate observations from inference. Evidence:
  experiments `20260725T222650Z-cmcp-mass-normalized` through
  `20260725T231500Z-cmcp-carom-bridge`. Completed: normalization collapsed the
  arms; complementary evidence gained positive value; response novelty beat
  gradient novelty and nearly matched oracle Task-B loss on disjoint seeds;
  ePC showed a plasticity/retention tradeoff and was dropped from the fast
  calibration loop; CAROM convergence remains an unsupported hypothesis.

- [ ] Implement and run the five-seed ePC r8 robustness/plasticity/
  representation battery requested by Ben on 2026-07-20. Deliverable: r7
  replication plus clean OOD, corruption/perturbation robustness, sequential
  low-rank and full-model adaptation, corrected CKA/rank/anisotropy,
  representation drift, weight geometry, and gradient-alignment results.
  Acceptance: local estimator tests and end-to-end smoke pass; one frozen
  RunPod job record receives an explicit cost bound; all arms/seeds complete;
  artifacts are verified and the pod terminated. Next command: implement the
  r8 trainer/evaluator around the validated GPT-2 pilot and outcome-probe
  components. Evidence: `docs/epc_r8_broad_outcome_protocol.md` and the next
  r8 experiment ledger.

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [x] 2026-07-19: The approved r6 one-seed mechanism screen failed after both
  200-update BP controls and before any ePC arm. The two JSON telemetry records
  were retrieved and hash-verified; no ePC conclusion is authorized. Pod
  `oq7laxlq83hqol` was deleted and RunPod was verified empty. Root cause is
  unknown because the launcher retained only `EXIT_CODE=1`. Evidence:
  `experiments/20260719T202100Z-epc-mechanism-screen-r6/RUN.md`.
- [ ] Diagnose the r6 first-ePC-arm failure without paid compute. Deliverable:
  a focused reproduction or fail-closed launcher regression that preserves
  Python stderr and the real pipeline exit status. Acceptance: the failure is
  explained or deterministically reproduced, focused/full tests pass, and no
  ePC result is inferred from the two BP-only records. Next command: run the
  mechanism-screen ePC arm as the smallest local/synthetic smoke with
  `set -o pipefail` and captured stderr. Evidence:
  `experiments/<run-id>-epc-mechanism-screen-failure-diagnosis/`.

- [ ] 2026-07-19: Execute the Fable/Sol ePC diagnostic ladder before changing
  training hyperparameters. Deliverable: (A1) corrected CKA/rank audit on
  identical WikiText and TinyStories token matrices with random-token OOD
  control; (A2) real-teacher no-update objective/gradient scale audit over
  lambda `{0.005,0.05,0.5,5,50}`; (A3) training-path reconstruction when
  intermediate checkpoints exist; (A4) clipping/Adam instrumentation plan;
  then one frozen seed-3253 GPU screen only if A1/A2 produce a valid selection.
  Acceptance: standard CKA is symmetric, feature-space and Gram formulations
  agree, centered effective rank is reported, D4 self-teacher data are excluded,
  real-teacher component/activity/parameter gradient scales and cosines are
  recorded without optimizer updates, and the GPU protocol is outcome-independent.
  Next command: run the correctness audit locally on the nine preserved
  checkpoints. Evidence: `experiments/20260719T*-epc-correctness-scale-audit/`.
  - [x] A1 corrected CKA/rank audit completed at
    `experiments/20260719T233244Z-epc-correctness-audit-v2/`; first float32
    cross-check failed closed, float64 rerun passed both formulations.
  - [x] A2 real-teacher no-update lambda/depth scale audit completed at
    `experiments/20260719T233948Z-epc-real-teacher-depth-scale-audit/`. Historical
    T4/lambda.05 gives zero gradients to blocks 0-3; high lambda reaches early
    blocks only with poor alignment/nonstationarity. No high lambda selected.
  - [x] A3 endpoint audit: no intermediate model checkpoints exist in the
    preserved Run-2 set, so causal ordering cannot be reconstructed. Freeze
    intermediate checkpoints in the next screen.
  - [ ] A4 clipping/Adam audit: instrument pre/post-clip per-block norms,
    clipped fraction, and Adam second-moment norms in the 200-update screen.
- [x] 2026-07-19 14:00: CPU diagnostic battery on 9 saved checkpoints.
  Acceptance: 5 diagnostics (weight spectral, representation geometry,
  cross-checkpoint CKA, ePC sweep, gradient flow) run on all 9 checkpoints
  with recorded results. Evidence:
  `experiments/20260719T135900Z-gpt2-diagnostic-cpu-battery/` (RUN.md,
  diagnostic_results.json, summary.json). Key findings: ePC representation
  collapse (rank ~1 in L1-L5), layer 5 weight explosion (20-40x), U-shaped
  gradient flow. D4 non-informative (self-reference teacher limitation).
- [ ] Design and run a follow-up GPU experiment only after the Fable/Sol scale
  audit. Do not assume that increasing `lambda_output` or adding hidden-state
  matching repairs the mechanism. Acceptance: one preregistered seed-3253
  200-update screen compares BP+KD, historical ePC, scale-selected current-
  semantics ePC, and normalized-energy ePC from common initialization/batches,
  with checkpoints at 0/10/50/100/200 and the full structural battery.
- [x] 2026-07-19: Deliver an ASCII-only LaTeX/PDF reproducibility and
  scientific-analysis report for the six-layer distillation and full outcome
  battery. Acceptance: source compiles to a readable PDF and reports exact
  frozen inputs, commands, raw per-seed results, bootstrap, structural probes,
  limitations, and artifact hashes. Evidence:
  `docs/relaleap_gpt2_six_layer_outcome_report.{tex,pdf}`; Tectonic compilation
  passed (4 letter pages) and `git diff --check` passed.
- [x] 2026-07-19: The frozen six-layer outcome battery is complete from the
  preserved Run-2 checkpoints, independently of the later r5 distillation-only
  rerun. Acceptance evidence: nine outcome rows, nine structural comparisons,
  adaptation/forgetting curves, paired bootstrap, normal exit, and result hash
  `647ed0dc...f1af` in
  `experiments/20260718T223300Z-epc-outcome-6layer-battery/`. Do not schedule a
  third GPU run merely to reproduce this already-valid artifact.

- [x] 2026-07-19: Run 4 (pod `nkda4fwx4uu5w9`) failed. Both pipeline stages
  crashed: Stage 1 distillation hit an `IndexError` in GPT-2 `lm_head` due to a
  2D/3D tensor squeeze in `_evaluate()`; Stage 2 outcome battery passed relative
  checkpoint paths to `from_pretrained()` which HuggingFace rejected as repo IDs.
  Pod terminated, cron removed, ~$5 cost exposure (mostly idle). See
  `experiments/20260718T155500Z-epc-outcome-6layer-battery/RUN.md`.
  **Required fixes before retry:**
  1. Fix tensor dimension squeeze in `run_gpt2_pilot_gpu.py:_evaluate()`.
  2. Wrap checkpoint paths with `os.path.abspath()` in `run_gpt2_outcome_gpu.py`.
  3. Make Stage 2 conditional on Stage 1 exit code.
  Deliverable: commit the three fixes with regression tests and a recorded local
  smoke run. Acceptance test: focused tests exercise batched GPT-2 evaluation,
  absolute local checkpoint loading, and prove Stage 2 is skipped after a
  synthetic Stage-1 failure; the full local test suite and `git diff --check`
  pass. Next command: patch the runners/launcher and run the focused tests.
  Evidence path: `experiments/20260719T*-gpt2-run4-failure-fixes-smoke/RUN.md`.
  Completed at commit `dc61f31`: focused smoke 17/17; full suite 141/141;
  compilation and diff check passed. Fresh compute remains a separate approval
  gate under `experiments/20260719T153500Z-gpt2-six-layer-r5/REMOTE_JOB.md`.
- [x] 2026-07-19: r5 Runpod **distillation-only rerun** complete (pod
  `oo20lk2075y0dx`, deleted); the requested Stage-2 runner did not execute.
  Three-seed (1729, 3253, 6421) GPT-2 six-layer ePC/BP/KD distillation gate at
  commit `dc61f31`. **Promotion eval FAILED all criteria.** ePC_KD strictly
  worse than BP+KD: update-matched gain −0.52 nats, wall-clock-matched gain
  −1.56 nats. ePC_KD (6.49–6.54) also worse than plain BP+CE (5.25–5.30).
  Positive signal: activity_energy_monotone=true for all ePC_KD runs.
  kd_gap_nats very high (~880–893). Pod ran ~2.6h, terminated promptly.
  Artifacts: `experiments/r5-runpod-20260719/` (13 JSON + summary).
  Experiment record: `experiments/r5-runpod-20260719/EXPERIMENT.md`.
  Monitor cron `efc7eba3` disabled.
  This record must not be cited as outcome-battery completion. Operational
  failure: deployment/monitoring treated Stage-1 termination as job completion
  despite the artifact-level acceptance contract.
  **Open question:** fundamental ePC scaling issue or config/credit problem?
  - 2026-07-17: The initial authorized regions were out of stock. Ben then
    approved expanded regions; A100 pod `lop52u56xugpxk` allocated in Canada
    but remained unready with zero uptime and no SSH for about 52 minutes. It
    was terminated to stop cost exposure before any transfer or execution.
    Blocked pending provider-readiness investigation or a new bounded retry.
    Evidence: `experiments/20260717T155300Z-epc-outcome-6layer-run1/RUN.md`.
  - 2026-07-18 run 2: the three-seed distillation stage completed at pinned
    commit `7d4d4dc`, produced all 12 records and nine verified checkpoints,
    and failed its frozen promotion rule. The pod was terminated after strict
    artifact verification, but before the separately frozen structural and
    WikiText-103-to-TinyStories outcome battery ran. This task was subsequently
    completed by `20260718T223300Z-epc-outcome-6layer-battery`.
    Deliverable: execute `run_gpt2_outcome_gpu.py` once against these exact nine
    retrieved checkpoints and frozen config `gpt2_epc_outcome_6layer.json`.
    Acceptance test: config/source/checkpoint hashes match; nine outcome rows,
    structural probes, adaptation curves, paired bootstrap, exit status, and
    local artifact hashes are present; provider cleanup is verified empty.
    Next command after fresh bounded approval: upload only the pinned source,
    frozen public caches/config, and
    `experiments/20260718T073312Z-epc-outcome-6layer-run2/artifacts/results/checkpoints/`,
    then run `PYTHONPATH=src python3 scripts/run_gpt2_outcome_gpu.py --config
    configs/gpt2_epc_outcome_6layer.json --checkpoints <remote-checkpoints>
    --output <remote-output>/gpt2_epc_outcome_6layer.json --device cuda
    --offline`. Completion evidence path:
    `experiments/<run-id>-epc-outcome-6layer-battery/RUN.md`. Blocker: fresh
    explicit remote-compute approval; do not provision from heartbeat.
- [x] 2026-07-17: Added hash-manifested checkpoint preservation and the
  six-layer scalable outcome runner: pinned WikiText-103 to TinyStories shift,
  identical frozen-backbone low-rank adaptation, adaptation AUC/forgetting,
  CKA, spectral rank, block-skip, corruption, and paired seed/segment
  bootstrap. Commit `7d4d4dc`; 138 full tests, compilation, and diff check pass.
  The twelve-layer configuration is recorded as contingent, not launched.

- [x] 2026-07-17: Ben redirected the ePC evaluation from a perplexity-only gate
  to a subtler network-outcome battery, local first and then scalable. Frozen
  and implemented a common-rule adaptation/forgetting primary endpoint plus
  CKA, effective-rank, block-skip, and corruption probes at clean commit
  `e398876`. The two-seed local instrument pilot reproduced byte-for-byte and
  all 132 tests passed. Its chronological Tiny Shakespeare shift was too weak:
  all arms improved on both domains and CKA was approximately 1. This is an
  instrumentation pass and scientifically inconclusive, not an ePC null.
- [x] Extend the provenance-correct GPT-2 runner to preserve matched BP/KD/ePC
  checkpoints and run the frozen outcome battery. Freeze a genuine domain
  shift, at least three seeds, common adaptation budget, uncertainty analysis,
  and promotion thresholds before requesting fresh bounded RunPod approval.

- [x] 2026-07-16: Frozen a machine-validated GPT-2-small pilot protocol in
  `worktrees/tinyshakespeare-hdpc/configs/gpt2_small_epc_pilot.json` and
  `docs/gpt2_small_epc_pilot_protocol.md`: pinned GPT-2/model/tokenizer and
  WikiText-103 revisions/hashes, six-layer student, primary CE/KD/ePC arms,
  separately labeled hidden-match arm, fixed relaxation schedule, three seeds,
  structured metrics, update- and wall-clock-matched controls, and a pre-run
  promotion rule. Protocol/transformer targeted tests passed 11/11 and the full
  suite passed 113/113. This is implementation/spec evidence, not promotion.
- [ ] Implement the GPT-2/Hugging Face adapter, structured JSON evaluator, and
  two-layer CPU dry-run through the exact pilot arm interface. Record two-run
  determinism excluding declared timing fields before requesting GPU approval.
  - [x] 2026-07-16: Added the lazy fail-closed Hugging Face construction seam,
    structured finite-metric validator, frozen three-seed/two-layer arm runner,
    and two-run comparator at local commit `c310230`. Nine records matched
    outside `elapsed_seconds`; full suite 118/118. This closes the CPU interface
    gate only. Production GPT-2 block-state adaptation and launch runner remain.
  - [x] 2026-07-16: Added the production Hugging Face GPT-2 block-state ePC
    adapter at local commit `0cdc70a`. It matches native GPT-2 logits exactly,
    preserves the exact depth-one KD endpoint, performs monotone four-state
    relaxation with finite earlier-block gradients, and rejects cache/dropout/
    token-shape drift. Targeted tests passed 19/19 and the full suite 121/121.
    The launch/training CLI and structured production evaluator remain open.
  - [x] 2026-07-16: Reviewed and corrected the production GPU runner at local
    commit `e4f2f58`. Wall-clock BP+KD now stops by the measured ePC training
    budget; promotion fails on per-seed regression, missing/duplicate matched
    records, non-finite metrics, or missing credit in any student block. The
    pod script verifies the source marker and pinned public artifact hashes.
    Full suite: 126 passed. Same-runner one-update GPU smoke remains open.
  - [x] 2026-07-16: After the aborted RunPod attempt, reviewed the unaccepted
    post-launch fixes and corrected another blocking control defect at local
    commit `d400c15`: wall-clock BP+KD is no longer capped at the 1,000-update
    control, execution uses only the hash-verified preflight cache, eval chunk
    indices/hashes are emitted, and non-finite control metrics/energy fail
    closed. Targeted tests passed 11/11 and the full suite passed 129/129.
    This is local validation only; a same-commit GPU smoke remains open.
- [ ] Complete the RunPod approval draft with a final clean launch commit,
  immutable image digest, live console price/region, CPU dry-run record, and measured
  runtime estimate; obtain Ben's explicit bounded approval before provisioning.
  - [x] CPU dry-run evidence recorded at
    `experiments/20260716T201500Z-gpt2-pilot-cpu-dry-run/RUN.md`.
  - [ ] Obtain Ben's explicit bounded approval. A concurrent automation run
    incorrectly recorded approval at 17:03 PDT without an approving inbound
    message; this was withdrawn fail-closed at `e4f2f58`.
  - [x] Ben later explicitly approved the old frozen attempt in Telegram
    message 8487. That attempt was aborted and all observed pods were deleted;
    its approval is consumed and does not authorize another attempt.
  - [ ] Prepare a replacement job record pinned to corrected commit `d400c15`,
    immutable image/digest and fresh runtime/cost bounds, then obtain new
    explicit approval before provisioning.

- [x] 2026-07-16: Created interim isolated cron worker `5a517e45-dc8a-4e2d-9d06-b4c3133a1a2c`, scheduled every two hours at minute 15 of odd hours (`America/Vancouver`). It advances the synthetic known-credit ePC gate and is intended to migrate to a task-specific ThreadKeeper persistent agent once that runtime is ready.

- [x] 2026-07-15: implemented and ran the first state-matched local ePC diagnostic gate at commit `941b8b3`. Three seeds, fixed minibatches/teacher logits/evaluation batches, dropout off, identical student initial state, `lambda={0,.001,.01,.05}`, and inference depth `T={1,2,4,8}`. All endpoint/energy/finite-gradient invariants passed, but every genuine `T>1` arm failed to beat matched KD across seeds; promotion failed closed. Evidence: `experiments/20260715T153035Z-epc-distillation-gate-local-r2/RUN.md`, artifact SHA-256 `20ff0c3fd721cf70f10163ba03637ba49770f5acc93bbe8aebbd94e48583e5ab`.
- [x] Diagnosed the v1 failure mechanism and corrected hidden-error normalization
  at commit `cbe4c08`: local credit had been suppressed by approximately
  `seq_len*d_model`. Synthetic invariant tests and the full 110-test suite pass.
  A fresh preregistered v2 on untouched seeds restored substantial earlier-block
  credit but again lost to matched KD; see
  `experiments/20260715T154938Z-epc-distillation-gate-v2/RUN.md` (artifact SHA-256
  `9f5c92a6d7d15a439ad9f6aa596dc5b6ec3676ee30e5b3f77d69e971323a78d8`).
- [ ] Run the synthetic known-credit benchmark as a nonblocking diagnostic for
  the GPT-2 pilot; do not use it to override the preregistered corpus gate.

- [x] 2026-07-09: Created isolated HDPC/ePC Tiny Shakespeare worktree `projects/relaleap/worktrees/tinyshakespeare-hdpc` on branch `agent/tinyshakespeare-hdpc` from `projects/relaleap/repos/relaleap` branch `agent/train-time-causal-slice1` commit `622ede2`.
- [x] 2026-07-09: Implemented local CPU-first toy HDPC/ePC scaffold under `src/relaleap/hdpc/`: explicit MLP PC energy, local error-based activity relaxation with monotonic backtracking, BP endpoint, detached teacher/KD anchor, PC endpoint distinctness, identity-initialized crown, and static-PC/ePC state-gradient equivalence. Verification: targeted `9 passed`; full suite `102 passed`; `git diff --check` clean. Transformer/Tiny Shakespeare adaptation remains the next task.

## Afterwards / upgrades

- [ ] Add SLT inputs to the HDPC/ePC process after the Tiny Shakespeare HDPC prototype is technically viable.
- [ ] Add columnar models for the residual layer after the baseline PC-crown mechanism is working and measurable.
- [ ] Wave 2: Run real SGLD/WBIC sampler against analytic calibration benchmarks (regular linear, rank-deficient, product singularity, composition) and fix scaling/sampler bugs. Produce executable validation reports rather than mock/pass-through targets.
- [ ] Wave 3: Sample-size sweeps (n = {256,512,1024,2048,4096,8192}), slope fitting, block-wise and joint Iλ protocols, shared-core-conditioned and full-adapter projected checks, prior-sensitivity sweeps.
- [ ] Wave 4: RelaLeap-shaped validation — run all 7 regime benchmarks with real sampler, confirm expected winners and interaction signs.
- [ ] Implement remaining mandatory SLT-estimation validity contract: actual trainable parameter-block masks, module-vs-joint estimates, null-normalized uncertainty, minibatch/preconditioning diagnostics.
- [ ] Validate all SLT estimators on a Tiny Shakespeare level corpus before using SLT evidence for scientific promotion or SLT-guided residual-layer claims.

## Next

- [ ] Update `docs/slt_estimation_validation_checklist.md` to incorporate the sharper 2026-07-04 plan, especially total-energy vs mean-loss WBIC convention, negative-lambda policy, sample-size slope fitting, exact Gaussian posterior validation, and gauge policy.
- [ ] Add frozen-tail abstraction beyond the current linear test suffix.
- [ ] Add train/validation/test cache manifests and command manifests for larger reproducible runs.

## Waiting or blocked

- [ ] MacBook-side prior RelaLeap worktree cleanup remains unresolved if Mac execution is needed: uncommitted `docs/relaleap_summary.{tex,pdf}` caused prior loop skips.

## Someday or exploratory

- [ ] Real transformer residual-cache validation after synthetic gates pass.
- [ ] GPU validation only after fail-closed synthetic and causal audit gates pass locally.
- [ ] Refinement-DAG controller for broader factorization search after the minimal train-time learner is stable.

## Done recently

- [x] Run the preregistered local CMCP-guided ePC continual-learning Phase 1
  experiment. Deliverable: five arms, three seeds, 2,000 student updates,
  frozen CL/representation/robustness battery, raw JSON and checkpoints.
  Acceptance test: `command.sh` exits zero; all 15 arm/seed records are finite,
  KD-bearing arms report mass 1.0, ePC traces are monotone, and `RUN.md` records
  observations and the frozen promotion decision. Next command:
  `experiments/20260725T231807Z-cmcp-epc-cl-phase1/command.sh`. Evidence path:
  `experiments/20260725T231807Z-cmcp-epc-cl-phase1/`. Result: 15/15 records,
  exit 0, all mass/monotonicity invariants passed, but the Phase-2 gate was
  false. CMCP-ePC improved plasticity over ePC but worsened forgetting in every
  seed and did not beat CMCP-KD on any functional CL endpoint.

- [x] 2026-07-25: Implemented CMCP typed-protocol Phases 7 and 8 on
  `agent/e1-guarded-homotopy`: five-arm mechanism-indexed credit-highway
  comparison with Eq. 47 transport and forward-isolated credit-only routing,
  plus disjoint-seed sealed confirmation, frozen acceptance gates, required
  artifact hashing, and stop conditions. Deliverable: two implementation
  modules and 24 tests. Acceptance test:
  `/home/openclaw/research-agent/projects/relaleap/repos/relaleap/.venv/bin/python
  -m pytest tests/ -q`; result `412 passed, 1 skipped`. Evidence:
  commit `cad8d9a`;
  `experiments/20260725T095107Z-cmcp-phase7-8-full-suite-venv/RUN.md`.
- [x] 2026-07-24: Implemented Schweizer-Sklar quantale-weak CMCP accounting,
  constructed-fixture calibration, and a provenance-unprotected biased
  injection runner. Calibration selected `p=0.05`
  (exact/biased/independent/partial means
  `0.0/0.0/0.8709297/0.3630205`); seed-61001 biased smoke gave ratio `0.0`
  with distinct innovation IDs. Focused tests: 9 passed; existing CMCP/store
  compatibility tests: 12 passed. Evidence:
  `experiments/20260725T033949Z-e4-quantale-focused-verification/`.
- [x] 2026-07-14: Added a CPU-friendly SGLD step-size diagnostic sweep, diagonal gradient-variance preconditioner, focused quadratic tests, and production decision gate. Verification: 4 focused tests and 97 full-suite tests passed; experiment records `20260714T182809Z-sgld-step-size-sweep-targeted` and `20260714T182834Z-sgld-step-size-sweep-full-suite`.
- [x] 2026-07-10: Wrote `docs/slt_tiny_shakespeare_transformer_analysis.tex` and compiled `.pdf`, an ASCII-only conceptual report interpreting the Tiny Shakespeare transformer SLT validation runs for readers not already fluent in SLT.
- [x] 2026-07-09: Added the first HDPC/ePC invariant slice in worktree `tinyshakespeare-hdpc` (uncommitted, local only): `src/relaleap/hdpc/{mlp,crown}.py` and `tests/test_hdpc_scaffold.py`; no paid/remote compute and no push.
- [x] 2026-07-07: Wave 1 implementation complete. 6 parallel subagents merged into `agent/train-time-causal-slice1` (commit `622ede2`): SGLD/WBIC core (A), analytic calibration registry with 7 benchmark families (B), MAP/prior refinement (D), RelaLeap-shaped benchmarks with 7 regimes (G), null distributions with 8 null types (H), CI gates and decision reports (J). 93 tests pass. 5004 lines across 21 source modules and 30 test files.
- [x] 2026-07-07: Integrated first-wave SLT estimator branches into local worktree `worktrees/slt-integration` on branch `agent/slt-integration` at commit `6dca8eb`; merged SGLD/WBIC core, analytic calibration registry, prior/MAP sensitivity, RelaLeap-shaped benchmarks, and adversarial review. Verification: `PYTHONPATH=src python3 -m pytest tests/ -q` => 66 passed, 7 xfailed; `git diff --check` clean.
- [x] 2026-07-04: Preserved Ben's uploaded `Validation of SLT Parameter Estimation for RelaLeap` PDF/text in project docs and library, and added `docs/slt_estimator_validation_plan_summary.md` as the current implementation-planning pointer.
- [x] 2026-07-03: Wrote `docs/slt_estimator_implementation_guide.tex` and compiled `docs/slt_estimator_implementation_guide.pdf`, an ASCII-only LaTeX guide explaining what is involved in implementing trustworthy finite-sample WBIC/SGLD/RLCT proxy estimators.
- [x] 2026-07-03: Implemented first coding slice in local repo `repos/relaleap` on branch `agent/train-time-causal-slice1`: synthetic generators for all six regimes, identity-initialized rank-one learner, flat/SVD controls, exact ablation auditor, dependency contracts/null specs, event log, fail-closed report, and unit tests.
- [x] 2026-07-03: Added a code-level guardrail that `scientific_status=pass` requires calibrated finite-sample SLT evidence fields over actual parameter blocks.
- [x] 2026-07-03: Created local `projects/relaleap/` project notebook.
- [x] 2026-07-03: Preregistered new train-time causal factor learner design at `docs/train_time_causal_factor_preregistration.md`.
- [x] 2026-07-26: Repair the co-learned causal critic Phase-0 protocol and
  add a trainable planted learner fixture. Deliverable: v2 preregistration,
  three-module trainable fixture, real decision features, paired restoration,
  four-family effect tests, and policy diagnostics. Acceptance test:
  `PYTHONPATH=src:. .../.venv/bin/python -m pytest tests/ -q`; result:
  `459 passed, 1 skipped`. Evidence: branch
  `agent/colearned-causal-critic-v1`; protocol
  `docs/colearned_global_causal_critic_protocol_v2.md`. This is infrastructure
  evidence only; no v2 confirmation or policy efficacy claim has been run.
- [x] 2026-07-26: Run the frozen co-learned causal critic v2 Phase-0
  confirmation. Deliverable: trainable paired-rollout confirmation with
  two-part ensemble, calibration-only isotonic mapping, all seven estimation
  gates, raw evidence, and fail-closed decision. Acceptance test: focused and
  full pytest suites pass and experiment
  `experiments/20260726T130602Z-colearned-causal-critic-v2-phase0/` is
  complete. Result: estimation failed fail-closed; policy gates blocked.
  Full verification: 461 passed, 1 skipped. Evidence:
  `experiments/20260726T130602Z-colearned-causal-critic-v2-phase0/`.
- [x] 2026-07-26: Implement and execute the co-learned causal critic v3
  pre-confirmation trajectory audit. Deliverable: versioned stronger fixture,
  augmented decision-time features, standardized hurdle amounts, 10x training
  configuration, and five-checkpoint audit before calibration/confirmation.
  Acceptance: v3 audit passes every family and keeps null/harmful below 5%
  positive utility, else stop before confirmation. Result: stopped fail-closed:
  all four families lost their declared ordering at checkpoint 99/100;
  null/harmful's positive rate was 0% but it also lost ordering. No calibration,
  confirmation, policy, or Shakespeare phase ran. Full verification: 463
  passed, 1 skipped. Evidence:
  `worktrees/colearned-causal-critic-v1/experiments/20260726T184000Z-colearned-causal-critic-v3-preconfirmation-audit/`.
