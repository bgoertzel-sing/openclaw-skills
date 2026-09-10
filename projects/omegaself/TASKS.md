# OmegaSelf — Tasks

## Phase 0: Setup (done)

- [x] Preserve OmegaSelf package in research library with provenance
- [x] Create project notebook
- [x] Copy coding-agent-pack into project repos for stable reference

## Phase 1: Smoke test and baseline

- [x] Run the unchanged smoke script through the canary venv (documented direct command is non-executable; global `python` alias is absent)
- [x] Record target commits, Python version, reasoner backend, truth-semantics status, and policy hash
- [x] Verify 44 Python unit tests and 21 JSON Schemas pass locally
- [x] Establish provider-free ProtoMegaBot2 canary behavior before integration (7 focused tests); full PeTTa boot remains unavailable without SWI-Prolog

## Phase 2: Record-only observation layer

- [x] Install `python/omegaself` 1.0.0 in the canary venv and import a fail-isolated `omegaself_bridge.py`
- [x] Add default-off record-only observations for cycle start, parsed calls, receipts, errors, policy loads, and reasoner invocations
- [x] Verify ledger on startup and expose root hash to logs; synthetic five-record ledger verified
- [x] Test on an isolated ProtoMegaBot2 canary branch (12/12 provider-free tests); native PeTTa loop test remains pending SWI-Prolog

## Phase 3: Evidence ledger and applicability

- [x] Implement bridge-level closure traversal, append-only correction/disqualification events, and dependence groups (`f5add4b`; 14/14 provider-free tests)
- [ ] Implement renewable SelfHereNow using at least one live causal-control binding
- [ ] Define exact context keys, context transfers, evidence-identity deduplication
- [ ] Add freshness profiles and append-only applicability assessments

## Phase 4: Reasoner SPI

- [ ] Introduce SelfReasoner; bind Patham9 through one adapter
- [ ] Add golden NAL tests plus provenance, dependence, calibration tests
- [ ] Shadow OmegaPLN before any governed backend migration

## Phase 5: Governance and policy gates

- [ ] Verify signed policy manifest through external trust root
- [ ] Convert parsed skill expressions into proposals; commit predictions before execution
- [ ] Enable capability-aware dispatch for low-impact read-only actions only
- [ ] Add exact-input continuity certificates; high-impact cache miss → RequireReview/Defer

## Phase 6: MeTTa self-model integration

- [ ] Integrate 15 MeTTa self-model files into OmegaClaw MeTTa workspace
- [ ] Test loop_hooks, tripwires, and governance relations
- [ ] Verify reasoner_seam connects to SelfReasoner SPI

## Phase 7: Canary deployment and validation

- [ ] Full ProtoMegaBot2 canary test with OmegaSelf integrated
- [ ] Validate against threat model and adversarial scenarios
- [ ] Notify Ben before any live ProtoMegaBot deployment
- [ ] Deploy to ProtoMegaBot with rollback plan
- [ ] Monitor for routing, continuation, or governance regressions

## Deferred successor: OMERA emotion regimes (after OmegaSelf)

- [ ] Begin OMERA only after OmegaSelf Phases 1–7 are implemented and the OmegaSelf–PeTTa Memory evidence/prediction/policy/receipt interfaces are stable.
  - Deliverable: schema-first OMERA implementation following the supplied phased plan, starting with record schemas, clocks, persistence, and deterministic replay; no behavioral deltas initially.
  - Acceptance test: OmegaSelf canary validation is green, OMERA Phase-0 fixtures round-trip and replay byte-identically, and record-only operation produces zero action-log differences from control.
  - Next command after the dependency gate clears: inventory the stabilized OmegaSelf and PeTTa Memory APIs against OMERA WP0.1–WP0.3 and create an isolated implementation worktree.
  - Evidence path: this project record plus a future `projects/omera/` notebook and its Phase-0 experiment record.
  - Source: Telegram messages 10378–10383, 2026-07-20 (`omegaself_emotion_regimes_extended` and `omera_implementation_plan`).

## Track D: OmegaSelf interface contracts

- [x] Specify versioned evidence-ledger, prediction, and policy-gate records with MeTTa-shaped canonical fixtures.
  - Deliverable: `contracts/` specifications, fixtures, and provider-free stub tests.
  - Acceptance test: all fixtures round-trip byte-identically; malformed fixtures fail with typed validation errors; every valid record carries schema identity/version, evidence closure, and causal/record/adoption clocks.
  - Verification: `python3 projects/omegaself/contracts/stub_tests.py` passes 2 test methods over 9 fixture subcases (6 byte-identical valid/edge round trips; 3 clean malformed rejections), 2026-07-20.
  - Evidence path: `projects/omegaself/contracts/` and `NOTES.md` Track D entry.
