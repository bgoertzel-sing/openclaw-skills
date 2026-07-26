# CAROM Execution Semantics

- Slug: `carom`
- Status: `active`
- Created: `2026-07-19`
- Last reviewed: `2026-07-24`
- Owner: Benjamin Goertzel

## Purpose

Test, at GPU scale, whether CAROM's shared command-routed operator core can
support scheduled, genuinely convergent fixed-point, and itinerant GLV
execution semantics on compositional sequence transforms.

## Success criteria

- The supplied code passes a local generator/model/training smoke test.
- A preregistered, bounded RunPod experiment compares the three execution
  semantics without silently changing the fixed-point model into an unrolled
  network.
- Every run records configuration, seed, hardware, wall time, accuracy by
  program depth, fixed-point residuals, itinerant trajectories, routing
  diagnostics, and retrieved artifact hashes.
- The pod and any billable storage are terminated after verified artifact
  retrieval.

## Scope

### In scope

- One-off RunPod GPU experiment on the supplied synthetic composition task.
- Scheduled, contraction-regularized fixed-point, fixed-chain itinerant, and
  exploratory free-inhibition itinerant variants.
- Correctness checks and mechanism diagnostics before endpoint comparisons.

### Out of scope for now

- Subagent delegation.
- Claims of broad algorithmic superiority from this toy task.
- Paid compute beyond an explicitly approved resource and cost/time bound.
- Implicit-gradient DEQ training, larger tasks, and downstream applications.

## Current state

Ben supplied three Python modules, a Colab notebook, two working notes, and two
reference plots. The CPU sandbox reports stable learning, a 256/256 itinerary
positive control for the trained hand-built GLV chain, a non-itinerant free-rho
baseline at 124 updates, and a fixed-point failure in which residuals grow
without contraction pressure. These are supplied claims pending independent
reproduction. Immediate next step: local smoke test, then freeze the bounded
GPU protocol and obtain explicit RunPod spend approval.

The first GPU screen is complete. The five-seed E0/E1 campaign is closed with
a deterministic-gate caveat. Raw fixed-minus-free was `+0.06956`
(seed-bootstrap 95% CI `[+0.00438,+0.13610]`); normalization worsened free
performance by `-0.29193` and collapsed activity mass. Evaluation randomized
initial activity in 15/20 arm/seeds, so these are exploratory mechanism
patterns rather than exact paired causal estimates. Deterministic E2 fitness
ablations and permutation-invariant E3 regularizers now pass CPU smoke and
fixture gates; E4/E5 remain closed. Ben subsequently supplied *The Heteroclinic Cap*
and a compiled-channel prototype that generates per-instance inhibition from
dependency-language span representations. The prototype passes a minimal CPU
smoke, but its executable currently uses TinyLM; a real GPT-2 span adapter and
repaired evaluation instrument are prerequisites to a GPU claim. A completed
one-seed TinyLM compiled-channel screen reached 0.695 task accuracy at L=2--4
but only 0.306 at held-out L=5, despite 0.865 edge accuracy; itinerary tau was
0.492. The separate TinyLM teach-loop screen acquired two held-out operators
by taught name (0.632 each) but showed weak paraphrase transfer (0.410/0.275)
and an unpaired old-task change (0.702 to 0.627), suggestive but not conclusive
of routing-mediated interference. These are
mechanism diagnostics, not GPT-2 or LLM-teaching claims. Evidence:
`experiments/20260721T055900Z-exp2-compiled-channel-tinylm/` and
`experiments/20260720T134700Z-exp3-teach-loop/`.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| Supplied prototype | none | `projects/carom/repos/carom` | unversioned import | SHA-256 recorded in project notes |

## Environments

- Local: Pop!_OS host, Python 3, PyTorch `2.12.1+cpu`, no CUDA.
- Data: procedurally generated sequence-transform compositions over six slots
  in Z8; no private data.
- Remote: RunPod account authenticated via `runpodctl`; no resource provisioned.

## Key results

- 2026-07-25: Local CPU forensics over all 13 preserved 12k compiled-channel
  checkpoints localized the acute collapse to steps 3,000--4,000 at peak LR.
  Broad operator-core norm growth and repaired itinerary decline lead it; a
  raw-gradient crisis coincides with it, followed by low-rank/starved hyper
  routing. Edge AUPRC improves while itinerary dominance fails, and the
  imported RelaLeap “Layer 5” premise does not describe CAROM. Schedule
  surgery can prevent the acute failure, but structural gain control remains
  indicated. Evidence:
  `experiments/20260726T-forensics-12k-collapse/`.

- 2026-07-25: Corrected GPT-2 controller v5 applied selected LR scales to
  state-restored, common-random held-out continuations at nonterminal updates
  600 and 1200. Action sensitivity and oracle headroom passed, but utility
  failed: at update 600 the selector chose 1.5x while 0.25x was oracle,
  worsening loss about 2.35% versus passive; at update 1200 it chose the
  oracle 0.5x and improved about 0.12%. The A100 run cost about USD 1.00;
  artifacts were hash-verified and the pod was terminated. Evidence:
  `experiments/20260725T161000Z-gpt2-controller-v5-active/`.

- 2026-07-25: The approved E2/E3 GPU attempt did not produce a scientific
  result within the USD 10 bound. A40 and H100 timing probes did not complete
  even the first of 25 arms; the H100 lower bound projects beyond 4.5 hours
  and USD 13.45. Partial logs were retrieved and every pod was terminated.
  The next gate is exact compiled/vectorized equivalence for the 70-step
  recurrence before another campaign. Evidence:
  `experiments/20260724T194500Z-e2-e3-gpu-r1/`.

- 2026-07-25: Full-shape local E2/E3 feasibility slices passed deterministic
  execution but ruled out a practical CPU confirmation on the current host.
  Fifty arm-updates took 3:26.47 with 7.80 GB peak RSS, projecting about
  86 wall hours for the frozen 75,000 training updates before full evaluation.
  This is resource calibration, not a scientific disposition. Numerical paired
  trajectory/exposure thresholds remain to be frozen; E4 stays closed.
  Evidence:
  `experiments/20260725T094800Z-e2-e3-full-cpu-feasibility-r1/` and
  `experiments/20260725T095240Z-e2-e3-full-cpu-train-rate-r1/`.

- 2026-07-23: Stochastic transition identification v2 completed locally and
  passed all preregistered gates at five frozen AdamW checkpoints. Distributional
  coverage was calibrated (median random/PCA ratios `0.9877/1.0532`), mean
  prediction matched AR(1) (`0.9922` ratio), oracle forcing reduced the error
  to `0.00472` of deployable distributional error, and AdamW mean dynamics
  passed (`1.2777` ratio). The v1 multi-step failure is therefore attributed to
  unobserved future minibatch noise, not demonstrated nonlinear state-model
  error. Active control remains shadow-only until a distributional activation
  gate is independently tested. Evidence:
  `experiments/20260723T224500Z-stochastic-transition-id-v2/`.

- 2026-07-22: Produced an eight-page ASCII-LaTeX/PDF report for BridgeLearn
  shadow-mode v2 with the exact CAROM task/model, AdamW/OneCycleLR schedule,
  all observer/planner parameters, complete evaluation trajectory, blockwise
  variance/innovation/sharpness/AR(2) results, telemetry schema, hashes,
  limitations, and a bounded next gate. The evidence separates already
  calibrated one-step variance tracking from innovation and momentum-state
  model misspecification; active control remains blocked. Report:
  `docs/carom_bridgelearn_shadow_v2_report_2026-07-22.{tex,pdf}`.

- 2026-07-22: BridgeLearn v0.3.0 shadow calibration v2 completed 1,500
  scheduled CAROM CPU updates with matched per-update observations. All 1,500
  LR non-mutation checks passed. Per-block variance correlations exceeded
  0.999996 and the maximum variance error fell from 0.111 in the cadence-
  confounded v1 trace to 0.00124. Active control remains blocked: innovation
  is underpredicted by several orders of magnitude, sharpness funnels are
  extremely wide with near-zero confidence, and AR(1) adequacy fails
  throughout while stable AR(2)-like dynamics dominate. Evidence:
  `experiments/20260722T200000Z-bridgelearn-shadow-mode-v2/`.

- 2026-07-22: A BridgeLearn v0.3.0 shadow integration completed 1,500 scheduled
  CAROM CPU updates under unchanged OneCycleLR control. The 11-point trace
  found its largest contraction discrepancy (0.338) and variance calibration
  error (0.111) near the LR peak, but predictions are one-step while realized
  statistics span evaluation intervals, so this is a schedule-instability
  diagnostic requiring matched-cadence estimator validation, not causal
  evidence. Evidence:
  `experiments/20260722T190000Z-bridgelearn-shadow-mode/`.

- 2026-07-22: The preregistered frozen-GPT-2 12,000-update extension completed
  but failed both accuracy targets. Frozen L2--4 accuracy peaked at 0.3268 at
  step 3,000 and ended at 0.1888; itinerary tau fell from 0.9870 at the peak to
  0.3281 final, while edge accuracy remained near 0.70. The collapse begins as
  the stretched OneCycleLR approaches its peak near step 3,600, supporting a
  schedule-destabilization hypothesis that remains single-seed and confounded
  with duration. All 13 checkpoints/results and 31 manifest files verified;
  pod terminated. Evidence:
  `experiments/20260722T015200Z-carom-gpt2-12k/`; detailed report:
  `docs/carom_gpt2_12k_detailed_results_2026-07-22.pdf`.
  Independent Fable/Sol reviews agree that high LR is the leading but unproven
  cause, and both reject interpreting ~0.70 raw edge accuracy as preserved
  graph prediction because it may be the majority-negative baseline. They
  recommend repaired checkpoint-only diagnostics followed by a bounded 1e-4
  warm start from the earlier 4k checkpoint, then matched fresh schedule
  controls. Synthesis: `docs/reviews/2026-07-22-carom-gpt2-12k-synthesis.md`.

- 2026-07-21: Completed a five-page detailed report of the frozen-GPT-2
  compiled-channel arm, including protocol, all checkpoint/intervention/budget
  results, TinyLM context, corrected interpretation, limitations, and a frozen
  12,000-update follow-up. Report:
  `docs/carom_gpt2_compiled_channel_report_2026-07-21.pdf`; rerun ledger:
  `experiments/20260722T015200Z-carom-gpt2-12k/` (completed 2026-07-22).

- 2026-07-21: The frozen GPT-2-small compiled-channel arm completed 4,000
  steps and, after repairing a corpus-unpacking defect, all three checkpoint
  intervention panels across nine checkpoints. Final L2--4 accuracy was 0.412,
  repaired tau 0.904, and natural-minus-shuffled accuracy 0.115; L5 remained
  weak (0.214 at S=72, 0.234 at S=120). These are single-seed provisional
  observations pending the full harness control suite. Artifacts and hashes:
  `experiments/20260721T222400Z-carom-gpt2-arm/`. Pod stopped after retrieval.

- 2026-07-21: Received and preserved a six-page CAROM--Oruzi reconciliation
  note. It motivates the v3 checkpoint panel, schedule and cross-slot
  interventions, staged PC-CAROM, reachability-first teach-loop registration,
  and portfolio evaluation. Its smoke readings are supplied rather than
  reproduced, and the supplied probe implementation remains blocked on the
  existing v3 audit and constructed controls. Source and sidecar:
  `../../library/carom-oruzi-reconciliation-2026/`.

- 2026-07-21: Received a three-page response to the Exp2/Exp3 audit. It accepts
  the shared-RNG and unpaired-M2 flaws and prioritizes two checkpoint-only
  discriminators before new training: repaired itinerary/intervention analysis
  and an L=5 test-time integration-budget sweep. Preserved source and sidecar:
  `../../library/carom-exp2-exp3-audit-response-2026/`.

- 2026-07-21: Audit of Ben's supplied `harness_v2.py` found that its own
  syntax and self-tests pass, but added counterexamples expose three blockers:
  revisits are erased before exact-order/transition scoring, AUROC is biased by
  tied logits, and evaluation hardcodes the TinyLM span path and fails the
  repository's GPT-2 adapter contract. Do not use it unchanged to revise
  Exp2/Exp3 conclusions. Evidence:
  `docs/compiled-channel/harness_v2_audit_2026-07-21.md`.

- Supplied sandbox report: `docs/carom_sandbox_report.pdf`.
- Theory note: `docs/carom_itinerant_note.pdf`.
- Reference diagnostics: `docs/fixed_point_deq_kink.jpg` and
  `docs/itinerant_trajectories.jpg`.
- Compiled-channel note/source audit:
  `../../library/heteroclinic-cap-carom-2026/SOURCE.md`.
- Detailed Exp2/Exp3 experiment and results synthesis:
  `docs/carom_exp2_exp3_detailed_summary.md` and rendered PDF.

## Open questions

- At matched updates and wall clock, what endpoints do the three semantics reach?
- Does the fixed-point residual decrease across sweeps throughout training and
  under extra inference sweeps?
- Can free inhibition discover ordered itinerancy, and under which explicit
  pressure, if any?
- Are synonym commands routed similarly at convergence?
- How do residual convergence and phase dwell statistics vary with program depth?

## Related projects and concepts

Deep-equilibrium models, content-addressable recurrent operator machines,
generalized Lotka-Volterra dynamics, stable heteroclinic channels, adaptive
computation, and compositional generalization.

## Risks

- A decreasing training loss does not establish equilibrium semantics; the
  per-sweep residual profile is a mandatory validity gate.
- The hand-built chain tests execution, while free rho tests order discovery;
  conflating them would overstate the result.
- Different variants have very different per-update compute, so report both
  update-matched and wall-clock-normalized views.
- The current `scrambled` CLI flag is unused by the generator and must not be
  presented as an order-discovery experiment until implemented and tested.
- Remote cost is disallowed without an explicit bound and approval.
- Licensing/provenance of supplied code is not stated; keep the run private
  and do not publish until clarified.

## Research-rule focus

Rules 1, 2, 5, and 7 are most relevant: validate residual/itinerary detectors,
freeze a plain-language protocol before scaling, preserve full reproducibility,
and keep execution semantics behind common instrumentation interfaces.
