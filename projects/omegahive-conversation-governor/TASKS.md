# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [ ] **E1a narrow deterministic egress activation** — authorized by Ben on
  2026-08-12 in Telegram message 18264. Deliverable: activate only exact
  structured-silence (`NO_REPLY`, `NO_RESPONSE`) and the already-labeled
  attachment-promise watchdog-noise class at the common `message_sending`
  seam, while all admission decisions remain shadow-only. Acceptance: focused
  tests cover allowlisted cancellation, all other egress pass-through,
  shadow compatibility, fail-open exceptions, and truthful active ledger
  mode; an independent review has no unresolved blocker; one production
  suppression canary is durably correlated and a normal control message is
  delivered unchanged; exactly one gateway is active; rollback is recorded.
  Next command: implement and run the provider-free focused test suite.
  Evidence: `docs/narrow-activation-proposal-20260812.md` and
  `experiments/20260812T*-e1a-narrow-egress-activation/`.

- [x] **B8 watchdog-noise egress policy** — deliverable: classify attachment-
  promise watchdog diagnostics as `SUPPRESS` counterfactuals across raw
  watchdog and Telegram-rendered forms. Acceptance: focused governor tests
  pass and ordinary watchdog alerts remain `SEND`; enforcement remains
  shadow-only until the separately approved active-mode gate. Next command:
  run `npm test` in `plugins/conversation-governor`. Evidence: focused test
  output and `core.js` policy.
  Completed 2026-08-07: raw `WATCHDOG_ALERT` and Telegram-rendered forms map
  to `SUPPRESS/WATCHDOG_ATTACHMENT_NOISE`; unrelated watchdog alerts map to
  `SEND`; 9/9 focused tests pass. This remains shadow-only pending the active
  enforcement gate and completion of the direct-post delivery seam.

- [x] **B5 shadow observer completion** — shadow deployment approved by Ben
  2026-08-06 23:09 PDT (D-20260806-shadow-deployment-approved). Deliverable:
  load the already-installed, shadow-locked observer and capture one synthetic
  local ledger entry. Completed 2026-08-06 23:48 PDT after Ben's two controlled
  service restarts: plugin is loaded with conversation-hook access, its 8/8
  suite passes, and `evt_720384979a490ab6e4321` records shadow
  `ADMIT/DEFAULT_ALLOW` and `SEND/DEFAULT_SEND` in the private JSONL ledger.
  No model was invoked, no payload was sent, and no active-mode suppression is
  authorized. Evidence:
  `experiments/20260804T230000Z-b5-live-admission-enable/RUN.md`.
- [x] **B6 shadow-observation review checkpoint** — after ~24h of shadow
  telemetry, summarize the ledger's counterfactual recommendations and check
  they make sense (Ben's acceptance wording, D-20260806-shadow-deployment-approved).
  Deliverable: short review note in `docs/` + summary to Ben. Acceptance: every
  recommendation class in the ledger is either endorsed or flagged with a
  concrete false-positive/false-silence concern. Completed 2026-08-08: 200
  records reviewed (45 admission, 155 egress). One
  `DROP/DUPLICATE_MESSAGE_ID` was a concrete false positive caused by
  `message_id="unknown"`, while a 36-event identical spam burst was entirely
  admitted under changing synthetic channel IDs; all 155 egress records were
  `SEND/DEFAULT_SEND`. Active suppression remains unapproved. Evidence:
  `docs/shadow-observation-review-20260808.md`.
- [x] **B7 direct-post delivery seam audit** — scope extension
  D-20260806-direct-post-subagent-scope: determine whether cron `announce`
  deliveries and isolated agentTurn posts (e.g. `Channel watchdog scan` job
  70cd9d3f, the 2026-08-06 spam source) pass any instrumentable OpenClaw plugin
  hook. Deliverable: `docs/direct-post-seam-audit.md` naming the seam or its
  absence plus a minimal shadow observation design. Acceptance: a synthetic
  cron announce is recorded in the shadow ledger, or the audit documents why
  the hook surface cannot see it and proposes the smallest viable seam. This
  continuation also repairs immutable Telegram `message_id` and stable
  chat/session identity propagation before replay. Deployability acceptance:
  provider-free regressions prove unknown IDs cannot trigger duplicate drops,
  stable transport IDs group true retries correctly, and direct-post traffic
  has an identified shadow observation path; focused and relevant integration
  tests pass, with production enforcement still disabled. Next command:
  inspect the installed OpenClaw plugin hooks and cron/announce delivery call
  graph with `rg`. Evidence:
  `experiments/20260811T*-b7-seam-identity-deployability/` and
  `docs/direct-post-seam-audit.md`.
  Completed 2026-08-11: installed OpenClaw source proves cron announce uses
  `sendDurableMessageBatch` and the global `message_sending` hook. The staged
  governor moves egress observation to that common seam and ingress shadow
  capture to identity-bearing `message_received`; sentinel identities cannot
  recommend duplicate drops. Provider-free focused tests pass 12/12. The
  reviewed extension was subsequently installed and loaded under B9.

- [x] **B9 guarded shadow deployment and direct-post canary** — deliverable:
  independently review the B7 patch, install the exact reviewed shadow-only
  extension, restart through the owning supervisor, and send one bounded
  synthetic cron announcement to a dedicated test destination. Acceptance:
  exactly one gateway is active; the announcement has a `message_sending`
  ledger record and Telegram receipt; content is byte-equivalent; no payload
  is suppressed or mutated; rollback target is recorded. Next command:
  perform a separate frontier-model review of the B7 diff. Evidence:
  `experiments/20260811T232122Z-b7-seam-identity-deployability/` plus a new
  guarded-deployment run. Active enforcement is explicitly out of scope.
  Completed 2026-08-11 after Ben's controlled restart: exactly one gateway
  loaded the reviewed plugin; his inbound message `18226` was ledgered with
  immutable Telegram `messageId=18226`, `senderId=402314199`, and canonical
  session identity. The one-shot cron announcement
  `GOVERNOR_SHADOW_CRON_CANARY_20260811` was delivered exactly once and has
  exactly one `message_sending` egress ledger record
  (`rec_d798c0110a781c4e62a09`, `SEND/DEFAULT_SEND`, mode `shadow`) with
  byte-equivalent content. The temporary cron job was removed. No governor
  hook failure was logged and no suppression or mutation was enabled.

- [x] **OmegaBuzz feedback brief** — delivered: `docs/omegabuzz-feedback-brief-20260730.{tex,pdf}`; acceptance: summarizes shared strengths, prioritized implementation corrections, and immediate pre-build decisions; evidence: successful Tectonic compile, 2-page PDF visual inspection, SHA-256 `b68956cf6e2a18274e4b7e37e47e7c61a3b14b691bbe8305a162e32a58e424ea`, and Telegram attachment requested in message `15306`.
- [x] **Resident Learner minimal-governor design note** — delivered:
  `docs/resident-learner-minimal-governor.{tex,pdf}`; acceptance: the PDF
  synthesizes Cassio's wake-based foundation with the ProtoCosmoBot and
  ProtomegaBot critiques, specifies a minimal governor with explicit
  invariants, rollout gates, metrics, and open questions, and is attached in
  the originating Telegram discussion; evidence: the two files above,
  successful Tectonic compilation and PDF extraction check, and Telegram
  attachment message `15075`.
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
- [x] **B5 activate shadow observer** — deliverable: gateway loads the
  installed shadow-only plugin and begins bounded JSONL telemetry; acceptance:
  plugin is listed as loaded after restart, a synthetic local delivery records
  admission/egress decisions, and no payload is changed; completed 2026-08-06
  23:48 PDT. Evidence: plugin inspection, 8/8 focused tests, private ledger
  event `evt_720384979a490ab6e4321`, and
  `experiments/20260804T230000Z-b5-live-admission-enable/RUN.md`.

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
