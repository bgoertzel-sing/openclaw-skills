# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [x] Run E4 channel diagnostic calibration + confirmation on the frozen
  75-update student. Deliverable: full-versus-capped factor information,
  constraint weights `0.5x,1x,2x,5x`, and hidden/logit/both injection
  channels over three calibration seeds (`12011,13121,14251`) plus three
  disjoint confirmation seeds (`20801,21903,23017`) under five frozen
  thresholds (C1--C5). Acceptance: all thresholds frozen before unblinding,
  raw JSON and RUN.md records are durable, model weights unchanged, frozen
  negative E4 gate not revised. Evidence:
  `experiments/20260724T202915Z-e4-channel-diagnostic-summary-v2/` (cal),
  `experiments/20260724T210500Z-e4-channel-confirmation-3seed/` (conf).
  Completed 2026-07-24: all 5 thresholds passed on confirmation. full4/two-cap
  ratio exactly 2.0; logit/hidden ratio 2.16-2.18; both≈logit (max diff 1.5e-5);
  best G=4.344±0.283. Evidence: `docs/e4_channel_diagnostic.md`.

- [x] Complete E3 non-ceiling calibration and confirmation from an early-stop
  Option-1 homotopy student, then re-run E4 if E3 is informative. Deliverable:
  a 70--90% pre-E3 task-accuracy substrate, metered V1--V3 calibration on
  seeds `12011,13121,14251`, frozen-threshold confirmation on disjoint seeds
  `15313,16417,17519,18637,19739`, Prediction-1/V4 evidence where feasible,
  and a non-ceiling E4 FF/TC/OT/SC/OT+SC read. Acceptance: exact commands,
  configs, raw JSON, hashes, RUN.md interpretation, focused tests, and local
  coherent commits; supplied fibres remain labelled imposed structure and C2
  atoms are not used. Next command: calibrate the early-stop update count
  against held-out ID/CS task accuracy before running any E3 arm. Evidence:
  `experiments/20260724T195826Z-e3-partial-student-calibration/`.
  Completed 2026-07-24: 75 updates met the aggregate selection target;
  disjoint 3/5 E3 ran; supplied fibre failed the DGC bar; V4 did not cleanly
  support Prediction 1; E4 mean CS-loss G was `0.19828`, below `0.2`.
  Aggregate evidence:
  `experiments/20260724T201712Z-e3-nonceiling-disposition-v2/`.

- [ ] Execute ePC programme v1.1 Steps 1--7 sequentially on local CPU and
  document Step 8 scope. Deliverable: residual and transformer-like P1/M0
  controls; shared adjoint-field artifacts; dual-substrate M0--M5; matched
  E3 conditions with frontier-cost metering; E4 information-injection
  comparison; and E5 scope memo. Acceptance: each step has focused tests,
  machine-readable artifacts, a complete experiment record, and a coherent
  local commit; M3/M4 stay blinded until Prediction 2 is frozen against the
  selected substrate. Next command: implement and test
  complete. Next command: if revisiting Prediction 1, preregister effective
  displacement/step matching rather than changing the failed E3/E4 bars. C2
  completed 2026-07-24:
  positive dictionary structure on observable settled block 6 and all adjoint
  blocks, but C2 atoms remain barred from post-hoc E3 selection. Evidence:
  `experiments/20260724T185721Z-e2-c2-dictionary-5seed-v1-1-hungarian/`.
  E3 progress: all conditions and exact meters are implemented, but the three
  calibration seeds hit a no-update CS ceiling (`0.9974` exact), so no quality
  comparison or confirmation claim is justified. E4 calibration is negative:
  SC loss-headroom `G=0.062--0.098`, below `0.2`. E5 W1/W2 standalone MORK
  linalg parity passes; in-store tensor sinks remain absent. Evidence:
  `docs/e3_e5_reduced_disposition.md`.
  Non-ceiling follow-up 2026-07-24: the 75-update substrate enabled disjoint
  E3 confirmation, but supplied fibres failed the DGC bar; V4 was
  ambiguous/negative for Prediction 1; E4 improved to mean `G=0.19828` but
  remained below `0.2`. Evidence: `docs/e3_nonceiling_disposition.md`.
  Progress 2026-07-24: residual paths increased
  upstream observability but left 100% of KD/CE global top-5% mass in block 6
  at all depths; residual self-attention/MLP token mixing produced the same
  readout-local frontier and weaker upstream M0. Evidence:
  `experiments/20260724T135659Z-e1-residual-p1-m0-v1-1/` and
  `experiments/20260724T140015Z-e1-token-mixing-p1-m0-v1-1/`.
  Adjoint/M0 progress 2026-07-24: raw CE adjoints have 83.5% of top-5% mass
  in blocks 1--2, but settled/adjoint depth agreement is zero. Prediction 2
  is frozen per track in `configs/e2_prediction_2_frozen_v1_1.json`.
  Evidence: `experiments/20260724T140310Z-e2-residual-adjoint-m0-v1-1/`.
  Dual-battery progress: 18 tests and the reduced M1--M5 run passed; all 12
  JBD fits converged, but Prediction 2 is mixed/negative and no frozen
  confirmatory M1--M5 envelope exists. Evidence:
  `experiments/20260724T140951Z-e2-dual-m1-m5-v1-1-fixed/`.
  E2 decision 2026-07-24: criteria 1.2.0 frozen from constructed fixtures;
  disjoint 3-seed calibration and 5-seed confirmation completed; both tracks
  classify E2-B, M0 and Prediction 2 fail, and recovered fibres are barred
  from E3. Evidence: `docs/e2_disposition_memo.md` and experiments
  `20260724T181654Z-e2-calibration-3seed-v1-1-frozen-rerun/`,
  `20260724T181805Z-e2-confirmation-5seed-v1-1-frozen/`.

- [ ] Reconcile and execute the v1.1 ePC programme delta supplied by Ben on
  2026-07-23. Deliverable: preserved/hash-verified v1.1 source; immutable v1.0
  E1 record; versioned v1.1 criteria; shared settled-error/adjoint field
  schema; E1 post-hoc P1 depth profile and P2/M0 equivalence checks; and the
  E2 dual-substrate fast path with Prediction 2 frozen before fingerprint
  unblinding. Acceptance: P1 reports KD and CE top-5% mass by block; M0
  reports per-block cosine, norm ratio, top-5% Jaccard, depth-profile
  agreement, and random-field null; weights stay frozen during settle; fields
  share one schema; all launched runs and guard failures are retained. Next
  command: implement constructed M0 fixtures and a reduced terminal-student
  P1/P2 CPU run. Evidence:
  `../../library/revised-epc-experimental-programme-2026/v1.1/`,
  `configs/e1_e2_acceptance_v1_1.json`, and
  `experiments/<run-id>-e1-posthoc-m0/`.
  Progress 2026-07-23: source preserved and criteria frozen; 12 focused tests
  passed. The corrected reduced run preserved weights but put 100% of KD and
  CE top-5% mass in block 6 at `T=8`; blocks 1--3 had zero settled field.
  Next command: preregister and run a fixed-terminal-student depth sweep
  through `T=128`, checking field convention and upstream observability before
  any M3/M4 unblinding. Evidence:
  `experiments/20260724T061200Z-e1-posthoc-m0-v1-1-corrected/`.
  Depth sweep completed 2026-07-24: greater `T` propagated tiny upstream
  fields, but KD and CE retained 100% of global top-5% mass in block 6 through
  `T=128`; blocks 1--2 remained unobservable. Next command: audit exact field
  definition, normalization, loss placement, and update dynamics against
  Mesto/R8, with a constructed chain positive control. Evidence:
  `experiments/20260724T082216Z-e1-m0-depth-sweep-v1-1/`.

- [ ] Implement revised-programme Phase 1: shared E1 harness plus C1 control.
  Deliverable: reconciled canonical R8/R9 source/config; versioned
  plain-language and JSON protocol; geometric homotopy schedule and guards;
  provably teacher-free evaluator; per-block frontier/rank/concentration
  metrics; matched-seed direct-R8 contrast; artifact metering; and separate
  calibration versus confirmatory seed sets. Acceptance: constructed tests
  prove frozen weights during settlement, no teacher access on the
  teacher-free path, exact matched-seed pairing, per-block/pooled metric
  agreement, guard retention, deterministic artifact hashes, and rejection of
  factor-schema mismatches; reduced CPU smoke exits zero; resource/storage
  estimate is recorded before any paid run. Provenance reconciliation
  completed: `ecf2f79` is the direct child/final crash-fix commit of
  `9ccb151`. Next command: draft `docs/e1_homotopy_protocol.md` with distinct
  `R8-WikiText` pathology-reproduction and `E1-synthetic-grammar` homotopy
  identities; then add reduced frozen-weight/teacher-free invariant tests.
  Evidence: `docs/e1_homotopy_protocol.md`,
  `configs/e1_homotopy_acceptance_v1.json`, and
  `experiments/<run-id>-e1-homotopy-smoke/RUN.md`.
  Progress 2026-07-23: reduced six-block E1-SG harness implemented at
  RelaLeap branch `agent/e1-guarded-homotopy`, commit `dd1a6e9`; 15 focused
  and R8 regression tests pass. Final CPU smoke passed matched identities,
  frozen settlement weights, structurally teacher-free evaluation, finite
  outputs, constructed diagnostics, and deterministic scientific/NPZ replay.
  Milestone JSONL, factor closure/spill, retained guard evidence, and the
  objective-control identity test are included. Next command: freeze disjoint
  3/5 seeds and run calibration scale. Evidence:
  `experiments/20260724T001351Z-e1-homotopy-smoke-complete/`.
  Superseded priority note: v1.1 moves that calibration off the critical path;
  preserve any completed artifacts, but run P1/P2 and E2 adjoint/M0 first.

- [ ] Retain target-scope H0 as standing BP-residual control C1 on every
  teacher-free E3/E4 metric. Acceptance: multiple-seed held-out Γ,
  factor-specific intervals, spill, and all budgets are recorded; classify
  the interface by the paper's `>0.50` confidence gate. Next command: reuse
  the Phase-1 frozen rig/data identity rather than launch an independent,
  potentially mismatched H0 campaign. Evidence:
  `experiments/<run-id>-c1-h0-gpt2-small/RUN.md`.

## Next

- [ ] Implement E2 dual-substrate estimator validation before emergence
  claims: shared settled-error/adjoint schema, M0 equivalence, support
  Jaccard, principal angles, robust JBD, factor alignment, interventional
  fingerprints, observability floor, shuffled/random nulls, and dictionary C2
  on identical stored errors. Acceptance: constructed factorized,
  repeated-copy/underidentified, rotated-context, sparse-unstructured, and null
  fixtures classify correctly. Next command: map 0.4.0 JBD/dictionary APIs to
  the E2 metric contract.

- [x] Implement exact budget metering for dense/top-k/fibre/random E3 arms,
  including frontier-discovery cost, DGC-style error-feedback sparsification,
  and the proximal settle-versus-raw-BP ablation after E2 disposition.

- [x] Implement v1.1 E4 test-time-information evaluators: FF deployed default,
  OT, SC, OT+SC, and teacher-clamped diagnostic anchor; remove
  “amortization-gap” wording from new configs and memos.

- [x] Scope E5 W1/W2 against the actual local MORK API in parallel only after
  E1 student identity is frozen; E5 does not block E1/E2 interpretation.

## Waiting or blocked

None for the E2 decision gate. E3 may use supplied fibres under branch 5.2,
but recovered-fibre selection is closed by the E2-B result.

## Someday or exploratory

- [ ] Continue remaining H1--H6 claims only through the E1--E5 branch logic;
  supplied fibres remain diagnostics if emergence fails.

## Done recently

Move durable conclusions into `PROJECT.md`, `DECISIONS.md`, or experiment results rather than relying on this list.

- [x] 2026-07-23: Installed causal-fibres 0.4.0 in the project venv; doctor,
  smoke test, and all 54 released tests passed.
- [x] 2026-07-23: Completed the H0 CPU toy gate. The best combined-layer MLP
  achieved `Gamma_L=0.99143` (95% CI `[0.99070,0.99220]`) and
  `Gamma_A=1.0` (CI `[1,1]`); all five `Gamma_j` values were
  `0.81971`--`0.86188`. Evidence:
  `experiments/20260723T181654Z-h0-frozen-interface-cpu-final/RUN.md`.
- [x] 2026-07-23: Prepared but did not run
  `configs/h1_stage0b_toy_prepared.json`.
- [x] 2026-07-23: Preserved and audited Ben's revised E1--E5 programme at
  `../../library/revised-epc-experimental-programme-2026/SOURCE.md`; adopted
  Phase 1 with a calibration/confirmation correction and explicit compute
  metering.
- [x] 2026-07-24: Froze E2 criteria 1.2.0 from constructed fixtures, ran
  disjoint 3/5-seed calibration/confirmation, and classified settled-error and
  adjoint tracks E2-B. Prediction 2 and M0 fail; no recovered fibres advance.
- [x] 2026-07-24: Ran mandatory C2 SAE baseline on identical five-seed fields.
  It passes frozen M3/M4 on observable settled block 6 and all adjoint blocks,
  narrowing E2-B to a JBD-specific failure while leaving E3 on supplied fibres.
- [x] 2026-07-24: Implemented and calibrated reduced E3/E4 plus eligible E5
  W1/W2 kernels. E3 quality is ceiling-inconclusive, E4 SC is below material
  headroom, and MORK linalg parity passes while in-store integration is open.
