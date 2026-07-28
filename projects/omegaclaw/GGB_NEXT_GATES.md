# Protobots GGB Next Gates

- Updated: 2026-07-28 15:34 UTC
- Scope: next small, non-live empirical gates; the full capacity history remains in `GGB_CAPACITIES_ROADMAP.md`.
- Rule: one bounded artifact, one negative fixture, one replay command, and explicit non-actions per gate.

## Current frontier

The representation contract is frozen independently of semantic evolution.
The first explicit v0.2-to-v0.3 candidate-registry migration adds only
`defer_for_review`, preserves checkpoint cursor/incumbent/trace, and binds the
old/new registry and checkpoint digests in a candidate-only receipt. Seven
provider-free tests pass; downgrade, removal/renumbering, mutation, authority
widening, and checkpoint unbinding fail closed. Evidence:
`artifacts/ggb-capacity-gates/20260725-motivation-candidate-registry-migration/`.
An independent consumer now verifies the receipt and preserved-tail replay.
A separate preregistered holdout advances the pinned cursor only after all
three preserved candidates and reaches exactly `defer_for_review`, with no
score function and no scoring-policy change. Five provider-free checks pass at
`artifacts/ggb-capacity-gates/20260725-motivation-new-candidate-reachability/`.
An independent strict consumer now reproduces that result from sealed JSON
without importing producer or prior gate code. Six checks cover deterministic
selection plus duplicate-member, trailing-content, mutation, rehashed-cursor,
and rehashed-authority negatives at
`artifacts/ggb-capacity-gates/20260725-motivation-new-candidate-serialized-consumer/`.
The evidence contract is now frozen at
`artifacts/ggb-capacity-gates/20260726-motivation-reachability-contract-freeze/`.
Five checks pin artifact identities, replay position, exact selection, no
score policy, and candidate-only authority. This grants no runtime authority.
The separate score-policy v0.1 preregistration now passes seven provider-free
contract checks at
`artifacts/ggb-capacity-gates/20260726-motivation-score-policy-preregistration/`.
It binds fixed-point arithmetic, exact features and weights, conservative tie
breaking, a review-risk override, three holdouts, and candidate-only authority
without changing the frozen predecessor. The independent runner reproduced all
three selections in five provider-free checks. A separately sealed
five-case boundary holdout binds both policy and runner identities and
discriminates four-way/request-review ties, a one-unit rank change, and the
adjacent 799/800 override boundary. Eight contract checks pass at
`artifacts/ggb-capacity-gates/20260726-motivation-score-policy-boundary-holdout-preregistration/`.
An independent runner now reproduces all five sealed selections and reasons
without importing the preregistration validator or prior runner. Six
provider-free checks cover sealed-byte drift, expectation drift, malformed
features, weakened admission, and authority widening at
`artifacts/ggb-capacity-gates/20260727-motivation-score-policy-boundary-holdout-independent-runner/`.
No policy parameter was calibrated. An out-of-sample feature-interaction suite
is now sealed at
`artifacts/ggb-capacity-gates/20260727-motivation-score-policy-feature-interaction-preregistration/`.
Seven cases probe joint feature pressure, score crossovers, and override
interaction. It also preregisters the structural finding that
`inspect_evidence` is dominated by `defer_for_review` throughout the valid
feature domain and therefore cannot be selected under v0.1. Nine
provider-free contract checks pass. Its independent runner reproduced all
seven cases and proved the v0.1 dominance result. The separately versioned
v0.2 policy candidate replaces the unreachable evidence action's score with
the internally derived `evidence_gap = 1000 - evidence_sufficiency`. Its
independent runner reproduces all five sealed witnesses, reaches all four
candidates, and passes eight provider-free checks at
`artifacts/ggb-capacity-gates/20260727-motivation-score-policy-v02-independent-runner/`.
The v0.2 boundary suite is now preregistered at
`artifacts/ggb-capacity-gates/20260727-motivation-score-policy-v02-boundary-preregistration/`.
Eight sealed cases cover the exact and adjacent inspect/answer and
inspect/request boundaries plus the adjacent 799/800 review override where
the override replaces an otherwise winning inspection action. Seven
provider-free contract checks pass, and its independent runner reproduced all
eight cases. The follow-on joint-feature suite is preregistered at
`artifacts/ggb-capacity-gates/20260728-motivation-score-policy-v02-joint-feature-preregistration/`.
Seven new cases vary all three admitted inputs below the override; eight
provider-free contract checks pass. A new independent runner reproduced all
seven selections without importing the validator or prior runners. Six
provider-free checks cover sealed/source identity, strict JSON, malformed and
derived inputs, expectation/set drift, admission weakening, and authority
widening at
`artifacts/ggb-capacity-gates/20260728-motivation-score-policy-v02-joint-feature-independent-runner/`.
No calibration was performed. The combined v0.2 evidence freeze now
content-addresses all three preregistration/execution pairs, recomputes 20
executed cases and four-candidate coverage, and verifies candidate-only,
adjudication-required authority in five provider-free checks at
`artifacts/ggb-capacity-gates/20260728-motivation-score-policy-v02-evidence-freeze/`.
No calibration dataset is authorized. Next: draft a synthetic-only calibration
dataset contract with disjoint calibration/confirmation identities and no
parameter fitting.

| Priority | Gate | GGB capacities | Existing anchors | Pass condition | Next implementation task | Status |
|---|---|---|---|---|---|---|
| 1 | Motivation score-policy v0.2 reachability | 1.2, 2.2, 3.2, 3.5, 4.1, 5.2, 5.4 | Frozen candidate registry; v0.1 interaction dominance result; fixed-point and strict-consumer gates; GoalChainer-shaped candidates; ThreadKeeper candidate-only boundary | An independent runner binds the sealed revision sources, derives evidence gap without accepting it from callers, reproduces every witness, reaches every registered candidate, and rejects identity/input/policy/admission/authority drift | **DONE 2026-07-28:** combined freeze binds three preregistration/execution pairs, 20 reproduced cases, and all four candidates. Evidence: `artifacts/ggb-capacity-gates/20260728-motivation-score-policy-v02-evidence-freeze/`; 5/5 provider-free checks pass. Next: synthetic-only calibration dataset contract; no fitting yet | ✅ pass; evidence frozen, no calibration |
| 1 | Motivation-state v0.1 replay | 1.2, 2.1, 2.2, 3.2, 3.5, 4.1, 4.3, 5.2, 5.4 | Bach assessment; MetaMo `G × M`; immutable `petta-memory` snapshot; GoalChainer candidates; ThreadKeeper candidate-only boundary | A pinned evidence snapshot deterministically updates two bounded needs and ranks fixed candidates; ordering is invariant; mutation, stale/missing time, and invalid/non-finite state fail closed; uncertainty urgency is monotonic | **DONE 2026-07-20:** 7/7 provider-free tests plus compile pass; `inspect_bounded_evidence` ranks first; output is adjudication-required with ThreadKeeper effect `none`. Evidence: `artifacts/ggb-capacity-gates/20260720-motivation-state-replay/`. Next: three-event temporal decay/restart-equivalence fixture, still candidate-only | ✅ pass |
| 1 | Motivation temporal replay v0.1 | 1.2, 2.1, 2.2, 3.2, 3.5, 4.1, 4.3, 5.2, 5.4 | Motivation-state v0.1; MetaMo state evolution; GoalChainer-shaped candidates; ThreadKeeper effect boundary | Three strictly ordered events apply elapsed-time decay; a self-hashed checkpoint resumes to the same terminal state/ranking as uninterrupted replay; checkpoint mutation and non-monotonic time fail closed; a clock-only event does not oscillate the top rank | **DONE 2026-07-20:** 6/6 provider-free tests plus compile pass; `inspect_bounded_evidence` remains first and every output remains adjudication-required/candidate-only with effect `none`. Evidence: `artifacts/ggb-capacity-gates/20260720-motivation-temporal-replay/`. Next: preregister a competing-needs rank switch with hysteresis | ✅ pass |
| 1 | Motivation competing-needs rank switch v0.1 | 1.2, 2.1, 2.2, 3.2, 3.5, 4.1, 4.3, 5.2, 5.4 | Motivation-state and temporal replays; MetaMo competing needs; GoalChainer-shaped candidates; ThreadKeeper effect boundary | A pinned state/event sequence produces exactly one preregistered rank switch; a small counter-perturbation below an explicit hysteresis margin cannot oscillate selection; malformed inputs and changed expectation fail closed | **DONE 2026-07-20:** 7/7 provider-free tests plus compile pass; selection switches once from `inspect_bounded_evidence` to `answer_from_current_model`, then remains stable across a small uncertainty wobble. Evidence: `artifacts/ggb-capacity-gates/20260720-motivation-rank-switch/`. Next: checkpoint/restart equivalence including incumbent and hysteresis-policy identity | ✅ pass |
| 1 | Motivation hysteresis checkpoint v0.1 | 1.2, 2.1, 2.2, 3.2, 3.5, 4.1, 4.3, 5.2, 5.4 | Rank-switch replay; MetaMo state continuity; GoalChainer-shaped candidates; ThreadKeeper effect boundary | A self-hashed checkpoint binds input, state, event cursor, incumbent, and hysteresis policy; resumed replay exactly matches uninterrupted selection and terminal state; mutation, policy drift, and invalid incumbent fail closed | **DONE 2026-07-21:** holdout and topology replays support margin `0.05` in their original score units. A scale-sensitivity replay then shows the absolute margin is not portable, while a scale-bound margin preserves the trace at `1.0`, `0.5`, and `0.25`. Evidence: `artifacts/ggb-capacity-gates/20260721-motivation-score-scale/`. Candidate-only; no runtime default frozen. Next: preregister a dimensionless normalization contract and fail-closed scale metadata | ✅ pass |
| 1 | Memory-informed disposition appraisal | 1.2, 2.1, 2.2, 3.2, 3.5, 4.1, 4.3, 5.2, 5.4 | Operator dispositions `f09c621`; restart stability `8c106b6`; immutable `petta-memory` evidence replay; GoalChainer reviewer thresholds; [gate contract](GGB_DISPOSITION_APPRAISAL_GATE.md) | A provider-free, read-only appraisal deterministically ranks only `hold`, `request_cancel`, `fail_terminal`, or `expire` from exact task/checkpoint and selected evidence. Ambiguity defaults to adjudicated `hold`; changed provenance or any direct-effect request fails closed; persistent roots remain unchanged | **DONE 2026-07-17; hardened 2026-07-18:** provenance, threshold, and bounded perturbation gates pass. The latest artifact exhaustively tests 405 score samples: four clear archetypes are 81/81 stable; the ambiguous case adjudicates 72/81 and otherwise resolves only to its nominal top action; 15/15 checks and 4 unit tests pass. Evidence: `artifacts/ggb-capacity-gates/20260718-disposition-perturbation-calibration/`. Next offline slice, before any canary: derive a separately reviewed, redacted corpus from immutable evidence packets and preregister reference labels; a canary still requires Ben's explicit decision | ✅ pass |
| — | Crash-before-handoff stability and operator dispositions | 3.1, 3.2, 3.4, 3.5, 4.1, 5.2, 5.4 | Formal handoff `b6be4ea`; retry/requeue reconstruction `35bf3b1`; WAITING_INPUT enforcement `50aaaa2`; restart stability `8c106b6`; operator dispositions `f09c621` | A task lacking a current formal handoff remains effect-free across restarts. An explicit disposition is immutable and bound to the exact task, manifest, newest opaque checkpoint, actor, rationale, and evidence, without fabricating a handoff, using an older checkpoint, or enqueueing work | **DONE 2026-07-17:** restart gate produced identical `handoff_required` outcomes and zero enqueues; `hold`, `request_cancel`, `fail_terminal`, and `expire` records replay idempotently across event-write crashes. Combined provider-free gate: 375 passed; evidence: `experiments/20260717T210750Z-threadkeeper-operator-dispositions/` | ✅ pass |
| 2 | Isolated ProtoMegaBot2 persistent-worker canary contract | 3.1, 3.2, 3.4, 3.5, 4.1, 5.1, 5.2, 5.5 | Completed provider-free supervisor boundary at `e7e997e`; restart harness `c06725e`; reconciliation `3673e94`; isolated ProtoMegaBot2 path | Before any launch, record an approved exact root/config, fake or explicitly approved provider, zero Telegram egress, one synthetic task, strict attempt/token/tool/runtime caps, cancellation/stop path, expected artifacts, rollback, and a production-path isolation check; a preflight must fail closed when approval or any bound is absent | **DONE offline 2026-07-17:** draft manifest and inspection-only validator archived at `artifacts/ggb-capacity-gates/20260717-protomegabot2-persistent-canary-contract/`; contract validation and ten negative tests pass. Launch preflight intentionally fails without approval. Next action requires Ben's explicit scope/stop-condition approval; do not launch or wire runtime/provider/Telegram behavior | 🟡 contract pass; launch blocked pending approval |
| 3 | Persistent-worker supervisor boundary | 3.1, 3.2, 3.4, 3.5, 4.1, 5.1, 5.2, 5.5 | Persistent lifecycle/status, recovery, receipts, budgets, inbox/results, and execution accounting; reconciliation `3673e94`; process restart harness `c06725e`; exclusive ownership `e7e997e` | A provider-free supervisor pass restarts from verified state, observes cancellation before effects, stops on budget exhaustion, excludes concurrent owners, and never widens queue/provider/Telegram authority | **DONE** 2026-07-16: restart/cancellation records exactly one enqueue and zero runner effects; a two-interpreter contention fixture proves the contender fails before effects while the owner enqueues exactly once. Lifecycle: 49 passed; combined provider-free gate: 362 passed. Evidence: `experiments/20260716T193800Z-threadkeeper-persistent-supervisor-subprocess-v1/` and `experiments/20260716T210300Z-threadkeeper-persistent-supervisor-ownership-v1/` | ✅ pass |
| 4 | Persistent-worker execution accounting | 3.1, 3.2, 3.4, 4.1, 5.1, 5.2, 5.4 | Task budget ledger `4b7399e`; crash-safe result accounting `fed6c2a`; queue runner structured returns | Queue results expose mechanically observed token, attempted-tool, and whole-second runtime counters; receipts bind them before one idempotent ledger append; malformed counters fail closed | **DONE** 2026-07-16: implementation `c1f7b57`, documentation `a756315`; provider-free combined gate passes 356 tests. Evidence: `experiments/20260716T113400Z-threadkeeper-persistent-execution-accounting-v1/` | ✅ pass |
| 5 | Persistent-worker inbox/result delivery | 3.1, 3.2, 3.4, 3.5, 4.1, 4.3, 5.1, 5.2, 5.4, 5.5 | Inbox storage `66b249a`; consumption receipts `dc8dd79`; terminal delivery/acknowledgement `bf5cf10` | Inbox consumption cannot enqueue twice across receipt/event crashes; terminal deliveries are immutable, event-bound, at-least-once, and idempotently acknowledged | **DONE** 2026-07-16: consumption and delivery slices pass the 355-test combined provider-free gate. No supervisor or live runtime wiring | ✅ pass |
| 6 | Persistent-worker attempt/checkpoint/requeue recovery | 3.1, 3.2, 3.4, 3.5, 4.1, 5.1, 5.2, 5.5 | Attempt/checkpoint records at `43d34fe`; explicit requeue at `9727ad7`; verified checkpoint handoff at `1b2d670`; manifest-bound enqueue receipts at `29948e9` | One active lease per task; immutable hash-linked checkpoint lineage; stale claims fail closed; resume binds verified checkpoint identity/payload; spawn/requeue retries after the queue-effect/event crash window do not enqueue twice; corrupt receipts fail closed | **DONE** 2026-07-15: provider-free recovery, requeue, handoff, and enqueue-receipt slices passed the combined 340-test gate. Evidence: `experiments/20260715T151639Z-threadkeeper-persistent-attempt-checkpoint-recovery-v1/` and `experiments/20260715T190300Z-threadkeeper-persistent-enqueue-receipts-v1/` | ✅ pass |
| 7 | Persistent lifecycle/status and spawn/cancel | 3.1, 3.2, 3.4, 4.1, 5.1, 5.2 | Branch `agent/threadkeeper-persistent-workers`; MeTTa lifecycle truth table; versioned manifests/events; validated queue-only spawn; durable cancellation token | Tampering and invalid transitions fail closed; duplicate spawn/cancel IDs are idempotent; cancellation winning before claim causes zero worker/provider calls; bounded `delegate` tests remain unchanged | **DONE** 2026-07-15: lifecycle gate passed 5 unit + 10 regression tests and PeTTa/SWI compile; durable storage/status commit `f82d168`; spawn/cancel gate passed 315 combined tests. Replayed locally by this roadmap worker: 315 passed, Python compile and `git diff --check` clean | ✅ pass |
| 8 | Goal/task adapter conformance | 1.1, 2.2, 3.2, 4.3, 4.5, 5.1, 5.5 | `docs/GOAL_TASK_STATE_CONTRACT.md`; GoalChainer canary; ThreadKeeper queue validation; read-only `petta-memory` handoff | Eligible `recommended`/`candidate` decisions become checksum-protected, patch-proposal-only, adjudication-required candidates; forbidden/held/weak/blocked/malformed/duplicate actions never queue | **DONE** 2026-07-14: `goal_task_adapter_validator.py` + 48-test negative matrix; commit `d993e49`; gate archived at `artifacts/ggb-capacity-gates/20260714-ggb-goal-task-adapter-conformance/` | ✅ pass |
| 9 | Immutable evidence → appraisal replay | 1.2, 2.1, 2.2, 3.1, 4.3, 5.2, 5.4 | `petta-memory` EvidenceSnapshot v2 / PiChart; patham9 admitted handoff; GoalChainer heuristic-memory bridge | Replaying one pinned snapshot yields the same admitted evidence IDs, decision ordering, proof pointers, and hashes; one mutated packet or stale chart fails before appraisal | **DONE** 2026-07-14: replay bundle with source hashes, determinism check, packet-mutation negative, stale-chart negative, memory-read-only, no-promotion; 5/5 checks pass; gate archived at `artifacts/ggb-capacity-gates/20260714-ggb-immutable-evidence-replay/` | ✅ pass |
| 10 | Neutral GGB run-contract schema | 2.3, 3.4, 4.4, 5.2, 5.4 | `petta-chem` run contracts; positional and two keyword-shaped GGB fixtures; local PeTTa runtime checker | A normalized v0.1 summary/check schema represents one chemistry, one ThreadKeeper, one memory, and one GoalChainer gate without source-specific parsing; old fixtures remain replayable | **DONE** 2026-07-14: 8-shape neutral schema + 4 translated fixtures + validator; 5/5 checks pass; old fixtures still replayable; gate archived at `artifacts/ggb-capacity-gates/20260714-ggb-neutral-run-contract-schema/` | ✅ pass |

## Hold points

The 2026-07-18 disposition corpus preregistration is now hardened at the
dataset boundary: duplicate record IDs, duplicate complete provenance tuples,
repeated packet digests within a record, reuse of task/checkpoint/packet
digests across records, unbound document metadata, and empty, non-string, or
unscoped reviewer/adjudicator identities fail closed. This blocks
correlated provenance from crossing a later evaluation split or inflating
sample size. The next permitted slice remains synthetic/offline; selecting or
redacting operational evidence requires separate review.

The synthetic-only split contract is now frozen at
`artifacts/ggb-capacity-gates/20260719-disposition-split-preregistration/`.
Its deterministic 60/20/20 assignment depends only on a scoped seed and the
immutable task-version digest; record order, labels, and reviewer metadata are
excluded from assignment. The report now binds the exact canonical input with
`input_corpus_sha256`, making any relabeling or reviewer-metadata change visible
without causing label leakage. Twelve unit checks plus fixture replay pass. This still does not
authorize selection or redaction of operational evidence.

The synthetic-only split adequacy contract is archived at
`artifacts/ggb-capacity-gates/20260719-disposition-split-adequacy/`. Before any
scoring, it requires exact corpus/assignment identity, at least four examples
per partition, and all four authorized disposition labels in every partition.
This prevents an apparently valid hash split from silently yielding empty,
underfilled, or label-incomplete evaluation strata. It does not authorize an
operational corpus or scorer fitting.

- **Live private Telegram / GoalChainer sidecar:** blocked pending explicit Ben approval and stop conditions. Exclusive persistent-supervisor ownership is now provider-free tested, but existing offline acceptance is not live authority.
- **ThreadKeeper integration:** persistent work is isolated on `agent/threadkeeper-persistent-workers`, based on `agent/threadkeeper-hardening-next` commit `a2c62eb`; preserve bounded `delegate`, coordinate with PR #1, and do not overwrite the modified OmegaClaw-Core runtime tree.
- **Formal handoff maturity:** schema, process-death reconstruction, retry and
  `WAITING_INPUT` enforcement, restart stability, and auditable operator
  dispositions now pass provider-free gates through `f09c621`. This evidence
  still grants no authority to modify PR #1 or live runtime wiring.
- **Persistent-worker live effects:** a canary manifest/validator may be prepared offline, but launching a supervisor, using a provider or Telegram, touching ProtoMegaBot/ProtoMegaBot2 runtime paths, or using credentials remains outside current authority. A passing checkpoint, budget, delivery, or ownership test is evidence, not deployment authority.
- **PeTTaChainer `compileadd`:** keep isolated; the bounded patham9/heuristic routes are evidence gates, not proof that the bottleneck is solved.
- **Algorithmic chemistry claims:** preserve `emergence-claim none` until random/control multi-run evidence meets the project criteria.

## Graduation evidence

Each new gate bundle must include:

1. pinned source/artifact identities and hashes;
2. bounded inputs, permissions, and timeout;
3. positive and fail-closed negative fixtures;
4. exact commands and observed results;
5. claim/evidence separation and known exclusions;
6. explicit confirmation of no live egress, memory write/promotion, paid compute, secret access, push, merge, or runtime authority change.
