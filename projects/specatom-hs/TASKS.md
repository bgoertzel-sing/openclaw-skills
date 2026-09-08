# Tasks

- [x] **Revise expanded report with purpose, benchmark guidance, and serial /
  parallel plans (Ben, 2026-08-19)** — extend the latest PDF without pretending
  the future benchmark specifications are already complete.
  **Acceptance test:** the report explains the conceptual purpose and design
  rationale, summarizes prototype lessons, gives detailed authoring guidance
  for each prospective benchmark, and provides separate plans for one coding
  agent and six parallel coding agents; LaTeX compiles and sampled pages are
  visually readable.
  **Evidence:**
  `docs/plain2metta-architecture-and-worked-examples-expanded.{tex,pdf}` and
  `experiments/20260819T153624Z-plain2metta-expanded-r2-compile/`.  Tectonic,
  PDF metadata, text extraction, section-marker, and three-page visual checks
  passed.  Revised PDF is 30 pages / 12,802 extracted words; SHA-256
  `1c9d6a564bb3c73f84acea92dbcd34a8ad7244fc8ac387c02f9cf0ed4c34da88`.
  Published with curated reproducibility records on branch
  `agent/publish-expanded-report`, commit `f626dfe`, draft GitHub PR #4.

- [ ] **Realistic Plain2Metta benchmark suite and parallel acceleration plan
  (Ben, 2026-08-19)** — specify several substantially more complex, realistic
  cases in enough detail to drive the next implementation phase, and replace
  the implicit serial 6--8 week schedule with an explicit dependency graph for
  parallel coding agents.
  **Acceptance test:** a durable design document defines each case's Plain
  problem, semantic obligations, desired Plain→IR→MeTTa/Lean/runtime evidence,
  G0--G6 targets, acceptable Unknowns, adversarial mutations, fixtures, and
  measurable exit criteria; it also states agent/worktree ownership,
  prerequisite interfaces, integration cadence, critical path, realistic
  compressed schedule, and the tests preventing parallel merge drift.
  **Next command:** inventory existing general-pipeline seams and select a
  balanced benchmark portfolio spanning stateful/concurrent, transactional,
  temporal/numerical, and policy/epistemic semantics.
  **Evidence path:**
  `docs/plain2metta-realistic-benchmarks-and-parallel-roadmap.{tex,pdf}` and a
  compilation/verification experiment record.

- [x] **Expanded expository Plain2Metta architecture report (Ben,
  2026-08-18)** — replace the terse five-page status memo with a frontier-model
  authored, source-fact-checked tutorial/report for readers casually familiar
  with Plain, MeTTa, and Lean 4 but new to the Plain2Metta process.
  **Acceptance test:** revised LaTeX compiles to a substantially longer PDF;
  explains the artifact pipeline and Stages 1--11 in detail; walks through all
  three examples with concrete source/generated/runtime behavior; distinguishes
  observed evidence from limitations; and both files are delivered to Ben.
  **Next command:** launch the requested frontier-model drafting pass against
  the merged source and experiment records, then fact-check and compile it.
  **Evidence path:**
  `docs/plain2metta-architecture-and-worked-examples-expanded.{tex,pdf}`.
  Frontier-model draft was fact-checked against source and durable run records,
  compiled successfully with Tectonic, and verified with `pdfinfo` and
  `pdftotext`: 19 pages and 7,411 extracted words. SHA-256: PDF
  `5ab5ea6b0cbd759b9ee8dee2cbf663d213d66180479ecc1d52c953ccc0609402`;
  LaTeX `28042907ddc65c5afb0722c9de413789c8c98c72fb46d71ac6982ff3653d7cd0`.

- [x] **Plain2Metta architecture and progress report in LaTeX/PDF (Ben,
  2026-08-18)** — document what has been implemented, the current end-to-end
  architecture, validation/evidence stages, deployment state, and the three
  worked examples, using merged source and experiment records as evidence.
  **Acceptance test:** the LaTeX source compiles without errors to a readable
  PDF; both artifacts are stored under `docs/`, include exact current commit
  and deployment status, and are delivered to Ben.
  **Next command:** inspect merged source, worked-example fixtures, and Stage
  11/deployment records, then draft and compile the report.
  **Evidence path:** `docs/plain2metta-current-architecture-and-progress.tex`
  and `docs/plain2metta-current-architecture-and-progress.pdf`.
  Compiled successfully with Tectonic; PDF integrity check reports 5 pages,
  no encryption, and extractable text. SHA-256: source
  `5d843f3916ffd523113160760d775a5400ca0daf9e882c2bf3dfab9edc39d268`;
  PDF `4ec63e923c4177e2596599ab43ef97fe52b6e7af257ad2380904151ad1163202`.

- [x] **Merge accepted evaluation UI and deploy to existing ASI:Cloud VM2
  (Ben, 2026-08-18)** — merge draft PR #3 only if its head remains exact
  accepted commit `1755dddcb31dc02c04d7db35dec01ba1fb6b9215` and GitHub reports
  it mergeable, then deploy the resulting exact `main` commit to the existing
  VM2 without provisioning, resizing, or changing provider resources.
  **Acceptance test:** VM2 records the deployed Git commit, exactly one bounded
  Plain2Metta web service is listening on the intended interface, GET `/` and
  fresh POST `/api/evaluate` requests for all three bundled examples succeed
  with server-derived Stage 1--10 evidence, and the pre-deployment checkout and
  service configuration remain available as a rollback target.
  **Next command:** capture VM2's read-only host/service/repository baseline and
  PR identity, then merge PR #3 and deploy using the least-privilege existing
  VM mechanism.
  **Evidence:**
  `experiments/20260818T153337Z-plain2metta-pr3-merge-vm2-deployment/`.
  PR #3 merged at `5ce102cb02e72f377314205b28f102e5fc39911f`.
  VM2 runs exactly one systemd worker on `127.0.0.1:8081`; all three exact
  examples passed the Stage 1--10/G0--G6 canary after two fail-closed,
  successfully rolled-back trials (Lean cache permissions; newline-stripping
  canary bug). The exact release remains the rollback/restart target.

- [x] **Vertical Stage 1--11 evaluation-UI integration (Ben,
  2026-08-17)** — replace the legacy `/api/evaluate` shortcut and
  browser-synthesized grades with one exact-ancestry execution path through the
  revision-0.2 semantic-validation architecture. Work on public task branch
  `agent/plain2metta-public-evaluation-ui`; do not merge, release, deploy to
  VM2, expose a public service, use paid compute, install system-wide tools, or
  weaken any fail-closed gate. Preserve the existing legacy endpoint only as
  an explicitly labeled compatibility route if needed during migration.

  **Implementation order (each gate must pass before the next begins):**

  1. **Freeze the vertical contract.** Add a source-located route/service
     contract mapping each live example request to Stage 1 artifacts, Stage 2
     calculus, Stage 3 plan/review/approval, Stage 4--7 authorized backends,
     Stage 8 verdict composition, and Stage 9 evidence/API/UI projection.
     Define which Stage 10 corpus/calibration facts are immutable release
     metadata rather than rerun per request, and treat Stage 11 as the final
     acceptance gate rather than a runtime stage. Record resource bounds,
     timeout behavior, supported-example policy, and all fail-closed states.
  2. **Build the server-side orchestrator.** For each exact supported example,
     construct canonical Stage 1 source/contract/obligation artifacts; lower
     and interpret the Stage 2 typed contract; create and independently review
     one Stage 3 plan; execute only the tools authorized by that approved plan.
     Reuse the pinned Stage 4 Hypothesis, Stage 5 TLC, Stage 6 Z3, Stage 7 Lean,
     Hyperon, and Python adapters without bypassing their hash, ancestry,
     attribution, approval, or resource gates. A tool that is inapplicable must
     yield an explicit justified non-applicability/Unknown result, never a
     fabricated Pass.
  3. **Compose and expose real evidence.** Feed admitted runtime/formal evidence
     into the Stage 8 composer. The API response must be derived from stored
     canonical artifacts and expose exact IDs/hashes, plan/review state,
     backend attribution, counterexamples, assumptions/holes, residual risk,
     and the actual G0--G6 vector. Remove client-side grade inference and all
     hard-coded G4--G6 values; the Stage 9 UI must render only server-returned
     evidence. Downloads must use the existing exact-hash authorization gate.
  4. **Close semantic and adversarial tests.** Add end-to-end tests for all
     three graduated UI examples plus at least: source-byte mutation; stale or
     mismatched plan; missing approval; backend hash mismatch; timeout;
     malformed/misattributed evidence; cross-runtime disagreement; failing
     property/model/proof result; inapplicable backend; and unsupported or
     reworded input. Every case must either produce the expected conservative
     verdict/grade or fail atomically with no partial promoted state. Assert
     that changing source, contract, plan, review, or approval invalidates all
     downstream evidence and verdicts.
  5. **Vertical acceptance and handoff.** From a clean checkout, run the new
     focused vertical suite, the complete provider-free suite, pinned backend
     replay, compilation/diff/secret/large-file hygiene, browser/API smoke,
     and all three live dual-runtime examples. Create a reproducible experiment
     record before the consequential run, including exact commit, commands,
     tool hashes/versions, timings, and raw logs. Update the Stage 11 script so
     it proves the UI request path itself traverses Stages 1--9 and consumes
     recorded Stage 10 calibration metadata; it must not merely run component
     tests beside the legacy UI. Obtain an independent code-path audit before
     marking this task complete.

  **Acceptance test:** a fresh `POST /api/evaluate` for each supported example
  returns a server-derived exact-ancestry graph containing the canonical
  Stage 1--8 artifacts/evidence and actual G0--G6 verdict, while instrumented
  tests prove the approved Stage 4--7 adapters were invoked (or explicitly
  adjudicated inapplicable) and all mutation/staleness cases fail closed. No
  JavaScript grade synthesis remains. The full clean-checkout gate passes and
  a new experiment record contains the evidence.

  **Gate 4 increment 14 evidence (2026-08-17):** a current semantic-contract
  byte change after plan approval returns error-only HTTP 422 before any Stage
  4--7 adapter or legacy evaluation. Focused 1/1 and proportional 94/94 checks
  passed with compilation and diff hygiene. Evidence:
  `experiments/20260818T052300Z-plain2metta-evaluation-contract-invalidation/`
  and
  `experiments/20260818T052500Z-plain2metta-evaluation-contract-invalidation-proportional/`.
  Task-branch-only commit `f221825` is pushed.
  Next: one immutable-review invalidation case; Stage 11 remains unopened.

  **Gate 4 increment 15 evidence (2026-08-17):** replacing the current
  immutable Stage 3 review record after plan approval returns error-only HTTP
  422 before any Stage 4--7 adapter or legacy evaluation. Focused 1/1 and
  proportional 95/95 checks passed with compilation and diff hygiene.
  Evidence:
  `experiments/20260818T055528Z-plain2metta-evaluation-immutable-review-invalidation/`
  and
  `experiments/20260818T055546Z-plain2metta-evaluation-immutable-review-invalidation-proportional/`.
  Task-branch-only commit `56b53f8` is pushed.
  Next: Gate 5 begins with the smallest test-first change to
  `scripts/run-stage11-acceptance.sh` proving the UI request traverses Stages
  1--9 and consumes Stage 10 metadata. Create the consequential acceptance
  ledger before running it.

  **Gate 5 increment 1 evidence (2026-08-17):** the Stage 11 focused phase now
  invokes the complete real-route `tests.test_evaluation_web` module. Its
  29/29 tests passed, including fresh `/api/evaluate` assertions over Stage
  1--8 exact ancestry, server-derived G0--G6 grades, Stage 9 projection, and
  Stage 10 release metadata; shell syntax, compilation, and diff hygiene also
  passed. Evidence:
  `experiments/20260818T062821Z-plain2metta-evaluation-stage11-ui-instrumentation/`.
  This is not the consequential Stage 11 acceptance or clean-checkout result.
  Task-branch-only commit `1755ddd` is pushed.
  Next: create the acceptance ledger before running the updated Stage 11
  script.

  **Gate 5 increment 2 evidence (2026-08-17):** the pre-recorded Stage 11
  script passed on the clean task-branch working tree at exact commit
  `1755ddd`: focused 106/106 and complete provider-free 777/777 tests, plus
  compilation, diff, credential-pattern, large-file, and untracked-file
  hygiene. Evidence:
  `experiments/20260818T065419Z-plain2metta-evaluation-stage11-vertical-acceptance/`.
  This is not the required fresh-clean-checkout replay or independent audit.
  Next: create a new ledger and run the same script from a fresh temporary
  clone of `origin/agent/plain2metta-public-evaluation-ui`.

  **Gate 5 increment 3 evidence (2026-08-18):** a fresh single-branch clone
  resolved both checked-out and remote-tracking task-branch identities to exact
  commit `1755dddcb31dc02c04d7db35dec01ba1fb6b9215`, rebuilt the pinned Lean
  package (3015 jobs), and passed the Stage 11 script: focused 106/106 in
  54.455s, complete provider-free 777/777 in 70.111s, plus compilation, diff,
  credential-pattern, large-file, and untracked-file hygiene. The post-run
  checkout remained clean. Evidence:
  `experiments/20260818T072517Z-plain2metta-evaluation-stage11-clean-checkout/`.
  This does not complete the task: the required independent code-path audit is
  still outstanding. Next: perform exactly that read-only audit against the
  pushed commit before considering acceptance complete.

  **Gate 5 increment 4 / completion evidence (2026-08-18):** an independent
  read-only audit at exact pushed commit
  `1755dddcb31dc02c04d7db35dec01ba1fb6b9215` confirmed that the browser POSTs
  to `/api/evaluate`; the route invokes the Stage 1--8 orchestrator before the
  compatibility evaluator; the server returns the Stage 9 evidence projection
  with recorded Stage 10 release metadata; and JavaScript renders the returned
  `grade_achieved.vector` without synthesizing grades. Evidence:
  `experiments/20260818T075514Z-plain2metta-evaluation-stage11-independent-audit/`.
  Together with the fresh-clean-checkout acceptance record above, this closes
  the explicit task acceptance conditions. Merge, release, deployment, and
  service exposure remain separate human decisions.

  **Gate 1 evidence (2026-08-17):** frozen route/service contract added at
  `docs/evaluation-vertical-contract.md`. The new real-route end-to-end test
  returned HTTP 200 for the exact greeting example and then failed at the
  first required field with `KeyError: 'ancestry'`, proving the legacy response
  lacks Stage 1--8 ancestry; source inspection also locates browser grade
  synthesis in `evidenceView`. The unchanged legacy evaluation suite passed
  5/5 and diff hygiene passed. These changes intentionally remain uncommitted
  while the required red test is failing.

  **Gate 2 increment 1 evidence (2026-08-17):** `/api/evaluate` now admits only
  exact checked-in example bytes, persists canonical Stage 1 contract and
  obligation artifacts, checks/interprets the Stage 2 finite contract, and
  admits one independently authored/reviewed/approved Stage 3 plan. No Stage
  4--7 adapter is invoked. Focused checks passed 13 tests plus 10 subtests; the
  frozen full assertion now fails at the honest `[1,2,3]` boundary. Evidence:
  `experiments/20260817T181925Z-plain2metta-evaluation-vertical-stage123-r2/`.

  **Gate 2 increment 2 evidence (2026-08-17):** the exact approved plan invokes
  the existing bounded Hypothesis 6.138.15 coordinator with seed 417 and
  persists one exact-ancestry Stage 4 runtime-evidence node. Its closed
  `exact-equality` case validates only frozen source-byte admission, not general
  semantic behavior. Focused checks passed 14 tests plus 3 subtests and diff
  hygiene; the frozen full assertion remains red at `[1,2,3,4]` versus
  `[1..8]`. Evidence:
  `experiments/20260817T185258Z-plain2metta-evaluation-vertical-stage4/`.

  **Gate 2 increment 3 evidence (2026-08-17):** the same exact approved plan
  now carries a closed finite `exact-admission-stability` model, invokes pinned
  TLC 1.7.4/engine 2.19, and persists one exact-ancestry Stage 5 evidence node.
  Focused checks passed 31 tests plus 3 subtests and diff hygiene; the frozen
  full assertion remains red at `[1,2,3,4,5]` versus `[1..8]`. Evidence:
  `experiments/20260817T192622Z-plain2metta-evaluation-vertical-stage5-r2/`.

  **Gate 2 increment 4 evidence (2026-08-17):** the exact approved plan now
  includes a closed `exact-boolean-postcondition` task and invokes pinned Z3
  4.15.3. The admitted Stage 6 node retains exact plan/review ancestry, formula
  and source-map hashes, unsat core, proof, and resource bounds. Focused checks
  passed 40 tests plus 3 subtests and diff hygiene; the frozen full assertion
  remains red at `[1..6]` versus `[1..8]`. Evidence:
    `experiments/20260817T195503Z-plain2metta-evaluation-vertical-stage6-r2/`.

  **Gate 2 increment 5 evidence (2026-08-17):** the exact approved route plan
  now invokes pinned Lean 4.33.0 with pinned Mathlib through the existing
  hash-checked semantic-kernel coordinator. Its admitted Stage 7 node retains
  plan/review ancestry, package manifest, tool hashes, theorem source map, and
  bounds. Focused checks passed 36 tests plus 3 subtests and diff hygiene; the
  frozen full assertion remains red at `[1..7]` versus `[1..8]`. Evidence:
  `experiments/20260817T202518Z-plain2metta-evaluation-vertical-stage7-r3/`
  and `experiments/20260817T202558Z-plain2metta-evaluation-vertical-stage7-boundary/`.

  **Gate 2 increment 6 evidence (2026-08-17):** the route passes the four
  stored exact-plan Stage 4--7 evidence refs to the existing conservative
  Stage 8 composer and returns its stored verdict identity/hash plus the full
  server-derived G0--G6 vector. The verdict is correctly `unknown` because the
  canonical project still lacks admitted Hyperon/Python dual-runtime evidence;
  no legacy output was fabricated into evidence. Focused checks passed 53
  tests plus 3 subtests and diff hygiene. The frozen full assertion now reaches
  Stage 8 and remains red only at missing Stage 10 release metadata. Evidence:
  `experiments/20260817T205530Z-plain2metta-evaluation-vertical-stage8-r2/`.

  **Gate 3 increment 1 evidence (2026-08-17):** the route now returns a
  server-built `plain2metta-evaluation-evidence/v1` projection of the exact
  Stage 1--8 ancestry and verdict, with exact plan/review refs, backend
  attribution, counterexamples, assumptions, unresolved holes, and residual
  risk. The focused test first failed at `KeyError: 'evidence_projection'`,
  then passed. Proportional checks passed 36 tests plus 3 subtests and diff
  hygiene; the frozen acceptance assertion remains red only at missing Stage
  10 release metadata. Evidence:
  `experiments/20260817T212620Z-plain2metta-evaluation-vertical-stage9-r2/`.

  **Gate 3 increment 2 evidence (2026-08-17):** the Stage 10 loader now binds
  the checked-in corpus to its exact SHA-256 and calibration release ID,
  rejects changed bytes before parsing, and projects the validated threshold
  and mutation result as server-owned release metadata. Focused checks passed
  20/20 and the complete provider-free suite passed 763/763; compilation and
  diff hygiene passed. The first ledger run exposed only an invalid mock of a
  read-only `Path` method and is retained as failed evidence. Evidence:
  `experiments/20260817T215617Z-plain2metta-evaluation-vertical-stage10/`,
  `experiments/20260817T215712Z-plain2metta-evaluation-vertical-stage10-r2/`,
  and
  `experiments/20260817T215756Z-plain2metta-evaluation-vertical-stage10-full/`.
  Commit `3812d0c` is pushed on the task branch only.

  **Gate 4 increment 1 evidence (2026-08-17):** the browser now reads the
  Stage 9 server projection for the ancestry graph, complete G0--G6 vector,
  backend details, counterexamples, assumptions, and holes. Client-derived
  G0--G6 logic and hard-coded G4--G6 values are removed. The browser assertion
  first failed on the legacy synthesis. A source-byte mutation test also
  proves the request is rejected before either the legacy evaluator or Stage 4
  Hypothesis coordinator is called. Focused 2/2 and proportional 21/21 tests
  plus diff hygiene passed. Evidence:
  `experiments/20260817T222712Z-plain2metta-evaluation-browser-server-grades/`.
  Task-branch-only commit `d5afa00` is pushed.

  **Gate 4 increment 2 evidence (2026-08-17):** suppressing the exact Stage 3
  plan-review/approval transition makes the real route return only HTTP 422
  and the Hypothesis executor, TLC/Z3/Lean coordinators, and legacy evaluator
  are all uncalled. The focused red/green test and proportional web/API suite
  passed 16/16. Evidence:
  `experiments/20260817T225627Z-plain2metta-evaluation-missing-approval/`.
  Task-branch-only commit `b441698` is pushed.

  **Gate 4 increment 3 evidence (2026-08-17):** forging the Stage 4 adapter
  result's request hash makes the real route return only HTTP 422 after one
  Hypothesis call and before TLC, Z3, Lean, or the legacy evaluator can run.
  The focused test passed 1/1 and the proportional web/API plus Hypothesis
  suite passed 22/22 with diff hygiene. Evidence:
  `experiments/20260817T232547Z-plain2metta-evaluation-stage4-hash-mismatch/`
  and `experiments/20260817T232554Z-plain2metta-evaluation-gate4-proportional/`.
  Task-branch-only commit `eb2a0a2` is pushed.

  **Gate 4 increment 4 evidence (2026-08-17):** an injected Stage 4
  `subprocess.TimeoutExpired` now yields only HTTP 422 with a stable timeout
  error after one Hypothesis call and before TLC, Z3, Lean, or the legacy
  evaluator can run. The focused test passed 1/1; the proportional web/API
  plus Hypothesis suite passed 23/23 with compilation and diff hygiene.
  Evidence:
  `experiments/20260817T235835Z-plain2metta-evaluation-stage4-timeout/`.
  Task-branch-only commit `2fbb55d` is pushed.

  **Gate 4 increment 5 evidence (2026-08-17):** a Stage 4 adapter result with
  one unknown top-level claim now yields error-only HTTP 422 after one
  Hypothesis call and before TLC, Z3, Lean, or legacy evaluation. Focused 1/1
  and proportional web/API plus Hypothesis 24/24 tests passed with compilation
  and diff hygiene. Evidence:
  `experiments/20260818T002549Z-plain2metta-evaluation-malformed-stage4-evidence/`.
  Task-branch-only commit `bb7b68f` is pushed.

  **Gate 4 increment 6 evidence (2026-08-17):** a real-route Hyperon/Python
  output disagreement now has a regression proving the legacy semantic result
  fails while the canonical Stage 8 verdict remains honestly `unknown`, with
  G2/G3 false and exactly the four admitted Stage 4--7 evidence references.
  Legacy runtime output is not fabricated into the evidence graph. Focused
  1/1 and proportional evaluation/verdict 36/36 tests passed with diff
  hygiene. Evidence:
  `experiments/20260818T005400Z-plain2metta-evaluation-cross-runtime-disagreement/`.
  Task-branch-only commit `e65e839` is pushed.

  **Next command:**
  `rg -n "inapplicable|admissible_methods|formal_tasks|state_models" tests/test_evaluation_web.py src/specatom_hs/evaluation_vertical.py src/specatom_hs/validation_plan.py`.
  Gate 4 must next add exactly one smallest inapplicable-backend case with an
  explicit justified Unknown result; do not start Stage 11.

  **Gate 4 increment 7 evidence (2026-08-17):** a valid failing Stage 4
  property result now yields a conservative failed verdict with G4 false and
  projects its exact obligation/evidence-bound persisted counterexample through
  Stage 9. The focused test first failed at the prior hard-coded empty
  counterexample list. Proportional evaluation/verdict/Hypothesis checks passed
  42/42 with compilation and diff hygiene. Evidence:
  `experiments/20260818T012701Z-plain2metta-evaluation-failing-property/`.
  Task-branch-only commit `93f0581` is pushed.

  **Gate 4 increment 8 evidence (2026-08-17):** an explicitly inapplicable
  Stage 5 TLC backend is not invoked, is projected as justified `unknown`,
  leaves G5 false, and contributes its `tla-tlc` limitation to the canonical
  Stage 8 residual risk. The focused test first failed because no applicability
  boundary existed. Focused 1/1 and proportional evaluation/verdict 38/38
  tests passed with compilation and diff hygiene. Evidence:
  `experiments/20260818T022403Z-plain2metta-evaluation-inapplicable-tlc/`.
  Task-branch-only commit `d4837bc` is pushed.

  **Next command:**
  `rg -n "invariant_satisfied|counterexample_trace|formal backend rejected" tests/test_evaluation_web.py tests/test_tlc_backend.py src/specatom_hs/evaluation_vertical.py src/specatom_hs/verdict_composition.py`.
  Gate 4 must next add exactly one failing TLC model-result case; do not start
  Stage 11.

  **Gate 4 increment 9 evidence (2026-08-17):** an admitted failing TLC model
  result returns a server-derived Stage 5 `fail` status, forces the Stage 8
  verdict to fail, keeps G5 false, and projects the persisted counterexample
  through Stage 9. Focused 1/1 and proportional 39/39 tests passed with
  compilation and diff hygiene. Evidence:
  `experiments/20260818T025041Z-plain2metta-evaluation-failing-tlc-r2/`.
  Task-branch-only commit `d894c6c` is pushed.

  **Next command:**
  `rg -n "replace_source|invalidate|stale|approval" tests/test_evaluation_web.py tests/test_projects.py src/specatom_hs/projects.py`.
  Add exactly one uncovered transitive-invalidation case; Stage 11 remains
  unopened.

  **Gate 4 increment 10 evidence (2026-08-17):** a rejected Stage 7 Lean
  result now has a real-route regression proving error-only HTTP 422 after one
  Lean call and before legacy evaluation. No failed proof is admitted or
  projected. Focused 1/1 and proportional evaluation/verdict/Lean 46/46 tests
  passed with compilation and diff hygiene. Evidence:
  `experiments/20260818T032408Z-plain2metta-evaluation-failing-lean/`.
  Task-branch-only commit `3317133` is pushed.

  **Gate 4 increment 11 evidence (2026-08-17):** replacing the exact source
  immediately after Stage 3 approval returns error-only HTTP 422 before any
  Stage 4--7 adapter or legacy evaluation call. Focused 1/1 and proportional
  web/project/plan/verdict 91/91 tests passed with compilation and diff
  hygiene. Evidence:
  `experiments/20260818T035512Z-plain2metta-evaluation-source-invalidation-r2/`
  and
  `experiments/20260818T035525Z-plain2metta-evaluation-source-invalidation-proportional/`.
  Task-branch-only commit `b545dc8` is pushed.

  **Next command:**
  `rg -n "add_semantic_artifact|submit_plan_review|decide\(|_invalidate" tests/test_evaluation_web.py tests/test_projects.py src/specatom_hs/evaluation_vertical.py src/specatom_hs/projects.py`.
  Add exactly one remaining contract/plan/review/approval transitive-
  invalidation case; Stage 11 remains unopened.

  **Gate 4 increment 12 evidence (2026-08-17):** revoking the exact Stage 3
  plan approval immediately after its independent review returns error-only
  HTTP 422 before any Stage 4--7 adapter or legacy evaluation call. Focused
  1/1 and proportional web/project/plan/verdict 92/92 tests passed twice with
  compilation and diff hygiene. Evidence:
  `experiments/20260818T042448Z-plain2metta-evaluation-approval-revocation/`,
  `experiments/20260818T042503Z-plain2metta-evaluation-approval-revocation-proportional/`,
  and its independent local rerun `experiments/20260818T042601Z-plain2metta-evaluation-approval-revocation-proportional-r2/`.
  Task-branch-only commit `b4da714` is pushed.

  **Next command:**
  `rg -n "add_semantic_artifact|submit_plan_review|review|_invalidate" tests/test_evaluation_web.py tests/test_validation_plan.py src/specatom_hs/evaluation_vertical.py src/specatom_hs/projects.py`.
  Add exactly one remaining contract, plan-byte, or review invalidation case;
  Stage 11 remains unopened.

  **Gate 4 increment 13 evidence (2026-08-17):** a new current validation-plan
  version created after independent approval, with changed canonical bytes and
  no matching immutable review, now has a real-route regression proving
  error-only HTTP 422 before Hypothesis, TLC, Z3, Lean, or legacy evaluation.
  Focused 1/1 and proportional web/project/plan/verdict 93/93 tests passed with
  compilation and diff hygiene. Evidence:
  `experiments/20260818T045459Z-plain2metta-evaluation-plan-byte-invalidation/`
  and
  `experiments/20260818T045510Z-plain2metta-evaluation-plan-byte-invalidation-proportional/`.
  Task-branch-only commit `ced782f` is pushed.

  **Next command:**
  `rg -n "SEMANTIC_CONTRACT|add_semantic_artifact|review binding|requires an approved reviewed plan" tests/test_evaluation_web.py tests/test_validation_plan.py src/specatom_hs/evaluation_vertical.py src/specatom_hs/projects.py`.
  Gate 4 must next add exactly one contract or immutable-review invalidation
  case; do not start Stage 11.

- [ ] **Implement general semantic validation revision 0.2 (Ben,
  2026-08-16)** — implement
  `docs/plain2metta-general-semantic-validation-spec.tex` revision 0.2 through
  its ordered Stage 0--11 gates. Begin with Stage 0 only: freeze the current
  interfaces and threat model; verify and pin candidate Hypothesis, TLA+/TLC,
  Z3/SMT-LIB, Lean 4/Mathlib, and Hyperon toolchains in isolated environments;
  preserve the live dual-runtime evaluation baseline. Acceptance for Stage 0:
  a source-located interface/trust map, compatibility and migration rules,
  unchanged upstream smoke tests for selected tools, full existing Plain2MeTTa
  regression and live example replay, and reproducible evidence. Later stages
  must not start until their predecessor's gate passes. Continue on
  `agent/plain2metta-public-evaluation-ui` / draft PR #3 unless isolation or a
  focused successor branch is needed. Never push/merge the default branch,
  force-push, publish a release, install system-wide dependencies, expose the
  UI publicly, or use paid compute. Stage 0 is complete: the interface map is
  frozen, the 662-test and live baselines replayed, and isolated smokes passed
  for Hypothesis 6.138.15, Z3 4.15.3, TLC 1.7.4, Lean/Mathlib 4.33.0, and
  Hyperon 0.2.10. Stage 1 is complete at public task-branch commit
  `3073448`: all eight strict semantic artifact types use canonical
  schema v1 serialization and exact reviewed-source/contract ancestry;
  adversarial inputs fail closed; a source-byte mutation invalidates the full
  contract-to-verdict chain. Focused 6/6, full 668/668, compile/diff/hygiene,
  and live three-example dual-runtime replay passed. Stage 2 is complete: the
  finite closed calculus, deterministic provider-free interpreter, and typed
  canonical MeTTa projection bind the exact Stage 1 artifact; unsupported or
  unresolved meaning fails closed. Focused 9/9, full 677/677, static/hygiene,
  and live dual-runtime gates passed. Stage 3 is complete: a one-call,
  provider-independent validation author sees only exact reviewed source and
  contracts/obligations; strict plan admission, immutable review/edit records,
  exact approval binding, and transitive invalidation fail closed. Focused
  12/12, full 683/683, static/hygiene, and live dual-runtime gates passed.
  Current objective: **Stage 4 only**, the Hypothesis property/state-machine
  backend; do not begin Stage 5. Evidence:
  `experiments/20260817T035226Z-plain2metta-general-semantic-validation-stage0/`
  `experiments/20260817T040300Z-plain2metta-stage0-tlc-lean/`, and
  `experiments/20260817T073700Z-plain2metta-general-semantic-validation-stage1/`,
  and
  `experiments/20260817T075100Z-plain2metta-general-semantic-validation-stage2/`.
  `experiments/20260817T080828Z-plain2metta-general-semantic-validation-stage3/`.

- [x] **General semantic-validation architecture specification (Ben,
  2026-08-16)** — wrote an ASCII-only LaTeX specification integrating typed
  contracts, independent validation plans, graded evidence, executable
  oracles, property/metamorphic/state-machine/differential/formal methods,
  immutable provenance, narrow APIs, UI requirements, and five qualitatively
  different examples. Revision 0.2 adds a concrete Hypothesis, TLA+/TLC,
  Z3/SMT-LIB, Lean 4/Mathlib, and Hyperon/Python routing architecture plus an
  eleven-stage coding-agent plan with acceptance gates. Tectonic produced an
  11-page PDF; source and PDF hashes, textual completeness, metadata, and
  visual inspection are
  recorded in
  `experiments/20260817T034237Z-plain2metta-semantic-validation-spec-r02-compile/`.
  Artifacts:
  `docs/plain2metta-general-semantic-validation-spec.{tex,pdf}`. Next: Ben
  reviews revision 0.2 before it becomes an implementation milestone.

- [x] **Runtime-validated mixed MeTTa/Python evaluation examples (Ben,
  2026-08-16)** — extend the public evaluation UI so its representative
  examples execute generated MeTTa through a real, pinned MeTTa runtime as
  well as generated Python through the bounded sandbox. Add substantive,
  example-specific expected-output assertions that test behavior against the
  Plain requirements, rather than treating exit code 0 or balanced
  parentheses as semantic validation. Acceptance: each graduated example
  visibly preserves Plain → reviewed logical IR → generated artifacts
  provenance; both runtime paths execute under recorded bounds; exact expected
  results pass; negative/mismatch cases fail closed; focused/full tests and
  live UI smoke pass; the public task branch/draft PR and an experiment record
  contain the evidence. Completed at public task-branch head `752debd` and
  draft PR #3. Hyperon CLI 0.2.10 and bounded Python execute exact behavioral
  profiles for greeting trace retention, task validation/ownership, and
  forecast split/horizon/baseline reporting, with assertions visible in the
  default claim-evidence view. Focused 11/11 and full 662/662
  passed; live dual-runtime replay passed all three examples; both language
  mismatch cases fail closed. Evidence:
  `experiments/20260816T223000Z-plain2metta-behavior-validation/`. PDF work
  remains deferred until Ben evaluates this behavior.

- [x] **Plain2MeTTa public evaluation milestone (Ben, 2026-08-16)** —
  deliver an extended web UI for concrete examples across the logical-IR
  pipeline, expose a safe experimental URL, integrate a real but sandboxed
  path from Plain spec through logical IR to inspectable executable MeTTa and
  Python outputs, publish the completed code on a task branch in the public
  `bgoertzel-sing/plain2metta` repository, and produce a concise PDF design and
  implementation report suitable for frontier-model review. Acceptance:
  representative end-to-end examples in the UI; provenance/review gates remain
  visible; generated code is explicitly distinguished from validated code;
  focused/full tests and browser smoke pass; public branch/PR and PDF hashes
  are recorded. Next command: audit the existing webapp and v2 worktrees,
  public branches/PRs, and deployment options before choosing the smallest
  Completed first usable evaluation release on public task branch
  `agent/plain2metta-public-evaluation-ui` at `4683984`, draft PR #3. The
  Tailnet-only UI is live at `http://100.72.218.34:8081/` in tmux session
  `plain2metta-eval`. Focused tests passed 6/6 and full provider-free discovery
  passed 655/655. The two-page PDF report was visually inspected; SHA-256
  `3042d573728685b585f8165a50262ccd106a90393b79fe81fa3c4728291bbaeb`.
  Evidence: `experiments/20260816T181041Z-plain2metta-public-evaluation-ui/`.
  integration branch. Evidence path: a new run under `experiments/`.
  **Priority order clarified by Ben:** (1) working extended UI; (2) concrete
  executable MeTTa/Python examples that visibly pass through logical IR and
  run/tests; (3) Ben evaluates and iterates on behavior; (4) only after the
  design behaves sensibly, write the PDF; (5) incorporate frontier-model
  review; (6) seek review from human MeTTa developers. PDF work must not delay
  or substitute for UI/executable-example progress.
  Latest product increment: branch `agent/plain2metta-public-evaluation-ui`
  at `4c30a35` adds a browser-local download of the complete evaluation
  evidence JSON. Focused tests passed 7/7, full discovery passed 658/658, and
  live health/UI/export-marker/sandbox smoke passed at the Tailnet URL.

- [x] **Plain2MeTTa v2 current-HEAD acceptance revalidation — 2026-08-16:**
  at clean isolated revision `590fc7d`, reverified the expected PDF hash,
  passed the focused artifact/version, approval, invalidation, persistence,
  logical-IR, and end-to-end set 64/64, and passed the full provider-free suite
  651/651. Byte-compilation, diff, credential-pattern, large-file, and
  untracked-file checks also passed. Evidence:
  `experiments/20260816T131920Z-plain2metta-v2-head-revalidation/RUN.md`.
  Next: Ben must select any scope-expanding product milestone.

- [x] **Plain2MeTTa v2 provider-free Phase 2–7 acceptance replay — 2026-08-14:**
  added a persisted end-to-end exact-chain test and an original-source mutation
  replay proving all downstream phases invalidate and trace retrieval fails
  closed. Added a source-located PDF completion audit that distinguishes the
  completed provider-free logical-IR core from the unimplemented web UI,
  concrete provider/compiler, and sandbox-executor work. Focused tests passed
  2/2; full provider-free suite passed 651/651. Evidence:
  `experiments/20260814T165042Z-plain2metta-v2-end-to-end-acceptance/RUN.md`.
  Next: Ben must select the next scope-expanding product milestone.

- [x] **Plain2MeTTa v2 Phase 7 exact-chain traceability retrieval — 2026-08-14:**
  strengthened the existing read-only trace query and exact
  `GET /api/trace/<project-id>` route so the report is independently rebuilt
  from the nine exact current artifact versions (original, elaborated, tests,
  paired reviewed snapshots, logical IR, compiler output, sandbox handoff, and
  test result). Noncanonical reports, incomplete or mismatched upstream chains,
  stale source replacements, and unknown spec filters fail closed. The response
  contains provenance and coverage/failure metadata but no artifact, generated
  file, stdout, or stderr bodies and no mutation/execution authority. Focused
  tests passed 40/40 and the full provider-free suite passed 649/649. Evidence:
  `experiments/20260814T164358Z-plain2metta-v2-phase7-exact-chain/RUN.md`.
  Local implementation commit: `361bdb7` (not pushed).
  Next: provider-free end-to-end Phase 2–7 acceptance replay and PDF-derived
  completion audit.

- [x] **Plain2MeTTa v2 Phase 6 sandbox adapter and atomic admission — 2026-08-14:**
  added an explicitly configured, provider-independent sandbox coordinator. It
  makes exactly one injected adapter call with the canonical inert handoff,
  validates strict result structure, request binding, and configured adapter
  attribution, rechecks the exact handoff after external I/O, and atomically
  saves the test result. Failures and concurrent mutation cause no retry or
  partial result write. No built-in host executor, network, secrets, or file
  publisher was added. Focused tests passed 4/4 and the full provider-free
  suite passed 644/644. Evidence:
  `experiments/20260814T160752Z-plain2metta-v2-sandbox-adapter/RUN.md`.
  Local implementation commit: `91c9350` (not pushed).
  Next: strict opt-in `POST /api/test/<project-id>` transport around this
  configured coordinator.

- [x] **Plain2MeTTa v2 validated compiler-output metadata query — 2026-08-14:**
  added a read-only query and exact
  `GET /api/compiler-output/<project-id>` route bound to the current validated
  compilation-log/output/logical-IR chain. It returns compiler attribution,
  artifact IDs/hashes, generated paths, per-file hashes/byte sizes, and
  spec/test traceability IDs without generated bodies, guidance, mutation,
  approval, publication, or execution authority. Focused tests passed 38/38
  and the full provider-free suite passed 640/640. Evidence:
  `experiments/20260814T155155Z-plain2metta-v2-compiler-output-query/RUN.md`.
  Local implementation commit: `bba7a9c` (not pushed).
  Next: provider-independent Phase 6 sandbox adapter envelope and atomic
  test-result admission, without a built-in host executor.

- [x] **Plain2MeTTa v2 Phase 5 single-call adapter and atomic admission — 2026-08-14:**
  added an explicitly configured vendor-neutral compilation coordinator. It
  makes exactly one call, binds the canonical prompt to exact current reviewed
  spec/test and approved logical-IR bytes, validates provider/model attribution,
  rechecks all inputs after external I/O, and atomically saves a canonical
  provenance log plus inert compiler output. Reload rejects partial, forged, or
  misattributed state. Focused tests passed 50/50 and the full provider-free
  suite passed 635/635. Evidence:
  `experiments/20260814T151947Z-plain2metta-v2-compilation-adapter/RUN.md`.
  Local implementation commit: `f76d9b4` (not pushed).
  Next: strict `POST /api/compile/<project-id>` transport without provider
  selection, retry, credentials, publication, or execution authority.

- [x] **Plain2MeTTa v2 deterministic type and obligation reachability checks — 2026-08-14:**
  Phase 4 review now reports critical inconsistent-type findings for duplicate
  contract names with differing signatures and typed holes that disagree with
  their contract outputs. Requirement obligations whose source provenance
  reaches no contract are reported as unreachable. Findings are deterministic,
  source-linked, and use the existing exact review/decision/compile gates.
  Focused tests passed 20/20 and the full provider-free suite passed 622/622.
  Evidence: `experiments/20260814T144815Z-plain2metta-v2-logical-ir-type-reachability/`.
  Local implementation commit: `282c12e` (not pushed).
  Next: exercise exact repair/waive/defer decision replay across all eight PDF
  §3.5 critical finding categories and verify regenerated-review stability.

- [x] **Plain2MeTTa v2 deterministic Phase 4 consistency checks — 2026-08-14:**
  added source-linked critical findings for exact contradictory invariant
  polarities, invalid ordering endpoints/cycles, and positive future/test
  leakage patterns. Explicit prohibitions remain non-findings. Focused tests
  passed 14/14 and the full provider-free suite passed 619/619. Evidence:
  `experiments/20260814T144044Z-plain2metta-v2-logical-ir-consistency/RUN.md`.
  Local implementation commit: `ac5272e` (not pushed).
  Next: deterministic inconsistent-type and unreachable-obligation checks.

- [x] **Plain2MeTTa v2 Phase 4 logical-IR gold fixtures — 2026-08-14:**
  added provider-free auth and ML/time-series logical-IR fixtures covering all
  11 reviewed clauses, with exact requirement/test obligations and one explicit
  typed operational hole per grounded contract. Real deterministic review
  replay retains unresolved policy/model definitions as source-linked critical
  findings and blocks compilation. Focused tests passed 4/4 and the full
  provider-free suite passed 616/616. Evidence:
  `experiments/20260814T143255Z-plain2metta-v2-logical-ir-gold-fixtures/RUN.md`.
  Local implementation commit: `79c7d78` (not pushed).
  Next: add deterministic Phase 4 checks for contradictory invariants,
  invalid ordering/data flow, and possible leakage.

- [x] **Plain2MeTTa v2 strict Phase 4 logical-IR POST transport — 2026-08-14:**
  added exact `POST /api/logical-ir/<project-id>` to the bounded POST-only WSGI
  adapter. It accepts only optional text guidance, requires an explicitly
  configured coordinator, invokes its one-call transaction, and returns only
  the admitted interaction-log, logical-IR, and logical-review identities and
  hashes. Alternate identities, unknown/duplicate fields, bad framing,
  unconfigured generation, and backend failure fail closed; failure makes no
  artifact write or retry. Focused tests passed 23/23 and the full
  provider-free suite passed 607/607. Evidence:
  `experiments/20260814T134939Z-plain2metta-v2-logical-ir-post-transport/RUN.md`.
  Local implementation commit: `e818489` (not pushed).
  Next: strict read-only retrieval of the current validated logical-IR review
  and exact-version finding-decision transport from PDF §§3.5 and 4.3.

- [x] **Plain2MeTTa v2 Phase 4 single-call adapter and atomic admission — 2026-08-14:**
  added an explicitly configured vendor-neutral logical-IR adapter boundary.
  It makes one call, binds the canonical prompt to exact current reviewed
  snapshot bytes, validates provider/model provenance, rechecks those versions
  after the external call, and atomically persists the provenance log, strict
  logical IR, and deterministic review. Reload rejects forged logs. Failure
  cases leave no logical-IR write and trigger no retry. Focused tests passed
  56/56; the full provider-free suite passed 604/604. Evidence:
  `experiments/20260814T133600Z-plain2metta-v2-logical-ir-adapter/RUN.md`.
  Local implementation commit: `83ede24` (not pushed). Next: expose the exact
  `POST /api/logical-ir/<project-id>` boundary from PDF §5 without adding
  provider selection, retry, credentials, or generic mutation authority.

- [x] **Plain2MeTTa v2 Phase 4 reviewed-input admission — 2026-08-14:**
  logical-IR creation now requires the exact current paired reviewed
  elaborated/test snapshots and persists those refs as its upstream provenance.
  Direct Phase 2 approvals cannot bypass Phase 3; reload rejects logical IRs
  rebound to Phase 2 inputs. Phase 7 traceability now includes both reviewed
  snapshots. Focused tests passed 49/49 and the full provider-free suite passed
  594/594. Evidence:
  `experiments/20260814T130310Z-plain2metta-v2-phase4-reviewed-inputs/RUN.md`.
  Local commit: `92612b3` (not pushed). Next: add a provider-independent Phase 4
  logical-IR request/response envelope bound to these reviewed refs.

- [x] **Plain2MeTTa v2 reviewer-edited reviewed snapshots — 2026-08-14:**
  Phase 3 review-log v2 accepts an exact paired elaborated/test edit set and,
  only after full exact-input approval, persists those bytes as immutable
  reviewed artifacts. Unchanged review remains byte-identical; partial, blank,
  stale, unapproved, malformed, or forged edits fail closed. Read-only decision
  retrieval returns edit hashes without bodies. Focused tests passed 38/38 and
  the full provider-free suite passed 593/593. Evidence:
  `experiments/20260814T125622Z-plain2metta-v2-reviewed-snapshot-edits/RUN.md`.
  Next: bind Phase 4 logical-IR admission to the exact reviewed snapshot refs.

- [x] **Plain2MeTTa v2 current Phase 3 review-decision retrieval — 2026-08-14:**
  added a read-only query that strictly reparses and validates the current
  review log against the exact current elaborated/test refs. Added exact
  `GET /api/review-decisions/<project-id>` without query parameters, artifact
  bodies, or mutation authority. Focused tests passed 12/12; the full suite
  passed 590/590. Evidence:
  `experiments/20260814T124300Z-plain2metta-v2-phase3-review-decision-query/RUN.md`.
  Local implementation commit: `519938a` (not pushed).
  Next: exact-version reviewer-edited reviewed snapshots for PDF §3.4.

- [x] **Plain2MeTTa v2 exact Phase 3 review POST transport — 2026-08-14:**
  added strict `POST /api/review/<project-id>` handling for the canonical
  exact-version review log. It reuses bounded duplicate-safe JSON framing,
  rejects alternate identities, stale hashes, expanded schemas, and malformed
  decisions without persistence, and returns the immutable review-log ID/hash
  after the atomic transaction creates reviewed snapshots. Focused Phase 3 and
  transport tests passed 19/19; the full provider-free suite passed 588/588;
  compileall and diff hygiene passed. Evidence:
  `experiments/20260814T123554Z-plain2metta-v2-phase3-review-post-transport/RUN.md`.
  Local implementation commit: `6d14384` (not pushed).
  Next command: expose the validated current review log through the narrow
  read-only query/GET boundary so persisted decisions are retrievable without
  returning reviewed artifact bodies.

- [x] **Plain2MeTTa v2 exact Phase 3 decisions and reviewed snapshots — 2026-08-14:**
  added a strict transaction binding approve/request-changes/reject decisions,
  optional section/item targets and comments, whole-second UTC timestamps, and
  reviewer identities to the exact current elaborated/test hashes. Exact
  artifact-level approval creates byte-identical reviewed-spec snapshots bound
  to the immutable review log; source mutation transitively invalidates log,
  snapshots, and approvals. Focused tests passed 60/60 and the full
  provider-free suite passed 586/586; compileall, diff, credential, large-file,
  and untracked inspection passed. Evidence:
  `experiments/20260814T122412Z-plain2metta-v2-phase3-review-decisions/RUN.md`.
  Local implementation commit: `1060d65` (not pushed).
  Next command: expose this exact transaction through strict
  `POST /api/review/<project-id>` transport without generic mutation authority.

- [x] **Plain2MeTTa v2 exact Phase 3 review GET transport — 2026-08-14:**
  added `GET /api/review/<project-id>` to the server-independent read-only WSGI
  adapter. It returns the recomputed exact-version report, accepts no query
  parameters, and rejects stale chains, unknown projects, noncanonical paths,
  and mutation methods. Focused tests passed 17/17 and the full provider-free
  suite passed 580/580; compileall and repository hygiene passed. Evidence:
  `experiments/20260814T120953Z-plain2metta-v2-phase3-review-transport/RUN.md`.
  Local implementation commit: `4840c4b` (not pushed).
  Next command: add the Phase 3 exact-version review decision/log transition
  and reviewed snapshots required by PDF §3.4.

- [x] **Plain2MeTTa v2 deterministic Phase 3 review diff — 2026-08-14:**
  bind the exact current original/elaborated/test versions to deterministic
  original-to-elaborated and test-addition review views; strictly deserialize
  and recompute them so stale, forged, malformed, or expanded reports fail
  closed. Focused tests passed 4/4 and the full provider-free suite passed
  579/579; compileall and diff hygiene passed. The existing query service also
  exposes the recomputed report without artifact bodies or mutation authority. Evidence:
  `experiments/20260814T120352Z-plain2metta-v2-phase3-review-diff/RUN.md`.
  Superseded next step: exact GET route completed above.

- [x] **Persistent Plain2MeTTa v2 implementation worker — launched
  2026-08-07:** implement ProtomegaTron's revised logical-IR design from
  `projects/omegaclaw/workspace/plain2metta-spec-v2-revised-logical-ir.pdf`
  (SHA-256 `10969aabb39d4de057ca06cce151b780c07b381802a079f411814826665b2c4c`)
  in the authoritative public implementation repository, not the deployment
  lane. First milestone: preserve the existing compiler, then add the immutable
  project/artifact/version model, provenance hashes, explicit approval state,
  and invalidation when upstream source changes. Acceptance: focused tests plus
  the full provider-free suite pass; implementation is committed on an isolated
  task branch; `git diff --check` passes; evidence and the next PDF-derived
  milestone are recorded. **Worker correction authorized by Ben 2026-08-14
  00:30 PDT:** the old two-hour isolated cron was discovered spinning on the
  already-completed Monday playground task. Retarget it to the v2 PDF as a
  genuine persistent `openai/gpt-5.6-sol`/high session on a five-minute
  continuation cadence. Each turn must execute as many consecutive safe,
  unblocked acceptance steps as practical and report only evidence-backed
  progress or a real blocker. Next command: create the isolated implementation
  worktree and inspect the current package/API boundaries. Worker cron:
  `31e85b3b-784f-4b80-ab24-43e7167561b8`; session:
  `plain2metta-v2-sol`. Evidence path:
  `projects/specatom-hs/experiments/<run-id>-plain2metta-v2-artifact-model/`.
  **POST transport gate 2026-08-14 03:15 PDT:** added a separate POST-only WSGI
  adapter for project creation, exact artifact-bound annotations, and declared
  approval decisions. Bodies require strict UTF-8 JSON, explicit canonical
  `Content-Length`, a 1 MiB maximum, unique schema fields, canonical paths, and
  no transfer encoding. Focused v2 tests passed 65/65 and the full provider-free
  suite passed 545/545; compileall and repository hygiene checks passed. Next
  command: add optimistic, exact-upstream artifact-submission commands for the
  elaborated-spec and test-spec stages. Evidence:
  `experiments/20260814T101530Z-plain2metta-v2-post-transport-verification/RUN.md`.
  Local implementation commit: `380e543` (not pushed).
  **Exact-upstream submission gate 2026-08-14 03:24 PDT:** added optimistic
  persisted commands and strict POST routes for original-spec → elaborated-spec
  and elaborated-spec → test-spec transitions. Each requires the exact current
  upstream artifact ID and SHA-256; stale, forged, wrong-stage, missing-stage,
  or expanded-schema requests fail without persistence. Focused tests passed
  19/19 and the full provider-free suite passed 549/549; compileall and hygiene
  checks passed. Next command: define a pure elaboration request/response
  protocol carrying provider provenance and validation admission without
  invoking a provider. Evidence:
  `experiments/20260814T102140Z-plain2metta-v2-spec-submission/RUN.md`.
  Local implementation commit: `de832e7` (not pushed).
  **Pure elaboration protocol gate 2026-08-14 03:35 PDT:** added canonical,
  provider-neutral request/response/admission messages bound to exact source
  and request hashes. Provider/model interaction provenance is mandatory;
  marker loss, validation failures, blocking questions, forged admission, and
  malformed/expanded schemas fail closed. The seam does not invoke a provider.
  Focused tests passed 5/5 and the full provider-free suite passed 554/554;
  compileall and hygiene checks passed. Next command: connect the existing
  validation pipeline to an adapter-independent admission service and persist
  the exact admitted outputs plus interaction log atomically. Evidence:
  `experiments/20260814T103000Z-plain2metta-v2-elaboration-protocol/RUN.md`.
  Local implementation commit: `4f070ae` (not pushed).
  **Elaboration admission/persistence gate 2026-08-14 03:54 PDT:** connected
  the existing SpecAtom-HS validator to an adapter-independent response seam.
  Exact admitted returns atomically persist a canonical interaction log,
  elaborated spec, and test spec; stale sources, marker loss, failures,
  blocking questions, rewritten diagnostics, and forged provenance fail
  closed without partial writes. Focused tests passed 9/9 and the full
  provider-free suite passed 558/558; compileall and repository hygiene checks
  passed. Next command: add a narrow request-construction boundary for the
  exact current original spec, still without invoking a provider. Evidence:
  `experiments/20260814T104243Z-plain2metta-v2-elaboration-admission-persistence/RUN.md`.
  Local implementation commit: `273feaa` (not pushed).
  **Exact-current request-construction gate 2026-08-14 04:00 PDT:** added a
  read-only service that loads the exact current original-spec bytes and
  identity and constructs a validated elaboration request with optional
  guidance/section scope. Source replacement yields a different request;
  malformed options fail closed, and the service has no save, provider,
  retry, or execution capability. Focused tests passed 12/12 and the full
  provider-free suite passed 561/561; compileall and hygiene checks passed.
  Next command: define an explicitly configured provider-adapter contract and
  response-import boundary without selecting a vendor or enabling retries.
  Evidence:
  `experiments/20260814T105531Z-plain2metta-v2-elaboration-request-builder/RUN.md`.
  Local implementation commit: `0990f28` (not pushed).
  **Configured adapter-contract gate 2026-08-14 04:14 PDT:** added an injected,
  vendor-neutral `ElaborationBackend` contract plus immutable backend/model/
  temperature/token configuration. The coordinator makes exactly one call,
  checks exact request binding and returned provider provenance, then uses the
  existing atomic validation-admission seam. Stale/misattributed responses,
  malformed configuration, and adapter failures fail without retry or state
  write. Focused tests passed 17/17 and the full provider-free suite passed
  566/566; compileall and hygiene checks passed. Next command: define a strict
  canonical elaboration prompt envelope that carries task constraints and
  response format without provider-specific formatting or automatic retry.
  Evidence:
  `experiments/20260814T110830Z-plain2metta-v2-provider-adapter-contract/RUN.md`.
  Local implementation commit: `fe06c12` (not pushed).
  **Canonical elaboration-prompt gate 2026-08-14 04:25 PDT:** the configured
  adapter now receives an exact request-bound two-message envelope with the
  PDF's reviewable-English, marker-preservation, explicit-question, coverage,
  and dependency constraints plus a provider-independent strict JSON response
  schema. Non-JSON, blank, schema-expanded, prompt-tampered, and misattributed
  completions fail before admission or persistence. Focused tests passed 21/21
  and the full provider-free suite passed 570/570. Next command: add
  gold-standard elaboration fixtures for the existing ML/auth examples and
  validate their requirement-to-test coverage without a paid/provider call.
  Evidence:
  `experiments/20260814T112250Z-plain2metta-v2-elaboration-prompt-envelope/RUN.md`.
  Local implementation commit: `c943558` (not pushed).
  **First acceptance-gate advance 2026-08-14 00:37 PDT:** verified the PDF hash,
  created isolated branch/worktree `agent/plain2metta-v2-logical-ir`, and added
  the pure immutable project/artifact/version model with SHA-256 content
  provenance, approvals bound to exact versions, transitive invalidation after
  source or derived-version changes, and strict fail-closed serialization.
  Focused tests passed 10/10; the unchanged baseline passed 471/471 and the
  post-change provider-free suite passed 481/481; bytecode compilation and
  `git diff --check` passed. Local commit: `713a720` (not pushed). **Second
  acceptance-gate advance 2026-08-14 00:49 PDT:** added atomic filesystem
  persistence with create/get/save/list-status operations, traversal-safe
  project IDs, fully flushed atomic publication, and fail-closed malformed,
  forged, symlink, duplicate, and unexpected-entry handling. Focused tests
  passed 18/18 and the full provider-free suite passed 489/489; compileall and
  `git diff --check` passed. Local commit: `0506f61` (not pushed). **Third
  acceptance-gate advance 2026-08-14 01:04 PDT:** added exact artifact-bound
  general/section/item annotations and the sole `add_logical_ir` transition,
  requiring explicit approvals for both exact current elaborated-spec and
  test-spec versions. Generic creation cannot bypass the gate; approval
  revocation invalidates downstream logical IR; stale, malformed, and forged
  review state fails closed. Focused tests passed 25/25 and the full
  provider-free suite passed 496/496; compileall and `git diff --check` passed.
  Local commit: `1cde4d2` (not pushed).
  Superseded next command: the non-executable logical-IR schema and
  machine-readable critical-finding review report from PDF §3.5 were completed,
  followed by the provider-free Phase 2–7 pipeline. Final acceptance replay at
  isolated revision `51fdefe` passed focused 64/64 and full 651/651 tests; see
  `experiments/20260816T110303Z-plain2metta-v2-acceptance-revalidation/RUN.md`.
  Earlier evidence:
  `experiments/20260814T080406Z-plain2metta-v2-review-gate-verification/RUN.md`.
  **Phase 6 protocol gate 2026-08-14 02:23 PDT:** added a pure canonical
  sandbox request boundary and strict per-test result artifacts bound to the
  exact request digest/current handoff. There remains no host invocation path.
  Focused project tests passed 35/35 and the full provider-free suite passed
  521/521; compileall, diff, credential, large-file, and untracked checks passed.
  Next command: derive a provenance-chain report artifact from test results and
  compiler traceability (PDF §§3.8 and 4.2.7). Evidence:
  `experiments/20260814T091848Z-plain2metta-v2-sandbox-results/RUN.md`.
  **Phase 7 traceability gate 2026-08-14 02:39 PDT:** added a canonical
  full-chain report artifact joining each compiler-declared spec ID to generated
  paths, planned tests, exact sandbox results, pass/fail/skip/untested status,
  and failure detail. Unknown test/spec IDs, incomplete provenance, generic
  creation bypass, and forged report state fail closed. Focused tests passed
  55/55 and the full provider-free suite passed 526/526; compileall and
  repository hygiene checks passed. Next command: expose the narrow read-only
  status/version/trace query service boundary without LLM or execution
  integration. Evidence:
  `experiments/20260814T093310Z-plain2metta-v2-traceability-report/RUN.md`;
  local commit `580ee3b` (not pushed).
  **Read-query boundary gate 2026-08-14 02:46 PDT:** added a storage-agnostic,
  read-only service for project list/status, artifact-version history, full
  trace, and exact spec-ID trace queries. History omits artifact bodies and the
  service has no mutation/execution/provider capability. Traversal IDs, missing
  reports, malformed filters, and unknown spec IDs fail closed. Focused tests
  passed 52/52 and the full provider-free suite passed 530/530; compileall and
  repository hygiene checks passed. Next command: add the minimal read-only
  transport adapter for the corresponding GET routes. Evidence:
  `experiments/20260814T094318Z-plain2metta-v2-read-query-boundary/RUN.md`.
  Local commit `2ae8ec4` (not pushed).
  **Read-transport gate 2026-08-14 02:55 PDT:** added a server-independent
  WSGI adapter exposing only exact GET routes for project list/status, version
  metadata, full trace, and exact spec-ID trace. Non-GET methods, unknown or
  ambiguous query parameters, alternate/encoded project identities, traversal,
  missing state, and unknown routes fail closed; no server, socket, mutation,
  execution, LLM, or provider capability was added. Focused tests passed 8/8
  and the full provider-free suite passed 534/534; py_compile, diff, credential,
  large-file, and untracked-artifact checks passed. Next command: define the
  narrow framework-neutral command service for create/elaborated-review state
  transitions before exposing any POST transport. Evidence:
  `experiments/20260814T095338Z-plain2metta-v2-read-transport-verification/RUN.md`.
  Local commit `7da5a0e` (not pushed).
  **Command-service gate 2026-08-14 03:03 PDT:** added a framework-neutral
  persisted boundary exposing only project creation, exact hash-bound review
  annotations, and declared approval decisions. Malformed or stale commands
  fail before persistence, and no generic artifact/provider/execution method is
  exposed. Focused tests passed 52/52 and the full provider-free suite passed
  540/540. Next command: add a strict bounded-JSON POST adapter for only these
  operations. Evidence:
  `experiments/20260814T100249Z-plain2metta-v2-command-service-verification/RUN.md`.

- [x] **Graduated web-app example suite — completed 2026-08-06:** added five
  readable Plain specifications with increasing complexity to the deployed
  app and publish them with the `webapp` branch. Acceptance: the app's example
  API lists every new file; each file compiles through `POST /api/compile`
  with HTTP 200, zero Fail checks, resolvable JSON and nonempty MeTTa output;
  focused regressions and the full provider-free suite pass; exact results are
  preserved in an experiment record. Next command: inspect the concurrently
  created candidate examples, add a web/API regression, and execute the
  validation ledger. Evidence target:
  `experiments/20260806T*-webapp-example-suite/RUN.md`.
  Result: `01_hello_world` through `05_knowledge_graph` increase from 17 to
  170 compiled objects. All five return HTTP 200 through the Flask test client,
  emit JSON/MeTTa/diagnostics, have zero Fail checks, and have only Pass checks
  for requirement/test coverage. Focused tests passed 2/2; the provider-free
  suite passed 473/473; `git diff --check` passed. A concurrent `webapp`
  commit contained byte-identical candidate files, so the validation commit
  was rebased and fast-forward pushed without overwriting it. Published remote
  commit: `0d4804ff7cd833f01f8bcfcb3e9720778f659c75` on `webapp`. Evidence:
  `experiments/20260806T200134Z-webapp-example-suite/RUN.md`.

- [ ] **Local Plain2Metta web-app deployment — requested 2026-08-06:** deploy
  the published `webapp` branch on the Pop!_OS research laptop as a
  non-public, Tailscale-bound service that Ben can open locally and from his
  Tailscale-connected Mac. Acceptance: the service survives terminal logout;
  `localhost` and the host's Tailscale address return the compiler page; a
  real compile request succeeds; startup/restart instructions and the chosen
  address are recorded. Next command: create an isolated `webapp` worktree
  and virtual environment, then launch and probe the service.
  Progress 2026-08-06: deployed checkout is detached at `6776842`; its `.venv`
  uses Flask 3.1.3. Managed listeners are restricted to `127.0.0.1:8080` and
  `100.72.218.34:8080` (no general-LAN listener). Both returned HTTP 200, and
  the Tailnet endpoint completed a real compile request (`objects=6`,
  Pass=227, Fail=0, Unknown=2, Refusals=76). Current URLs are
  `http://localhost:8080/` and
  `http://pop-os.tail7767ab.ts.net:8080/`. `tailscale ping benjamins-laptop`
  succeeded via DERP. Tailscale Serve HTTPS is disabled by Tailnet admin
  policy. The managed sessions are live, but automatic restart after a host
  reboot remains blocked: the `openclaw` account has no user systemd manager
  and cannot write a crontab/at queue. Evidence/restart commands: `NOTES.md`.
  Correction 2026-08-06: the managed command sessions terminated across the
  agent-turn boundary; port 8080 was no longer listening. The deployment task
  therefore remains open and must not be described as persistent or currently
  live until a host service is installed or the manual runner is restarted.
  Progress 2026-08-06: published verified systemd template commit `ea45993`
  to the non-default `webapp` branch. It runs two hardened, restart-on-failure
  instances bound exactly to `127.0.0.1:8080` and `100.72.218.34:8080`. The
  template passed `systemd-analyze verify`, but installation is blocked because
  this agent's process has Linux `no_new_privileges` and cannot invoke sudo or
  write `/etc/systemd/system`. Ben must run the documented root-owned install
  commands in `repos/plain2metta-webapp/deploy/systemd/README.md`; then verify
  with the two curl commands in that file.

- [x] **Monday playability milestone — due 2026-08-03:** deliver one compact,
  reproducible Plain2Metta “lab bench” that Ben can install and explore after
  the conference. The primary episode must take a small, readable Plain
  specification through source-preserving compilation into bounded JSON,
  reified `.metta`, and a concise diagnostics/explanation report, then execute
  at least one meaningful query or validation through a pinned available
  MeTTa/PeTTa backend (or record a precise backend blocker and provide a
  deterministic semantic reference runner).
  Acceptance:
  (1) fresh-checkout setup plus one command completes locally;
  (2) bundled input and expected semantic results are human-checkable;
  (3) generated default artifacts are bounded to practical interactive size
  and contain no combinatorial check explosion;
  (4) at least one edited-input variant visibly changes the compiled/query
  result, giving Ben something substantive to experiment with;
  (5) focused tests and the full provider-free suite pass at an immutable
  revision;
  (6) a short `PLAYGROUND.md` explains the model, commands, expected output,
  editable knobs, limitations, and exact revision;
  (7) an experiment `RUN.md` records the clean-room command, environment,
  artifact hashes, timings, sizes, exit status, and observed result.
  Scope stop: no new marker families, arity expansion, Unicode/provenance
  edge-case hardening, or broad refactoring unless required by a failure in
  this acceptance path.
  Progress 2026-07-27 16:16 PDT: closed the oldest acceptance gap, default
  output/check explosion, by restricting validation-layer self-checks to the
  obligations and checks present when validation begins. On
  `examples/minimal.plain`, the default run fell from 28,784 checks,
  34,750,366-byte JSON, 12,369,116-byte MeTTa, 7.69 s, and 292,188 KiB max RSS
  to 592 checks, 770,826-byte JSON, 279,923-byte MeTTa, 0.26 s, and 24,524 KiB
  max RSS; diagnostics are 10,889 bytes. A CLI regression pins interactive
  bounds of 1,000 checks, 1 MB JSON, 500 KB MeTTa, and 50 KB diagnostics.
  Focused CLI/validation suite: 89 tests passed; `git diff --check` passed.
  Local implementation commit `d285472`; unpushed.
  Progress 2026-07-27 17:30 PDT: specified and implemented the compact
  task-list episode in `examples/playground/`. The base file deliberately
  leaves `TASK-ARCHIVE` without a covering acceptance test; the edited variant
  adds one line that changes diagnostics `coverage_unknown` from 1 to 0 and
  adds the corresponding reified `CoverageClaim`/`Covers` atoms. Both default
  compilations exit zero. Base/edited artifact sizes are 453,691/551,747-byte
  JSON, 165,333/201,019-byte MeTTa, and 11,006/13,197-byte diagnostics, with
  342/417 Pass and 0/0 Fail checks. A regression pins the semantic delta and
  interactive bounds; the 13-test playground/coverage/CLI suite and
  `git diff --check` pass. Local implementation commit `daa1aa0`; unpushed.
  Next command: inspect and pin an available canonical MeTTa/PeTTa backend and
  execute a meaningful query over the edited episode, or preserve exact
  blocker evidence and implement the deterministic semantic reference runner.
  Progress 2026-07-27 19:30 PDT: pinned the locally available canonical
  Hyperon MeTTa CLI at `0.2.10` and added `scripts/playground-query.sh`.
  The runner rejects any other backend version and joins `CoverageClaim`,
  `Covers`, and `RequirementLabel` atoms to require exactly one
  `TASK-ARCHIVE` coverage pair. The edited episode executed successfully:
  compile exit 0 in 0.23 s/22,880 KiB max RSS; backend exit 0 in
  0.08 s/28,632 KiB max RSS; observed result was the single expected
  test/requirement pair. Installed CLI SHA-256:
  `53455bfb107c7c71eb9686c57a3e4d4c65544102af3b860999e213ab8d9b37af`.
  Focused playground suite: 2 tests passed; `git diff --check` passed. Local
  implementation commit `b4bbfc1`; unpushed.
  Next command: write the one-command clean setup and expected-results guide
  in `repos/specatom-hs/PLAYGROUND.md`, incorporating this pinned query runner.
  Progress 2026-07-27 21:30 PDT: added `PLAYGROUND.md` and
  `scripts/run-playground.sh`. From the repository root, one command creates an
  isolated venv, installs the checkout, compiles the base and edited episodes,
  executes the pinned Hyperon query, and prints the visible diagnostics delta.
  The verified run produced the single pair
  `[(test-783dbd97f4 req-1d0821f07b)]`; base/edited coverage was
  Pass=2/4 and Unknown=1/0. The guide records prerequisites, expected results,
  generated artifacts, editable knobs, bounded-size ceilings, semantic limits,
  backend version, and revision behavior. Focused playground tests: 2 passed;
  `git diff --check` passed.
  Next command: execute the clean-room experiment under
  `experiments/20260803T*-monday-playground/`, recording environment,
  commands, hashes, timings, sizes, status, and observed semantics.
  Evidence target:
  `experiments/20260803T*-monday-playground/RUN.md`,
  `repos/specatom-hs/PLAYGROUND.md`, and a task-specific local commit.
  Completed 2026-07-27 23:30 PDT: the clean-room one-command run at immutable
  repository revision `990ced38ccd2f041bf0599bae6837a33fa6ccaff`
  completed with exit 0 in 3.12 s and 76,184 KiB max RSS. The base/edited
  diagnostics changed archive coverage from Unknown=1 to 0, while pinned
  Hyperon MeTTa 0.2.10 returned exactly one joined acceptance-test/requirement
  pair. All JSON, MeTTa, and diagnostics artifacts remained within the
  documented interactive bounds. Focused playground tests passed 2/2, the
  full provider-free suite passed 471/471, and `git diff --check` passed.
  Clean-room environment, command, hashes, timings, sizes, exit status, and
  observed semantics are recorded in
  `experiments/20260728T063000Z-monday-playground/RUN.md`. The milestone is
  checkpointed by local annotated tag `monday-playground-20260803`.
  Audit 2026-07-28 03:30 PDT: rechecked every preserved artifact against the
  acceptance record. All eight SHA-256 values match; corrected the displayed
  `stdout.log`/`stderr.log` byte counts to the preserved 1,617/909-byte files.
  The immutable tag still resolves to
  `990ced38ccd2f041bf0599bae6837a33fa6ccaff`. The focused playground tests
  passed 2/2, the full provider-free suite passed 471/471, and
  `git diff --check` passed.

- [x] 2026-07-27 15:30 PDT: Added derived `DataFlowEdge` occurrence ground
  truth after all eight non-CR/LF separators recognized by Python
  `splitlines()`. Acceptance: an explicit edge phrase following VT, FF, FS,
  GS, RS, NEL, U+2028, or U+2029 and preceding non-ASCII text slices its exact
  UTF-8 bytes and stays on physical line 2. Evidence:
  `tests/test_specatom_source_indexer.py`; focused 10-test indexer suite and
  full 468-test discovery passed; `git diff --check` passed.
  Local implementation commit `de5a2b6`; unpushed.

- [x] 2026-07-27 13:30 PDT: Added derived concept-occurrence ground truth
  after all eight non-CR/LF separators recognized by Python `splitlines()`.
  Acceptance: a `:Café:` reference following VT, FF, FS, GS, RS, NEL, U+2028,
  or U+2029 slices its exact non-ASCII UTF-8 bytes and stays on physical line
  2. Evidence: `tests/test_specatom_source_indexer.py`; focused 9-test indexer
  suite and full 467-test discovery passed; `git diff --check` passed.
  Local implementation commit `8f9f610`; unpushed.

- [x] 2026-07-27 11:30 PDT: Added derived semantic-occurrence ground truth
  after all eight non-CR/LF separators recognized by Python `splitlines()`.
  Acceptance: an `Evidence:` marker following VT, FF, FS, GS, RS, NEL, U+2028,
  or U+2029 slices its exact non-ASCII UTF-8 bytes and stays on physical line
  2. Evidence: `tests/test_specatom_source_indexer.py`; focused 8-test indexer
  suite and full 466-test discovery passed; `git diff --check` passed.
  Local implementation commit `ba1cadf`; unpushed.

- [x] 2026-07-27 09:30 PDT: Aligned derived semantic/source occurrence spans
  across CR, LF, and CRLF continuation boundaries. Acceptance: an `Evidence:`
  marker on a lone-CR continuation line compiles without alignment failure,
  slices its exact non-ASCII UTF-8 source bytes, and reports physical line 3.
  Evidence: `src/specatom_hs/source_indexer.py`,
  `src/specatom_hs/passes.py`, and
  `tests/test_specatom_source_indexer.py`; focused 7-test indexer suite,
  168 semantic/information-flow tests, and full 465-test discovery passed;
  `git diff --check` passed. Local implementation commit `64f53cc`; unpushed.

- [x] 2026-07-27 07:30 PDT: Generalized physical-line ground truth across all
  eight non-CR/LF separators recognized by Python `splitlines()`: VT, FF, FS,
  GS, RS, NEL, U+2028, and U+2029. Acceptance: each separator remains literal
  first-item content and exact UTF-8 provenance, while the following item
  remains on physical line 3. Evidence:
  `tests/test_specatom_source_indexer.py`; focused 6-test indexer suite and
  full 464-test stdlib discovery passed; `git diff --check` passed. Local
  implementation commit `7e5befd`; unpushed.

- [x] 2026-07-27 05:30 PDT: Aligned source record splitting with the documented
  CR/LF/CRLF line-number model instead of Python's broader Unicode
  `splitlines()` behavior. Acceptance: U+2028 remains inside one item's text
  and exact UTF-8 span while the following item starts on physical line 3.
  Evidence: `src/specatom_hs/source_indexer.py` and
  `tests/test_specatom_source_indexer.py`; focused 6-test indexer suite and
  full 464-test stdlib discovery passed; `git diff --check` passed.

- [x] 2026-07-27 03:30 PDT: Made source line indexing recognize LF, CRLF, and
  lone-CR boundaries while preserving UTF-8 byte offsets. Acceptance: one
  mixed-newline fixture reports section/item start lines 1--4, slices every
  exact record span from the encoded source, and counts CRLF only once.
  Evidence: `src/specatom_hs/source_indexer.py` and
  `tests/test_specatom_source_indexer.py`; focused 5-test indexer suite and
  full 463-test stdlib discovery passed; `git diff --check` passed.
  Local implementation commit `4b28d16`; unpushed.

- [x] 2026-07-27 01:30 PDT: Made first-heading recognition compatible with a
  UTF-8 BOM without altering source provenance. Acceptance: a BOM-bearing
  `***definitions***` heading is indexed, its exact byte span retains the
  three-byte BOM, and the following item span slices the original encoded
  source at the correct byte offsets. Evidence:
  `src/specatom_hs/source_indexer.py` and
  `tests/test_specatom_source_indexer.py`; exact 4-test indexer suite and
  90-test source/concept/semantic-object suite passed, as did
  `git diff --check`. Local implementation commit `ac841f8`; unpushed.

- [x] 2026-07-26 13:30 PDT: Corrected source provenance offsets to use
  actual UTF-8 byte positions rather than Python character indexes.
  Acceptance: a non-ASCII heading and `:Café:` marker round-trip from emitted
  section, item, concept-occurrence, and semantic `Evidence:` spans by slicing
  the original encoded bytes; source-span validation uses encoded file length
  and byte-relative line counting. Evidence: `src/specatom_hs/source_indexer.py`,
  `src/specatom_hs/passes.py`, `src/specatom_hs/validators.py`, and
  `tests/test_specatom_source_indexer.py`; focused 193-test
  source/validation/backend suite passed, as did the 65-test
  source/concept/semantic-object suite and `git diff --check`. Local
  implementation commit `e861052`; unpushed.

- [x] 2026-07-26: Complete the v0.1 usability gate: publish install metadata,
  install the CLI into a fresh virtual environment, and compile three realistic
  specifications through JSON/MeTTa/diagnostics output. Acceptance: all three
  runs exit zero and preserve nonempty outputs plus SHA-256 summary data.
  Evidence: `repos/specatom-hs/setup.py`,
  `repos/specatom-hs/scripts/usability-gate.sh`, and
  `experiments/20260726T185730Z-v01-three-spec-install-report/`; durable output
  digest summary in that run's `artifacts/summary.json`. Scope remains the
  frozen conservative profile.

- [x] 2026-07-26 09:30 PDT: Centralized canonical object-scoped validation
  subtarget checks shared by crisp validation and PeTTa/diagnostics admission.
  Acceptance: one ground-truth corpus covers canonical ASCII/NFC identities
  plus empty, padded, format, control, surrogate, noncharacter, private-use,
  unassigned, non-NFC, non-NFKC, variation-selector, and combining-mark
  refusals; validator/backend behavior remains unchanged. Evidence:
  `src/specatom_hs/identities.py`,
  `src/specatom_hs/validators.py`,
  `src/specatom_hs/backends/petta.py`, and
  `tests/test_specatom_identities.py`; focused 191-test suite and full
  460-test discovery passed; `git diff --check` passed.
  Local implementation commit `ce1e9cd`; unpushed.

- [x] 2026-07-26 07:30 PDT: Closed Unicode combining-mark ambiguity for
  object-scoped validation subtargets. Acceptance:
  `object:child:fact<U+0338>:0` fails crisp declaration validation, is refused
  by the PeTTa profile, and cannot contribute linked evidence to diagnostics;
  the unmodified neighbor `object:child:fact:0` remains emitted and counted.
  Evidence: `src/specatom_hs/validators.py`,
  `src/specatom_hs/backends/petta.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression and
  full 459-test discovery passed; `git diff --check` passed.
  Local implementation commit `f06254a`; unpushed.

- [x] 2026-07-26 05:30 PDT: Closed Unicode variation-selector ambiguity for
  object-scoped validation subtargets. Acceptance:
  `object:child:fact<U+FE0F>:0` fails crisp declaration validation, is refused
  by the PeTTa profile, and cannot contribute linked evidence to diagnostics;
  the unmodified neighbor `object:child:fact:0` remains emitted and counted.
  Evidence: `src/specatom_hs/validators.py`,
  `src/specatom_hs/backends/petta.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression and
  full 457-test discovery passed; `git diff --check` passed.
  Local implementation commit `85e5fff`; unpushed.

- [x] 2026-07-26 03:30 PDT: Closed Unicode compatibility-normalization
  ambiguity for object-scoped validation subtargets. Acceptance:
  `object:child:<FULLWIDTH f>act:0` fails crisp declaration validation, is
  refused by the PeTTa profile, and cannot contribute linked evidence to
  diagnostics; its NFKC neighbor `object:child:fact:0` remains emitted and
  counted. Evidence: local implementation commit `63d2667`,
  `src/specatom_hs/validators.py`,
  `src/specatom_hs/backends/petta.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression, 212
  relevant validation/backend/diagnostics tests, and full 455-test discovery
  passed; `git diff --check` passed.

- [x] 2026-07-26 01:30 PDT: Closed canonical Unicode normalization ambiguity
  for object-scoped validation subtargets. Acceptance: decomposed
  `object:child:cafe<U+0301>` fails crisp declaration validation, is refused
  by the PeTTa profile, and cannot contribute linked evidence to diagnostics;
  its NFC neighbor `object:child:caf<U+00E9>` remains emitted and counted.
  Evidence: local implementation commit `a881927`,
  `src/specatom_hs/validators.py`,
  `src/specatom_hs/backends/petta.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression, 210
  relevant validation/backend/diagnostics tests, and full 453-test discovery
  passed; `git diff --check` passed.

- [x] 2026-07-25 23:30 PDT: Closed unassigned Unicode handling for
  object-scoped validation subtargets. Acceptance:
  `object:child:fact:<U+0378>0` fails crisp declaration validation, is refused
  by the PeTTa profile, and cannot contribute linked check evidence to
  diagnostics; a canonical neighboring target remains emitted and counted.
  Evidence: local repository commit `0018fe6`,
  `src/specatom_hs/validators.py`,
  `src/specatom_hs/backends/petta.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression and
  208 relevant validation/backend/diagnostics tests passed; `git diff --check`
  passed.

- [x] 2026-07-25 21:30 PDT: Closed Unicode private-use handling for
  object-scoped validation subtargets. Acceptance:
  `object:child:fact:<U+E000>0` fails crisp declaration validation, is refused
  by the PeTTa profile, and cannot contribute linked check evidence to
  diagnostics; a canonical neighboring target remains emitted and counted.
  Evidence: local repository commit `3372def`,
  `src/specatom_hs/validators.py`,
  `src/specatom_hs/backends/petta.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression and
  180 relevant validation/backend tests passed; `git diff --check` passed.

- [x] 2026-07-25 19:30 PDT: Closed reserved Unicode noncharacter handling for
  object-scoped validation subtargets. Acceptance:
  `object:child:fact:<U+FDD0>0` fails crisp declaration validation, is refused
  by the PeTTa profile, and cannot contribute linked check evidence to
  diagnostics; a canonical neighboring target remains emitted and counted.
  Evidence: local repository commit `f069218`,
  `src/specatom_hs/validators.py`,
  `src/specatom_hs/backends/petta.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression,
  178 relevant validation/backend tests in 2.519s, all 447 tests in 511.660s,
  and `git diff --check` passed.

- [x] 2026-07-25 17:30 PDT: Closed non-scalar Unicode surrogate handling for
  object-scoped validation subtargets. Acceptance:
  `object:child:fact:<LONE HIGH SURROGATE>0` produces a crisp declaration
  failure instead of a `UnicodeEncodeError`, is refused by the PeTTa profile,
  and cannot contribute linked check evidence to diagnostics; a canonical
  neighboring target remains emitted and counted. Evidence:
  local repository commit `a02074d`,
  `src/specatom_hs/schema.py`, `src/specatom_hs/backends/petta.py`,
  `src/specatom_hs/validators.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression,
  176 relevant validation/backend tests in 5.512s, all 445 tests in 714.128s,
  and `git diff --check` passed.

- [x] 2026-07-25 15:30 PDT: Closed invisible Unicode control-character
  evasion for object-scoped validation subtargets. Acceptance:
  `object:child:fact:<BELL>0` fails crisp declaration validation, is refused by
  the PeTTa profile, and cannot contribute linked check evidence to
  diagnostics; a canonical neighboring target remains emitted and counted.
  Evidence: local repository commit `24c8f10`,
  `src/specatom_hs/backends/petta.py`,
  `src/specatom_hs/validators.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression, all
  443 tests in 501.447s, and `git diff --check` passed.

- [x] 2026-07-25 13:30 PDT: Closed interior invisible Unicode format-character
  evasion for object-scoped validation subtargets. Acceptance:
  `object:child:fact:<ZERO WIDTH SPACE>0` fails crisp declaration validation,
  is refused by the PeTTa profile, and cannot contribute linked check evidence
  to diagnostics; a canonical neighboring target remains emitted and counted.
  Evidence: local repository commit `f4b1fcf`,
  `src/specatom_hs/backends/petta.py`,
  `src/specatom_hs/validators.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression,
  172 relevant validation/backend tests in 2.372s, all 441 tests in 451.797s,
  and `git diff --check` passed.

- [x] 2026-07-25 11:30 PDT: Closed trailing invisible Unicode format-padding
  evasion for object-scoped validation subtargets. Acceptance:
  `object:child:fact:0<ZERO WIDTH SPACE>` fails crisp declaration validation,
  is refused by the PeTTa profile, and cannot contribute linked check evidence
  to diagnostics; a canonical neighboring target remains emitted and counted.
  Evidence: local repository commit `7c20c9f`,
  `src/specatom_hs/backends/petta.py`,
  `src/specatom_hs/validators.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression, all
  439 tests in 439.928s, and `git diff --check` passed.

- [x] 2026-07-25 09:30 PDT: Added end-to-end regression coverage for invisible
  Unicode format padding immediately before an object-subtarget separator.
  Acceptance: `object:child<ZERO WIDTH SPACE>:fact:0` fails crisp declaration
  validation, is refused by the PeTTa profile, and cannot contribute linked
  check evidence to diagnostics; a canonical neighboring target remains
  emitted and counted. Evidence: local repository commit `154952a`,
  `tests/test_specatom_validation_records.py` and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression, all
  437 tests in 473.121s, and `git diff --check` passed.

- [x] 2026-07-25 07:30 PDT: Closed invisible Unicode format-padding evasion
  immediately after an object-subtarget separator. Acceptance:
  `object:child:<ZERO WIDTH SPACE>fact:0` fails crisp declaration validation,
  is refused by the PeTTa profile, and cannot contribute linked check evidence
  to diagnostics; a canonical neighboring target remains emitted and counted.
  Evidence: local repository commit `88bfee9`,
  `src/specatom_hs/backends/petta.py`,
  `src/specatom_hs/validators.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression,
  166 relevant validation/backend tests in 2.210s, all 435 tests in 436.308s,
  and `git diff --check` passed.

- [x] 2026-07-25 05:30 PDT: Added end-to-end regression coverage for Unicode
  whitespace immediately after an object-subtarget separator. Acceptance:
  `object:child:<EM SPACE>fact:0` fails crisp declaration validation, is
  refused by the PeTTa profile, and cannot contribute linked check evidence to
  diagnostics; a canonical neighboring target remains emitted and counted.
  Evidence: local repository commit `10f9279`,
  `tests/test_specatom_validation_records.py` and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression,
  190 relevant validation/backend/diagnostics tests, all 433 tests in
  437.845s, and `git diff --check` passed.

- [x] 2026-07-25 03:30 PDT: Closed Unicode-whitespace pre-separator evasion
  for object-scoped validation targets. Acceptance:
  `object:child<NBSP>:fact:0` fails crisp declaration validation, is refused by
  the PeTTa profile, and cannot contribute linked check evidence to
  diagnostics; a canonical neighboring target remains emitted and counted.
  Evidence: local repository commit `691a313`,
  `src/specatom_hs/backends/petta.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 3-test regression,
  162 relevant tests in 2.304s, all 431 tests in 459.985s, and
  `git diff --check` passed.

- [x] 2026-07-25 01:30 PDT: Closed pre-separator whitespace evasion for
  object-scoped validation targets. Acceptance: `object:child :fact:0` fails
  crisp declaration validation, is refused by the PeTTa profile, and cannot
  contribute linked check evidence to diagnostics; a canonical neighboring
  target remains emitted and counted. Evidence:
  local repository commit `0c27586`,
  `src/specatom_hs/backends/petta.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`; exact 2-test regression,
  186 relevant tests, all 429 tests in 445.495s, and `git diff --check`
  passed.

- [x] 2026-07-24 23:30 PDT: Closed leading-padding evasion for object-scoped
  validation targets. Acceptance: a target such as
  ` object:child:fact:0` fails crisp declaration validation, is refused by the
  PeTTa profile with the padded-subtarget reason, and cannot affect
  diagnostics; valid unpadded neighbors remain supported. Evidence:
  local repository commit `9a4a7b7`,
  `src/specatom_hs/backends/petta.py`,
  `tests/test_specatom_validation_records.py`, and
  `tests/test_specatom_petta_profile_gates.py`.

- [x] 2026-07-24 21:30 PDT: Closed padded object-subtarget ambiguity.
  Targets such as `object:child: fact:0 ` now fail crisp declaration
  validation; PeTTa export suppresses the obligation and linked checks with an
  exact padded-subtarget refusal; diagnostics cannot count or render their
  evidence. Three focused regressions, 182 relevant
  validation/backend/diagnostics tests, all 425 tests in 443.066s, and
  `git diff --check` passed. Local implementation commit `408a9a1`; unpushed.

- [x] 2026-07-24 19:30 PDT: Closed the whitespace-only object-subtarget gap.
  Targets such as `object:child:   ` now fail crisp declaration validation;
  PeTTa export suppresses the obligation and linked checks with the same exact
  empty-subtarget refusal; diagnostics cannot count or render their evidence.
  Three focused regressions, 179 relevant validation/backend/diagnostics tests,
  all 422 tests in 398.208s, and `git diff --check` passed. Local
  implementation commit `413ff7c`; unpushed.

- [x] 2026-07-24 17:30 PDT: Aligned PeTTa export and diagnostics with crisp
  rejection of empty object-scoped validation subtargets. An obligation
  targeting `object:child:` is now suppressed with an exact refusal, its
  linked checks cannot affect summaries or reports, and the valid semantic
  object still emits. Three focused regressions, 110 backend/diagnostics tests,
  all 419 tests in 387.104s, and `git diff --check` passed. Local
  implementation commit `8c5b8ff`; unpushed.

- [x] 2026-07-24 15:30 PDT: Tightened object-scoped validation-target
  declaration so a trailing separator without a subtarget, such as
  `object:child:`, fails closed while a real colon-bearing subtarget remains
  accepted. Exact positive/negative regressions passed; the concurrently
  started baseline discovery passed all prior 416 tests in 380.585s; and
  `git diff --check` passed. Local implementation commit `96df4e9`; unpushed.

- [x] 2026-07-24 13:30 PDT: Aligned crisp validation-target declaration with
  colon-bearing semantic object IDs. Object-scoped targets such as
  `object:child:fact:0` now resolve against the complete declared object ID
  instead of splitting at the first colon and producing a false Fail. Exact
  regression, all 64 validation-record tests, all 416 tests in 397.943s, and
  `git diff --check` passed. Local implementation commit `452dc5a`; unpushed.

- [x] 2026-07-24 11:30 PDT: Made validation-target ownership robust for
  colon-bearing/nested semantic object IDs. The exporter and diagnostics now
  resolve the longest exact or object-scoped declared ID, preventing an
  emitted parent from masking a refused child target. Two focused regressions,
  109 backend/diagnostics tests, all 415 tests in 467.788s, and
  `git diff --check` passed. Local implementation commit `2e0b6cd`; unpushed.

- [x] 2026-07-24 09:30 PDT: Made validation-obligation object targets fail
  closed with semantic-object emission. An obligation targeting an exact or
  object-scoped subtarget of a refused semantic object is now suppressed with
  its linked checks; diagnostics exclude those checks, while valid neighboring
  object targets remain admitted. Updated end-to-end summary ground truth to
  compare against admitted diagnostics. Three focused regressions, all 413
  tests in 354.107s, and `git diff --check` passed. Local implementation
  commit `417ac22`; unpushed.

- [x] 2026-07-24 07:30 PDT: Made PeTTa validation-obligation provenance fail
  closed before semantic emission. Malformed, blank, missing, or otherwise
  non-emitted source-span references now suppress the obligation atom,
  rationale, and linked checks while retaining exact backend refusal evidence;
  valid neighboring obligations/checks remain admitted. Five focused
  profile/diagnostics regressions, all 411 tests in 331.462s, and
  `git diff --check` passed. Local implementation commit `9ef608b`; unpushed.

- [x] 2026-07-24 05:30 PDT: Made PeTTa semantic-object provenance fail closed
  for explicit malformed values. Non-string and whitespace-only source-span
  IDs now suppress the whole object and its facts instead of emitting
  provenance-free semantics beside a refusal; diagnostics preserve the same
  admission contract and valid neighbors still emit/report. Three focused
  profile/diagnostics tests, all 411 tests in 338.446s, and
  `git diff --check` passed. Local implementation commit `ef8de39`; unpushed.

- [x] 2026-07-24 03:30 PDT: Aligned diagnostics semantic-object admission with
  the PeTTa runtime-role gate. A string lookalike `"ConceptObject"` can no
  longer inflate defined-concept counts through an otherwise valid
  `ConceptStatus` fact after export refuses the object and facts. Exact
  atom/summary ground truth, all 20 diagnostics tests, all 410 tests in
  319.673s, and `git diff --check` passed. Local implementation commit
  `def18d0`; unpushed.

- [x] 2026-07-24 01:30 PDT: Made explicit object provenance fail closed across
  PeTTa export and diagnostics. Objects citing missing/refused manifest spans
  now suppress the object atom and facts rather than degrading into
  provenance-free semantic claims; their question text is excluded from
  diagnostics while a valid neighbor remains admitted. Focused backend and
  diagnostics suites passed 104 tests; full discovery passed 410 tests in
  335.528s; `git diff --check` passed. Local implementation commit `2928bb8`;
  unpushed.

- [x] 2026-07-23 23:30 PDT: Aligned diagnostics obligation provenance with
  PeTTa source-manifest admission. A check linked to an obligation citing a
  scalar-safe but non-emitted span is excluded from summary/report counts while
  backend refusal evidence remains visible and a valid neighboring Pass is
  admitted. Exact regression and all 409 tests passed; `git diff --check`
  passed. Local implementation commit `c24012d`; unpushed.

- [x] 2026-07-23 21:30 PDT: Aligned diagnostics check admission with the
  PeTTa validation-obligation source-provenance scalar gate. Checks linked to
  obligations with structured or blank source-span identities no longer
  contribute summary/coverage counts or detailed failure output; exact backend
  refusal evidence remains visible and a valid neighboring Pass is preserved.
  Focused diagnostics passed 18 tests in 71.155s; full discovery passed 408
  tests in 338.934s; `git diff --check` passed. Local implementation commit
  `c098b80`; unpushed.

- [x] 2026-07-23 19:30 PDT: Aligned diagnostics check admission with PeTTa
  validation-obligation linkage gates. Orphan checks, checks linked to refused
  obligations, and checks whose property or target disagrees with the emitted
  obligation no longer contribute summary/coverage counts or detailed failure
  output; exact backend refusals remain visible and a valid neighboring Pass
  is preserved. Focused diagnostics passed 17 tests in 67.564s; full discovery
  passed 407 tests in 340.673s; `git diff --check` passed. Local implementation
  commit `eb82952`; unpushed.

- [x] 2026-07-23 15:30 PDT: Aligned diagnostics check admission with PeTTa
  validation-layer identity gates. Blank, structured, and duplicate check IDs
  no longer contribute Pass/Fail/Unknown or per-property summaries and cannot
  leak failure evidence into Markdown; exact backend refusals remain visible
  and a valid neighboring Pass is preserved. Focused diagnostics passed 15
  tests in 75.865s; full discovery passed 405 tests in 343.895s;
  `git diff --check` passed. Local implementation commit `5a9f028`; unpushed.

- [x] 2026-07-23 13:30 PDT: Aligned diagnostics semantic object admission with
  the PeTTa reified facts-container gate. Objects with malformed `None` facts
  containers no longer contribute semantic question counts, while exact crisp
  validation and backend refusal evidence remain visible and a valid
  neighboring question is still reported. Focused diagnostics passed 14
  tests in 66.398s; full discovery passed 404 tests in 329.188s;
  `git diff --check` passed. Local implementation commit `0cb5f34`; unpushed.

- [x] 2026-07-23 11:30 PDT: Aligned diagnostics semantic object admission with
  the PeTTa reified semantic-level gate. `RawTextOnly` and malformed level
  objects no longer contribute question/concept/acceptance-test summaries or
  question report text; exact refused/valid neighboring ground truth preserves
  backend refusal evidence. Focused diagnostics passed 14 tests; full discovery
  passed 404 tests in 538.467s; `git diff --check` passed. Local implementation
  commit `84d66a7`; unpushed.

- [x] 2026-07-23 09:30 PDT: Aligned diagnostics semantic object admission with
  PeTTa identity gates. Blank, structured, and duplicate SpecObject IDs no
  longer contribute question/concept/acceptance-test summaries or question
  report text; exact malformed/valid neighboring ground truth preserves crisp
  failures and backend refusals. Focused regression, all 403 tests, and
  `git diff --check` passed. Local commit `dec79c7`; unpushed.

- [x] 2026-07-23 07:30 PDT: Aligned diagnostics semantic fact consumption
  with exact fact-arity validation. Four-argument `ConceptStatus`, `TestKind`,
  and `QuestionText` facts no longer inflate concept/acceptance-test summaries
  or leak question text; exact validation/backend refusal evidence and a valid
  neighboring question remain visible. Focused diagnostics passed 12 tests;
  full discovery passed 402 tests in 336.205s; `git diff --check` passed.
  Local implementation commit `23b5b97`; unpushed.

- [x] 2026-07-23 05:30 PDT: Aligned diagnostics semantic fact consumption
  with object-subject validation. Mismatched `ConceptStatus`, `TestKind`, and
  `QuestionText` subjects no longer inflate concept/acceptance-test summaries
  or leak question text; exact validation/backend refusal evidence and a valid
  neighboring question remain visible. Focused regression passed; full
  discovery passed 401 tests in 334.777s; `git diff --check` passed. Local
  implementation commit `8b4bbf2`; unpushed.

- [x] 2026-07-23 03:30 PDT: Hardened question validation and diagnostics
  against structured `QuestionText` and `Blocks` fact values. List-backed
  values now produce exact backend-safe fact failures, cannot be credited as
  reviewable text or obligation links, and cannot crash membership lookup;
  malformed question text is omitted from reports while a valid neighboring
  question remains visible. Focused diagnostics passed 10 tests; full
  discovery passed 400 tests in 326.010s; `git diff --check` passed; local
  implementation commit `ec15952`.

- [x] 2026-07-23 01:30 PDT: Hardened diagnostics semantic summaries against
  undeclared string object roles. Enum-value string lookalikes no longer
  inflate question, requirement, or acceptance-test counts or leak malformed
  question text; backend refusals remain visible and a valid neighboring
  question remains reported. Focused diagnostics passed 9 tests; full
  discovery passed 399 tests in 320.650s; `git diff --check` passed; local
  implementation commit `1e14790`.

- [x] 2026-07-22 23:30 PDT: Hardened diagnostics concept summaries against
  structured `ConceptStatus` fact values. A list-backed status now remains
  excluded from concept counts while its crisp Fail and PeTTa refusal remain
  visible; a valid neighboring `defined` concept is still counted. Focused
  regression passed; full discovery passed 398 tests in 327.632s;
  `git diff --check` passed; local implementation commit `caf278d`.

- [x] 2026-07-22 21:30 PDT: Tightened diagnostics status classification so
  only declared `CheckStatus.PASS`/`FAIL` enum members receive those counts.
  A malformed string `"Pass"` now remains Unknown and its existing backend
  refusal is reported. Focused diagnostics passed 7 tests; full discovery
  passed 397 tests in 335.928s; `git diff --check` passed; local implementation
  commit `682bb81`.

- [x] 2026-07-22 19:30 PDT: Hardened diagnostics summary/report traversal
  against malformed `CheckRecord` status and property fields. Ground truth
  confirms structured statuses become Unknown, unhashable properties receive
  a stable invalid-property bucket, backend refusal evidence remains visible,
  and a valid neighboring Pass is preserved. Focused diagnostics suite passed
  7 tests; full discovery passed 397 tests in 334.403s; `git diff --check`
  passed; local implementation commit `396983c`.

- [x] 2026-07-22 17:30 PDT: Hardened diagnostics summary/report traversal
  against malformed `SpecObject`/`CheckRecord` entries, malformed facts
  containers, and non-tuple facts. Ground truth confirms malformed entries do
  not crash reporting, backend refusals remain visible, and valid neighboring
  `QuestionText` is preserved. Focused diagnostics suite passed 6 tests; full
  discovery passed 396 tests in 337.348s; `git diff --check` passed; local
  implementation commit `741a9a4`.

- [x] 2026-07-22 15:30 PDT: Hardened question review and edge-provenance
  traversal against malformed non-tuple facts. Exact ground truth shows
  `None`/integer facts Fail through `fact-has-supported-arity` without
  crashing, while valid neighboring `QuestionText`/`Blocks` facts Pass.
  Focused validation/profile suites passed 147 tests; full discovery passed
  395 tests; `git diff --check` passed; local implementation commit `ed6356f`.

- [x] 2026-07-22 13:30 PDT: Added `check-has-valid-record-type` crisp
  validation matching the PeTTa backend's malformed `CheckRecord` refusal.
  `None` and list entries Fail exactly and are excluded from check indexes and
  validation traversal, while a valid neighboring record Passes. Focused
  146-test validation/profile suites, full 394-test unittest discovery, and
  `git diff --check` passed; local implementation commit `ff89ce0`.

- [x] 2026-07-22 11:30 PDT: Added
  `validation-obligation-has-valid-record-type` crisp validation matching the
  PeTTa backend's malformed `ValidationObligation` refusal. `None` and list
  entries Fail exactly and are excluded from obligation indexes/traversal,
  while a valid neighboring record Passes. Focused 145-test validation/profile
  suites, full 393-test unittest discovery, and `git diff --check` passed; local
  implementation commit `2519085`.

- [x] 2026-07-22: Added `object-has-valid-facts-container` validation and a
  matching PeTTa refusal so `None`/mapping fact containers cannot crash graph,
  provenance, question, fact, or export traversal or yield a partial object;
  malformed/valid-neighbor ground truth passes. Focused suites: 144 tests;
  full discovery: 392 tests in 314.566s; `git diff --check` passed; local commit
  `8897d50`.

- [x] 2026-07-22 07:30 PDT: Added `object-has-valid-record-type` validation
  plus matching PeTTa refusal for malformed `SpecObject` entries. Malformed
  neighbors Fail/refuse exactly; a valid neighbor Passes and exports. Focused
  2-test regression, full 390-test discovery, and `git diff --check` pass;
  local implementation commit `dc700a3`.

- [x] 2026-07-22 03:30 PDT: Added `section-has-valid-record-type` crisp
  validation matching the PeTTa backend's malformed `Section` refusal gate.
  `None` and list entries now Fail exactly and are excluded from section
  identity, provenance, and validation-target indexes, while a valid
  neighboring record Passes. Focused 57-test validation suite, full 387-test
  unittest discovery, and `git diff --check` pass; local implementation commit
  `d36d5a4`.

- [x] 2026-07-22 01:30 PDT: Added `source-span-has-valid-record-type`
  crisp validation matching the PeTTa backend's malformed `SourceSpan` refusal
  gate. `None` and list entries now Fail exactly and are excluded from span
  identity, provenance, and edge indexes, while a valid neighboring record
  Passes. Focused 56-test validation suite, full 386-test unittest discovery,
  and `git diff --check` pass; local implementation commit `b43e109`.

- [x] 2026-07-21 23:30 PDT: Added `plain-file-has-valid-record-type` crisp
  validation matching the PeTTa backend's malformed `PlainFile` refusal gate.
  `None` and list entries now Fail exactly and are excluded from downstream
  file indexes/provenance checks, while a valid neighboring record Passes.
  Focused 55-test validation suite, full 385-test unittest discovery, and
  `git diff --check` pass; local implementation commit `826f8f2`.

- [x] 2026-07-21: Added `source-span-has-safe-file-identity` crisp validation
  matching the PeTTa backend's non-blank string gate; malformed `None`, list,
  and blank file links now Fail before unsafe lookup, with valid-neighbor ground
  truth; focused 54-test suite and full 384-test suite pass.

- [x] 2026-07-21 19:30 PDT: Added `item-has-safe-source-span` crisp
  validation matching the PeTTa backend's concrete PlainItem SourceSpan and
  non-blank span-identity gate. `None`, list, and blank-identity spans now Fail
  exactly before dereference; a valid neighboring item Passes. Focused 53-test
  validation suite, full 383-test unittest discovery, and `git diff --check`
  pass; local implementation commit `ea3e391`.

- [x] 2026-07-21: Added backend-safe Section source-span validation matching
  the PeTTa export gate: malformed record types and blank span identities Fail
  before dereference, with exact malformed/valid neighboring ground truth; 382
  tests pass.

- [x] 2026-07-21 15:30 PDT: Added `section-has-safe-file-identity` crisp
  validation matching the PeTTa backend's non-blank Section file-link gate.
  List and blank links now Fail exactly and stop before unsafe index
  membership; a valid neighboring section Passes. Focused regression, full
  381-test unittest discovery, and `git diff --check` pass; local implementation
  commit `de721c8`.

- [x] 2026-07-21 13:30 PDT: Added `item-has-safe-link-identities` crisp
  validation matching the PeTTa backend's non-blank file/section and
  absent-or-non-blank parent identity gates. List and blank links now Fail
  exactly and stop before unsafe index membership; a valid neighboring item
  Passes. Focused 50-test validation suite, full 380-test unittest discovery,
  and `git diff --check` pass; local implementation commit `17a9c7d`.

- [x] 2026-07-21 11:30 PDT: Added backend-safe PlainItem nesting-level
  validation in both crisp checks and PeTTa source-manifest export. Boolean and
  negative levels now Fail/refuse with exact diagnostics while a valid neighbor
  Passes. Focused regressions, full 379-test unittest discovery, and
  `git diff --check` pass; local implementation commit `517c081`.

- [x] 2026-07-21 09:30 PDT: Added `item-has-safe-fields` crisp validation
  matching the PeTTa backend's non-negative, non-boolean ordinal and non-blank
  raw-text gates. Exact ground truth rejects boolean/negative ordinals plus
  list/blank raw text while accepting a valid neighboring item. Focused
  49-test validation suite, full 379-test unittest discovery, and
  `git diff --check` pass; local implementation commit `805783e`.

- [x] 2026-07-21 07:30 PDT: Added `section-has-safe-fields` crisp validation
  matching the PeTTa backend's non-blank kind and non-negative, non-boolean
  ordinal gates. Exact ground truth rejects list/blank kinds plus boolean and
  negative ordinals while accepting a valid neighboring section. Focused
  48-test validation suite, full 378-test unittest discovery, and
  `git diff --check` pass; local implementation commit `f9a9455`.

- [x] 2026-07-21 05:30 PDT: Added `plain-file-has-safe-fields` crisp
  validation for non-blank string paths/digests and string preserved source
  text. Exact ground truth rejects `None`, list, and blank fields without
  crashing digest recomputation while accepting a valid neighboring file.
  Focused 47-test validation suite, full 377-test unittest discovery, and
  `git diff --check` pass; local implementation commit `ed7a3d8`.

- [x] 2026-07-21 03:30 PDT: Added `source-span-has-safe-bounds` crisp
  validation matching the PeTTa backend's non-boolean integer and bound-order
  gates. Exact ground truth rejects list, boolean, `None`, and reversed bounds
  without numeric-comparison crashes while accepting a valid neighboring span.
  Focused 46-test validation suite, full 376-test unittest discovery, and
  `git diff --check` pass; local implementation commit `0b826ac`.

- [x] 2026-07-21 01:30 PDT: Added
  `object-has-safe-source-span-id` crisp validation, matching the PeTTa backend
  provenance identity gate and preventing unhashable malformed provenance from
  crashing the source-or-generated check. Exact ground truth accepts absent
  optional provenance and a non-blank string identity while rejecting list and
  blank identities. Focused 45-test validation suite, full 375-test unittest
  discovery, and `git diff --check` pass; local implementation commit
  `07110cb`.

- [x] 2026-07-20 23:30 PDT: Added
  `validation-obligation-has-safe-source-span-id` crisp validation, matching
  the PeTTa backend provenance identity gate. Exact ground truth accepts absent
  optional provenance and a non-blank string identity while rejecting list and
  blank identities. Focused regression, full 374-test unittest discovery, and
  `git diff --check` pass; local implementation commit `ac96423`.

- [x] 2026-07-20 19:30 PDT: Added `check-has-safe-target` crisp validation,
  matching the PeTTa backend's check-target identity gate. Exact ground truth
  rejects `None`, list, and blank target IDs while accepting a valid non-blank
  target. Focused regression, full 371-test unittest discovery, and
  `git diff --check` pass; local implementation commit `da432ff`.

- [x] 2026-07-20 15:30 PDT: Added
  `check-has-safe-obligation-id` crisp validation, matching the PeTTa backend's
  check-obligation identity gate. Exact ground truth rejects `None`, list, and
  blank obligation IDs without unsafe dictionary membership while accepting a
  valid non-blank link. Focused regression, full 370-test unittest discovery,
  and `git diff --check` pass; local implementation commit `7a73b32`.

- [x] 2026-07-20 13:30 PDT: Added
  `validation-obligation-has-safe-target` crisp validation, matching the PeTTa
  backend's target-identity gate. Exact ground truth rejects `None`, list, and
  blank targets while accepting non-blank strings. Focused regression, full
  unittest discovery, and `git diff --check` pass; local implementation commit
  `3b0d508`.

- [x] 2026-07-20 09:30 PDT: Added
  `validation-obligation-has-reviewable-rationale` crisp validation, matching
  the PeTTa backend's rationale gate. Exact ground truth rejects `None`, list,
  and blank rationales while accepting non-blank text. Focused 37-test
  validation suite, full 367-test suite, and `git diff --check` pass; local
  implementation commit `82625f7`.

- [x] 2026-07-20 07:30 PDT: Made `check-has-evidence` fail closed on
  non-string CheckRecord evidence, matching the PeTTa backend's reviewable-text
  gate. Exact ground truth rejects `None` and list evidence, preserves the
  blank-string diagnostic, and accepts non-blank text. Focused 36-test
  validation suite, full 366-test suite, and `git diff --check` pass; local
  implementation commit `42432b2`.

- [x] 2026-07-20 05:30 PDT: Made `fact-subject-matches-object` fail closed on
  non-string subjects, matching the PeTTa backend's exact subject-type gate.
  Ground truth proves integer `7` cannot alias object ID `"7"`, while the exact
  string owner passes. Focused 35-test validation suite, full 365-test suite,
  and `git diff --check` pass; local implementation commit `da469fd`.

- [x] 2026-07-20 03:30 PDT: Added `fact-arguments-are-backend-safe` crisp
  validation aligned with PeTTa export refusal gates. Exact ground truth now
  rejects container arguments, non-string object references, blank values, and
  non-finite floats while accepting supported non-empty scalars. Focused
  34-test validation suite, full 364-test suite, and `git diff --check` pass;
  local implementation commit `255484a`.

- [x] 2026-07-20 01:30 PDT: Made crisp fact validation fail closed for
  malformed non-tuple fact records and non-string predicates, matching the
  PeTTa backend refusal gates. Exact list/string/dict/None and integer/None
  predicate ground truth now yields deterministic Fail evidence; provenance
  validation also skips malformed facts safely. Focused 33-test validation
  suite, full 363-test suite, and `git diff --check` pass; local implementation
  commit `f243bd3`.

- [x] 2026-07-19 23:30 PDT: Added backend-safe Section and PlainItem identity
  validation and filtered malformed IDs from section/item and fact-validation
  indexes. List-valued and blank IDs now yield deterministic Fail evidence
  instead of crashing, while valid neighboring IDs Pass. Focused 32-test
  validation suite, full 362-test suite, and `git diff --check` pass; local
  implementation commit `4fa1853`.

- [x] 2026-07-19 21:30 PDT: Added `source-span-has-safe-identity` validation
  and made uniqueness, validation-provenance, and edge-provenance span indexes
  ignore unhashable/blank IDs. Exact regression coverage, focused 31-test
  validation suite, all 361 tests, and `git diff --check` pass; local
  implementation commit `440399b`.

- [x] 2026-07-19 19:30 PDT: Added backend-safe PlainFile identity validation
  and filtered malformed file IDs from source-span and validation-target
  indexes. List-valued and blank IDs now yield deterministic Fail evidence
  instead of crashing, while valid neighboring IDs Pass. Focused 30-test
  validation suite, full 360-test suite, and `git diff --check` pass; local
  implementation commit `752c5b2`.

- [x] 2026-07-19 17:30 PDT: Added explicit backend-safe identity validation
  for ValidationObligation and CheckRecord IDs. Non-string and blank IDs now
  produce dedicated deterministic Fail evidence, while valid IDs produce Pass
  evidence, matching the PeTTa exporter gates. Focused 29-test validation suite,
  full 359-test suite, and `git diff --check` pass; local implementation commit
  `386ff29`.

- [x] 2026-07-19 15:30 PDT: Made validation-layer identity checks fail closed
  for unhashable malformed ValidationObligation and CheckRecord IDs. Safe-ID
  filtering now covers Counter, set, and dictionary indexes, and list-valued
  IDs yield deterministic identity Fail evidence while downstream validation
  continues. Focused 28-test validation suite, full 358-test suite, and
  `git diff --check` pass; local implementation commit `75a37b8`.

- [x] 2026-07-19 13:30 PDT: Made crisp object-identity validation fail closed
  for unhashable malformed IDs. List-valued IDs now produce deterministic
  `object-identity-is-unique` and `object-has-safe-identity` Fail evidence
  instead of crashing set/Counter membership and downstream obligation
  validation. Focused 27-test validation suite, full 357-test suite, and
  `git diff --check` pass; local implementation commit `81fda0f`.

- [x] 2026-07-19 11:30 PDT: Added `object-has-safe-identity` crisp validation
  aligned with the PeTTa non-string/blank object-ID refusal gates. Exact
  integer, whitespace-only, and valid-string ground truth, focused 26-test
  validation suite, full 356-test suite, and `git diff --check` pass; local
  implementation commit `a9fe38f`.

- [x] 2026-07-19 09:30 PDT: Made crisp semantic-level and PeTTa-profile
  validation reject unhashable malformed values without crashing. Exact list
  value ground truth, focused 25-test validation suite, full unittest discovery,
  and `git diff --check` pass; local commit `747efdf`.

- [x] 2026-07-19 01:30 PDT: Added `object-identity-is-unique` crisp validation
  aligned with the PeTTa duplicate-object refusal gate. Exact duplicate and
  unique ground truth, focused regression, full 351-test suite, and
  `git diff --check` pass; local implementation commit `2fcf5ee`.

- [x] 2026-07-18 21:30 PDT: Added crisp, fail-closed validation obligations
  for nested Plain-item parents: uniquely indexed parent, no self-parenting,
  and matching file/section context. Exact ground-truth regression, focused
  19-test validation suite, full 349-test suite, and `git diff --check` pass;
  local commit `4fbbe89`.

- [x] 2026-07-18 17:30 PDT: Make section/item exact-source-span membership
  checks fail closed on duplicate indexed `SourceSpan` IDs, with exact
  ambiguity evidence and regression coverage; 347-test suite passed.

- [x] 2026-07-18: Made source-span, section, and item file-link validation fail closed for duplicate indexed `PlainFile` IDs. The three crisp checks now emit deterministic ambiguity evidence instead of treating the ID as indexed or selecting the last file record. Focused 17-test validation suite, full 347-test suite, and `git diff --check` pass; local commit `4c67665`.

- [x] 2026-07-18: Made item-to-section validation fail closed for duplicate indexed section IDs. `item-has-section` and `item-file-matches-section-file` now emit exact Fail evidence instead of selecting the last matching section and risking a false Pass. Focused 16-test validation suite, full 346-test suite, and `git diff --check` pass; local commit `8fe7bc1`.

- [x] 2026-07-18: Added the symmetric item-span aliasing regression: `item-span-file-matches-item-file` is now pinned to the canonical indexed span even when an embedded `SourceSpan` with the same ID masks a cross-file mismatch. Exact Fail evidence, focused 14-test validation suite, full 344-test suite, and `git diff --check` pass; local commit `dbc4c94`.

- [x] 2026-07-18: Closed the validation-layer counterpart of the section-span aliasing gap: `section-span-file-matches-section-file` now checks the canonical indexed span rather than a conflicting embedded span record. Exact status/evidence ground truth, focused 13-test validation suite, full 343-test suite, and `git diff --check` pass; local commit `afd48da`.

- [x] 2026-07-18: Closed a PeTTa section-provenance aliasing gap by checking a section's file against the canonical source span admitted to the manifest, not a conflicting embedded `SourceSpan` object with the same ID. Exact atom/refusal ground truth, focused regression, full 342-test suite, and `git diff --check` pass; local commit `1da9671`.

- [x] 2026-07-18: When a source manifest is present, refused dangling `derived-from` links from SpecObjects and validation obligations to absent or earlier-refused source spans, while preserving valid links, absent optional provenance, and standalone object-only projection. Exact atom/refusal ground truth, full 340-test suite, and `git diff --check` pass; local commit `dc00958`.

- [x] 2026-07-17: Refused PeTTa `PlainItem` records linked to absent/earlier-refused files, sections, or source spans, plus items whose emitted section/span belongs to another file; valid neighboring item atoms remain unchanged. Exact ground-truth regression, focused 81-test source/profile suites, full 339-test suite, and `git diff --check` pass; local commit `f53f120`.

- [x] 2026-07-17: Refused PeTTa `SourceSpan` records linked to absent or earlier-refused `PlainFile` identities, preventing dangling `source-span` atoms while preserving valid neighboring provenance. Exact ground-truth regression, focused 79-test source/profile suites, full 337-test suite, and `git diff --check` pass; local commit `48d22c2`.

- [x] 2026-07-17: Refused every occurrence of duplicate `PlainFile`, `SourceSpan`, `Section`, and `PlainItem` IDs before PeTTa source-manifest emission, preventing ambiguous provenance atoms while preserving uniquely identified neighboring records. Exact ground-truth regression, focused 78-test source/profile suites, full 336-test suite, and `git diff --check` pass; local commit `c97f2c1`.

- [x] 2026-07-17: Refused malformed PeTTa `Section` and `PlainItem` atom-bearing fields before source-manifest emission: unsafe IDs/links, invalid ordinals, malformed provenance spans, blank item text, and non-string parent IDs no longer crash or alias emitted atoms, while valid neighboring records still emit. Focused source-index/profile suites passed 77 tests; full 335-test suite and `git diff --check` pass; local commit `346055e`.

- [x] 2026-07-17: Refused malformed PeTTa `PlainFile` identities, paths, and digests before source-manifest or summary emission, while preserving a valid neighboring file as the document identity. Focused source-index/profile suites passed 76 tests; full 334-test suite and `git diff --check` pass; local commit `11e298f`.

- [x] 2026-07-17: Refused malformed PeTTa source-span identities/file links and invalid byte/line bounds, including boolean pseudo-integers, while preserving valid neighboring span atoms. Focused source-index/profile suites passed 75 tests; full 333-test suite and `git diff --check` pass; local commit `bf37ab8`.

- [x] 2026-07-17: Refused malformed `PlainFile`, `SourceSpan`, `Section`, and `PlainItem` container entries during PeTTa reified source-manifest export instead of dereferencing them until a crash; valid neighboring provenance still emits and document/graph summaries use the first emitted file identity. Focused 72-test profile suite and full 332-test suite pass; `git diff --check` passes; local commit `4988bbd`.

- [x] 2026-07-17: Refused malformed non-`ValidationObligation` and non-`CheckRecord` entries in PeTTa reified export with structured type-bearing backend refusals instead of crashing, while continuing to emit valid neighboring records and counting only emitted checks; focused 71-test profile suite and full 331-test suite pass; `git diff --check` passes; local commit `269b708`.

- [x] 2026-07-17: Refused every duplicate SpecObject ID from PeTTa reified export, suppressing ambiguous object/fact/provenance atoms and counting only emitted question objects in document-validation summaries; focused 70-test profile suite and full 330-test suite pass; `git diff --check` passes; local commit `be41253`.

- [x] 2026-07-17: Refused PeTTa reified checks whose property or target disagrees with the emitted validation obligation they cite, suppressing inconsistent check atoms and excluding them from validation-summary counts; focused 67-test profile suite and full 327-test suite pass; `git diff --check` passes; local commit `4e06a16`.

- [x] 2026-07-16: Refused checks whose referenced validation obligation was absent or refused by the PeTTa reified gate, suppressing dangling `check-obligation` atoms and excluding those checks from validation-summary counts; focused 66-test profile suite and full 326-test suite pass; `git diff --check` passes; local commit `d59965e`.

- [x] 2026-07-16: Refused whitespace-only object and validation-obligation source-span IDs in PeTTa reified export instead of emitting malformed `derived-from` atoms, while preserving absent optional provenance; focused 64-test profile suite and full 324-test suite pass; `git diff --check` passes; local commit `5afe6c3`.

- [x] 2026-07-16: Refused non-string and blank validation-obligation rationales in PeTTa reified export, preventing numeric/string rationale aliasing and suppressing the entire malformed obligation; focused 63-test profile suite and full 323-test suite pass; `git diff --check` passes; local commit `62a19c4`.

- [x] 2026-07-16: Refused non-string and blank validation-obligation properties in PeTTa reified export, preventing numeric/string property aliasing and suppressing the entire malformed obligation and rationale; focused regression and full 321-test suite pass; `git diff --check` passes; local commit `2115035`.

- [x] 2026-07-16: Refused non-string and blank validation-check target IDs in PeTTa reified export, preventing numeric/string target aliasing and suppressing malformed checks from atoms and document-validation summary counts; focused 60-test profile suite and full 320-test suite pass; `git diff --check` passes; local commit `894a7b5`.

- [x] 2026-07-16: Refused non-string and blank validation-check properties in PeTTa reified export, preventing numeric/string property aliasing and suppressing malformed checks from atoms and document-validation summary counts; focused 59-test profile suite and full 319-test suite pass; `git diff --check` passes; local commit `39eda2d`.

- [x] 2026-07-16: Refused non-string and blank check-to-obligation IDs in PeTTa reified export, preventing numeric/string link aliasing and suppressing the entire malformed check from atoms and validation-summary counts; focused 57-test profile suite and full 317-test suite pass; `git diff --check` passes; local commit `83c18d3`.

- [x] 2026-07-16: Refused non-string and blank validation-obligation IDs in PeTTa reified export, suppressing aliased obligation/rationale atoms and emitting explicit backend refusals; focused 55-test profile suite and full 315-test suite pass; `git diff --check` passes; local commit `58ab362`.

- [x] 2026-07-15: Refused non-string object source-span IDs in PeTTa reified provenance and executable lowering, including referenced objects, preventing misleading `derived-from` atoms and `.strip()` crashes; focused 53-test profile suite and full 313-test suite pass; local commit `1ae563b`.
- [x] 2026-07-15: Refuse empty and whitespace-only object IDs in the PeTTa reified profile, suppressing the invalid object, provenance, and fact atoms; focused 51-test profile suite and full 311-test suite pass; local commit `0e09f18`.
- [x] 2026-07-15: Refuse malformed non-tuple fact records in both PeTTa profiles instead of indexing/iterating them until export crashes; suppress misleading fact atoms and keep information-flow summary generation safe; focused 50-test profile suite and full 310-test suite pass; local commit `71dcd92`.
- [x] 2026-07-15: Refuse malformed non-enum semantic levels in both PeTTa profiles instead of raising while reading `.value`; preserve safe diagnostic text for invalid levels and suppress object/fact emission; focused 49-test profile suite and full 309-test suite pass; local commit `45b6b88`.
- [x] 2026-07-15: Require string IDs in object-scoped PeTTa fact subject positions; integer, float, and boolean subjects can no longer alias object IDs through implicit stringification; added reified/executable ground-truth regression; full 306-test suite passes; local commit `0777830`.
- [x] 2026-07-15: Require string IDs in PeTTa object-reference fact positions; numeric and boolean values can no longer alias declared objects through implicit stringification; added reified/executable ground-truth regression; full 305-test suite passes; local commit `7bb1514`.
- [x] 2026-07-15: Quote ASCII control characters in PeTTa scalar serialization so emitted atoms contain JSON escapes instead of raw NUL/control bytes; added fact-atom ground-truth regression; full 304-test suite passes; local commit `4f644be`.
- [x] 2026-07-15: Quote semicolon-bearing source and fact text in PeTTa reified output so MeTTa comment syntax cannot silently truncate generated atoms; added source/fact ground-truth regression; full 303-test suite passes; local commit `1dfd8ed`.
- [x] 2026-07-14: Added ground-truth coverage proving structured values in object-reference positions are refused by both PeTTa profiles before ID resolution/stringification; full 302-test suite passes.
- [x] 2026-07-14: Refuse `None` and whitespace-only object-reference fact arguments in the PeTTa reified profile instead of serializing them as IDs, while preserving executable-skeleton empty-reference and deep missing-ID diagnostics; full 299-test suite passes.
- [x] 2026-07-14: Refuse `None` scalar fact arguments in both PeTTa reified emission and executable-skeleton gating instead of serializing them as meaningful atoms; focused regression and full 298-test suite pass.
- [x] 2026-07-14: Refuse whitespace-only scalar fact arguments in both PeTTa reified emission and executable-skeleton gating while preserving the existing object-reference-specific diagnostics; focused profile suite 37 tests and full suite 297 tests pass.

- [x] 2026-07-14: Added ground-truth coverage proving whitespace-only source provenance fails closed for executable lowering directly, at the referencing object, and through an outer arbitrary-depth reference chain; 296 tests pass.
- [x] 2026-07-14: Added ground-truth coverage proving whitespace-only executable object IDs fail closed both directly and through arbitrary-depth object-reference traversal; 295 tests pass.
- [x] 2026-07-14: Closed the arbitrary-depth form of the empty executable-object identity fail-open: an outer safe object now receives a `MissingObjectId` refusal when its reference graph reaches an empty-ID descendant; added ground-truth coverage; 294 tests pass.
- [x] 2026-07-14: Closed an executable-skeleton identity fail-open: empty object IDs now produce `missing-object-id-for-executable-skeleton`, and otherwise profile-valid facts with empty object-reference targets produce `unsafe-profile-fact:empty-object-reference:*`; added direct and referenced ground-truth regressions; 293 tests pass.
- [x] 2026-07-14: Added positive executable-skeleton ground truth for a profile-safe diamond reference DAG, proving shared descendants are not misclassified as reference cycles while fail-closed traversal remains intact; 291 tests pass.
- [x] 2026-07-13: Made mixed-depth executable-reference refusal selection globally canonical by ordering complete traversal paths rather than letting a shallower lexically later sibling mask a deeper `alpha` branch; added mixed-depth RawTextOnly ground truth; 290 tests pass.
- [x] 2026-07-13: Made direct executable-skeleton refusal record ordering independent of an originating object's fact insertion order by canonically sorting candidate facts; added reversed-order two-target RawTextOnly ground truth; 289 tests pass.
- [x] 2026-07-13: Made arbitrary-depth executable-reference refusal selection independent of descendant fact insertion order: deep traversal now visits canonical predicate/target references, with reversed-order ground truth for competing deep RawTextOnly paths; 288 tests pass.
- [x] 2026-07-13: Made executable-reference refusal selection deterministic when a safe target contains multiple unsafe referenced facts: canonical minimum predicate/target/reason selection now avoids fact-order-dependent diagnostics; added a reversed-fact-order ground-truth regression; 287 tests pass.
- [x] 2026-07-13: Added depth-parameterized ground-truth coverage proving unsupported semantic-level refusals take precedence over missing source provenance at direct, one-hop, and deeper executable-reference paths; 286 tests pass.
- [x] 2026-07-13: Restored refusal precedence for unsafe semantic levels: `RawTextOnly` and other non-executable levels now retain their explicit semantic-level refusal even when source provenance is also absent; added a two-object ground-truth regression; 285 tests pass.
- [x] 2026-07-13: Closed the one-hop descendant traversal gap in executable-reference safety: a directly referenced safe object whose immediate child has missing provenance, missing profile facts, profile-invalid facts, or an ambiguous ID now refuses explicitly; added a four-case ground-truth regression; 284 tests pass.
- [x] 2026-07-12: Closed the remaining arbitrary-depth executable-reference ambiguity gap: descendant references to duplicate object IDs now refuse as `AmbiguousReference`; added `coverage -> requirement -> artifact -> duplicate source` ground-truth coverage; 283 tests pass.
- [x] 2026-07-12: Extended arbitrary-depth executable-reference safety to refuse deep safe-level descendants with missing source provenance, missing profile facts, or profile-invalid facts; added a three-case ground-truth regression; 282 tests pass.
- [x] 2026-07-12: Tightened executable-skeleton arbitrary-depth reference safety to refuse cyclic descendant chains explicitly (`ReferenceCycle`) instead of silently skipping revisited objects; added `coverage -> requirement -> artifact -> requirement` ground-truth coverage; 281 tests pass.
- [x] 2026-07-12: Extended executable-skeleton arbitrary-depth reference safety to refuse descendant chains ending in undeclared objects; added `coverage -> requirement -> artifact -> missing-source` ground-truth coverage; 280 tests pass.
- [x] 2026-07-12: Extended executable-skeleton safety through arbitrary-depth profile-valid object-reference chains; deep RawTextOnly descendants now cause explicit refusal; 279 tests pass.
- [x] 2026-07-12: Extended executable-skeleton transitive reference safety to refuse safe intermediate objects that reference `RawTextOnly` or otherwise executable-unsafe targets; added a three-object ground-truth regression; 278 tests pass.
- [x] 2026-07-12: Tightened executable-skeleton reference safety transitively: referenced safe-level objects whose own profile facts contain dangling object references now block lowering with an explicit refusal; added ground-truth coverage; 277 tests pass.
- [x] 2026-07-12: Tightened executable-skeleton reference safety so safe-level targets with missing provenance, missing facts, or profile-invalid facts cannot be lowered transitively; added ground-truth refusal coverage; 276 tests pass.
- [x] 2026-07-12: Tightened executable-skeleton gating to refuse duplicate object IDs and references whose target ID is ambiguous (`duplicate-object-id-for-executable-skeleton`, `unsafe-profile-fact:ambiguous-object-reference:*`); added a ground-truth regression; 275 tests pass.
- [x] 2026-07-12: Tightened executable-skeleton gating to refuse otherwise valid object references when the declared target is `RawTextOnly` or another non-executable-safe semantic level (`unsafe-profile-fact:unsafe-object-reference-semantic-level:*`); added unsafe-target and safe-target regressions; 274 tests pass.
- [x] 2026-07-12: Tightened executable-skeleton gating to refuse profile-valid facts with dangling object references (`unsafe-profile-fact:dangling-object-reference:*`); added dangling and declared-reference regressions, including one-shot iterable input; 273 tests pass.
- [x] 2026-07-12: Tightened executable-skeleton gating to refuse source-provenanced lowered/verified objects with no profile facts (`missing-profile-facts-for-executable-skeleton`); added regression coverage; 271 tests pass.
Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [x] 2026-07-15: Refused non-string PeTTa fact predicates before schema lookup, preventing custom or scalar runtime values from aliasing supported predicate names through string conversion; added reified/executable ground-truth coverage; 312 tests pass.

- [x] 2026-07-11: Tightened executable-skeleton gating so `BackendLowered`/`Verified` labels are not sufficient by themselves: unknown predicates, malformed fact arity, and object-fact subject mismatches now produce explicit `unsafe-profile-fact:*` refusals; added safe-lowered and three unsafe ground-truth regressions; 269 tests pass.

- [x] 2026-07-11: Tightened axiom justification so placeholder/unsupported `Proof:` markers remain blocking review objects but do not create `AxiomEvidence` or pass `axiom-has-explicit-justification`; added a ground-truth regression covering both `MissingProofDetail` and `MissingAxiomJustification`; 267 tests pass.

- [x] 2026-07-11: Added explicit `Axiom:` marker support: source-spanned proposition objects with `Axiom`/`AxiomText`/`AxiomFor`/`SourceItem` facts, same-item support links via `AxiomEvidence` to explicit `Evidence:` or `Proof:` markers, Unknown `axiom-has-explicit-justification` checks plus exported `MissingAxiomJustification` blocking questions when justification is absent, PeTTa reified export coverage, exact-boundary regression before following `Proof:`, README support-surface update, and 266 passing tests.

- [x] 2026-07-11: Added explicit `Proof:` marker support: source-spanned evidence/review objects with `Proof`/`ProofText`/`ProofFor`/`SourceItem` facts, Pass/Unknown `proof-marker-reviewable` checks for concrete proof artifacts/procedures versus TODO/raw-text-only/prove-later placeholders, exported `MissingProofDetail` blocking questions when proof detail is absent, PeTTa reified export coverage, exact-boundary regression before following `Evidence:`, README support-surface update, and 264 passing tests.


- [x] 2026-07-11: Added explicit `Claim:` marker support: source-spanned proposition objects with `Claim`/`ClaimText`/`ClaimFor`/`SourceItem` facts, same-item evidence links via `ClaimEvidence`, Unknown `claim-has-explicit-evidence` checks plus exported `MissingClaimEvidence` blocking questions when evidence is absent, PeTTa reified export coverage, exact-boundary regression before following `Evidence:`, README support-surface update, and 262 passing tests.

- [x] 2026-07-11: Added explicit `Counterexample:` marker support: source-spanned validation objects with `Counterexample`/`CounterexampleText`/`CounterexampleFor`/`SourceItem` facts, Pass `counterexample-has-source-provenance` checks that preserve falsification examples without automatically rejecting/proving claims, PeTTa reified export coverage, exact-boundary regression before following `Evidence:`, and 260 passing tests.

- [x] 2026-07-11: Added explicit `Observation:` marker support: source-spanned proposition objects with `Observation`/`ObservationText`/`ObservationFor`/`SourceItem` facts, Pass `observation-has-source-provenance` checks that preserve reported observations without implying validation success/executable semantics, PeTTa reified export coverage, exact-boundary regression before following `Evidence:`, and 259 passing tests.
- [x] 2026-07-11: Added explicit `Hypothesis:` marker support: source-spanned proposition objects with `Hypothesis`/`HypothesisText`/`HypothesisFor`/`SourceItem` facts, same-item evidence links via `HypothesisEvidence`, Unknown `hypothesis-has-explicit-evidence` checks plus exported `MissingHypothesisEvidence` blocking questions when evidence is absent, PeTTa reified export coverage, README support-surface update, and 258 passing tests.
- [x] 2026-07-11: Added `Verification:` as an explicit validation-procedure alias alongside `Validation:` / `Check:`, preserving exact source spans before following `Evidence:` markers while exporting the same conservative `Validation`/`ValidationText`/`ValidationFor` facts, Pass/Unknown `validation-marker-reviewable` behavior, PeTTa reified coverage, and 256 passing tests.

- [x] 2026-07-11: Added explicit `Precondition:` / `Postcondition:` marker support: source-spanned obligation/proposition objects with `Precondition`/`PreconditionText`/`PreconditionFor` and `Postcondition`/`PostconditionText`/`PostconditionFor` facts, same-item evidence links via `PreconditionEvidence`/`PostconditionEvidence`, Unknown checks plus `MissingPreconditionEvidence`/`MissingPostconditionEvidence` blocking questions when evidence is absent, PeTTa reified export coverage, and 255 passing tests.

- [x] 2026-07-11: Added explicit `Validation:` / `Check:` marker support: source-spanned validation objects with `Validation`/`ValidationText`/`ValidationFor`/`SourceItem` facts, Pass/Unknown `validation-marker-reviewable` checks for concrete test/golden-fixture/audit/diagnostic procedures versus validate-later placeholders, `MissingValidationDetail` blocking questions, PeTTa reified export coverage, and 253 passing tests.

- [x] 2026-07-10: Added explicit `Metric:` marker support: source-spanned validation objects with `Metric`/`MetricText`/`MetricFor`/`SourceItem` facts, Pass/Unknown `metric-definition-reviewable` checks for concrete named metrics/thresholds/units versus placeholder values, `MissingMetricDefinition` blocking questions, PeTTa reified export coverage, and 251 passing tests.

- [x] 2026-07-10: Added explicit `Citation:` / `Reference:` marker support: source-spanned evidence/reference objects with `Citation`/`CitationText`/`CitationFor`/`SourceItem` facts, Pass/Unknown `citation-reference-reviewable` checks for concrete DOI/arXiv/URL/bibliography/file references versus placeholder citation-needed values, `MissingCitationReference` blocking questions, PeTTa reified export coverage, and 249 passing tests.

- [x] 2026-07-10: Added explicit `Example:` marker support: source-spanned review/example objects with `Example`/`ExampleText`/`ExampleFor`/`SourceItem` facts, Pass/Unknown `example-detail-reviewable` checks for concrete examples versus placeholder TODO/TBD/raw-text-only values, `MissingExampleDetail` blocking questions, PeTTa reified export coverage, and 247 passing tests.

- [x] 2026-07-10: Added explicit `Acceptance Criterion:` / `Acceptance Criteria:` / `Criterion:` marker support: source-spanned validation objects with `AcceptanceCriterion`/`AcceptanceCriterionText`/`AcceptanceCriterionFor`/`SourceItem` facts, Pass/Unknown `acceptance-criterion-reviewable` checks for concrete criteria versus placeholder TODO/TBD/raw-text-only values, `MissingAcceptanceCriterionDetail` blocking questions, PeTTa reified export coverage, and 245 passing tests.

- [x] 2026-07-10: Added explicit `Deadline:` / `Due:` marker support: source-spanned review objects with `Deadline`/`DeadlineText`/`DeadlineValue`/`DeadlineFor`/`SourceItem` facts, Pass/Unknown `deadline-value-reviewable` checks for concrete dates/quarters/halves/bounded relative intervals versus vague/TODO/ASAP placeholders, `UnsupportedDeadlineValue` blocking questions, PeTTa reified export coverage, and 243 passing tests.

- [x] 2026-07-10: Added explicit `Priority:` marker support: source-spanned review objects with `Priority`/`PriorityText`/`PriorityValue`/`PriorityFor`/`SourceItem` facts, Pass/Unknown `priority-value-reviewable` checks for supported values (`blocker`, `critical`, `high`, `medium`, `low`, `P0`-`P3`) versus TODO/TBD/unsupported placeholders, `UnsupportedPriorityValue` blocking questions, PeTTa reified export coverage, and 241 passing tests.

- [x] 2026-07-10: Added explicit `Owner:` / `Assignee:` marker support: source-spanned accountability objects with `Owner`/`OwnerText`/`OwnerFor`/`SourceItem` facts, Pass/Unknown `owner-assignment-reviewable` checks, `MissingOwnerAssignment` blocking questions for TODO/TBD/unassigned placeholders, PeTTa reified export coverage, and 239 passing tests.

- [x] 2026-07-10: Added explicit `Deprecated:` / `Deprecation:` and `Replacement:` marker support: source-spanned review objects with `Deprecated`/`DeprecatedText`/`DeprecatedFor` and `Replacement`/`ReplacementText`/`Replaces`/`SourceItem` facts, same-item `DeprecatedReplacedBy` links, Unknown `deprecated-item-has-replacement-or-disposition` checks plus `MissingDeprecationDisposition` blocking questions when no replacement/migration/sunset/removal disposition is present, PeTTa reified export coverage, and 237 passing tests.

- [x] 2026-07-10: Added explicit `TODO:` / `To-do:` marker support: source-spanned blocking question objects with `TodoItem`/`TodoText`/`TodoFor`/`QuestionText`/`SourceItem`/`Blocks` facts, Unknown `todo-item-needs-resolution` checks, boundary handling before following `Evidence:` / `Open issue:` markers, PeTTa reified export coverage, and 235 passing tests.

- [x] 2026-07-10: Added explicit `Open issue:` / `Issue:` marker support: source-spanned blocking question objects with `OpenIssue`/`OpenIssueText`/`IssueFor`/`QuestionText`/`SourceItem`/`Blocks` facts, Unknown `open-issue-needs-resolution` checks, boundary handling before following `Evidence:` / `Question:` markers, PeTTa reified export coverage, and 233 passing tests.

- [x] 2026-07-10: Added explicit `NonGoal:` / `Non-goal:` marker support: source-spanned exclusion objects with `NonGoal`/`NonGoalText`/`NonGoalFor`/`SourceItem` facts, Pass `non-goal-has-source-provenance` checks, marker-boundary handling before following `Evidence:` clauses, PeTTa reified export coverage, and 231 passing tests.

- [x] 2026-07-10: Added explicit `Limitation:` marker support: source-spanned review objects with `Limitation`/`LimitationText`/`LimitationFor`/`SourceItem` facts, optional same-item mitigation links via `LimitationMitigatedBy`, Unknown `limitation-has-review-disposition` checks plus exported `MissingLimitationDisposition` blocking questions when no mitigation/workaround/disposition is present, PeTTa reified export coverage, and 230 passing tests.

- [x] 2026-07-09: Broadened `Resource:` reviewability so artifact-path-only declarations such as `docs/capacity.v1.yaml` and `infra/limits.toml` pass `resource-requirement-reviewable` with exact source spans and PeTTa export, while TODO/raw-text-only placeholders remain Unknown; full suite now 228 passing tests.

- [x] 2026-07-09: Broadened `Process:` reviewability so script/config/build artifact-only declarations such as `scripts/deploy.sh` and `Makefile` pass `process-definition-reviewable` with exact source spans and PeTTa export, while TODO/raw-text-only placeholders remain Unknown; full suite now 227 passing tests.

- [x] 2026-07-09: Broadened witness/dependency concrete artifact recognition for extensionless build files (`Dockerfile`, `Containerfile`, `Makefile`) so explicit markers pass reviewability checks and PeTTa export without Missing* questions; full suite now 226 passing tests.

- [x] 2026-07-09: Broadened dependency concrete path recognition so operational/config artifacts such as `scripts/bootstrap.sh`, `pyproject.toml`, and lockfiles can satisfy `dependency-requirement-reviewable` while retaining exact source spans and PeTTa export; full suite now 224 passing tests.

- [x] 2026-07-09: Broadened witness/backend-artifact concrete path recognition so `.yaml`, `.yml`, and `.sh` artifacts such as `docs/capacity.v1.yaml` and `scripts/demo.sh` pass `witness-artifact-reviewable` while retaining exact source spans and PeTTa export; full suite now 223 passing tests.
- [x] 2026-07-09: Tightened explicit `Process:` and `Resource:` marker boundary parsing so period-bearing operational/artifact references such as `scripts/demo.sh`, `out/review.metta`, and `docs/capacity.v1.yaml` stop before following same-item markers (for example `Evidence:`) without truncating file paths; full suite now 222 passing tests.
- [x] 2026-07-09: Tightened explicit `Epistemic status:` / `Status:` marker boundary parsing so supported labels such as `verified` stop before following same-item markers (for example `Evidence:`), avoiding false unsupported statuses like `verified-evidence` while preserving exact epistemic/evidence source spans and PeTTa export; full suite now 221 passing tests; local commit `8cd114e`.
- [x] 2026-07-09: Tightened explicit `Scope:`/`Context:` and `Confidence:` marker boundary parsing so period-bearing file/artifact scope references and percent confidence values stop before following same-item semantic markers (for example `Evidence:`), preserving exact scope/confidence/evidence source spans and PeTTa export; full suite now 220 passing tests.
- [x] 2026-07-09: Tightened explicit `Interpretation:` marker boundary parsing so file-path/artifact interpretation text with periods stops before following same-item semantic markers (for example `Bridge:`), preserving exact interpretation/bridge source spans and PeTTa export; full suite now 219 passing tests.
- [x] 2026-07-09: Tightened explicit `Rationale:` marker boundary parsing so file-path/artifact rationale text with periods stops before following same-item semantic markers (for example `Evidence:`), preserving exact rationale/evidence source spans and PeTTa export; full suite now 218 passing tests.
- [x] 2026-07-09: Tightened explicit `Evidence:` marker boundary parsing so file-path/test evidence with periods stops before following same-item semantic markers (for example `Outcome:`), preserving exact evidence/outcome source spans and PeTTa export; full suite now 217 passing tests.
- [x] 2026-07-08: Tightened `Witness:` / `Artifact:` marker boundary parsing so file-path witness text with periods stops before following same-item semantic markers (for example `Outcome:`), preserving separate exact source spans and PeTTa export; full suite now 216 passing tests.
- [x] 2026-07-08: Added explicit `Dependency:` marker support: source-spanned dependency/resource objects with `Dependency`/`DependencyText`/`DependencyFor`/`SourceItem` facts, concrete service/API/file/package/dataset/artifact review via `dependency-requirement-reviewable`, Unknown `MissingDependencyDetail` blocking questions for TODO/vague placeholders, PeTTa reified export coverage, and 215 passing tests.
- [x] 2026-06-30: Expanded the `specatom_hs` source indexer to preserve multi-line bullet continuations without swallowing nested acceptance-test bullets.
- [x] 2026-06-30: Added conservative concept-table pass distinguishing explicit local definitions, external links, and unresolved references with Unknown checks/questions.
- [x] 2026-06-30: Extended concept-table pass to support conservative aliases (`[def:]`, `[ref:]`, `[concept:]`) and bare glossary definitions beyond explicit `:Concept:` / `[external:...]` syntax.
- [x] 2026-06-30: Extended concept-table pass to preserve first-class concept reference occurrence atoms with exact marker-level spans and occurrence-targeted validation checks.
- [x] 2026-06-30: Added a shallow requirement/test coverage pass with Pass/Unknown `requirement-has-acceptance-test` checks, missing-test questions, and coverage atoms.
- [x] 2026-07-01: Added initial scaffold fact-arity and declared-reference validators for supported object-fact predicates, with Fail diagnostics for malformed arity/dangling targets and Unknown for predicates outside the current schema.
- [x] 2026-07-01: Tightened `petta_reified_v0` backend projection with profile-filtered supported predicates/arity refusals and fuller validation rationale/evidence atoms.
- [x] 2026-07-01: Added first Unknown-to-question validator path beyond concept/coverage cases: unsupported fact predicates now produce profile question objects that block the relevant fact-profile obligation.
- [x] 2026-07-01: Added validation-layer self-checks so check records must cite a known obligation and match its property/target.
- [x] 2026-07-01: Added validation-obligation provenance/target self-checks so malformed obligation source spans and undeclared targets fail crisply.
- [x] 2026-07-01: Extended `petta_reified_v0` export with source provenance manifest atoms (`plain-file`, `source-span`, `section`, `plain-item`, `derived-from`) and ground-truth regression coverage.
- [x] 2026-07-01: Tightened concept occurrence span indexing so marker spans on multi-line bullet continuation lines carry exact start/end line numbers.
- [x] 2026-07-01: Added PeTTa reified-profile semantic-level validation so unsupported levels such as `RawTextOnly` create explicit Unknown checks and blocking questions before export/refusal.
- [x] 2026-07-01: Added explicit requirement/test coverage labels (`[id:...]` / `[covers:...]`) with `RequirementLabel` and `CoverageClaim` atoms, label-resolved coverage, and Unknown/blocking-question handling for unresolved coverage labels.
- [x] 2026-07-01: Added duplicate requirement-label ambiguity handling: explicit `[covers:...]` claims now require exactly one matching label and otherwise produce Unknown checks plus duplicate/ambiguous target questions.
- [x] 2026-07-01: Added orphan acceptance-test coverage obligations/questions plus profile-safe `OrphanAcceptanceTest` export.
- [x] 2026-07-01: Added object-fact subject validation and PeTTa refusal for facts whose declared subject does not match the owning SpecObject.
- [x] 2026-07-02: Made explicit requirement coverage labels document-scoped, so `[covers:...]` acceptance tests can resolve forward to later requirement sections instead of falsely becoming missing-label questions.
- [x] 2026-07-02: Added `check-status-is-known` validation so check records with undeclared/non-enum statuses fail crisply, and made PeTTa check export robust to malformed status text.
- [x] 2026-07-02: Added `check-has-evidence` validation so check records with empty evidence fail crisply as malformed diagnostics.
- [x] 2026-07-02: Added source-span byte/line validation (`source-span-within-file-bounds`, `source-span-lines-match-byte-offsets`) so malformed indexed spans fail crisply as malformed provenance.
- [x] 2026-07-02: Added Plain file digest validation (`plain-file-digest-matches-content`) so corrupted preserved-source manifests fail crisply as malformed provenance.
- [x] 2026-07-02: Added section/item PlainFile link validation (`section-file-is-indexed`, `section-has-source-span`, `item-file-is-indexed`) so malformed source-index records fail crisply before backend provenance export.
- [x] 2026-07-02: Tightened source-index provenance consistency with section/item/span file-ID cross-checks so cross-file-corrupted source records fail crisply.
- [x] 2026-07-02: Froze the v0.1 target profile and completed a validator gap audit against Appendix N/P categories; docs live in `repos/specatom-hs/docs/v01-profile.md` and `repos/specatom-hs/docs/validator-gap-audit.md`.
- [x] 2026-07-02: Added v0.1 CLI/demo outputs (`specatom_hs.cli`, grouped `.metta`, Markdown diagnostics, `scripts/demo.sh`) plus an `auth_service.plain` review fixture and regression checks for duplicate labels, missing coverage targets, unresolved concepts, and backend refusals.
- [x] 2026-07-02: Optimized validation obligation/check de-duplication to use stable record IDs instead of whole-dataclass membership, making the larger auth-service review fixture practical in the unit suite.
- [x] 2026-07-02: Added question-object blocker validation so unresolved concept questions point at their exact Unknown obligations and malformed QuestionObjects fail when review text/blocker links are missing or dangling.
- [x] 2026-07-07: Added the first Phase 2 semantic-object slice for explicit `Scope`/`Context`, `EpistemicStatus`, `Evidence`, `Interpretation`, and `Bridge` markers with stable IDs, exact source provenance, conservative validation obligations/checks, Unknown/question handling for unsupported labels/profile gaps and missing evidence, PeTTa reified export coverage, and 189 passing tests. Decision: Ben chose this over further information-flow deepening on 2026-07-07 (`DECISIONS.md` D-20260707).
- [x] 2026-07-07: Tightened Phase 2 semantic-object source-span alignment so repeated markers and continuation-line markers cite the exact regex occurrence instead of the first matching text in the item; added regression coverage for repeated `Evidence:` clauses and continuation-line evidence spans; 191 tests pass.
- [x] 2026-07-07: Broadened Phase 2 `Bridge:` marker parsing so arbitrary unsupported ontology labels still create reviewable, source-spanned `BridgeObject`s plus Unknown `bridge-profile-supported` checks and `UnsupportedBridgeOntology` blocking questions instead of being silently ignored; 192 tests pass; local commit `b23cc36`.
- [x] 2026-07-07: Added explicit Phase 2 `Confidence:` marker support: percent/decimal confidence annotations normalize to `ConfidenceValue` atoms, valid `[0,1]` values pass `confidence-value-in-unit-interval`, and out-of-range values produce Unknown checks plus `UnsupportedConfidenceValue` blocking questions; 194 tests pass; local commit `7b7aedb`.
- [x] 2026-07-07: Added conservative Phase 2 bridge relation validation: supported graded correspondence relations pass `bridge-relation-conservative`, while identity/equivalence-style labels such as `identical` produce Unknown checks plus `UnsupportedBridgeRelation` blocking questions and PeTTa reified review atoms; 195 tests pass; local commit `6c5e2df`.
- [x] 2026-07-07: Tightened explicit Phase 2 `Confidence:` marker behavior so non-numeric scales such as `Confidence: high` still become source-spanned confidence objects with `confidence-value-in-unit-interval` Unknown checks plus `UnsupportedConfidenceValue` blocking questions instead of being silently ignored; 196 tests pass; local commit `565a348`.
- [x] 2026-07-08: Added a first Phase 3 witness/backend-artifact marker slice: explicit `Witness:` / `Artifact:` / `Backend artifact:` annotations now create source-spanned `BackendArtifact` objects with `Witness`/`WitnessText`/`WitnessFor` facts, `witness-artifact-reviewable` Pass checks for concrete file/test/log/commit/hash-style artifacts, Unknown checks plus `MissingWitnessArtifact` blocking questions for TODO/raw-text-only/non-concrete placeholders, and PeTTa reified export support; 199 tests pass; local commit `a838ba7`.
- [x] 2026-07-07: Added a first Phase 3-adjacent explicit `Revision:` marker slice: source-spanned `RevisionObject`s now carry `Revision`/`RevisionText`/`Revises`/`SourceItem` facts, get `revision-has-source-provenance` Pass checks, and export through the PeTTa reified profile; 197 tests pass.
- [x] 2026-07-06: Added `document-validation-summary` atom to PeTTa reified export with Pass/Fail/Unknown check counts and QuestionObject count; added 18-test end-to-end ground-truth test suite for `auth_service.plain` fixture covering source provenance, concepts, requirements/coverage, validation summary, refusals, and reified export structure; 159 tests pass.
- [x] 2026-07-02: Added first v0.2 conservative ML/time-series methodology validation slice: metric declaration, horizon/frequency declaration, reproducibility evidence, and train-only preprocessing fit-scope obligations/questions.
- [x] 2026-07-02: Extended the v0.2 ML/time-series methodology slice with baseline-comparison and uncertainty/error-bar reporting obligations/questions.
- [x] 2026-07-02: Added explicit preprocess-then-split leakage review (`ml-preprocessing-order-reviewed`) with Unknown checks/questions when specs say normalize/scale/preprocess before splitting without train-only fit scope.
- [x] 2026-07-03: Added explicit future/label-as-feature leakage review (`ml-future-label-leakage-reviewed`) with Unknown checks/questions when future values, labels, or targets appear in feature/input contexts.
- [x] 2026-07-03: Added first conservative metric/task appropriateness review (`ml-metric-task-appropriateness-reviewed`) for classification-style metrics on forecast/regression-like ML specs.
- [x] 2026-07-03: Added conservative temporal split-order review (`ml-temporal-split-order-reviewed`) for random/shuffled time-series split wording without chronological/walk-forward/out-of-time evidence.
- [x] 2026-07-03: Added generic-vs-named baseline/uncertainty methodology review (`ml-baseline-comparator-named`, `ml-uncertainty-method-named`) so vague baseline/uncertainty mentions become Unknown blocking questions.
- [x] 2026-07-03: Added prediction-time feature availability review (`ml-feature-availability-reviewed`) so declared ML inputs/features require point-in-time/as-of, lagged, historical, or equivalent availability evidence.
- [x] 2026-07-08: Added explicit `Assumption:` marker support: source-spanned `AssumptionObject`s with `Assumption`/`AssumptionText`/`AssumptionFor`/`SourceItem` facts, same-item evidence links via `AssumptionEvidence`, Unknown `assumption-has-explicit-evidence` checks plus exported `MissingAssumptionEvidence` blocking questions when evidence is absent, PeTTa reified export coverage, and 204 passing tests; local commit `30365db`.
- [x] 2026-07-08: Added explicit `Invariant:` marker support: source-spanned proposition objects with `Invariant`/`InvariantText`/`InvariantFor`/`SourceItem` facts, same-item evidence links via `InvariantEvidence`, Unknown `invariant-has-explicit-evidence` checks plus exported `MissingInvariantEvidence` blocking questions when evidence is absent, PeTTa reified export coverage, and 206 passing tests; local commit `75b77a4`.
- [x] 2026-07-08: Added explicit `Rationale:` marker support: source-spanned explanation objects with `Rationale`/`RationaleText`/`RationaleFor`/`SourceItem` facts, `rationale-has-source-provenance` Pass checks, PeTTa reified export coverage, and 209 passing tests; local commit `2514410`.
- [x] 2026-07-08: Added explicit `Constraint:` marker support: source-spanned obligation objects with `Constraint`/`ConstraintText`/`ConstraintFor`/`SourceItem` facts, same-item evidence links via `ConstraintEvidence`, Unknown `constraint-has-explicit-evidence` checks plus exported `MissingConstraintEvidence` blocking questions when evidence is absent, PeTTa reified export coverage, and 208 passing tests; local commit `ea3cb26`.
- [x] 2026-07-08: Added explicit `Risk:` / `Mitigation:` marker support: source-spanned review objects with `Risk`/`RiskText`/`RiskFor` and `RiskMitigation`/`RiskMitigationText`/`MitigatesRiskFor` facts, same-item mitigation links via `RiskMitigatedBy`, Unknown `risk-has-explicit-mitigation` checks plus exported `MissingRiskMitigation` blocking questions when mitigation/control evidence is absent, PeTTa reified export coverage, and 211 passing tests; local commit `83e8112`.
- [x] 2026-07-08: Added explicit `Decision:` marker support: source-spanned proposition objects with `Decision`/`DecisionText`/`DecidesFor`/`SourceItem` facts, Pass `decision-has-source-provenance` checks, PeTTa reified export coverage, README support-surface update, and 212 passing tests; local commit `df8cb83`.
- [x] 2026-07-08: Added explicit `Outcome:` marker support: source-spanned proposition objects with `Outcome`/`OutcomeText`/`OutcomeFor`/`SourceItem` facts, Pass `outcome-has-source-provenance` checks, PeTTa reified export coverage, README support-surface update, and 213 passing tests; local commit `59250c6`.
- [ ] v0.2 follow-up: deepen ML/time-series methodology validation with richer comparator/uncertainty semantics and stronger metric appropriateness once target/task facets are explicit.
- [x] 2026-07-04: Added real-time/current feature freshness review (`ml-feature-freshness-reviewed`) so ML/time-series specs with current/live/recent/fresh features require freshness, staleness, latency, update-cadence, data-age, or as-of timestamp evidence.
- [ ] v0.2 candidate: continue information-flow and temporal-availability obligations for declared inputs/outputs and temporally impossible claims.
- [x] 2026-07-07: Added duplicate/parallel DataFlowEdge review (`information-flow-duplicate-edge-reviewed`) so repeated declarations of the same normalized component-level edge produce Pass when absent/acknowledged and Unknown blocking questions when unacknowledged; 186 tests pass.
- [x] 2026-07-07: Extended component-level `DataFlowEdge` extraction to include explicit `pulls ... from` / `pushes ... to` wording with `pulls-from` / `pushes-to` normalization, information-flow signal coverage, exact source-span provenance, and ground-truth regression coverage; 186 tests pass.
- [x] 2026-07-07: Extended component-level `DataFlowEdge` extraction to include explicit `ingests ... from` / `emits ... to` wording with `ingests-from` / `emits-to` normalization, information-flow signal/declaration coverage, exact source-span provenance, and ground-truth regression coverage; 186 tests pass.
- [x] 2026-07-07: Extended component-level `DataFlowEdge` extraction to include explicit `feeds into` wording with `feeds-into` normalization, exact source-span provenance, target-span trimming for trailing preposition/temporal words, and ground-truth regression coverage; 186 tests pass.
- [x] 2026-07-07: Extended component-level `DataFlowEdge` extraction to include explicit `receives ... from` wording with `receives-from` normalization, exact source-span provenance, and ground-truth regression coverage; 186 tests pass.
- [x] 2026-07-07: Tightened `TemporalOrderEdge` provenance from whole-item spans to exact matched temporal-ordering phrase spans, with regression coverage comparing generated source slices to ground truth; 186 tests pass.
- [x] 2026-07-06: Tightened DataFlowEdge provenance from item-level spans to exact matched edge-phrase source spans; edge provenance validator now passes exact/item-contained spans and regression tests compare generated spans against ground-truth source slices; 180 tests pass.
- [x] 2026-07-06: Added sink-reachability review (`information-flow-sink-reachability-reviewed`) using reverse BFS from sinks to catch source-reachable trapped cycles/dead ends that cannot reach any output sink; Unknown creates blocking `MissingInformationFlowEvidence` questions, Pass when all nodes have a sink path; 180 tests pass.
- [x] 2026-07-06: Added temporal ordering impossibility detection: extracts explicit "A before/after/then/precedes/follows B" statements, builds temporal ordering graph, detects impossible cycles via DFS, emits TemporalOrderEdge atoms, `information-flow-temporal-impossibility-reviewed` obligation (Fail on impossible cycles, Pass when consistent or no temporal statements), blocking questions, and PeTTa reified profile export; 131 tests pass.
- [x] 2026-07-03: Added first v0.2 security/privacy obligation scaffolding for secrets, PII/privacy handling, access boundaries, and destructive-action safety, defaulting to Unknown/question where evidence is missing.
- [x] 2026-07-03: Added secret log-exposure review (`security-secret-log-exposure-reviewed`) so secret/token/password specs require redaction, masking, or no-logging evidence.
- [x] 2026-07-03: Added first data/sensitivity classification declaration review (`privacy-data-classification-declared`) for PII/personal-data specs, with Unknown blocking questions when classification evidence is absent.
- [x] 2026-07-03: Added privilege-escalation review (`security-privilege-escalation-reviewed`) so access/auth/admin/role specs require least-privilege, approval, audit, admin-only, or self-grant-prevention evidence.
- [x] 2026-07-03: Added PII retention/deletion review (`privacy-retention-deletion-reviewed`) so personal-data specs require retention, deletion/erasure, expiry, or minimization evidence.
- [x] 2026-07-03: Added data-residency/cross-border transfer review (`privacy-data-residency-reviewed`) so PII specs with region/country/jurisdiction/residency/cross-border wording require policy evidence or produce Unknown blocking questions.
- [x] 2026-07-03: Added third-party/vendor/processor sharing review (`privacy-third-party-sharing-reviewed`) so PII specs that mention vendors, processors, partners, external services, exports, uploads, or sharing require DPA/vendor-review/data-sharing policy evidence.
- [x] 2026-07-04: Added lawful-basis/consent review (`privacy-lawful-basis-reviewed`) so PII/personal-data specs require consent, lawful/legal basis, contract, legal-obligation, legitimate-interest, or similar evidence.
- [x] 2026-07-04: Added purpose-limitation review (`privacy-purpose-limitation-reviewed`) so PII/personal-data specs require specific-purpose, use-limitation, no-secondary-use, or secondary-use-review evidence.
- [x] 2026-07-04: Added data-subject rights review (`privacy-data-subject-rights-reviewed`) so PII/personal-data specs require access/correction/rectification/portability/opt-out/privacy-rights evidence.
- [x] 2026-07-04: Added rights-request identity/authentication review (`privacy-rights-request-authentication-reviewed`) so PII/personal-data specs with rights/access/deletion/erasure request wording require identity-verification or authenticated-request evidence.
- [x] 2026-07-04: Added PII access audit review (`privacy-pii-access-audit-reviewed`) so PII/personal-data specs with access/admin/role wording require access audit, logging, or monitoring evidence.
- [x] 2026-07-04: Added PII incident-response/breach-notification review (`privacy-incident-response-reviewed`) so PII/personal-data specs require incident response, breach notification, or escalation evidence.
- [x] 2026-07-04: Added PII encryption-scope/key-management review (`privacy-encryption-scope-reviewed`) so generic encryption mentions no longer satisfy protection evidence unless encryption-at-rest, transport encryption/TLS, database/field encryption, KMS, key rotation, or equivalent scope is stated.
- [x] 2026-07-04: Added authentication/API abuse-protection review (`security-auth-abuse-protection-reviewed`) so auth/login/API/password/token specs require rate limiting, throttling, brute-force protection, lockouts, abuse detection, bot detection, or CAPTCHA evidence; 73 tests pass.
- [x] 2026-07-04: Added credential rotation/expiry/revocation review (`security-credential-rotation-reviewed`) so secret/token/password/credential specs require lifecycle evidence; 74 tests pass.
- [x] 2026-07-04: Added authentication/API transport-protection review (`security-auth-transport-protection-reviewed`) so auth/login/API/password/token specs require TLS, HTTPS, mTLS, certificate-pinning, transport-encryption, or secure-channel evidence; 75 tests pass.
- [x] 2026-07-05: Added API authorization/scope review (`security-api-authorization-reviewed`) so API/endpoint/request specs in auth/access context require authorization, permission/scope, RBAC/access-control, deny-by-default, or policy-enforcement evidence; 76 tests pass.
- [x] 2026-07-05: Added webhook/callback request-authenticity review (`security-webhook-request-authenticity-reviewed`) so webhook/callback/external-request specs require HMAC/signature verification, webhook-secret, timestamp-window, nonce, idempotency-key, or replay-protection evidence; 77 tests pass.
- [x] 2026-07-05: Added API/webhook input-validation review (`security-api-input-validation-reviewed`) so request payload/body/query/parameter/JSON/form/upload specs require input/schema/payload validation, sanitization, allow-listing, type checks, or bounds checks; 78 tests pass.
- [x] 2026-07-05: Added API/webhook error-disclosure review (`security-api-error-disclosure-reviewed`) so API/webhook error, exception, stack-trace, traceback, debug, or diagnostic response specs require generic/redacted/sanitized/opaque/correlation-ID style safe error evidence; 79 tests pass.
- [ ] v0.2 follow-up: deepen security/privacy semantics with richer data-classification facets, policy provenance, and stronger access-control checks once Phase 2/3 objects exist.
- [ ] Extend profile-aware backend projection for `petta_reified_v0` beyond the current source manifest, supported object facts, and validation records, still without mutating the IR.
- [ ] Preserve the uploaded SpecAtom-HS PDF as a research-library source sidecar if/when desired; current implementation used `/home/openclaw/tmp/omegaclaw-telegram-attachments/1782780878-file_3.pdf.extracted.txt`.

## Next

- [x] 2026-06-29: Implemented first PeTTa target reality check scaffold: `petta_reified_v0` profile gates, supported semantic levels, unsupported-level refusals, and RawTextOnly executable-skeleton refusal policy.
- [ ] Continue Phase 2 SpecAtom-HS core after the first semantic-object slice lands: broaden `Scope`, `EpistemicStatus`/confidence, `Evidence`, `Interpretation`, and `Bridge` coverage against the design note.
- [ ] Continue Phase 3 facets beyond current witnesses/backend artifacts, process/resource placeholders, revisions, and explicit questions.
- [ ] Implement Phase 4 PeTTa reified backend producing target-profile-filtered `.metta` files and richer source provenance manifests.
- [ ] Add first SUMO/EXPO/Hyperseed bridge table with graded contextual correspondences from Appendix K.
- [ ] Compare emitted atoms against design note 0006 and record divergences.

## Waiting or blocked

- [x] 2026-07-15: Ben approved `Plain2Metta` and all publication
  recommendations. Renamed the existing remote to public
  `bgoertzel-sing/plain2metta` rather than creating a duplicate, retained
  `specatom_hs` as the package/IR name, updated README/description, pushed
  `agent/plain2metta-public-launch`, and opened draft PR #2. Secret-like tracked
  tree scan and `git diff --check` passed; the pre-branding code suite had 306
  passing tests at `0777830`.

- [x] Remote repository identity/publication — completed 2026-07-15 as public
  `bgoertzel-sing/plain2metta`; internal package/IR remains `specatom_hs`.
  Reconfirmed by Ben 2026-08-07 after a stale summary incorrectly requested a
  repository-name/visibility decision.
- [ ] Full PDF library preservation - needs a deliberate library-curation step if this source should be kept beyond the temporary attachment path.

## Someday or exploratory

- [ ] Richer information-flow/time validator for future pollution and temporal availability.
- [ ] PLN overlay for conflicting claims and confidence propagation.
- [ ] MeTTa-IL profile.
- [ ] Rholang process profile.
- [ ] TyLA/OSLF deeper type/proof alignment.

## Done recently

- [x] 2026-07-26 11:30 PDT: Rejected interior whitespace in canonical
  object-scoped validation subtargets through the shared crisp-validation and
  PeTTa/diagnostics admission predicate. Ground truth covers ASCII space and
  Unicode em space; 216 focused validation/backend/diagnostics tests and all
  460 tests pass; `git diff --check` passes.

- [x] 2026-07-23: Aligned diagnostics check scalar admission with the PeTTa
  backend's basic gates for obligation IDs, properties, target IDs, declared
  statuses, and non-blank evidence. Refused checks no longer affect diagnostic
  counts/property breakdowns or leak detailed evidence; focused diagnostics
  passed 16 tests, the full stdlib suite passed all 406 tests, and
  `git diff --check` passed. Local commit `2e60b16`.

- [x] 2026-07-22: Added crisp `item-has-valid-record-type` validation matching
  the PeTTa backend's malformed `PlainItem` refusal; malformed entries are
  excluded from item-derived indexes, exact malformed/valid regression
  coverage passes, the focused validation suite passes 58 tests, the full
  stdlib suite passes all 388 tests, and `git diff --check` passes.

- [x] 2026-07-20: Tightened `check-status-is-known` diagnostics to report
  exact unsupported status values and runtime types while preserving explicit
  Pass evidence for declared `CheckStatus` values; exact malformed/valid
  regression coverage, focused 43-test validation suite, all 373 tests, and
  `git diff --check` pass; local commit `a8e9372`.

- [x] 2026-07-20: Added crisp `check-has-safe-property` validation matching
  the PeTTa backend's non-blank string check-property gate; exact
  malformed/valid regression coverage, focused 41-test validation suite, all
  371 tests, and `git diff --check` pass; local commit `1adf2c0`.

- [x] 2026-07-20: Added crisp
  `validation-obligation-has-safe-property` validation matching the PeTTa
  backend's non-blank string property gate; exact malformed/valid regression
  coverage, focused 38-test validation suite, all 368 tests, and
  `git diff --check` pass; local commit `393047e`.

- [x] 2026-07-19: Added crisp `object-has-known-role` validation so malformed
  non-enum SpecObject roles fail deterministically before the matching PeTTa
  backend refusal gate; exact regression coverage, focused 24-test validation
  suite, all 354 tests, and `git diff --check` pass; local commit `1bafb57`.

- [x] 2026-07-19: Made crisp and PeTTa-profile semantic-level validation fail
  closed for malformed/unsupported non-enum values instead of crashing on
  `.value`; exact regression coverage, focused 23-test validation suite, all
  353 tests, and `git diff --check` pass; local commit `e408cf1`.

- [x] 2026-07-19: Added explicit `validation-obligation-identity-is-unique`
  and `check-identity-is-unique` crisp obligations so duplicate validation-layer
  IDs fail deterministically before the matching PeTTa backend refusal gates;
  focused 22-test validation suite and all 352 tests pass; `git diff --check`
  passes; local commit `70891ce`.

- [x] 2026-07-18: Added explicit `plain-file-identity-is-unique` and
  `source-span-identity-is-unique` crisp obligations so duplicate top-level
  source identities fail deterministically on the ambiguous records themselves;
  focused 20-test validation suite and all 350 tests pass; `git diff --check`
  passes; local commit `810c8f2`.

- [x] 2026-07-18: Added explicit `section-identity-is-unique` and
  `item-identity-is-unique` crisp obligations so duplicate source-record IDs
  fail with deterministic ambiguity evidence rather than collapsing target-keyed
  checks; narrow validation tests and all 348 tests pass; `git diff --check`
  passes; local commit `00a41c8`.

- [x] 2026-07-18: Made crisp section/item span-file validation fail closed on duplicate indexed SourceSpan IDs instead of using last-write-wins lookup; exact Fail/evidence regression coverage and all 344 tests pass; `git diff --check` passes; local commit `ffad34a`.

- [x] 2026-07-18: Closed Plain-item parent-link provenance gaps in PeTTa source-manifest export: missing/refused, self, cross-file, and cross-section parents now suppress the child; refusal cascades to descendants while forward references to valid parents still emit. Exact atom/refusal ground truth and all 341 tests pass; `git diff --check` passes; local commit `012c93d`.

- [x] 2026-07-17: Closed the PeTTa source-manifest provenance chain through `PlainItem`, refusing dangling/refused file, section, and span links and cross-file item provenance; exact atom/refusal ground truth and all 339 tests pass; local commit `f53f120`.

- [x] 2026-07-17: Refused sections whose file/span was not emitted or whose span belongs to a different file, preventing dangling/cross-file `section` and `derived-from` atoms; exact atom/refusal ground truth passes, the 78-test PeTTa profile suite and full 338-test stdlib suite pass, and `git diff --check` passes; local commit `2bfa970`.

- [x] 2026-07-17: Refused all duplicate validation-obligation and check IDs in PeTTa reified export, preventing order-dependent obligation selection and contradictory check atoms; linked checks to duplicate/refused obligations are suppressed, summary counts include only emitted checks, exact atom/refusal regressions pass, and the full suite passes 329 tests; local commit `8cc1078`.

- [x] 2026-07-16: Tightened PeTTa reified check export so evidence must be non-blank reviewable text; integer evidence can no longer alias string evidence, malformed checks are fully suppressed and excluded from summary counts, and exact ground-truth regression coverage passes; 325 tests pass and `git diff --check` passes; local commit `4d2512a`.

- [x] 2026-07-16: Tightened PeTTa reified validation-obligation export so target IDs must be non-blank strings; integer `7` can no longer alias the legitimate string target `"7"`, malformed obligation/rationale atoms are suppressed, and exact ground-truth regression coverage passes; 322 tests pass and `git diff --check` passes; local commit `6231ce3`.

- [x] 2026-07-16: Tightened PeTTa reified check export so only declared `CheckStatus` enum values are emitted; runtime strings such as `"Pass"` and missing statuses are refused without aliasing valid records or inflating document-validation summary counts; 318 tests pass and `git diff --check` passes; local commit `d9bf308`.

- [x] 2026-07-16: Tightened PeTTa reified check export so non-string/blank check IDs are refused instead of aliasing legitimate string IDs, and document-validation summary counts include only emitted checks; 316 tests pass and `git diff --check` passes; local commit `bc4b348`.

- [x] 2026-07-15: Tightened PeTTa reified export so non-string validation-obligation source-span IDs produce explicit backend refusals and cannot be silently stringified into false `derived-from` provenance atoms; 314 tests pass and `git diff --check` passes; local commit `e5ef724`.

- [x] 2026-07-14: Refused structured/non-scalar fact arguments (including lists and mappings) in both PeTTa reified and executable-skeleton profiles instead of stringifying them into misleading atoms, with ground-truth regression coverage; 301 tests pass; local commit `149bd57`.

- [x] 2026-07-14: Refused non-finite scalar fact arguments (`NaN`, `Infinity`, `-Infinity`) in both PeTTa reified and executable-skeleton profiles, with ground-truth regression coverage; 300 tests pass.

- [x] 2026-07-14: Checkpointed the accumulated conservative semantic-marker and fail-closed PeTTa profile work as local commit `0007d99`: exact-spanned Phase 2/3 objects and review questions, executable-reference safety through arbitrary-depth object graphs, and refusal of empty/`None` scalar and object-reference arguments. Full suite: 299 tests pass; `git diff --check` passes.
- [x] 2026-07-11: Tightened executable-skeleton lowering to refuse otherwise profile-safe objects with missing/blank source provenance; added regression coverage; 270 tests pass.
- [x] 2026-07-08: Added explicit `Dependency:` marker support: source-spanned dependency/resource objects with `Dependency`/`DependencyText`/`DependencyFor`/`SourceItem` facts, concrete service/API/file/package/dataset/artifact review via `dependency-requirement-reviewable`, Unknown `MissingDependencyDetail` blocking questions for TODO/vague placeholders, PeTTa reified export coverage, and 215 passing tests.
- [x] 2026-07-08: Added explicit `Decision:` marker support: source-spanned proposition objects with `Decision`/`DecisionText`/`DecidesFor`/`SourceItem` facts, Pass `decision-has-source-provenance` checks, PeTTa reified export coverage, README support-surface update, and 212 passing tests; local commit `df8cb83`.
- [x] 2026-07-08: Added explicit `Risk:` / `Mitigation:` marker support: source-spanned review objects with `Risk`/`RiskText`/`RiskFor` and `RiskMitigation`/`RiskMitigationText`/`MitigatesRiskFor` facts, same-item mitigation links via `RiskMitigatedBy`, Unknown `risk-has-explicit-mitigation` checks plus exported `MissingRiskMitigation` blocking questions when mitigation/control evidence is absent, PeTTa reified export coverage, and 211 passing tests; local commit `83e8112`.
- [x] 2026-07-08: Added explicit `Rationale:` marker support: source-spanned explanation objects with `Rationale`/`RationaleText`/`RationaleFor`/`SourceItem` facts, `rationale-has-source-provenance` Pass checks, PeTTa reified export coverage, and 209 passing tests; local commit `2514410`.
- [x] 2026-07-08: Added explicit `Constraint:` marker support: source-spanned obligation objects with `Constraint`/`ConstraintText`/`ConstraintFor`/`SourceItem` facts, same-item evidence links via `ConstraintEvidence`, Unknown `constraint-has-explicit-evidence` checks plus exported `MissingConstraintEvidence` blocking questions when evidence is absent, PeTTa reified export coverage, and 208 passing tests; local commit `ea3cb26`.
- [x] 2026-07-08: Added explicit `Invariant:` marker support: source-spanned proposition objects with `Invariant`/`InvariantText`/`InvariantFor`/`SourceItem` facts, same-item evidence links via `InvariantEvidence`, Unknown `invariant-has-explicit-evidence` checks plus exported `MissingInvariantEvidence` blocking questions when evidence is absent, PeTTa reified export coverage, and 206 passing tests; local commit `75b77a4`.
- [x] 2026-07-08: Added explicit `Assumption:` marker support: source-spanned `AssumptionObject`s with `Assumption`/`AssumptionText`/`AssumptionFor`/`SourceItem` facts, same-item evidence links via `AssumptionEvidence`, Unknown `assumption-has-explicit-evidence` checks plus exported `MissingAssumptionEvidence` blocking questions when evidence is absent, PeTTa reified export coverage, and 204 passing tests; local commit `30365db`.
- [x] 2026-07-08: Added explicit `Question:` marker support: source-spanned `QuestionObject`s with `ExplicitQuestion`/`QuestionText`/`QuestionsObject`/`SourceItem`/`Blocks` facts, `explicit-question-needs-answer` Unknown checks, PeTTa reified export coverage, and 202 passing tests; local commit `a510534`.
- [x] 2026-07-08: Added explicit `Process:` and `Resource:` Phase 3 marker support: source-spanned `ProcessObject`/`ResourceObject` atoms with `Process`/`ProcessText`/`ProcessFor` and `Resource`/`ResourceText`/`ResourceFor` facts, concrete process/resource validation (`process-definition-reviewable`, `resource-requirement-reviewable`), TODO/vague placeholder Unknown blocking questions (`MissingProcessDefinition`, `MissingResourceRequirement`), PeTTa reified export coverage, and 201 passing tests; local commit `09a5134`.
- [x] 2026-07-08: Added explicit `Witness:` / `Artifact:` / `Backend artifact:` marker support with source-spanned `BackendArtifact` witness atoms, concrete-artifact validation, TODO/raw-text-only Unknown blocking questions, PeTTa export coverage, and 199 passing tests.
- [x] 2026-07-07: Added explicit `Revision:` marker support with source-spanned `RevisionObject` atoms, provenance validation, PeTTa export coverage, and 197 passing tests.
- [x] 2026-07-07: Extended component-level `DataFlowEdge` extraction to include explicit `pulls ... from` / `pushes ... to` wording with `pulls-from` / `pushes-to` normalization, information-flow signal coverage, exact source-span provenance, and ground-truth regression coverage; 186 tests pass.
- [x] 2026-07-07: Extended component-level `DataFlowEdge` extraction to include explicit `ingests ... from` / `emits ... to` wording with `ingests-from` / `emits-to` normalization, information-flow signal/declaration coverage, exact source-span provenance, and ground-truth regression coverage; 186 tests pass.
- [x] 2026-07-07: Extended component-level `DataFlowEdge` extraction to include explicit `feeds into` wording with `feeds-into` normalization, exact source-span provenance, target-span trimming for trailing preposition/temporal words, and ground-truth regression coverage; 186 tests pass.
- [x] 2026-07-07: Extended component-level `DataFlowEdge` extraction to include explicit `receives ... from` wording with `receives-from` normalization, exact source-span provenance, and ground-truth regression coverage; 186 tests pass.
- [x] 2026-07-07: Tightened `TemporalOrderEdge` provenance from whole-item spans to exact matched ordering phrase spans; temporal edge regression coverage now compares source slices against ground truth while preserving edge provenance validation; 186 tests pass.
- [x] 2026-07-07: Broadened Phase 2 `Bridge:` marker parsing so arbitrary unsupported ontology labels still create reviewable `BridgeObject`s plus Unknown checks/questions instead of being skipped; 192 tests pass.
- [x] 2026-07-07: Added explicit Phase 2 `Confidence:` marker support with normalized `ConfidenceValue` export and Unknown/blocking-question handling for out-of-range values; 194 tests pass; local commit `7b7aedb`.
- [x] 2026-07-07: Tightened explicit Phase 2 `Confidence:` marker behavior so non-numeric scales such as `Confidence: high` still become source-spanned confidence objects with `confidence-value-in-unit-interval` Unknown checks plus `UnsupportedConfidenceValue` blocking questions instead of being silently ignored; 196 tests pass; local commit `565a348`.
- [x] 2026-07-07: Added conservative bridge relation validation so `Bridge: ... as identical` remains a source-spanned `BridgeObject` but gets an Unknown `bridge-relation-conservative` check plus `UnsupportedBridgeRelation` blocking question instead of being accepted as identity; 195 tests pass; local commit `6c5e2df`.
- [x] 2026-07-07: Added duplicate/parallel edge review to the information-flow validation slice: repeated declarations of the same normalized `DataFlowEdge` now emit `information-flow-duplicate-edge-reviewed` Pass/Unknown checks, blocking questions for unacknowledged duplication, and PeTTa reified export coverage; 186 tests pass.
- [x] 2026-07-06: Added sink-reachability review to the information-flow validation slice: reverse BFS from sinks finds components that cannot reach any output sink even when they are source-reachable. Emits `information-flow-sink-reachability-reviewed` Pass/Unknown checks, blocking questions for trapped cycles/dead ends/missing outputs, and PeTTa reified export coverage; 180 tests pass.
- [x] 2026-07-06: Fixed O(n^2) validator deduplication bottleneck: replaced linear-scan `all(existing.id != ...)` in `add_validation_obligation` and `add_check` with O(1) set-based lookups using `SpecDocument._obligation_ids` and `_check_ids`. Auth_service compile time dropped from >17s to 0.14s.
- [x] 2026-07-06: Added `information-flow-graph-summary` atom to PeTTa reified export: computes node count, edge count, temporal edge count, source/sink counts, cycle count, connected component count, max dependency depth, and bottleneck node count from DataFlowEdge/TemporalOrderEdge facts; 4 ground-truth tests; 174 tests pass.
- [x] 2026-07-06: Added bidirectional edge review to information-flow validation: detects A→B and B→A pairs in the DataFlowEdge graph, emits `information-flow-bidirectional-edge-reviewed` obligation (Pass when no bidirectional pairs or acknowledged via request-response/feedback-loop/bidirectional/two-way/mutual/round-trip wording, Unknown with blocking question when unacknowledged); 5 regression tests; 178 tests pass.
- [x] 2026-07-06: Added connected-components detection to the information-flow validation slice: undirected BFS finds disconnected subgraphs in the DataFlowEdge graph, emits `information-flow-connected-components-reviewed` obligation (Pass when acknowledged as independent/separate/standalone, Unknown with blocking question otherwise); 3 regression tests; 170 tests pass.
- [x] 2026-07-06: Added `document-validation-summary` atom to PeTTa reified export with Pass/Fail/Unknown check counts and QuestionObject count; added 18-test end-to-end ground-truth test suite for `auth_service.plain` fixture covering source provenance, concepts, requirements/coverage labels, duplicate label detection, orphan acceptance tests, unresolved concepts, validation summary counts, reified export structure, backend refusals, and grouped `.metta` section separators; 159 tests pass.
- [x] 2026-07-06: Added temporal ordering impossibility detection to the information-flow validation slice: regex-based extraction of "A before/after/then/precedes/follows B" statements, temporal ordering graph construction, DFS-based cycle detection for impossible orderings, TemporalOrderEdge atoms, `information-flow-temporal-impossibility-reviewed` obligation (Fail on impossible cycles, Pass when consistent or no temporal statements), blocking questions, PeTTa reified profile export, and 9 regression tests; 131 tests pass.
- [x] 2026-07-06: Added cross-layer DataFlowEdge vs TemporalOrderEdge consistency check: when data flows A→B but temporal statements say B before A, emits `information-flow-data-temporal-consistency-reviewed` obligation (FAIL on contradictions, PASS when consistent or either edge type absent), blocking questions, and PeTTa reified profile export; 4 regression tests; 135 tests pass.

- [x] 2026-07-05: Added API/webhook error-disclosure review to the conservative security/privacy slice; 79 tests pass.
- [x] 2026-07-05: Added component-level data-path edge extraction to the information-flow pass; `DataFlowEdge` atoms, `information-flow-data-path-declared` obligation, `DataFlowEdge` fact schema, regression tests; 93 tests pass.
- [x] 2026-07-05: Added first v0.2 information-flow validation slice (`information-flow-inputs-declared`, `information-flow-outputs-declared`, `information-flow-dependency-direction-declared`, `information-flow-temporal-availability-reviewed`, `information-flow-circular-dependency-reviewed`) with `InformationFlowReview`/`MissingInformationFlowEvidence` atoms, blocking questions, and PeTTa reified profile export; 88 tests pass.
- [x] 2026-07-05: Added component-level data-path edge extraction to the information-flow pass: `DataFlowEdge` atoms for explicit "X reads from Y" / "X writes to Y" / "X consumes from Y" / "X depends on Y" patterns, `information-flow-data-path-declared` obligation (Pass with edges, Unknown with only vague wording), `DataFlowEdge` fact schema for PeTTa export, and regression tests comparing extracted edges to ground truth; 93 tests pass.
- [x] 2026-07-05: Added transitive dependency chain detection from extracted DataFlowEdge atoms: builds adjacency graph from edges, detects A→B→C chains via BFS, emits `information-flow-transitive-dependency-reviewed` obligation (Pass when spec acknowledges with 'through'/'via'/'indirect'/'transitive' wording, Unknown with blocking question when unacknowledged); 96 tests pass.
- [x] 2026-07-05: Added graph-based cycle detection from extracted DataFlowEdge atoms: builds directed adjacency graph, detects cycles via DFS white/gray/black coloring, emits `information-flow-cycle-detected` obligation (Pass when acyclic, Unknown with blocking question when cycles exist); 100 tests pass.
- [x] 2026-07-05: Added fan-out/fan-in concentration detection from extracted DataFlowEdge atoms: computes per-node out-degree and in-degree, triggers review when any component has >=3 edges in one direction, emits `information-flow-fan-out-reviewed` and `information-flow-fan-in-reviewed` obligations (Pass when acknowledged or below threshold, Unknown with blocking question when unacknowledged); 107 tests pass.
- [x] 2026-07-05: Added source/sink identification and reachability analysis from extracted DataFlowEdge atoms: identifies source nodes (no incoming edges) and sink nodes (no outgoing edges), emits `information-flow-source-sink-identified` obligation (Pass when both exist, Unknown when missing), and BFS-based reachability check emitting `information-flow-reachability-reviewed` obligation (Pass when all nodes reachable from sources, Unknown with blocking question when unreachable nodes exist); 113 tests pass.
- [x] 2026-07-05: Added isolated component detection from broader data-flow verbs: components mentioned with non-edge verbs like `receives data from`, `feeds into`, `flows to`, `provides to`, `gets from`, `pulls from`, `pushes to` that don't produce DataFlowEdge atoms trigger `information-flow-isolated-component-reviewed` obligation (Pass when all mentioned components appear in edges, Unknown with blocking question when isolated components are found); 117 tests pass.
- [x] 2026-07-06: Added redundant path detection from extracted DataFlowEdge atoms: finds all simple paths between node pairs, detects when multiple distinct paths (direct + indirect) connect the same pair, emits `information-flow-redundant-path-reviewed` obligation (Pass when no redundant paths or spec acknowledges redundancy via 'redundant'/'backup'/'fallback'/'failover'/'fault tolerance'/'high availability'/'duplicate'/'resilient'/'replicated' wording, Unknown with blocking question when unacknowledged); 122 tests pass.
- [x] 2026-07-06: Added cross-layer DataFlowEdge vs TemporalOrderEdge consistency check: when data flows A→B but temporal statements say B before A, emits `information-flow-data-temporal-consistency-reviewed` obligation (FAIL on contradictions, PASS when consistent or either edge type absent), blocking questions, and PeTTa reified profile export; 4 regression tests; 135 tests pass.
- [x] 2026-07-06: Added dependency depth / critical path length detection from extracted DataFlowEdge atoms: computes longest path in the acyclic graph via topological sort + DP, emits `information-flow-dependency-depth-reviewed` obligation (Pass when depth < 4 or acknowledged via 'deep'/'multi-layer'/'multi-hop'/'long chain'/'critical path'/'layered'/'pipeline depth' wording, Unknown with blocking question when deep and unacknowledged), 6 regression tests; 141 tests pass.
- [x] 2026-07-06: Added bottleneck node detection (high fan-in AND high fan-out cross-dimension check): emits `information-flow-bottleneck-node-reviewed` obligation (Pass when no node is both high fan-in and high fan-out, or acknowledged via 'bottleneck'/'single point of failure'/'SPoF'/'critical'/'choke-point'/'overloaded'/'capacity-constrained'/'throughput-limit' wording, Unknown with blocking question when unacknowledged), 5 regression tests; 67 information-flow tests pass.
- [x] 2026-07-06: Fixed O(n^2) validator deduplication bottleneck: replaced linear-scan `all(existing.id != ...)` in `add_validation_obligation` and `add_check` with O(1) set-based lookups using `SpecDocument._obligation_ids` and `_check_ids`. This fixes a 17s timeout on the `auth_service.plain` fixture (auth_service compile dropped from >17s to 0.14s).
- [x] 2026-07-06: Added connected-components detection to the information-flow validation slice: undirected BFS finds disconnected subgraphs in the DataFlowEdge graph, emits `information-flow-connected-components-reviewed` obligation (Pass when acknowledged as independent/separate/standalone, Unknown with blocking question otherwise); 3 regression tests; 170 tests pass.
- [x] 2026-07-05: Added API/webhook input-validation review to the conservative security/privacy slice; 78 tests pass.
- [x] 2026-07-05: Added webhook/callback request-authenticity review to the conservative security/privacy slice; 77 tests pass.
- [x] 2026-07-05: Added API authorization/scope review to the conservative security/privacy slice; 76 tests pass.
- [x] 2026-07-04: Added authentication/API transport-protection review to the conservative security/privacy slice; 75 tests pass.
- [x] 2026-07-04: Added credential rotation/expiry/revocation review to the conservative security/privacy slice; 74 tests pass.
- [x] 2026-07-04: Added authentication/API abuse-protection review to the conservative security/privacy slice; 73 tests pass.
- [x] 2026-07-04: Added real-time/current feature freshness review to the conservative ML/time-series methodology slice; 72 tests pass.
- [x] 2026-07-04: Added PII encryption-scope/key-management review to the conservative security/privacy slice; 69 tests pass.
- [x] 2026-07-04: Added authentication/session-management review (`security-session-management-reviewed`) so auth/login/session specs require MFA, session timeout/expiry, revocation/logout, refresh-token rotation, or reauthentication evidence; 70 tests pass.
- [x] 2026-07-04: Added PII incident-response/breach-notification review to the conservative security/privacy slice; 68 tests pass.
- [x] 2026-07-04: Added PII access audit/logging review to the conservative security/privacy slice; 67 tests pass.
- [x] 2026-07-04: Added rights-request authentication review to the conservative security/privacy slice; 66 tests pass.
- [x] 2026-07-04: Added data-subject rights review to the conservative security/privacy slice; 65 tests pass.
- [x] 2026-07-04: Added purpose-limitation review to the conservative security/privacy slice; 64 tests pass.
- [x] 2026-07-04: Added lawful-basis/consent review to the conservative security/privacy slice; 63 tests pass.
- [x] 2026-07-03: Added third-party/vendor/processor sharing review to the conservative security/privacy slice; 62 tests pass.
- [x] 2026-07-03: Added data-residency/cross-border transfer review to the conservative security/privacy slice; 61 tests pass.
- [x] 2026-07-03: Added first data/sensitivity classification declaration review to the conservative security/privacy slice; 59 tests pass.
- [x] 2026-07-03: Added PII retention/deletion review to the conservative security/privacy slice; 60 tests pass.
- [x] 2026-07-03: Added privilege-escalation review to the conservative security/privacy slice; 59 tests pass.
- [x] 2026-07-03: Added secret log-exposure review to the conservative security/privacy slice; 59 tests pass.
- [x] 2026-07-03: Added security/privacy obligation scaffolding for secrets/PII/access/destructive actions; 59 tests pass.
- [x] 2026-07-03: Added prediction-time feature availability review obligations/questions; 57 tests pass.
- [x] 2026-07-03: Added named baseline-comparator and uncertainty-method review obligations/questions; 55 tests pass.
- [x] 2026-07-03: Added conservative ML temporal split-order review obligations/questions; 54 tests pass.
- [x] 2026-07-03: Added conservative ML metric/task appropriateness review obligations/questions; 52 tests pass.
- [x] 2026-07-03: Added future/label-as-feature leakage review obligations/questions to the conservative ML/time-series methodology pass; 51 tests pass.
- [x] 2026-07-02: Added preprocess-then-split leakage review obligations/questions to the conservative ML/time-series methodology pass; 50 tests pass.
- [x] 2026-07-02: Added baseline-comparison and uncertainty/error-bar obligations/questions to the conservative ML/time-series methodology pass; 49 tests pass; pushed private backup `718a8c8`.
- [x] 2026-07-02: Added conservative ML/time-series methodology obligations/questions; 49 tests pass.
- [x] 2026-07-02: Added question-object blocker validation and unresolved-concept `Blocks` links; 47 tests pass.
- [x] 2026-07-02: Added v0.1 CLI/demo output path, grouped PeTTa atoms, Markdown diagnostics, auth-service review fixture, and stable-ID validation record de-duplication; 46 tests pass.
- [x] 2026-07-02: Tightened section/item/span file-ID provenance consistency plus malformed cross-file regression coverage; 37 tests pass.
- [x] 2026-07-02: Added section/item PlainFile link validation plus malformed-file-link regression coverage; 37 tests pass.
- [x] 2026-07-02: Added Plain file digest validation plus malformed-digest regression coverage; 36 tests pass.
- [x] 2026-07-02: Added source-span byte/line validation plus malformed-span regression coverage; 35 tests pass.
- [x] 2026-07-02: Added validation-layer evidence self-checks (`check-has-evidence`) plus empty-evidence regression coverage; 34 tests pass.
- [x] 2026-07-02: Added validation-layer status self-checks (`check-status-is-known`) plus malformed-status regression coverage; 34 tests pass.
- [x] 2026-07-02: Added document-scoped coverage-label resolution for explicit `[covers:...]` claims; 34 tests pass.
- [x] 2026-07-01: Added `fact-subject-matches-object` validation plus backend subject-mismatch refusals for object-scoped facts; 33 tests pass.
- [x] 2026-07-01: Added orphan acceptance-test coverage obligations/questions with profile-safe `OrphanAcceptanceTest` export and regression coverage; 33 tests pass.
- [x] 2026-07-01: Added duplicate requirement-label ambiguity handling with Unknown checks/questions and regression coverage; 32 tests pass.
- [x] 2026-07-01: Added explicit requirement/test coverage labels (`[id:...]` / `[covers:...]`) with export ground-truth regression and unresolved-target questions; 31 tests pass.
- [x] 2026-07-01: Added PeTTa reified-profile semantic-level obligations (`object-supported-by-petta-reified-profile`) with Unknown/blocking-question handling for RawTextOnly unsupported export; 29 tests pass.
- [x] 2026-07-01: Added validation-obligation provenance/target self-checks (`obligation-has-source-provenance`, `obligation-target-is-declared`) with malformed-obligation regression tests; 28 tests pass.
- [x] 2026-07-01: Tightened concept occurrence line-span indexing for continuation-line references, with regression coverage; 27 tests pass.
- [x] 2026-07-01: Added PeTTa source provenance manifest export with exact source/index atoms and a regression test comparing generated atoms to ground truth; 26 tests pass.
- [x] 2026-07-01: Added validation-layer self-checks (`check-links-known-obligation`, `check-target-matches-obligation`) with malformed diagnostic regression tests; 25 tests pass.
- [x] 2026-07-01: Added Unknown-to-question handling for unsupported fact predicates with `UnsupportedFactPredicate`, `QuestionText`, and `Blocks` facts; 24 tests pass.
- [x] 2026-07-01: Added `petta_reified_v0` profile filtering for supported object-fact predicates/arity plus reified validation rationales, check-obligation links, and check evidence; 23 tests pass.
- [x] 2026-07-01: Added `FACT_SCHEMAS`-based arity/reference validation in `specatom_hs.validators`, including tests for passing supported facts, malformed `Covers` arity, and dangling coverage targets; 21 tests pass.
- [x] 2026-06-30: Added `build_requirement_test_coverage`, conservative requirement/test objects, Pass/Unknown coverage validation, missing acceptance-test questions, and PeTTa reified export of supported object facts/checks; 19 tests pass.
- [x] 2026-06-30: Added conservative concept aliases (`[def:Name]`, `[ref:Name]`, `[concept:Name]`) and bare definition/glossary bullets, with exact occurrence spans and regression coverage.
- [x] 2026-06-30: Preserved multi-line bullet continuations in `specatom_hs.source_indexer` with regression coverage for child/nested acceptance-test bullets.
- [x] 2026-06-30: Added exact-span `ConceptReferenceObject` occurrence atoms for concept definitions/references/external markers plus occurrence-targeted validation checks.
- [x] 2026-06-30: Added `specatom_hs.passes.build_concept_table` plus tests for `ConceptObject`, `ConceptStatus`, `concept-reference-resolved` obligations/checks, and unresolved concept questions.

- [x] 2026-06-29: Added minimal `specatom_hs` scaffold modules (`schema.py`, `passes.py`, `source_indexer.py`, `validators.py`, `backends/petta.py`), `examples/minimal.plain`, and focused tests for source spans, validation records, PeTTa gates, and reified atom stubs.
- [x] 2026-06-29: Created `projects/specatom-hs/` project notebook and source-summary/implementation-plan document from Benjamin's uploaded SpecAtom-HS design PDF and existing project context.
- [x] 2026-06-29: Created local prototype repo `projects/specatom-hs/repos/specatom-hs` with Python stdlib package, parser/indexer, SpecAtom-HS JSON/MeTTa-ish emitter, shallow Appendix G/O templates, crisp validator checks, examples, and 5 passing unit tests.

- [x] 2026-07-06: Added self-dependency review (`information-flow-self-dependency-reviewed`) for direct DataFlowEdge self-loops; unacknowledged component→same-component dependencies create Unknown blocking questions, acknowledged recursion/feedback/fixed-point wording Passes, and ordinary edges Pass; 183 tests pass.
- [x] 2026-07-15: Refused non-string SpecObject IDs in both PeTTa reified emission and executable-skeleton gating, preventing numeric/boolean IDs from aliasing string IDs or crashing validation; focused profile suite passed 47 tests and full suite passed 307 tests; local commit `1367d46`.
- [x] 2026-07-15: Refused non-enum SpecObject roles in both PeTTa reified emission and executable-skeleton gating, preventing malformed runtime roles from raising during `.value` serialization or leaking supported facts; targeted regression passed and full suite passed 308 tests; local commit `d844856`.
- [x] 2026-08-14: Added the PDF §3.5 non-executable logical-IR schema and
  hash-bound machine-readable critical-finding review report; 7 focused and 505
  full provider-free tests pass. Evidence:
  `experiments/20260814T082317Z-plain2metta-v2-logical-ir-schema/RUN.md`.
- [x] 2026-08-14: Persisted logical-review decision transitions against the
  exact report/IR version and expose a compile-admission predicate that requires
  approved logical IR and no open/deferred critical findings. Deserialization
  regenerates the baseline review and rejects dropped/rewritten findings.
  Focused 37/37 and full provider-free 508/508 tests passed. Evidence:
  `experiments/20260814T084048Z-plain2metta-v2-compile-admission/RUN.md`.
- [x] 2026-08-14: Persisted a strict, inert compiler-output bundle only from
  the exact admitted logical IR. Safe relative paths and per-file spec
  traceability are required; publication/execution are absent; executable or
  unknown fields, stale admission, and forged state fail closed. Focused 35/35
  and full provider-free 513/513 tests passed. Evidence:
  `experiments/20260814T085100Z-plain2metta-v2-compiler-output/RUN.md`.
- [x] 2026-08-14: Added exact compiler-output approval admission and a strict,
  inert sandbox-handoff manifest. The manifest is digest-pinned, explicitly
  opt-in, resource-bounded, denies host filesystem/network/secrets, and must
  name exactly the approved generated files; revocation and forged/weak state
  fail closed. Focused 39/39 and full provider-free 517/517 tests passed.
  Evidence: `experiments/20260814T091103Z-plain2metta-v2-output-handoff/RUN.md`.
- [x] Defined the narrow non-invoking sandbox adapter protocol and structured
  test-result artifact; see the Phase 6 evidence above.
- [x] 2026-08-14: Added provider-free gold Phase 2 elaboration/test corpora for
  the auth and ML/time-series examples plus exact requirement-to-test coverage
  admission. Duplicate requirement IDs, unknown coverage targets, and missing
  coverage fail before persistence. Focused 24/24 and full provider-free
  573/573 passed. Evidence:
  `experiments/20260814T113929Z-plain2metta-v2-gold-elaboration-fixtures/RUN.md`.
- [x] Replay the gold elaborations through the real SpecAtom-HS validator and
  define the narrow, explicit review-question disposition boundary. Both gold
  corpora now declare `admission: reject`; their intended human questions are
  matched exactly to real blocking `ExplicitQuestion` objects, and validator
  failures/blockers cannot be mistaken for admission. Focused 10/10 and full
  provider-free 574/574 passed. Evidence:
  `experiments/20260814T115324Z-plain2metta-v2-gold-validator-replay/RUN.md`.
- [x] Add the narrow Phase 3 review-diff artifact over exact original,
  elaborated, and test-spec identities; acceptance: deterministic changed-ID,
  retained-question, and coverage summaries fail closed on stale/malformed
  inputs and do not imply approval. Focused review-diff/query tests passed 9/9
  and the full provider-free suite passed 579/579. Evidence:
  `experiments/20260814T120352Z-plain2metta-v2-phase3-review-diff/RUN.md`.
- [x] 2026-08-14: Added the canonical provider-independent Phase 4 logical-IR
  request/prompt/response envelope. Both exact reviewed snapshot identities
  and bytes are hash-bound; strict logical-IR parsing rejects malformed,
  expanded, executable, duplicate-key, or stale inputs. Focused 50/50 and full
  provider-free 598/598 passed. Evidence:
  `experiments/20260814T132457Z-plain2metta-v2-logical-ir-envelope/RUN.md`.
- [x] 2026-08-14: Added fail-closed logical-review decision replay and exact
  regenerated finding-order stability across all eight PDF §3.5 categories.
  Focused tests passed 96/96 and the full provider-free suite passed 624/624.
  Evidence:
  `experiments/20260814T145802Z-plain2metta-v2-logical-review-replay/RUN.md`.
  Next: provider-independent Phase 5 compilation envelopes bound to the exact
  approved reviewed-spec, reviewed-test, and logical-IR versions.
- [x] 2026-08-14: Added the canonical provider-independent Phase 5 compilation
  request/prompt/response envelope. Request construction first enforces the
  Phase 4 compile-admission gate, then hash-binds the exact reviewed spec,
  reviewed tests, and approved logical IR bytes. Strict completion parsing
  rejects malformed, expanded, duplicate-key, executed, stale, misattributed,
  or guidance-mismatched output. Focused 45/45 and full provider-free 630/630
  tests passed. Evidence:
  `experiments/20260814T151308Z-plain2metta-v2-compilation-envelope/RUN.md`.
  Next: single-call Phase 5 adapter and atomic compiler-output/provenance
  admission transaction.
- [x] 2026-08-14: Added strict opt-in `POST /api/test/<project-id>` through an
  explicitly injected Phase 6 sandbox coordinator. Only `{}` is accepted;
  canonical identity, one-call execution, atomic admission, and fail-closed
  malformed/unconfigured/backend-failure behavior are tested. Focused 24/24
  and full provider-free 647/647 passed. Evidence:
  `experiments/20260814T162600Z-plain2metta-v2-test-post-transport/RUN.md`.
  Next: validated read-only test-result metadata retrieval without output
  bodies, mutation, or execution authority.
- [x] 2026-08-14: Added validated `GET /api/test-result/<project-id>` bound to
  the exact current sandbox handoff and canonical test-result artifact. The
  response exposes statuses, durations, coverage, assertions, and captured
  stream hashes/byte sizes, but never stdout/stderr bodies or mutation or
  execution authority. Focused 38/38 and full provider-free 649/649 passed.
  Evidence:
  `experiments/20260814T163755Z-plain2metta-v2-test-result-query-verification/RUN.md`.
  Next: Phase 7 exact-chain traceability/report retrieval for the completed
  reviewed-input → logical-IR → compiler-output → sandbox-result path.
# 2026-08-14 07:06 PDT — Phase 4 logical-review decision transport

- [x] Expose validated current logical findings without logical-IR bodies.
- [x] Persist repair/waive/defer decisions only against exact current IR and review hashes.
- [x] Require reviewer identity/rationale and fail closed without writes on malformed or stale requests.
- [x] Verify focused 38/38 and full provider-free 612/612 tests; commit `c77da79` (not pushed).
- [x] Provider-free auth and ML/time-series logical-IR gold fixtures with
  complete clause provenance and explicit operational holes were added and
  validated; see
  `experiments/20260814T143255Z-plain2metta-v2-logical-ir-gold-fixtures/RUN.md`.
- Evidence: `experiments/20260814T135749Z-plain2metta-v2-logical-review-decisions/RUN.md`.
# 2026-08-14 Phase 5 compile transport

- [x] Add strict `POST /api/compile/<project-id>` over the explicitly configured
  single-call coordinator, with optional text guidance only, atomic result
  identities, and malformed/alternate/unconfigured/backend-failure cases.
- [x] Validated read-only compiler-output metadata retrieval was added without
  generated-file bodies, publication, approval, or execution authority; see
  `experiments/20260814T155155Z-plain2metta-v2-compiler-output-query/RUN.md`.

# 2026-08-16 Public evaluation example identity gate

- [x] Replace general compiler fixtures in the UI picker with three valid,
  explicit-ID graduated evaluation examples.
- [x] Reject missing and duplicate requirement IDs rather than inventing or
  silently deduplicating traceability identities.
- [x] Verify 6/6 focused, 657/657 full, compile/diff/hygiene, and live Tailnet
  example/sandbox smoke; published commit `c6d5d9a` to draft PR #3.
- Evidence:
  `experiments/20260816T195813Z-plain2metta-evaluation-example-validation/RUN.md`.
- Next: Ben hands-on product feedback; PDF remains deferred.

# 2026-08-16 Public evaluation API input bound

- [x] Enforce the 128 KiB Plain specification limit at the Flask boundary and
  on decoded UTF-8 text, independent of browser controls.
- [x] Verify focused 7/7, full 658/658, compile/diff/hygiene, live valid
  sandbox smoke, and live oversized HTTP 413; published `bfb8cc9` to PR #3.
- Evidence: `experiments/20260816T203100Z-plain2metta-api-input-bound/RUN.md`.
- Next: Ben hands-on product feedback; PDF remains deferred.
# Runtime-validation milestone (2026-08-16)

- [x] Execute generated MeTTa with pinned Hyperon CLI 0.2.10 and require exact
  requirement-derived output, alongside bounded Python execution; fail closed
  on output mismatch. Evidence:
  `experiments/20260816T220300Z-plain2metta-metta-runtime-validation/RUN.md`.

# General semantic validation Stage 4 (2026-08-17)

- [x] Lower exact approved validation plans to canonical, closed-world
  Hypothesis modules with pinned version, settings, seeds, and ancestry.
- [x] Execute only in the bounded Python sandbox and persist immutable runtime
  evidence plus replayable minimal counterexamples and shrink history.
- [x] Pass numerical, authentication, idempotency, seeded-mutant,
  fail-closed, invalidation, 13/13 focused, 690/690 full, hygiene, and live
  dual-runtime gates. Evidence:
  `experiments/20260817T082100Z-plain2metta-general-semantic-validation-stage4/`.
- [x] Stage 5: implemented exact-ancestry canonical TLA+ lowering and bounded
  pinned TLC execution with immutable model-check evidence and source-linked
  traces. Authentication ordering and idempotency/recovery gold models plus
  three mutants passed the 15/15 focused, 696/696 full, hygiene, and live
  dual-runtime gates. Evidence:
  `experiments/20260817T084600Z-plain2metta-general-semantic-validation-stage5/`.
- [x] Stage 6: implemented exact-ancestry canonical SMT-LIB lowering and
  bounded pinned Z3 execution with immutable formula, declaration/source-map,
  model, unsat-core, optional proof, and replay evidence. Contradictory
  contracts, unreachable states, boundary errors, and finite-counterexample
  gold/mutation pairs passed 7/7 focused and 703/703 full tests, hygiene, and
  live dual-runtime gates. Evidence:
  `experiments/20260817T091400Z-plain2metta-general-semantic-validation-stage6/`.
- [x] Stage 7: exact-ancestry Lean 4 semantic kernel passed pinned build,
  focused 6/6, full 709/709, hygiene, and live dual-runtime gates. Evidence:
  `experiments/20260817T092933Z-plain2metta-general-semantic-validation-stage7/`.
- [x] Stage 8: approved-plan dual-runtime normalization and conservative cross-tool verdict synthesis (740/740 tests; experiment `20260817T094100Z-plain2metta-general-semantic-validation-stage8`).
- [x] Stage 9: narrow authorized plan/review/execution/result/trace routes and
  evidence-focused Web UI passed 12/12 focused and 746/746 full tests, pinned
  backend replay, live dual-runtime replay, and hygiene gates. Evidence:
  `experiments/20260817T101110Z-plain2metta-general-semantic-validation-stage9/`.
- [x] Stage 10: five strict Section 9 data artifacts cover pure numerical,
  authentication, temporal lineage, distributed idempotency, and intentionally
  blocked policy shapes. The corpus killed 8/8 relevant mutants; its cosmetic
  survivor was explicitly reviewed. Focused 3/3, full 749/749, pinned backend,
  live dual-runtime, trace, and hygiene gates passed. Evidence:
  `experiments/20260817T102837Z-plain2metta-general-semantic-validation-stage10/`.
- [x] Stage 11: final hardening, clean-checkout reproduction, threat-model
  matrix, pinned-tool replay, browser/API smoke, live dual-runtime replay, and
  audits passed at 72/72 focused and 749/749 full tests. Evidence:
  `experiments/20260817T104940Z-plain2metta-general-semantic-validation-stage11/`.
- [x] Revision 0.2 implementation objective complete. Human review, merge, and
  release remain separate decisions.
