# Phase B Implementation Plan and Test Matrix

Date: 2026-07-24  
Status: frozen for the smallest shadow-only vertical slice  
Inputs: Revision 2 design, `docs/runtime-discovery.md`, and
`docs/event-ledger-contract.md`

## Outcome

Implement a standalone OpenClaw plugin at
`plugins/conversation-governor/`. The plugin will normalize events, compute
deterministic admission and egress decisions, and append audit records without
changing inference or delivery while `mode = "shadow"`.

Phase B freezes interfaces and module boundaries. The first executable slice
will prove the contract end to end for one inbound event and one outbound
candidate. It will not activate suppression, allocate production leases, call
a classifier, compute embeddings, or modify the existing intent router.

## Relevant research rules

- **Rule 1:** validate the governor with exact fixtures before trusting it to
  classify live traffic.
- **Rule 2:** freeze stateful invariants and schemas before implementation.
- **Rule 3:** use OpenClaw's documented plugin hooks and Node test runner
  rather than creating a parallel runtime.
- **Rule 7:** keep policy, runtime adapters, state, and persistence replaceable
  behind narrow interfaces.

## Architecture decision

Phase A confirmed Topology A: all configured agents share one gateway and one
plugin pipeline.

- `before_agent_run` is the pre-inference admission seam.
- `reply_payload_sending` is the pre-delivery egress seam.
- `intent-model-router` continues to own `before_model_resolve`.
- The new governor coordinates with the router; it does not absorb or replace
  model selection.
- A topology-neutral pure core remains worthwhile so a later deployment can
  substitute coordinated local adapters without rewriting policy.

## Proposed repository layout

```text
plugins/conversation-governor/
├── package.json
├── openclaw.plugin.json
├── index.js
├── config.js
├── core/
│   ├── ids.js
│   ├── normalize-event.js
│   ├── classify-control.js
│   ├── admission.js
│   ├── ownership.js
│   ├── leases.js
│   ├── thread-state.js
│   ├── egress.js
│   ├── semantic-firewall.js
│   └── cost.js
├── adapters/
│   └── openclaw-hooks.js
├── state/
│   ├── memory-store.js
│   └── jsonl-ledger.js
├── schemas/
│   ├── event-envelope.schema.json
│   ├── admission-decision.schema.json
│   ├── response-lease.schema.json
│   ├── thread-state.schema.json
│   ├── egress-candidate.schema.json
│   └── ledger-record.schema.json
├── fixtures/
│   ├── retry-idempotency.json
│   ├── own-message-loopback.json
│   ├── sibling-not-addressed.json
│   ├── parallel-answer-lease.json
│   ├── visible-silence.json
│   ├── human-override.json
│   ├── closed-thread-ack.json
│   ├── shadow-observation.json
│   ├── governor-cost.json
│   └── semantic-firewall.json
└── test/
    ├── schema.test.js
    ├── normalization.test.js
    ├── admission.test.js
    ├── ownership.test.js
    ├── leases.test.js
    ├── thread-state.test.js
    ├── egress.test.js
    ├── semantic-firewall.test.js
    ├── ledger.test.js
    └── hooks-shadow.test.js
```

The canonical prose contract stays in the project notebook. Executable schemas
and minimized fixtures live with the plugin so its tests do not depend on
workspace-relative paths.

## Module responsibilities

| Module | Responsibility | Must not do |
|---|---|---|
| `index.js` | Register plugin hooks and lifecycle; construct dependencies | Contain policy rules |
| `config.js` | Validate defaults and feature flags | Read secrets or mutate live config |
| `core/ids.js` | Deterministic event, lease, and record IDs | Use random IDs for idempotent objects |
| `core/normalize-event.js` | Map trusted hook fields into `EventEnvelope` | Infer semantic project state |
| `core/classify-control.js` | Exact control values, known bot IDs, override grammar | Use embeddings or an LLM |
| `core/admission.js` | Pure ordered decision cascade and reason codes | Enforce hook outcomes directly |
| `core/ownership.js` | Precedence, explicit address, capability owner, stickiness | Send or redirect messages |
| `core/leases.js` | Atomic in-process lease acquire/renew/complete/expire | Persist unrelated conversation text |
| `core/thread-state.js` | Validate lifecycle transitions and reopen conditions | Reopen from acknowledgments |
| `core/egress.js` | Produce `SEND`, `SUPPRESS`, `REPAIR_THEN_SEND`, `AGGREGATE` | Rewrite substantive content |
| `core/semantic-firewall.js` | Permit only truncation, formatting, narration stripping | Add, alter, or summarize claims |
| `core/cost.js` | Record CPU, model calls, tokens, projected savings | Invoke models during Phase B |
| `adapters/openclaw-hooks.js` | Translate decisions into hook pass/block/cancel results | Decide policy |
| `state/memory-store.js` | Active event keys, leases, and thread state | Claim crash durability |
| `state/jsonl-ledger.js` | Append bounded audit records with restrictive permissions | Store credentials or raw broad transcripts |

## Public interfaces

The pure core should expose these interfaces:

```js
normalizeBeforeAgentRun(event, context, config) -> EventEnvelope
decideAdmission(envelope, snapshot, config, clock) -> AdmissionDecision
decideEgress(candidate, snapshot, config, clock) -> EgressCandidate
applyNonSemanticRepair(candidate, contract) -> EgressCandidate
applyAdmissionToHook(decision, mode) -> InputGateDecision | undefined
applyEgressToHook(candidate, mode) -> ReplyPayloadSendingResult | undefined
appendLedgerRecord(record) -> void
```

All time and storage dependencies are injected in tests. Pure decision
functions do not read global config, the filesystem, environment variables, or
the network.

## Configuration

Initial manifest fields:

```json
{
  "enabled": true,
  "mode": "shadow",
  "ledgerPath": "~/research-agent/plugins/conversation-governor/ledger",
  "knownBotIds": [],
  "ownerByChannel": {},
  "leaseTtlMs": 300000,
  "stickinessMs": 600000,
  "featureFlags": {
    "admission": true,
    "egress": true,
    "leases": false,
    "threadState": false,
    "humanOverrides": false,
    "nonSemanticRepair": false,
    "semanticDedup": false
  }
}
```

Safety invariants:

1. Missing or invalid mode fails to `shadow`.
2. `semanticDedup` remains false and unsupported in the Phase B slice.
3. `active` mode is implemented only after the applicable later-phase gate
   and explicit approval; Phase B tests reject accidental enforcement.
4. The ledger path is explicit, local, and created with user-only
   permissions.
5. Governor failures fail open for message delivery and emit a bounded audit
   error without message bodies or secrets.

## Decision order

### Admission

1. Normalize and validate the event.
2. Parse an explicit human override.
3. Check duplicate event/message identity.
4. Check own-message loopback.
5. Check non-addressed sibling bot traffic.
6. Check closed-thread and unchanged-state conditions.
7. Resolve explicit owner, existing lease, task owner, capability owner,
   stickiness, then channel default.
8. Record cost and the complete decision.
9. In shadow mode return pass regardless of the counterfactual decision.

Human safety, authority, spending, and explicit addressing bypass quietness
rules before lower-precedence suppression.

### Egress

1. Normalize the reply payload into `EgressCandidate`.
2. Check structured no-send and exact silence markers.
3. Check owner/lease and exact duplicate state when those feature flags are
   enabled.
4. Validate the response contract.
5. Permit only firewall-approved non-semantic repair.
6. Record cost and the complete candidate.
7. In shadow mode return the original payload unchanged.

## Ledger behavior

- `decisions.jsonl` receives admission and egress records.
- `leases.jsonl` and `threads.jsonl` are introduced with their feature slices.
- One JSON object is appended per line.
- Writes are serialized within the gateway process.
- Records include schema version, deterministic record ID, timestamp, mode,
  reason codes, and governor cost.
- Phase B stores hashes and bounded metadata. Raw prompt/output text is omitted
  by default; fixture tests use synthetic text.
- A malformed prior line does not prevent a new append, but is counted during
  replay.
- Gateway restart clears active Maps. Reconstructing leases from JSONL is
  explicitly deferred until restart behavior is measured.

## Hook integration

### `before_agent_run`

The adapter constructs an envelope, reads a state snapshot, calls
`decideAdmission`, and writes a ledger record. In `shadow` it returns
`undefined` or `{ outcome: "pass" }`. It never returns block in Phase B.

### `reply_payload_sending`

The adapter constructs an egress candidate and calls `decideEgress`. In
`shadow` it returns no mutation and no cancellation. The exact payload object
observed at entry must be deep-equal to the payload delivered onward.

### Hook priority

The governor does not register `before_model_resolve`. Its egress observer
must coexist with the intent router's fallback-notice filter. Tests should run
both priority orders with synthetic hooks and show that the governor observes
the final candidate without reintroducing a router-cancelled notice.

## Test matrix

| ID | Named test | Fixture / input | Expected decision and evidence |
|---|---|---|---|
| B-S01 | `schemas_accept_all_canonical_fixtures` | all 10 fixtures | Every object validates against exactly one intended schema set |
| B-S02 | `schemas_reject_unknown_and_missing_fields` | mutated fixtures | `additionalProperties` and required-field failures are reported |
| B-N01 | `normalizes_openclaw_hook_context` | synthetic Telegram human event | Stable event ID; sender, reply, session, run, and content hash map correctly |
| B-N02 | `normalization_is_deterministic` | same context twice | Byte-identical envelope except no uncontrolled clock fields |
| B-F01 | `retry_is_dropped_by_message_identity` | Fixture 1 | `DROP`, `DUPLICATE_MESSAGE_ID`; no model/classifier cost |
| B-F02 | `own_outbound_loopback_is_dropped` | Fixture 2 | `DROP`, `OWN_MESSAGE_LOOPBACK` |
| B-F03 | `unaddressed_sibling_is_dropped_for_current_agent` | Fixture 3 | `DROP`, `SIBLING_NOT_ADDRESSED` |
| B-F04 | `active_lease_blocks_parallel_public_owner` | Fixture 4 | non-holder gets `DROP`, `LEASE_HELD_BY_OTHER` |
| B-F05 | `visible_no_reply_is_structured_suppression` | Fixture 5 | egress `SUPPRESS`; no visible replacement text |
| B-F06 | `everyone_answer_override_allows_scoped_owners` | Fixture 6 | both decisions carry `HUMAN_OVERRIDE_BYPASS`; scope is one event |
| B-F07 | `closed_thread_ack_does_not_reopen` | Fixture 7 | `DROP`, `ACKNOWLEDGMENT_ONLY`; state remains `CLOSED` |
| B-F08 | `shadow_never_blocks_or_mutates` | Fixture 8 plus F01–F07 | hook returns pass/original payload while ledger records counterfactual result |
| B-F09 | `every_decision_records_governor_cost` | Fixture 9 | nonnegative `cpu_ms`; `model_calls=0`; `tokens_used=0` |
| B-F10 | `semantic_firewall_allows_only_nonsemantic_repair` | Fixture 10 | allowed transform is declared and no claim is added or altered |
| B-I01 | `same_message_produces_same_event_id` | repeated normalized input | deterministic `evt_` ID |
| B-I02 | `retry_lineage_does_not_create_second_public_slot` | retry plus completed lease | no second lease or outbound slot |
| B-L01 | `lease_acquire_is_atomic_in_process` | two concurrent claim attempts | exactly one holder and one `OWNER_LEASE_ACTIVE` result |
| B-L02 | `lease_expiry_uses_injected_clock` | expired lease | reassignment is deterministic and recorded |
| B-H01 | `stickiness_prevents_owner_thrashing` | rapid same-thread continuation | current owner retained within window |
| B-H02 | `explicit_readdress_breaks_stickiness` | explicit human mention | newly addressed owner wins |
| B-T01 | `closed_thread_requires_reopen_condition` | each lifecycle condition | only enumerated conditions transition to `REOPENED` |
| B-E01 | `ack_with_new_protocol_state_is_not_suppressed` | acknowledgment plus state/action | candidate preserved; prevents overbroad exact-text rules |
| B-E02 | `repair_cannot_add_or_change_claims` | adversarial repair result | firewall rejects result and returns original or suppresses per contract |
| B-P01 | `ledger_append_is_valid_jsonl_and_ordered` | three records | three parseable ordered records; mode and reason retained |
| B-P02 | `ledger_permissions_are_private` | temporary ledger directory | files are not group/world readable |
| B-P03 | `ledger_failure_fails_open_without_content_leak` | unwritable test sink | delivery proceeds; bounded error excludes prompt/output |
| B-C01 | `invalid_mode_defaults_to_shadow` | missing/invalid config | no enforcement possible |
| B-C02 | `semantic_dedup_cannot_activate_in_phase_b` | flag set true | configuration rejected or forced false |
| B-O01 | `governor_coexists_with_intent_router` | synthetic hook composition | no model override; no cancelled notice is reintroduced |

## Property and adversarial checks

1. For arbitrary messages in shadow mode, hook output equals hook input.
2. For any event identity, no more than one active lease with
   `public_slots = 1` exists.
3. A closed thread remains closed unless at least one enumerated reopen
   condition is present.
4. Reordering JSON object keys does not change deterministic IDs.
5. Exact text containing `NO_REPLY` as a substring is not suppressed unless
   it is a structured no-send or exact normalized control value.
6. A human override from a bot sender is ignored.
7. The governor never reports nonzero model calls in deterministic Phase B
   decisions.
8. No persisted record contains configured token, authorization, cookie, or
   credential-shaped fields.

## Smallest vertical slice

Commit 1 should include:

1. plugin and manifest scaffolding;
2. the six executable schemas;
3. deterministic ID and normalization code;
4. pure deterministic admission and egress decisions for Fixtures 1–5;
5. JSONL decision ledger;
6. `before_agent_run` and `reply_payload_sending` adapters locked to shadow;
7. schema, fixture, ledger, and hook-observation tests.

Acceptance:

- all canonical fixtures validate;
- Fixtures 1–5 produce the expected counterfactual decisions;
- no hook can block, cancel, or mutate;
- no model, embedding, network, or paid service is called;
- the ledger regenerates deterministically from fixtures except timestamps and
  measured CPU duration;
- focused tests and `git diff --check` pass.

Commit 2 may add override parsing, leases, thread lifecycle, hysteresis, and the
semantic firewall tests, still without active enforcement.

## Phase B completion gate

Phase B is complete when:

1. each of the six schemas exists as executable JSON Schema;
2. all ten canonical fixtures exist and have the named tests above;
3. every module in the proposed layout has one documented responsibility;
4. the shadow adapter tests prove zero behavior change;
5. the ledger is append-only, parseable, private, and contains governor cost;
6. known limitations are documented;
7. no runtime config is activated and no gateway restart is performed.

Passing Phase B authorizes Phase C replay-corpus construction, not active
suppression.

## Known limitations and deferred work

- `before_agent_run` can block but cannot redirect; ownership works by allowing
  the owner and suppressing non-owners only after active-mode approval.
- Outbound `runId` correlation is incomplete; use `sessionKey` plus event and
  lease IDs, and test same-session concurrency explicitly.
- Project/task scope inference is omitted when not supplied reliably.
- Crash-safe lease reconstruction is deferred.
- Templates, aggregation, private review, incidents, embeddings, semantic
  novelty, and adaptive budgets belong to later gated phases.
- The predeclared live thresholds remain: proceed toward activation only with
  sufficient measured waste, false silence below the accepted bound, favorable
  net savings, and explicit human approval.

