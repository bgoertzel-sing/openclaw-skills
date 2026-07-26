# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [ ] Execute the approved GPT-2 piecewise-vs-OneCycle schedule experiment.
  Deliverable: two complete 12,000-update arms with frozen evaluations and
  checkpoints, hash-verified retrieved artifacts, gate disposition, and
  confirmed RunPod termination. Acceptance: local runner tests pass; remote
  manifest verifies; no task pod remains; `RUN.md` separates observation,
  inference, and hypothesis. Next command: provision the approved H100 SXM
  with a four-hour provider termination deadline. First attempt stopped after
  12.8 minutes: the runner used absolute LRs as `LambdaLR` multipliers, making
  the actual peak 500× too small, and evaluated every 500 rather than 1000
  updates. Partial artifacts verified 13/13 and pod inventory is empty. Next
  command: add optimizer-level realized-LR and cadence regression tests,
  correct the runner, and freeze a new commit for explicit rerun approval.
  Evidence: `experiments/20260726T100000Z-gpt2-piecewise-schedule/`.

- [x] Complete local checkpoint forensics for the 12k compiled-channel
  collapse. Deliverable: repaired-instrument evaluation of all 13 preserved
  checkpoints, raw JSON, weight/gradient/representation timelines,
  correlations, and a mechanism/schedule disposition. Acceptance: every
  checkpoint validates; deterministic CPU analysis exits zero; report
  separates observation, inference, and hypothesis. Next command:
  `bash experiments/20260726T-forensics-12k-collapse/command.sh`. Evidence:
  `experiments/20260726T-forensics-12k-collapse/`. Result: collapse localized
  to `(3000, 4000]` at peak LR; broad core growth leads it, a raw-gradient
  crisis coincides with it, hyper routing then becomes low-rank/starved, and
  edge AUPRC improves despite itinerary failure. Schedule surgery prevents
  the acute collapse but structural gain control remains indicated.

- [x] Run the preregistered GPT-2 low-peak schedule diagnostic after explicit
  approval of its concrete RunPod proposal. Deliverable: step-3000 warm start
  (explicit optimizer/scheduler reset) plus matched-shape fresh low-peak
  control, frozen validation corpora, checkpoint-complete L2--4/L5/edge/
  itinerary traces, hash-verified retrieval, termination, and inventory
  recheck. Acceptance: operational and stability gates in the run ledger pass
  within 2 hours/USD 6. Next command: await approval, then recheck H100 price
  and region before provisioning. Completed on H100 within approximately
  1.58 hours/USD 4.72. Stability passed: warm final L2--4 0.3529, tau 0.8398,
  coverage 0.6921; no collapse. Promotion failed: L2--4 below 0.45 and L5
  0.2396 below 0.25. Fresh low-peak control was stable but underpowered at
  0.2122 L2--4. Retrieved hashes matched and the pod was deleted. Evidence:
  `experiments/20260726T000748Z-gpt2-schedule-diagnostic/`.

- [x] Repair compiled-channel v2/v3 instruments and constructed controls.
  Deliverable: revisit-preserving order/transition metrics, tie-correct edges,
  explicit span adapters, CPU corpora, dominance/unclassified state,
  mutation-safe sweeps, locally seeded probes, natural switching baseline,
  device/zero-safe coupling, live decisiveness, portable loading, and
  non-categorical reports. Acceptance: constructed controls pass before
  checkpoint interpretation. Result: 19 local tests pass; GPU-device
  operational preflight remains part of the first approved remote run.
  Evidence:
  `experiments/20260726T003000Z-compiled-channel-instrument-repair/`.

- [ ] Run the GPT-2 multi-seed compiled-channel confirmation. Blocked until
  a separate exact paid-compute proposal is approved. Step-2 stability passed,
  but its low-peak schedule is licensed only for warm starts; a fresh schedule
  needs calibration. Protocol and numerical gates are frozen in
  `docs/compiled-channel/gpt2-multiseed-protocol-2026-07-26.md`.

- [ ] Independently validate the v6 controller peak-LR guard. Local historical
  replay selects the held-out oracle at both v5 checkpoints, but this is
  post-hoc and not an activation result. Acceptance requires new common-random
  continuations spanning rising, peak, falling, and tail LR regimes. Evidence:
  `docs/gpt2-controller-v6-peak-guard-2026-07-26.md`.

- [x] Compile and equivalence-gate the CAROM E2/E3 70-step recurrence, then
  relaunch under a fresh bounded GPU approval, requested by Ben on 2026-07-25.
  Deliverable: optional whole-graph compilation without changing recurrent
  semantics; eager/compiled forward, activity, gradient, optimizer-step,
  seeded-noise, and deterministic-evaluation checks; separate compile and
  steady-state timing; full-shape cost estimate; retrieved/hash-verified GPU
  results and terminated resource. Acceptance: local equivalence and existing
  E0--E3 tests pass, measured speedup supports the approved bound, and the
  original five-seed gates remain unchanged. Next command: implement the
  optional compiler seam and focused equivalence harness. Evidence:
  `experiments/20260725T173639Z-e2-e3-compiled-recurrence-v1/`.
  Local implementation commit `4d24f77`: all 33 CAROM tests and a five-arm
  smoke pass. The full-width CPU Inductor probe gives 2.37x steady-state
  speedup with maximum post-AdamW parameter error `3.86e-6`; the bounded H100
  CUDA calibration/campaign proposal awaits explicit approval in
  `REMOTE_JOB.md`.
  The completion campaign produced all 25 arm/seeds. Example-level aggregation
  verifies the reported means. E2 full passed all three prospective paired
  feature gates; E3 failed the safety/trajectory gate because its mean slot
  accuracy loss was 0.02725 (limit 0.010) and terminal trapping increased by
  0.00332. The joint gate failed and E4 remains closed. Aggregator and
  regression tests: `aggregate_e2_e3.py`, `test_aggregate_e2_e3.py`.

- [x] Correct and rerun the GPT-2 active-controller gate (v5), approved by Ben
  on 2026-07-25. Deliverable: nonterminal checkpoints, controller-selected
  LR applied to explicit state-restored continuations, common future batches
  for active/passive/oracle arms, exact parent immutability, and paired
  loss/accuracy outcomes. Acceptance: constructed action-selection tests and
  local smoke pass; remote job remains within 2 hours/USD 3; artifacts are
  retrieved and hash-verified; pod is terminated. Next command: implement and
  test `run_carom_gpt2_controller_v5.py`. Evidence:
  `experiments/20260725T161000Z-gpt2-controller-v5-active/`.
  Completed on an A100 in 40.11 minutes. Action sensitivity and oracle
  headroom passed, but controller utility and selection failed: the selector
  was harmful at update 600 and matched the oracle at update 1200. Artifacts
  were hash-verified and the pod was terminated.

- [x] Complete the accepted Fable/Sol E2/E3 ladder. Deliverable:
  deterministic five-seed mode-specific fitness ablations and generic
  direction-free regularization on the frozen corpus. Acceptance: full-scale
  paired accuracy and trajectory gates pass without successor-pair encoding or
  excess exposure; only then open E4. Next command: reduce or freshly
  authorize the full-run resource requirement. Evidence:
  `experiments/20260724T182939Z-e2-e3-cpu-smoke-r1/` and
  `experiments/20260724T183038Z-e2-e3-cpu-fixture-r1/`. Implementation and
  seven tests pass; smoke and fixture are deterministic. Fixture cost was
  74.23 s and 375 MB RSS. Full-shape local calibrations on 2026-07-25 measured
  3:26.47 for 50 arm-updates (7.80 GB peak RSS), projecting about 86 CPU-hours
  for the frozen 75,000 updates before full evaluation. Eight focused E0/E1
  plus E2/E3 tests pass. No remote resource was provisioned or used. The
  preregistration describes joint scientific selection qualitatively but does
  not freeze numerical paired accuracy, trajectory, or excess-exposure
  thresholds; therefore a run cannot honestly be called a preregistered gate
  pass yet. Next command: freeze those numerical gates, then execute the
  existing five-seed GPU runner under a separately authorized paid-compute
  action (or explicitly accept the approximately 86-hour local projection).
  Evidence:
  `experiments/20260725T094800Z-e2-e3-full-cpu-feasibility-r1/` and
  `experiments/20260725T095240Z-e2-e3-full-cpu-train-rate-r1/`. This remains
  calibration, not a scientific disposition; E4 remains closed.
  GPU feasibility was subsequently measured under Ben's USD 10 approval:
  A40 exceeded 17.5 minutes and H100 exceeded 10.8 minutes without completing
  the first of 25 arms. The H100 lower-bound projects beyond 4.5 hours /
  USD 13.45. Partial logs were retrieved and all E2/E3 pods terminated; no
  scientific result exists. Next command: validate a compiled/vectorized
  70-step recurrence against exact eager outputs and determinism before
  requesting another full campaign.
  Completed by the compiled recurrence campaign. E2 passed; E3 and the joint
  promotion gate failed under thresholds prospectively frozen before r2.
  E4 stays closed. Evidence:
  `experiments/20260725T173639Z-e2-e3-compiled-recurrence-v1/`.

- [x] Run the GPT-2-scale CAROM distributional controller utility gate
  requested by Ben on 2026-07-24. Deliverable: frozen-GPT-2-small
  compiled-channel warm-start trajectory with complete optimizer/RNG
  checkpoints and disjoint calibration/held-out LR-action branches.
  Acceptance: local smoke and constructed action/oracle tests pass; explicit
  RunPod cost approval is recorded; parent states remain immutable; replay is
  exact; paired informed-versus-passive loss/accuracy and uncertainty are
  reported; artifacts are retrieved/hash-verified; pod is terminated and
  inventory rechecked. Next command: finish and CPU-smoke the v4 runner, then
  provision only after approval of the 2-hour/USD 3.00 cap. Evidence:
  `experiments/20260724T082409Z-gpt2-distributional-controller-v4/`.
  The 2026-07-25 v4 rerun repaired the terminal-scheduler crash but is not a
  valid active-control utility result: it never applies a selected action to
  the parent trajectory, and its final gate occurs at the OneCycleLR zero-LR
  endpoint. Next command: implement a state-restored, common-random-number
  continuation comparison in which the selected scale affects the actual
  continuation and all gates precede the terminal LR region. Evidence:
  `experiments/20260725T095200Z-gpt2-controller-v4-rerun/RUN.md`.
  Superseded and completed by the corrected v5 active-continuation gate above;
  the valid result is negative overall controller utility.

- [x] Build and execute CAROM Frozen-State Replica Calibration v1, requested
  by Ben on 2026-07-22. Deliverable: a deterministic CPU experiment that
  captures complete model/AdamW/OneCycle/RNG states at updates 150, 450, 900,
  1350, and 1499; performs same-state one-step replicas across batch and
  paired-LR conditions; compares AR(1), AR(2), frozen-v companion AdamW, and
  v-aware transition predictors on short replicated trajectories; and
  estimates repeatable Adam-preconditioned top curvature by multi-start power
  iteration. Acceptance: reduced smoke proves parent-state immutability,
  exact replay, common-random LR pairing, raw/clipped gradient and
  delta-theta/m/v capture, finite machine-readable output, and deterministic
  hashes; the full local run records exact commands, resources, results, and
  go/no-go gates in an experiment ledger. Next command: implement
  `repos/carom/run_carom_frozen_replica_calibration.py` and its focused tests.
  Evidence: `experiments/20260723T*-frozen-state-replica-calibration-v1/`.
  Completed 2026-07-23: all operational invariants passed. Innovation Models
  1--3 passed calibration (frozen-preconditioner median ratio `1.0144`; full
  one-step `1.0000`), while scalar Model 0 failed (`4.0726`). The augmented
  v-aware state model failed (`1.0235x` vs required `>=2x`) and curvature
  repeatability failed (max CV `0.7374`, 90% width `1.4277`). Evidence:
  `experiments/20260723T181323Z-frozen-state-replica-calibration-v1/`.

- [x] Build and execute CAROM stochastic-transition identification v2.
  Deliverable: a frozen-checkpoint experiment that uses the v1-calibrated
  AdamW-preconditioned innovation model but compares AR(2), explicit AdamW,
  time-varying/local-linear, and a preregistered nonlinear empirical state
  representation over disjoint checkpoint/LR/batch interventions; estimate
  curvature as a batch-conditioned distribution with uncertainty rather than a
  controller point estimate. Acceptance: exact branch replay and parent
  immutability; held-out 8-step state prediction reduces error at least 2x
  relative to AR(1); the winning state representation transfers across at
  least one withheld LR/batch condition; sharpness uncertainty is quantified
  rather than silently averaged; no active controller mutation occurs. Next
  command: write the v2 plain-language state contract, then construct
  time-varying and nonlinear positive controls before implementing the runner.
  Evidence: `experiments/<run-id>-stochastic-transition-id-v2/`.
  Completed 2026-07-23: all distributional, mean-dynamics, oracle-gap, and
  operational gates passed across five frozen checkpoints. Median random/PCA
  coverage ratios were `0.9877/1.0532`; mean RMSE versus AR(1) `0.9922`;
  oracle/distributional ratio `0.00472`; AdamW/calibration RMSE ratio `1.2777`.
  This attributes the v1 deterministic failure primarily to irreducible future
  minibatch uncertainty, rather than state insufficiency. Active control is
  still shadow-only pending a separately tested distributional activation gate.
  Evidence: `experiments/20260723T224500Z-stochastic-transition-id-v2/`.

- [x] Produce the requested exact-parameter BridgeLearn shadow-mode v2 PDF.
  Deliverable: ASCII-only LaTeX and compiled PDF documenting the precise
  CAROM/BridgeLearn configuration, command, environment, all 1,500-observation
  telemetry fields and aggregate results, calibration gates, interpretation,
  limitations, and parameter-tuning implications. Acceptance: every numerical
  claim traces to the hash-verified telemetry; Tectonic compilation, PDF text
  extraction, all-page visual inspection, ASCII validation, and artifact
  hashes pass. Next command: generate the report tables from
  `experiments/20260722T200000Z-bridgelearn-shadow-mode-v2/telemetry.json`.
  Evidence: `docs/carom_bridgelearn_shadow_v2_report_2026-07-22.{tex,pdf}`.
  Completed 2026-07-22: the eight-page report traces all numerical claims to
  the hash-verified 1,500-row telemetry, records every model/optimizer/
  scheduler/observer/planner parameter, and distinguishes scalar tuning from
  innovation/state-model misspecification. Tectonic compilation, ASCII source
  validation, PDF text extraction, and visual inspection of all eight pages
  passed.

- [x] Run the matched-cadence BridgeLearn shadow calibration gate.
  Deliverable: 1,500 per-update transition observations, split-batch noise
  measurements, HVP sharpness probes, AR(2) diagnostics, and LR non-mutation
  assertions. Acceptance: exit zero, all shadow invariants pass, telemetry and
  hashes verify, and observer adequacy is explicitly assessed before active
  control. Completed 2026-07-22: all 1,500 invariants passed and variance
  tracking calibrated closely, but innovation, sharpness confidence, and
  AR(1) adequacy failed the activation gate. Next command: implement a
  shadow-only companion/momentum adapter with replicated same-parameter
  stochastic transitions and multi-probe or power-iteration sharpness.
  Evidence:
  `experiments/20260722T200000Z-bridgelearn-shadow-mode-v2/`.

- [x] Build and run the BridgeLearn v0.3.0 shadow-mode integration for the
  scheduled CAROM variant. Deliverable: CPU-runnable
  `repos/carom/run_carom_bridge_shadow.py`, JSON telemetry containing
  OneCycleLR and BridgeController transition/calibration/sharpness diagnostics,
  and experiment record
  `experiments/20260722T190000Z-bridgelearn-shadow-mode/RUN.md`. Acceptance:
  a 1,500-step seed-0 scheduled run exits zero without BridgeLearn changing
  optimizer or scheduler state, and the telemetry parses with nonempty shadow
  observations. Completed 2026-07-22: the 1,500-step run exited zero with 11
  observations and the LR non-mutation invariant held. The largest contraction
  discrepancy (0.338) and variance calibration error (0.111) occurred near the
  LR peak, but cadence mismatch makes this diagnostic rather than causal
  evidence. Next command: match prediction and realization at every optimizer
  update and validate the sharpness/AR(2) observers. Evidence:
  `experiments/20260722T190000Z-bridgelearn-shadow-mode/`.

- [x] Complete the CAROM frozen-GPT-2 12k run, detailed results PDF, and two
  independent parameter reviews requested 2026-07-22. Deliverable: retrieved
  and hash-verified 13-checkpoint run artifacts; terminated CAROM pod; detailed
  comparative PDF covering optimization dynamics, interventions, L5 behavior,
  failure analysis, limitations, and reproducibility; independent Fable and
  Sol reviews grounded in that PDF; and a synthesized, testable next-parameter
  ladder. Acceptance: run exit/result status and cost recorded; every PDF value
  traces to raw JSON/logs; PDF text extraction and all-page visual inspection
  pass; both reviews are preserved verbatim; synthesis distinguishes agreement,
  disagreement, and proposed discriminating experiments. Next command: inspect
  pod `wsllxvsshf7jf1`, retrieve/verify outputs on completion, and terminate it.
  Completed 2026-07-22. The run artifacts were retrieved and verified, the pod
  was terminated, the five-page PDF passed text extraction and all-page visual
  inspection, and Fable and Sol independently reviewed it. Their synthesis
  corrects the edge-accuracy interpretation, identifies shared-RNG/cadence
  confounding, and specifies a checkpoint-forensics -> low-LR warm start ->
  matched fresh-schedule ladder. Evidence:
  `experiments/20260722T015200Z-carom-gpt2-12k/`,
  `docs/carom_gpt2_12k_detailed_results_2026-07-22.pdf`, and
  `docs/reviews/2026-07-22-carom-gpt2-12k-*`.

- [x] Produce a detailed PDF report for the completed frozen-GPT-2 compiled
  channel arm and freeze a higher-accuracy rerun protocol. Deliverable: report
  with exact model/task/training/evaluation description, checkpoint tables,
  TinyLM context, causal and budget-sweep interpretation, limitations, and a
  bounded rerun proposal. Acceptance: every reported number traces to the
  hash-verified JSON; PDF text extraction and page rendering are checked;
  rerun has an exact command, acceptance rule, A100 time/cost cap, artifact
  path, and cleanup plan before approval is requested. Next command: generate
  tables/plots from the two retained summaries and render the report. Evidence:
  `experiments/20260721T222400Z-carom-gpt2-arm/` and forthcoming rerun ledger.
  Completed 2026-07-21. The five-page PDF and TeX source passed clean Tectonic
  rendering, five-page text extraction, visual inspection of every page, and
  `git diff --check`. Evidence:
  `docs/carom_gpt2_compiled_channel_report_2026-07-21.{pdf,tex}` and
  `experiments/20260722T015200Z-carom-gpt2-12k/`.

- [x] Run the preregistered 12,000-update frozen-GPT-2 accuracy extension after
  explicit bounded approval. Deliverable: 13 checkpoint panels, final accuracy
  and mechanism/extrapolation comparison against the 4,000-step arm, retrieved
  checkpoints/results/logs with SHA-256 manifest, and terminated pod.
  Acceptance: exact frozen protocol in the ledger; primary target L2--4 >0.55,
  strong target >=0.65; three-hour/USD 4.47 hard cap; provider inventory empty
  for this job after cleanup. Next command after approval: provision one Secure
  Cloud A100 SXM4 80GB using the recorded template and auto-terminate deadline.
  Evidence: `experiments/20260722T015200Z-carom-gpt2-12k/`.
  Completed 2026-07-22. Training and all 13 intervention panels completed; the
  >0.55 target failed (best 0.3268 at step 3,000; final 0.1888). The 31-file
  manifest verified and pod `wsllxvsshf7jf1` was terminated.

- [ ] Repair and validate Ben's supplied Oruzi-derived v3 intervention probes.
  Deliverable: pluggable TinyLM/GPT-2 span adapter; locally seeded JVP and
  perturbation probes; matched natural switching baseline; device-safe,
  zero-safe cross-slot effects; live-mode decisiveness metrics; portable
  checkpoint loading; and non-categorical reporting language. Acceptance:
  constructed commuting/noncommuting, stable/unstable-word, zero-coupling,
  padded-mode, CPU/GPU-device, and repeatability controls pass before any
  scientific interpretation. Next command: implement fixtures around the six
  probe families without changing the active training jobs. Evidence:
  `docs/compiled-channel/harness_v3_probes_audit_2026-07-21.md`.
  Theory/bench rationale and immediate-run ordering are preserved at
  `../../library/carom-oruzi-reconciliation-2026/SOURCE.md`; do not adopt its
  categorical smoke interpretations until these acceptance controls pass.

- [ ] Repair and validate the supplied Exp2/Exp3 v2 harness before using its
  metrics. Deliverable: tie-correct edge metrics, revisit-sensitive itinerary
  metrics, explicit smeared/unclassified diagnostics, pluggable TinyLM/GPT-2
  span extraction, CPU-canonical frozen corpora, and regression tests.
  Acceptance: supplied tests plus all-tied AUROC=0.5, revisit-not-exact,
  smeared-not-itinerary, TinyLM/GPT-2 adapter contract, and device round-trip
  fixtures pass. Next command: create an isolated CAROM branch/worktree and
  implement the metric fixtures first. Evidence:
  `docs/compiled-channel/harness_v2_audit_2026-07-21.md` and
  `../../library/carom-exp2-exp3-audit-response-2026/SOURCE.md`.

- [ ] After harness repair, re-evaluate retained Exp2 checkpoints on one frozen
  paired corpus. Deliverable: checkpoint-wise itinerary drift curves,
  forced-correct/shuffled/smeared/natural endpoint results, and an L=5
  integration-depth sweep including `S=72,100,120` (with a wider curve if the
  endpoint has not stabilized). Acceptance: identical examples across
  checkpoints/conditions; exposure and workspace-update norms reported;
  conclusions distinguish metric failure, decorative control, load-bearing
  itinerancy, and time-budget limitation. Next command: inventory and hash the
  retained Exp2 model and TinyLM checkpoints. Evidence: forthcoming experiment
  ledger; source rationale in
  `../../library/carom-exp2-exp3-audit-response-2026/SOURCE.md`.

- [x] Audit Ben's supplied `harness_v2.py` against the CAROM Exp2/Exp3
  implementations and Priority-0 instrument requirements. Deliverable: a
  preserved source copy plus a review of correctness, compatibility, and
  required repairs. Acceptance: source hash recorded; Python syntax/self-tests
  checked; itinerary, edge, intervention, budget-sweep, and paired-M2 logic
  inspected against the actual model APIs; findings recorded with an evidence
  path. Completed 2026-07-21. The supplied self-tests pass, but additional
  counterexamples establish revisit-erasure, tie-biased AUROC, and GPT-2 span
  incompatibility; do not use unchanged for claims. Evidence:
  `docs/compiled-channel/harness_v2_audit_2026-07-21.md`. Next command: repair
  these failures and add regression tests before checkpoint evaluation.

- [x] Produce the detailed Exp2/Exp3 experiment-and-results report requested
  2026-07-21. Deliverable: durable Markdown and rendered PDF covering questions,
  implementations, protocols, complete logged metrics, learning dynamics,
  interpretation, alternative explanations, limitations, and next experiments.
  Acceptance: values trace to hash-verified raw logs; unpaired and missing-control
  caveats are explicit; Markdown renders to PDF; `git diff --check` passes.
  Completed 2026-07-21. Evidence: `docs/carom_exp2_exp3_detailed_summary.md`,
  `.html`, and `.pdf`; nine-page PDF text extraction checked; source/log hashes
  and `git diff --check` verified.

- [x] Obtain independent Fable and Sol experiment-design reviews aimed at
  closing the learned free-inhibition heteroclinic accuracy gap to the
  hand-engineered chain. Deliverable: two preserved reviews and a synthesized,
  testable next-experiment ladder. Acceptance: both reviewers receive the GPU
  report plus the original CAROM sandbox and itinerant-theory papers; replies
  identify mechanisms, ablations, metrics, and go/no-go criteria. Next command:
  launch isolated Fable and Sol review sessions with the three PDFs and frozen
  result summary. Evidence: `docs/reviews/2026-07-20-*`. Completed 2026-07-20;
  both reviews converge on instrument repair, exposure normalization, and
  mode-specific fitness before generic direction-free channel regularization.

- [x] Implement and audit the E0/E1 exposure-controlled CAROM experiment.
  Deliverable:
  fixed paired evaluation, separated RNGs, trajectory/exposure diagnostics,
  normalized activity mixing, and fixed-versus-free trajectory replay.
  Acceptance: at least five seeds; accuracy and mechanism metrics with paired
  intervals; a causal determination of whether the fixed/free gap survives
  matched activity mass, command exposure, and workspace-update norm. Next
  command: after Ben approves the frozen USD 10.43 / 7-hour bound, provision
  one A100 SXM 80GB Secure Cloud pod and launch `command.sh`. Evidence:
  `experiments/20260720T140710Z-e0-e1-exposure-controlled-r1/`. Completed
  2026-07-24: all 20 trainings and 40,960 rows audited. Raw fixed-minus-free
  was `+0.06956` (95% CI `[+0.00438,+0.13610]`); normalization worsened free
  by `-0.29193`. The deterministic gate failed because evaluation randomized
  initial activity, so retain the pattern only as exploratory evidence.

- [ ] Prepare the one-off RunPod experiment. Deliverable: preserved source and
  figures, local smoke evidence, preregistered remote job record, and bounded
  resource proposal. Acceptance: generator and all variants execute locally;
  job record specifies exact commands, metrics, artifact path, resource,
  price, time/cost cap, and teardown. Next command: run the local smoke ledger.
  Evidence: `experiments/*-local-smoke/` and `experiments/*-runpod-gpu/`.
  Status: approved by Ben up to USD 10 on 2026-07-19. The temporary sequencing
  block cleared at 23:10 PDT when the failed RelaLeap ePC pod's partial
  artifacts were retrieved and the pod was deleted. The next command is to
  freeze the GPU runner/protocol and its remote-job record; this commitment is
  mirrored in `catalog/KANBAN.md`.

## Next

- [ ] Harden and run the compiled-channel experiment supplied 2026-07-20.
  Deliverable: real frozen GPT-2 span adapter, fixed paired evaluation,
  separated RNGs, multi-seed compiler-supervised/task-only/oracle/null controls,
  calibrated edge metrics, itinerary diagnostics, and L=5 structural holdout.
  Acceptance: frozen-base probe and instrument tests pass before a bounded GPU
  run; results distinguish language compilation from topology scaffolding and
  operator-core learning. Next command: freeze the experiment spec and
  implement/test GPT-2 offset-mapped span extraction. Evidence:
  `docs/compiled-channel/exp2_compiled_channel_supplied.py` and
  `library/heteroclinic-cap-carom-2026/SOURCE.md`.
  A one-seed TinyLM screen completed: edge labels were learned but L=5 and
  trajectory generalization were poor; it does not meet this task's acceptance
  criteria. Evidence: `experiments/20260721T055900Z-exp2-compiled-channel-tinylm/`.

- [ ] Strengthen the teach-loop mechanism screen before treating it as an LLM
  teaching result. Deliverable: paired old-task evaluation before/after each
  registration, routing-calibration/no-regression controls, N and teacher-noise
  sweep, ≥3 seeds, frozen GPT-2 description encoder, and prompted teacher
  traces. Acceptance: separated operator-acquisition, paraphrase-routing, and
  old-behavior-interference estimates with uncertainty. Next command: validate
  the pre/post routing diagnostic on a frozen-slot positive control. Evidence:
  `experiments/20260720T134700Z-exp3-teach-loop/`.

- [ ] After explicit approval, provision the approved RunPod resource, execute
  the frozen protocol, retrieve and verify artifacts, and terminate all
  billable resources.
- [ ] Interpret results with observed/inferred/hypothesis labels and update the
  project record.

## Waiting or blocked

- [ ] No current approval or sequencing blocker. Ben approved up to USD 10 on
  2026-07-19; protocol freezing and preflight remain before provisioning.

## Someday or exploratory

- [ ] Scrambled-order discovery, loops/halting, implicit-gradient DEQ, and
  length extrapolation after the one-off screen.

## Done recently

Move durable conclusions into `PROJECT.md`, `DECISIONS.md`, or experiment results rather than relying on this list.

- [x] Preserved supplied code, notebook, reports, and diagnostic figures with
  SHA-256 hashes; local all-variant forward/backward smoke test passed in
  `experiments/20260719T232358Z-local-smoke/`.
