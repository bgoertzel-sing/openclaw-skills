# SpecAtom-HS Plain-to-MeTTa Compiler

- Slug: `specatom-hs`
- Status: `active`
- Created: `2026-06-29`
- Last reviewed: `2026-08-17` (general semantic validation Stage 3 complete)
- Owner: Benjamin Goertzel

## 2026-08-18 architecture/progress report

A current five-page technical report covering completed work, the Stage 1--11
architecture, G0--G6 evidence model, three worked examples, acceptance,
deployment, limitations, and next directions is available as both LaTeX and
PDF in `docs/plain2metta-current-architecture-and-progress.{tex,pdf}`.
The PDF was compiled and text/integrity checked on 2026-08-18.

The original five-page memo was subsequently superseded for explanatory use
by `docs/plain2metta-architecture-and-worked-examples-expanded.{tex,pdf}`.
Its 2026-08-19 revision is a 30-page, 12,802-word report for readers familiar
with Plain, MeTTa, and Lean 4 but new to the Plain2Metta process.  It retains
the original memo for concise status reference while adding detailed pipeline,
backend, example, failure, deployment, and limitation explanations; a new
conceptual introduction and lessons learned; guidance for authoring four
realistic benchmark tasks; and separate one-agent and six-agent development
plans.  Compilation and visual-check evidence is in
`experiments/20260819T153624Z-plain2metta-expanded-r2-compile/`.

## Purpose

Build a conservative compiler pipeline from Plain software specifications into SpecAtom-HS, a typed, source-preserving, context-indexed, evidence-bearing Atomspace-style intermediate representation, then project that IR first to PeTTa/MeTTa reified atoms and later to executable skeletons, MeTTa-IL, Rholang, and PLN reasoning workflows.

## 2026-08-16 public evaluation UI

Deployment update (2026-08-18): PR #3 is merged at main commit `5ce102c` and
the exact accepted release is active on existing ASI:Cloud VM2 as one bounded
systemd worker on `127.0.0.1:8081`. All three exact bundled examples passed
fresh Stage 1--10/G0--G6 canaries. Evidence:
`experiments/20260818T153337Z-plain2metta-pr3-merge-vm2-deployment/`.

The v2 provider-free core now has a browser workbench on public task branch
`agent/plain2metta-public-evaluation-ui` / draft PR #3. At head `752debd` it
exposes exact artifacts, decisions, logical findings, deterministic reference
MeTTa/Python, bounded dual-runtime results, behavioral assertions, and
traceability. Tailnet URL: `http://100.72.218.34:8081/`. MeTTa executes under
pinned Hyperon CLI 0.2.10; Python executes under the bounded subprocess. The
three exact graduated examples pass behavior-specific oracles, while custom or
reworded inputs fail closed as not semantically validated. Evidence:
`experiments/20260816T223000Z-plain2metta-behavior-validation/`.

## 2026-08-16 general semantic validation Stage 0

Revision 0.2's interfaces and trust boundaries are frozen in
`docs/general-semantic-validation-stage0-map.md`. The 662-test and live
three-example baselines remain green. Project-local pinned smokes passed for
Hypothesis, Z3, TLC/Temurin, Lean/Mathlib, and Hyperon with exact provenance
recorded in the Stage 0 experiments. Stage 1 is now the sole objective.

## 2026-08-17 general semantic validation Stage 1

Strict schema `plain2metta-semantic-artifact/v1` now covers contracts,
obligations, plans, generators, oracles, runtime evidence, counterexamples,
and graded verdicts. Canonical document identities, exact ordered input hashes,
reviewed-source ancestry, immutable storage validation, and transitive
invalidation fail closed. Focused 6/6 and full 668/668 tests, static/hygiene
checks, and the three-example live dual-runtime replay passed. Evidence:
`experiments/20260817T073700Z-plain2metta-general-semantic-validation-stage1/`.
Stage 2 finite contract calculus and deterministic reference interpretation is
now the sole objective.

## 2026-08-17 general semantic validation Stage 2

Finite calculus `plain2metta-contract-calculus/v1` defines typed literals,
variables, state, explicit UTC time, bounded quantifiers, trace predicates,
approximation, assumption references, effects, and an ownership locus. The
provider-free interpreter is deterministic and its canonical MeTTa projection
binds the exact Stage 1 contract artifact ID and content hash. Free prose,
unknown operations, malformed types, missing assumptions, and typed holes fail
closed. Focused 9/9 and full 677/677 tests, static/hygiene checks, and the live
three-example dual-runtime replay passed. Evidence:
`experiments/20260817T075100Z-plain2metta-general-semantic-validation-stage2/`.
Stage 3 independent validation-plan synthesis is now the sole objective.

## 2026-08-17 general semantic validation Stage 3

The provider-independent validation-author boundary makes exactly one call
with only the exact reviewed source, strict contracts, and obligations. Strict
plan responses bind the request hash, adapter identity, reviewed contracts,
and Stage 2 ancestry; malformed or misattributed output fails atomically with
no retry. Immutable review records support exact edits and approval decisions,
while unresolved critical meaning blocks approval. Source or contract byte
changes invalidate plans, reviews, and approvals transitively. Focused 12/12
and full 683/683 tests, static/hygiene checks, and the live three-example
dual-runtime replay passed. Evidence:
`experiments/20260817T080828Z-plain2metta-general-semantic-validation-stage3/`.
Stage 4 Hypothesis backend work is now the sole objective.

## 2026-08-17 evaluation UI vertical integration Gate 1

The replacement `POST /api/evaluate` contract is frozen on
`agent/plain2metta-public-evaluation-ui`: exact supported source admission,
canonical Stage 1--8 ancestry, server-composed grades, immutable Stage 10
release metadata, Stage 11 acceptance-only status, adapter bounds, and atomic
fail-closed behavior. Its new real-route test is deliberately red against the
legacy handler at `KeyError: 'ancestry'`; the unchanged evaluation unit suite
passes 5/5. No commit or push was made while the required test is red. Evidence:
`experiments/20260817T174901Z-plain2metta-evaluation-vertical-contract-red/`.
Next: the smallest Stage 1--3 vertical service slice only.

## 2026-08-17 evaluation UI vertical Gate 2 increment 1

The route now rejects unsupported/reworded bytes before semantic work and
returns honest Stage 1--3 ancestry: canonical stored contract and obligation,
checked/interpreted finite calculus, and an independently authored, reviewed,
approved plan. Focused checks passed 13 tests plus 10 subtests. The full
vertical test remains red at missing Stages 4--8, so no commit/push was made.
Evidence: `experiments/20260817T181925Z-plain2metta-evaluation-vertical-stage123-r2/`.

## 2026-08-17 evaluation UI vertical Gate 2 increment 2

The exact approved plan now invokes the existing bounded Hypothesis 6.138.15
coordinator with seed 417 and admits its hash-bound Stage 4 runtime evidence.
The added closed `exact-equality` operation checks only the frozen source-byte
admission claim; it does not claim arbitrary behavioral semantics. Focused
checks passed 14 tests plus 3 subtests and diff hygiene. The full vertical test
remains red at missing Stages 5--8, so no commit or push was made. Evidence:
`experiments/20260817T185258Z-plain2metta-evaluation-vertical-stage4/`.

## 2026-08-17 evaluation UI vertical Gate 2 increment 3

The exact approved shared plan now separates Hypothesis-owned executable cases
from a closed TLC-owned `exact-admission-stability` model, invokes pinned TLC
1.7.4/engine 2.19, and admits one hash-bound Stage 5 evidence node. Focused
checks passed 31 tests plus 3 subtests and diff hygiene. The full vertical test
remains red at missing Stages 6--8, so no commit/push was made. Evidence:
`experiments/20260817T192622Z-plain2metta-evaluation-vertical-stage5-r2/`.

Next: the smallest test-first Stage 6 Z3 slice only.

## 2026-08-17 evaluation UI vertical Gate 2 increment 4

The exact approved shared plan now invokes pinned Z3 4.15.3 for a closed
Boolean-postcondition contradiction and admits its hash-bound Stage 6 proof
evidence. Focused checks passed 40 tests plus 3 subtests and diff hygiene. The
full vertical test remains red at missing Stages 7--8, so no commit/push was
made. Evidence:
`experiments/20260817T195503Z-plain2metta-evaluation-vertical-stage6-r2/`.

Next: the smallest test-first Stage 7 Lean slice only.

## 2026-08-17 evaluation UI vertical Gate 2 increment 5

The exact approved route plan now invokes pinned Lean 4.33.0/Mathlib
`db584cd6` through the existing semantic-kernel coordinator and admits its
hash-bound Stage 7 evidence. Focused checks passed 36 tests plus 3 subtests and
diff hygiene. The frozen full vertical test remains red at missing Stage 8, so
no commit/push was made. Evidence:
`experiments/20260817T202518Z-plain2metta-evaluation-vertical-stage7-r3/` and
`experiments/20260817T202558Z-plain2metta-evaluation-vertical-stage7-boundary/`.

Next: the smallest test-first Stage 8 verdict-composition slice only.

## 2026-08-17 evaluation UI vertical Gate 2 increment 6

The route now feeds the four admitted, exact-plan Stage 4--7 evidence artifacts
to the existing Stage 8 composer and returns the stored verdict identity, hash,
ancestry, and complete server-derived G0--G6 vector. The verdict remains
honestly `unknown` because canonical Hyperon/Python dual-runtime evidence has
not yet been admitted to this project; legacy output is not re-labeled as
composer evidence. Focused checks passed 53 tests plus 3 subtests. The frozen
full vertical test remains red only at missing Stage 10 release metadata, so no
commit/push was made. Evidence:
`experiments/20260817T205530Z-plain2metta-evaluation-vertical-stage8-r2/`.

Next: the smallest test-first Stage 9 server evidence/API projection slice
only; do not remove browser grade synthesis until that server payload exists.

## 2026-08-17 evaluation UI vertical Gate 3 increment 1

The route now returns a Stage 9 `plain2metta-evaluation-evidence/v1`
projection built server-side from the exact Stage 1--8 ancestry and verdict,
including plan/review refs, backend attribution, counterexamples, assumptions,
holes, and residual risk. The new test first failed at missing
`evidence_projection`, then passed. Proportional checks passed 36 tests plus 3
subtests and diff hygiene; the frozen acceptance assertion remains red only at
missing Stage 10 release metadata. Evidence:
`experiments/20260817T212620Z-plain2metta-evaluation-vertical-stage9-r2/`.

Next: the smallest test-first Stage 10 immutable release-metadata slice only.

## 2026-08-17 evaluation UI vertical Gate 3 increment 2

The service now verifies the repository Stage 10 corpus against frozen SHA-256
`d1a795ad448a3aa0433b2c995b918c43d5e3ba90440ab302b656f14b6b72a8ee`
and returns its calibration release ID, mutation threshold, and observed 8/8
result as server-owned release metadata. Changed corpus bytes fail before JSON
admission. Focused checks passed 20/20, the full provider-free suite passed
763/763, and compilation/diff hygiene passed. Evidence:
`experiments/20260817T215712Z-plain2metta-evaluation-vertical-stage10-r2/` and
`experiments/20260817T215756Z-plain2metta-evaluation-vertical-stage10-full/`.
Task-branch commit `3812d0c` is pushed to
`origin/agent/plain2metta-public-evaluation-ui`.

Next: Gate 4, beginning with the smallest test-first removal of browser grade
synthesis plus one adversarial end-to-end case; Stage 11 remains unopened.

## 2026-08-18 evaluation UI vertical Gate 5 clean-checkout replay

The pushed task branch at exact commit `1755ddd` passed the updated Stage 11
script from a fresh single-branch clone with no inherited repository or Lean
build state: pinned Lean rebuilt 3015 jobs, the focused real-route suite passed
106/106, complete provider-free discovery passed 777/777, and compilation plus
repository hygiene passed. Evidence:
`experiments/20260818T072517Z-plain2metta-evaluation-stage11-clean-checkout/`.
The vertical task remains open pending the required independent code-path
audit. No merge, release, deployment, or default-branch change is authorized.

## 2026-08-17 evaluation UI vertical Gate 4 increment 1

The browser now renders only the Stage 9 server evidence projection for its
ancestry, G0--G6 vector, backend details, counterexamples, assumptions, and
holes; the client grade inference and hard-coded G4--G6 values are gone. An
exact source-byte mutation is rejected before the legacy evaluator or Stage 4
backend can run. Focused checks passed 2/2 and the proportional web/API suite
passed 21/21 with diff hygiene. Evidence:
`experiments/20260817T222712Z-plain2metta-evaluation-browser-server-grades/`.
Task-branch-only commit `d5afa00` is pushed.

Next: one smallest test-first stale/mismatched-plan or missing-approval case
with atomic-state assertions; Stage 11 remains unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 2

The real route now has an adversarial missing-approval regression: suppressing
the Stage 3 review transition yields only HTTP 422 before Hypothesis execution,
TLC, Z3, Lean, or the legacy evaluator can run. The proportional web/API suite
passed 16/16. Evidence:
`experiments/20260817T225627Z-plain2metta-evaluation-missing-approval/`.
Task-branch-only commit `b441698` is pushed.

Next: one smallest test-first stale/mismatched-plan or backend-hash-mismatch
case with atomic-state assertions; Stage 11 remains unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 3

A forged Stage 4 result request hash now has a real-route regression proving
error-only HTTP 422 and no TLC, Z3, Lean, or legacy-evaluator execution. The
focused test passed 1/1; the proportional web/API plus Hypothesis suite passed
22/22 with diff hygiene. Evidence:
`experiments/20260817T232547Z-plain2metta-evaluation-stage4-hash-mismatch/` and
`experiments/20260817T232554Z-plain2metta-evaluation-gate4-proportional/`.
Task-branch-only commit `eb2a0a2` is pushed.

Next: one smallest test-first timeout case with atomic-state assertions; Stage
11 remains unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 4

An injected Stage 4 subprocess timeout now returns an error-only HTTP 422 after
one Hypothesis call and before TLC, Z3, Lean, or legacy evaluation. The focused
test passed 1/1; the proportional web/API plus Hypothesis suite passed 23/23
with compilation and diff hygiene. Evidence:
`experiments/20260817T235835Z-plain2metta-evaluation-stage4-timeout/`.
Task-branch-only commit `2fbb55d` is pushed.

Next: one smallest test-first malformed/misattributed-evidence case with
atomic-state assertions; Stage 11 remains unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 5

A Stage 4 adapter result containing one unknown top-level claim now has a
real-route regression proving error-only HTTP 422 before TLC, Z3, Lean, or the
legacy evaluator can run. Focused 1/1 and proportional web/API plus Hypothesis
24/24 tests passed with compilation and diff hygiene. Evidence:
`experiments/20260818T002549Z-plain2metta-evaluation-malformed-stage4-evidence/`.
Task-branch-only commit `bb7b68f` is pushed.

Next: one smallest test-first cross-runtime-disagreement case with conservative
verdict and atomic-state assertions; Stage 11 remains unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 6

A forced Hyperon/Python output disagreement on the real route now proves that
legacy semantic validation fails without being promoted into canonical Stage 8
evidence. The vertical verdict remains conservatively `unknown`, G2/G3 remain
false, and its evidence refs remain exactly the admitted Stage 4--7 records.
Focused 1/1 and proportional evaluation/verdict 36/36 tests passed with diff
hygiene. Evidence:
`experiments/20260818T005400Z-plain2metta-evaluation-cross-runtime-disagreement/`.
Task-branch-only commit `e65e839` is pushed.

Next: one smallest test-first failing property/model/proof case with
conservative-verdict and atomic-state assertions; Stage 11 remains unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 7

A valid failing Stage 4 property run now stays admitted as conservative
evidence: the route returns `status=fail`, G4 false, and the exact persisted
counterexample bound to the composed obligation and runtime-evidence refs.
The focused test first exposed the prior hard-coded empty counterexample list;
the proportional evaluation/verdict/Hypothesis suite passed 42/42 with
compilation and diff hygiene. Evidence:
`experiments/20260818T012701Z-plain2metta-evaluation-failing-property/`.
Task-branch-only commit `93f0581` is pushed.

Next: one smallest test-first inapplicable-backend case with explicit justified
Unknown; Stage 11 remains unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 8

The route now checks TLC applicability before execution. An explicitly
inapplicable Stage 5 backend is not invoked, is exposed as justified Unknown,
keeps G5 false, and is incorporated into the stored composer-produced residual
risk. Focused 1/1 and proportional evaluation/verdict 38/38 tests passed with
compilation and diff hygiene. Evidence:
`experiments/20260818T022403Z-plain2metta-evaluation-inapplicable-tlc/`.
Task-branch-only commit `d4837bc` is pushed.

Next: one test-first failing TLC model-result case; Stage 11 remains unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 9

An admitted failing Stage 5 TLC model now appears as `status=fail` in the
server projection, forces the Stage 8 verdict to fail even when TLC is not a
required method, keeps G5 false, and projects its persisted counterexample
through Stage 9. Focused 1/1 and proportional evaluation/verdict 39/39 tests
passed with compilation and diff hygiene. Evidence:
`experiments/20260818T025041Z-plain2metta-evaluation-failing-tlc-r2/`.
Task-branch-only commit `d894c6c` is pushed.

Next: one smallest failing formal-proof or uncovered transitive-invalidation
case; Stage 11 remains unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 10

A rejected Stage 7 Lean result now has a real-route regression proving an
error-only HTTP 422 after exactly one Lean call and before legacy evaluation.
The coordinator admits no failed proof evidence, so no partial verdict or
grade is projected. Focused 1/1 and proportional evaluation/verdict/Lean 46/46
tests passed with compilation and diff hygiene. Evidence:
`experiments/20260818T032408Z-plain2metta-evaluation-failing-lean/`.
Task-branch-only commit `3317133` is pushed.

Next: one smallest uncovered transitive-invalidation case; Stage 11 remains
unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 11

Replacing the exact source immediately after Stage 3 plan approval now has a
real-route regression proving error-only HTTP 422 before Hypothesis, TLC, Z3,
Lean, or legacy evaluation. The focused test passed 1/1 and the proportional
web/project/plan/verdict suite passed 91/91 with compilation and diff hygiene.
Evidence:
`experiments/20260818T035512Z-plain2metta-evaluation-source-invalidation-r2/`
and
`experiments/20260818T035525Z-plain2metta-evaluation-source-invalidation-proportional/`.
Task-branch-only commit `b545dc8` is pushed.

Next: one smallest uncovered contract/plan/review/approval transitive-
invalidation case; Stage 11 remains unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 12

Revoking the exact approved Stage 3 plan after its independent review now has
a real-route regression proving error-only HTTP 422 before Hypothesis, TLC,
Z3, Lean, or legacy evaluation. Focused 1/1 and proportional
web/project/plan/verdict 92/92 tests passed twice with compilation and diff
hygiene. Evidence:
`experiments/20260818T042448Z-plain2metta-evaluation-approval-revocation/`,
`experiments/20260818T042503Z-plain2metta-evaluation-approval-revocation-proportional/`,
and
`experiments/20260818T042601Z-plain2metta-evaluation-approval-revocation-proportional-r2/`.
Task-branch-only commit `b4da714` is pushed.

Next: one smallest contract, plan-byte, or review invalidation case; Stage 11
remains unopened.

The seed design is Benjamin's 2026-06-29/30 PDF *SpecAtom-HS: A Hyperseed-Compatible Intermediate Representation for Plain-to-MeTTa Compilation, PeTTa Execution, Logical Validation, and PLN Reasoning* and its coding-agent appendices, plus earlier local design notes in `projects/hyperseed-formalizations/repos/hyperseed-formalizations/papers/0005-plain-metta-rholang-spec-compiler/` and `papers/0006-plain-metta-rholang-spec-ir/`.

## Success criteria

Initial milestone:

> Given a small Plain-like input, emit inspectable SpecAtom-HS atoms with stable IDs, source spans, roles, concepts, requirements, tests, evidence wrappers, validation obligations, and a PeTTa reified projection; run structural validation checks and report Pass/Fail/Unknown diagnostics without hallucinating executable semantics.

Observable criteria:

- Source indexer preserves file, section, item, raw text, and source spans for every emitted object.
- PlainAST parser recognizes core Plain sections, bullet nesting, concept references, and acceptance-test attachment.
- SpecAtom-HS core emits object roles, semantic levels, contexts, claims/propositions, evidence, interpretations, bridge suggestions, and validation objects.
- MVP facets cover concepts/types, requirements/obligations, actions, tests/validation experiments, witnesses/backend artifacts, process/resource placeholders, questions, and revisions.
- PeTTa target profile emits reified atoms only from supported facets and marks TODO/unknown witnesses rather than inventing code.
- Validator emits validation obligations and check records for schema integrity, source provenance, undefined concepts, uncovered obligations, TODO witnesses, raw-text-only skeleton violations, and selected information-flow/time checks.
- Tests demonstrate malformed/underspecified inputs produce structured diagnostics/questions rather than silent success.

## Scope

### In scope

- Local project notebook and implementation planning.
- Local prototype repository under `projects/specatom-hs/repos/specatom-hs`.
- Parser and IR schema for a practical Plain subset.
- JSON and PeTTa/MeTTa reified backends.
- Validation obligation generation and crisp structural validators.
- SUMO, EXPO, and Hyperseed bridge records as graded contextual correspondences, not identity mappings.
- Test-run representation as EXPO-like validation experiments with measurements and p-bit evidence.
- Python or another host language for the compiler implementation, as long as emitted target atoms and validation outputs are inspectable.

### Out of scope for now

- Full natural-language understanding of arbitrary English.
- Direct generation of production code from raw Plain text.
- Creating a duplicate remote repository; the authoritative public repository
  is already `bgoertzel-sing/plain2metta`.
- Paid compute.
- Full SUMO/EXPO import, full Hyperseed ontology import, or full PLN execution in the MVP.
- Treating generated PeTTa/Rholang skeletons as verified unless validation evidence supports that claim.

## Current state

The provider-free Phase 2–7 artifact pipeline now has an end-to-end acceptance
replay covering persistence, metadata-only exact-chain retrieval, and transitive
invalidation after original-source mutation. The full suite passes 651/651.
The PDF-derived completion audit records the logical-IR core as complete while
explicitly retaining the web UI, concrete provider adapters, production compiler,
and sandbox executor as incomplete. Evidence:
`20260814T165042Z-plain2metta-v2-end-to-end-acceptance` and
`docs/v2-completion-audit.md`.

Current-HEAD revalidation at `590fc7d` passed the focused acceptance set 64/64
and the complete provider-free suite 651/651, plus byte-compilation, diff, and
repository-hygiene checks. Evidence:
`20260816T131920Z-plain2metta-v2-head-revalidation`.

Next: choose whether the next authorized milestone is the web review UI, a
concrete provider integration, or a separately sandboxed executor integration.

Phase 7 traceability retrieval now independently reconstructs the exact current
nine-artifact chain before returning a report through the existing read-only
query and exact GET route. It rejects stale, incomplete, noncanonical, or
mismatched provenance and exposes no artifact/generated/output bodies or
mutation/execution authority. Focused tests passed 40/40 and the full
provider-free suite passed 649/649. Evidence:
`20260814T164358Z-plain2metta-v2-phase7-exact-chain`.
Local implementation commit: `361bdb7` (not pushed).

Next: provider-free end-to-end Phase 2–7 acceptance replay and a PDF-derived
completion audit.

Phase 6 now has strict opt-in `POST /api/test/<canonical-project-id>` transport.
It is available only when an explicit sandbox coordinator is injected, accepts
only `{}`, invokes the adapter once, and returns only the admitted test-result
identity and hash. Alternate encodings, expanded schemas, missing
configuration, and backend failures fail without writes or retries. Focused
tests passed 24/24 and the full provider-free suite passed 647/647. Evidence:
`20260814T162600Z-plain2metta-v2-test-post-transport`.

Next: validated read-only test-result metadata retrieval without captured
output bodies, mutation, or execution authority.

Phase 6 now has an explicitly configured, provider-independent, single-call
sandbox coordinator. It sends the canonical inert handoff only to an injected
adapter, validates the strict per-test result plus exact request and adapter
attribution, rechecks the current handoff after external I/O, and atomically
saves the result. Adapter failures, malformed/misattributed returns, and
concurrent upstream changes produce no retry or partial result state. No
built-in host executor, network, secrets, or generated-file publisher was
added. Focused tests passed 4/4 and the full provider-free suite passed 644/644.
Evidence: `20260814T160752Z-plain2metta-v2-sandbox-adapter`.
Local implementation commit: `91c9350` (not pushed).

Phase 5 compiler outputs now have a validated read-only metadata boundary and
exact `GET /api/compiler-output/<project-id>` route. The response binds the
current compilation log, inert compiler output, and exact logical IR while
returning only artifact identities, compiler attribution, generated paths,
content hashes, byte sizes, and spec/test traceability IDs. Generated bodies,
guidance, approval/mutation, publication, and execution authority are omitted.
Focused tests passed 38/38 and the full provider-free suite passed 640/640.
Evidence: `20260814T155155Z-plain2metta-v2-compiler-output-query`.
Local implementation commit: `bba7a9c` (not pushed).

Phase 5 now has an explicitly configured, vendor-neutral, single-call
compilation coordinator. It binds the exact approved reviewed specification,
reviewed tests, and logical IR; rechecks those versions after external I/O; and
atomically persists a canonical provider-provenance log plus inert compiler
output. Failure and concurrent mutation leave no partial Phase 5 state, and
reload fails closed on partial, forged, or misattributed logs. Focused tests
passed 50/50 and the full provider-free suite passed 635/635. Evidence:
`20260814T151947Z-plain2metta-v2-compilation-adapter`.
Local implementation commit: `f76d9b4` (not pushed).

Phase 4 now implements all eight PDF §3.5 critical finding categories. The
latest deterministic checks report conflicting contract signatures, typed
operational holes whose expected types disagree with contract outputs, and
requirement obligations whose provenance reaches no contract. Focused tests
passed 20/20 and the full provider-free suite passed 622/622. Evidence:
`20260814T144815Z-plain2metta-v2-logical-ir-type-reachability`.

Phase 4 review now deterministically reports source-linked critical findings
for exact contradictory invariant polarities, invalid ordering endpoints and
cycles, and positive future/test leakage patterns while recognizing explicit
prohibitions. Focused tests passed 14/14 and the full provider-free suite passed
619/619. Evidence: `20260814T144044Z-plain2metta-v2-logical-ir-consistency`.

Provider-free auth and ML/time-series Phase 4 gold skeletons now retain complete
provenance for all 11 reviewed clauses, map every requirement to a planned test,
and represent every grounded operation with exactly one explicit typed
operational hole. Deterministic validator replay retains the unresolved auth
policy and ML model/baseline definitions as source-linked critical findings and
blocks compilation. Focused tests passed 4/4 and the full provider-free suite
passed 616/616. Evidence:
`20260814T143255Z-plain2metta-v2-logical-ir-gold-fixtures`.

The strict Phase 4 transport gate is now complete on the isolated v2 branch:
exact `POST /api/logical-ir/<project-id>` accepts only optional text guidance,
requires an explicitly configured one-call coordinator, and returns only the
atomically admitted interaction-log, logical-IR, and logical-review identities
and hashes. Malformed/alternate requests, missing configuration, and backend
failure fail closed without retry or partial writes. Focused tests passed 23/23
and the full provider-free suite passed 607/607. Evidence:
`20260814T134939Z-plain2metta-v2-logical-ir-post-transport`.
Local implementation commit: `e818489` (not pushed).

As of 2026-08-14 01:42 PDT, the revised Plain2MeTTa v2 implementation has
started on isolated branch `agent/plain2metta-v2-logical-ir` at the preserved
`990ced3` history. The first pure domain seam now represents immutable,
content-addressed project/artifact versions, exact approval bindings, and
transitive invalidation after upstream changes, with strict versioned
serialization. An atomic local filesystem repository now adds traversal-safe
create/get/save/list-status operations and fails closed on malformed, forged,
symlinked, or unexpected state. The existing compiler remains unchanged.
Persisted annotations now bind comments and optional section/item targets to
exact artifact bytes. Logical-IR creation requires explicit approval of both
exact current reviewed inputs, and approval revocation invalidates downstream
IR. A strict non-executable logical-IR schema now carries source-linked
contracts, obligations, dependencies, operational holes, and deterministic
critical findings. Finding decisions persist as immutable review versions, and
compile admission requires exact logical-IR approval plus no open/deferred
critical findings; forged finding removal or rewriting fails closed. Evidence:
local commits `713a720`, `0506f61`, `1cde4d2`, `27008b2`, and `f52a9ac` and experiment records
`20260814T073333Z-plain2metta-v2-artifact-model` and
`20260814T074256Z-plain2metta-v2-filesystem-repository`, plus run
`20260814T080406Z-plain2metta-v2-review-gate-verification`,
`20260814T082317Z-plain2metta-v2-logical-ir-schema`, and
`20260814T084048Z-plain2metta-v2-compile-admission`. Approved compiler output
can now produce an inert, digest-pinned sandbox request, and strict structured
test results persist only when bound to that exact request. No host execution
adapter is implemented. A strict Phase 7 traceability artifact now joins the
full current provenance chain to generated paths, planned tests, exact sandbox
results, coverage classifications, and failure details. Evidence: runs
`20260814T091848Z-plain2metta-v2-sandbox-results` and
`20260814T093310Z-plain2metta-v2-traceability-report`; local commit `580ee3b`.
A framework-neutral read-only service now exposes JSON-ready project status,
artifact-version history, and full or spec-filtered traceability metadata while
omitting artifact bodies and all mutation/execution/provider capabilities.
Evidence: `20260814T094318Z-plain2metta-v2-read-query-boundary`.
A minimal server-independent WSGI adapter now maps that service to exact GET
project/status/version/trace routes. It starts no listener and rejects all
mutation methods and ambiguous route/query identities. Evidence:
`20260814T095338Z-plain2metta-v2-read-transport-verification`.
Local implementation commit: `7da5a0e` (not pushed).
A framework-neutral command service now persists only project creation, exact
artifact-hash annotations, and declared approval decisions. It excludes
generic artifact mutation and provider/compile/execution capabilities.
Evidence: `20260814T100249Z-plain2metta-v2-command-service-verification`.
A separate strict POST-only WSGI adapter now exposes only those three commands.
It requires exact bounded `application/json` framing and rejects duplicate or
unknown fields, alternate identities, stale hashes, and every compile/execution
route. Evidence: `20260814T101530Z-plain2metta-v2-post-transport-verification`.
Local implementation commit: `380e543` (not pushed).
The authoring boundary now also persists optimistic elaborated-spec and
test-spec submissions bound respectively to the exact current original-spec
and elaborated-spec identities. It exposes no generic mutation or provider
invocation seam. Evidence:
`20260814T102140Z-plain2metta-v2-spec-submission` (549/549 full tests).
Local implementation commit: `de832e7` (not pushed).
A pure provider-neutral Phase 2 protocol now binds elaboration requests to the
exact original-spec bytes, binds responses to canonical requests, requires
complete backend/model interaction provenance, and produces self-verifying
validation admission evidence. It preserves original identity/concept markers
and fails closed on validation failures or blocking questions without invoking
any provider. Evidence:
`20260814T103000Z-plain2metta-v2-elaboration-protocol` (554/554 full tests).
Local implementation commit: `4f070ae` (not pushed).
An adapter-independent Phase 2 return service now runs the existing validator
over the combined elaborated/test review corpus and atomically persists the
canonical interaction log plus both outputs only after exact admission. Stored
validation evidence is recomputed on load; stale, rejected, partially written,
or forged interaction state fails closed. Evidence:
`20260814T104243Z-plain2metta-v2-elaboration-admission-persistence` (558/558
full tests). Local implementation commit: `273feaa` (not pushed).
A read-only request-construction service now exports only the exact current
original-spec identity and bytes plus validated optional guidance/section
scope. It performs no state write, provider selection/invocation, retry, or
execution. Evidence:
`20260814T105531Z-plain2metta-v2-elaboration-request-builder` (561/561 full
tests). Local implementation commit: `0990f28` (not pushed).
An explicitly configured vendor-neutral elaboration adapter contract now makes
one call only, verifies exact request binding and backend/model provenance, and
imports the return through atomic validation admission. It provides no retry,
fallback, provider selection, or credential policy. Evidence:
`20260814T110830Z-plain2metta-v2-provider-adapter-contract` (566/566 full tests).
Local implementation commit: `fe06c12` (not pushed).
The adapter input is now a canonical exact-request-bound system/user envelope
with the PDF's Phase 2 constraints and a strict provider-independent JSON
response schema. Prompt mutation, non-JSON, blank, missing/extra-field, and
malformed-provenance returns fail before admission. Evidence:
`20260814T112250Z-plain2metta-v2-elaboration-prompt-envelope` (570/570 full
tests). Provider-free auth and ML gold corpora now have exact requirement/test
coverage plus explicit reject dispositions for intentionally retained review
questions. Real-validator replay proves those questions remain blocking and
that neither corpus is admission-ready; the full provider-free suite passes
574/574. Evidence: `20260814T115324Z-plain2metta-v2-gold-validator-replay`.
A deterministic Phase 3 review report now binds the exact current original,
elaborated, and test artifact IDs/hashes and exposes recomputable unified review
views. Strict serialization rejects expanded schemas, and stale or edited
reports fail closed without adding approval/mutation authority. Evidence:
`20260814T120352Z-plain2metta-v2-phase3-review-diff` (579/579 full tests). The
existing read-only query boundary exposes that recomputed report without
artifact bodies or review-decision authority. Its GET-only WSGI adapter now
maps the exact `/api/review/<project-id>` route with no query parameters and
fails closed on stale chains, missing projects, alternate identities, and
non-GET methods. Evidence:
`20260814T120953Z-plain2metta-v2-phase3-review-transport` (580/580 full tests).
Local implementation commit: `4840c4b` (not pushed).
Exact-version Phase 3 decisions now persist reviewer identity, whole-second UTC
timestamp, optional section/item target and comment, and the disposition in a
strict immutable review log bound to the current elaborated/test hashes. Exact
approval of both full artifacts creates byte-identical reviewed-spec snapshots;
source mutation invalidates the log, snapshots, and approvals transitively.
Evidence: `20260814T122412Z-plain2metta-v2-phase3-review-decisions` (586/586
full tests). Local implementation commit: `1060d65` (not pushed). Next
milestone completed: the bounded POST-only WSGI adapter now exposes exact
`POST /api/review/<project-id>` submission of the canonical review log. It
returns the persisted review-log artifact identity and rejects stale,
expanded, malformed, or alternate-identity requests without a write. Evidence:
`20260814T123554Z-plain2metta-v2-phase3-review-post-transport` (588/588 full
tests). Local implementation commit: `6d14384` (not pushed). Validated current
review-log retrieval is now implemented as a strict read-only query plus exact
`GET /api/review-decisions/<project-id>`. It returns canonical decision metadata
and the log ID/hash only after rebinding to the exact current elaborated/test
refs, without artifact bodies or mutation authority. Evidence:
`20260814T124300Z-plain2metta-v2-phase3-review-decision-query` (590/590 full
tests). Local implementation commit: `519938a` (not pushed). PDF §3.4's
non-identical reviewed-output case is now implemented: review-log v2 carries
an optional exact pair of reviewer edits, full approval materializes immutable
reviewed snapshots from those bytes, unchanged review preserves Phase 2 bytes,
v1 unchanged logs remain readable, and malformed/partial/unapproved/forged
edits fail closed. Metadata queries expose hashes instead of edited bodies.
Evidence: `20260814T125622Z-plain2metta-v2-reviewed-snapshot-edits` (38/38
focused, 593/593 full tests). Local commit: `ee211cc` (not pushed). Next:
bind Phase 4 admission to the exact reviewed snapshot refs. That gate is now
complete: logical-IR artifacts require and directly cite the paired reviewed
snapshot IDs/hashes; Phase 2 refs cannot substitute during reload, and Phase 7
traceability carries the reviewed pair. Evidence:
`20260814T130310Z-plain2metta-v2-phase4-reviewed-inputs` (49/49 focused,
594/594 full tests). Local commit: `92612b3` (not pushed). Next: the narrow
provider-independent Phase 4 request/response envelope bound to those refs.

As of the 2026-07-27 15:30 PDT worker, exact data-flow-edge occurrence spans
also remain aligned after each of the eight non-CR/LF separators recognized by
Python `splitlines()`. Ground truth verifies the extracted phrase slices the
correct UTF-8 bytes after preceding non-ASCII text and remains on physical
line 2.

As of the 2026-07-27 13:30 PDT worker, concept-reference occurrence spans
also remain exact after each of the eight non-CR/LF separators recognized by
Python `splitlines()`. Ground truth verifies `:Café:` slices its exact UTF-8
bytes and remains on physical line 2 after VT, FF, FS, GS, RS, NEL, U+2028,
or U+2029.

As of the 2026-07-27 11:30 PDT worker, semantic occurrence spans remain exact
after each of the eight non-CR/LF separators recognized by Python
`splitlines()`. Ground truth verifies an `Evidence:` atom after VT, FF, FS, GS,
RS, NEL, U+2028, or U+2029 slices the exact non-ASCII UTF-8 bytes and remains
on physical line 2.

As of the 2026-07-27 09:30 PDT worker, derived occurrence-span alignment uses
the same CR/LF/CRLF physical-line model as source indexing. A semantic marker
on a lone-CR continuation line now compiles to its exact non-ASCII UTF-8 byte
slice and correct physical line instead of failing alignment.

As of the 2026-07-27 07:30 PDT worker, the explicit CR/LF/CRLF record
splitter has ground-truth coverage for all eight other separators recognized
by Python `splitlines()` (VT, FF, FS, GS, RS, NEL, U+2028, and U+2029).
Each remains literal item content, preserves its exact UTF-8 byte slice, and
does not create a phantom source line.

As of the 2026-07-27 05:30 PDT worker, source record splitting and source-line
numbering use the same explicit CR/LF/CRLF boundary model. Unicode separators
such as U+2028 remain source content rather than creating phantom lines; exact
UTF-8 ground truth verifies the item text, byte slice, and following line.

As of the 2026-07-27 03:30 PDT worker, source-span line numbers recognize lone
carriage returns as well as LF and CRLF boundaries. Mixed-newline ground truth
confirms section/item line numbers and UTF-8 byte slices across all three
styles without counting CRLF as two line breaks.

As of the 2026-07-27 01:30 PDT worker, a UTF-8 byte-order mark at the start of
a Plain file no longer hides the first section heading. The BOM remains inside
the exact section source span, subsequent item offsets remain true UTF-8 byte
positions, and paired ground truth slices both spans from the encoded source.

As of the 2026-07-26 13:30 PDT worker, `SourceSpan.start_byte` and
`SourceSpan.end_byte` are true UTF-8 byte offsets even when headings or item
text contain non-ASCII characters. Exact ground truth round-trips a
non-ASCII section, item, `:Café:` concept occurrence, and semantic `Evidence:`
occurrence from the encoded source; validators now check encoded file length
and byte-relative lines.

**Reproduced 2026-07-26:** a fresh virtual environment installed the local
`plain2metta` console command and compiled `auth_service`, `task_manager`, and
`ml_timeseries` from copied inputs into JSON, reified MeTTa, and Markdown
diagnostic reports. All three commands exited zero; the preserved output
hashes are in `experiments/20260726T185730Z-v01-three-spec-install-report/`.
This demonstrates the narrow v0.1 install-to-report path, not general-English
compilation or executable-code generation.

As of the 2026-07-26 11:30 PDT worker, canonical object-scoped validation
subtargets cannot contain interior whitespace. The shared crisp-validation,
PeTTa-export, and diagnostics admission policy now refuses both ASCII space
and Unicode em-space variants, closing a visually ambiguous identity gap.

As of the 2026-07-26 09:30 PDT worker, crisp validation and PeTTa/diagnostics
admission share one canonical object-subtarget identity policy. A ground-truth
corpus verifies parity across canonical values and every supported refusal
class, reducing the risk that later hardening changes drift between layers.

As of the 2026-07-26 07:30 PDT worker, Unicode combining marks cannot appear
inside object-scoped validation subtargets. Crisp validation rejects these
visually modifying identities; PeTTa export suppresses the obligation and
linked check; diagnostics exclude their evidence while admitting the
unmodified neighboring target.

As of the 2026-07-26 05:30 PDT worker, Unicode variation selectors cannot
appear inside object-scoped validation subtargets. Crisp validation rejects
these visually ambiguous identities; PeTTa export suppresses the obligation
and linked check; diagnostics exclude their evidence while admitting the
unmodified neighboring target.

As of the 2026-07-26 03:30 PDT worker, object-scoped validation subtargets
must also use Unicode NFKC. Crisp validation rejects compatibility-equivalent
identities such as full-width Latin letters; PeTTa export suppresses the
obligation and linked check; diagnostics exclude their evidence while
admitting the ASCII neighbor.

As of the 2026-07-26 01:30 PDT worker, object-scoped validation subtargets
must use Unicode NFC. Crisp validation rejects decomposed canonically
equivalent identities; PeTTa export suppresses the obligation and linked
check; diagnostics exclude their evidence while admitting the NFC neighbor.

As of the 2026-07-25 23:30 PDT worker, object-scoped validation subtargets
cannot contain Unicode code points unassigned in the runtime Unicode database.
Crisp validation rejects these version-unstable identities; PeTTa export
suppresses the obligation and linked check; diagnostics exclude their evidence
while admitting a canonical neighbor.

As of the 2026-07-25 21:30 PDT worker, object-scoped validation subtargets
cannot contain Unicode private-use code points. Crisp validation rejects these
locally defined identities; PeTTa export suppresses the obligation and linked
check; diagnostics exclude their evidence while admitting a canonical
neighbor.

As of the 2026-07-25 19:30 PDT worker, reserved Unicode noncharacters cannot
appear inside object-scoped validation subtargets. Crisp validation rejects
the non-portable identity; PeTTa export suppresses the obligation and linked
check; diagnostics exclude their evidence while admitting a canonical
neighbor.

As of the 2026-07-25 17:30 PDT worker, object-scoped validation subtargets
containing lone Unicode surrogates fail closed without crashing stable check-ID
generation. Crisp validation rejects the non-scalar identity; PeTTa export
suppresses the obligation and linked check; diagnostics exclude their evidence
while admitting a canonical neighbor.

As of the 2026-07-25 15:30 PDT worker, object-scoped validation subtargets
cannot contain invisible Unicode control characters. A bell-character-bearing
subtarget fails crisp validation; PeTTa export suppresses the obligation and
linked check; diagnostics exclude their evidence while admitting a canonical
neighbor.

As of the 2026-07-25 13:30 PDT worker, object-scoped validation subtargets
cannot evade canonical identity checks with invisible Unicode format
characters in the interior of the suffix. A `fact:<ZERO WIDTH SPACE>0`
subtarget fails crisp validation; PeTTa export suppresses the obligation and
linked check; diagnostics exclude their evidence while admitting a canonical
neighbor.

As of the 2026-07-25 11:30 PDT worker, object-scoped validation subtargets
cannot evade canonical identity checks with trailing invisible Unicode format
padding. A zero-width-space-suffixed subtarget fails crisp validation; PeTTa
export suppresses the obligation and linked check; diagnostics exclude their
evidence while admitting a canonical neighbor.

As of the 2026-07-25 09:30 PDT worker, zero-width-space padding immediately
before an object-scoped validation target's colon separator has exact
end-to-end regression coverage. Crisp validation fails the changed identity;
PeTTa export suppresses the obligation and linked check; diagnostics exclude
their evidence while admitting a canonical neighbor.

As of the 2026-07-25 07:30 PDT worker, object-scoped validation subtargets
cannot evade canonical identity checks with invisible Unicode format padding
immediately after the colon separator. A zero-width-space-padded subtarget
fails crisp validation; PeTTa export suppresses the obligation and linked
checks; diagnostics exclude their evidence while admitting a canonical
neighbor.

As of the 2026-07-25 05:30 PDT worker, object-scoped validation subtargets
cannot evade canonical identity checks with Unicode whitespace immediately
after the colon separator. Crisp validation rejects an em-space-padded
subtarget; PeTTa export suppresses the obligation and linked checks; diagnostics
exclude their evidence while admitting a canonical neighbor.

As of the 2026-07-25 03:30 PDT worker, object-scoped validation targets
cannot evade canonical separator checks with Unicode whitespace such as a
non-breaking space between the owning object ID and colon. Crisp validation
rejects the changed identity; PeTTa export suppresses the obligation and
linked checks; diagnostics exclude their evidence while admitting a canonical
neighbor.

As of the 2026-07-25 01:30 PDT worker, object-scoped validation targets
cannot evade canonical subtarget checks by inserting whitespace between the
owning object ID and its colon separator. Crisp validation rejects the changed
identity; PeTTa export suppresses the obligation and linked checks; diagnostics
exclude their evidence while admitting a canonical neighbor.

As of the 2026-07-24 23:30 PDT worker, object-scoped validation targets
cannot evade canonical subtarget checks by adding whitespace before the owning
object ID. Crisp validation rejects the changed identity; PeTTa export
suppresses the obligation and its linked checks; diagnostics exclude it.

As of the 2026-07-24 21:30 PDT worker, object-scoped validation subtargets
must be canonical identities without leading or trailing whitespace. Crisp
validation rejects padded suffixes, while PeTTa export suppresses their
obligations and linked checks and diagnostics exclude their evidence.

As of the 2026-07-24 19:30 PDT worker, validation targets consisting of a
declared semantic-object ID, a colon, and only whitespace fail closed. Crisp
validation rejects them, while PeTTa export suppresses their obligations and
linked checks and diagnostics exclude them from summaries and reports.

As of the 2026-07-24 17:30 PDT worker, PeTTa export and diagnostics fail
closed on validation targets consisting only of a declared semantic-object ID
and a trailing colon. Such obligations and their linked checks are suppressed
with an exact backend refusal instead of emitting validation claims that crisp
validation has already rejected.

As of the 2026-07-24 15:30 PDT worker, crisp validation rejects an
object-scoped validation target whose colon separator is followed by no
subtarget. A target such as `object:child:` now fails declaration validation,
while `object:child:fact:0` remains accepted.

As of the 2026-07-24 13:30 PDT worker, crisp validation recognizes
object-scoped validation targets owned by colon-bearing semantic object IDs.
Targets such as `object:child:fact:0` no longer falsely fail declaration
validation because of first-colon splitting.

As of the 2026-07-24 11:30 PDT worker, validation-obligation target ownership
uses the longest exact/object-scoped match among declared semantic object IDs.
Colon-bearing child IDs can no longer be mistaken for an emitted parent, so
obligations and diagnostics fail closed when the actual child target is
refused.

As of the 2026-07-24 09:30 PDT worker, PeTTa export suppresses a validation
obligation and its linked checks when its exact or object-scoped target belongs
to a semantic object refused by the target profile. Diagnostics use the same
admission rule, preventing validation summaries from describing non-emitted
semantic targets.

As of the 2026-07-24 07:30 PDT worker, PeTTa export applies provenance
admission before emitting a validation obligation or rationale. An obligation
with malformed or non-emitted source provenance is now suppressed together
with its linked checks, rather than leaving a provenance-free validation claim
beside a refusal.

As of the 2026-07-24 05:30 PDT worker, PeTTa export refuses an entire
semantic object and its facts when optional source provenance is explicitly
malformed (non-string or whitespace-only), rather than emitting an
unprovenanced semantic claim alongside a refusal. Diagnostics already use the
same fail-closed admission rule.

As of the 2026-07-24 03:30 PDT worker, diagnostics admit semantic objects only
when their runtime role is a declared `Role` enum member, matching PeTTa export.
An object with the string lookalike role `"ConceptObject"` can no longer
contribute a valid-looking `ConceptStatus` fact to concept summaries after its
object atom and facts have been refused.

As of the 2026-07-24 01:30 PDT worker, PeTTa export refuses an entire semantic
object and its facts when the object explicitly cites a source span that the
source manifest cannot emit. Diagnostics apply the same admission rule, so
question counts and report text cannot be derived from refused provenance; a
valid neighboring object remains exported and reported.

As of the 2026-07-23 23:30 PDT worker, diagnostics admit checks linked to
source-derived validation obligations only when the cited source span is
actually emittable by the PeTTa source manifest. Scalar-safe but missing or
otherwise refused span references no longer affect summaries, coverage totals,
or detailed reports; backend refusal evidence remains visible.

As of the 2026-07-23 21:30 PDT worker, diagnostics admit checks only when
their linked validation obligation has an absent or backend-safe source-span
identity. Checks linked to obligations refused for structured or blank
provenance no longer affect summaries, coverage totals, or detailed reports,
while refusal evidence remains visible.

As of the 2026-07-23 19:30 PDT worker, diagnostics summaries and Markdown
reports admit checks only when their validation obligation is itself
backend-admissible and the check property and target match that obligation.
Orphan checks, checks linked to refused obligations, and property/target
mismatches retain PeTTa refusal evidence but no longer affect summary counts,
coverage totals, or detailed check output.

As of the 2026-07-23 17:30 PDT worker, diagnostics summaries and Markdown
reports admit only checks whose obligation, property, target, status, and
evidence scalar fields satisfy the PeTTa backend's basic safety gates.
Malformed scalar fields retain backend refusal evidence but no longer affect
Pass/Fail/Unknown counts, property breakdowns, coverage totals, or detailed
check output.

As of the 2026-07-23 15:30 PDT worker, diagnostics validation summaries and
Markdown reports admit only checks with backend-safe, unique identities.
Blank, structured, and duplicate check IDs retain PeTTa refusal evidence but
no longer inflate Pass/Fail/Unknown counts or leak failure evidence.

As of the 2026-07-23 13:30 PDT worker, diagnostics semantic summaries and
question reports admit only objects with list-backed facts containers.
Malformed `None` facts containers retain crisp validation and PeTTa refusal
evidence but no longer inflate question counts.

As of the 2026-07-23 11:30 PDT worker, diagnostics semantic summaries and
question reports admit only semantic levels supported by the PeTTa reified
profile. `RawTextOnly` and malformed level values retain backend refusal
evidence but no longer inflate counts or leak question text.

As of the 2026-07-23 09:30 PDT worker, diagnostics semantic summaries and
question reports use only SpecObjects with backend-safe, unique identities.
Blank, structured, and duplicate object IDs retain crisp validation and PeTTa
refusal evidence but no longer inflate counts or leak question text.

As of the 2026-07-23 07:30 PDT worker, diagnostics semantic summaries and
question reports require exact three-argument schema arity for `ConceptStatus`,
`TestKind`, and `QuestionText`. Over-arity facts retain crisp validation and
PeTTa refusal evidence but no longer inflate counts or leak question text.

As of the 2026-07-23 05:30 PDT worker, diagnostics semantic summaries and
question reports require each consumed fact subject to match its containing
object ID. Mismatched `ConceptStatus`, `TestKind`, and `QuestionText` facts no
longer inflate concept/acceptance-test counts or leak question text, matching
crisp validation and PeTTa refusal behavior.

As of the 2026-07-23 03:30 PDT worker, question validation and diagnostics
fail closed on structured `QuestionText` and `Blocks` values. List-backed
question text is no longer credited or rendered, list-backed obligation links
no longer reach unsafe membership checks, exact fact-argument refusals remain
visible, and a valid neighboring question still passes and is reported.

As of the 2026-07-23 01:30 PDT worker, diagnostics summaries fail closed on
undeclared string object roles. String lookalikes such as `"QuestionObject"`,
`"RequirementObject"`, and `"ValidationObject"` no longer inflate question,
requirement, or acceptance-test counts or leak question text into reports;
PeTTa refusal evidence remains visible and a valid neighboring question is
still counted and reported.

As of the 2026-07-22 23:30 PDT worker, diagnostics concept summaries fail
closed on structured `ConceptStatus` fact values. Malformed list-backed
statuses are excluded from counts while crisp validation and PeTTa refusal
evidence remain visible, and valid neighboring concepts are still counted.

As of the 2026-07-22 21:30 PDT worker, diagnostics summaries fail closed on
undeclared string check statuses. A runtime string such as `"Pass"` is now
classified as Unknown rather than being credited as a valid pass, matching
crisp validation and PeTTa backend refusal behavior.

As of the 2026-07-22 19:30 PDT worker, diagnostics summaries and Markdown
reports fail closed on malformed `CheckRecord` status and property fields.
Structured statuses are classified as Unknown, unhashable properties receive
an explicit invalid-property bucket, coverage filtering remains safe, backend
refusals stay visible, and a valid neighboring check is still counted.

As of the 2026-07-22 17:30 PDT worker, diagnostics summaries and Markdown
reports remain available for documents containing malformed object/check
records, malformed facts containers, and non-tuple facts. Invalid entries are
excluded from summary traversal while their crisp validation failures and
PeTTa backend refusals remain visible; valid neighboring question text is
still reported.

As of the 2026-07-22 15:30 PDT worker, question review and edge-provenance
validation ignore malformed non-tuple facts after the general fact validator
records exact Fail evidence. `None` and integer facts no longer crash either
downstream traversal, while valid neighboring `QuestionText` and `Blocks`
facts still produce Pass checks.

As of the 2026-07-22 13:30 PDT worker, crisp validation mirrors the PeTTa
backend's malformed `CheckRecord` refusal. `None` and list entries now produce
exact record-type Fail checks and are excluded from check identity, target,
and validation-layer traversal, while a valid neighboring check Passes.

As of the 2026-07-22 11:30 PDT worker, crisp validation mirrors the PeTTa
backend's malformed `ValidationObligation` record refusal. `None` and list
entries now produce exact record-type Fail checks and are excluded from
validation-layer indexes and traversal, while a valid neighboring obligation
Passes.

As of the 2026-07-22 09:30 PDT worker, crisp validation and PeTTa export now
fail closed when a valid `SpecObject` carries a malformed facts container.
`None` and mapping containers produce exact Fail checks/backend refusals and
are never iterated or partially emitted, while a valid neighboring list-backed
object Passes and exports.

As of the 2026-07-22 07:30 PDT worker, crisp validation and PeTTa export now
fail closed on malformed `SpecObject` entries. `None` and list entries produce
exact record-type Fail checks/backend refusals and are excluded from downstream
object processing, while a valid neighboring object Passes and exports.

As of the 2026-07-22 05:30 PDT worker, crisp validation mirrors the PeTTa
backend's malformed `PlainItem` record refusal. Non-`PlainItem` manifest
entries now produce exact Fail evidence and are excluded from item identity,
fact-reference, validation-target, and edge-provenance indexes, while a valid
neighboring record Passes.

As of the 2026-07-22 03:30 PDT worker, crisp validation mirrors the PeTTa
backend's malformed `Section` record refusal. Non-`Section` manifest entries
now produce exact Fail evidence and are excluded from section identity,
provenance, and validation-target indexes, while a valid neighboring record
Passes.

As of the 2026-07-22 01:30 PDT worker, crisp validation mirrors the PeTTa
backend's malformed `SourceSpan` record refusal. Non-`SourceSpan` manifest
entries now produce exact Fail evidence and are excluded from downstream span
identity and provenance indexes, while a valid neighboring record Passes.

As of the 2026-07-21 23:30 PDT worker, crisp validation mirrors the PeTTa
backend's malformed `PlainFile` record refusal. Non-`PlainFile` source-manifest
entries now produce exact Fail evidence and are excluded from all downstream
file indexes and provenance checks, while a valid neighboring record Passes.

As of the 2026-07-21 21:30 PDT worker, crisp SourceSpan file-link identity
validation matches the PeTTA backend's non-blank string gate. `None`, list, and
blank file links now Fail with exact evidence and stop before unsafe dictionary
or Counter lookup, while a valid neighboring span explicitly Passes.

As of the 2026-07-21 19:30 PDT worker, crisp PlainItem source-span validation
matches the PeTTa backend's concrete-SourceSpan/non-blank-identity gate. `None`,
container, and blank-identity span values now Fail with exact evidence before
any `.id` dereference, while a valid neighboring item explicitly Passes.

As of the 2026-07-21 17:30 PDT worker, crisp Section source-span validation
matches the PeTTa backend's concrete-SourceSpan/non-blank-identity gate. `None`,
container, and blank-identity span values now Fail with exact evidence before
any `.id` dereference, while a valid neighboring section explicitly Passes.

As of the 2026-07-21 15:30 PDT worker, crisp Section file-link identity
validation matches the PeTTa backend's non-blank string gate. List and blank
file links now Fail with exact evidence and stop before unsafe Counter/set
membership, while a valid neighboring section explicitly Passes.

As of the 2026-07-21 13:30 PDT worker, crisp PlainItem link-identity
validation matches the PeTTa backend's file/section/optional-parent gates.
List and blank links now Fail with exact evidence and stop before unsafe
Counter/dictionary membership, while a valid neighboring item explicitly
Passes.

As of the 2026-07-21 11:30 PDT worker, crisp PlainItem nesting-level
validation matches the PeTTa backend's non-negative, non-boolean integer gate.
Boolean and negative levels now Fail with exact evidence and are refused before
source-manifest export, while a valid neighboring item explicitly Passes.

As of the 2026-07-21 09:30 PDT worker, crisp PlainItem content validation
matches the PeTTa backend's non-negative, non-boolean ordinal and non-blank
raw-text gates. Malformed values now Fail with exact evidence while a valid
neighboring item explicitly Passes.

As of the 2026-07-21 07:30 PDT worker, crisp Section field validation matches
the PeTTa backend's non-blank kind and non-negative, non-boolean ordinal gates.
Malformed kinds and ordinals now Fail with exact evidence before export, while
valid neighboring sections explicitly Pass.

As of the 2026-07-21 05:30 PDT worker, crisp PlainFile field validation
matches the PeTTa backend's non-blank path/digest gates and safely requires
preserved source text to be a string before digest recomputation. Malformed
values now Fail deterministically instead of crashing or reaching export.

As of the 2026-07-21 03:30 PDT worker, crisp SourceSpan bound validation
matches the PeTTa backend's integer/order gates. List, boolean, `None`, and
reversed byte/line bounds now deterministically Fail instead of raising during
numeric comparisons, while valid bounds explicitly Pass.

As of the 2026-07-21 01:30 PDT worker, crisp SpecObject source-span identity
validation matches the PeTTa backend provenance gate. `None` remains valid
optional absence, list and blank identities deterministically Fail, non-blank
string identities Pass, and malformed unhashable provenance no longer crashes
the broader source-or-generated provenance check.

As of the 2026-07-20 23:30 PDT worker, crisp ValidationObligation source-span
identity validation matches the PeTTa backend provenance gate. `None` remains a
valid absent optional provenance value, list and blank identities Fail exactly,
and non-blank string identities Pass before declared-span resolution.

As of the 2026-07-20 21:30 PDT worker, crisp CheckRecord status validation
reports exact unsupported runtime values and types, matching the PeTTa backend's
declared-enum refusal gate without ambiguously stringifying malformed statuses.

As of the 2026-07-20 19:30 PDT worker, crisp CheckRecord target validation
matches the PeTTa backend's target-identity gate. `None`, container, and blank
targets now deterministically Fail, while valid non-blank target text
explicitly Passes.

As of the 2026-07-20 17:30 PDT worker, crisp CheckRecord property validation
matches the PeTTa backend's safe-symbol gate. `None`, container, and blank
properties now deterministically Fail, while valid non-blank property text
explicitly Passes.

As of the 2026-07-20 15:30 PDT worker, crisp CheckRecord obligation-link
validation matches the PeTTa backend's obligation-identity gate. `None`,
container, and blank obligation IDs now deterministically Fail instead of
reaching unsafe dictionary membership, while valid non-blank string links Pass.

As of the 2026-07-20 13:30 PDT worker, crisp ValidationObligation target
validation matches the PeTTa backend's target-identity gate. `None`, container,
and blank targets now deterministically Fail, while non-blank string targets
explicitly Pass before declared-target resolution is considered.

As of the 2026-07-20 11:30 PDT worker, crisp ValidationObligation property
validation matches the PeTTa backend's safe-symbol gate. `None`, container,
and blank properties now deterministically Fail, while non-blank property text
explicitly Passes.

As of the 2026-07-20 09:30 PDT worker, crisp ValidationObligation rationale
validation matches the PeTTa backend's reviewable-text gate. `None`, container,
and blank rationales now deterministically Fail, while non-blank rationale text
explicitly Passes.

As of the 2026-07-20 07:30 PDT worker, crisp CheckRecord evidence validation
matches the PeTTa backend's reviewable-text gate. `None` and container values
now deterministically Fail instead of passing through string coercion, while
non-blank string evidence still Passes and blank strings retain their explicit
empty-evidence failure.

As of the 2026-07-20 05:30 PDT worker, crisp fact-subject validation mirrors
the PeTTa backend's exact string-subject gate. Scalar values such as integer
`7` can no longer alias the owning string object identity `"7"`; malformed
subject types deterministically Fail while exact string owners Pass.

As of the 2026-07-20 03:30 PDT worker, crisp fact validation mirrors the
PeTTa backend's argument gates. Container-valued arguments, non-string object
references, blank/None values, and non-finite floats now receive deterministic
Fail evidence, while supported non-empty scalar arguments explicitly Pass.

As of the 2026-07-20 01:30 PDT worker, crisp validation rejects malformed
non-tuple fact records and non-string predicates with deterministic Fail
evidence, matching the PeTTa backend's existing refusal gates. Malformed facts
also can no longer crash generated-provenance inspection.

As of the 2026-07-19 23:30 PDT worker, crisp validation requires Section and
PlainItem identities to be non-blank strings and excludes malformed identities
from section/item and fact-validation indexes. List-valued and blank IDs now
produce deterministic identity Fail evidence instead of crashing, while valid
neighboring IDs explicitly Pass.

As of the 2026-07-19 21:30 PDT worker, crisp validation requires SourceSpan
identities to be non-blank strings and excludes malformed identities from all
span lookup paths. List-valued and blank span IDs now produce deterministic
identity Fail evidence instead of crashing uniqueness, validation-provenance,
or edge-provenance indexing, while valid neighboring span IDs explicitly Pass.

As of the 2026-07-19 19:30 PDT worker, crisp validation requires PlainFile
identities to be non-blank strings and avoids indexing malformed unhashable IDs.
List-valued and blank file IDs now produce deterministic identity Fail evidence
instead of crashing source-span or validation-target indexing, while valid
neighboring file IDs receive explicit Pass records.

As of the 2026-07-19 17:30 PDT worker, crisp validation explicitly requires
ValidationObligation and CheckRecord identities to be non-blank strings. This
matches the PeTTa backend's existing record-ID gates: malformed list-valued or
blank IDs now receive dedicated backend-safe identity Fail evidence, while
valid IDs receive explicit Pass records.

As of the 2026-07-19 15:30 PDT worker, crisp validation handles unhashable
malformed ValidationObligation and CheckRecord identities without attempting
unsafe Counter, set, or dictionary membership. List-valued IDs now produce
deterministic Fail evidence and downstream validation continues instead of
crashing, matching the PeTTa backend's existing refusal gates.

As of the 2026-07-19 13:30 PDT worker, crisp validation handles unhashable
malformed SpecObject identities without attempting unsafe Counter or set
membership. List-valued IDs now produce deterministic Fail evidence for both
identity uniqueness and backend-safe identity obligations, while downstream
validation continues instead of crashing.

As of the 2026-07-19 11:30 PDT worker, crisp validation requires SpecObject
identities to be non-blank strings. Non-string and whitespace-only IDs now
produce deterministic Fail evidence before the PeTTa backend's existing refusal
gate, while valid identities receive an explicit Pass.

As of the 2026-07-19 09:30 PDT worker, crisp validation handles unhashable
malformed semantic-level values without attempting unsafe set membership. Such
values now produce the existing deterministic Fail identity-level check and
Unknown PeTTa-profile refusal/question instead of crashing validation.

As of the 2026-07-19 07:30 PDT worker, crisp validation explicitly requires
every SpecObject role to be a declared `Role` enum member. Malformed or
unsupported role values now produce a deterministic Fail check before the
PeTTa backend's existing refusal gate, rather than leaving the refusal visible
only during export.

As of the 2026-07-19 05:30 PDT worker, crisp validation handles malformed or
unsupported semantic-level values without dereferencing them as enum members.
It now emits a deterministic Fail identity-level check and an Unknown PeTTa
profile refusal/question instead of crashing before diagnostics are available.

As of the 2026-07-19 03:30 PDT worker, crisp validation now requires unique
ValidationObligation and CheckRecord identities. Duplicate validation-layer IDs
produce one deterministic Fail record with the ambiguous identity and occurrence
count, aligning diagnostics with the PeTTa exporter's existing refusal gates.

As of the 2026-07-19 01:30 PDT worker, crisp validation explicitly requires
unique SpecObject identities. Duplicate object IDs now produce one deterministic
Fail record with the ambiguous identity and occurrence count, matching the
PeTTa exporter's existing duplicate-object refusal gate.

As of the 2026-07-18 23:30 PDT worker, crisp validation explicitly requires
unique indexed PlainFile and SourceSpan identities. Duplicate IDs now produce a
single deterministic Fail record on the ambiguous source record itself, in
addition to the existing fail-closed downstream link diagnostics.

As of the 2026-07-18 21:30 PDT worker, crisp validation now mirrors the PeTTa
exporter's nested-item safety gates. Every declared parent link produces
obligations checking that the parent is uniquely indexed, is not the child
itself, and belongs to the same file and section. Missing or duplicate parents,
self-parenting, and cross-context parenting produce deterministic Fail evidence.

As of the 2026-07-18 19:30 PDT worker, crisp validation explicitly requires
unique indexed Section and PlainItem identities. Duplicate IDs now produce a
single deterministic Fail record with the ambiguous identity and occurrence
count instead of collapsing per-target obligations into an apparently valid
record.

As of the 2026-07-18 17:30 PDT worker, `section-has-source-span` and
`item-has-source-span` require a unique indexed source-span identity. Duplicate
span IDs now produce Fail checks with deterministic ambiguity evidence instead
of passing on set membership while adjacent file-match checks fail.

As of the 2026-07-18 15:30 PDT worker, source-span, section, and item
file-link validation fails closed when an indexed PlainFile ID is duplicated.
The validators no longer treat ambiguous file membership as sufficient or use
the final duplicate for bounds/line checks; exact regression evidence includes
the ambiguous identity and occurrence count.

As of the 2026-07-18 13:30 PDT worker, item section-link validation fails
closed when an indexed section ID is duplicated. `item-has-section` and
`item-file-matches-section-file` no longer select the last duplicate and risk
reporting a false Pass; exact regression coverage requires Fail evidence with
the ambiguous ID and occurrence count.

As of the 2026-07-18 11:30 PDT worker, crisp section/item span-file
validation fails closed when an indexed source-span ID is duplicated. It no
longer selects the last duplicate and risks reporting a false Pass; exact
regression coverage requires Fail evidence identifying the ambiguous ID and
occurrence count.

As of the 2026-07-18 09:30 PDT worker, exact regression coverage now pins
`item-span-file-matches-item-file` to the canonical span in `doc.spans`. A
conflicting embedded `SourceSpan` with the same ID cannot mask an item
cross-file mismatch; the validator emits Fail with the canonical file ID.

As of the 2026-07-18 07:30 PDT worker, the crisp
`section-span-file-matches-section-file` validator resolves a section's span ID
through the indexed `doc.spans` manifest. A conflicting embedded `SourceSpan`
with the same ID can no longer mask a canonical cross-file mismatch and produce
a false Pass validation record.

As of the 2026-07-18 05:30 PDT worker, section provenance validation resolves a section's span ID against the source span actually admitted to the PeTTa manifest before checking file consistency. A conflicting embedded `SourceSpan` record can no longer mask that the canonical emitted span belongs to another file and induce a false cross-file `derived-from` atom.

As of the 2026-07-18 03:32 PDT worker, PeTTa source-manifest export also fails closed on Plain-item parent links: missing, previously refused, self-referential, cross-file, and cross-section parents suppress the child item, and refusal propagates to descendants of a refused parent. Forward references to valid parents remain supported.

As of the 2026-07-18 01:30 PDT worker, when a source manifest is present the PeTTa reified exporter emits object and validation-obligation `derived-from` atoms only for source spans that survived the manifest field, duplicate-ID, and file-link gates. Missing or earlier-refused spans produce structured refusals, valid neighboring links still emit, absent optional provenance remains allowed, and standalone object-only projection remains backward-compatible.

As of the 2026-07-17 23:30 PDT worker, PeTTa reified source-manifest export also refuses Plain items whose file, section, or source span was not actually emitted, and refuses items whose emitted section or span belongs to a different file. Together with the earlier file/span/section gates, this closes the emitted provenance chain through `PlainItem` while retaining valid neighboring manifest atoms.

On 2026-06-29, Benjamin uploaded the revised SpecAtom-HS design PDF and requested a bounded subagent lane. Existing related formalization notes live in `hyperseed-formalizations` and should be treated as design context, not the software implementation home. This project notebook tracks the compiler/prototype itself.

As of 2026-07-17, PeTTa reified export fails closed on malformed source-manifest and validation-record container entries, malformed `PlainFile`, `SourceSpan`, `Section`, and `PlainItem` atom-bearing fields, duplicate source-manifest/object IDs, non-string/blank/duplicate obligation/check IDs, malformed obligation properties, target IDs, rationales, and malformed check links, properties, target IDs, statuses, and evidence. Section/item gates now reject unsafe identities and links, boolean/non-integer or negative ordinals, malformed provenance-span records/IDs, blank item text, and malformed optional parent IDs while valid neighboring records still emit. Non-`PlainFile`, non-`SourceSpan`, non-`Section`, non-`PlainItem`, non-`ValidationObligation`, and non-`CheckRecord` entries produce structured type-bearing refusals instead of crashing. Summary atoms use the first actually emitted file identity rather than dereferencing an invalid first source record. All occurrences of a duplicate file, span, section, item, object, or validation identity are suppressed; checks linked to refused obligations are also suppressed. Duplicate question objects are excluded from document-validation summaries rather than being counted despite having no emitted object atoms. Emitted checks must agree with their cited obligation's property and target, so `check-obligation` atoms and summaries cannot claim ambiguous, dangling, or internally inconsistent validation records. Whitespace-only object and validation-obligation source-span IDs are refused rather than exported as malformed `derived-from` atoms, while genuinely absent optional provenance remains allowed. Runtime values such as integer `7` can no longer alias legitimate string fields in emitted atoms; refused checks are excluded from the document-validation summary so it cannot claim records that were not exported.

A local-only Python stdlib MVP now exists at `projects/specatom-hs/repos/specatom-hs`. It parses a Plain-like subset, preserves source spans and file digests, emits SpecAtom-HS JSON plus MeTTa-ish S-expressions, and runs initial crisp validators. The recommended minimal `specatom_hs` scaffold modules are also present (`schema.py`, `passes.py`, `source_indexer.py`, `validators.py`, `backends/petta.py`) with tests for source indexing, validation records, PeTTa refusal gates, and safe reified emission. A first conservative concept-table/validation pass now distinguishes explicit local definitions, external links, unresolved references, exact-span concept reference occurrence atoms, conservative aliases (`[def:]`, `[ref:]`, `[concept:]`, and bare glossary definitions), and multi-line bullet continuations while keeping nested acceptance-test bullets separate. Concept occurrence spans now also preserve exact marker line numbers for references found on continuation lines, not just exact byte slices. A shallow requirement/test coverage pass now creates requirement and acceptance-test objects, emits `requirement-has-acceptance-test` obligations with Pass/Unknown checks, asks missing-test questions, and exports supported object facts/validation records through the PeTTa reified profile. The validator now also emits scaffold fact-arity and declared-reference checks for supported predicates (`Covers`, `SourceItem`, `Blocks`, `RefersToConcept`, etc.), producing Fail diagnostics for malformed arity or dangling targets and Unknown for predicates outside the current schema. Unknown fact predicates now also create explicit `QuestionObject` records with `UnsupportedFactPredicate` and `Blocks` facts, so profile gaps are reviewable rather than only buried in check text. Unresolved concept questions now also block their exact `concept-reference-resolved` Unknown obligations, and question records are self-validated for non-empty review text plus known blocked obligations. The information-flow slice now also extracts explicit `feeds into`, `pulls ... from`, `pushes ... to`, `ingests ... from`, and `emits ... to` component data-path wording as exact-spanned `DataFlowEdge` atoms, with target-span trimming to avoid swallowing surrounding temporal/preposition words while preserving component labels. The PeTTa backend filters object facts by the supported predicate/arity/subject profile instead of exporting unknown, malformed, or wrong-subject facts, while preserving validation rationales, check-obligation links, and check evidence as reified atoms. Validation-layer self-checks now ensure Plain file digests reproduce from preserved source text, source spans cite indexed files with in-bounds byte ranges and byte-offset-derived line numbers, sections/items link back to indexed PlainFiles/source spans with matching file IDs, validation obligations cite known source spans/targets where available, and each check record cites a known obligation, uses a declared status, preserves non-empty evidence, and matches its declared property/target, catching malformed source/provenance/diagnostic records as first-class failures. The PeTTa reified profile now also emits a source provenance manifest (`plain-file`, `source-span`, `section`, `plain-item`, and `derived-from`) with regression tests comparing generated atoms to indexed ground truth, plus grouped `.metta` output sections for source, object, validation, and refusal review. PeTTa reified-profile semantic-level support is now explicit in validation: unsupported levels such as `RawTextOnly` create `object-supported-by-petta-reified-profile` Unknown checks and blocking `QuestionObject`s instead of being left only to backend refusals. Phase 2 semantic markers now align source spans by raw-text occurrence index, so repeated same-item markers and continuation-line markers cite exact slices instead of the first matching text. `Bridge:` markers now accept arbitrary ontology labels but keep the conservative support whitelist (`sumo`, `expo`, `hyperseed`): unsupported labels still become source-spanned `BridgeObject`s, Unknown `bridge-profile-supported` checks, and blocking review questions rather than being silently skipped. Explicit `Confidence:` markers now create source-spanned epistemic metadata with normalized `Confidence`/`ConfidenceValue` atoms; values in `[0,1]` (including percentages such as `83%`) pass `confidence-value-in-unit-interval`, while out-of-range or non-numeric values produce Unknown checks plus blocking `UnsupportedConfidenceValue` questions rather than being treated as truth values or silently ignored. Bridge relation validation now keeps correspondences conservative: supported labels such as `related`, `analogy`, `refines`, and `approximates` pass `bridge-relation-conservative`, while identity/equivalence-style labels such as `identical` produce Unknown checks plus blocking `UnsupportedBridgeRelation` questions instead of being accepted as ontology identity claims. Explicit `Revision:` markers now create source-spanned `RevisionObject`s with `Revision`/`RevisionText`/`Revises` facts, a `revision-has-source-provenance` Pass check, and PeTTa reified export support without inferring migration semantics. A first Phase 3 witness/backend-artifact marker slice now detects explicit `Witness:`, `Artifact:`, and `Backend artifact:` annotations, emits source-spanned `BackendArtifact` objects with `Witness`/`WitnessText`/`WitnessFor` facts, passes concrete file/test/log/commit/hash-style artifacts, and turns TODO/raw-text-only/non-concrete placeholders into `witness-artifact-reviewable` Unknown checks plus exported `MissingWitnessArtifact` blocking questions rather than inventing executable evidence. Requirement/test coverage now supports document-scoped explicit requirement labels (`[id:...]`) and acceptance-test coverage claims (`[covers:...]`), exports `RequirementLabel`/`CoverageClaim` atoms, avoids proximity-only misattachment when labels resolve (including forward references to later requirement sections), turns unresolved coverage labels into Unknown checks plus blocking questions, refuses ambiguous duplicate-label coverage by emitting `requirement-label-is-unique` / `coverage-claim-target-resolved` Unknown checks plus duplicate/ambiguous target questions, and flags orphan acceptance tests with `acceptance-test-covers-requirement` Unknown checks plus exported `OrphanAcceptanceTest` blocking questions. The v0.2 methodology slice now detects ML/time-series-like specs and emits conservative obligations for evaluation metric declaration, metric/task appropriateness review, horizon/frequency declaration, reproducibility evidence, train-only preprocessing fit scope, explicit preprocess-then-split leakage review, future/label-as-feature leakage review, prediction-time feature availability review, real-time/current feature freshness review, temporal split-order review, baseline comparison, named baseline-comparator review, uncertainty/error-bar reporting, and named uncertainty-method review; missing evidence becomes `MissingMethodologyEvidence` blocking questions and supported PeTTa atoms. Explicit author `Question:` markers now also become source-spanned `QuestionObject`s with `ExplicitQuestion`/`QuestionText`/`QuestionsObject`/`SourceItem`/`Blocks` facts, `explicit-question-needs-answer` Unknown checks, and PeTTa reified export support so review questions are preserved as blocking obligations rather than ordinary prose. Explicit `Open issue:` / `Issue:` markers now likewise become source-spanned blocking question objects with `OpenIssue`/`OpenIssueText`/`IssueFor` facts and `open-issue-needs-resolution` Unknown checks, preserving unresolved issue prose as review obligations while stopping spans before following markers. Explicit `TODO:` / `To-do:` markers now likewise become source-spanned blocking question objects with `TodoItem`/`TodoText`/`TodoFor` facts and `todo-item-needs-resolution` Unknown checks, preserving incomplete spec/implementation notes as blocking review obligations while stopping spans before following markers. Explicit `Priority:` markers now create source-spanned review objects with `Priority`/`PriorityText`/`PriorityValue`/`PriorityFor` facts, Pass/Unknown `priority-value-reviewable` checks, and `UnsupportedPriorityValue` blocking questions for unsupported or placeholder values. Explicit `Owner:` / `Assignee:` markers now create source-spanned accountability review objects with `Owner`/`OwnerText`/`OwnerFor` facts, Pass/Unknown `owner-assignment-reviewable` checks, and `MissingOwnerAssignment` blocking questions for TODO/TBD/unassigned placeholders. Explicit `Deprecated:` / `Deprecation:` and `Replacement:` markers now create source-spanned review objects with `Deprecated`/`DeprecatedText`/`DeprecatedFor` and `Replacement`/`ReplacementText`/`Replaces` facts; same-item replacements link via `DeprecatedReplacedBy`, while missing replacement/migration/sunset/removal dispositions produce Unknown checks plus exported `MissingDeprecationDisposition` blocking questions. Explicit `Acceptance Criterion:` / `Acceptance Criteria:` / `Criterion:` markers now create source-spanned validation objects with `AcceptanceCriterion`/`AcceptanceCriterionText`/`AcceptanceCriterionFor` facts, Pass/Unknown `acceptance-criterion-reviewable` checks, and `MissingAcceptanceCriterionDetail` blocking questions for TODO/TBD/raw-text-only placeholders. Explicit `Assumption:` markers now become source-spanned `AssumptionObject`s with `Assumption`/`AssumptionText`/`AssumptionFor` facts, same-item evidence links via `AssumptionEvidence`, and `assumption-has-explicit-evidence` Pass/Unknown checks plus exported `MissingAssumptionEvidence` blocking questions when evidence is absent. Explicit `Invariant:` markers now become source-spanned proposition objects with `Invariant`/`InvariantText`/`InvariantFor` facts, same-item evidence links via `InvariantEvidence`, and `invariant-has-explicit-evidence` Pass/Unknown checks plus exported `MissingInvariantEvidence` blocking questions when evidence is absent. Explicit `Constraint:` markers now become source-spanned obligation objects with `Constraint`/`ConstraintText`/`ConstraintFor` facts, same-item evidence links via `ConstraintEvidence`, and `constraint-has-explicit-evidence` Pass/Unknown checks plus exported `MissingConstraintEvidence` blocking questions when evidence is absent. Explicit `Risk:` and `Mitigation:` markers now create source-spanned review objects with `Risk`/`RiskText`/`RiskFor` and `RiskMitigation`/`RiskMitigationText`/`MitigatesRiskFor` facts, same-item mitigation links via `RiskMitigatedBy`, and `risk-has-explicit-mitigation` Pass/Unknown checks plus exported `MissingRiskMitigation` blocking questions when mitigation/control evidence is absent. Explicit `Rationale:` markers now become source-spanned explanation objects with `Rationale`/`RationaleText`/`RationaleFor` facts, `rationale-has-source-provenance` Pass checks, and PeTTa reified export support, preserving design reasons without treating them as executable semantics. Process reviewability now also accepts script/config/build artifact-only declarations such as `scripts/deploy.sh` and `Makefile` as concrete process evidence, and resource reviewability accepts direct artifact-path-only declarations such as `docs/capacity.v1.yaml` and `infra/limits.toml`, without relaxing TODO/raw-text-only refusal behavior. A first v0.2 security/privacy slice now detects secrets, PII/personal data, access/auth/role boundaries, and destructive-action wording, emitting Unknown checks plus `MissingSecurityPrivacyEvidence` blocking questions when handling evidence is absent and exporting supported review/question atoms through the PeTTa profile. It now also requires explicit data/sensitivity classification evidence for PII/personal-data specs via `privacy-data-classification-declared`, encryption-scope/transport/key-management evidence via `privacy-encryption-scope-reviewed`, lawful-basis/consent evidence via `privacy-lawful-basis-reviewed`, retention/deletion/minimization evidence via `privacy-retention-deletion-reviewed`, purpose-limitation/use-limitation/secondary-use-review evidence via `privacy-purpose-limitation-reviewed`, data-subject/access/correction/portability/opt-out/privacy-rights evidence via `privacy-data-subject-rights-reviewed`, identity/authentication evidence for rights/access/deletion/erasure requests via `privacy-rights-request-authentication-reviewed`, access audit/logging/monitoring evidence via `privacy-pii-access-audit-reviewed` when PII appears with access/admin/role wording, incident-response/breach-notification evidence via `privacy-incident-response-reviewed`, data-residency/cross-border transfer policy evidence via `privacy-data-residency-reviewed` when PII appears with region/country/jurisdiction/cross-border wording, third-party/vendor/processor sharing evidence via `privacy-third-party-sharing-reviewed` when PII appears with vendor/processor/partner/external-service/export/upload/share wording, and privilege-escalation review evidence for access/auth/admin/role specs via `security-privilege-escalation-reviewed`, authentication/session-management evidence via `security-session-management-reviewed` when login/auth/session wording appears, authentication/API abuse-protection evidence via `security-auth-abuse-protection-reviewed` when auth/login/API/password/token wording appears, API authorization/scope evidence via `security-api-authorization-reviewed` when API/endpoint/request wording appears with auth/access context, authentication/API transport-protection evidence via `security-auth-transport-protection-reviewed` when auth/login/API/password/token wording appears, credential rotation/expiry/revocation evidence via `security-credential-rotation-reviewed` when secrets/tokens/passwords/credentials appear, API/webhook input-validation evidence via `security-api-input-validation-reviewed` when request/payload/body/query/parameter/JSON/form/upload wording appears with API/webhook context, webhook/callback request-authenticity plus replay-protection evidence via `security-webhook-request-authenticity-reviewed` when webhook/callback/external-request wording appears, and safe generic/redacted/sanitized API/webhook error-response evidence via `security-api-error-disclosure-reviewed` when API/webhook error/exception/stack-trace/debug/diagnostic wording appears, defaulting to Unknown blocking questions when absent. The next step is deeper Appendix N/P methodology/security semantics, broader information-flow/temporal availability checks, and richer profile-aware projection beyond the current scaffold predicates/source manifest. A dependency depth / critical path length detection check now computes the longest path in the acyclic DataFlowEdge graph and flags deep dependency chains (>= 4 edges) for review. A bottleneck node detection check now flags components that are both high fan-in and high fan-out (>= 3 in each dimension), emitting `information-flow-bottleneck-node-reviewed` obligations with Unknown blocking questions when unacknowledged. The PeTTa reified profile now also exports an `information-flow-graph-summary` atom with quick-triage graph stats (node count, edge count, temporal edge count, source/sink counts, cycle count, connected component count, max depth, bottleneck count) computed from DataFlowEdge and TemporalOrderEdge facts. A bidirectional edge review check now detects when A→B and B→A both exist in the DataFlowEdge graph, emitting `information-flow-bidirectional-edge-reviewed` obligations (Pass when no bidirectional pairs or acknowledged via request-response/feedback-loop/bidirectional wording, Unknown with blocking questions when unacknowledged). A Phase 3 process/resource/dependency marker slice now detects explicit `Process:`, `Resource:`, and `Dependency:`/`Dependencies:` annotations, emits source-spanned `ProcessObject`/`ResourceObject` atoms with `Process`/`ProcessText`/`ProcessFor`, `Resource`/`ResourceText`/`ResourceFor`, and `Dependency`/`DependencyText`/`DependencyFor` facts, passes concrete operational/capacity/service/API/file/package/dataset/artifact evidence via `process-definition-reviewable`/`resource-requirement-reviewable`/`dependency-requirement-reviewable`, and turns TODO/vague placeholders into Unknown checks plus `MissingProcessDefinition`/`MissingResourceRequirement`/`MissingDependencyDetail` blocking questions rather than inventing operational semantics. Witness/backend-artifact marker parsing has also been tightened to stop before following same-item semantic markers such as `Outcome:` while preserving file paths with periods, keeping exact-span witness atoms separate from adjacent proposition atoms; concrete witness recognition now treats `.yaml`, `.yml`, and `.sh` operational artifacts as reviewable evidence rather than missing-witness placeholders. Evidence, rationale, interpretation, scope/context, confidence, epistemic-status, process, and resource marker parsing now use the same boundary discipline, so file-path/test-selector/artifact references such as `tests/test_cli.py::CliTests`, `docs/v01-profile.md`, `out/semantic-map.metta`, `docs/v0.2.review.md`, `scripts/demo.sh`, and `docs/capacity.v1.yaml`, plus percent confidences such as `83%`, are preserved while adjacent semantic markers keep separate exact spans.

A first v0.2 information-flow validation slice now detects data-flow/dependency wording (inputs, outputs, consumes, produces, reads, writes, sends, receives, pipelines, upstream/downstream) and emits conservative obligations for input declaration, output declaration, dependency-direction declaration, temporal-availability review, and circular-dependency termination review; missing evidence becomes `MissingInformationFlowEvidence` blocking questions and supported PeTTa atoms. It also extracts explicit component-level data-path edges ("X reads from Y", "X writes to Y", "X consumes from Y", "X receives ... from Y", "X pulls ... from Y", "X ingests ... from Y", "X pushes ... to Y", "X emits ... to Y", "X feeds into Y", "X depends on Y") as `DataFlowEdge` atoms with exact matched edge-phrase source spans and an `information-flow-data-path-declared` obligation that passes when edges are found and produces Unknown blocking questions when only vague wording exists. Duplicate/parallel declarations of the same normalized edge now emit `information-flow-duplicate-edge-reviewed` (Pass when absent or acknowledged, Unknown with blocking questions when unacknowledged). Direct self-loop edges now get a dedicated `information-flow-self-dependency-reviewed` obligation before broader graph-cycle review, producing Unknown blocking questions for unacknowledged component→same-component dependencies and Pass when recursion/feedback/fixed-point wording acknowledges intent. Transitive dependency chain detection builds an adjacency graph from extracted edges, detects A→B→C chains via bounded BFS, and emits `information-flow-transitive-dependency-reviewed` obligations (Pass when acknowledged, Unknown with blocking questions when not). Graph-based cycle detection via DFS white/gray/black coloring finds actual cycles in the extracted edge graph and emits `information-flow-cycle-detected` obligations (Pass when acyclic, Unknown with blocking questions when cycles exist). Fan-out/fan-in concentration detection computes per-node out-degree and in-degree from extracted edges and triggers `information-flow-fan-out-reviewed` and `information-flow-fan-in-reviewed` obligations when any component has >=3 edges in one direction (Pass when acknowledged or below threshold, Unknown with blocking questions when unacknowledged). Source/sink identification finds source nodes (no incoming edges) and sink nodes (no outgoing edges) and emits `information-flow-source-sink-identified` obligations (Pass when both exist, Unknown with blocking questions when missing). BFS-based source reachability checks whether all nodes are reachable from source nodes and emits `information-flow-reachability-reviewed` obligations (Pass when all reachable, Unknown with blocking questions when unreachable nodes exist); reverse-BFS sink reachability checks whether all nodes can reach at least one sink and emits `information-flow-sink-reachability-reviewed` obligations (Pass when all nodes have a sink path, Unknown with blocking questions for trapped cycles/dead ends/missing outputs). Isolated component detection finds components mentioned with broader data-flow verbs (`flows to`, `provides to`, `gets from`, `pulls from`, `pushes to`) that do not produce explicit DataFlowEdge atoms, and emits `information-flow-isolated-component-reviewed` obligations (Pass when all mentioned components appear in edges, Unknown with blocking questions when isolated components are found). Redundant path detection finds all simple paths between node pairs in the edge graph and, when multiple distinct paths (direct + indirect) connect the same pair, emits `information-flow-redundant-path-reviewed` obligations (Pass when no redundant paths or spec acknowledges redundancy via 'redundant'/'backup'/'fallback'/'failover'/'fault tolerance'/'high availability'/'duplicate'/'resilient'/'replicated' wording, Unknown with blocking questions when unacknowledged). Temporal ordering impossibility detection extracts explicit "A before/after/then/precedes/follows B" statements from spec text, builds a temporal ordering graph, detects impossible cycles via DFS, emits exact-source-spanned `TemporalOrderEdge` atoms and `information-flow-temporal-impossibility-reviewed` obligations (Fail on impossible cycles, Pass when consistent or no temporal statements) with blocking questions.

## Repositories

| Role | Remote | Local path | Branch/default | Pinned/reference commit |
|---|---|---|---|---|
| design context | `https://github.com/bgoertzel-sing/hyperseed-formalizations` | `projects/hyperseed-formalizations/repos/hyperseed-formalizations` | `agent/protomegatron-formalization-0002` | contains notes 0005/0006; no changes made by this task |
| Plain2Metta public implementation | public `https://github.com/bgoertzel-sing/plain2metta` | `projects/specatom-hs/repos/specatom-hs` | default `main`; launch branch `agent/plain2metta-public-launch` | repository renamed/published 2026-07-15; internal package/IR remains `specatom_hs`; draft PR #2 updates default-branch branding and carries current conservative compiler work through `351bad1` |

## Environments

- Workspace: `/home/openclaw/research-agent`.
- No paid compute approved.
- No compiler implementation environment exists yet.
- PeTTa/SWI-Prolog runtime may later reuse the local PeTTa/SWI stack already validated for `petta-chem`, but the first SpecAtom-HS compiler prototype can be host-language based.

## Key results

- 2026-07-15: Closed a PeTTa fact-predicate type fail-open: non-string predicate values are now refused before schema lookup instead of being stringified into potentially supported predicate names; exact reified/executable ground-truth tests pass; 312 tests pass.
- 2026-07-14: Closed an executable-skeleton identity fail-open by refusing empty object IDs and empty object-reference targets explicitly; added direct and referenced ground-truth tests; 293 tests pass.
- 2026-07-13: Made arbitrary-depth executable-reference refusal selection globally canonical across mixed-depth branches by traversing complete reference paths in lexicographic order; added ground truth where an `alpha` deep RawTextOnly path competes with a shallower `zeta` path; 290 tests pass.
- 2026-07-13: Made direct executable-skeleton refusal record ordering deterministic across originating fact insertion order by canonically sorting candidate facts; added reversed-order two-target RawTextOnly ground truth; 289 tests pass.
- 2026-07-13: Made arbitrary-depth executable-reference refusal selection deterministic across fact insertion order by canonically sorting descendant references before traversal; added reversed-order deep-path ground truth; 288 tests pass.
- 2026-07-13: Locked executable-skeleton refusal precedence across direct and one-to-three-edge references: unsupported semantic levels such as `TemplateParsed` remain the reported cause even when the target also lacks source provenance; added a parameterized ground-truth regression; 286 tests pass.
- 2026-07-11: Added explicit `Axiom:` marker support with exact source spans, same-item Evidence/Proof support links, Unknown missing-justification obligations, `MissingAxiomJustification` blocking questions, PeTTa export coverage, and 266 passing tests.
- 2026-07-11: Added explicit `Hypothesis:` proposition markers with exact source spans, same-item evidence links, Pass/Unknown evidence obligations, `MissingHypothesisEvidence` blocking questions, PeTTa export coverage, and 258 passing tests.
- 2026-07-11: Added explicit `Precondition:` / `Postcondition:` formal condition markers with exact source spans, same-item evidence links, Pass/Unknown evidence obligations, `MissingPreconditionEvidence` / `MissingPostconditionEvidence` blocking questions, PeTTa export coverage, and 255 passing tests.
- 2026-07-10: Added explicit `Metric:` validation markers with source-spanned measurable criteria, Pass/Unknown `metric-definition-reviewable` checks, `MissingMetricDefinition` blocking questions, PeTTa export coverage, and 251 passing tests.
- 2026-07-10: Added explicit `Acceptance Criterion:` / `Acceptance Criteria:` / `Criterion:` validation markers with source-spanned review criteria, Pass/Unknown `acceptance-criterion-reviewable` checks, `MissingAcceptanceCriterionDetail` blocking questions, PeTTa export coverage, and 245 passing tests.
- 2026-07-10: Added explicit `Priority:` review markers with source-spanned priority values, Pass/Unknown `priority-value-reviewable` checks, `UnsupportedPriorityValue` blocking questions, PeTTa export coverage, and 241 passing tests.
- 2026-07-10: Added explicit `Owner:` / `Assignee:` accountability markers with Pass/Unknown owner-assignment review, `MissingOwnerAssignment` blocking questions, PeTTa export coverage, and 239 passing tests.
- 2026-06-29: Created project notebook and source-plan summary at `projects/specatom-hs/docs/source-summary.md`.
- 2026-06-29: Created local-only Python stdlib MVP in `projects/specatom-hs/repos/specatom-hs`; 5 unit tests pass and two examples generate JSON/MeTTa-ish outputs.
- 2026-07-15: With Ben's explicit approval, renamed the existing remote to
  `bgoertzel-sing/plain2metta`, made it public, updated the description and
  README branding, pushed `agent/plain2metta-public-launch`, and opened draft
  PR #2. A tracked-tree secret-like scan found no matches; the MIT license and
  `specatom_hs` internal package name are retained.
- 2026-06-30: Added conservative `specatom_hs` concept-table pass with `ConceptObject`/`ConceptStatus`, external-link recognition, unresolved-question records, and `concept-reference-resolved` validation checks; 14 unit tests pass.
- 2026-06-30: Added exact-span `ConceptReferenceObject` occurrence atoms for definitions/references/external markers and occurrence-targeted validation checks; 15 unit tests pass.
- 2026-06-30: Added `specatom_hs.source_indexer` support for multi-line bullet continuations that extend source spans/raw text without swallowing nested bullets; 16 unit tests pass.
- 2026-06-30: Added conservative concept grammar aliases (`[def:]`, `[ref:]`, `[concept:]`) plus bare definition/glossary bullets and raw-text-to-source span alignment; 17 unit tests pass.
- 2026-06-30: Added shallow requirement/test coverage pass plus PeTTa reified export of supported object facts and validation records; 19 unit tests pass.
- 2026-07-01: Added scaffold fact-arity and declared-reference validation with regression tests for good facts, malformed arity, and dangling references; 21 unit tests pass.
- 2026-07-01: Tightened `petta_reified_v0` profile filtering so unsupported/malformed object facts produce backend refusals instead of exported atoms, and validation rationales/evidence are preserved in the reified projection; 23 unit tests pass.
- 2026-07-01: Added Unknown-to-question handling for unsupported object-fact predicates, emitting `QuestionObject` records that block the relevant profile/arity obligation; 24 unit tests pass.
- 2026-07-01: Added validation-layer self-checks for check records (`check-links-known-obligation`, `check-target-matches-obligation`) with malformed-diagnostic regression coverage; 25 unit tests pass.
- 2026-07-01: Added validation-obligation provenance/target self-checks (`obligation-has-source-provenance`, `obligation-target-is-declared`) with malformed-obligation regression coverage; 28 unit tests pass.
- 2026-07-01: Added PeTTa source provenance manifest export with exact source/index atoms and ground-truth regression coverage; 26 unit tests pass.
- 2026-07-01: Tightened concept occurrence spans to preserve exact marker line numbers for references found on multi-line bullet continuations; 27 unit tests pass.
- 2026-07-01: Added PeTTa reified-profile semantic-level validation with blocking questions for unsupported levels such as `RawTextOnly`; 29 unit tests pass.
- 2026-07-01: Added explicit requirement coverage labels (`[id:...]` / `[covers:...]`) with `RequirementLabel`/`CoverageClaim` export and Unknown questions for unresolved coverage targets; 31 unit tests pass.
- 2026-07-01: Added duplicate requirement-label ambiguity handling so explicit coverage claims require exactly one target label; 32 unit tests pass.
- 2026-07-01: Added orphan acceptance-test coverage obligations/questions and `OrphanAcceptanceTest` profile export; 33 unit tests pass.
- 2026-07-01: Added object-scoped fact subject validation plus PeTTa subject-mismatch refusals; 33 unit tests pass.
- 2026-07-02: Made explicit requirement coverage labels document-scoped so `[covers:...]` can resolve forward to later requirement sections; 34 unit tests pass.
- 2026-07-02: Added validation-layer status self-checks (`check-status-is-known`) so malformed check records with non-declared statuses fail crisply before backend export; PeTTa check export now preserves malformed status text without crashing; 34 unit tests pass.
- 2026-07-02: Added validation-layer evidence self-checks (`check-has-evidence`) so empty diagnostic evidence fails crisply before backend export; 34 unit tests pass.
- 2026-07-02: Added source-span byte/line self-validation (`source-span-within-file-bounds`, `source-span-lines-match-byte-offsets`) so malformed indexed spans fail crisply before backend export; 35 unit tests pass.
- 2026-07-02: Added Plain file digest self-validation (`plain-file-digest-matches-content`) so corrupted source manifests fail crisply before source-span/backend export review; 36 unit tests pass.
- 2026-07-02: Added section/item PlainFile link validation (`section-file-is-indexed`, `section-has-source-span`, `item-file-is-indexed`) so malformed source-index records fail before backend provenance export; 37 unit tests pass.
- 2026-07-02: Tightened source-index provenance consistency with section/item/span file-ID cross-checks (`section-span-file-matches-section-file`, `item-file-matches-section-file`, `item-span-file-matches-item-file`); 37 unit tests pass.
- 2026-07-02: Added CLI/demo tooling for SpecAtom-HS JSON, grouped PeTTa `.metta`, and Markdown diagnostics reports; added an `auth_service.plain` fixture that surfaces duplicate coverage labels, unresolved coverage targets, unresolved concepts, and backend refusals as reviewable questions; optimized validation record de-duplication by stable IDs; 46 unit tests pass.
- 2026-07-02: Added question-object blocker validation: unresolved concept questions now carry `Blocks` links to their exact Unknown obligations, and `QuestionObject` records self-check for non-empty review text plus known blocked obligations; 47 unit tests pass.
- 2026-07-02: Added first v0.2 ML/time-series methodology validator slice (`ml-evaluation-metric-declared`, `ml-horizon-or-frequency-declared`, `ml-reproducibility-evidence-declared`, `ml-preprocessing-fit-scope-declared`) with `MLTimeSeriesExperiment`/`MissingMethodologyEvidence` atoms and blocking questions; 49 unit tests pass.
- 2026-07-02: Extended the ML/time-series methodology slice with `ml-baseline-comparison-declared` and `ml-uncertainty-reporting-declared` obligations, MissingMethodologyEvidence questions, and regression coverage in the existing methodology tests; 49 unit tests pass.
- 2026-07-02: Added explicit preprocess-then-split leakage review via `ml-preprocessing-order-reviewed` obligations/questions; 50 unit tests pass.
- 2026-07-03: Added explicit future/label-as-feature leakage review via `ml-future-label-leakage-reviewed` obligations/questions; 51 unit tests pass.
- 2026-07-03: Added conservative ML metric/task appropriateness review via `ml-metric-task-appropriateness-reviewed`; forecast/regression-like specs with classification-style metrics now produce Unknown blocking questions unless classification-task wording is present; 52 unit tests pass.
- 2026-07-03: Added conservative ML temporal split-order review via `ml-temporal-split-order-reviewed`; random/shuffled time-series split wording without chronological/walk-forward/out-of-time evidence now produces Unknown blocking questions; 54 unit tests pass.
- 2026-07-03: Added conservative named baseline/uncertainty review via `ml-baseline-comparator-named` and `ml-uncertainty-method-named`; generic `baseline`/`uncertainty` mentions now pass declaration checks but produce Unknown blocking questions until a concrete comparator/method is named; 55 unit tests pass.
- 2026-07-03: Added conservative prediction-time feature availability review via `ml-feature-availability-reviewed`; ML/time-series specs with declared features/inputs/predictors/covariates now produce Unknown blocking questions unless availability is described as prediction-time, point-in-time/as-of, lagged, historical, or equivalent; 57 unit tests pass.
- 2026-07-03: Added first conservative security/privacy obligation scaffolding (`security-secrets-handling-reviewed`, `privacy-pii-handling-reviewed`, `security-access-boundary-declared`, `security-destructive-action-safety-reviewed`) with `SecurityPrivacyReview`/`MissingSecurityPrivacyEvidence` export and blocking questions for missing evidence; 59 unit tests pass.
- 2026-07-03: Deepened the security/privacy slice with `security-secret-log-exposure-reviewed`, requiring secret/token/password specs to state redaction/masking/no-logging evidence or produce Unknown blocking questions; 59 unit tests pass.
- 2026-07-03: Added `privacy-data-classification-declared` to require explicit data/sensitivity classification evidence for PII/personal-data specs, with Unknown blocking questions when absent; 59 unit tests pass.
- 2026-07-03: Added `security-privilege-escalation-reviewed` to require access/auth/admin/role specs to state least-privilege, approval, audit, admin-only, or self-grant-prevention evidence; 59 unit tests pass.
- 2026-07-03: Added `privacy-retention-deletion-reviewed` to require PII/personal-data specs to state retention, deletion/erasure, expiry, or minimization evidence; 60 unit tests pass.
- 2026-07-03: Added `privacy-data-residency-reviewed` to require data-residency/cross-border transfer policy evidence when PII/personal-data specs mention regions, countries, jurisdictions, residency, or cross-border context; 61 unit tests pass.
- 2026-07-03: Added `privacy-third-party-sharing-reviewed` to require DPA/vendor-review/data-sharing policy evidence when PII/personal-data specs mention vendors, processors, partners, external services, exports, uploads, or sharing; 62 unit tests pass.
- 2026-07-04: Added `privacy-lawful-basis-reviewed` to require consent, lawful/legal basis, contract, legal-obligation, legitimate-interest, or similar evidence for PII/personal-data specs; 63 unit tests pass.
- 2026-07-04: Added `privacy-purpose-limitation-reviewed` to require purpose limitation, use limitation, specific-purpose, or secondary-use-review evidence for PII/personal-data specs; 64 unit tests pass.
- 2026-07-04: Added `privacy-pii-access-audit-reviewed` to require access audit/logging/monitoring evidence when PII/personal-data specs also mention access/admin/role wording; 67 unit tests pass.
- 2026-07-04: Added `privacy-incident-response-reviewed` to require incident-response, breach-notification, or escalation evidence for PII/personal-data specs; 68 unit tests pass.
- 2026-07-04: Added `privacy-encryption-scope-reviewed` to require encryption-at-rest, transport-encryption, field/database encryption, key-management, KMS, key-rotation, or equivalent scope evidence for PII/personal-data specs; 69 unit tests pass.
- 2026-07-04: Added `security-session-management-reviewed` to require MFA, session timeout/expiry, revocation/logout, refresh-token rotation, or reauthentication evidence when auth/login/session wording appears; 70 unit tests pass.
- 2026-07-04: Added `ml-feature-freshness-reviewed` to require freshness, staleness, latency, update-cadence, data-age, or as-of timestamp evidence when ML/time-series specs mention real-time/live/current/latest/recent/fresh features or inputs; 72 unit tests pass.
- 2026-07-04: Added `security-auth-abuse-protection-reviewed` to require rate limiting, throttling, brute-force protection, lockouts, abuse detection, bot detection, or CAPTCHA evidence when auth/login/API/password/token wording appears; 73 unit tests pass.
- 2026-07-04: Added `security-credential-rotation-reviewed` to require rotation, expiry, or revocation evidence when secrets/tokens/passwords/credentials appear; 74 unit tests pass.
- 2026-07-04: Added `security-auth-transport-protection-reviewed` to require TLS, HTTPS, mTLS, certificate-pinning, transport-encryption, or secure-channel evidence when auth/login/API/password/token wording appears; 75 unit tests pass.
- 2026-07-05: Added `security-api-authorization-reviewed` to require authorization, permission/scope, RBAC/access-control, deny-by-default, or policy-enforcement evidence when API/endpoint/request wording appears with auth/access context; 76 unit tests pass.
- 2026-07-05: Added `security-webhook-request-authenticity-reviewed` to require HMAC/signature verification, webhook secrets, timestamp windows, nonces, idempotency keys, or replay-protection evidence when webhook/callback/external-request wording appears; 77 unit tests pass.
- 2026-07-05: Added `security-api-input-validation-reviewed` to require schema/input/payload/parameter validation, sanitization, allow-listing, type checks, or bounds checks when API/webhook request input wording appears; 78 unit tests pass.
- 2026-07-05: Added `security-api-error-disclosure-reviewed` to require generic/redacted/sanitized/opaque/correlation-ID-style error-response evidence when API/webhook error, exception, stack-trace, traceback, debug, or diagnostic response wording appears; 79 unit tests pass.
- 2026-07-05: Added first v0.2 information-flow validation slice (`information-flow-inputs-declared`, `information-flow-outputs-declared`, `information-flow-dependency-direction-declared`, `information-flow-temporal-availability-reviewed`, `information-flow-circular-dependency-reviewed`) with `InformationFlowReview`/`MissingInformationFlowEvidence` atoms and blocking questions; 88 unit tests pass.
- 2026-07-05: Added component-level data-path edge extraction: `DataFlowEdge` atoms for explicit "X reads from Y" / "X writes to Y" / "X consumes from Y" / "X depends on Y" patterns, `information-flow-data-path-declared` obligation (Pass with edges, Unknown with only vague wording), `DataFlowEdge` fact schema for PeTTa export, and regression tests comparing extracted edges to ground truth; 93 unit tests pass.
- 2026-07-05: Added graph-based cycle detection from extracted DataFlowEdge atoms: builds directed adjacency graph, detects cycles via DFS white/gray/black coloring, emits `information-flow-cycle-detected` obligation (Pass when acyclic, Unknown with blocking question when cycles exist); 100 unit tests pass.
- 2026-07-05: Added fan-out/fan-in concentration detection from extracted DataFlowEdge atoms: computes per-node out-degree and in-degree, triggers review when any component has >=3 edges in one direction, emits `information-flow-fan-out-reviewed` and `information-flow-fan-in-reviewed` obligations (Pass when acknowledged or below threshold, Unknown with blocking question when unacknowledged); 107 unit tests pass.
- 2026-07-05: Added source/sink identification and reachability analysis from extracted DataFlowEdge atoms: identifies source nodes (no incoming edges) and sink nodes (no outgoing edges), emits `information-flow-source-sink-identified` obligation (Pass when both exist, Unknown with blocking question when missing), and BFS-based reachability check emitting `information-flow-reachability-reviewed` obligation (Pass when all nodes reachable from sources, Unknown with blocking question when unreachable nodes exist); 113 unit tests pass.
- 2026-07-05: Added isolated component detection from broader data-flow verbs: components mentioned with non-edge verbs like `receives data from`, `feeds into`, `flows to`, `provides to`, `gets from`, `pulls from`, `pushes to` that don't produce DataFlowEdge atoms trigger `information-flow-isolated-component-reviewed` obligation (Pass when all mentioned components appear in edges, Unknown with blocking question when isolated components are found); 117 unit tests pass.
- 2026-07-06: Added redundant path detection from extracted DataFlowEdge atoms: finds all simple paths between node pairs, detects when multiple distinct paths (direct + indirect) connect the same pair, emits `information-flow-redundant-path-reviewed` obligation (Pass when no redundant paths or spec acknowledges redundancy via 'redundant'/'backup'/'fallback'/'failover'/'fault tolerance'/'high availability'/'duplicate'/'resilient'/'replicated' wording, Unknown with blocking question when unacknowledged); 122 unit tests pass.
- 2026-07-06: Added temporal ordering impossibility detection: extracts explicit "A before/after/then/precedes/follows B" statements from spec text, builds a temporal ordering graph, detects impossible cycles via DFS white/gray/black coloring, emits `TemporalOrderEdge` atoms, `information-flow-temporal-impossibility-reviewed` obligation (Fail on impossible cycles, Pass when consistent or no temporal statements), blocking `QuestionObject`s, and PeTTa reified profile export; 131 unit tests pass.
- 2026-07-06: Added cross-layer DataFlowEdge vs TemporalOrderEdge consistency check: when data flows A→B (reads from / writes to / depends on) but temporal statements say B before A, emits `information-flow-data-temporal-consistency-reviewed` obligation (FAIL on contradictions, PASS when consistent or either edge type absent), blocking questions, and PeTTa reified profile export; 135 unit tests pass.
- 2026-07-06: Added dependency depth / critical path length detection from extracted DataFlowEdge atoms: computes longest path in the acyclic graph via topological sort + DP, emits `information-flow-dependency-depth-reviewed` obligation (Pass when depth < 4 or acknowledged via 'deep'/'multi-layer'/'multi-hop'/'long chain'/'critical path'/'layered'/'pipeline depth' wording, Unknown with blocking question when deep and unacknowledged), 6 regression tests; 141 unit tests pass.
- 2026-07-06: Added bidirectional edge review to information-flow validation: detects A→B and B→A pairs in the DataFlowEdge graph, emits `information-flow-bidirectional-edge-reviewed` obligation (Pass when no bidirectional pairs or acknowledged via request-response/feedback-loop/bidirectional/two-way/mutual/round-trip wording, Unknown with blocking question when unacknowledged); 5 regression tests; 178 tests pass.
- 2026-07-07: Added duplicate/parallel edge review to information-flow validation: repeated declarations of the same normalized DataFlowEdge emit `information-flow-duplicate-edge-reviewed` (Pass when absent or acknowledged, Unknown with blocking question when unacknowledged) and export through PeTTa reified validation atoms; 3 regression tests; 186 tests pass.
- 2026-07-07: Tightened Phase 2 semantic-object source-span alignment for repeated same-item markers and continuation-line markers, with regression tests comparing generated `Evidence:` spans to ground truth; 191 tests pass; local commit `c018b74`.
- 2026-07-07: Broadened Phase 2 `Bridge:` parsing so arbitrary unsupported ontology labels (for example `OpenCog.AtomSpace`) still produce reviewable `BridgeObject`s, Unknown checks, and `UnsupportedBridgeOntology` blocking questions instead of being silently ignored; 192 tests pass; local commit `b23cc36`.
- 2026-07-07: Added explicit Phase 2 `Confidence:` marker support: percent/decimal confidence annotations normalize to `ConfidenceValue` atoms and pass only when in `[0,1]`; out-of-range values become Unknown `confidence-value-in-unit-interval` checks with `UnsupportedConfidenceValue` blocking questions; 194 tests pass; local commit `7b7aedb`.
- 2026-07-08: Added explicit Phase 3 `Witness:` / `Artifact:` / `Backend artifact:` marker support with source-spanned `BackendArtifact` witness atoms, concrete-artifact validation, TODO/raw-text-only Unknown blocking questions, PeTTa export coverage, and 199 passing tests; local commit `a838ba7`.
- 2026-07-08: Added explicit `Question:` marker support with source-spanned `QuestionObject` atoms, `explicit-question-needs-answer` Unknown checks, PeTTa export coverage, and 202 passing tests.
- 2026-07-08: Added explicit Phase 3 `Process:` and `Resource:` marker support with source-spanned `ProcessObject`/`ResourceObject` atoms, concrete process/resource validation, TODO/vague placeholder Unknown blocking questions, PeTTa export coverage, and 201 passing tests; local commit `09a5134`.
- 2026-07-09: Tightened `Evidence:` marker boundary parsing so file-path/test evidence with periods stops before following same-item semantic markers while preserving exact evidence/outcome spans and PeTTa export; 217 tests pass.
- 2026-07-09: Tightened `Rationale:` marker boundary parsing so file-path/artifact rationale text with periods stops before following same-item semantic markers while preserving exact rationale/evidence spans and PeTTa export; 218 tests pass.
- 2026-07-09: Tightened `Interpretation:` marker boundary parsing so file-path/artifact interpretation text with periods stops before following same-item semantic markers while preserving exact interpretation/bridge spans and PeTTa export; 219 tests pass.
- 2026-07-09: Tightened `Process:` and `Resource:` marker boundary parsing so period-bearing operational/artifact references stop before following same-item markers without truncating file paths; 222 tests pass.
- 2026-07-09: Broadened `Resource:` concrete artifact recognition so direct artifact-path-only declarations such as `docs/capacity.v1.yaml` and `infra/limits.toml` satisfy `resource-requirement-reviewable` with exact source spans and PeTTa export while placeholders remain Unknown; 228 tests pass.
- 2026-07-10: Added explicit `NonGoal:` / `Non-goal:` marker support: source-spanned exclusion objects with `NonGoal`/`NonGoalText`/`NonGoalFor`/`SourceItem` facts, Pass `non-goal-has-source-provenance` checks, marker-boundary handling before following `Evidence:` clauses, PeTTa reified export coverage, and 231 passing tests.
- 2026-07-07: Added conservative Phase 2 bridge relation validation: `bridge-relation-conservative` passes only for graded correspondence labels and turns identity/equivalence-style labels such as `identical` into Unknown checks plus `UnsupportedBridgeRelation` blocking questions; 195 tests pass; local commit `6c5e2df`.
- 2026-07-07: Tightened `Confidence:` markers so non-numeric scales such as `Confidence: high` become source-spanned confidence objects with `confidence-value-in-unit-interval` Unknown checks and `UnsupportedConfidenceValue` blocking questions instead of being silently ignored; 196 tests pass; local commit `565a348`.
- 2026-07-07: Extended component-level DataFlowEdge extraction to explicit `receives ... from` wording with `receives-from` normalization and exact source-span ground-truth regression coverage; 186 tests pass.
- 2026-07-07: Extended component-level DataFlowEdge extraction to explicit `pulls ... from` / `pushes ... to` wording with `pulls-from` / `pushes-to` normalization, information-flow signal coverage, and exact source-span ground-truth regression coverage; 186 tests pass.
- 2026-07-07: Extended component-level DataFlowEdge extraction to explicit `ingests ... from` / `emits ... to` wording with `ingests-from` / `emits-to` normalization, information-flow signal/declaration coverage, and exact source-span ground-truth regression coverage; 186 tests pass.
- 2026-07-07: Tightened TemporalOrderEdge provenance from whole-item spans to exact matched ordering phrase spans while preserving `edge-has-item-level-source-provenance` validation; source-slice ground-truth regression added; 186 tests pass.
- 2026-07-06: Added sink-reachability review to information-flow validation: reverse BFS from sink nodes detects components/cycles that are source-reachable but cannot reach any output sink, emits `information-flow-sink-reachability-reviewed` obligations with Unknown blocking questions for trapped cycles/dead ends/missing outputs; 2 direct regression tests plus export/no-edge coverage; 180 tests pass.
- 2026-07-06: Added `information-flow-graph-summary` atom to PeTTa reified export with node/edge/temporal-edge/source/sink/cycle/component/max-depth/bottleneck counts computed from DataFlowEdge/TemporalOrderEdge facts; 4 ground-truth tests; 174 tests pass.
- 2026-07-06: Added connected-components detection to the information-flow validation slice: undirected BFS finds disconnected subgraphs, emits `information-flow-connected-components-reviewed` obligation (Pass when acknowledged as independent/separate/standalone, Unknown with blocking question otherwise); 3 regression tests; 170 tests pass.
- 2026-07-06: Fixed O(n^2) validator deduplication bottleneck: replaced linear-scan with O(1) set-based lookups in `add_validation_obligation` and `add_check`; auth_service compile time dropped from >17s to 0.14s.
- 2026-07-06: Added `document-validation-summary` atom to PeTTa reified export with Pass/Fail/Unknown check counts and QuestionObject count; added 18-test end-to-end ground-truth test suite for `auth_service.plain` fixture; 159 tests pass.
- 2026-07-06: Added bottleneck node detection (high fan-in AND high fan-out cross-dimension check): emits `information-flow-bottleneck-node-reviewed` obligation; 5 regression tests; 67 information-flow tests pass.
- 2026-07-06: Added temporal ordering impossibility detection: extracts explicit "A before/after/then/precedes/follows B" statements, builds temporal ordering graph, detects impossible cycles via DFS, emits TemporalOrderEdge atoms, `information-flow-temporal-impossibility-reviewed` obligation (Fail on impossible cycles, Pass when consistent or no temporal statements); 131 tests pass.
- 2026-07-06: Added cross-layer DataFlowEdge vs TemporalOrderEdge consistency check: when data flows A→B but temporal statements say B before A, emits `information-flow-data-temporal-consistency-reviewed` obligation (FAIL on contradictions, PASS when consistent or either edge type absent); 4 regression tests; 135 tests pass.
- 2026-07-06: Added dependency depth / critical path length detection from extracted DataFlowEdge atoms: computes longest path via topological sort + DP, emits `information-flow-dependency-depth-reviewed` obligation (Pass when depth < 4 or acknowledged, Unknown with blocking question when deep and unacknowledged); 6 regression tests; 141 tests pass.
- 2026-07-06: Added per-edge source provenance for DataFlowEdge and TemporalOrderEdge: edges now carry the source span of the specific indexed item where the edge was found; `edge-has-item-level-source-provenance` validation; 167 tests pass.
- 2026-07-06: Added redundant path detection from extracted DataFlowEdge atoms: detects when multiple distinct paths connect the same pair, emits `information-flow-redundant-path-reviewed` obligation (Pass when no redundant paths or spec acknowledges redundancy, Unknown with blocking question when unacknowledged); 122 tests pass.
- 2026-07-06: Added `document-validation-summary` atom to PeTTa reified export: emits Pass/Fail/Unknown check counts and QuestionObject count for quick downstream triage; added comprehensive end-to-end ground-truth test suite for `auth_service.plain` fixture (18 tests) covering source provenance, concepts, requirements/coverage labels, duplicate label detection, orphan acceptance tests, unresolved concepts, validation summary counts, reified export structure, backend refusals, and grouped `.metta` section separators; 159 unit tests pass.

## Open questions

- Which Plain grammar source should be treated as authoritative for the MVP parser?
- Should the first target emit pure PeTTa-readable `.metta`, JSON plus `.metta`, or both from the start?
- How much of SUMO/EXPO should be hand-seeded as bridge tables versus linked as external ontology references?
- Which validation domain should be implemented first after generic structural checks: time-series ML methodology, process/resource discipline, or security/privacy obligations?

## Related projects and concepts

- `hyperseed-formalizations`: design notes 0005 and 0006, plus broader Hyperseed formalization work.
- `petta-memory`: p-bit/PLN-ready atom storage patterns may be reusable for SpecAtom-HS journals or memory views.
- `petta-chem`: computational-experiment records can later be represented through the EXPO/Hyperseed validation facet.
- SUMO typed MeTTa bridge and EXPO experiment ontology PDFs uploaded by Benjamin on 2026-06-29.
- OSLF, TyLA, Curry-Howard, MeTTa-IL, Rholang, PeTTa.

- 2026-07-11: Executable-skeleton gating now requires nonblank source provenance in addition to a safe semantic level and fact profile; 270 tests pass.
- 2026-07-13: Executable-reference refusal diagnostics now select unsafe profile facts and immediate transitive targets canonically rather than depending on fact insertion order; reversed-fact-order ground truth added; 287 tests pass.

## Risks

Current v2 state (2026-08-14): local branch
`agent/plain2metta-v2-logical-ir` now includes immutable project storage,
artifact-bound approval/review, and the strict non-executable logical-IR plus
critical-finding report gate through the run
`experiments/20260814T082317Z-plain2metta-v2-logical-ir-schema/RUN.md`.
Persisted finding dispositions and exact compile admission are now implemented,
along with a strict inert compiler-output bundle bound to the exact admitted
logical IR. Generated files require safe relative paths and spec traceability;
publication and execution remain absent. Exact compiler-output approval now
admits an inert, digest-pinned sandbox handoff with mandatory opt-in, bounded
resources, denied host filesystem/network/secrets, and an exact generated-file
set. No execution adapter exists yet. Evidence:
`experiments/20260814T091103Z-plain2metta-v2-output-handoff/RUN.md`.

Phase 4 now also has a provider-neutral canonical prompt envelope bound to the
exact reviewed specification and test snapshot bytes. Provider completions are
parsed into the existing non-executable logical IR with strict fail-closed
schema enforcement. Evidence:
`experiments/20260814T132457Z-plain2metta-v2-logical-ir-envelope/RUN.md`.
The explicit vendor-neutral Phase 4 coordinator now makes exactly one call,
validates configured backend/model provenance, rechecks the reviewed snapshot
versions after the call, and atomically persists a strict provenance log,
logical IR, and its deterministic review. Reload validates all bindings.
Evidence:
`experiments/20260814T133600Z-plain2metta-v2-logical-ir-adapter/RUN.md`.
All eight §3.5 finding categories now have deterministic regeneration and
fail-closed attributed decision replay: unchanged reviews preserve exact
decisions, while changed or reordered finding sets require fresh review.
Evidence:
`experiments/20260814T145802Z-plain2metta-v2-logical-review-replay/RUN.md`.

- **False semantic precision:** shallow English extraction may look more formal than it is. Mitigation: semantic levels, interpretation evidence, questions, and TODO witnesses.
- **Ontology overbuild:** importing too much SUMO/EXPO/Hyperseed can stall the MVP. Mitigation: bridge tables with graded correspondences and small curated slices.
- **Backend capture:** PeTTa details could distort the IR. Mitigation: target profiles and reified facts before executable skeletons.
- **Validation theater:** checks might produce superficial pass/fail labels. Mitigation: every check needs provenance, status, evidence, and counterexample/question when relevant.
- **Security/codegen risk:** never generate positive operational code from negative/security obligations or raw text alone.

## 2026-06-29 implementation update

Created local-only prototype repo `projects/specatom-hs/repos/specatom-hs` (no remote). Implemented a Python stdlib MVP for Appendix H / recommended early phases:

- source indexer with SHA-256 file digests, deterministic IDs, and byte/line `SourceSpan` atoms;
- Plain-like parser for `***section***` headings and nested bullet items;
- SpecAtom-HS subset emitter for source atoms, concepts, requirements, propositions/claims, obligations, shallow action templates, acceptance tests, undefined predicate questions, context/TV assertions, and validation checks;
- JSON and MeTTa-ish S-expression output;
- Appendix G compact task-manager fixture and Appendix O compact ML time-series fixture;
- crisp validator checks for exactly-one primary role, source/generated provenance, obligation propositions, and assertion context/TV.

Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 5 tests. Example generation commands for `examples/task_manager.plain` and `examples/ml_timeseries.plain` succeeded.

## 2026-08-17 Stage 4 semantic validation

The public evaluation branch now contains the approved-plan-bound Hypothesis
backend. It generates canonical closed-world modules, runs them under the
bounded Python sandbox, and records pinned settings, seed, normalized
observations, shrinking data, runtime evidence, and minimal counterexamples.
The full suite passes 690/690. Stage 5 TLA+/TLC is the sole next objective.

## 2026-08-17 Stage 5 semantic validation

The public evaluation branch now contains the exact-approved-plan-bound TLA+/
TLC backend. It deterministically renders finite modules/configs/source maps,
runs pinned project-local TLC under explicit bounds, and admits immutable
state-space evidence and source-linked counterexamples only after strict hash
and ancestry validation. Stage 6 now adds canonical QF_LIA SMT-LIB bundles,
exact declaration/source maps, bounded pinned Z3 4.15.3 execution, and strict
model/unsat-core/optional-proof admission. The full suite passes 703/703 and
the three-example live dual-runtime baseline remains green. Stage 7 is the
sole next objective.

Stage 7 adds an isolated Lean 4 semantic kernel with pinned Lean 4.33.0 and
Mathlib. It kernel-checks the supported type/value, predicate, contract, trace,
lowering-preservation, pure-example, and finite state-invariant theorems with
no additional trust declarations. The full suite passes 709/709 and the live
three-example dual-runtime baseline remains green. Stage 8 passed at 740/740 tests with approved-plan dual-runtime execution and conservative cross-tool verdict composition. Stage 9 passed at 746/746 tests with bounded authorized semantic APIs and an exact-identity evidence workbench. Stage 10 is the sole next
objective.

## 2026-06-29 scaffold update

Added the PDF-recommended minimal `specatom_hs` package alongside the earlier `plain_to_metta` MVP. It includes source indexing with file/section/item/source spans, first-class validation obligations/check records, a conservative pass registry, and PeTTa backend gates that refuse RawTextOnly/unsupported executable skeleton generation while allowing only safe reified atom stubs. Verification: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 12 tests.
# 2026-08-14 Phase 4 logical-review gate

Validated current logical-review retrieval and exact-version finding decisions
are implemented on `agent/plain2metta-v2-logical-ir` at local commit `c77da79`.
The GET boundary omits logical-IR bodies; the POST boundary requires exact IR and
review hashes plus an attributed rationale. Provider-free tests pass 612/612.
Evidence: `experiments/20260814T135749Z-plain2metta-v2-logical-review-decisions/RUN.md`.
Next: gold auth and ML/time-series logical-IR fixtures and validator replay.

# 2026-08-16 Public evaluation UI status

The Tailnet-only v2 workbench is live at `http://100.72.218.34:8081/` from
public task branch `agent/plain2metta-public-evaluation-ui`, head `c6d5d9a`, in
draft PR #3. It exposes the immutable artifact/review/logical-IR/generation/
sandbox/trace chain with precise generated/executed/tested/validated labels.
Its three graduated examples now require unique explicit requirement IDs;
missing or duplicate IDs fail closed. Focused 6/6, full provider-free 657/657,
and live example/sandbox smoke pass. MeTTa remains syntax-checked only and is
not runtime-validated. PDF work is deferred until Ben has used the UI.
Evidence:
`experiments/20260816T195813Z-plain2metta-evaluation-example-validation/RUN.md`.

# 2026-08-14 Phase 5 compilation-envelope gate

The provider-independent Phase 5 request/prompt/response boundary is
implemented on `agent/plain2metta-v2-logical-ir`. It enforces the exact Phase 4
compile admission before exposing hash-bound reviewed spec, reviewed tests, and
logical IR inputs; strict returned compiler bundles remain inert and must match
the provider/model and guidance attribution. Provider-free tests pass 630/630.
Evidence: `experiments/20260814T151308Z-plain2metta-v2-compilation-envelope/RUN.md`.
Next: one-call Phase 5 coordination and atomic persistence with interaction
provenance.

# 2026-08-14 Phase 5 compile-transport gate

Exact `POST /api/compile/<project-id>` now invokes only an explicitly configured
single-call coordinator and returns the atomically admitted compilation-log and
compiler-output identities/hashes. Provider-free tests pass 638/638. Evidence:
`experiments/20260814T153854Z-plain2metta-v2-compile-post-transport/RUN.md`.
Next: read-only compiler-output metadata retrieval without bodies or authority.

# 2026-08-14 Phase 6 test-result query gate

Validated `GET /api/test-result/<project-id>` now returns only exact-chain test
metadata, including stream digests and sizes instead of captured bodies. It
cannot invoke the sandbox or mutate state. Provider-free tests pass 649/649.
Evidence:
`experiments/20260814T163755Z-plain2metta-v2-test-result-query-verification/RUN.md`.
Next: Phase 7 exact-chain traceability/report retrieval across reviewed inputs,
logical IR, compiler output, and sandbox result.
## Stage 10 vertical acceptance (2026-08-17)

Complete at 749/749 tests. Five strict Section 9 data artifacts cover pure,
stateful, temporal, distributed, and unresolved-policy shapes; 8/8 relevant
seeded mutants were killed and the sole cosmetic survivor was reviewed. Stage
11 final hardening is the sole next objective.

## Stage 11 final acceptance (2026-08-17)

Revision 0.2 implementation is complete on the public task branch. The final
matrix passed 72/72 focused and 749/749 full tests, pinned backend and clean
checkout replay, three live dual-runtime examples, browser/API smoke, and all
repository audits. Claims remain bounded by exact ancestry and G0--G6; this is
not a merge or release. Evidence:
`experiments/20260817T104940Z-plain2metta-general-semantic-validation-stage11/`.

## 2026-08-17 evaluation UI vertical Gate 4 increment 13

A real-route regression now creates a new current validation-plan version
after independent approval without creating a matching immutable review. The
request fails atomically with HTTP 422 before Hypothesis, TLC, Z3, Lean, or
legacy evaluation. Focused 1/1 and proportional 93/93 checks passed with
compilation and diff hygiene. Evidence:
`experiments/20260818T045459Z-plain2metta-evaluation-plan-byte-invalidation/`
and
`experiments/20260818T045510Z-plain2metta-evaluation-plan-byte-invalidation-proportional/`.
Task-branch-only commit `ced782f` is pushed.

Next: one contract or immutable-review invalidation case; Stage 11 remains
unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 14

A current semantic-contract byte change after plan approval now has a
real-route regression proving error-only HTTP 422 before Hypothesis, TLC, Z3,
Lean, or legacy evaluation. Focused 1/1 and proportional 94/94 checks passed
with compilation and diff hygiene. Evidence:
`experiments/20260818T052300Z-plain2metta-evaluation-contract-invalidation/`
and
`experiments/20260818T052500Z-plain2metta-evaluation-contract-invalidation-proportional/`.
Task-branch-only commit `f221825` is pushed.

Next: one immutable-review invalidation case; Stage 11 remains unopened.

## 2026-08-17 evaluation UI vertical Gate 4 increment 15

Replacing the current immutable Stage 3 review record after plan approval now
has a real-route regression proving error-only HTTP 422 before Hypothesis, TLC,
Z3, Lean, or legacy evaluation. Focused 1/1 and proportional 95/95 checks
passed with compilation and diff hygiene. Evidence:
`experiments/20260818T055528Z-plain2metta-evaluation-immutable-review-invalidation/`
and
`experiments/20260818T055546Z-plain2metta-evaluation-immutable-review-invalidation-proportional/`.
Task-branch-only commit `56b53f8` is pushed.

Next: Gate 5 begins with the smallest test-first Stage 11 script change that
instruments the UI request path through Stages 1--9 and Stage 10 metadata; do
not run the consequential clean-checkout acceptance until its ledger exists.

## 2026-08-17 evaluation UI vertical Gate 5 increment 1

The Stage 11 focused phase now runs the complete real-route evaluation-web
module. All 29 tests passed, including fresh `/api/evaluate` coverage of Stage
1--8 exact ancestry, server-derived G0--G6 grades, Stage 9 evidence projection,
and recorded Stage 10 calibration release metadata. Shell syntax, compilation,
and diff hygiene passed. Evidence:
`experiments/20260818T062821Z-plain2metta-evaluation-stage11-ui-instrumentation/`.
Task-branch-only commit `1755ddd` is pushed.

This is script instrumentation only, not the consequential acceptance,
clean-checkout replay, browser/API smoke, or independent audit. Next: create
the acceptance ledger, then execute the updated Stage 11 script.

## 2026-08-17 evaluation UI vertical Gate 5 increment 2

The pre-recorded Stage 11 script passed on the clean task-branch working tree
at exact commit `1755ddd`: 106/106 focused tests and 777/777 complete
provider-free tests, followed by compilation, diff, credential-pattern,
large-file, and untracked-file hygiene. Evidence:
`experiments/20260818T065419Z-plain2metta-evaluation-stage11-vertical-acceptance/`.

This is current-checkout evidence only. Next: replay the same gate from a
fresh temporary clone of the pushed task branch under a new experiment ledger;
the live browser/API and three-example dual-runtime smoke and independent
code-path audit remain required.

## Evaluation UI vertical completion (2026-08-18)

The Stage 1--11 evaluation-UI integration acceptance is complete on pushed
task-branch commit `1755dddcb31dc02c04d7db35dec01ba1fb6b9215`. A fresh
single-branch clone passed 106/106 focused and 777/777 provider-free tests plus
repository hygiene, and an independent read-only audit confirmed the browser
request traverses the server-side Stage 1--8 orchestrator, consumes the Stage 9
projection and recorded Stage 10 metadata, and renders only the server-derived
G0--G6 vector. Evidence:
`experiments/20260818T072517Z-plain2metta-evaluation-stage11-clean-checkout/`
and
`experiments/20260818T075514Z-plain2metta-evaluation-stage11-independent-audit/`.
No merge, release, deployment, or service exposure was performed.
