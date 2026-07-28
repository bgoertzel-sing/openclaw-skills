# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [x] **A1 repository/runtime discovery** — deliverable: `docs/runtime-discovery.md`; acceptance: identifies the actual inbound dispatch, router, outbound-send, event-ID, and persistence seams without changing runtime behavior; evidence: `docs/runtime-discovery.md`.
- [ ] **A2 cross-reference discovery with OmegaClaw agent** — deliverable: confirm OmegaClaw's discovery run agrees on seam placement; acceptance: both discovery docs agree on whether the shared pre-inference boundary exists and where the governor plugin hooks land; evidence: OmegaClaw `current_event_flow.md`.
- [x] **B1 frozen event and ledger contract** — deliverable: `docs/event-ledger-contract.md`; acceptance: 6 JSON schemas (EventEnvelope, AdmissionDecision, ResponseLease, ThreadState, EgressCandidate, LedgerRecord) + 10 fixtures covering retry idempotency, own-message loopback, sibling not addressed, lease parallel-answer prevention, visible silence suppression, human override, closed-thread no-reopen, shadow observation-only, governor cost recording, and semantic firewall; evidence: `docs/event-ledger-contract.md`.
- [x] **B2 Phase B implementation plan and test matrix** — deliverable: concrete module layout mapped to repo paths + test matrix; acceptance: every Phase B fixture has a named test case and every module has a clear responsibility; evidence: `docs/implementation-plan.md`.
- [x] **B3 smallest shadow-only vertical slice** — deliverable: standalone
  `plugins/conversation-governor/` scaffold, deterministic decisions for the
  first fixture classes, JSONL audit, and hook adapters; acceptance: tests
  prove counterfactual decisions are recorded while inference and delivery are
  never blocked or mutated; evidence: initial executable slice at
  `plugins/conversation-governor/`; six Node tests pass.
- [x] **B4 canonical contract artifacts** — delivered: six executable JSON
  Schema artifacts, Fixtures 1–10, deterministic-ID checks, and fixture/schema
  validation. Acceptance: focused plugin suite passes 8/8; evidence:
  `plugins/conversation-governor/{schemas,fixtures,test}`. The remaining
  semantic policy cases (leases, lifecycle, override grammar, repair) remain
  independent Phase-B completion work and are not enforcement-ready.
- [ ] **B5 activate shadow observer** — deliverable: gateway loads the
  installed shadow-only plugin and begins bounded JSONL telemetry; acceptance:
  plugin is listed as loaded after restart, a synthetic local delivery records
  admission/egress decisions, and no payload is changed; blocker: system-scope
  `openclaw-agent.service` restart requires operator authority; evidence:
  plugin doctor/status and ledger sample.

## Next

- [ ] C1 build a minimized transcript-derived replay corpus with labeled noise/useful-response cases, including at least 48 hours of actual shadow ledger data; the prior design-only interval does not count as observation.
- [ ] D1 implement shadow admission and egress decisions; no suppression.
- [ ] E1 activate only deterministic no-op suppression after replay and canary gates pass and Ben approves activation.
- [ ] F1 add response leases/ownership behind an independent feature flag.
- [ ] G1 add the private review bus behind an independent feature flag.
- [ ] H1 migrate routine worker reports to state snapshots/digests.
- [ ] I1 add incident coalescing.
- [ ] J1 evaluate semantic deduplication in advisory/shadow mode.
- [ ] K1 expose metrics and tune policies from measured errors.

## Waiting or blocked

- [ ] Production activation of any suppression or shared topology — blocked on phase-specific replay/canary evidence and explicit approval — Ben — 2026-07-24.

## Someday or exploratory

- [ ] Generalize the validated two-agent protocol into typed multi-channel OmegaHive governance.

## Done recently

Move durable conclusions into `PROJECT.md`, `DECISIONS.md`, or experiment results rather than relying on this list.

- [x] Preserved the 53-page Revision 2 governing design with SHA-256
  provenance and extracted text; recorded it as the current specification
  while retaining Revision 1.
- [x] Created the project record, preserved the governing PDF with SHA-256 provenance, and recorded the staged implementation mandate.
