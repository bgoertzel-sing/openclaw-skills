
- Current progress slice hardens the read-only `live-goal-bridge` GoalChainer decision-status boundary. After validating object-shaped decision entries, the bridge now requires every decision `status` to be a non-empty string from the known GoalChainer review vocabulary (`recommended`, `candidate`, `held`, `weak`, `blocked`) before selecting/emitting the recommended action, preventing malformed or newly invented statuses from crossing into the OmegaClaw-facing bridge artifact. Verification: focused `PYTHONPATH=src python3 -m unittest tests.test_live_bridge -v` passed 20 tests; local implementation commit `0d376e9`; full `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 433 tests; `git diff --check` passed. Boundaries preserved: no PeTTaChainer `compileadd`, no memory write, no inferred-belief promotion, no patham9/PLN source change, no OmegaClaw skill/task claim.

# Decisions

## 2026-07-10: Require GoalChainer heuristic-memory check assertion in live bridge

**Decision:** When `live-goal-bridge` requests `include_heuristic_memory_probe=True`, downstream GoalChainer output must now both include a validated `heuristic_memory_probe` sidecar and assert `checks.heuristic_with_memory_path_checked is True`; otherwise the bridge raises `ValidationError` before emitting output.

**Rationale:** The probe sidecar is the evidence detail, while the `checks` object is the downstream gate's summary contract. Requiring both prevents an adapter from copying probe-looking metadata while omitting the audited check that the heuristic-with-memory path actually ran.

**Consequences:** GoalChainer runners/adapters used with requested probes must preserve `heuristic_with_memory_path_checked: true` in their checks block. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-10: Require requested heuristic-memory probe in live bridge

**Decision:** `live-goal-bridge` now treats `include_heuristic_memory_probe=True` as a contract: downstream GoalChainer output must include a validated `heuristic_memory_probe` sidecar, or the bridge raises `ValidationError` before emitting output.

**Rationale:** The heuristic-with-memory probe is the audit sidecar showing that GoalChainer appraisal was grounded through the reviewed memory path and that the leak check remained safe. If the bridge requests that proof and the adapter omits it, emitting a bridge artifact would make the memory-proof boundary ambiguous.

**Consequences:** GoalChainer runners/adapters used with the default requested probe must return the probe sidecar with valid schema/mode/boundary metadata plus `memory_proof_present is True` and `leak_check_safe is True`. Callers can still explicitly set `include_heuristic_memory_probe=False` for tests or reviewed paths that do not require the sidecar. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-10: Reject non-finite GoalChainer contextual EvidencePacket numbers in live bridge

**Decision:** `live-goal-bridge` now accepts optional decision `evidence.contextual_evidence` numeric fields only when EC `support`/`opposition` counts are finite non-boolean non-negative numbers and optional `derived_strength`/`derived_confidence` values are finite non-boolean numbers in `[0,1]`. NaN and Infinity fail closed before bridge output is emitted.

**Rationale:** Contextual EvidencePacket summaries may feed future operator/OmegaClaw-facing artifacts. Non-finite numeric values are JSON/Python drift hazards and can break ranking, display, or downstream validation while appearing numeric. Failing closed keeps the evidence/provenance boundary auditable.

**Consequences:** GoalChainer runners/adapters that include contextual evidence must normalize or reject non-finite EC/truth values before returning bridge output. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.



## 2026-07-10: Validate GoalChainer contextual EvidencePacket truth/provenance in live bridge

**Decision:** `live-goal-bridge` now accepts optional decision `evidence.contextual_evidence` entries only when optional `derived_strength` and `derived_confidence` fields are non-boolean numeric values in `[0,1]`, and when each entry carries non-empty string `belief_id`, `cluster_id`, and `promotion_event` provenance. Malformed truth/provenance sidecars raise `ValidationError` before bridge output is emitted.

**Rationale:** Contextual EvidencePacket summaries are the audit bridge from promoted PeTTa EC evidence to GoalChainer appraisal. EC counts alone are not sufficient if the derived truth-value sidecar or source provenance can drift; future operator/OmegaClaw-facing artifacts need bounded truth values and traceable source ids. Failing closed preserves a reviewable evidence boundary.

**Consequences:** GoalChainer runners/adapters that include contextual evidence must preserve bounded derived truth values when present and source provenance for every contextual-evidence entry. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-10: Validate GoalChainer contextual EvidencePacket EC counts in live bridge

**Decision:** `live-goal-bridge` now accepts optional decision `evidence.contextual_evidence` entries only when each entry includes numeric, non-boolean, non-negative `support` and `opposition` counts. Malformed EC-count summaries raise `ValidationError` before bridge output is emitted.

**Rationale:** Contextual EvidencePacket sidecars are used to audit how promoted PeTTa EC evidence influenced GoalChainer appraisal. If the sidecar lacks well-formed support/opposition counts, a future operator/OmegaClaw-facing artifact could appear evidence-grounded without reviewable EC provenance. Failing closed preserves a clear evidence boundary.

**Consequences:** GoalChainer runners/adapters that include contextual evidence must preserve numeric non-negative EC counts for each entry. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-10: Validate GoalChainer contextual evidence sidecars in live bridge

**Decision:** `live-goal-bridge` now accepts optional decision `evidence.contextual_evidence` sidecars only when they are list-shaped and every entry is object-shaped. Malformed contextual evidence raises `ValidationError` before bridge output is emitted.

**Rationale:** Contextual EvidencePacket summaries are part of the audit trail connecting promoted PeTTa memory/EC evidence to a GoalChainer recommendation. Copying scalar or mixed-shape contextual evidence into a future operator/OmegaClaw-facing bridge artifact would weaken provenance review. Failing closed preserves a clear evidence boundary.

**Consequences:** GoalChainer runners/adapters that include contextual evidence in decision sidecars must preserve list/object shapes. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-10: Validate GoalChainer decision evidence before action-id handling

**Decision:** `live-goal-bridge` now validates optional decision `evidence` sidecars before action-id-specific handling, so every decision record must provide object-shaped evidence and list-shaped `evidence.proofs` when those fields are present, even if the decision has no `action_id`.

**Rationale:** Candidate/held/weak/blocked decisions may legitimately omit an action id in some adapter outputs, but their proof/provenance sidecars are still audit material. Validation should not depend on action-id presence; otherwise malformed provenance could cross the future operator/OmegaClaw-facing boundary.

**Consequences:** GoalChainer runners/adapters that include decision evidence on any decision must preserve object/list shapes. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-10: Validate GoalChainer decision evidence sidecars in live bridge

**Decision:** `live-goal-bridge` now accepts optional GoalChainer decision `evidence` sidecars only when they are object-shaped, and accepts nested `evidence.proofs` only when list-shaped. Malformed decision evidence raises `ValidationError` before bridge output is emitted.

**Rationale:** Decision evidence/proofs are the audit trail connecting promoted PeTTa memory and admitted pi-PLN evidence to a GoalChainer recommendation. Copying malformed proof sidecars into a future operator/OmegaClaw-facing artifact could make unreviewable provenance look legitimate. Failing closed keeps the bridge artifact auditable.

**Consequences:** GoalChainer runners/adapters that include decision evidence must preserve object-shaped evidence and list-shaped proofs. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-10: Validate GoalChainer heuristic-memory-probe sidecar in live bridge

**Decision:** `live-goal-bridge` now accepts an optional GoalChainer `heuristic_memory_probe` sidecar only when it is object-shaped, has non-empty string `schema`, `mode`, and `boundary` fields, and explicitly asserts both `memory_proof_present is True` and `leak_check_safe is True`. Malformed, missing-proof, or unsafe leak-check probe sidecars raise `ValidationError` before bridge output is emitted.

**Rationale:** The heuristic-with-memory probe is an audit sidecar for the read-only bridge. Copying it into a future operator/OmegaClaw-facing artifact without validating the proof/leak-check claims could make malformed downstream runner output look safe or memory-grounded. Failing closed keeps the bridge artifact reviewable.

**Consequences:** GoalChainer runners/adapters that include `heuristic_memory_probe` must preserve its schema/mode/boundary metadata and positive memory-proof/leak-check booleans. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-09: Require unique well-formed GoalChainer decision action IDs in live bridge

**Decision:** `live-goal-bridge` now rejects GoalChainer decision records that include a missing/non-string/empty `action_id`, and rejects duplicate `action_id` values across the decision list before emitting bridge output.

**Rationale:** The bridge artifact is meant to carry auditable GoalChainer appraisal into later operator/OmegaClaw review. If one action appears twice with conflicting statuses, or a decision record carries a malformed action identifier, the recommendation set becomes ambiguous. Failing closed keeps the read-only integration boundary reviewable.

**Consequences:** GoalChainer runners/adapters must produce unique non-empty string action identifiers for any decision record that includes `action_id`; recommended decisions continue to require one. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-09: Reject multiple GoalChainer recommended decisions in live bridge

**Decision:** `live-goal-bridge` now rejects GoalChainer output that contains more than one decision with `status: recommended`. A duplicate recommendation raises `ValidationError` before bridge output is emitted.

**Rationale:** The bridge artifact is intended to carry one auditable recommended action into later operator/OmegaClaw review. Silently choosing the first recommended decision would make malformed or drifted GoalChainer adapters ambiguous and could hide competing recommendations.

**Consequences:** GoalChainer runners/adapters must produce zero or one recommended decision, and any recommended decision must still carry a non-empty string `action_id`. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.

## 2026-07-09: Require GoalChainer no-write/no-directive checks in live bridge

**Decision:** `live-goal-bridge` now accepts GoalChainer output only when the downstream `checks` object explicitly asserts `no_memory_write is True` and `no_live_directive_or_task_claim is True`. Missing, false, or malformed boundary-check assertions raise `ValidationError` before bridge output is emitted.

**Rationale:** The bridge artifact is a safety/audit boundary for future OmegaClaw wrappers. It should not synthesize top-level no-write/no-task claims if the GoalChainer gate failed to provide its own matching assertions. Requiring exact booleans keeps adapter drift fail-closed.

**Consequences:** GoalChainer runners/adapters must preserve these two boundary checks. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-09: Fail closed on malformed GoalChainer notes and recommended action IDs

**Decision:** `live-goal-bridge` now treats GoalChainer `decision_payload.notes` as an audited list-shaped field and requires every selected `status: recommended` decision to include a non-empty string `action_id`. Malformed notes or recommended decisions raise `ValidationError` before bridge output is emitted.

**Rationale:** The live bridge artifact is intended for review and possible future OmegaClaw handoff. A recommended decision without an action identifier, or a non-list notes payload, weakens downstream auditability and could turn malformed GoalChainer output into ambiguous operator-facing state.

**Consequences:** GoalChainer runners/adapters must preserve list-shaped notes and a concrete recommended action ID. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-09: Require top-level patham9 runtime schema and zero returncode before GoalChainer appraisal

**Decision:** In `live-goal-bridge --run-patham9-runtime`, a patham9 runtime result is accepted only if the top-level result includes a non-empty string `schema` and exact integer `returncode: 0`, in addition to the existing `status: passed`, semantic marker, and program-sidecar checks. Boolean, string, missing, or nonzero returncodes raise `ValidationError` before GoalChainer appraisal.

**Rationale:** The patham9 runtime gate is a proof/audit boundary. A result that says `status: passed` but has ambiguous schema or shell-return metadata should not produce downstream GoalChainer recommendations. Exact top-level metadata keeps runtime adapters auditable and prevents JSON/Python type drift such as `true == 1` from weakening the gate.

**Consequences:** Patham9 runner adapters must preserve a non-empty result schema and integer zero return code on success. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-09: Require semantic patham9 audit fields before GoalChainer appraisal

**Decision:** In `live-goal-bridge --run-patham9-runtime`, a patham9 runtime result is accepted only if it has `status: passed`, object-shaped `semantic_markers` with `semantic_passed: true`, an object-shaped `program` artifact, and a non-empty string program schema. Malformed or semantically failing audit fields raise `ValidationError` before GoalChainer appraisal.

**Rationale:** The patham9 runtime gate is an audit/proof boundary over the admitted pi-PLN handoff. A top-level status alone is too weak if the semantic markers or program sidecar are missing or malformed; downstream recommendations should not be produced from ambiguous proof artifacts.

**Consequences:** Patham9 runner adapters must preserve semantic marker and program metadata. The live bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-09: Do not synthesize PR reconciliation in canary-only GoalChainer scenarios

**Decision:** The ThreadKeeper project-control GoalChainer scenario must only include `reconcile_threadkeeper_pr` as a goal/action/obligation when PR-reconciliation evidence is present in the PeTTa/GoalChainer handoff. Canary-only admitted patham9 evidence should recommend the bounded canary directly instead of inventing a prerequisite.

**Rationale:** The bridge should appraise promoted/admitted evidence, not create missing project-control facts. The richer ThreadKeeper feedback fixture still uses PR-reconciliation evidence to rank `reconcile_threadkeeper_pr` first, but a canary-only handoff should not be held behind an absent default action.

**Consequences:** Future GoalChainer scenario adapters should keep conditional project-control obligations tied to explicit evidence. The path remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.

## 2026-07-09: Fail closed on malformed GoalChainer scalar metadata in live bridge

**Decision:** After `live-goal-bridge` validates object-shaped GoalChainer gate output, the nested gate metadata fields `schema`, `mode`, and `boundary` must be present as non-empty strings before the bridge emits a read-only live-bridge artifact. Malformed or missing scalar metadata raises `ValidationError`.

**Rationale:** The bridge artifact is an audit boundary. Missing schema/mode/boundary metadata weakens operator review and previously could surface as incidental dictionary-key errors while assembling output. Explicit scalar checks preserve fail-closed behavior for malformed downstream GoalChainer gate results.

**Consequences:** GoalChainer runners and test adapters must return non-empty string schema, mode, and boundary metadata. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.


## 2026-07-09: Fail closed on malformed GoalChainer decisions in live bridge

**Decision:** After `live-goal-bridge` validates the GoalChainer gate result, the nested `decision_payload.decisions` field must be list-shaped and every decision entry must be object-shaped before the bridge scans for a recommended action. Malformed decision containers or entries raise `ValidationError`.

**Rationale:** The live bridge should not emit read-only integration artifacts from ambiguous or malformed downstream recommendation records, and Python attribute errors are not an auditable boundary failure mode. Explicit schema checks keep the bridge safer for later OmegaClaw wrapper review.

**Consequences:** GoalChainer runners and test adapters must return decision lists containing object records. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.

## 2026-07-08: Fail closed on malformed GoalChainer gate output in live bridge

**Decision:** After `live-goal-bridge` invokes the local/injected GoalChainer runner, the runner result must be an object-shaped artifact containing object-shaped `decision_payload` and `checks` fields before the bridge emits any read-only live-bridge artifact. Malformed GoalChainer output raises `ValidationError`.

**Rationale:** The live bridge is a reviewed boundary from PeTTa memory into GoalChainer appraisal. Malformed downstream-gate output should not become ambiguous bridge records or incidental Python exceptions. Failing closed keeps the read-only bridge auditable and makes future OmegaClaw integration wrappers easier to reason about.

**Consequences:** Test adapters and future GoalChainer runners must return explicit object-shaped result/check payloads. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9/PLN source change, or OmegaClaw skill/task claim.

## 2026-07-08: Fail closed on malformed patham9/PLN runtime results in live bridge

**Decision:** When `live-goal-bridge --run-patham9-runtime` invokes a patham9/PLN runtime runner, the runner result must be an object-shaped artifact before the bridge inspects status/returncode metadata or proceeds to GoalChainer appraisal. Non-object results raise `ValidationError` and abort the bridge.

**Rationale:** The patham9 runtime gate is an auditable proof/runtime artifact. A malformed runner return could otherwise produce incidental Python errors or ambiguous downstream behavior at the boundary immediately before GoalChainer recommendation. Failing closed preserves clear operator semantics and prevents recommendation output from being produced after malformed proof-gate output.

**Consequences:** Injected test runners and future runtime adapters must return dict/object artifacts with explicit status metadata. The bridge remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, patham9 source change, or OmegaClaw skill/task claim.

## 2026-07-08: Fail closed on patham9/PLN runtime failure before GoalChainer appraisal

**Decision:** When the read-only live bridge is invoked with `--run-patham9-runtime`, a patham9/PLN runtime result whose status is not `passed` aborts the bridge with `ValidationError` before any GoalChainer appraisal is run.

**Rationale:** The optional patham9 gate is the proof/runtime check over the ranked/admitted pi-PLN handoff. Allowing GoalChainer to appraise after that gate failed could produce a recommendation that looks downstream-approved even though the proof gate did not pass. Failing closed keeps the live bridge semantics auditable and safer for later OmegaClaw integration.

**Consequences:** Operators get an explicit bridge failure on patham9 runtime failure and must inspect the runtime artifact/logs before rerunning. GoalChainer recommendations are only produced when the optional runtime gate is skipped or passes. The boundary remains read-only: no memory write, inferred-belief promotion, PeTTaChainer `compileadd`, or OmegaClaw skill/task claim.

## 2026-07-08: Use patham9/PLN runtime gate inside the read-only live bridge

**Decision:** Add an optional `--run-patham9-runtime` gate to `live-goal-bridge` that executes a bounded local patham9/PLN multi-sentence derivation smoke over only the ranked/admitted pi-PLN handoff items before GoalChainer appraisal.

**Rationale:** PeTTaChainer `compileadd` remains blocked in `materialize-stmt-lambdas`, but patham9/PLN `PLN.Query`/derivation smokes work over generated Sentence atoms. Running patham9 after the audited admission gate gives a practical PeTTaChainer bypass while keeping branch selection explicit and bounded.

**Consequences:** The bridge can now demonstrate journal -> admitted pi-PLN handoff -> live patham9 derivation -> GoalChainer recommendation without invoking PeTTaChainer `compileadd`. It still does not append memory, promote inferred beliefs, load OmegaClaw skills, or accept tasks/directives. Relative path handling for `pln_repo` is resolved before deriving the project-local environment script.

## 2026-07-08: Reject boolean/non-integer metadata in ranked/admitted pre-derive gates

**Decision:** Treat handoff/plan counts and branch rank/item-index keys as exact integer audit fields, rejecting bools and non-integers before estimator/controller dispatch, branch-plan mirror validation, or admitted premise copying.

**Rationale:** JSON artifact drift can otherwise use values like `true` that compare equal to integer `1` in Python, weakening audit clarity around reviewed branch counts and admission order. These fields control the non-live plan reviewed before any future derive gate, so loose typing should fail explicitly.

**Consequences:** Handoff and ranked-plan producers must emit numeric integer metadata, not booleans or strings. The gate remains wrapper-only and non-live; no runtime derive path, memory append, inferred-belief promotion, or patham9/PLN source change is introduced.

## 2026-07-08: Validate ranked-plan source handoff containers and counts before planning

**Decision:** The ranked inference-control plan gate now treats the source handoff `items` collection and `item_count` as part of the schema-level preflight for branch-plan construction, rejecting non-list `items` and item-count drift before estimator/controller wrappers run.

**Rationale:** The ranked plan is the reviewed artifact that later feeds admitted-handoff selection. If the source handoff container or count has drifted, the plan could present misleading `input_count`/branch metadata before the stricter admission gate catches it. Failing early gives clearer audit errors and keeps branch-plan provenance tied to the exact source handoff.

**Consequences:** Handoff producers must keep `item_count` synchronized with `items` before invoking `pi-pln-ranked-plan` or `ranked_inference_control_plan()`. The gate remains wrapper-only and non-live; no runtime derive path, memory append, or patham9/PLN source change is introduced.

## 2026-07-08: Validate admitted-handoff source item records before mirror checks

**Decision:** The ranked-plan admission gate now treats each referenced source handoff `items` entry as a schema-level object and rejects non-object entries before branch-plan/source mirror checks or admitted premise copying.

**Rationale:** The admitted handoff remains the final non-live artifact before any future separately reviewed derive gate. Malformed source items should produce explicit validation failures rather than incidental Python attribute errors, especially when comparing audited `belief_id`/`term` fields against source handoff items.

**Consequences:** Future handoff producers must preserve object-shaped item records. The gate remains wrapper-only and non-live; no runtime derive path, memory append, or patham9/PLN source change is introduced.

## 2026-07-08: Validate admitted-handoff container types before partition checks

**Decision:** The ranked-plan admission gate now treats the source handoff item collection and reviewed branch partitions as schema-level containers and requires each to be a list before count, status, rank, source, and mirror validation proceeds.

**Rationale:** The admitted handoff is a pre-derive audit artifact. Malformed artifacts should fail with explicit validation errors, not incidental Python iteration or attribute errors, so reviewers and future automation can distinguish schema drift from runtime failures.

**Consequences:** Future plan producers must preserve list-shaped `items`, `recommended_branches`, `held_branches`, and `branch_plan` fields. The gate remains wrapper-only and non-live; no runtime derive path or patham9/PLN source change is introduced.

## 2026-07-08: Require contiguous ranks in admitted-handoff reviewed plans

**Decision:** The ranked-plan admission gate now treats the audited `branch_plan` rank sequence as part of the reviewed artifact and requires contiguous ranks from `1` through `candidate_count` before producing an admitted handoff subset.

**Rationale:** Unique ranks alone are not enough: a malformed or edited plan could preserve uniqueness while introducing gaps or shifted order that weaken auditability. The admitted handoff is the last non-live gate before any future reviewed `PLN.Derive`, so rank semantics should be deterministic and complete.

**Consequences:** Future plan producers must keep dense rank ordering. The gate remains wrapper-only and non-live; no patham9/PLN source changes or runtime derive calls are introduced.

## 2026-07-06: Keep ranked inference-control as an auditable non-live gate before PLN.Derive

**Decision:** Compose the PLN estimator/EDCall ranking and continuation-predicate controller into a `ranked_inference_control_plan()` wrapper that recommends or holds branches before any future live `PLN.Derive` invocation.

**Rationale:** All eight trueagi/chaining-inspired inference-control patterns now exist at the wrapper level. A unified plan gate is the smallest safe next step toward runtime integration: it makes branch admission explicit and testable without invoking SWI/PeTTa/MeTTa, changing patham9/PLN, appending memory, or promoting inferred beliefs.

**Consequences:** Future runtime work should consume this plan artifact first, and only allow recommended branches into a separately reviewed live derive gate. Held branches retain explicit reasons (probability threshold, query irrelevance, controller reject/terminate, or missing controller decision) for debugging and policy review.

## 2026-07-06: Implement PLN estimator as first long-term inference-control pattern

**Decision**: Implement the "PLN-based inference controller" (PLN estimator) pattern from the trueagi-io/chaining inference-control survey as the first long-term inference-control mechanism. The wrapper converts each handoff Sentence into PLN viability prior parameters (alpha/beta) derived from EC support/opposition counts when available, or from STV strength × confidence when EC is absent. It then Thompson-samples from the Beta(alpha, beta) posterior to produce sampled viability scores, and ranks branches by sampled viability into EDCall (Estimated Delayed Call) records for PLN.Derive exploration.

**Rationale**: All four near-term patterns (probabilistic filtering, context selection, chained pipeline, meta-learning benchmark) and both medium-term patterns (continuation predicate, controlled backward chainer) are now implemented. The PLN estimator is the natural next step from the survey: it was categorized as long-term complexity and directly maps to the `pln-inf-ctl.metta` pattern in `trueagi-io/chaining/experimental/pln-inf-ctl/`, where a Control structure holds a PLN knowledge base and an estimator function that converts queries into PLN statements to estimate branch viability before committing to recursive search. The EDCall pattern (pairing a probability estimate with a deferred branch call) is the core mechanism.

**Key design decisions**:
- EC-based priors: when EvidencePacket counts are available, use `alpha = support + 1`, `beta = opposition + 1` (Laplace-smoothed). When EC is absent, derive from STV: `alpha = strength × confidence × 10 + 1`, `beta = (1 - strength) × confidence × 10 + 1`. The confidence factor scales the effective sample size.
- Exploration weight: higher values shrink Beta parameters toward uniform `Beta(1,1)`, increasing variance and thus exploration. This is achieved by dividing the evidence contribution `(alpha - 1, beta - 1)` by the weight. Lower values concentrate the distribution, increasing exploitation.
- Thompson sampling: uses the gamma-ratio method (via Python's `random.gammavariate`) for beta distribution sampling, which is numerically stable and requires no external dependencies.
- Query target relevance: simple text containment matching to flag which branches are relevant to the query target.

**Alternatives considered**: (1) Implement the controller-as-chainer pattern (second long-term) instead. Rejected because the PLN estimator is the more fundamental pattern and the controller-as-chainer would build on it. (2) Use a simpler ranking without Thompson sampling. Rejected because Thompson sampling is the core of the trueagi-io/chaining pattern and provides principled exploration/exploitation balancing. (3) Use numpy/scipy for beta sampling. Rejected to keep the dependency-light stdlib-only constraint.

**Consequences**: The remaining long-term pattern (controller-as-chainer) is still open. The PLN estimator provides a testable foundation for future live integration: a live version would use the estimator to rank branches before actual `PLN.Derive` calls, selecting the top-k EDCall records for exploration. The EDCall pattern naturally maps to the deferred branch concept in the trueagi-io/chaining Control structure.

## 2026-07-06: Implement controlled backward chainer as second medium-term inference-control pattern

**Decision**: Implement the "controlled backward chainer" pattern from the trueagi-io/chaining inference-control survey as the second medium-term inference-control mechanism. The wrapper simulates a bounded backward-chaining loop using the continuation predicate as a per-branch decision function, with context updaters tracking depth and EC accumulation between steps, and max_steps/max_branches safety caps. Three context update modes are supported: `accumulate_depth` (increment derivation depth for continued branches), `accumulate_ec` (also accumulate EC support counts), and `fixed` (no context update, baseline control).

**Rationale**: The continuation predicate was the first medium-term pattern and provides a per-branch decision function. The controlled backward chainer is the natural next step: it wraps the continuation predicate in an iterative loop with context tracking, demonstrating how multiple derivation steps would be controlled. This maps directly to the `bc` (backward chainer) function in `trueagi-io/chaining/experimental/inference-control/inf-ctl-month-bc-cont-xp.metta`, which takes a knowledge base, control structure (context updaters + continuation predicates), context, and query, and recursively applies the continuation predicate at each branch point. The wrapper-level implementation simulates this loop without requiring live PLN runtime, keeping the boundary safe.

**Alternatives considered**: (1) Skip directly to the long-term patterns (PLN estimator, controller-as-chainer). Rejected because the controlled chainer is a prerequisite for understanding how context updaters and continuation predicates compose across multiple steps. (2) Implement the controlled chainer with live runtime. Rejected because the patham9/PLN runtime integration is still at the query/derivation smoke stage; adding multi-step live control would be premature.

**Consequences**: Both medium-term patterns are now implemented. The remaining long-term patterns (PLN estimator, controller-as-chainer) would require running the chainer at multiple abstraction levels or using another chainer as a controller, which is beyond the current wrapper boundary. The controlled backward chainer provides a testable foundation for future live integration: a live version would replace the simulated loop with actual `PLN.Derive` calls while using the same continuation predicate and context update logic.

## 2026-06-27: Local-first standalone prototype before OmegaClaw integration

**Decision:** Start `petta-memory` as a standalone local repository under `projects/petta-memory/repos/petta-memory`, then integrate into OmegaClaw/ProtomegaTron only after append/query/view tests pass.

**Rationale:** The memory store affects prompt context and later PLN inference, so schema mistakes could silently shape agent behavior. A standalone prototype permits deterministic tests and review before live agent integration.

**Alternatives considered:** Patch OmegaClaw directly first; rejected for v0 because live integration would mix schema design, runtime policy, and prompt behavior too early.

## 2026-06-27: Append-only clusters are canonical

**Decision:** The canonical write unit is an append-only `MemoryCluster`; current state is derived from status/truth/salience events and supersession links.

**Rationale:** This preserves auditability and is safer for later PLN belief revision than in-place mutation.

## 2026-06-27: Separate audit, prompt, and PLN views

**Decision:** The implementation will maintain distinct view functions for human audit, LLM prompt context, and PLN-safe atoms.

**Rationale:** Raw observed/quoted material is useful evidence but should not be exported as factual PLN premises without explicit promotion.

## 2026-06-30: PLN promotion requires rule, bounded trust, and domain metadata

**Decision:** A `DerivedBelief` is PLN-eligible only when an explicit `PromotionEvent` supplies `PromotesTo`, `PromotionRule`, bounded numeric `PromotionTrust` in `[0, 1]`, and `PromotionDomain`, and the belief has both `TruthValue` and `EvidenceFor`. Normalized exports use `MM-PLNPremise`, `MM-PLNDomain`, `MM-PLNTrust`, and `MM-PLNPromotionRule` mapping atoms.

**Rationale:** Promotion without trust/domain metadata is too ambiguous for later PLN inference and can make quoted or derived material look more authoritative than intended. Keeping normalized mapping atoms explicit makes the intermediate store safer to inspect before choosing a concrete PLN runtime.

## 2026-07-04: Pivot to patham9/PLN as functional chainer base with pi-PLN extensions

**Decision:** Start a parallel PLN chainer track using `patham9/PLN` (aka `trueagi-io/PLN`) as the functional base, adding pi-PLN evidence/context semantics on top. PeTTaChainer remains a semantic reference and comparison target, not the critical path.

**Rationale:** PeTTaChainer's `compileadd`/`materialize-stmt-lambdas` bottleneck is structural (adjacent arity-two nested sibling payloads in a four-field wrapper time out even for lambda-free statements). It blocks the live inference substrate but not the memory/export layer. `patham9/PLN` already exposes `PLN.Derive` and `PLN.Query` with task/belief queues, max steps, evidential bases, and `(stv S C)` sentences — much closer to a usable chainer API. The missing pi-PLN layer (contextual evidence packets, EC counts, context selection, STV projection from contextual evidence) can be added around/into it.

**Alternatives considered:** (1) Keep forcing progress through PeTTaChainer's `compileadd` bottleneck. (2) Use trueagi-io/chaining pure-MeTTa experiments as the base. Rejected as primary because `patham9/PLN` has a more complete functional chainer already.

**Consequences:** `petta-memory` stays as the structured memory/export layer. The handoff cache/precompiled path remains useful. PeTTaChainer integration stays gated. A new work track begins: clone `patham9/PLN`, reproduce its smoke tests, then add pi-PLN evidence/context extensions.

**Revisit trigger:** If `patham9/PLN` proves harder to extend than expected, or if PeTTaChainer's materialize bottleneck gets fixed upstream.

## 2026-07-01: First PeTTaChainer export uses STV proof statements, not EC packets yet

**Decision:** Export promoted beliefs to PeTTaChainer initially as `(: proof-id statement (STV strength confidence))`. The mapper preserves the `TruthValue` strength and caps confidence by `PromotionTrust` so promotion can reduce but not inflate confidence. `EvidencePacket`/`EC pos neg` export is deferred until the memory schema represents explicit support and opposition counts.

**Rationale:** PeTTaChainer can validate this shape immediately with `check_stmt`, giving a narrow runtime smoke without inventing unsupported evidence-count semantics.

## 2026-07-01: PeTTa runtime parse checks remain explicit and pre-append

**Decision:** Wire PeTTa runtime validation through an opt-in `make_petta_parse_checker(...)` hook rather than making PeTTa/PeTTaChainer a default dependency of `MediumMemoryStore` or enabling any live OmegaClaw write path.

**Rationale:** Runtime syntax compatibility is useful before PLN/OmegaClaw integration, but the core store should remain dependency-light and deterministic. Keeping the checker explicit preserves local-first operation, lets tests use fake runtimes, and ensures a runtime failure happens before append so the journal remains unchanged.

## 2026-07-01: Preserve PeTTaChainer's pi-PLN semantics, then split work into mechanics optimization and inference control

**Decision:** Use PeTTaChainer because its pi-PLN setup is semantically appropriate for experiential learning across multiple contexts, but treat the current implementation as an initial semantic substrate rather than an optimized or inference-controlled engine. After the basic pipeline works, proceed on two threads: (1) profile and optimize rule-application/truth-value mechanics, and (2) collaborate with Ben on richer OmegaClaw-specific inference control.

**Rationale:** Context-indexed evidence is important for OmegaClaw-style experiential learning; flattening evidence prematurely into a single global truth value would lose exactly the structure the memory layer needs. At the same time, semantic adequacy does not imply efficient implementation or good search/control behavior.

**Alternatives considered:** Replace PeTTaChainer immediately with a simpler/faster PLN substrate; rejected for now because it risks losing the pi-PLN/context semantics before we understand the optimization and control bottlenecks.

## 2026-07-02: EvidencePacket export requires explicit support/opposition counts

**Decision:** PeTTaChainer `EvidencePacket` export is enabled only for promoted beliefs with explicit `EvidenceSupportCount` and `EvidenceOppositionCount` atoms. The exporter emits `(EC pos neg)` from those schema values and does not derive counts from `TruthValue`/STV.

**Rationale:** EC packets carry evidence-count semantics that are stronger than a truth-value confidence. Requiring explicit counts avoids silently inventing support/opposition evidence while still giving OmegaClaw-context workloads a principled path into PeTTaChainer's context-indexed evidence machinery.

## 2026-07-02: Instrument `compileadd` subforms before optimizing or bypassing add

**Decision:** Keep the next PeTTaChainer performance work diagnostic-first: profile `compileadd`'s internal subforms in bounded subprocesses before adding a minimal/precompiled add path or changing exported PeTTaChainer atoms.

**Rationale:** Constructor-only profiling showed initialization is fast while add-only stages time out. The new probes give a narrower failure surface without changing PeTTaChainer semantics or petta-memory export contracts.


## 2026-07-02: Direct-vs-eval probe controls before bypassing PeTTaChainer add

**Decision:** Treat the `materialize-stmt-lambdas`/`mm2compile` timeout as not explained by the previous eval-wrapped probe alone. Keep direct subform probes as the default profiling path, retain narrow eval controls for comparison, and do not change petta-memory export semantics until a minimal/precompiled add option is selected and gated.

**Rationale:** Direct probes mirror PeTTaChainer's `compileadd` `let*` path more closely than `!(eval ...)`. The direct-vs-eval artifact shows both materialize and mm2compile still time out under a 5s bound, while index/maybe-process stages are fast, so bypassing or optimizing add should target materialization/compilation rather than query or context projection.

## 2026-07-02: Use a non-live precompiled statement cache gate before full PeTTaChainer add/query

**Decision:** The next minimal PeTTaChainer path is a non-live precompiled-statement cache/handoff gate for checked promoted STV statements and EvidencePackets. Cached atoms are PLN-ready inputs for downstream inspection or future GoalChainer/OmegaClaw mapping, not inferred beliefs. Full PeTTaChainer `compileadd`/query remains behind an explicit gate until `materialize-stmt-lambdas`/`mm2compile` are instrumented upstream or a precompiled add API exists.

**Rationale:** The direct-vs-eval probe artifact shows that both direct and eval-control materialization/compilation paths time out, while `check_stmt`, constructor initialization, `index-source-implication`, and `maybe-process-on-add` succeed quickly. A direct KB fact add risks bypassing PeTTaChainer indexing/proof semantics; deeper upstream instrumentation is still needed, but a cache gate gives petta-memory and OmegaClaw planning a stable, testable handoff artifact now.

**Alternatives considered:** Minimal direct KB fact add; rejected for the immediate path because query semantics likely depend on PeTTaChainer's compiled/internalized proof structures. Upstream-only instrumentation; kept as a follow-up, but it would not advance the petta-memory handoff contract in this slice.

## 2026-07-02: Handoff cache is non-live input evidence, not inferred memory

**Decision:** `pettachainer_handoff_cache` packages promotion-eligible STV proof statements and explicit-EC EvidencePackets as a JSON handoff artifact for review and future OmegaClaw/GoalChainer mapping. Items are labeled `pln-ready-input-not-inferred-belief`; the cache is not appended to the journal, does not invoke PeTTaChainer `compileadd`/query, and does not claim inference results.

**Rationale:** This advances the integration contract despite the current `materialize-stmt-lambdas`/`mm2compile` bottleneck. Optional `statement_checker` support allows runtime validation of STV statement shape via `PeTTaChainer.check_stmt`, while keeping full add/query semantics behind the existing gate.

## 2026-07-02: GoalChainer smoke remains non-live and cannot use current compileadd path as the gate

**Decision:** Keep the GoalChainer gate at a non-live decision-payload contract and do not treat the current external GoalChainer demo as passed until its PeTTaChainer `compileadd` path is bypassed, adapted to precompiled handoff evidence, or instrumented upstream.

**Rationale:** The hand-picked `petta-memory` handoff fixture and wrapper can enforce provenance/no-task/no-write boundaries, but the external GoalChainer demo still reaches PeTTaChainer `compileadd` and fails with SWI `stack_limit=8g` before producing a decision payload. A passing gate must consume promoted evidence without claiming tasks or live skills and without relying on the currently blocked compileadd path.

## 2026-07-02: Precompiled GoalChainer smoke is the first non-live decision gate

**Decision:** Use a precompiled `goalchainer-handoff-cache` bridge as the first passing non-live GoalChainer decision-payload gate. The gate consumes promoted `Acceptable` STV evidence from petta-memory and runs only GoalChainer scenario/scoring/explanation code with a local cache-backed reasoner. It must not invoke GoalChainer CLI, PeTTaChainer `compileadd`/query, directives, execution, OmegaClaw skills, or memory writes. The older external CLI path remains available only as an explicit blocked comparison via `--external-cli`.

**Rationale:** The external GoalChainer demo currently fails before producing a decision payload because its PeTTaChainer `compileadd` path exceeds the SWI stack limit. The precompiled gate preserves provenance and exercises GoalChainer's decision machinery now, while truth-changing PeTTaChainer add/query semantics remain gated pending upstream instrumentation or a proper precompiled-add API.


## 2026-07-03: Keep GoalChainer precompiled and add bounded EC influence before returning to compileadd

**Decision:** The next non-live GoalChainer evidence-depth step is not live integration and not the external CLI path. Keep the precompiled decision gate, but let matching `EvidencePacket` support/opposition counts influence promoted `Acceptable` action appraisal as bounded derived strength/confidence, with explicit proof provenance and `compileadd_not_invoked` checks.

**Rationale:** The external GoalChainer/PeTTaChainer `compileadd` path is still blocked, but ignoring EC packets would discard the context-rich evidence signal Ben wanted preserved for OmegaClaw-style reasoning. A precompiled EC influence path gives a testable bridge from promoted EvidencePackets to GoalChainer decision scoring without claiming inferred beliefs, tasks, skills, or memory writes.

## 2026-07-03: No public PeTTaChainer precompiled-add API in checked-out source

**Decision:** Treat the current PeTTaChainer checkout as not exposing a public precompiled-add/cache API for petta-memory to adopt. Continue using the non-live petta-memory handoff cache as checked input evidence only, and focus further PeTTaChainer work on upstream `materialize-stmt-lambdas`/`mm2compile` instrumentation before full add/query gates.

**Rationale:** Source-level inspection of `pettachainer/pettachainer.py` and `pettachainer/metta/petta_chainer.metta` found public add methods routing through `compileadd`/`compileadd-mine` and no public precompiled/cache/handoff API terms. This matches the prior runtime profiles where `check_stmt` and initialization are healthy but `materialize-stmt-lambdas`/`mm2compile` and add stages time out.

**Alternatives considered:** Adopt a direct KB/precompiled fact add immediately; rejected because source inspection did not reveal a supported public API and direct adds could bypass PeTTaChainer indexing/proof semantics.

## 2026-07-03: Keep compileadd bottleneck work source-grounded before changing semantics

**Decision:** After confirming no public PeTTaChainer precompiled-add/cache API, add a no-runtime source map of the `compileadd` bottleneck path and target future instrumentation at `materialize-stmt-lambdas`, `mm2compile`, and the downstream `compile_` dispatcher before modifying export/add semantics.

**Rationale:** Prior runtime artifacts show tiny promoted-belief add stages timing out while `check_stmt`, constructor init, index-source, and maybe-process hooks are healthy. A source-grounded map narrows the next upstream instrumentation surface without invoking noisy SWI/PeTTaChainer runtime or risking semantic drift. The non-live handoff cache remains the safe integration path until a separate add/query gate passes.

## 2026-07-03: Petta-memory STV proofs should target PeTTaChainer's fact compile branch

**Decision:** Treat the current petta-memory promoted-belief statement shape `(: proof (Requires target PLNReadyViews) (STV s c))` as a PeTTaChainer `compile_` fact-assertion path, not an implication or bidirectional-rule path, unless future export semantics intentionally change the `BeliefContent` type.

**Rationale:** Source-level dispatch inspection of checked-out PeTTaChainer `compile.metta` and `logic_config.metta` shows `(Requires MemoryTarget0 PLNReadyViews)` is a concrete non-`Implication` type and not a configured bidirectional form. After `materialize-stmt-lambdas`/`mm2compile`, `compile_` should therefore use `compile-fact-kb` plus `compile-outputs`. This narrows future instrumentation without invoking runtime `compileadd` or changing the non-live handoff-cache boundary.

## 2026-07-03: Static import is not a direct current PeTTaChainer add bypass

**Decision:** Do not use PeTTa `static-import!` directly for current petta-memory PeTTaChainer exports, and do not treat it as a supported PeTTaChainer precompiled-add/indexing API. Keep it as a possible later non-live scratch benchmark only after symbol quoting/normalization and read-only query semantics are verified.

**Rationale:** Source inspection of checked-out `lib/lib_import.pl` shows a fast `.metta` -> `.pl` -> `.qlf` path, but the converter is line-oriented, intended for S-expression data only/no bangs, and mechanically replaces parentheses/spaces without quoting tokens. Current petta-memory STV/EvidencePacket exports contain uppercase symbols and hyphenated identifiers that are unsafe as unquoted Prolog terms and may not preserve PeTTaChainer compile/index semantics.

**Alternatives considered:** Run `static-import!` immediately as a compileadd bypass; rejected for this slice because it would mix token-conversion uncertainty with PeTTaChainer indexing semantics and could create misleading benchmark results.

## 2026-07-03: Static-import benchmark requires normalized scratch atoms first

**Decision:** Before any runtime `static-import!` microbenchmark, use a scratch-only normalized atom format rather than current PeTTaChainer exports. The designed format uses lowercase/underscore symbols and exactly three top-level fields, e.g. `(pm_stv_statement proof-id (pm_stv_payload statement-key strength confidence))` and `(pm_evidence_packet statement-key (pm_ec_payload support opposition provenance))`.

**Rationale:** PeTTa's converter mechanically turns one line into a Prolog space predicate and declares that predicate as arity 3. Keeping the benchmark records Prolog-safe and arity-compatible isolates loader/query semantics from token quoting bugs and from PeTTaChainer `compileadd` semantics. The benchmark remains non-live, temporary-directory-only, and cannot produce inferred beliefs or OmegaClaw memory writes.

## 2026-07-03: Static-import microbenchmark confirms loader viability for normalized atoms

**Decision:** The non-live runtime `static-import!` microbenchmark passed: 2 normalized atoms were successfully loaded into the `gckb/3` space predicate, all generated `.pl` fact lines matched expected converted Prolog facts, and the predicate count matched (2 facts in ~0.07s). Treat `static-import!` as a confirmed viable bounded loader for Prolog-safe normalized atoms in temporary-directory/non-live benchmarks. It remains a bulk data loader and not a PeTTaChainer `compileadd`/indexing API; do not use it to bypass PeTTaChainer proof/index semantics or claim inferred beliefs.

**Rationale:** The microbenchmark exercised the full `static-import!` path (`.metta` → `.pl` → `.qlf` → consult) with janus_swi in a bounded subprocess. Implementation findings: (1) `static-import!` must be called directly via `janus_swi.query_once` after consulting `lib_import.pl`, not through PeTTa `process_metta_string`; (2) `janus_swi`'s `findall/3` has an instantiation error on the result list variable, so `aggregate_all(count, ...)` and `query_once` are used instead; (3) fact comparison uses generated `.pl` file lines rather than runtime query results to avoid janus iteration limitations.

**Alternatives considered:** Use `static-import!` as a PeTTaChainer compileadd bypass; rejected because it loads atoms into a separate space predicate without PeTTaChainer's compiled proof structures, indexing, or truth-value semantics. The loaded facts are raw data records, not PeTTaChainer-inferred beliefs.
## 2026-07-03: Static-import benchmark spaces must be explicit and safe

**Decision:** Future non-live PeTTa `static-import!` microbenchmarks should use an explicit, Prolog-safe space predicate when isolation matters, and the benchmark must verify generated facts and runtime counts against that same selected predicate rather than assuming `gckb/3`.

**Rationale:** The first loader gate proved normalized atoms can load into `gckb/3`, but follow-up probes may need separate scratch predicates to avoid stale/runtime cross-talk and to compare alternative normalized representations. Validating the space name and using it consistently in expected facts plus runtime queries keeps these checks bounded and avoids a false pass from the default space. This remains a loader benchmark only, not a PeTTaChainer `compileadd`/indexing API or inferred-belief path.

## 2026-07-03: Static-import runtime gates must prove exact fact membership

**Decision:** Treat a PeTTa `static-import!` microbenchmark as passed only when the generated `.pl` facts match expectation, the selected predicate has the expected count, and each expected generated fact is directly queryable against the consulted runtime predicate.

**Rationale:** Text conversion and aggregate count are useful but can miss a false pass where the wrong named space is consulted or generated facts are not actually reachable as runtime Prolog goals. Exact membership checks keep the normalized-atom loader benchmark honest while preserving the existing boundary: this is still not PeTTaChainer `compileadd`/indexing, not query/inference success, and not a live OmegaClaw memory path.

## 2026-07-03: Lambda-free materialize should be an identity gate before mm2compile

**Decision:** For the current petta-memory promoted-belief proof shape, treat `materialize-stmt-lambdas` as expected to be a source-level identity walk because the statement contains no `|->` lambda forms. The next runtime probe should be a narrow non-live materialize identity gate before proceeding to `mm2compile` or full `compileadd`.

**Rationale:** Checked-out PeTTaChainer source only invokes `eval` inside `materialize-stmt-lambdas` when the current expression head is `|->`. The tiny STV proof `(: b-profile-000 (Requires MemoryTarget0 PLNReadyViews) (STV 0.70 0.55))` has 0 lambda forms, so any timeout on this stage is unlikely to be caused by user lambda execution. This narrows the bottleneck toward PeTTa/MeTTa evaluator recursion/materialization overhead while keeping add/query and live OmegaClaw paths gated.

## 2026-07-03: Do not advance past materialize until the identity runtime gate passes

**Decision:** Keep `mm2compile`, full PeTTaChainer `compileadd`/query, and live OmegaClaw/GoalChainer integration gated until a lambda-free `materialize-stmt-lambdas` identity runtime gate completes with matching output under a bounded subprocess timeout.

**Rationale:** The first runtime identity gate for the tiny promoted-belief STV proof timed out at 6s despite source inspection predicting a pure identity walk. That means the blocker is already at materializer/evaluator recursion overhead, before `mm2compile` or the `compile_` fact branch can be meaningfully profiled. Proceeding deeper would conflate stages and risk misleading benchmarks; the next useful work is upstream materializer instrumentation or a smaller evaluator-level reproduction.

## 2026-07-04: Instrument materialization as a ladder before mm2compile

**Decision:** Treat `materialize-stmt-lambdas` as the current blocked PeTTaChainer add-stage boundary, but instrument it as a non-live ladder of source-checked lambda-free subforms before attempting `mm2compile` or `compileadd` again. Identity checks should compare MeTTa structure and tolerate renderer-only numeric formatting changes such as `0.70` to `0.7`.

**Rationale:** The ladder gate shows simple subforms from the promoted-belief proof materialize quickly, while the complete `(: proof type tv)` atom still times out under the bound. This narrows the bottleneck to full proof-atom traversal/evaluator behavior rather than user lambdas, PeTTaChainer construction, static-import loading, or later query/context stages.

**Alternatives considered:** Proceed directly to `mm2compile` instrumentation; rejected because the full proof has not passed the materialization identity gate. Treat string formatting differences as failure; rejected because PeTTa runtime may normalize floats without changing the structure or truth-value semantics.

## 2026-07-04: Keep PeTTaChainer add/query gated after proof-shape materialize timeout

**Decision:** Do not proceed to `mm2compile`, `compileadd`, query, or any live OmegaClaw/GoalChainer integration from the current PeTTaChainer proof-shape gate. Continue instrumentation at the `materialize-stmt-lambdas` evaluator behavior for the full four-field proof atom.

**Rationale:** The proof-shape ladder artifact (`pettachainer_materialize_proof_shape_ladder_gate_2026-07-04T1000Z.json`, sha256 `43669be7cd99dd9fc618ed07297518dd53d1a22527d8fa5d8fb6c9f78553ef24`) showed the type subform, STV subform, `(: proof)`, and `(: proof type)` all materialize as identity quickly, while adding the STV as the fourth field to form the exact proof atom still times out under a 4s bound. This indicates the remaining blocker is not either subform alone and not the shorter proof prefix.

**Alternatives considered:** Treat passing prefix/subform rungs as enough to try `mm2compile`; rejected because the exact full proof statement remains blocked at the first `compileadd` binding.

## 2026-07-04: Target materializer instrumentation at nested statement-type expressions inside proof atoms

**Decision:** Treat the next PeTTaChainer materialization investigation as focused on how `materialize-stmt-lambdas` handles nested statement-type expressions such as `(Requires MemoryTarget0 PLNReadyViews)` when they appear as the type field of a full `(: proof type tv)` atom. Keep `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, and memory-write paths gated.

**Rationale:** The sentinel proof-shape ladder shows that independent type/STV subforms, proof prefixes, and even a synthetic full-arity `(: proof ProofShapeSentinel (STV 1.0 1.0))` atom materialize as identity quickly, while `(: proof (Requires MemoryTarget0 PLNReadyViews) (STV 1.0 1.0))` times out under the same bound. That narrows the failure surface from generic proof arity/STV handling to nested type-expression traversal inside the full proof shape.

**Alternatives considered:** Proceed directly to `mm2compile` or a direct KB fact add; rejected because the pre-`mm2compile` materialization rung remains blocked, and bypassing it risks semantic drift from PeTTaChainer's compile/index path.

## 2026-07-04: Narrow materialize blocker to nested Type arity in full proof atoms

**Decision:** Keep `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, and memory-write paths gated. Continue the PeTTaChainer investigation at `materialize-stmt-lambdas`, focused specifically on full proof atoms whose nested Type expression has at least two arguments, e.g. `(: b-profile-000 (Requires MemoryTarget0 PLNReadyViews) (STV 1.0 1.0))`.

**Rationale:** The nested-Type ladder artifact (`pettachainer_materialize_nested_type_ladder_gate_2026-07-04T1400Z.json`, sha256 `bc5aab720dde2427afb1fbf2ad66dba53c2abcb32022e06b1d0ee4a1f8e8c5f2`) shows that atom Type heads, empty nested Type expressions, and one-argument nested Type expressions materialize as identity quickly under full proof shape plus sentinel STV. The timeout appears only when the nested Type reaches the original two-argument shape. This is a sharper boundary than the previous sentinel proof-shape gate and should guide the next upstream evaluator/materializer reproduction.

**Alternatives considered:** Proceed to `mm2compile` because smaller Type rungs pass; rejected because the exact two-argument nested Type still blocks at the first `compileadd` binding. Treat `static-import!` as a bypass; rejected because it remains a normalized bulk-loader benchmark outside PeTTaChainer compile/index semantics.
## 2026-07-04: Treat two-argument nested Type arity as the current materialize blocker

**Decision:** Keep `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw, and memory-write paths gated. The next PeTTaChainer investigation should reproduce or instrument `materialize-stmt-lambdas` on a full proof atom whose Type field is any two-argument nested expression, before spending time on original-token-specific hypotheses.

**Rationale:** The arity/token matrix artifact (`pettachainer_materialize_nested_type_arity_matrix_gate_2026-07-04T1600Z.json`, sha256 `d24401f89cef49eddb83eb6c03ae2990cb626883c7f2f45b01647238e980fa35`) shows that `(: proof (Requires) (STV 1.0 1.0))` and `(: proof (Requires TypeArgSentinel0) (STV 1.0 1.0))` materialize quickly, but `(: proof (Requires TypeArgSentinel0 TypeArgSentinel1) (STV 1.0 1.0))` times out at 4s. Because the first failing rung uses sentinel arguments rather than `MemoryTarget0` or `PLNReadyViews`, the blocker is now localized to generic nested Type arity inside the full proof shape.

**Alternatives considered:** Continue testing mixed/original argument tokens first; rejected because the all-sentinel two-argument rung already blocks before those controls. Proceed to `mm2compile`; rejected because the first `compileadd` binding still fails on a lambda-free materialization identity check.

## 2026-07-04: Treat materialize blocker as generic nested-expression context cost, not PeTTaChainer `:` syntax

**Decision:** Keep `mm2compile`, full `compileadd`/query, GoalChainer runtime, and live OmegaClaw integration gated while the next diagnostic targets PeTTa/MeTTa evaluator recursion for four-field list contexts containing a two-argument nested expression. Do not focus only on PeTTaChainer `:` proof syntax or original `MemoryTarget0`/`PLNReadyViews` tokens.

**Rationale:** The nested-Type context matrix materializes the all-sentinel two-argument nested Type by itself, under `(: proof type)`, and under a synthetic three-field `ProofEnvelope`, but times out when the same nested expression appears in a generic four-field `ProofEnvelope` with sentinel STV. That shows the current blocker is broader than the `:` proof head while still preceding `mm2compile` and `compile_`.
## 2026-07-04 - Continue upstream materializer instrumentation at generic four-field/nested-arity blocker

Decision: keep PeTTaChainer `mm2compile`, `compileadd`, query, GoalChainer live use, and OmegaClaw integration gated until the upstream `materialize-stmt-lambdas` evaluator behavior is understood for generic four-field lists containing two-argument nested subexpressions.

Evidence: local commit `53eb8e8` and artifact `projects/petta-memory/artifacts/pettachainer_materialize_generic_four_field_context_arity_gate_2026-07-04T2000Z.json` (sha256 `5877d1966b10c99d6eccd66a27e41e49f56b41aab365200b77486919ea6d9e9`) show empty and one-argument nested Types materialize in a synthetic four-field `ProofEnvelope`, while the all-sentinel two-argument nested Type times out at 4s. Prior gates already ruled out original argument tokens and the PeTTaChainer `:` proof head as necessary causes.

Consequence: the next bounded task should inspect or instrument the upstream recursive/materialization/evaluator path around `cons` + `map-flat materialize-stmt-lambdas` on four-field expressions, rather than broadening to `mm2compile`/`compileadd` or live integration.


## 2026-07-04: Refine materialize blocker to proof-like four-field neighbor shape

Decision: keep `mm2compile`, full PeTTaChainer `compileadd`/query, GoalChainer runtime, live OmegaClaw integration, and memory-write paths gated. Continue upstream materializer/evaluator instrumentation on the proof-like four-field shape where a proof id, two-argument nested Type, and STV are adjacent.

Evidence: artifact `projects/petta-memory/artifacts/pettachainer_materialize_four_field_nested_position_gate_2026-07-04T2200Z.json` (sha256 `00dda1cfd8319db4edb5fc665a4d9b40af97493a032c1869cabc24d6a9bb8ac7`) shows the all-sentinel two-argument nested Type materializes as identity when placed in each generic four-field `ProofEnvelope` argument slot with simple Payload siblings, but times out in the proof-like `(ProofEnvelope b-profile-000 nested-type (STV 1.0 1.0))` layout.

Consequence: the blocker is no longer best described as any four-field list containing a two-argument nested expression. The next bounded task should inspect/reproduce how `materialize-stmt-lambdas` handles STV/proof-neighbor payloads around a nested Type, rather than broadening to `mm2compile`/`compileadd` or live integration.
## 2026-07-04: Materialize blocker is STV-sibling shaped, not proof-id-specific

**Decision:** Keep `mm2compile`, full `compileadd`/query, GoalChainer live paths, and OmegaClaw integration gated while the next materializer probes target the adjacent truth-value/STV payload shape in four-field wrappers, rather than proof-id handling alone.

**Rationale:** The four-field neighbor-shape gate showed that `(ProofEnvelope b-profile-000 (Requires TypeArgSentinel0 TypeArgSentinel1) PayloadB)` materializes as identity, while `(ProofEnvelope PayloadA (Requires TypeArgSentinel0 TypeArgSentinel1) (STV 1.0 1.0))` times out. This shifts the suspected blocker from the left proof-id neighbor to the combination of a two-argument nested Type and an STV-shaped right sibling under `materialize-stmt-lambdas`.

**Gates:** No `mm2compile`, `compileadd`, query, GoalChainer, OmegaClaw path, journal write, or inferred-belief claim is enabled by this diagnostic.

## 2026-07-05: patham9/PLN runtime stamps stay chainer-compatible; rich provenance stays sidecar

**Decision:** For the current patham9/PLN bridge, load generated petta-memory `Sentence` inputs into the chainer with numeric evidence stamps (for example `(0)`) while preserving the original `(PMEvidence ...)`, promotion metadata, and contextual `EvidencePacket`/EC counts in the JSON result sidecar. Do not project EC counts into STV or promote query results as inferred beliefs until the π-PLN formula/wrapper boundary is reviewed.

**Rationale:** A direct query smoke showed patham9/PLN's current stamp utilities expect sortable evidence stamps; symbolic `PMEvidence` stamps can trip lower-level sorting. Numeric runtime stamps let the local chainer execute the first read-only query gate while retaining provenance needed for later contextual evidence semantics.

**Consequences:** The patham9 bridge can now run a bounded local `PLN.Query` smoke, but the next gate should test a tiny two-premise derivation with the same numeric-stamp/sidecar policy before deeper π-PLN EC projection work.

## 2026-07-05: Treat patham9/PLN derivation smoke outputs as gated evidence, not memory beliefs

**Decision:** The first two-premise patham9/PLN derivation gate may verify a derived term using one promoted handoff Sentence plus a synthetic bridge implication, but the result remains a runtime smoke artifact only. Numeric stamps are allowed for patham9/PLN compatibility when each stamp is mapped back to PMEvidence or synthetic-bridge provenance in a sidecar.

**Rationale:** This proves the local chainer can do more than direct recall without silently promoting synthetic bridge conclusions into petta-memory, OmegaClaw, or GoalChainer. The wrapper-vs-internal boundary for contextual EC projection formulas still needs review before any derived belief promotion path exists.

## 2026-07-05: Use a wrapper-first boundary for patham9/pi-PLN extensions

**Decision:** Keep the checked-out `patham9/PLN` core unmodified for the next pi-PLN step. Petta-memory will own a wrapper layer that maps promoted handoff evidence into runtime-compatible `Sentence` atoms, assigns simple numeric runtime stamps, preserves PMEvidence/EvidencePacket provenance in sidecars, and later pre-projects reviewed EC/context formulas before calling `PLN.Query` or `PLN.Derive`.

**Rationale:** The direct query and two-premise derivation smokes pass with ordinary `Sentence` atoms, while richer symbolic stamps already showed compatibility risk. A wrapper preserves a working chainer base and keeps provenance/read-write boundaries explicit before truth-changing EC formulas or internal patham9 changes are attempted.

**Consequences:** EC support/opposition is currently summarized as artifact-only projection input, not a live STV change. No inferred result is appended or promoted until a separate reviewed non-live gate validates the formula and provenance behavior.

**Revisit trigger:** If wrapper-level EC/context projection cannot express required pi-PLN semantics, then consider a narrowly scoped patham9/PLN internal extension with regression tests over `StampDisjoint`, queue priority, and proof provenance.

## 2026-07-05: patham9/PLN API surface mapped; wrapper boundary confirmed as sufficient for current pi-PLN extension

**Decision:** Treat the patham9/PLN API surface as now mapped at source level. The wrapper-first boundary remains sufficient for current pi-PLN extension work (sentence construction, STV pre-projection, stamp/provenance sidecar, context selection). Internal patham9/PLN extensions (context-indexed evidence, EC-aware truth formulas, inference control) remain deferred under the existing revisit trigger.

**Rationale:** The source-level `patham9_pln_api_surface(...)` inspection documents all core API entries (PLN.Derive, PLN.Query, Sentence, StampDisjoint, PriorityRank, ConfidenceRank, LimitSize, BestCandidate), 16 truth-value formulas, 17 inference rules, 5 guard predicates, 3 config defaults, 14 utility helpers, 4 translator definitions, and the Python PLN.Init entrypoint. The identified wrapper boundary extension points (sentence construction, stamp assignment, STV pre-projection, context selection, queue priority, provenance lineage) match exactly what the existing `ec_projected_stv()` wrapper formula and handoff/query/derivation smokes already exercise. Internal extension points (context-indexed evidence, EC-aware truth formulas, inference control, custom link types) are documented but not yet needed.

**Consequences:** The next pi-PLN step should either (1) design a concrete π-PLN extension layer spec from the mapped extension points, or (2) test a multi-Sentence derivation with real petta-memory handoff evidence to validate the wrapper boundary at scale, before any internal patham9/PLN modification is attempted.

## 2026-07-09: Real petta-memory evidence export is the non-live Protomegabot replay boundary

**Decision:** Advance the GoalChainer integration by replaying an archived Protomegabot decision candidate over a real `MediumMemoryStore.goalchainer_handoff_cache()` export, rather than Python-constructing synthetic handoff dictionaries. The replay must use a bounded immutable journal, an explicit belief-ID allowlist and item cap, preserve cluster/promotion provenance, hash the journal before/after, and call only local deterministic GoalChainer logic.

**Rationale:** The production petta-memory exporter and GoalChainer `memory_items` heuristic bridge already exist; the remaining evidence gap was the OmegaClaw sidecar's synthetic fixture assembly. A small artifact-local harness proves the real export contract without modifying or enabling either live bridge.

**Consequences:** Gate `projects/omegaclaw/artifacts/ggb-capacity-gates/20260709-goalchainer-real-petta-memory-replay/` is the evidence for this slice. It passed 9/9 checks and left the journal hash unchanged. The next useful non-live step is a second decision/evidence replay with the same bounded contract. LLM task-text-to-logic parsing, AtomSpace population, and ECAN-like attention/LTI/staleness retention are future work only and require separate design and approval.

## 2026-07-05: π-PLN extension layer spec formalized; multi-Sentence derivation smoke program ready

**Decision:** The π-PLN extension layer is now formalized as `patham9_pi_pln_extension_spec()`, covering sentence construction protocol, EC projection formula, provenance sidecar policy, context selection policy, inference control hooks, read/write boundaries, and revisit triggers. The wrapper-first boundary is confirmed as sufficient for current work. A multi-Sentence derivation smoke program builder (`patham9_pln_multi_sentence_derivation_smoke_program()`) is now ready to validate the wrapper boundary with multiple handoff Sentences at scale.

**Rationale:** The spec consolidates the design decisions from the API surface mapping, EC projection smokes, and wrapper boundary plan into a single reviewable artifact. The multi-Sentence derivation smoke extends the single-Sentence derivation pattern to all handoff items, exercising StampDisjoint across multiple numeric stamps and testing that PLN.Query can find a derivation path through multiple loaded beliefs. Both are pure design/program-builder artifacts with no runtime invocation.

**Consequences:** The next step is to run the multi-Sentence derivation smoke with real handoff evidence from the local patham9/PLN runtime to validate the wrapper boundary end-to-end. After that, the remaining open task is connecting petta-memory handoff cache exports as input to the patham9/PLN + π-PLN chainer for a full end-to-end validation. Inference control design remains deferred (roadmap item 4).

## 2026-07-05: Multi-Sentence patham9/PLN programs must use whitespace-separated MeTTa lists, not comma-separated

**Decision:** When building patham9/PLN programs that pass multiple Sentence atoms to `PLN.Query` or `PLN.Derive`, Sentence atoms must be whitespace/newline-separated inside the outer parentheses (MeTTa list syntax), not comma-separated. The multi-Sentence derivation smoke program builder has been fixed accordingly.

**Rationale:** The first end-to-end multi-Sentence derivation smoke failed with empty query results `()` when Sentence atoms were joined with `, ` (comma). Patham9/PLN's MeTTa-to-Prolog translator parses comma-separated items as Prolog conjunctions rather than list elements, producing a malformed sentence list that the chainer cannot match. The working single-derivation smoke already used whitespace/newline separation. After changing the separator from `, ` to `\n                  `, the same multi-Sentence program passed with correct derivation output `((stv 0.706 0.495) (0 3))`.

**Consequences:** Any future code that constructs patham9/PLN programs with multiple Sentence atoms or other list items must use whitespace separation, not commas. This is a MeTTa syntax requirement, not a patham9/PLN-specific one.

## 2026-07-05: trueagi-io/chaining inference-control patterns surveyed for pi-PLN wrapper adoption

**Decision:** Survey six concrete inference-control patterns from the trueagi-io/chaining repo (commit `bc9beb2`) as source-level, no-runtime artifacts mapping to pi-PLN wrapper extension points. All six patterns can be adopted at the wrapper boundary without modifying patham9/PLN source. Categorize by adoption complexity: near-term (probabilistic filtering, meta-learning benchmark), medium-term (controlled chainer, continuation predicate), long-term (PLN estimator, controller-as-chainer).

**Rationale:** The pi-PLN extension spec defers inference control to roadmap item 4. Ben pointed to the trueagi-io/chaining repo as possibly useful for PLN prototypes and inference control. The survey provides concrete patterns for that deferred item, documenting key concepts (EDCall, Thompson sampling, context updaters, continuation predicates, probabilistic filtering) and how each maps to the wrapper boundary. This avoids premature implementation while ensuring the design space is mapped.

**Alternatives considered:** (1) Start implementing a specific inference-control pattern immediately. Rejected because the basic patham9/PLN pipeline just reached end-to-end validation; design space should be surveyed first. (2) Skip the survey and revisit when inference control becomes urgent. Rejected because Ben explicitly flagged the repo and the patterns are relevant to current design decisions about context selection and EC projection.

**Consequences:** The survey informs the next inference-control design step. The near-term probabilistic filtering pattern is the most immediately actionable: STV confidence (potentially via `ec_projected_stv()`) as a filter probability for Sentences before loading into PLN.Derive. The medium-term continuation predicate pattern aligns with the wrapper's context selection policy. The long-term PLN estimator pattern would require running the chainer at two levels.

## 2026-07-06: Implement continuation predicate as first medium-term inference-control pattern

**Decision**: Implement the "continuation predicate" pattern from the trueagi-io/chaining survey as the first medium-term inference-control mechanism. The wrapper evaluates each handoff item against six continuation criteria (STV strength, STV confidence, derivation depth, domain match, EC support ratio, promotion rule match) and produces one of three decisions: `continue`, `terminate`, or `reject`. The key distinction from the near-term probabilistic filter and context selection wrapper is that the continuation predicate can *terminate* an item (keep it as a final result without further derivation) rather than only accepting or rejecting it.

**Rationale**: All four near-term patterns (probabilistic filtering, context selection, chained pipeline, meta-learning benchmark) are now implemented. The continuation predicate is the natural next step from the survey: it was categorized as medium-term complexity and directly maps to the backward-chaining continuation predicates in `trueagi-io/chaining/experimental/inference-control/inf-ctl-month-bc-cont-xp.metta`. The three-way decision (continue/terminate/reject) is semantically richer than the existing two-way wrappers (include/exclude) and provides a testable foundation for the remaining medium-term pattern (controlled backward chainer) and long-term patterns (PLN estimator, controller-as-chainer).

**Alternatives considered**: (1) Implement the controlled backward chainer pattern next instead. Rejected for this slice because the continuation predicate is a simpler building block that the controlled chainer would likely depend on. (2) Wait until all near-term patterns are validated with live runtime tests. Rejected because the wrapper-level design space is still being mapped and the continuation predicate extends the design without requiring live runtime.

**Consequences**: The remaining medium-term pattern (controlled backward chainer with context updaters) and both long-term patterns (PLN estimator, controller-as-chainer) are still open. The continuation predicate wrapper provides a foundation for the controlled chainer: a controlled chainer could use the continuation predicate as its per-branch decision function, adding context updaters and a termination condition around it.

## 2026-07-06: Implement controller-as-chainer as final inference-control pattern

**Decision**: Implement the "controller-as-chainer" pattern from the trueagi-io/chaining survey as the second long-term inference-control mechanism. A second backward chainer instance (with stricter parameters) supervises the primary chainer's continuation decisions, providing a meta-level termination policy that can confirm, override-terminate, or override-reject branches the primary would have continued.

**Rationale**: All seven prior patterns (4 near-term, 2 medium-term, 1 long-term) are now implemented. The controller-as-chainer is the final pattern from the survey. It builds on the controlled backward chainer by running it as the primary chainer, then evaluating its results with a controller chainer that has independent (typically stricter) parameters. Override-terminate takes priority over override-reject because termination preserves the result as a final answer rather than discarding it.

**Alternatives considered**: (1) Skip this pattern since it is long-term and complex. Rejected because it completes the survey implementation and provides the meta-level control concept that the survey identified as the most sophisticated pattern. (2) Wait for live runtime validation of prior patterns first. Rejected because the wrapper-level design space is fully mapped and this pattern extends the design without requiring live runtime.

**Consequences**: All eight inference-control patterns from the trueagi-io/chaining survey are now implemented at the wrapper level. The next inference-control work would be to validate these patterns against the patham9/PLN runtime in a bounded non-live gate, or to design a unified inference-control policy that composes multiple patterns. The PeTTaChainer `compileadd` upstream instrumentation track remains deprioritized in favor of the patham9/PLN pivot.
