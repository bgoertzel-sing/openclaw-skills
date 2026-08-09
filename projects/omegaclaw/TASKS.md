# Tasks

Use small, testable tasks. Keep the top of each section in priority order.

## Now

- [x] 2026-08-09: Independently verify the Capacity 1.1 candidate freeze and
  public replay. The verifier content-binds the candidate, digest record,
  public harness, complete v0.6 sandbox chain, and sealed commitment; all 22
  public cases, two tests including source-drift failure, and compilation
  pass. A09--A12 remain sealed. Next: obtain explicit held-out reveal/execution
  authorization from Ben; harness adoption remains closed. Evidence:
  `artifacts/ggb-capacity-gates/20260809-request-to-contract-candidate-freeze-independent-verification/`.

- [x] 2026-08-09: Strictly validate ThreadKeeper durable patch-proposal
  summaries at commit `e0d7568`. Queued results now cap proposals at 20 and
  require exact write/append actions plus safe relative workspace paths. All
  27 boundary tests and 54 subtests, compilation, `git diff --check`, and draft
  PR #1 safety-floor ancestry passed.

- [x] 2026-08-09: Keep ThreadKeeper bounded structured-return fallbacks
  queue-parseable at commit `c9bcef4`. Minimal adjudication returns now use
  `incomplete` when exact pending metadata cannot fit, and the final fallback
  uses a recognized durable status. Two focused tests, all 26 boundary tests
  and 49 subtests, compilation, `git diff --check`, and draft PR #1
  safety-floor ancestry passed.

- [ ] **2026-08-09: Bring live ProtoCosmo2 to Protomega's reviewed
  non-blocking transport/supervisor safety level.** Deliverable: ProtoCosmo2
  loads the schema-3 deferred long/document path, private prompt-file and strict
  rendering fixes under an identity-bound single-owner supervisor with
  cutover/start locks, exact child readiness, watchdog recognition, and a
  schema-compatible synchronous rollback. Acceptance: focused provider-free
  tests, compilation/shell/diff gates, isolated schema-2 migration and rollback
  rehearsal, independent frontier PASS, explicit guarded deployment approval,
  then fresh short and PDF-plus-interleaved-short production traces with one
  receiver and immutable routing. Rollback: stop only the owning supervisor,
  activate its secure synchronous marker, restart the same schema-3 runtime,
  and require preserved durable state plus one receiver. First guarded cutover
  safely entered synchronous rollback after the drained legacy owner removed
  its PID file and tripped the final drain gate. The inode/content/TOCTOU repair
  now has 11/11 focused and 90/90 full tests plus independent PASS. Next
  command: request a fresh cutover decision before enabling deferred jobs,
  then run the short and PDF-plus-interleaved-short canaries. Evidence:
`experiments/20260809T130200Z-protocosmo2-nonblocking-parity/`.

- [x] 2026-08-09: Implement and freeze the Capacity 1.1 zero-effect candidate
  without revealing A09--A12. All 22 public cases pass through the v0.6
  Bubblewrap facade; source SHA-256 is
  `df182ee8cafab2a7356352375916e06c2b1e39a60aae61378bb918fb39a27126`.
  Next: independent freeze/public replay verification before seeking explicit
  held-out reveal authorization. Evidence:
  `artifacts/ggb-capacity-gates/20260809-request-to-contract-candidate-freeze/`.

- [x] 2026-08-09: Validate exact ThreadKeeper durable adjudication returns at
  commit `71d9188`. `needs_adjudication` now requires the exact bounded pending
  metadata emitted by synchronous dispatch, and that metadata cannot accompany
  another status. Three focused tests, all 25 boundary tests and 49 subtests,
  compilation, `git diff --check`, and draft PR #1 safety-floor ancestry passed.

- [x] 2026-08-09: Validate exact ThreadKeeper durable structured-result shapes
  at commit `f6144b1`. Malformed scalar/list/proposal fields, non-boolean
  truncation markers, and inconsistent nonnegative token accounting now fail
  closed before terminal publication. Four focused tests, all 24 boundary
  tests and 45 subtests, compilation, `git diff --check`, and draft PR #1
  safety-floor ancestry passed.

- [x] 2026-08-09: Pass Capacity 1.1's combined R1/R2/R4 readiness and
  candidate-freeze review. The provider-free checker content-binds the 22
  public cases, sealed four-case commitment, and passing v0.6 R4/invocation
  consumer; two tests include source-drift failure. Next: implement a non-live
  candidate without revealing A09--A12, then freeze and verify its SHA-256.
  Evidence: `artifacts/ggb-capacity-gates/20260809-request-to-contract-combined-readiness-review/`.

- [x] 2026-08-09: Reject undeclared ThreadKeeper durable structured-result
  fields at commit `b48f968`. A worker result can no longer attach invented
  authority-bearing metadata such as `approved: true`; parsed JSON is limited
  to the synchronous dispatch return schema, while bounded non-JSON results
  retain their opaque compatibility path. Two focused tests, all 23 boundary
  tests and 40 subtests, compilation, `git diff --check`, and draft PR #1
  safety-floor ancestry passed.

- [x] 2026-08-08: Enforce ThreadKeeper durable queued-result size contracts at
  commit `24a35a6`. Queued worker returns above the task's exact `max_chars`
  bound, or non-string returns, now fail closed through durable failure
  retention instead of publishing an oversized terminal success. One focused
  regression, all 1,243 provider-free hardening tests and 40 subtests,
  compilation, `git diff --check`, and draft PR #1 safety-floor ancestry
  passed.

- [x] 2026-08-08/09: Independently content-bind and replay Capacity 1.1's v0.6
  Bubblewrap facade. All twelve R4 probes pass with E1--E6 coverage, including
  generic rejection of the prior stderr flood; exact binary success, fixed
  candidate rejection, source-drift rejection, four tests, and compilation
  pass. Next: review combined R1/R2/R4 readiness and the candidate-freeze
  procedure before any held-out reveal or harness adoption. Evidence:
  `artifacts/ggb-capacity-gates/20260809-request-to-contract-os-sandbox-v06-independent-replay/`.

- [x] 2026-08-08: Retain ThreadKeeper claimed-task integrity evidence until
  terminal commit at `51f2cf5`. The worker no longer deletes the enqueue
  checksum immediately after claim; abrupt interruption before `.done` or
  `.failed` publication leaves the claimed task authenticated. One focused
  regression, all 1,242 provider-free hardening tests and 40 subtests,
  compilation, `git diff --check`, and draft PR #1 ancestry passed.

- [x] 2026-08-08: Restrict ThreadKeeper durable queued-worker structured
  statuses at commit `58eba7e`. Structured results must include one of the
  exact synchronous-dispatch states (`ok`, `error`, `cancelled`,
  `needs_adjudication`, or `incomplete`); missing and invented authority states
  fail closed. Two focused tests, all 21 hardening tests and 40 subtests,
  compilation, `git diff --check`, and draft PR #1 safety-floor ancestry
  passed.

- [x] 2026-08-08: Revise Capacity 1.1's non-live Bubblewrap facade to bound
  captured stdout, stderr, and their aggregate before accepting a child report.
  The v0.6 producer rejects a caught stderr file-cap overflow and aggregate
  overflow with the exact generic failure while preserving binary success.
  Three provider-free tests and compilation pass. Next: independently content-
  bind and replay the twelve R4 probes plus public invocation seam. Evidence:
  `artifacts/ggb-capacity-gates/20260808-request-to-contract-os-sandbox-v06-stream-bounds/`.

- [x] **2026-08-08: Restore non-blocking Protomega long/document requests via
  isolated Protomega2 staging.** Deliverable: an addressed long/document
  request receives a bounded immediate acknowledgement, runs outside the
  Telegram polling loop with immutable source-chat routing, and later delivers
  a clean final result without blocking a second short DM/group request.
  Acceptance: provider-free concurrency/rollback/rendering tests pass; a live
  Protomega2 staging trace binds both the long-task acknowledgement/final reply
  and an interleaved short-message reply; an independent frontier review passes;
  then Protomega is deployed through its owning supervisor and a fresh external
  production trace passes with exactly one receiver. Rollback: restore the
  current runner and restart the prior supervisor target. Next command: inspect
  the existing Protomega2 launcher/state isolation and specify the smallest
  queue/worker change in `phase6_private_canary_runner.py`. 2026-08-08 21:41
  staging evidence: reply-to-PDF message 112 was durably acknowledged as 113;
  its deferred task failed before provider completion as receipt 114, while
  interleaved ping 115 completed as `PING-OK` receipt 116. Immediate repair
  obligation: replace the extracted-document `--prompt` argv handoff with a
  private bounded prompt file, preserve cleanup/fail-closed behavior, and
  autonomously replay a large-input worker regression before another external
  staging event. Acceptance evidence path remains:
  `experiments/20260808T232800Z-protomega-nonblocking-long-task/`.
  2026-08-09 00:01 staging closure: hardened R4 passed source 121, ack 122,
  interleaved `SHORT-R4-OK` receipt 124, and final PDF receipt 125; bounded raw
  durable-state/topology artifacts and hashes are now committed with the exact
  production restart/rollback boundary. Final independent PASS and guarded
  production restart/external acceptance remain open. 2026-08-09 05:38
  production update: independent review R6 passed; Ben authorized the guarded
  restart; one-owner/one-receiver restart passed with preserved cursor,
  processed IDs, and outbox projection hash `581be68a...b0f0`, healthy watchdog,
  free topology lock, and no rollback marker. Fresh private source 9746 received
  exact `PROD-OK` as receipt 9747, correlated to the same source/chat. Remaining
  acceptance closed 2026-08-09 05:53: production source 9753 received ack 9754;
  interleaved short source 9755 received exact `PROD-SHORT-OK` as 9756 while
  the deferred task was active; completed task
  `49e144e0166466e17b49a9ee3f3fbb7059866f186a7726b0cd65b16779e6d7b0`
  delivered its clean summary as 9757 replying to 9753. The short reply preceded
  the long result by 23 seconds. One receiver, healthy watchdog, free topology
  lock, no pending inbound, no wrapper leak, and no rollback activation.

- [x] 2026-08-08: Validate ThreadKeeper durable queued-worker result statuses
  at commit `f50e738`. Parsed structured returns can no longer persist a
  non-string, control-bearing, or overlong status as authority-bearing audit
  metadata; they fail the claimed task closed through normal failure retention.
  One focused regression plus all 20 hardening tests and 32 subtests passed,
  with compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] **2026-08-08: Audit reported Protomega DM and bot-philosophy outage** —
  deliverable: correlate the reported missing replies through Telegram ingress,
  responder/outbox, and delivery receipts without consuming updates through a
  diagnostic poll. Acceptance: identify both source-chat receipts, verify one
  outer owner/receiver, watchdog health, inactive maintenance, free topology
  lock, and zero Telegram backlog. Next command: inspect durable outer state,
  supervisor/watchdog status, and non-consuming `getWebhookInfo` metadata.
  Evidence: `experiments/20260808T152700Z-protomega-reported-dual-chat-outage/RUN.md`.
  Completed: bot-philosophy message 9723 delivered receipt 9726; private DM
  9724 delivered receipt 9727. Live owner 2343127 has one receiver, watchdog
  reports `OUTER_OWNER_RUNNING`, maintenance is inactive, the lock is free,
  and Telegram reports zero pending updates. Availability was healthy; the DM
  reply exposed a separate internal `(send ...)` rendering defect.

- [x] **2026-08-08: Make Protomega outer-mode recovery durable** — deliverable:
  make the watchdog recover the accepted outer production supervisor after an
  owner crash/reboot, retaining legacy only as an explicit rollback target.
  Acceptance: provider-free tests prove outer-owner healthy, outer-owner crash
  restart, no competing legacy receiver, lock/maintenance safety, and
  cursor/outbox preservation; a guarded live recovery trace verifies exactly
  one outer receiver after recovery. Next command: inspect
  `bin/omegaclaw-watchdog.sh`, the outer supervisor, and focused watchdog
  tests. Evidence path:
  `experiments/20260808T220100Z-protomega-outer-recovery/`.
  Completed: outer is now the sole automatic recovery target; legacy is an
  explicit rollback state. Parent-death binding, receiver drain-before-start,
  PID identity, lock closure, and failure-safe no-legacy-fallback are covered
  by 38 provider-free tests. A guarded live SIGKILL recovered in one watchdog
  invocation after 12 seconds to `legacy=0 outer=1`, preserving offset
  940522245, seven processed messages, seven delivered outbox items, and zero
  pending/undelivered items. The scheduled job now recognizes outer-mode
  statuses. An actual laptop reboot was not forced; the zero-owner startup path
  used by reboot is covered by staging and the live crash recovery.

- [x] 2026-08-08: Bound and sanitize ThreadKeeper durable queued-worker
  failure summaries at commit `412f556`. Primary worker exceptions and
  secondary audit-retention exceptions can no longer create arbitrarily large
  structured result records or expose absolute host paths. Two focused tests
  and all 1,220 provider-free hardening tests passed, with compilation,
  `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-08: Independently replay Capacity 1.1's codec-bound v0.5
  Bubblewrap facade. Eleven of twelve R4 probes pass, along with exact binary
  return, fixed candidate-rejection typing, and source-drift rejection. The
  output-flood probe exposes an unbounded success-path stderr capture and the
  gate fails closed as `revision_required_before_harness_adoption`. Four tests,
  replay JSON validation, compilation, and `git diff --check` pass. Next:
  bound both captured streams and their aggregate, then repeat independent
  replay. Evidence:
  `artifacts/ggb-capacity-gates/20260808-request-to-contract-os-sandbox-v05-independent-replay/`.

- [x] 2026-08-08: Bind durable ThreadKeeper queued-task identity at commit
  `8d593df`. A checksum-valid task whose declared `run_id` does not match its
  queue filename now fails closed before worker dispatch. One focused
  regression and all 1,238 provider-free hardening tests plus 28 subtests
  passed, with compilation, `git diff --check`, and draft PR #1 safety-floor
  ancestry.

- [x] 2026-08-08: Strictly validate durable ThreadKeeper queued tool subsets
  at commit `fbdd0f3`. Checksum-valid queued tasks can no longer defer
  duplicate, unknown, excluded, or aggregate-oversized tool-subset rejection
  until after worker claim. Five focused tests plus 19 subtests and all 1,264
  provider-free hardening tests plus 28 subtests passed, with compilation,
  `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-08: Bind Capacity 1.1's accepted child-result codec into a new
  non-live Bubblewrap facade. Four provider-free tests pass for exact binary
  bytes, fixed candidate rejection, generic other failures, and non-bytes
  returns; compilation passes. The initial replay caught and repaired an
  isolated-mode codec import defect. Verdict:
  `ready_for_independent_r4_and_invocation_seam_replay`. Evidence:
  `artifacts/ggb-capacity-gates/20260808-request-to-contract-os-sandbox-v05-codec-binding/`.
  No held-out reveal, harness adoption, ThreadKeeper PR #1 change, or runtime
  effect.

- [x] 2026-08-08: Require complete, consistent durable ThreadKeeper queued-task
  records at commit `cad5953`. Checksum-valid tasks can no longer omit
  runtime-authored fields and inherit claim-time defaults, or pair a queued
  goal with a different task-contract objective. Eighteen focused tests plus
  25 subtests and all 1,218 provider-free hardening tests passed, with
  compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-08: Reject out-of-range durable ThreadKeeper worker limits at
  commit `c6d334f`. Queued tasks now require exact integer `max_turns` and
  `max_chars` values inside their configured hard bounds instead of silently
  changing persisted task meaning at claim time. Sixteen focused tests plus
  15 subtests and all 1,218 provider-free hardening tests passed, with
  compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] **Add a bounded watchdog maintenance/cutover lease before the next
  Protomega transport attempt (Ben, 2026-08-08).** Deliverable: make the host
  watchdog suppress legacy-supervisor restart only under an explicit,
  short-lived lease; reject malformed, symlinked, overlong, or over-duration
  leases; and verify actual legacy/outer receiver process trees. Acceptance:
  provider-free tests cover lease enter/status/expiry/clear, invalid lease
  fail-closed behavior, active legacy ownership, and active outer ownership;
  production remains on exactly one legacy receiver throughout staging.
  Next command: implement the lease and ownership checks in
  `bin/omegaclaw-watchdog.sh` with temporary-path test seams. Evidence:
  `experiments/20260808T122000Z-protomega-watchdog-maintenance-mode/`.
  Progress: 11 provider-free tests pass and the demonstrated
  owner-vs-child-readiness race is fixed. Anthropic review run
  `e6c99486-f194-4e53-8913-252f06ec6e19` returned a partial BLOCK before its
  explicit provider timeout; OpenAI review run
  `27c2280f-773a-4175-9df3-8d9d1edb4be0` completed with a structured BLOCK.
  Revision 7 closes the shared lock, both-owner PID/start/cmdline identity,
  safe temp publication, concurrency/stop, and fail-closed rollback gates.
  The focused suite passes 35 tests. Fresh GPT-5.6 Sol re-review session
  `agent:main:explicit:protomega-cutover-review-r5-20260808` returned PASS with
  no blockers. Production remains one bound legacy receiver. Next command:
  after Ben explicitly authorizes exactly one guarded attempt, rerun preflight
  and execute `local/protomega-cutover.sh cutover`; immediately invoke its
  rollback command on any topology or end-to-end acceptance failure.
  Attempt 17677 reached outer-only topology but was rolled back before canary
  because the owner inherited the topology-lock fd. Both launchers now close
  fd 9; 37 tests pass; restored state is `legacy=1 outer=0`, maintenance
  inactive, watchdog healthy, and lock free. Authorization consumed. Next:
  fresh review, then a new explicit one-attempt authorization.
  R7 GPT-5.6 Sol review returned PASS with no blockers after independently
  replaying both behavioral fd tests and the 37-test gate. Awaiting Ben's new
  explicit authorization for exactly one guarded attempt.
  Ben authorized attempt 17686; outer-only topology is now healthy at PID
  2254194, watchdog recognizes it, maintenance is inactive, and the lock is
  free. Awaiting Ben's fresh `PROTOMEGA-CANARY-17686-20260808` message to
  `@Protomegabot` for correlated ingress/provider/outbox/Telegram acceptance.
  Canary 9708 failed at the responder before provider invocation; durable
  visible failure receipt 9709 was delivered. Immediate rollback restored
  legacy PID 2256514 with one worker. Next: preserve bounded inner-driver
  stderr/error classification, reproduce the pre-provider failure in isolated
  staging, repair it, and repeat review before seeking new authorization.
  Isolated replay now identifies and repairs the missing file-bridge provider,
  wrong agent/model routing, and legacy history/reparse seam. The exact canary
  completes through agent `protomegabot-opus` on Anthropic Claude Opus 4.6;
  52 focused tests, compilation, shell syntax, diff checks, and history-isolation
  hashes pass. Production remains `legacy=1 outer=0` with a free cutover lock.
  Next: fresh independent review, then request exactly one new guarded attempt.
  Evidence:
  `experiments/20260808T203000Z-protomega-responder-failure-repro/`.
  R8 review run `d2aebc5a-3f0b-4b38-997c-7e719b79176f` BLOCKed on
  incident-file hardening, raw-stderr privacy, and actual route validation.
  All three are repaired with behavioral tests; the focused gate now passes
  56 tests and the exact isolated canary replay again exits 0. Next: R9
  independent review before any authorization request.
  R9 run `2d1e8e11-bcbe-4ece-86c5-2f183043360a` independently replayed the
  remediation and returned PASS with no blockers. Awaiting Ben's explicit
  authorization for exactly one guarded cutover/canary attempt.
  Ben explicitly authorized exactly one guarded attempt in Telegram message
  17702. Acceptance: outer-only healthy topology followed by one fresh
  Ben-authored nonce trace through ingress, verified provider/model, durable
  outbox, and Telegram receipt; any failure immediately restores legacy-only.
  Cutover completed: `legacy=0 outer=1`, outer owner PID 2312624 with exactly
  one child, watchdog reports the owner, maintenance is inactive, and three
  consecutive lock probes are free. Awaiting fresh canary nonce
  `PROTOMEGA-CANARY-17702-20260808` directly to `@Protomegabot`.
  Acceptance passed. Ben's Telegram message 9714 was processed; state advanced
  to update offset 940522238 (binding accepted update 940522237), provider run
  `337869bb-c063-48a2-8dc6-61fd59f123fc` used verified Anthropic
  `claude-opus-4-6`, durable outbox item
  `1d6ebdeed9eacb77e535ae3a092caab04c3ed093b3aa899c828fdb9e5d82ef4a`
  was delivered as Telegram receipt 9715, and Ben's screenshot confirms the
  exact nonce reply. Final topology remains `legacy=0 outer=1`, watchdog
  healthy, maintenance inactive, and lock free.

- [ ] **Repair foundation-model routing and empty-review observability (Ben,
  2026-08-08).** Deliverable: distinguish model selection/unavailability,
  provider invocation, and result-capture failures; remove stale/unavailable
  primary routing where justified; and retain bounded error/empty-result
  telemetry. Acceptance: provider-free routing tests plus isolated live probes
  of configured foundation routes produce non-empty correlated results or
  explicit provider errors, without changing Protomega transport. Next command:
  capture non-secret effective model config, provider/auth presence, recent
  fallback events, and the two empty-review invocation records. Evidence:
  `experiments/20260808T120000Z-foundation-model-routing-repair/`.

- [x] 2026-08-08: Independently review Capacity 1.1's standalone child-result
  codec v0.3. A content-bound replay covers empty/binary exact bytes, exact
  bounds, canonical JSON/base64, fixed rejection privacy, generic failures,
  and source/contract drift. One direct check and six provider-free tests pass.
  Verdict: `codec_accepted_for_sandbox_facade_revision`; held-outs, harness,
  ThreadKeeper PR #1, and runtime remain closed. Evidence:
  `artifacts/ggb-capacity-gates/20260808-request-to-contract-result-codec-v03-independent-review/`.

- [x] 2026-08-08: Bound ThreadKeeper queued-worker identifiers at commit
  `01e44b8`. Durable queued tasks now reject persona and tool identifiers over
  64 characters before lookup, joining, or diagnostic use; direct persona
  lookup uses the same bounded grammar. Three focused regressions, all 1,218
  provider-free hardening tests, 15 boundary tests plus 11 subtests,
  compilation, `git diff --check`, and draft PR #1 safety-floor ancestry
  passed.

- [x] 2026-08-08: Validate bounded ThreadKeeper candidate run-status
  identifiers at commit `05de483`. Candidate review now rejects
  integrity-valid transcript statuses containing controls or exceeding the
  64-character lowercase identifier grammar before returning them to an
  operator. Twenty focused and all 1,231 provider-free hardening tests plus 9
  subtests passed, with compilation, `git diff --check`, and draft PR #1
  safety-floor ancestry.

- [x] 2026-08-08: Implement Capacity 1.1's accepted child-result v0.3 protocol
  as a standalone reference codec. Five provider-free tests cover exact bytes,
  bounds, rejection typing, and generic malformed/non-bytes/exception failure.
  Verdict: `ready_for_independent_codec_review`. Evidence:
  `artifacts/ggb-capacity-gates/20260808-request-to-contract-result-codec-v03/`.

- [x] 2026-08-08: Reject silently truncated ThreadKeeper patch proposals at
  commit `79613f7`. Proposal-only write/append content above the configured
  cap now fails the complete tool batch closed before recording anything, so
  an operator never reviews a semantically different truncated patch.
  Seventeen focused and all 1,216 provider-free hardening tests passed, with
  compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

- [ ] **Independent production review of the standalone Protomega Bot-API
  long-poller (Ben, 2026-08-07).** Deliverable: a PASS/BLOCK verdict limited
  to concrete blockers across ingress, receiver ownership, routing,
  credential scrubbing, crash recovery, isolation, and side effects.
  Acceptance: inspect implementation and launch topology, rerun narrow tests,
  and retain an evidence-backed review record. Next command: inspect the
  parameterized adapter, runner, supervisor, and recovery tests. Evidence: a
  new dated experiment review record.
  Emergency exception: Ben explicitly approved a one-production-canary waiver
  in Telegram message 17588 on 2026-08-07 after two review calls returned empty
  results. The waiver covers only independent review and expires on this one
  canary; failure requires immediate restoration of the preceding supervisor.
  Evidence: `experiments/20260808T060200Z-protomega-outer-transport-cutover/`.
  Result: the new child failed before Telegram polling because the runner did
  not accept the existing env file's shell `export KEY=value` syntax. It was
  stopped immediately and the old supervisor restored with one worker and no
  bridge. The parser is now repaired and its focused suite passes 5/5, but the
  one-attempt waiver is consumed. Next command: after renewed authorization,
  repeat the guarded stop/start topology gate and request one fresh canary.
  Renewal: Ben authorized exactly one second guarded attempt in Telegram
  message 17603 on 2026-08-08; the same immediate-rollback condition applies.
  Second-attempt result: the repaired runner started, but the host watchdog
  restarted the old supervisor and created two receivers before any canary.
  The outer receiver was stopped and the old single receiver retained. The
  renewed waiver is consumed. Next: add a bounded watchdog maintenance/cutover
  mode and process-tree stop verification, then seek authorization for a new
  guarded attempt.

- [x] 2026-08-07: Require safe bounded ThreadKeeper tool-name identifiers at
  commit `d3f3cbc`. Parsed names containing controls/invisible Unicode or more
  than 64 characters now fail the entire batch before registry access or
  diagnostic interpolation. Two focused tests and all 1,229 provider-free
  hardening tests plus 9 subtests passed, with compilation, `git diff --check`,
  and draft PR #1 safety-floor ancestry.

- [ ] **Transplant ProtoCosmo2's durable outer Telegram transport into
  Protomega while retaining Protomega's prompt and memories (Ben,
  2026-08-07).** Deliverable: an identity-parameterized, isolated Protomega
  runner using durable inbox/outbox/cursor/crash-recovery semantics and bounded
  per-request OmegaClaw invocation, with no ProtoCosmo2 persona or mutable
  state copied. Acceptance: provider-free gates, isolated staging repeated
  idle/restart trials, independent concurrency/identity review, then one fresh
  human-authored production request correlated through ingress, provider,
  outbox, Telegram receipt, and observed reply with exactly one receiver.
  Next command: parameterize the ProtoCosmo2 contract/transport identity and
  create a Protomega-specific runner with disjoint state/config/PID/log paths.
  Evidence: `docs/protomega-protocosmo2-transport-transplant-spec.md` and a new
  dated experiment record. Rollback: production commit `f4d7a0b`, archived
  pre-cutover state, and the existing owning supervisor.

- [x] 2026-08-08: Independently review Capacity 1.1's bounded child-result
  contract v0.3. The revised 49,125-byte decoded maximum is exact and maximal:
  its canonical report is 65,534 bytes, while the next payload produces 65,538
  bytes above the 65,536-byte cap. One direct check and four tests pass.
  Verdict: `contract_accepted_for_implementation`; this grants no implementation,
  held-out reveal, harness adoption, sandbox, ThreadKeeper PR #1, or runtime
  authority. Evidence:
  `artifacts/ggb-capacity-gates/20260808-request-to-contract-result-tag-contract-v03-independent-review/`.

- [x] 2026-08-07: Make ThreadKeeper's structured-return size bound total at
  commit `b97515e`. The final shrink path previously retained fixed audit
  metadata, so sufficiently large queue/transcript fields could still exceed
  a caller's `max_chars` cap. It now emits minimal valid JSON with an explicit
  truncation marker when the full schema cannot fit. One focused and all 12
  boundary-hardening tests plus 6 subtests passed, with compilation and `git
  diff --check`.

- [x] 2026-08-07: Bound complete ThreadKeeper worker tool batches at commit
  `ebf8eb1`. Effect quotas intentionally exclude the final structured `emit`,
  but that left malformed provider output able to supply an arbitrarily large
  emit-only batch for preflight. The complete parsed batch is now capped at
  the per-turn effect limit plus one final-return slot before iteration or
  registry access. One focused and all 1,227 provider-free hardening tests plus
  6 subtests passed, with compilation, `git diff --check`, and draft PR #1
  safety-floor ancestry.

- [x] 2026-08-07: Revise Capacity 1.1's bounded child-result contract as v0.3.
  Lowered the decoded maximum from the inconsistent 49,152 bytes to the exact
  maximal representable 49,125 bytes. The checker proves that its canonical
  report is 65,534 bytes and the next payload produces 65,538 bytes above the
  65,536-byte cap. One direct check and seven tests pass. Verdict:
  `ready_for_independent_contract_review`; implementation, held-out reveal,
  sandbox changes, ThreadKeeper PR #1 changes, and runtime remain closed.
  Evidence: `artifacts/ggb-capacity-gates/20260807-request-to-contract-result-tag-contract-v03/`.

- [x] 2026-08-07: Require complete ThreadKeeper candidate patch proposals at
  commit `ba70005`. Runtime always persists proposal `content`, but candidate
  review previously accepted a checksum-valid record with that field omitted.
  Eight focused and all 1,216 provider-free hardening tests passed, with
  compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-07: Bound ThreadKeeper candidate-review content at commit
  `5b3c62d`. Integrity-verified review records can no longer exceed the
  runtime's configured patch-proposal content cap or present empty/oversized
  adjudication summaries to an operator. Fifty-seven focused and all 1,215
  provider-free hardening tests passed, with compilation, `git diff --check`,
  and draft PR #1 safety-floor ancestry.

- [ ] **Remove stale ProtoCosmo2 shadow-only production prompt and prove live
  Telegram behavior (Ben, 2026-08-07).** Screenshot evidence showed the live
  Telegram receiver answering that it was a Phase-5 shadow evaluation and
  could not send PDFs. Root cause: the launcher resolves the OmegaClaw library
  from the Phase-2 PeTTa checkout, not the Phase-6 worktree; the first repair
  edited the inert worktree prompt and a post-restart screenshot disproved it.
  Replaced the actual nested runtime prompt at local commit `a2cfde8` with the
  live supervised Telegram contract. Thirty-six focused provider-free tests,
  compilation, and shell syntax pass. Restarted with exactly one receiver;
  durable state SHA-256 remained
  `237e3245cb3a2c747fa8791838d55e6a4c02dd3885f0ca98c9c34f422c722fe7`.
  Acceptance remains open pending one fresh human-authored post-restart request
  with correlated ingress, provider result, and Telegram receipt. Rollback:
  restore worktree commit `d7f8e5d329b603a8c73104ca954bf3c2f5415b8f`'s prompt and restart the owning
  supervisor.

- [ ] **Restore live `@Protomegabot` request processing (Ben, 2026-08-07).**
  Observed production supervisor/receiver topology is live and polls Telegram,
  and it enqueued Ben-authored updates `940522120`/message `9643` and
  `940522126`/message `9646` in chat `-5437945421`, but no correlated provider
  completion/action or Telegram delivery follows.  Deliverable: isolate the
  queue-to-loop/provider handoff failure in staging, preserve a provider-free
  regression, then make the smallest reversible production repair. Acceptance:
  a fresh human-authored Telegram request has correlated ingress, provider or
  visible bounded failure, and a reply receipt in its originating chat, with
  exactly one production receiver and a recorded rollback target. Next command:
  capture production queue/cursor and recent loop trace, then reproduce the
  enqueue-without-dispatch transition in the isolated staging runtime. Evidence:
  `artifacts/telegram-private-supervisor/omegaclaw-telegram-private.log` and a
  new dated experiment record.
  Correction: `84946ce` fixes a real latent continuation bug but did not fully
  explain this incident; a clean restart initialized that state false and still
  starved dequeue. The experimental synchronous poller has now been removed at
  `f4d7a0b`, the 8.65 MB polluted history is preserved under `archive/`, the
  clean tracked history is active, and production has one threaded Bot-API
  worker with no MTProto bridge. Thirty-four focused test bodies passed;
  Docker-dependent teardown alone errored because Docker is absent. Acceptance
  remains open pending a fresh human-authored message and correlated reply.
  Evidence: `experiments/20260807T225500Z-protomega-clean-poller-recovery/`.
  A later private canary conclusively failed upstream of the queue: manual
  transport-only egress receipt `9670` reached Ben, Ben replied directly, but
  the sole threaded receiver recorded no poll result, enqueue, provider call,
  delivery, or poll error. This repair lane is superseded by the durable outer
  transport transplant task above; it is not accepted as fixed.

- [x] 2026-08-07: Independently review Capacity 1.1's revised bounded
  child-result contract v0.2. The prior ambiguity is resolved, but its byte
  bounds conflict: a permitted 49,152-byte output produces a 65,570-byte exact
  report above the 65,536-byte cap; 49,125 bytes is the largest representable
  output. One direct check and three tests pass. Verdict:
  `revision_required_before_implementation`. Evidence:
  `artifacts/ggb-capacity-gates/20260807-request-to-contract-result-tag-contract-v02-independent-review/`.
  Next: lower the decoded maximum to 49,125 (preferred) or revise the report
  cap, then repeat independent review; sandbox and runtime remain closed.

- [x] 2026-08-07: Require complete pending ThreadKeeper adjudication metadata
  at commit `a2c4a0c`. Runtime always persists four fields for an unresolved
  candidate, but review previously accepted partial checksum-valid metadata.
  Review now requires exact `required`, `status`, `candidate_summary`, and
  `candidate_turn` fields before creating an operator gate. Fifty-four focused
  and all 1,212 provider-free hardening tests passed, with compilation, `git
  diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-07: Bind ThreadKeeper candidate patch proposals to contract
  path/action scope at commit `43c0610`. Candidate review now applies the same
  `allowed_paths` and `forbidden_actions` checks as runtime proposal capture,
  preventing a checksum-valid out-of-scope proposal from reaching an
  operator-facing gate. Fifty focused and all 1,208 provider-free hardening
  tests passed, with compilation, `git diff --check`, and draft PR #1
  safety-floor ancestry.

- [ ] **Agent-hive plumbing execution directive (Ben, 2026-08-07).** Prioritize
  live operational acceptance over discretionary research work: (1) restore
  `@Protomegabot` Telegram and Slack messaging; (2) prove autonomous native
  Telegram PDF/approved-attachment delivery by `@Protomegabot`; (3) complete
  `@Protocosmo2bot` text and attachment operation; (4) coordinate the staged
  conversation-governor rollout; and (5) enable bounded persistent-subagent
  launch and management for both identities. Acceptance: each item has a fresh,
  correlated external-channel trace (or, for governor, its specified shadow /
  canary evidence), no manual transport substitution, and a documented rollback
  state. Keep ASI:Cloud migration/GPU work deferred; it needs a separate
  approved plan. Next command: resolve the highest unclosed acceptance gate in
  this order, beginning with Protomega ingress and Slack evidence. Evidence:
  linked experiment records and `catalog/KANBAN.md`.

- [x] 2026-08-07: Prove `@Protocosmo2bot` can post PDF and other approved files
  in the Protobots Staging Telegram group (`-5543435724`). Deliverable: run a
  live upload through ProtoCosmo2's production `Api.send_document` adapter,
  preserve a redacted receipt and artifact hash, then restore the supervised
  receiver. Acceptance: Telegram returns a valid message receipt visible in
  the target group, focused outbound-document tests pass, and the supervisor
  reports active after restart. Next command: create the experiment record and
  invoke the adapter with a workspace-confined test PDF. Evidence path:
  `experiments/20260807T153918Z-protocosmo2-staging-file-egress-r2/`. Live PDF
  receipt `633` and LaTeX-source receipt `634` are visible in the group; 35
  focused tests and compilation passed; supervisor is active with one runner.

- [x] 2026-08-07: Revise Capacity 1.1's bounded child-result protocol as
  contract-only v0.2. Exact ASCII JSON serialization, strict canonical RFC
  4648 base64 with a 49,152-byte decoded cap, and generic failure for non-bytes
  returns resolve the three independent-review blockers. One direct check and
  six tests pass. Evidence:
  `artifacts/ggb-capacity-gates/20260807-request-to-contract-result-tag-contract-v02/`.
  Next: independent content-bound review only; do not change the sandbox,
  reveal held-outs, adopt the harness, or alter runtime behavior.

- [x] 2026-08-07: Validate the complete ThreadKeeper task contract behind
  candidate-review gates at commit `370282d`. Review previously consumed only
  the proposal/adjudication booleans, so checksum-valid records with an empty
  objective, escaping path scope, or oversized quota could still appear
  operator-reviewable. Authority-bearing records now reuse the runtime's full
  contract validator; failed runs without candidates remain reviewable.
  Forty-eight focused and all 1,206 provider-free hardening tests passed, with
  compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-07: Bind ThreadKeeper patch-proposal review to its authorizing
  task contract at commit `35b21d9`. A checksum-valid transcript could
  previously present patch proposals to the parent/operator without enabling
  `patch_proposal_only`; review now requires that flag to be exact boolean true
  whenever proposals exist. A failed run retaining only the flag remains
  review-unneeded. Forty-five focused and all 1,213 provider-free hardening
  tests plus 6 subtests passed, with compilation, `git diff --check`, and draft
  PR #1 safety-floor ancestry.

- [x] 2026-08-07: Independently review Capacity 1.1's bounded child-result
  protocol. The content-bound review preserves the narrow `ValueError` source
  and generic failure channel but stops implementation because JSON
  canonicalization, base64 canonicality/decoded size, and non-bytes return
  handling are under-specified. One direct check and five tests pass. Verdict:
  `revision_required_before_implementation`. Evidence:
  `artifacts/ggb-capacity-gates/20260807-request-to-contract-result-tag-contract-independent-review/`.
  Next: freeze those three details in a contract-only v0.2 revision and repeat
  independent review; do not modify the sandbox or runtime.

- [x] 2026-08-07: Require consistent unresolved ThreadKeeper adjudication
  state at commit `be12522`. Checksum-valid candidate records can no longer
  create an adjudication gate from `adjudication_required` status alone, pair
  pending metadata with a non-candidate run, or omit the task-contract review
  requirement. Failed runs that merely retain `requires_adjudication: true`
  no longer appear to contain a candidate. Forty-two focused and all 1,209
  provider-free hardening tests plus 6 subtests passed, with compilation,
  `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-07: Require exact unresolved ThreadKeeper adjudication state at
  commit `fcae412`. An integrity-verified candidate transcript could previously
  set `adjudication.status` to an arbitrary string such as `approved`, which
  candidate review echoed to the parent/operator. Non-empty adjudication
  metadata must now contain exact `required: true` and `status: pending`, while
  missing/false requirements and forged dispositions fail closed. Thirty-seven
  focused and all 1,195 provider-free hardening tests passed, with compilation,
  `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-07: Freeze Capacity 1.1's bounded child-result tag contract
  before revising the accepted v0.4 sandbox. Exact `ok` and `rejected_input`
  reports preserve bytes-or-`ValueError` semantics without exposing candidate
  messages/tracebacks; every other failure remains generic `RuntimeError`.
  One direct check and seven tests pass. Evidence:
  `artifacts/ggb-capacity-gates/20260807-request-to-contract-result-tag-contract/`.
  Next: independent contract review, then implementation/content binding and
  fresh R4, invocation-seam, and A07/N01--N10 replay. No candidate freeze,
  held-out reveal, harness adoption, or runtime effect is authorized.

- [ ] 2026-08-07: Repair Protomega's nonresponse to the exact group input
  `.@Protomegabot can u try to post a pdf here as a test?`. Deliverable: trace
  the message through MTProto ingress, mention/address filtering, queueing, and
  action delivery; preserve the failing form as a provider-free regression and
  make the smallest bounded fix. Acceptance: the regression and focused
  Telegram tests pass, the supervised runtime restarts healthy, and a fresh
  addressed group smoke produces a reply or PDF action. Next command: inspect
  the MTProto bridge log/state and run the existing address-filter tests.
  Evidence path: `experiments/20260807T073436Z-protomega-dot-mention-nonresponse/`.
  The synchronous-polling provisional repair was reverted: while idle,
  `getLastMessage()` was not reached, so it could not acquire the next update.
  The preceding threaded Bot-API receiver is now active with native PDF egress
  retained. The exact dotted request plus routing envelope and document actions
  pass 26 focused provider-free tests; one worker, zero bridges, and `Polling
  started` are observed after restart. Evidence:
  `experiments/20260807T125032Z-protomega-threaded-polling-rollback-r1/`.
  Still open: one fresh human-authored end-to-end PDF request after this final
  restart.

- [x] 2026-08-07: Restore reviewability of legitimate ThreadKeeper
  adjudication transcripts at commit `a775f6b`. The exact-schema change had
  rejected runtime-generated `adjudication.candidate_turn`; candidate review
  now admits it only as an exact integer from 1 through the dispatch turn hard
  cap. An end-to-end regression covers dispatch, checksum persistence, and
  review, while boolean, zero, and oversized values fail closed. Thirty-five
  focused and all 1,192 provider-free hardening tests passed, with compilation,
  `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-06: Give ProtoCosmo2 and Protomega an auditable persistent-
  subagent lifecycle adapter. Deliverable: expose durable create/status/
  checkpoint/control/standing-authority operations from each OmegaClaw runtime,
  with immutable manifests, hash-chained events, strict state-root handling,
  and provider-free regressions. Acceptance: both runtime branches load the
  exact skills; creation/status/control tests pass; no worker/provider process
  is started by installation. Completed: ProtoCosmo2 already contained the
  reviewed adapter at `5c64918`; Protomega branch
  `agent/protomega-persistent-worker-adapter` carries it at `eb41200`
  (shared documentation `768c3d1`) and its live runtime received the same
  commits as `e88908a` and `20a2e35`. Both focused suites pass 26/26 and Python
  compilation passes. The ProtoCosmo2 capability policy now correctly records
  the state-only boundary; the restarted Protomega Telegram supervisor reports
  one healthy Bot-API worker. A separately reviewed executor and explicit
  provider/cost authorization remain required before a task can run.

- [x] 2026-08-06: Reject undeclared ThreadKeeper candidate escalation fields
  at commit `d6f6ac3`. Candidate review now requires exact nested schemas for
  `task_contract` and `adjudication`, so a checksum-valid transcript cannot
  attach misleading metadata such as `approved: true` to either escalation
  source. Thirty-one focused and all 1,189 provider-free hardening tests
  passed, with compilation, `git diff --check`, and draft PR #1 safety-floor
  ancestry.

- [x] 2026-08-06: Repair Protomega Telegram PDF/LaTeX egress. Deliverable:
  add a native, bounded `send-document` OmegaClaw action instead of relying on
  OpenClaw's in-band `MEDIA:` reply convention. Acceptance: raw-action and
  transport regressions pass; the live runner is restarted; an existing PDF is
  delivered to the Protobots group as a Telegram document. Completed: commit
  `d914aaf`; six focused attachment/action tests and Python compilation pass;
  supervisor restarted as PID `1605626`; live Telegram `sendDocument` returned
  receipt `9471` for the revised Plain2MeTTa PDF. Five unrelated pre-existing
  text-send tests still fail against this branch's older text-send semantics.

- [x] 2026-08-06: Content-bind and empirically review Capacity 1.1's public
  invocation seam against the accepted v0.4 sandbox. A real Bubblewrap call
  returns clean exact bytes, but candidate `ValueError` is collapsed to generic
  `RuntimeError`, contradicting A07/N01--N10. Three provider-free tests pass,
  including source-drift rejection. Verdict:
  `revision_required_before_harness_adoption`. Evidence:
  `artifacts/ggb-capacity-gates/20260807-request-to-contract-invocation-seam-review/`.
  Next: freeze a bounded input-rejection result tag, revise/content-bind the
  facade, and independently replay R4 and the seam before candidate freeze or
  held-out reveal.

- [x] 2026-08-06: Reject undeclared ThreadKeeper candidate patch-proposal
  metadata at commit `ba571bc`. The integrity-checked review boundary now
  requires each proposal to contain only `action`, `path`, and optional
  `content`; forged operator-facing fields such as `approved` fail closed.
  Six focused cases and all 1,197 provider-free hardening tests plus 6 subtests
  passed, with compilation, `git diff --check`, and draft PR #1 safety-floor
  ancestry.

- [x] 2026-08-06: Enable `@Protocosmo2bot` to post PDF and LaTeX Telegram
  attachments, and verify Protomega's shared gateway path. Deliverable: a
  durable, bounded outbound-document outbox record and Bot API `sendDocument`
  delivery for an explicit `MEDIA:/absolute/path` directive; PDFs and LaTeX
  sources only, workspace-confined, with safe size/caption limits. Acceptance:
  provider-free tests prove a PDF is sent as a document and an outside-workspace
  path fails visibly; focused suite, compilation, and supervised runner restart
  pass. Completed: core commit `6fd5e7e`, runner commit `9bd6608`; 35 focused
  tests pass and the runner restarted as PID `1558974`. The OpenClaw gateway
  already has `sendDocument` support, so no gateway code modification was
  required for Protomega.

- [x] 2026-08-06: Remove ProtoCosmo2's premature 60,000-character PDF
  truncation. Deliverable: admit the complete extracted text of the supplied
  104-page OmegaSelf PDF while retaining a documented bounded-input safety
  limit and explicit failure above it. Acceptance: a provider-free regression
  proves 160,374 extracted characters survive unchanged; focused Telegram
  tests, compilation, live config validation, and worker restart pass. Next
  Completed: the supplied PDF extracts to 160,374 characters and is preserved
  exactly; pathological expansion beyond 2,000,000 characters fails explicitly;
  33 focused tests, compilation, config validation, and diff checks pass; test
  commit `b2069d6`; supervisor restarted as PID `1553729`. Evidence path:
  `experiments/20260807T012000Z-protocosmo2-full-pdf-ingestion/`.

- [x] 2026-08-06: Strictly validate ThreadKeeper candidate-review patch
  proposal metadata at commit `9778222`. The read-only review helper now
  accepts only `write-file`/`append-file`, applies the existing strict
  workspace-relative path grammar, requires string content when present, and
  rejects proposal batches above the dispatch tool-call bound before exposing
  them to a parent/operator. Twenty-eight focused and all 1,186 provider-free
  subagent hardening tests passed, plus compilation, `git diff --check`, and
  draft PR #1 safety-floor ancestry.

- [x] 2026-08-06: Give `@Protocosmo2bot` bounded ambient Telegram context.
  Deliverable: retain human-authored messages and readable document text from
  every group update the bot receives, inject recent same-chat history as
  explicitly untrusted context only when the bot is mentioned/replied to, and
  continue suppressing replies to ambient chatter and bot-authored messages.
  Acceptance: provider-free tests prove ambient text/document retention,
  same-chat isolation, bounded persistence, restart recovery, and no ambient
  outbound reply. Next command: patch the Phase-6 transport/contract and run
  the focused provider-free suite. Evidence path:
  `experiments/20260807T011248Z-protocosmo2-telegram-context-ingestion/`.
  Completed: commit `4da168b`; 31 focused tests, compilation, migration, and
  diff checks pass. The supervisor is active on state schema v2 with one
  runner, no pending inbound, and its prior cursor preserved.

- [x] 2026-08-06: Enable bounded Telegram document visibility for
  `@Protocosmo2bot`. Deliverable: accept addressed PDF/plain-text documents,
  download them through the bot-owned Telegram API, inject bounded extracted
  text as explicitly untrusted prompt context, and retain attachment blocking
  for unsupported or oversized media. Acceptance: focused provider-free tests
  cover caption mentions, PDF/text extraction, unsupported types, size/length
  caps, and no attachment egress; the live configuration validates and the
  supervised worker restarts cleanly. Completed: commit `7a40c5d`; 27 tests,
  compilation, config validation, and diff checks pass; supervisor restarted
  cleanly. Evidence: `experiments/20260807T003656Z-protocosmo2-telegram-document-ingestion/`.
  Live acceptance needs a fresh PDF with `@Protocosmo2bot` in its caption.

- [x] 2026-08-06: Record Capacity 1.1's independent A09--A12 held-out
  commitment before generator implementation. Four exact withheld cases cover
  a bounded PeTTA-memory record request and paraphrase plus live and mixed
  GoalChainer-to-ThreadKeeper task-claim requests. The exact 9,132 reveal bytes
  are SHA-256 committed; the gate contains only an encrypted sealed copy and
  keeps reveal unauthorized until a candidate implementation hash is frozen.
  One direct check and four negative tests pass. Evidence:
  `artifacts/ggb-capacity-gates/20260806-request-to-contract-heldout-commitment/`.
  The seam is now content-bound but requires an exception-tagging revision;
  do not reveal or implement a generator without the separate candidate
  authorization/freeze step.

- [x] 2026-08-06: Strictly validate ThreadKeeper run-index audit path
  arguments at commit `ef9bf3b`. The operator-facing audit helper now rejects
  empty strings, leading/trailing whitespace, non-NFC spellings, control
  characters, and paths above the hard argument cap before filesystem
  resolution. Eight focused and all 1,181 provider-free subagent hardening
  tests passed, plus compilation, documentation, `git diff --check`, and draft
  PR #1 safety-floor ancestry.

- [x] 2026-08-06: Make `@Protocosmo2bot` continuously operational in every
  Telegram group where it receives messages, as explicitly authorized by Ben.
  Deliverable: authorize any negative Telegram group/supergroup chat ID and
  any human group sender while retaining Ben-only direct messages, durable
  deduplication/recovery, and loop controls; install/start a restart-on-failure
  supervisor. Acceptance: provider-free authorization regressions pass, the
  redacted live config validates, and the worker remains active after startup.
  Next command: extend the Phase-6 contract schema and focused tests, then
  start the persistent launcher. Completed: 25 focused tests pass; Telegram
  reports `can_join_groups=true` and `can_read_all_group_messages=true`; the
  supervised runner is active at durable offset `387572145`, with no pending
  transaction. Bot-authored updates and unaddressed group chatter are skipped
  to prevent echo/spam; any human may invoke it by mention or reply. Evidence:
  `experiments/20260806T224725Z-protocosmo2-universal-group-operation/`.

- [x] 2026-08-06: Strictly validate ThreadKeeper queued-worker task path
  spelling at commit `e91f221`. The operator-facing claim helper now rejects
  leading/trailing whitespace and non-NFC spellings before any queue rename,
  closing the remaining ambiguity at this worker control boundary. Fourteen
  focused and all 1,175 provider-free subagent hardening tests passed, plus
  compilation, `git diff --check`, documentation, and draft PR #1 safety-floor
  ancestry.

- [x] 2026-08-06: Freeze executable implementations of Capacity 1.1's 22
  public generator-facing cases (A01--A08 and N01--N14). The monitored
  invocation seam covers exact/canonical replay, determinism, paraphrase and
  authority discrimination, provenance/digest binding, strict raw-byte
  negatives, and clean-effect attestation. Three provider-free self-tests and
  compilation pass. Evidence:
  `artifacts/ggb-capacity-gates/20260806-request-to-contract-public-executable-cases/`.
  This is partial R1 evidence. The independent A09--A12 commitment now exists;
  invocation-seam adoption is blocked by the exception mismatch recorded in
  the newer task above.


- [x] 2026-08-06: Strictly validate ThreadKeeper candidate-review transcript
  path arguments at commit `8f299b6`. The operator-facing review helper now
  rejects leading/trailing whitespace, non-NFC spellings, control characters,
  and paths above the hard argument cap before filesystem resolution, matching
  the hardening already applied to other worker control paths. Twenty-three
  focused and all 1,173 provider-free subagent hardening tests passed, plus
  compilation, `git diff --check`, documentation, and draft PR #1 safety-floor
  ancestry.

- [x] 2026-08-06: Require ThreadKeeper candidate transcript checksums at
  commit `d0ee80b`. Candidate review previously accepted a transcript when its
  `.sha256` sidecar was absent, allowing sidecar deletion to downgrade
  integrity verification. Missing, malformed, or mismatched sidecars now fail
  closed before patch/adjudication metadata is trusted. Eighteen focused and
  all 1,168 provider-free subagent hardening tests passed, plus compilation,
  `git diff --check`, documentation, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-06: Independently replay Capacity 1.1's content-bound v0.4
  generic-failure sandbox across all twelve frozen cases. The consumer binds
  the contract, producer record, facade, and underlying Bubblewrap sources and
  reuses the separately implemented v0.3 probes rather than producer tests.
  All twelve cases pass, E1--E6 are covered, and the prior private stderr
  sentinel is exposed only as `sandbox candidate failed`. Five independent
  tests and compilation pass. Evidence:
  `artifacts/ggb-capacity-gates/20260806-request-to-contract-os-sandbox-v04-independent-replay/`.
  Verdict: `r4_empirical_replay_pass`; R1/R2 and harness adoption remain open.

- [x] 2026-08-06: Add integrity sidecars for ThreadKeeper queued-worker result
  records at commit `a28eacf`. Successful and failed compact result JSON now
  publishes with its own checksum before the final `*.done`/`*.failed` task
  rename, so terminal state cannot become visible with unsigned result
  evidence. Six focused and all 1,167 provider-free subagent hardening tests
  passed, plus compilation, `git diff --check`, documentation, and draft PR #1
  safety-floor ancestry.

- [x] 2026-08-06: Publish ThreadKeeper persistent run transcripts only after
  their checksum sidecars are durable at commit `2d290cf`. Finished transcript
  bytes now stay under a non-discoverable staging name until the checksum is
  written, with the final transcript rename serving as the publication commit
  point. An injected sidecar failure exposes neither artifact; an injected
  post-commit directory-fsync error retains the visible transcript/checksum
  pair. Six focused and all 1,167 provider-free subagent hardening tests
  passed, plus compilation, `git diff --check`, documentation, and draft PR #1
  safety-floor ancestry.

- [x] 2026-08-06: Content-bind Capacity 1.1's v0.4 generic-failure sandbox
  revision without mutating the frozen v0.3 evidence. The facade maps every
  sandbox `RuntimeError` to `sandbox candidate failed`; the exact private
  stderr sentinel regression no longer crosses the API boundary. Four focused
  revision tests, fourteen frozen twelve-case producer checks, and ten
  underlying sandbox regressions passed, plus binding validation and
  compilation. Evidence:
  `artifacts/ggb-capacity-gates/20260806-request-to-contract-os-sandbox-v04-binding/`.
  Next: independently bind and replay all twelve cases. R1/R2/R4 remain open.

- [x] 2026-08-06: Make ThreadKeeper queued-task enqueue publication atomic
  with its checksum at commit `a0fd814`. Pending tasks previously became
  worker-visible as `queue/*.json` before their checksum sidecar was written,
  so a sidecar persistence failure could leave a poisoned pending task. Task
  bytes now remain under a non-discoverable staging name until the checksum is
  durable; the final task rename is the enqueue commit point. Three focused
  and all 1,165 provider-free subagent hardening tests passed, plus compilation,
  `git diff --check`, documentation, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-06: Preserve ThreadKeeper queued-failure audit evidence after a
  post-commit directory-fsync error at commit `f300f5e`. The terminal rename
  can already be externally visible when its parent fsync raises, so deleting
  the staged checksum and compact failure result would leave an unauditable
  `*.failed` marker. Cleanup now occurs only before publication; an injected
  post-rename fsync failure retains all three terminal artifacts. Two focused
  and all 1,164 provider-free subagent hardening tests passed, plus compilation,
  `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-06: Independently replay Capacity 1.1's content-bound v0.3 OS
  sandbox across all twelve required cases without importing producer tests.
  Eleven cases pass; the network-isolation adversary exposes an E6 failure
  because its private stderr sentinel is returned verbatim through
  `RuntimeError`. Five independent checks plus compilation and JSON validation
  pass. Evidence:
  `artifacts/ggb-capacity-gates/20260806-request-to-contract-os-sandbox-v03-independent-replay/`.
  Next: replace child stderr detail with a generic failure, content-bind the
  revision, and independently replay again. R1/R2/R4 remain open.

- [x] 2026-08-06: Commit ThreadKeeper queued-task failure only after its audit
  artifacts are durable at commit `fe4fc73`. The worker previously renamed a
  claimed task to `*.failed` before writing the checksum and compact failure
  result, so persistence failure could publish an unauditable terminal marker.
  The checksum and result now stage first, the atomic failure rename is the
  commit point, and injected result-write failure cleans provisional artifacts
  while retaining `*.claimed`. Four focused and all 1,163 provider-free
  subagent hardening tests passed, plus compilation, `git diff --check`, and
  draft PR #1 safety-floor ancestry.

- [x] 2026-08-05: Make ThreadKeeper queued-task completion commit only after
  its audit artifacts are durable at commit `e1f3c47`. The prior worker renamed
  `*.claimed` to `*.done` before writing the checksum and result record, so a
  write failure or crash could publish a falsely complete task with missing
  evidence. The checksum and compact result now stage first; the atomic done
  rename is the completion commit point, and injected persistence failure
  retains `*.failed` evidence. Thirty-four focused and all 1,162 provider-free
  subagent hardening tests passed, plus compilation, `git diff --check`,
  documentation, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-05: Bind Capacity 1.1's Bubblewrap sandbox to the frozen v0.3
  externally observable-effect contract and replay all twelve required
  adversarial classes. The new producer-side artifact adds the previously
  missing stdin, address-space, and process-count probes and rejects bound
  source or authority drift. Fourteen provider-free tests, the direct binding
  checker, Python compilation, and diff checks pass. Evidence:
  `artifacts/ggb-capacity-gates/20260806-request-to-contract-os-sandbox-v03-binding/`.
  Next: independent replay without importing the producer tests. R1/R2/R4,
  harness adoption, generator implementation, and runtime effects remain open
  or unauthorized.

- [x] 2026-08-05: Fail closed on oversized ThreadKeeper LLM guard state at
  commit `e05191f`. The bounded reader previously returned an empty object
  when a persistent rate/concurrency JSON record exceeded its cap, discarding
  active reservations and admitting a provider call. Oversized state now
  blocks rate and concurrency acquisition and remains untouched for operator
  inspection. Twenty-one focused and all 1,161 provider-free subagent
  hardening tests passed, plus Python compilation, `git diff --check`,
  documentation, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-05: Reject future-dated ThreadKeeper queued tasks when expiry is
  enabled at commit `51912df`. The prior age check treated a future
  `queued_at` as negative age, allowing a forged or rollback-relative timestamp
  to postpone the configured expiry boundary. Future skew beyond the default
  300-second allowance now fails before worker dispatch; the allowance is
  configurable but hard-capped at 3,600 seconds. Five focused and all 1,161
  provider-free subagent hardening tests passed, plus Python compilation,
  `git diff --check`, documentation, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-05: Freeze Capacity 1.1's externally observable no-effect
  boundary v0.3 after the native `fork`/`exec` review exposed the prior
  call-denylist mismatch. The contract pins six outcome invariants and twelve
  required adversarial case classes while allowing wholly confined internal
  computation. Five provider-free tests, direct validation, compilation, and
  diff checks pass. Evidence:
  `artifacts/ggb-capacity-gates/20260805-request-to-contract-effect-boundary-v03/`.
  Next: content-bound sandbox revision and independent twelve-case replay; R4,
  harness adoption, generator implementation, and runtime effects remain open.

- [x] 2026-08-05: Enforce ThreadKeeper's supervised queued-worker runtime with
  a monotonic clock at commit `f5d4364`. The loop previously measured
  `max_runtime_s` and task duration with the adjustable civil clock, allowing
  clock rollback to extend its bound. Runtime admission and duration accounting
  now use `time.monotonic()`, while audit timestamps remain civil; idle polling
  also sleeps for no longer than the remaining runtime budget. Three focused
  and all 1,160 provider-free subagent hardening tests passed, plus Python
  compilation, `git diff --check`, documentation, and draft PR #1 safety-floor
  ancestry.

- [x] 2026-08-05: Enforce ThreadKeeper dispatch and retry deadlines with a
  monotonic clock at commit `e7d9d6e`. The prior adjustable-wall-clock
  arithmetic allowed a backward NTP/operator clock step to extend the dispatch
  safety bound and a forward step to abort valid work. Dispatch elapsed-time
  checks, retry admission/backoff, and provider-call timeout caps now share one
  monotonic deadline. Five focused and all 1,158 provider-free subagent
  hardening tests passed, plus Python compilation, `git diff --check`,
  documentation, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-05: Independently bypass-review the Capacity 1.1 OS sandbox.
  A content-bound `ctypes` adversary calls libc `fork`/`execl`, completes
  `/usr/bin/true`, and receives `pass`, bypassing Python audit events for an
  effect explicitly forbidden by the frozen acceptance contract. Bubblewrap
  still contains the child and this is not a demonstrated host escape. Eight
  provider-free review checks, direct JSON replay, compilation, and diff checks
  pass. Evidence:
  `artifacts/ggb-capacity-gates/20260805-request-to-contract-os-sandbox-independent-review/`.
  Verdict: `revision_required_before_harness_adoption`. Next: freeze either
  syscall-level no-effect enforcement or a narrower externally-observable-
  effect contract, then independently replay it. R1/R2/R4 remain open; no
  generator or runtime effect is authorized.

- [x] 2026-08-05: Make ThreadKeeper LLM quota-state writes crash-safe at
  commit `e7459ff`. Rate and concurrency JSON records now use stable sidecar
  locks plus atomic replacement, avoiding both the prior truncate/write loss
  window and the stale-inode locking race of replacing a locked data file. An
  injected replacement failure preserves the active quota and fails closed.
  Twenty-seven focused and all 1,156 provider-free tests passed, plus Python
  compilation, `git diff --check`, documentation, and draft PR #1 safety-floor
  ancestry.

- [x] 2026-08-05: Preflight optional-shell calls across ThreadKeeper's whole
  worker tool batch at commit `9316269`. Shell enablement, bounded argv parsing,
  executable allowlisting, and workspace availability previously failed only
  when the shell call executed, so a valid earlier file mutation in the same
  batch could be applied first. Those checks now fail closed before the first
  batch effect. Twenty focused and all 1,155 provider-free subagent hardening
  tests passed, plus Python compilation, `git diff --check`, documentation, and
  draft PR #1 safety-floor ancestry.

- [x] 2026-08-05: Build an OS-enforced revision of the Capacity 1.1
  import-inclusive effect sandbox after the Python audit-hook bypass. The new
  Bubblewrap boundary exposes only a read-only minimal Python runtime and work
  tree, disposable `/tmp`, `/proc`, and `/dev`, and separate mount/network/PID
  namespaces; it also scrubs the environment, tears down descendants, and
  hard-caps CPU, address space, file size, processes, open files, captured
  output, and wall time. Ten provider-free adversarial tests pass, including
  the exact `os.symlink` bypass, a native host-path write attempt, network and
  subprocess effects, descendant survival, CPU exhaustion, and output flood.
  Evidence: `artifacts/ggb-capacity-gates/20260805-request-to-contract-os-sandbox/`.
  Next: independent bypass review before acceptance-harness adoption. R1/R2
  remain open; no generator or runtime effects are authorized.

- [x] 2026-08-05: Canonicalize optional-shell inherited `PATH` directories at
  ThreadKeeper commit `bd592e1`. The previous sanitizer checked each entry's
  resolved target but passed the unresolved spelling to the child, so a
  symlink could be retargeted after validation and before executable lookup.
  The child now receives only canonical existing absolute directories outside
  the worker workspace; missing entries are dropped. Four focused and all
  1,152 provider-free subagent hardening tests passed, plus Python compilation,
  `git diff --check`, documentation, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-05: Reject relative inherited `PATH` entries from ThreadKeeper's
  optional shell child at commit `6751252`. Subprocess command lookup resolves
  relative entries from the child cwd, so the prior parent-cwd validation of a
  value such as `bin` could still select a workspace-controlled executable
  with an allowlisted name. The child now retains only absolute entries that
  resolve outside the worker workspace. Three focused and all 1,150
  provider-free subagent hardening tests passed, plus Python compilation,
  `git diff --check`, documentation, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-05: Independently bypass-review the Capacity 1.1 import-inclusive
  R4 sandbox. A content-bound adversary creates an `os.symlink` outside the
  child cwd while the prototype reports `pass`, proving that its Python event
  denylist and cwd-only manifest are not effect-none containment. Eight
  provider-free review tests, direct JSON replay, compilation, and diff checks
  pass. Evidence:
  `artifacts/ggb-capacity-gates/20260805-request-to-contract-import-effect-sandbox-independent-review/`.
  Verdict: `revision_required_before_harness_adoption`. Next: an OS-enforced
  disposable filesystem/network/process boundary with resource/output caps;
  do not embed the current prototype in the 26-case harness.

- [x] 2026-08-05: Strictly validate ThreadKeeper optional-shell allowlist
  configuration at commit `001c216`. The comma-separated allowlist now fails
  closed above 16,384 characters or 256 entries, and rejects entries above 255
  characters or outside the bounded ASCII command-name grammar before any
  subprocess execution. Thirteen focused and all 1,149 provider-free
  subagent hardening tests passed, plus Python compilation, `git diff --check`,
  documentation, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-05: Hard-cap ThreadKeeper RAG knowledge-prior reads at commit
  `ffbbf8a`. Oversized `OMEGACLAW_MAX_KNOWLEDGE_FILE_BYTES` values are now
  clamped to 64 MiB, so local configuration cannot turn one already no-follow,
  regular-file-validated RAG read into an effectively unbounded operation. The
  default remains 2 MiB. All 15 focused provider-free RAG hardening tests
  passed, plus Python compilation, `git diff --check`, documentation, and
  draft PR #1 safety-floor ancestry.

- [x] 2026-08-05: Make the Capacity 1.1 acceptance gate's R4 no-effect
  boundary operational as an import-inclusive isolated-child prototype.
  Candidate import and `generate_contract(bytes)` now run after an audit hook,
  with a minimal credential-free environment, fresh cwd, three-second timeout,
  and before/after content manifest. Six provider-free tests pass, including
  import-time write, call-time outside-cwd write, network, subprocess, and
  environment adversaries, plus compilation and `git diff --check`. Evidence:
  `artifacts/ggb-capacity-gates/20260805-request-to-contract-import-effect-sandbox/`.
  Next: independent bypass review before harness adoption. This is not R4
  closure; executable cases (R1), held-out commitment (R2), generator code,
  and runtime effects remain unauthorized.

- [x] 2026-08-05: Hard-cap ThreadKeeper worker data and dispatch
  configuration at commit `96b7f60`. Persisted patch proposals, final emits,
  and parsed worker responses are clamped to 1,000,000 characters; native
  worker response bodies to 16 MiB; queue age to one year; dispatch runtime to
  86,400 seconds and token budgets to 10,000,000; workspace files to 64 Mi
  characters; and retained run-index entries to 1,000,000. Oversized
  environment values can no longer turn these output, quota, persistent-file,
  or audit-retention controls into effectively unbounded operations. Two
  focused reload tests and all 1,144 provider-free subagent hardening tests
  passed, plus Python compilation, `git diff --check`, documentation, and
  draft PR #1 safety-floor ancestry. The first compile command used
  unavailable `python`; the corrected `python3` check passed.

- [x] 2026-08-04: Hard-cap ThreadKeeper persistent worker setup/state reads at
  commit `543525b`. Queue/transcript JSON reads are clamped to 64 MiB,
  checksum sidecars to 64 KiB, escalation policies and persona prompts to 16
  MiB, persona configs and LLM guard state to 1 MiB, persona control scalars
  to 65,536 characters, and index/transcript audit reads to 64 MiB. Oversized
  environment values can no longer turn these setup, integrity, quota-state,
  or audit reads into effectively unbounded operations. One focused reload
  test and all 1,143 provider-free subagent hardening tests passed, plus
  Python compilation, `git diff --check`, documentation, and draft PR #1
  safety-floor ancestry. The first two full runs encountered the suite's
  persistent rate/concurrency guards; the documented provider-free run with
  both local LLM guards disabled passed.

- [x] 2026-08-04: Hard-cap ThreadKeeper worker tool-return configuration at
  commit `d0a136b`. Shell output, external search/analysis output, and
  `read-file` output are clamped to at most 1,000,000 characters, while one
  optional shell subprocess is clamped to 600 seconds. Oversized environment
  values can no longer turn these bounded tool returns or subprocess waits into
  effectively unbounded worker operations. One focused test and all 1,142
  provider-free subagent hardening tests passed on the final full run, plus
  Python compilation, `git diff --check`, documentation, and draft PR #1
  safety-floor ancestry.

- [x] 2026-08-04: Independently review Capacity 1.1 generator acceptance
  preregistration v0.2. The bytes API closes R3 at the contract level, but the
  26 named cases have no executable implementations, no independent held-out
  byte commitment exists, and the effect monitor is declarative with candidate
  import outside it. Eight provider-free review tests pass. Evidence:
  `artifacts/ggb-capacity-gates/20260805-request-to-contract-generator-acceptance-v02-independent-review/`.
  Next: freeze executable cases, the held-out commitment, and an import-inclusive
  sandbox; generator implementation and runtime effects remain unauthorized.

- [x] 2026-08-04: Hard-cap ThreadKeeper budget/accounting read configuration
  at commit `33cbdda`. Usage-log read configuration is clamped to 1 KiB--64
  MiB and budget-config reads to 1 KiB--1 MiB, so oversized environment values
  cannot turn quota accounting or escalation-policy setup into unbounded local
  reads. All 27 focused provider-free budget hardening tests passed, plus
  Python compilation, `git diff --check`, documentation, and draft PR #1
  safety-floor ancestry.

- [x] 2026-08-04: Revise Capacity 1.1 generator acceptance preregistration at
  the contract level after the independent R1--R4 failure. V0.2 freezes an
  exact `generate_contract(bytes) -> bytes` API with `ValueError` rejection,
  canonical UTF-8 JSON, 26 named generator-facing cases, explicit effect and
  filesystem monitoring, and an independent held-out reveal only after
  candidate hash freeze. Ten provider-free structural tests pass. The harness
  intentionally refuses candidate execution until independent review freezes
  the real case implementations and held-out commitment. Evidence:
  `artifacts/ggb-capacity-gates/20260804-request-to-contract-generator-acceptance-preregistration-v02/`.
  Next: independent content-bound R1--R4 closure; generator code and runtime
  effects remain unauthorized.

- [x] 2026-08-04: Hard-cap ThreadKeeper supervised queue/worker configuration
  at commit `7130ffd`. Pending dispatches and tasks per invocation are clamped
  to 0--4,096, idle polls to 0--3,600, poll sleeps to 0--300 seconds, runtime
  to 0--86,400 seconds, retained results and consecutive errors to 0--256,
  and lock metadata to 1,024--65,536 bytes. Oversized environment values can
  no longer make an explicit worker invocation, queue scan, retained return,
  or stale-lock read effectively unbounded. Two focused checks and all 1,141
  provider-free subagent hardening tests passed, plus Python compilation,
  `git diff --check`, documentation, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-04: Execute ProtoCosmo2 Phase 6 as a bounded private Telegram
  canary, explicitly authorized by Ben in Protobots message 16261. Acceptance:
  distinct ProtoCosmo2 identity; Ben-only allowlist; outbound rate/depth and
  attachment bounds; no autonomous schedules or state-changing extras;
  verified receive/send, reply routing, duplicate handling, visible failures,
  and crash recovery; transcript hashes, incident log, latency/cost summary,
  and a recorded private-canary go/no-go. The fail-closed dedicated
  configuration is staged at `/home/openclaw/.openclaw/protocosmo2.env` and
  `/home/openclaw/.openclaw/protocosmo2-canary.json` (both mode 0600): it is
  Ben-only (chat/user `402314199`), blocks attachments and autonomous/stateful
  extras, allows at most 3 outbound messages/hour and reply depth 1. Next
  command after the blocker clears: verify the distinct bot identity and exact
  Ben-only config without sending, then start the supervised bounded private
  canary. Live blocker: the dedicated token slot is intentionally blank; do
  not reuse another bot's token. Evidence path:
  `experiments/20260805T011343Z-protocosmo2-phase6-private-canary-preflight/`.
  **Credential/identity gate passed 2026-08-05:** Ben supplied the dedicated
  token; it is installed only in the mode-0600 secret env file. A redacted
  `getMe` check verified the distinct `@Protocosmo2bot` / `ProtoCosmo2`
  identity without sending or polling. Evidence:
  `experiments/20260805T031907Z-protocosmo2-phase6-getme-identity/`. The live
  adapter is not yet started: the Phase-6 branch has `CanaryContract` but no
  Telegram transport bridge, and the legacy direct adapter is forbidden
  because it bypasses the frozen canary controls. Next command: implement and
  provider-free test that bridge, then launch it waiting for Ben's first DM.
  **2026-08-05 resumed acceptance:** two new Ben-only plain-text DMs were
  durably received and each produced exactly one routed reply (Telegram
  receipts 114 and 116); the state has no pending inbound and retains the
  fresh cursor. Deliverable: finish Phase-6 acceptance with a controlled
  runner restart plus provider-free duplicate/recovery/refusal replay, then
  archive redacted state/log evidence and record the private-canary go/no-go.
  Acceptance test: cursor and processed IDs survive restart without a second
  send; all contract/transport tests pass; no group or non-Ben live traffic.
  Next command: run the controlled restart and capture the before/after state
  snapshot in a timestamped experiment record.
  **Completed 2026-08-05:** the repaired dedicated `@Protocosmo2bot` canary
  received two new Ben-only plain-text DMs and sent one reply to each (receipts
  114 and 116), with no pending transaction or incident. The provider-free
  contract/transport acceptance suite passed 17/17. A controlled live runner
  restart preserved the exact durable state hash, cursor `387571971`, two
  committed records, and zero incidents without another send; final stop was
  clean. Evidence:
  `experiments/20260805T235502Z-protocosmo2-phase6-acceptance-provider-free/`
  and
  `experiments/20260805T235543Z-protocosmo2-phase6-live-restart-recovery/`.
  Phase 7 group enrollment/wider authority remains explicitly gated.

- [x] 2026-08-05: Stage ProtoCosmo2 Phase 7 for the discovered
  `Protobot-updates` supergroup (`-1003983157420`) after Ben authorized group
  use. Deliverable: allow signed Bot-API chat IDs while retaining a Ben-only
  user allowlist; archive the completed private cursor; establish a fresh
  group cursor that skips pre-enablement updates; and run one bounded
  plain-text group canary. Acceptance: signed group IDs are unit-tested,
  historic group messages receive no response, and one new Ben group message
  yields at most one reply. Next command: add the signed-chat-ID validation
  regression and run the focused transport suite. Evidence:
  `experiments/20260806T000123Z-protocosmo2-phase7-group-discovery/`.
  **Live canary defect and repair:** the first group attempt exposed a
  pending-transaction livelock: an inbound at the reply-depth cap was claimed,
  but its blocked outbound did not advance the cursor, so later updates were
  repeatedly rejected and incident-counted. The canary was stopped at
  incident sequence 537. Commit `8de2c4b` closes depth/rate-blocked
  transactions and adds an exact later-update regression; 21/21 focused tests
  plus compilation and diff checks pass. The failed state/log were archived
  intact and a repaired canary started fresh at offset `387571989`, empty and
  incident-free. Evidence:
  `experiments/20260806T000929Z-protocosmo2-phase7-pending-transaction-repair/`
  and
  `experiments/20260806T001016Z-protocosmo2-phase7-repaired-group-relaunch-r2/`.
  Next acceptance action: one new Ben-authored plain-text group mention, then
  verify exactly one receipt and no stalled transaction.
  **Completed 2026-08-06:** after the fail-closed launcher/recovery repair,
  Ben's new group mention received exactly one generated depth-1 reply
  (receipt `4837`), no transaction remained pending, and the launcher stopped
  the runner cleanly. Evidence:
  `experiments/20260806T200519Z-protocosmo2-phase7-group-canary-fixed-window-r2/`.
  This accepts the bounded group canary only; continuous operation, schedules,
  attachments, and wider-user authority remain separate decisions.
  **Repair obligation accepted 2026-08-05 07:41 PDT:** repair the responder
  bridge failure and fresh-offset/history-admission defect before any renewed
  live canary. Acceptance: provider-free regression tests reproduce both
  failures and pass after repair; a new experiment record captures exact
  commands and results; only then may the stopped Ben-only canary be relaunched.
  Next command: inspect the redacted canary log/state and run the focused
  Phase-6 transport tests from the isolated `protocosmo2` worktree. Completion
  evidence path: `experiments/20260805T*-protocosmo2-phase6-repair/`.
  **Offline repair gate passed:** commit `3438248` plus the project-local
  responder-driver repair passed 18/18 focused tests, a deterministic
  file-channel response (`phase6-repair-ok`, 1.786 s), and a real
  OpenClawFileBridge response (`phase6-real-bridge-ok`, 11.296 s), all without
  Telegram I/O or a fatal native signal. Evidence:
  `experiments/20260805T144715Z-protocosmo2-phase6-repair/`,
  `experiments/20260805T145213Z-protocosmo2-phase6-responder-smoke-r3/`, and
  `experiments/20260805T145229Z-protocosmo2-phase6-real-responder-gate/`.
  Live canary remains stopped. Next: reversibly archive the failed
  pending/rate-exhausted state and stage a fresh Ben-only canary for the
  remaining live duplicate/recovery/refusal acceptance cases.

  Offline preflight is complete at OmegaClaw-Core commit `2f714e9` on
  `agent/protocosmo2-phase6-private-canary-preflight`. The exact-schema,
  provider-free contract enforces the ProtoCosmo2 identity, chat-and-user
  allowlists, persistent outbound rate and reply-depth caps, attachment
  refusal, durable message-id/receipt deduplication, fixed visible failures,
  and atomic inbox/outbox cursor recovery. All 13 focused tests passed;
  Phase-5 structural
  preflight remained 10 cases/7 critical controls at frozen digest
  `9203c4a65edf128c3290c347099dcff32f28a02282e478b486a7f16ee175f6bf`,
  its dry runner remained inert, and file-bridge repair `bebe357` remains an
  ancestor. No provider, listener, credential, or Telegram traffic was used.
  Live checklist after the dedicated credential is provisioned: (1) verify a
  distinct ProtoCosmo2 bot identity and exact Ben chat/user IDs; (2) wire the
  poll/send adapter exclusively through the durable contract with schedules,
  attachments, state-changing extras, and groups disabled; (3) run bounded
  receive/send and reply-routing cases; (4) replay duplicate updates and test
  allowlist/rate/depth/attachment refusals; (5) force visible provider and
  transport failures; (6) crash before outbox and after queued outbox, restart,
  and verify cursor/receipt continuity without a second model processing; (7)
  hash the redacted transcript, preserve the incident log, summarize latency
  and token/provider cost, stop the canary, and record a private-canary go/no-go
  before any group enrollment.

- [x] 2026-08-05: Build and integrate an OmegaClaw-native adapter for the
  improved `persistent-subagent-orchestration` policy, explicitly requested by
  Ben. Deliverable: a bounded local durable task/event adapter exposed through
  OmegaClaw's skill catalog, with create/status/pause/resume/cancel/advance
  controls and provenance-aware standing-approval continuity. Acceptance:
  plain-language invariants frozen before implementation; exact schemas and
  path/resource bounds; atomic/hash-checked state; no provider, Telegram,
  scheduler, paid-compute, or generic shell authority; positive lifecycle,
  restart/idempotency, malformed/corrupt-state, authority precedence,
  revocation/expiry/exhaustion, and traversal/symlink refusal tests; focused
  provider-free suite plus relevant existing skill tests pass; coherent local
  commit and experiment record. **Completed offline:** commit `5c64918` is
  fast-forwarded into `agent/protocosmo2-phase6-live`. Five MeTTa skills expose
  bounded durable create/status/checkpoint/control/authority decisions.
  Forty-four provider-free tests passed; the modified Core loaded through
  pinned PeTTa and returned `adapter-core-load-ok` in 2.277 s; the dedicated
  real mode-0700 state root returned a canonical `task_not_found` refusal for
  an absent task. No provider, Telegram, scheduler, subprocess, shell action,
  approval mutation/consumption, remote compute, or paid use occurred. The
  state-only v1 is integrated; an autonomous executor remains deliberately out
  of scope. Evidence:
  `experiments/20260805T160618Z-protocosmo2-persistent-worker-adapter-r6/`,
  `experiments/20260805T160646Z-protocosmo2-persistent-worker-adapter-core-load/`,
  and
  `experiments/20260805T160829Z-protocosmo2-persistent-worker-adapter-configured-smoke/`.

- [x] 2026-08-04: Hard-cap ThreadKeeper task-contract configuration at commit
  `cd97ce8`. Contract list fields are clamped to 0--256 entries, individual
  items to 1--8,192 characters, and objectives to 1--65,536 characters, so
  oversized environment values cannot make validation and retained contract
  records effectively unbounded. The focused 143-case contract slice and all
  1,150 provider-free subagent hardening tests plus six subtests passed, along
  with Python compilation, `git diff --check`, documentation, and draft PR #1
  safety-floor ancestry.

- [x] 2026-08-04: Complete ProtoCosmo2 Phase 5 through the real pinned
  OmegaClaw/PeTTa runtime. Deliverable: isolate and repair the post-response
  SIGSEGV, pass a fresh-state one-case stability gate, then execute and score
  all ten frozen shadow cases with Telegram/outbound delivery disabled.
  Acceptance: no fatal native signal, captured real-runtime answers and tool
  traces for all cases, critical gates scored, and a complete experiment
  `RUN.md`. Next command: replay the exact captured real-model response through
  the deterministic provider on disposable history/Chroma state and compare
  shutdown versus natural-exit behavior. Evidence path:
  `experiments/20260804T064606Z-protocosmo2-phase5-loopback-bridge-real-gate/`
  and the next Phase-5 experiment record.
  Runtime stability is now repaired: the exact-response replay ruled out
  response/history corruption, and replacing embedded provider/channel RPC
  sockets with bounded private file bridges eliminated the Janus/SWI
  `POLLRDHUP` teardown race. A fresh ten-case run completed 10/10 with no
  SIGSEGV. Behavioral acceptance remains open: `project-status` did not inspect
  project records, and `recall-attribution` omitted the frozen private-canary
  decision/source. Next command: repair project-record retrieval/source
  resolution and rerun those two critical cases. Evidence:
  `experiments/20260804T173323Z-protocosmo2-phase5-real-runtime-frozen-suite-file-channel/`.
  Retrieval/source resolution is now repaired at the bounded host file-bridge
  boundary. Targeted reruns of `recall-attribution` and `project-status` meet
  their critical intents, and a fresh full frozen-suite run completed 10/10
  with exit zero, no fatal signal, and outbound disabled. Automated Phase-5
  gates are complete. Ben explicitly authorized moving to Phase 6 in
  Protobots message 16261, satisfying G5/go-no-go. Evidence:
  `experiments/20260804T211817Z-protocosmo2-phase5-retrieval-repair/`.

- [x] 2026-08-04: Hard-cap ThreadKeeper durable transcript retention at commit
  `75fc765`. Retained transcript turns are clamped to 1--64, per-turn fields
  to 1--1,000,000 characters, and persisted summaries to 1--65,536
  characters. Oversized environment values can no longer make persistent run
  transcripts effectively unbounded. Two focused and all 1,149 provider-free
  subagent hardening checks passed, plus Python compilation, `git diff
  --check`, corrected documentation, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-04: Hard-cap ThreadKeeper bounded-history and return
  configuration at commit `57ac088`. Per-dispatch turns and retained prompt
  history are clamped to 1--64, parent digests to 100--20,000 characters, and
  worker output to 1--65,536 tokens. Oversized environment values can no
  longer turn these safety controls into effectively unbounded worker state.
  Two focused and all 1,138 provider-free subagent hardening checks passed,
  plus Python compilation, `git diff --check`, documentation, and draft PR #1
  safety-floor ancestry.

- [x] 2026-08-04: Independently review Capacity 1.1 generator acceptance
  discrimination and implementability. The content-bound review found four
  blockers: the required command runs 10 metadata tests rather than 20
  generator-facing tests, public fixtures admit a hard-coded lookup, the raw
  JSON versus parsed-object API is ambiguous, and determinism/effect monitoring
  are not operationally defined. Nine provider-free tests, compilation, and
  `git diff --check` pass. Evidence:
  `artifacts/ggb-capacity-gates/20260804-request-to-contract-generator-acceptance-independent-review/`.
  Next: revise the preregistration and independently close R1--R4; generator
  implementation and runtime effects remain unauthorized.

- [x] 2026-08-04: Preregister Capacity 1.1 exact generator fixtures and
  implementation acceptance tests. Five exact input/output pairs cover the
  roadmap paraphrase pair, GoalChainer offline/live minimal pair, and mixed
  bounded/live request. The 20-case acceptance matrix has eight positive and
  12 negative cases; ten provider-free preregistration tests, compilation, and
  `git diff --check` pass. Evidence:
  `artifacts/ggb-capacity-gates/20260804-request-to-contract-generator-acceptance-preregistration/`.
  Next: independent discrimination/implementability review only; generator
  code and runtime effects remain unauthorized.

- [x] 2026-08-04: Hard-cap ThreadKeeper worker tool configuration at commit
  `bfb3de2`. Per-dispatch tool calls are clamped to 0--256 and per-turn calls
  to 1--32; path, general tool, query, shell-command, and shell-argv limits now
  also have finite maxima. Oversized environment values can no longer weaken
  strict tool-argument validation or permit arbitrarily large tool batches.
  Eighteen focused and all 1,137 provider-free subagent hardening checks
  passed, plus Python compilation, `git diff --check`, documentation, and
  draft PR #1 safety-floor ancestry.

- [x] 2026-08-04: Hard-cap ThreadKeeper worker LLM quota configuration at
  commit `df2d3be`. Calls per minute are clamped to 0--600 and cross-process
  concurrent calls to 0--64, preventing oversized environment values from
  disabling meaningful backpressure or producing arbitrarily large guard
  state. Seven focused and all 1,136 provider-free subagent hardening checks
  passed, plus Python compilation, `git diff --check`, and draft PR #1
  safety-floor ancestry.

- [x] 2026-08-04: Independently close Capacity 1.1 interface findings R1--R4.
  A content-bound reviewer directly enumerates every output type and bound,
  allowed-path grammar/containment, and exact ordered provenance without
  importing producer code. Ten provider-free checks include nine fail-closed
  mutations. Evidence:
  `artifacts/ggb-capacity-gates/20260804-request-to-contract-generator-interface-v02-closure-review/`.
  Next: preregister generator fixtures and acceptance tests; no generator code
  or runtime effect is authorized by this review.

- [x] 2026-08-04: Hard-cap ThreadKeeper worker LLM reliability configuration
  at commit `358ede3`. Per-call timeout is clamped to 1--600 seconds, retry
  count to 0--5, and exponential-backoff base to 0--60 seconds, preventing
  oversized environment values from creating effectively unbounded attempts
  or backoff. Nine focused and all 1,135 provider-free subagent hardening
  checks passed, plus Python compilation, `git diff --check`, and draft PR #1
  safety-floor ancestry.

- [x] 2026-08-04: Validate ThreadKeeper persistent LLM guard-state schemas at
  commit `b1c3d2f`. Rate-limit timestamps and concurrency token/PID/timestamp
  records now require exact bounded types and closed schemas. Parseable
  corruption fails closed before provider calls or slot reservations and is
  preserved for diagnosis instead of silently resetting quota state. Thirteen
  new schema cases and all 1,132 provider-free subagent hardening checks
  passed, plus Python compilation, `git diff --check`, and draft PR #1
  safety-floor ancestry.

- [x] 2026-08-04: Revise the Capacity 1.1 request-to-contract generator
  interface to v0.2. Exact output types and assigned bounds, strict normalized
  OmegaClaw-contained allowed paths, and exact ordered provenance equality
  address independent findings R1--R4. Exact replay, nine provider-free
  negative tests, compilation, and `git diff --check` pass. Evidence:
  `artifacts/ggb-capacity-gates/20260804-request-to-contract-generator-interface-v02/`.
  Next: independent closure review only; do not implement a generator.

- [ ] 2026-08-04: Restore ProtoMegaBot ingestion of Hugo-Bot posts in Slack
  channel `C0BGBD99T9A`. Deliverable: retain the narrow Hugo bot-user allowlist,
  add Ben's explicit Slack owner ID for the documented bot-message membership
  authorization path, and verify a fresh Hugo-authored mention reaches the
  `protomegabot-simple` Slack session. Applied `channels.slack.allowFrom =
  ["U0BH5UJNDK5"]` and Ben restarted the system gateway; post-restart Slack
  probe is healthy and connected. At 23:12 PDT, ProtoMega posted a direct
  request for Hugo's `ProtoMega ingress test` reply. Acceptance remains: a
  fresh inbound session record contains Hugo user `U0BGG0S76Q6`. Next command:
  inspect the newest ProtoMega Slack session after Hugo replies. Evidence path:
  this task entry plus gateway/session logs.

- [x] 2026-08-04: Validate ThreadKeeper's primary LLM gateway endpoint at
  commit `8b2ce80`. Main provider construction now reuses the strict
  channel/auth `GATEWAY_URL` boundary instead of consuming the raw environment
  value. Ambiguous, credential-bearing, and malformed endpoints fail before
  OpenAI client construction or provider effects. Forty-two focused
  provider-free LLM/RAG/auth checks passed, plus Python compilation, `git diff
  --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-04: Validate ThreadKeeper's RAG embedding gateway endpoint at
  commit `24462aa`. The embedding path now reuses the strict channel/auth
  `GATEWAY_URL` boundary instead of constructing an OpenAI client from the raw
  environment value. Ambiguous, credential-bearing, and malformed endpoints
  fail before client construction or provider effects. Thirty-four focused
  provider-free RAG/auth checks passed, plus Python compilation, `git
  diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-04: Independently review the Capacity 1.1 request-to-contract
  generator interface. The review confirms its effect-none and fail-closed
  authority controls but finds four blocking omissions: output types, output
  field bounds, allowed-path grammar, and provenance ordering/canonicalization.
  Exact replay and eight provider-free negative tests pass. Evidence:
  `artifacts/ggb-capacity-gates/20260804-request-to-contract-generator-interface-independent-review/`.
  Next: revise the interface to v0.2 and independently close R1--R4; do not
  implement a generator.

- [x] 2026-08-03: Validate ThreadKeeper gateway endpoint URLs at commit
  `97e7c27`. Nonempty `GATEWAY_URL` values now require a bounded, absolute
  HTTP(S) URL without whitespace/control ambiguity, userinfo credentials,
  query/fragment data, backslashes, invalid ports, or non-NFC spelling before
  auth or channel request construction. Seventy-one focused provider-free
  auth/Telegram/Slack/Mattermost checks passed, plus Python compilation,
  `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-03: Strictly validate ThreadKeeper delegated tool subsets at
  commit `ef134ef`. Explicit and persona-default subsets now require a bounded
  exact string containing unique, nonempty, control-free, NFC-normalized skill
  names; malformed inputs fail before provider construction or tool effects.
  Seven focused provider-free cases and all 1,119 subagent hardening checks
  passed, plus Python compilation, `git diff --check`, and PR #1 safety-floor
  ancestry.

- [x] 2026-08-03: Freeze the Capacity 1.1 request-to-contract generator
  interface before implementation. Exact bounded input/output schemas preserve
  the six-field task contract, request/evidence provenance, OmegaClaw-only
  paths, and effect `none`. Nine live, mixed-authority, and ambiguous-scope
  triggers fail closed to `decision_required`; nine provider-free negative
  tests pass. Evidence:
  `artifacts/ggb-capacity-gates/20260803-request-to-contract-generator-interface/`.
  Next: independent interface review only; no generator implementation or
  runtime effect is authorized.

- [x] 2026-08-03: Validate ThreadKeeper persona provider endpoint URLs at
  commit `e2b3df2`. Nonempty configured `base_url` values must now be absolute
  HTTP(S) URLs without whitespace, userinfo credentials, query/fragment data,
  backslashes, invalid ports, or non-NFC spelling before provider construction.
  Fifty-six focused provider-free persona/config checks passed, plus Python
  compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-03: Validate ThreadKeeper gateway authentication candidates at
  commit `91f40f7`. Auth candidates are no longer string-coerced: when gateway
  auth is configured, non-string, empty, over-4-KiB, invalid-Unicode, ASCII
  control, line-separator, and bidi-control values fail before request
  construction. Seven focused provider-free auth checks passed, plus Python
  compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

- [ ] 2026-08-03: Execute ProtoCosmo2 Phase 5 as a frozen, offline shadow
  evaluation. The redacted content-addressed suite and provider-free preflight
  are complete: 10 cases cover recall/provenance, source precedence, safety
  refusals, routing/loop suppression, unavailable-tool honesty, Hyperon/PeTTa,
  and experiment planning; all 7 critical controls and 9 categories passed
  structural validation. Acceptance for behavioral fidelity is still pending:
  run the unchanged suite through both agents under a separately approved,
  isolated provider configuration; preserve paired redacted answers/tool traces
  and score accuracy, provenance, policy, continuity, tool correctness,
  concision, latency, and cost. No outbound channel/provider was started.
  Evidence: `experiments/20260803T203107Z-protocosmo2-phase5-shadow-preflight/`.
  The paired harness and composed runtime prompt are now accepted offline:
  `protocosmo2/tools/phase5_shadow_runner.py` requires an explicit `--execute`,
  loopback endpoint, separate ZeroBot/ProtoCosmo2 session IDs, and
  `outbound_channels: disabled`. Evidence:
  `experiments/20260803T214622Z-protocosmo2-phase5-harness/`. A
  model-approved execution was attempted with `openai/gpt-5.6-terra`, but the
  nested gateway CLI runner hung before producing a first paired artifact; do
  not treat the configuration as a behavioral result. Evidence:
  `experiments/20260804T032814Z-protocosmo2-phase5-shadow-execution/`. Next
  command: run one frozen case through the CLI with a bounded timeout, inspect
  the result schema/latency, then repair the runner before a fresh full suite.
  Phase 6 remains blocked.
  A 2026-08-04 real-runtime repair proved the gateway CLI itself responsive
  and exposed pinned-checkout routing, host dependency/policy, embedding, and
  mock-transport defects. The first four were repaired; the MeTTa loop now
  records `(send ...)` commands, but mock delivery returns `False`, and a clean
  retry produced no turn before timeout. Acceptance remains unmet; next
  command is a minimal pinned-Core/Test-provider mock-RPC acknowledgement
  reproduction. Evidence:
  `experiments/20260804T060000Z-protocosmo2-phase5-real-runtime-repair/`.
  A follow-up one-case gate repaired the driver’s unread-stdout deadlock risk,
  process-group cleanup, and missing project-scoped `py_landlock` dependency
  path; it then captured a real mock-delivered frozen-case answer in 17.3 s.
  The PeTTa/OmegaClaw process emitted `fatal signal 11 (segv)` immediately
  afterward, so this is not a stable runtime pass and the ten-case suite must
  not be scored. Next command: reproduce that SIGSEGV with the smallest
  pinned Test-provider/mock-channel loop and collect terminal evidence.
  Evidence: `experiments/20260804T061920Z-protocosmo2-phase5-mock-rpc-gate-dependency-repair/`.
  Follow-up controls show the Test provider (including Unicode) and a minimal
  embedded-Python subprocess tear down cleanly, whereas the real OpenClaw
  response consistently reaches the mock then SIGSEGVs. Suppressing no-input
  calls and relocating CLI launch into a loopback-only host bridge did not
  eliminate the crash. Next command: replay the exact real-response bytes
  against a fresh disposable OmegaClaw history/Chroma copy to distinguish a
  response/history-state defect from the live model route. Evidence:
  `experiments/20260804T064116Z-protocosmo2-phase5-test-provider-segv-reproduction/`,
  `20260804T064434Z-protocosmo2-phase5-only-new-input-real-gate/`, and
  `20260804T064606Z-protocosmo2-phase5-loopback-bridge-real-gate/`.

- [x] 2026-08-03: Independently review Capacity 1.1 request-to-contract
  coverage v0.2. A content-bound checker imports no producer code and confirms
  the GoalChainer offline/live authority pair, mixed analysis/activation
  fail-closed case, semantic paraphrase equivalence, and retained
  `no_dispatch` controls. Exact replay and eight provider-free negative tests
  pass. Evidence:
  `artifacts/ggb-capacity-gates/20260803-request-to-contract-coverage-v02-independent-review/`.
  Next: define only a strict provider-free generator interface contract; no
  generator implementation or runtime effect is authorized.

- [x] 2026-08-03: Harden ThreadKeeper local-dashboard pricing override opens
  at commit `e09b284`. The bounded override reader now opens with no-follow
  semantics and requires a regular-file descriptor, preventing symlink and
  non-regular substitution from influencing accounting. Forty-three focused
  provider-free local-channel checks passed, plus Python compilation,
  `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-03: Harden ThreadKeeper local-dashboard reasoning-history opens
  at commit `ee6f671`. The bounded incremental reader now opens with no-follow
  semantics, requires a regular-file descriptor, and obtains file size from
  the descriptor it reads, preventing symlink/non-regular substitution and
  stale path metadata from selecting the read window. Fifty-four focused
  provider-free local-channel checks passed, plus Python compilation,
  `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-03: Preregister Capacity 1.1 request-to-contract coverage v0.2.
  Five sealed cases add the four elements required by the independent review:
  an offline/live GoalChainer minimal pair, a mixed analysis-plus-activation
  request that remains `decision_required`, a semantic paraphrase pair, and
  exact unordered invariant scoring. Exact replay and seven provider-free
  negative tests pass. Evidence:
  `artifacts/ggb-capacity-gates/20260803-request-to-contract-coverage-v02/`.
  Next: independent holdout review; no generator or runtime effect is
  authorized.

- [x] 2026-08-03: Harden ThreadKeeper local-dashboard avatar file opens at
  commit `aff7eb8`. The bounded reader now opens with no-follow semantics and
  verifies the opened descriptor is a regular file, preventing symlink
  substitution or non-regular inputs from being served. Fifty focused
  provider-free local-channel checks passed, plus Python compilation,
  `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-03: Keep ThreadKeeper durable transcript retention bounded at
  commit `9bbcf0f`. Transcript turn, per-field, and summary limits now use
  finite defaults and clamp configured or runtime zero to one, preventing a
  local setting from restoring unbounded persistent worker history. All 1,112
  focused provider-free subagent checks passed, plus Python compilation,
  `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-03: Independently review Capacity 1.1 fixture discrimination.
  The content-bound replay confirms two bounded positives and one live-effect
  negative, but fails the set closed before generator-interface work because
  it lacks a same-domain GoalChainer minimal pair, mixed bounded/live request,
  semantic paraphrase pair, and invariant-based equivalent-contract scoring.
  Six provider-free checks pass. Evidence:
  `artifacts/ggb-capacity-gates/20260803-request-to-contract-discrimination-review/`.
  Next: preregister those four coverage elements; no generator or runtime
  effect is authorized.

- [x] 2026-08-03: Bind ThreadKeeper run-index tail sizing and content to one
  opened descriptor at commit `159d0f4`. The bounded scanner now derives file
  size with `fstat` after its no-follow regular-file open, preventing an atomic
  path replacement from selecting the wrong tail and silently forking the
  audit hash chain. Thirty-two focused provider-free checks passed, plus
  Python compilation, `git diff --check`, and draft PR #1 safety-floor
  ancestry.

- [x] 2026-08-03: Close ThreadKeeper's knowledge-prior file-open race at
  commit `8ac4294`. The bounded reader now uses a no-follow open and requires
  the opened descriptor to be a regular file before reading, preventing a
  symlink swap or non-regular input from reaching embedding or collection
  mutation. Eight focused provider-free checks passed, plus Python
  compilation, `git diff --check`, and draft PR #1 safety-floor ancestry.

- [x] 2026-08-03: Preregister the first capacity 1.1 request-to-contract
  fixture set before any generator implementation. Three content-bound cases
  cover record-only roadmap work, PR-#1-safe artifact work, and a live
  GoalChainer auto-dispatch control that must remain `decision_required`.
  Seven provider-free tests reject request drift, duplicate JSON, missing
  fields, path escape, authority widening, and unsafe reclassification.
  Evidence: `artifacts/ggb-capacity-gates/20260803-request-to-contract-preregistration/`.
  Next: independent fixture-discrimination review; no generator or runtime
  effect is authorized.

- [x] 2026-08-03: Make ThreadKeeper workspace write/append directory creation
  crash-durable at commit `49097a5`. Each newly created nested parent is now
  parent-fsynced before the atomic file replacement below it, closing a gap
  that file fsync plus final-parent fsync alone did not cover. Five focused
  provider-free checks passed, plus Python compilation, `git diff --check`,
  and draft PR #1 safety-floor ancestry.

- [ ] 2026-08-02: Lead ProtoCosmo2 Phase 2 as the source agent: provision a
  clean, detached, mock-only baseline from the frozen OmegaClaw-Core/PeTTa/
  ChromaDB commits, verify commit ancestry plus declared dependencies, and run
  only an offline smoke with all provider, Telegram, listener, and supervisor
  settings refused. Acceptance: a reproducible experiment receipt records
  clean detached commits, tool versions, and a passing intended invariant;
  no live capability is configured or invoked. Next command: inspect the
  pinned repositories and build scripts, then clone exact commits into the
  separate `protocosmo2/phase2/` tree. Evidence:
  `experiments/<new-protocosmo2-phase2-run>/RUN.md`.
  Progress: the clean detached baseline, PeTTa smoke, and mock transport
  rerun passed. The initial mock runner remains recorded as an expected
  Docker-cleanup mismatch. Next: define and test the Core mock-loop identity
  adapter; do not configure a provider or real channel.

- [x] 2026-08-02: Strictly validate ThreadKeeper's direct Agentverse bridge
  arguments at commit `ae8eeac`. Remote search queries and market tickers now
  require nonempty exact strings within dedicated bounds; tickers use a closed
  1-32 character symbol grammar, and caller-supplied timeouts require exact
  integers from 1 through 120 seconds. Invalid inputs fail before request-model
  construction or remote dispatch. Nine focused provider-free checks passed,
  plus Python compilation, `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-08-02: Freeze ProtoCosmo2 Phase 0 and capture Phase 1's sanitized
  read-only source snapshot. The candidate baseline records exact component
  commits but requires clean detached re-clones in Phase 2. The manifest
  initially failed closed on an over-broad filename policy and a symlink;
  corrected rules then captured 639 SHA-256-bound 0400 files, with 13 explicit
  exclusions, and an independent full hash/permission verification passed.
  Evidence: `docs/protocosmo2-phase0-freeze-2026-08-02.md`,
  `docs/protocosmo2-phase1-manifest.py`, and
  `experiments/20260803T045142Z-protocosmo2-phase1-sanitized-snapshot-rerun/`.
  Next: create the isolated mock-only ProtoCosmo2 checkout from clean detached
  candidate commits; no token, provider, Telegram, or network listener.

- [x] 2026-08-02: Audit the first ThreadKeeper GGB gate's task contract. A
  content-bound provider-free checker verifies objective, allowed paths,
  forbidden actions, done criteria, compute bounds, rollback, and the recorded
  PR #1/safety boundaries. Source drift, missing requirements, duplicate JSON,
  and authority widening fail closed; five tests pass. Evidence:
  `artifacts/ggb-capacity-gates/20260803-threadkeeper-task-contract-record-audit/`.
  Next: preregister request-to-contract fixtures; this does not establish
  free-form task-framing quality or authorize dispatch/runtime effects.

- [x] 2026-08-02: Bound ThreadKeeper local usage-accounting recall at commit
  `0bcea38`. Dashboard reads now stop at 64 MiB total or 64 KiB per JSONL
  record and open the ledger through a no-follow descriptor that must be a
  regular file. Oversized files/records and symlinks fail before further
  parsing. Forty-one focused provider-free checks passed, plus Python
  compilation, `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-08-02: Freeze the motivation feature-unit evidence receipt. The
  compact verifier content-binds the preregistration fixture/validator/report
  and independent replay/report, recomputes both reports, and requires exact
  semantic-registry and candidate-only authority agreement. Five
  provider-free tests pass. Evidence:
  `artifacts/ggb-capacity-gates/20260803-motivation-feature-unit-schema-evidence-receipt/`.
  No runtime feature defaults, memory writes, GoalChainer integration, or
  ThreadKeeper effects are authorized. Next: stop this schema lane for
  adjudication before proposing a versioned runtime-facing feature contract.

- [x] 2026-08-01: Bound ThreadKeeper episode-history recall at commit
  `49dfb6c`. Timestamp recall now reads at most 64 MiB plus one
  growth-detection byte through a no-follow regular-file descriptor; oversized
  and symlink inputs fail before history scanning. Nineteen focused
  provider-free checks passed, plus Python compilation, `git diff --check`,
  and PR #1 safety-floor ancestry.

- [x] 2026-08-01: Produce and post a detailed PDF review draft of the
  ProtoCosmo2 migration plan, clarifying that ZeroBot/ProtoCosmoBot are the
  same source agent and incorporating the Protomega review: immutable archive
  plus indexed provenance, per-instance runtime paths, prompt contract,
  bounded `continue-thinking`, and commit re-verification. Acceptance:
  searchable PDF generated and delivered to Protobots. Evidence:
  `docs/protocosmo2-migration-plan-2026-08-01.pdf`; Telegram message 15772.
  Next: await Ben's approval, then begin only the Phase 0 freeze and Phase 1
  audited manifest.

- [x] 2026-08-01: Draft a detailed, reviewable ZeroBot/OpenClaw to
  ProtoCosmo2/OmegaClaw port plan covering sanitized provenance-preserving
  state capture, identity/policy and skill translation, idempotent memory
  import, behavioral fidelity tests, isolated Telegram canaries, dual-run
  operation, rollback, and post-baseline OmegaClaw feature gates. Acceptance:
  plan is durable and suitable for Ben and Protomegabot review. Evidence:
  `docs/protocosmo2-port-plan-2026-08-01.md`. Next: incorporate Protomegabot's
  review and freeze the Monday execution spec before runtime changes.

- [x] 2026-08-01: Independently replay the motivation feature-unit schema. A
  strict provider-free consumer reconstructs the exact semantic/unit registry
  without importing the preregistration validator and rejects duplicate or
  non-finite JSON, malformed features, authority widening, and the
  equal-dimensional competence/uncertainty semantic swap. Five tests pass.
  Evidence: `artifacts/ggb-capacity-gates/20260801-motivation-feature-unit-schema-independent-replay/`.
  Candidate-only; no runtime default or ThreadKeeper effect is authorized.
  Next: freeze a compact evidence receipt binding preregistration and replay.

- [x] 2026-08-01: Verify ThreadKeeper audit sync directory descriptors at
  commit `ee84d23`. Both the shared subagent audit helper and the separate
  budget/accounting helper now decline to fsync a non-directory descriptor if
  parent substitution occurs or `O_DIRECTORY` is unavailable. Four focused
  provider-free checks passed, plus Python compilation, `git diff --check`,
  and PR #1 safety-floor ancestry.

- [x] 2026-08-01: Close a ThreadKeeper atomic-write metadata-sync race at
  commit `8f54d7c`. The shared audit parent-directory fsync now uses
  `O_NOFOLLOW` where available, so a directory replaced by a symlink after
  validation is not followed during the final durability sync. Four focused
  provider-free checks passed, plus Python compilation, `git diff --check`,
  and PR #1 safety-floor ancestry.

- [x] 2026-08-01: Preregister the motivation feature-unit schema after the
  per-field affine replay. Each score field now binds an explicit quantity,
  dimension, and unit; an equal-dimensional competence/uncertainty swap fails
  closed, showing units alone cannot substitute for semantic identity. Five
  provider-free tests pass. Evidence:
  `artifacts/ggb-capacity-gates/20260801-motivation-feature-unit-schema/`.
  Candidate-only; no runtime default or ThreadKeeper effect is authorized.
  Next: independent replay before freezing a feature schema.

- [x] 2026-08-01: Make newly created ThreadKeeper budget/accounting audit
  directory trees crash-durable at commit `4d7ea1c`. Each new symlink-safe
  ancestor is now parent-fsynced before usage or escalation records are
  appended below it. Twenty-five focused provider-free checks passed, plus
  Python compilation, `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-08-01: Make newly created ThreadKeeper audit directory trees
  crash-durable at commit `32842a6`. The shared symlink-safe directory creator
  now fsyncs each new directory entry before queue, transcript, sidecar, index,
  or other audit files are created beneath it. Nine focused provider-free
  checks passed, plus Python compilation, `git diff --check`, and PR #1
  safety-floor ancestry.

- [x] 2026-08-01: Bind ThreadKeeper checksum sidecars to their exact target at
  commit `aa87439`. The strict sidecar parser now rejects filename mismatch,
  extra/trailing records, malformed format, and invalid UTF-8 before queue or
  transcript integrity decisions. Forty-eight focused provider-free checks
  passed, plus Python compilation, `git diff --check`, and PR #1 safety-floor
  ancestry.

- [x] 2026-07-31: Make ThreadKeeper persistent run-index creation
  crash-durable at commit `38c48aa`. Each fsynced index append now also fsyncs
  its parent directory, preserving a newly created `index.jsonl` across a
  crash/power loss boundary. Two focused provider-free checks passed, plus
  Python compilation, `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-07-31: Freeze the structural chemistry transfer evidence receipt.
  It content-binds the sealed larger-shape preregistration and independent
  runner plus all four exact selections and score maps. Five provider-free
  checks reject artifact/replay drift, duplicate JSON, and authority widening.
  Evidence: `artifacts/ggb-capacity-gates/20260731-chemistry-structural-transfer-evidence-receipt/`.
  Next: stop this chemistry lane for adjudication; no chemistry execution,
  scheduling, policy/runtime/ThreadKeeper change, or other effect is authorized.

- [x] 2026-07-31: Make ThreadKeeper queued-task state transitions
  crash-durable at commit `26a8e20`. Claim, `.done`, and `.failed` renames now
  fsync their parent directory before proceeding. Three focused provider-free
  checks passed, plus Python compilation, `git diff --check`, and PR #1
  safety-floor ancestry.

- [x] 2026-07-31: Bound ThreadKeeper RAG knowledge-prior reads at commit
  `ce9c2b1`. Each Markdown input is limited to 2 MiB plus one detection byte;
  oversized, invalid-UTF-8, non-regular, and symlink inputs fail before
  embedding or stored-collection mutation. Six focused provider-free checks
  passed, plus Python compilation, `git diff --check`, and PR #1 hardening
  ancestry.

- [x] 2026-07-31: Independently replay the preregistered structural chemistry
  transfer fixture. A content-bound, provider-free implementation reproduces
  all four larger RAF-shape selections and exact score maps without importing
  prior scorer code. Six checks cover sealed identity, duplicate JSON,
  malformed/derived features, exact scores, and authority widening. Evidence:
  `artifacts/ggb-capacity-gates/20260731-chemistry-structural-transfer-independent-replay/`.
  Next: freeze a compact transfer evidence receipt; no chemistry execution,
  scheduling, policy/runtime/ThreadKeeper change, or other effect is authorized.

- [x] 2026-07-31: Bound ThreadKeeper local-dashboard avatar reads at commit
  `c791766`. The static
  PNG endpoint now reads at most 2 MiB plus one detection byte and rejects
  oversized or behavior-bearing byte bodies before writing response headers.
  Forty-four focused provider-free checks passed, plus Python compilation,
  `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-07-31: Bound ThreadKeeper local `/send` request bodies at commit
  `77c014c`. The producer boundary now rejects ambiguous, negative, typed, and
  over-64-KiB `Content-Length` values before reading the body. Forty focused
  provider-free checks passed, plus Python compilation, `git diff --check`,
  and PR #1 safety-floor ancestry.

- [x] 2026-07-31: Preregister a structurally different chemistry transfer
  fixture. Four sealed synthetic holdouts combine an 80-rule sparse core and a
  40-rule whole-system core with absent or partial no-catalysis RAFs, while
  binding the frozen score-policy identity and candidate-only authority. Six
  provider-free contract checks pass; no scorer or chemistry run is included.
  Evidence: `artifacts/ggb-capacity-gates/20260731-chemistry-structural-transfer-preregistration/`.
  Next: separately bind an independent replay; no policy change, experiment
  scheduling, chemistry execution, or ThreadKeeper effect is authorized.

- [x] 2026-07-31: Bound ThreadKeeper local-dashboard pricing override reads at
  commit `a6fd94e`. Operator-selected JSON files are read only to 64 KiB plus
  one detection byte; oversized and invalid UTF-8 files fail closed to built-in
  pricing. Twenty-five focused provider-free checks passed, plus Python
  compilation, `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-07-31: Harden ThreadKeeper bootstrap channel API parsing at commit
  `5d820c8`. Telegram and Slack credential checks now read at most 2 MiB plus
  one detection byte and reject invalid UTF-8, duplicate keys, non-standard
  numbers, non-object roots, and non-boolean success markers. Twelve focused
  provider-free checks passed, plus Python/shell compilation, `git diff
  --check`, and PR #1 safety-floor ancestry.

- [x] 2026-07-31: Freeze the chemistry candidate-scoring evidence receipt.
  It binds the read-only adapter, sealed preregistration, independent runner,
  and all four exact replay selections and score maps. Five provider-free
  checks reject artifact/replay drift, duplicate JSON, and authority widening.
  Evidence:
  `artifacts/ggb-capacity-gates/20260731-chemistry-candidate-scoring-evidence-receipt/`.
  Next: preregister one structurally different chemistry fixture; no chemistry
  run, experiment scheduling, ThreadKeeper effect, or runtime change is
  authorized.

- [x] 2026-07-31: Bound ThreadKeeper local-dashboard reasoning-history reads
  at commit `7cafd70`. Caller-supplied incremental offsets can no longer cause
  an unbounded history suffix read; each request reads at most 64 KiB and
  advances an exact byte offset. Twenty-five focused provider-free checks
  passed, plus Python compilation, `git diff --check`, and PR #1 safety-floor
  ancestry.

- [x] 2026-07-31: Keep ThreadKeeper escalation-policy and persona-prompt read
  caps fail-closed at commit `aa2f188`. Configured or runtime zero now clamps
  to one byte, preventing setup-time integrity reads from becoming unbounded.
  Five focused provider-free checks passed, plus Python compilation,
  `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-07-31: Independently execute the sealed chemistry candidate-score
  policy. The content-bound provider-free runner reproduces all four holdouts,
  derives scores only from four admitted raw features, and rejects contract
  mutation, duplicate JSON keys, malformed/derived inputs, inadmissible
  relations, and authority widening. Six tests pass. Evidence:
  `artifacts/ggb-capacity-gates/20260731-chemistry-candidate-scoring-independent-runner/`.
  Results remain candidate-only and adjudication-required; no chemistry run,
  experiment scheduling, or ThreadKeeper effect is authorized. Next: freeze a
  compact evidence receipt binding adapter, preregistration, runner, and the
  four replay results before considering any new chemistry fixture.

- [x] 2026-07-31: Keep ThreadKeeper run-audit read caps fail-closed at commit
  `cf9b97c`. Configured or runtime zero now clamps to one byte for both the
  run index and referenced transcripts, preventing the read-only verifier
  from restoring unbounded scans or hash reads. Seventeen focused
  provider-free verifier checks passed, plus Python compilation,
  `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-07-31: Keep ThreadKeeper workspace file-write caps fail-closed at
  commit `4bfe047`. Configured or runtime zero now clamps to one character,
  preventing `append-file` from restoring an unbounded existing-file read and
  both file tools from restoring unbounded output. Five focused provider-free
  checks passed, plus Python compilation, `git diff --check`, and PR #1
  safety-floor ancestry.

- [x] 2026-07-31: Preregister the chemistry candidate-scoring holdout. The
  contract binds the existing read-only RAF adapter, three fixed candidates,
  exact integer features/formulas, conservative tie breaking, four synthetic
  holdouts, and candidate-only authority. Seven provider-free checks pass.
  Evidence:
  `artifacts/ggb-capacity-gates/20260731-chemistry-candidate-scoring-preregistration/`.
  No scorer or chemistry run was implemented. Next: a separately bound
  independent runner; no experiment scheduling or ThreadKeeper effect.

- [x] 2026-07-31: Keep ThreadKeeper's native-provider response-body cap
  fail-closed at commit `1a1cde3`. A configured zero now clamps to one byte
  rather than selecting an unbounded `read()`. Three focused provider-free
  checks passed, plus Python compilation, `git diff --check`, and PR #1
  safety-floor ancestry.

- [x] 2026-07-30: Bound ThreadKeeper Slack Web API response parsing at commit
  `7d61846`. Reads are capped at 2 MiB plus one detection byte; oversized and
  behavior-bearing byte bodies fail closed before UTF-8 decoding or strict
  JSON parsing. Ten focused provider-free checks passed, plus Python
  compilation, `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-07-30: Implement the cross-project frontier's read-only chemistry
  evidence adapter. It binds the pinned `petta-chem` rich-RAF digest and emits
  three fixed, adjudication-required planning candidates without selecting or
  executing one. Mutation and incomplete/unpinned evidence fail to review
  before candidate emission. Five provider-free tests, Python compilation,
  and `git diff --check` pass. Evidence:
  `artifacts/ggb-capacity-gates/20260730-chemistry-evidence-adapter/`. Next:
  preregister a candidate-scoring holdout; no chemistry run or ThreadKeeper
  effect is authorized.

- [x] 2026-07-30: Bound ThreadKeeper Mattermost REST response parsing at
  commit `9308010`. Bodies over 2 MiB and non-exact byte/string body types now
  fail closed before UTF-8 decoding or strict JSON parsing. Thirteen focused
  provider-free checks passed, plus Python compilation, `git diff --check`,
  and PR #1 safety-floor ancestry.

- [x] 2026-07-30: Bound ThreadKeeper Agentverse/Tavily response formatting at
  commit `349b990`. Responses over 1,000,000 characters and behavior-bearing
  string subclasses now fail closed before strict JSON decoding. Five focused
  provider-free checks passed, plus Python compilation, `git diff --check`,
  and PR #1 safety-floor ancestry.

- [x] 2026-07-30: Bound ThreadKeeper gateway authentication response bodies at
  commit `2908572`. `/auth/status` and `/auth/verify` responses larger than
  64 KiB now fail closed before UTF-8 decoding or strict JSON parsing.
  Thirty-three focused provider-free channel checks passed, plus Python 3
  compilation, `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-07-30: Review OmegaBuzz v0.1 as an implementation proposal and preserve it with source provenance. Acceptance: identify its strongest design decisions, critical implementation seams, a phased first-slice correction, and evidence references; completed in Bot Philosophy review and `library/omegabuzz-design-proposal/SOURCE.md`.

- [x] 2026-07-30: Bound ThreadKeeper Telegram API response bodies at commit
  `80583c1`. Responses larger than 2 MiB now fail before UTF-8 decoding or
  strict JSON parsing, preventing unbounded producer-boundary allocation.
  Twenty-eight focused provider-free checks passed, plus Python 3 compilation,
  `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-07-30: Strictly validate ThreadKeeper Telegram display-name fields
  at commit `a90d3e7`. Optional username, first/last name, and chat-title
  values now require exact JSON-derived strings at the `getUpdates` producer
  boundary, before polling-offset mutation. Twenty-seven focused provider-free
  checks passed, plus Python 3 compilation, `git diff --check`, and PR #1
  safety-floor ancestry.

- [x] 2026-07-30: Strictly validate nested ThreadKeeper Telegram message fields
  at commit `703b60a`. Present `message`/`edited_message`, text, chat/from
  objects, and actor IDs now require exact JSON-derived types at the
  `getUpdates` producer boundary, before polling-offset mutation. Twenty-one
  focused provider-free checks passed, plus Python 3 compilation,
  `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-07-30: Strictly validate ThreadKeeper Telegram `getUpdates`
  envelopes at commit `1f823b1`. Wrong-shaped result/update records and
  missing, boolean, negative, or string update IDs now fail before polling
  offset mutation. Thirteen focused provider-free checks passed, plus Python
  3 compilation, `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-07-30: Require exact ThreadKeeper final `emit` payload strings at
  commit `b3127ad`. Behavior-bearing string subclasses now fail before
  whitespace, Unicode, or control-character inspection. Three focused
  provider-free checks passed, plus Python 3 compilation, `git diff --check`,
  and PR #1 safety-floor ancestry.

- [x] 2026-07-30: Reject non-finite ThreadKeeper bounded queue-drain returns at
  commit `ef2f593`. The parent-facing structured envelope now emits strict
  standard JSON or fails closed. Eleven focused provider-free checks passed,
  plus Python 3 compilation, `git diff --check`, and PR #1 safety-floor
  ancestry.

- [x] 2026-07-30: Require exact ThreadKeeper command-normalizer input at
  commit `4aa87bc`. Non-strings and behavior-bearing string subclasses now
  fail before replacement, splitting, or tool-command parsing. Seventeen
  focused provider-free checks passed, plus Python compilation,
  `git diff --check`, and PR #1 safety-floor ancestry.

- [x] 2026-07-30: Reject non-finite ThreadKeeper operator worker-loop and
  run-index returns at commit `b4522b7`. Producer-side strict JSON now matches
  the runner's strict consumer boundary, so `NaN`/`Infinity` cannot cross the
  structured operator interface. Thirty-four focused provider-free checks
  passed, plus Python compilation, `git diff --check`, and PR #1 safety-floor
  ancestry.

- [x] 2026-07-29: Reject non-finite ThreadKeeper structured parent-return
  metadata at commit `347dce1`. All normal and size-reduced serialization
  paths now emit strict standard JSON or fail closed. Three focused
  provider-free checks passed, plus Python compilation and `git diff --check`.

- [x] 2026-07-29: Strictly validate ThreadKeeper budget/escalation config at
  commit `706bccc`. Wrong-shaped budget sections plus boolean, negative,
  out-of-range, and non-finite numeric controls/rates now fall back field by
  field to conservative defaults before accounting or escalation decisions.
  Twenty-four focused provider-free checks passed, plus Python compilation and
  `git diff --check`.

- [x] 2026-07-29: Strictly validate ThreadKeeper supervised worker-loop results
  at commit `27bb41a`. The operator entrypoint now rejects duplicate keys,
  non-standard `NaN`/`Infinity` tokens, and non-object roots before emitting a
  structured result; pretty output also uses strict JSON serialization. Six
  focused provider-free checks passed, plus Python compilation and
  `git diff --check`.

- [x] 2026-07-29: Add a fail-closed motivational dataset materialization
  preflight. It binds the reviewed generator, exact 64/32 split, disjointness,
  and zero fitting/memory/ThreadKeeper/provider/Telegram/runtime authority.
  Six provider-free tests pass; the 2026-07-30 19:33 UTC replay confirmed
  direct execution exits `3` while approval is pending. Next: Ben decision on
  deterministic materialization only.

- [x] 2026-07-29: Reject non-finite local HTTP JSON responses at ThreadKeeper
  commit `b099bab`. Response serialization now fails before headers/body are
  committed when a payload contains `NaN` or infinity. Twenty-three focused
  provider-free checks passed, plus Python compilation and `git diff --check`.

- [ ] 2026-07-29: Execute the approved ProtoMegaBot2 staging launch using the
  existing local credential configuration. Ben explicitly withdrew the prior
  credential-rotation/attestation prerequisite. Acceptance: a bounded staging
  deployment has an operator-visible startup/health record and rollback path;
  it must not expose, copy, log, or otherwise alter the credential. Next:
  inspect the ProtoMegaBot2 staging launcher and run its documented preflight.

- [x] 2026-07-29: Close ThreadKeeper's low-level tool-argument type seam at
  commit `d929440`. Tool names, argument containers, and argument values now
  require exact built-in `str`/`list` types before behavior-bearing operations.
  Twenty-one focused provider-free checks passed, plus Python compilation and
  `git diff --check`.

- [x] 2026-07-29: Independently reviewed the non-materializing motivation
  score-policy v0.2 generator primitives. The review binds the implementation
  and v2 preregistration, matches two OpenSSL SHA-256 vectors, checks all four
  transform families over boundary probes, and verifies retry/exhaustion and
  invalid-input behavior. Six provider-free checks pass. No dataset, fitting,
  memory, provider, Telegram, ThreadKeeper, or runtime authority was granted.
  Next: Ben decision before any sealed 64/32 split materialization.

- [x] 2026-07-29: Make queued-worker completion transactional with strict
  result serialization at ThreadKeeper commit `9226fb6`. The worker now
  preflights the complete result record before renaming a claim to `.done`;
  invalid/non-finite metadata is retained through the existing `.failed`
  record and sidecar path. Thirty-one focused provider-free checks passed,
  along with Python compilation and `git diff --check`.

- [x] 2026-07-29: Reject non-finite ThreadKeeper persistent run records at
  commit `b75ec16`. Transcript JSON, run-index hashing/appends, and index
  rotation now emit strict standard JSON; invalid state fails before atomic
  replacement or append and leaves the last valid record intact. Thirty-two
  focused provider-free checks passed, along with Python compilation and
  `git diff --check`.

- [x] 2026-07-29: Preserve valid ThreadKeeper supervised-worker lock metadata
  on serialization failure at commit `6bcfc12`. Metadata is now serialized as
  strict standard JSON before the live locked record is truncated, so invalid
  or non-finite state leaves the last valid operator-visible record intact.
  Three focused provider-free checks passed, along with Python compilation and
  `git diff --check`.

- [x] 2026-07-29: Preserve valid ThreadKeeper LLM guard state on serialization
  failure at commit `093cb00`. Quota/concurrency state is now serialized with
  strict standard JSON before the live locked file is truncated, so
  unserializable or non-finite data fails without destroying the last valid
  record. Eleven focused provider-free checks passed, along with Python
  compilation, `git diff --check`, and completed PR #1 safety-floor ancestry.

- [x] 2026-07-29: Independently review motivational score-policy v0.2
  synthetic-generator preregistration v2. The review closes R1--R4, binds the
  exact revision and policy oracle, exhaustively verifies all four declared
  candidate-witness regions, and checks both exact 799/800 boundary pairs.
  Seven provider-free checks pass at
  `artifacts/ggb-capacity-gates/20260729-motivation-score-policy-v02-generator-review-v2/`.
  No implementation, dataset materialization, fitting, memory write, provider,
  Telegram, or runtime change was authorized. Next: a separate provider-free
  generator implementation gate that does not materialize the preregistered
  dataset.

- [x] 2026-07-29: Reject non-finite ThreadKeeper audit-log records on commit
  `43521bb`. Budget usage/escalation and worker usage writers now serialize
  strict standard JSON, so `NaN`/`Infinity` cannot create records that the
  hardened readers must later discard. Three focused provider-free checks
  passed, along with Python compilation, `git diff --check`, and completed
  PR #1 safety-floor ancestry.

- [x] 2026-07-29: Serialize ThreadKeeper worker usage-log appends on commit
  `476a39c`. Worker accounting JSONL writes now take an exclusive
  cross-process lock around each complete write/flush/fsync sequence while
  preserving no-symlink and best-effort logging behavior. A four-process
  regression and five focused provider-free checks passed, along with Python
  compilation, `git diff --check`, and completed PR #1 safety-floor ancestry.

- [x] 2026-07-29: Serialize ThreadKeeper budget audit-log appends on commit
  `ee0f512`. Usage and escalation JSONL writers now take an exclusive
  cross-process lock around each complete write/flush/fsync sequence,
  preventing concurrent record interleaving while preserving fail-safe
  accounting behavior. A four-process regression test and fifteen focused
  provider-free checks passed, along with Python compilation,
  `git diff --check`, and completed PR #1 safety-floor ancestry.

- [x] 2026-07-28: Bound ThreadKeeper's episode-recall timestamp input on
  commit `f99a625`. The bridge now rejects timestamp strings longer than 23
  characters before normalization, parsing, or history-file reads while
  preserving plain, quoted, and MeTTa-escaped valid forms. Fourteen focused
  provider-free checks, Python compilation, `git diff --check`, and completed
  PR #1 safety-floor ancestry passed.

- [x] 2026-07-28: Independently review the motivational score-policy v0.2
  generator preregistration before implementation. The gate correctly binds
  its source and limits authority, but is `needs_revision`: template-family
  tuple semantics, digest rejection/counter advancement, deterministic
  coverage repair, and exact boundary-neighbor predicates are underspecified.
  Five provider-free review checks pass at
  `artifacts/ggb-capacity-gates/20260728-motivation-score-policy-v02-generator-review/`.
  No generator or data was produced. Next: revise the preregistration to close
  R1--R4, then repeat independent review before implementation.

- [x] 2026-07-28: Bound ThreadKeeper episode-recall scan memory on commit
  `53ebe6c`. `helper.around_time` now keeps only the current candidate window
  and a radius-bounded recent-line deque rather than retaining the full
  history file, while preserving nearest-timestamp and surrounding-line
  semantics. Eleven focused provider-free checks, Python compilation,
  `git diff --check`, and completed PR #1 safety-floor ancestry passed.

- [x] 2026-07-28: Close ThreadKeeper's episode-recall Python bridge argument
  boundary on commit `df20549`. `helper.around_time` now requires an exact
  timestamp string and exact integer radius bounded to 0--1000 before string
  operations or history reads. Nine focused provider-free checks, Python
  compilation, `git diff --check`, and completed PR #1 safety-floor ancestry
  passed.

- [x] 2026-07-28: Preregister the motivational score-policy v0.2 synthetic
  dataset generator and seed without implementing or executing it. The
  contract fixes SHA-256 counter sampling, split sizes, disjoint template
  families, cross-split tuple rejection, coverage obligations, confirmation
  sealing order, and zero execution authority. Eight provider-free checks
  pass at
  `artifacts/ggb-capacity-gates/20260728-motivation-score-policy-v02-generator-preregistration/`.
  No data was materialized and no fitting or runtime change was authorized.
  Next: independent review of generator completeness before implementation.

- [x] 2026-07-28: Close ThreadKeeper's persisted local usage-accounting type
  boundary on commit `447c6e7`. Usage records now require an exact object,
  exact model string, non-negative exact integer token counters, and a finite
  non-negative numeric timestamp before dashboard aggregation. Wrong-root,
  boolean, string, and negative accounting values are skipped without
  suppressing valid neighboring records. Twenty focused provider-free checks,
  Python compilation, `git diff --check`, and completed PR #1 ancestry passed.

- [x] 2026-07-28: Close ThreadKeeper's queued-worker result-envelope boundary
  on commit `c0b3c7d`. Direct queued execution, bounded draining, and the
  supervised worker loop now require strict JSON object results; duplicate
  keys, non-standard `NaN`/`Infinity`, and non-object roots fail closed before
  completion/error accounting or result persistence. Thirty-eight focused
  checks, Python compilation, `git diff --check`, and the 1077-test
  provider-free hardening suite passed.

- [x] 2026-07-28: Define the motivational score-policy v0.2 synthetic
  dataset contract without generating data or fitting. Calibration and
  confirmation identities and template families must be disjoint;
  confirmation labels stay sealed until a calibration candidate is frozen;
  both splits must cover all four candidates, boundary neighbors, and joint
  feature variation. Eight provider-free contract checks pass at
  `artifacts/ggb-capacity-gates/20260728-motivation-score-policy-v02-synthetic-dataset-contract/`.
  Candidate-only; no runtime, memory, ThreadKeeper, provider, or Telegram
  effect. Next: preregister a deterministic local generator and seed; do not
  materialize either split yet.

- [x] 2026-07-28: Close ThreadKeeper's local HTTP `/send` JSON boundary on
  commit `57c9ebf`. Request bodies now reject duplicate keys, non-standard
  `NaN`/`Infinity`, invalid UTF-8, non-object roots, and non-string
  `message`/`auth` fields before authentication or inbound processing.
  Eleven focused checks, Python compilation, `git diff --check`, completed
  PR #1 safety-floor ancestry, and the 1099-test provider-free hardening gate
  passed.

- [x] 2026-07-28: Close ThreadKeeper's Mattermost JSON boundary on commit
  `2dcab8e`. REST identity/profile responses and websocket event/post
  envelopes now reject duplicate object keys, non-standard `NaN`/`Infinity`,
  invalid UTF-8, and non-object roots before processing. Ten focused checks,
  Python compilation, `git diff --check`, and completed PR #1 safety-floor
  ancestry passed. A broad `Autotests/mock` invocation used an incomplete
  environment and was interrupted after unrelated failures; no full-suite
  claim is made.

- [x] 2026-07-28: Freeze the combined motivational score-policy v0.2
  evidence before any calibration proposal. The summary content-addresses the
  reachability, boundary, and joint-feature preregistration/execution pairs,
  recomputes 20 executed cases and four-candidate coverage, and verifies
  candidate-only, adjudication-required authority. Five provider-free checks,
  Python compilation, and strict JSON negative cases pass at
  `artifacts/ggb-capacity-gates/20260728-motivation-score-policy-v02-evidence-freeze/`.
  No calibration or runtime change. Next: draft a synthetic-only dataset
  contract with disjoint calibration/confirmation identities; do not fit.

- [x] 2026-07-28: Close ThreadKeeper's Slack Web API JSON boundary on commit
  `123d84e`. Responses now reject duplicate object keys, non-standard
  `NaN`/`Infinity`, invalid UTF-8, non-object roots, and non-boolean success
  markers before Slack response processing. Seven focused checks, Python
  compilation, `git diff --check`, completed PR #1 safety-floor ancestry, and
  the 1095-test provider-free hardening suite passed.

- [x] 2026-07-28: Close ThreadKeeper's local RPC JSON boundary on commit
  `80c7fa0`. Outer RPC envelopes and nested request/response payloads now
  reject duplicate object keys and non-standard `NaN`/`Infinity` tokens
  before dispatch or response delivery. Eight focused checks, Python
  compilation, `git diff --check`, completed PR #1 safety-floor ancestry, and
  the 1111-test provider-free hardening suite passed.

- [x] 2026-07-28: Independently execute the sealed motivational score-policy
  v0.2 joint-feature holdouts without importing their validator or prior
  runners. All seven selections reproduced while jointly varying all three
  admitted inputs. Six provider-free checks cover strict JSON, sealed/source
  identity, malformed and derived inputs, expectation/set drift, admission
  weakening, and authority widening at
  `artifacts/ggb-capacity-gates/20260728-motivation-score-policy-v02-joint-feature-independent-runner/`.
  Candidate-only; ThreadKeeper effect `none`; no calibration. Next: freeze a
  combined v0.2 evidence summary before proposing any calibration dataset.

- [x] 2026-07-28: Close ThreadKeeper's gateway-auth response JSON boundary on
  commit `802fadd`. Auth status and token-verification responses now reject
  duplicate object keys, non-standard `NaN`/`Infinity`, invalid UTF-8,
  non-object roots, and non-boolean decision markers before authentication
  state or token acceptance. Three focused checks, Python compilation,
  `git diff --check`, completed PR #1 safety-floor ancestry, and the 1103-test
  provider-free hardening suite passed.

- [x] 2026-07-28: Close ThreadKeeper's Agentverse/Tavily response JSON
  boundary on commit `900dc51`. Search responses now reject duplicate object
  keys and non-standard `NaN`/`Infinity` tokens before structured result
  extraction. Three focused checks, Python compilation, `git diff --check`,
  completed PR #1 safety-floor ancestry, and the 1100-test provider-free
  hardening suite passed.

- [x] 2026-07-28: Preregister the motivational score-policy v0.2 joint-feature
  holdout before further execution or calibration. Seven sealed out-of-sample
  cases vary all three admitted inputs together below the review override,
  probing inspect/answer and inspect/request rank changes, conservative review
  tie resolution, and near-override request selection. Eight provider-free
  contract checks pass at
  `artifacts/ggb-capacity-gates/20260728-motivation-score-policy-v02-joint-feature-preregistration/`.
  Candidate-only; ThreadKeeper effect `none`. Next: independently execute the
  sealed cases without importing this validator or prior runners.

- [x] 2026-07-28: Close ThreadKeeper's Telegram Bot API JSON boundary on
  commit `297f362`. API responses now reject duplicate object keys,
  non-standard `NaN`/`Infinity` tokens, invalid UTF-8, non-object roots, and
  non-boolean success markers before update/auth/message processing. Six
  focused checks, Python compilation, `git diff --check`, completed
  safety-floor ancestry, and the 1097-test provider-free suite passed.

- [x] 2026-07-27: Close ThreadKeeper's native-provider response JSON boundary
  on commit `edee61f`. Ollama-compatible responses now reject duplicate object
  keys and non-standard `NaN`/`Infinity` tokens as
  `provider_response_invalid` before worker output or token accounting.
  Four focused checks, Python compilation, `git diff --check`, completed
  safety-floor ancestry, and the 1091-test provider-free suite passed.

- [x] 2026-07-27: Independently execute the sealed motivational score-policy
  v0.2 boundary holdouts without importing their validator or prior runners.
  All eight exact/adjacent cases reproduced across the inspect/answer and
  inspect/request crossovers and the 799/800 review override. Five
  provider-free tests cover sealed/source identity, malformed and derived
  inputs, expectation/set drift, admission weakening, and authority widening
  at
  `artifacts/ggb-capacity-gates/20260727-motivation-score-policy-v02-boundary-independent-runner/`.
  Candidate-only; ThreadKeeper effect `none`; no calibration. Next:
  preregister a small out-of-sample suite varying two features jointly before
  considering any empirical calibration.

- [x] 2026-07-27: Close ThreadKeeper's local-channel accounting JSON boundary
  on commit `d726db4`. Pricing overrides and usage-ledger records now reject
  duplicate object keys and non-standard `NaN`/`Infinity` tokens before they
  influence displayed token or cost totals; valid neighboring JSONL records
  remain usable. Three focused checks, Python compilation, `git diff --check`,
  completed safety-floor ancestry, and the 1088-test provider-free hardening
  suite passed.

- [x] 2026-07-27: Close ThreadKeeper's persisted budget usage-ledger JSON
  boundary on commit `749cc91`. Duplicate object keys and Python's
  non-standard `NaN`/`Infinity` tokens are rejected per record rather than
  influencing token/cost accounting; valid neighboring JSONL records remain
  usable. Fourteen focused checks, Python compilation, `git diff --check`,
  completed safety-floor ancestry, and the 1085-test provider-free hardening
  suite passed.

- [x] 2026-07-27: Preregister the motivational score-policy v0.2 boundary
  holdout before any further execution or calibration. Eight sealed,
  out-of-sample cases distinguish exact and adjacent inspect/answer and
  inspect/request boundaries and the adjacent 799/800 review override where
  the override replaces an otherwise winning inspection action. Seven
  provider-free contract checks pass at
  `artifacts/ggb-capacity-gates/20260727-motivation-score-policy-v02-boundary-preregistration/`.
  Candidate-only; ThreadKeeper effect `none`. Next: independently execute the
  sealed cases without importing this validator or prior runners.

- [x] 2026-07-27: Close ThreadKeeper's persisted async-worker lock-metadata
  JSON boundary on commit `1bd8008`. Duplicate object keys and non-standard
  `NaN`/`Infinity` tokens now fail closed before stale-worker metadata is
  returned. Three new cases, six focused checks, Python compilation,
  `git diff --check`, completed safety-floor ancestry, and the 1084-test
  provider-free hardening suite passed.

- [x] 2026-07-27: Close ThreadKeeper's inline task-contract JSON boundary on
  commit `3779c9a`. JSON goal objects now reject duplicate object keys and
  Python's non-standard `NaN`/`Infinity` tokens as persistent
  `contract_invalid` results before escalation policy or worker/provider
  effects. Three new cases, seven focused checks, Python compilation,
  `git diff --check`, completed safety-floor ancestry, and the 1081-test
  provider-free hardening suite passed.

- [x] 2026-07-27: Independently execute the sealed motivational score-policy
  v0.2 reachability witnesses without importing its validator or prior
  runners. All five selections reproduce, all four registered candidates are
  reachable, and `evidence_gap` is recomputed solely from admitted inputs.
  Eight provider-free checks cover sealed identity, caller-supplied derived
  values, malformed scalars, policy/expectation drift, candidate
  unreachability, admission weakening, and authority widening at
  `artifacts/ggb-capacity-gates/20260727-motivation-score-policy-v02-independent-runner/`.
  Candidate-only; ThreadKeeper effect `none`. Next: preregister an
  out-of-sample v0.2 boundary suite around the new `inspect_evidence` region
  before calibration.

- [x] 2026-07-27: Close ThreadKeeper's persisted LLM quota-state JSON boundary
  on commit `d6b1b96`. Rate-limit and concurrency state now reject duplicate
  object keys and Python's non-standard `NaN`/`Infinity` tokens before quota
  reservation or provider effects, preserving the malformed evidence for
  diagnosis. Eight focused checks, Python compilation, `git diff --check`,
  completed safety-floor ancestry, and the 1083-test provider-free hardening
  suite passed.

- [x] 2026-07-27: Close ThreadKeeper's persona-config JSON boundary on commit
  `6f4f10d`. Persona files now reject duplicate object keys and Python's
  non-standard `NaN`/`Infinity` tokens before provider, model, tool,
  task-contract, or worker effects. Three new malformed-file cases, nine
  focused checks, Python compilation, `git diff --check`, completed
  safety-floor ancestry, and the 1077-test provider-free hardening suite
  passed.

- [x] 2026-07-27: Preregister motivational score-policy v0.2 as a
  candidate-only response to the independently reproduced v0.1 structural
  dominance result. The revision derives
  `evidence_gap = 1000 - evidence_sufficiency` from the three admitted inputs,
  forbids caller-supplied derived values, preserves the other candidate
  weights/tie order/review override, and seals witnesses making all four
  candidates reachable. Eight provider-free checks pass at
  `artifacts/ggb-capacity-gates/20260727-motivation-score-policy-v02-preregistration/`.
  ThreadKeeper effect `none`; no live behavior or calibration. Next:
  independently execute the sealed witnesses without importing this validator
  or prior runners.

- [x] 2026-07-27: Close ThreadKeeper's strict persisted-JSON boundary on
  commit `945de9e`. Duplicate object keys and Python-accepted `NaN`/`Infinity`
  tokens now fail closed across bounded queued-task/candidate-transcript reads
  and run-index append, rotation, and audit parsing. Five new focused cases,
  Python compilation, `git diff --check`, and the 1069-test provider-free
  hardening suite passed.

- [x] 2026-07-27: Close ThreadKeeper's persisted run-index entry boundary on
  commit `8669f16`. The read-only audit now requires an exact JSON object,
  exact strings for identity/status/path/hash fields, and finite numbers or
  null for timestamps before hashing, normalization, path resolution, or
  transcript reads. Malformed entries are reported as
  `invalid_index_entry:ValueError`. Fourteen focused checks and the 1064-test
  provider-free hardening suite passed.

- [x] 2026-07-27: Independently execute the sealed motivational score-policy
  feature-interaction suite without importing its validator or prior runners.
  All seven selections/reasons reproduce, including both crossovers, the
  conservative tie, and the review override. The runner also verifies directly
  from frozen coefficients and tie order that `inspect_evidence` is dominated
  across the valid domain. Eight provider-free checks pass at
  `artifacts/ggb-capacity-gates/20260727-motivation-score-policy-feature-interaction-independent-runner/`.
  Candidate-only; ThreadKeeper effect `none`; no calibration. Next: revise the
  candidate set under a new preregistered policy version if an independently
  selectable evidence-gathering action remains desired.

- [x] 2026-07-27: Close ThreadKeeper's persisted candidate-review field
  boundary on commit `4a141fd`. Decision-relevant transcript fields now
  require exact JSON object/list/string/boolean types before truth testing,
  slicing, or operator-facing review construction. Malformed patch proposals,
  adjudication metadata, task contracts, statuses, and summaries fail closed
  as `candidate_review_error`. Fifteen focused checks and the 1063-test
  provider-free hardening suite passed.

- [x] 2026-07-27: Close ThreadKeeper's parent/operator path-argument
  boundaries on commit `e834d39`. Run-index audit and candidate transcript
  review paths now require exact built-in strings, while worker stop-file
  controls require an exact built-in string or null, before truth testing,
  comparison, coercion, or filesystem path resolution. Behavior-bearing
  subclasses fail closed without acquiring the worker lock or touching the
  requested filesystem path. Eight focused checks and the 1054-test
  provider-free hardening suite passed.

- [x] 2026-07-27: Close ThreadKeeper's direct tool-runner control boundary on
  commit `9091e2e`. Call batches are exact-type checked before truth testing;
  allowed tool containers/items and optional quotas are exact-type checked
  before iteration, membership, comparison, or coercion. Behavior-bearing
  subclasses fail closed before any tool effect. Nine focused checks and the
  1051-test provider-free hardening suite passed.

- [x] 2026-07-27: Preregister an out-of-sample motivational score-policy
  feature-interaction suite without changing policy parameters. Seven sealed
  cases cover joint evidence/clarification pressure, the answer/defer
  crossover below/at/above equality, an answer/request tie, three high
  features, and the review override against a higher request score. The
  contract also records that `inspect_evidence` is structurally dominated by
  `defer_for_review` under v0.1 and therefore unreachable. Nine provider-free
  checks pass at
  `artifacts/ggb-capacity-gates/20260727-motivation-score-policy-feature-interaction-preregistration/`.
  Contract SHA-256:
  `1a7c0b3c60d9d3c66e3df415825b1a6b7fb5301cdd3df64d662ee6addfec258c`.
  Candidate-only; ThreadKeeper effect `none`. Next: independently execute the
  sealed suite without importing this validator or prior runners; do not
  calibrate from the result.

- [x] 2026-07-27: Independently execute the sealed motivational score-policy
  boundary holdout without importing its validator or the prior runner. All
  five preregistered selections and reasons reproduce, including conservative
  exact ties, the one-unit request advantage, and adjacent 799/800 override.
  Six provider-free checks pass at
  `artifacts/ggb-capacity-gates/20260727-motivation-score-policy-boundary-holdout-independent-runner/`.
  Candidate-only; ThreadKeeper effect `none`; no calibration. Next:
  preregister an out-of-sample feature-interaction suite before considering
  any score-policy parameter change.

- [x] 2026-07-26: Close ThreadKeeper's operator-facing queued-dispatch path
  boundary on commit `896a38e`. The path must be an exact non-empty built-in
  string; non-string values and behavior-bearing string subclasses return
  `queue_worker_error` before coercion, queue-directory access, task claim, or
  worker effects. Nine focused checks and the 1047-test provider-free
  hardening suite passed.

- [x] 2026-07-26: Preregister a discriminating motivational score-policy
  boundary holdout before calibration. The sealed five-case contract binds
  the policy and prior runner identities and tests four-way/request-review
  ties, a one-unit request advantage, and the adjacent 799/800 review-risk
  boundary. Eight provider-free checks pass at
  `artifacts/ggb-capacity-gates/20260726-motivation-score-policy-boundary-holdout-preregistration/`.
  Contract SHA-256:
  `a3d98d19a36132e130f8848fa0a8ef834f48a2ae5d2b26827520d5e9dfb30413`.
  Candidate-only; ThreadKeeper effect `none`. Next: independently execute the
  sealed holdout without importing its validator, and do not calibrate policy
  parameters from the result.

- [x] 2026-07-26: Close ThreadKeeper's direct-dispatch scalar boundary on
  commit `d8254ad`. Integer limits and goal/tool-subset/persona arguments must
  use exact built-in types; behavior-bearing subclasses return persistent
  `dispatch_args_invalid` records before overloaded operations, persona setup,
  or worker/provider calls. Five focused checks and the 1039-test provider-free
  hardening suite passed.

- [x] 2026-07-26: Close ThreadKeeper's bounded manual queue-drain quota
  boundary on commit `c16efa7`. `drain_queued_dispatches(max_tasks=...)`
  requires an exact non-negative built-in integer; malformed values and
  behavior-bearing integer subclasses return `worker_config_invalid` before
  queue enumeration or worker effects. Seven focused checks and the 1034-test
  provider-free hardening suite passed.

- [x] 2026-07-26: Close ThreadKeeper's supervised-worker numeric-bound
  boundary on commit `bb9cd07`. Explicit task, idle-poll, consecutive-error,
  poll-interval, and runtime limits must use exact built-in integer/float
  types; behavior-bearing subclasses fail closed before overloaded operations,
  lock acquisition, or queue effects. Two focused checks and the 1029-test
  provider-free hardening suite passed.

- [x] 2026-07-26: Close ThreadKeeper's persona-configuration boundary on
  commit `e67e05e`. Config containers, nested task contracts, scalar strings,
  output-token limits, and default tool lists/items must use exact built-in
  types; behavior-bearing subclasses fail closed during setup before worker or
  provider calls. Five focused checks and the 1015-test provider-free
  hardening suite passed.

- [x] 2026-07-26: Independently execute motivational score-policy v0.1
  without importing the preregistration validator. The runner binds the sealed
  preregistration and candidate-set identities, recomputes all candidate
  scores, reproduces the three registered selections, and exercises the
  review-risk override. Five provider-free checks pass at
  `artifacts/ggb-capacity-gates/20260726-motivation-score-policy-independent-runner/`.
  Candidate-only; ThreadKeeper effect `none`. Next: preregister a discriminating
  holdout set for tie-breaking and near-threshold behavior before calibration.

- [x] 2026-07-26: Close ThreadKeeper's durable queued-dispatch task boundary
  on commit `f0ed2da`. Queue record containers, scalar identity/control
  fields, tool lists/items, numeric limits, and nested contracts must use
  exact built-in types; behavior-bearing subclasses fail closed before queue
  execution or worker effects. Six focused checks and the 1010-test
  provider-free hardening suite passed.

- [x] 2026-07-26: Close ThreadKeeper's task-contract boundary on commit
  `5d964c6`. Contract mappings, objectives, list containers/items, quotas, and
  boolean policy fields must use exact built-in types; behavior-bearing
  subclasses fail closed before overloaded operations. Four focused checks and
  the 1017-test provider-free hardening suite passed.

- [x] 2026-07-26: Preregister motivational score-policy v0.1 separately from
  the frozen reachability evidence. The contract binds predecessor and
  candidate-set identities, scale-1000 integer arithmetic, three exact
  features, candidate weights, conservative tie breaking, a review-risk
  override, three holdouts, and candidate-only authority. Seven provider-free
  checks pass at
  `artifacts/ggb-capacity-gates/20260726-motivation-score-policy-preregistration/`.
  This is not implementation or calibration evidence. Next: implement an
  independent holdout runner without importing this validator.

- [x] 2026-07-26: Close ThreadKeeper's authenticated OpenAI-compatible
  `usage.total_tokens` boundary on commit `2886862`. The aggregate counter
  must be an exact built-in integer; behavior-bearing subclasses fail closed
  before overloaded comparison or arithmetic. Five focused checks and the
  1013-test provider-free hardening suite passed.

- [x] 2026-07-25: Close ThreadKeeper's authenticated OpenAI-compatible
  completion-metadata boundary on commit `dd251e8`. Completion object/model,
  finish reason, message role, choice index, choice containers, and SDK
  extra-field mappings must use exact built-in types. Behavior-bearing
  subclasses fail closed before overloaded comparison, length, or truth
  operations. Seven focused checks and the 1012-test provider-free hardening
  suite passed.

- [x] 2026-07-26: Freeze the motivational v0.3 new-candidate reachability
  evidence contract. The gate content-addresses the sealed fixture,
  independent consumer, and consumer tests while pinning registry/checkpoint
  identities, cursor/trace, exact `defer_for_review` selection, absence of a
  score policy, and candidate-only authority. Five provider-free checks pass
  at
  `artifacts/ggb-capacity-gates/20260726-motivation-reachability-contract-freeze/`.
  Next: preregister score-policy evolution separately; do not alter this
  frozen evidence boundary.

- [x] 2026-07-25: Close ThreadKeeper's authenticated native-provider
  `thinking` metadata boundary on commit `9fda4c5`. Non-null thinking metadata
  must be an exact built-in string; behavior-bearing subclasses fail closed
  before overloaded equality. Four focused checks and the 1005-test
  provider-free hardening suite passed.

- [x] 2026-07-25: Close ThreadKeeper's authenticated native-provider mapping
  and scalar-metadata boundary on commit `11c46d6`. Response/message mappings
  must be exact built-in dictionaries; model, creation-time, role, and
  completion-reason values must be exact built-in strings. Behavior-bearing
  subclasses fail closed before overloaded iteration, comparison, or
  normalization. Six focused checks and the 1004-test provider-free hardening
  suite passed.

- [x] 2026-07-25: Independently reproduce motivational v0.3 new-candidate
  reachability from a sealed JSON fixture without importing producer or prior
  gate code. The strict consumer verifies registry/checkpoint digests, exact
  cursor/trace/order, and bounded action authority; duplicate members,
  trailing content, semantic mutation, rehashed early cursor, and rehashed
  authority widening fail closed. Six provider-free tests pass at
  `artifacts/ggb-capacity-gates/20260725-motivation-new-candidate-serialized-consumer/`.
  Candidate-only; ThreadKeeper effect `none`. Next: freeze this reachability
  evidence contract before introducing any score-policy evolution.

- [x] 2026-07-25: Close ThreadKeeper's authenticated native-provider
  duration/context metadata boundary on commit `a8d338b`. Duration values,
  context containers, and context token IDs must use exact built-in integer/list
  types; behavior-bearing subclasses fail closed before overloaded comparison
  or iteration. Twenty-one focused checks and the 998-test provider-free
  hardening suite passed.

- [x] 2026-07-25: Close ThreadKeeper's authenticated OpenAI-compatible
  response-metadata boundary on commit `e638a15`. Response IDs and creation
  timestamps must be exact built-in strings/integers; behavior-bearing
  subclasses fail closed as `provider_response_invalid` before their
  overloaded operations can run. Nineteen focused checks and the 982-test
  provider-free hardening suite passed.

- [x] 2026-07-25: Preregister and exercise the first motivational v0.3
  new-candidate reachability holdout. A pinned checkpoint at cursor 3 reaches
  exactly `defer_for_review` by ordinal replay after the three preserved
  candidates; no score function or scoring-policy change is introduced.
  Changed expectation, early cursor with rehash, registry substitution, and
  authority widening fail closed. Five provider-free tests pass at
  `artifacts/ggb-capacity-gates/20260725-motivation-new-candidate-reachability/`.
  Candidate-only; ThreadKeeper effect `none`. Next: independently reproduce
  the result from a serialized fixture without importing producer code.

- [x] 2026-07-25: Close ThreadKeeper's authenticated provider-usage boundary
  to behavior-bearing integer subclasses on commit `d2c8611`. Input/output
  token counts must now be exact built-in integers or become a private
  `provider_response_invalid` control result before accounting or persistence.
  Three focused checks and the 980-test provider-free hardening suite passed.

- [x] 2026-07-25: Close ThreadKeeper's authenticated provider-content
  boundary to behavior-bearing string subclasses on commit `1d830c9`. Provider
  content must now be an exact built-in string or it becomes a private
  `provider_response_invalid` control result before parser, prompt, or
  transcript operations. Two focused checks and the 978-test provider-free
  hardening suite passed.

- [x] 2026-07-25: Independently consume the motivational v0.2-to-v0.3
  migration receipt and prove checkpoint replay equivalence. A separately
  implemented verifier binds both registry and checkpoint digests, preserves
  cursor/incumbent/trace, and replays the pre-existing tail identically before
  `defer_for_review` becomes reachable. Five provider-free tests pass at
  `artifacts/ggb-capacity-gates/20260725-motivation-migration-independent-replay/`.
  Candidate-only; ThreadKeeper effect `none`. Next: define a preregistered
  holdout where the new candidate is reached, without changing scoring policy.

- [x] 2026-07-25: Close ThreadKeeper's direct `run_tools()` boundary to
  behavior-bearing list, tuple, and string subclasses on commit `497c9c8`.
  Complete-batch validation now rejects these shapes before any earlier valid
  tool effect. Eleven focused checks and the 982-test provider-free hardening
  suite passed.

- [x] 2026-07-25: Persist ThreadKeeper tool-response parser exceptions as
  structured failures on commit `f8335c2`. Parser `ValueError`/`TypeError`
  failures now return bounded `skill_protocol_error` digests and durable
  transcripts instead of escaping `dispatch()`; exception messages remain
  private. Seven focused checks and the 985-test provider-free hardening suite
  passed.

- [x] 2026-07-25: Separate motivational semantic evolution from the frozen
  representation boundary. An explicit candidate-set v0.2-to-v0.3 migration
  adds only `defer_for_review`, preserves checkpoint cursor/incumbent/trace,
  and binds old/new registry and checkpoint digests in a candidate-only
  receipt. Seven provider-free tests pass; downgrade, removal/renumbering,
  candidate mutation, authority widening, and checkpoint unbinding fail
  closed. Evidence:
  `artifacts/ggb-capacity-gates/20260725-motivation-candidate-registry-migration/`.
  Next: independently consume the migration receipt and prove v0.3
  checkpoint replay equivalence before any scoring-policy change.

- [x] 2026-07-25: Enforce exact built-in string values for every parsed
  ThreadKeeper tool argument on commit `814be73`. String subclasses and
  non-string argument values now fail as persistent `skill_protocol_error`
  records during complete-batch preflight, before any earlier valid tool
  effect. Six focused checks and the 983-test provider-free hardening suite
  passed.

- [x] 2026-07-25: Enforce exact built-in container types at ThreadKeeper's
  closed parser-output boundary on commit `cbbc36f`. List/tuple/string
  subclasses for the batch, record, tool name, or arguments now fail as a
  persistent `skill_protocol_error` before any tool effect. Nine focused
  checks and the 968-test provider-free hardening suite passed.

- [x] 2026-07-25: Freeze the provider-free motivational representation
  evidence contract. The gate content-addresses the two-consumer admission
  contract, portable-boundary holdout, and both passing consumer reports while
  pinning the maximum portable integer, new Unicode scalar, admitted
  candidate-set digest, and candidate-only authority. Five checks pass at
  `artifacts/ggb-capacity-gates/20260725-motivation-representation-contract-freeze/`.
  Next: test an explicitly versioned candidate-registry migration separately
  from this frozen representation boundary.

- [x] 2026-07-25: Validate ThreadKeeper parser output before `dispatch()`
  destructures or records tool calls on commit `a43aa39`. Malformed batch,
  record, name, and argument-container shapes now return a persistent
  `skill_protocol_error` transcript and structured parent digest instead of
  raising outside the existing execution preflight. Five focused checks and
  the 964-test provider-free hardening suite passed.

- [x] 2026-07-24: Require canonical Unicode in ThreadKeeper final structured
  returns on commit `2bad03e`. Final `emit` values containing lone surrogate
  code points or non-NFC text now fail before a successful parent digest or
  transcript status is produced. Two focused checks and the 959-test
  provider-free hardening suite passed.

- [x] 2026-07-24: Hold out the motivational-registry cross-runtime
  representation boundary. Both strict consumers accept the maximum portable
  integer `9007199254740991` through raw parsing, reject `9007199254740992`
  before semantic hashing, and accept a new valid supplementary-plane Unicode
  scalar through representation preflight. The original candidate-set hash is
  unchanged. Twenty-four pinned-consumer assertions and three orchestration checks
  pass at `artifacts/ggb-capacity-gates/20260724-motivation-portable-boundary-holdout/`.
  Candidate-only; ThreadKeeper effect `none`. The content-addressed
  per-consumer admission record was refreshed for both bounded consumers.

- [x] 2026-07-24: Require list-shaped arguments for ThreadKeeper final `emit`
  records on commit `3973119`. Malformed scalar, tuple, mapping, and null emit
  containers now fail the complete-batch preflight before any earlier valid
  tool effect. Four focused checks and the 958-test provider-free hardening
  suite passed.

- [x] 2026-07-24: Preregister per-consumer raw-byte-preflight admission for
  motivational-registry portability evidence. The content-addressed strict
  Python and Node.js consumers must each own rejection of noncanonical
  integers, non-NFC/non-scalar strings, and duplicate members at registry,
  candidate, and nested-contract depths; a shared validator, peer import,
  missing failure case, identity drift, diversity collapse, or authority
  widening fails closed. Seven admission checks and both pinned consumer
  suites pass at
  `artifacts/ggb-capacity-gates/20260724-motivation-per-consumer-preflight/`.
  Candidate-only; ThreadKeeper effect `none`. Next: require a holdout registry
  fixture with a new valid Unicode scalar and maximum admitted integer before
  considering the representation contract stable.

- [x] 2026-07-24: Require a closed, strongly typed ThreadKeeper worker
  tool-call shape on commit `c0e4a61`. Tool names must be strings and argument
  containers must be JSON-array-shaped Python lists; scalar strings, tuples,
  mappings, and null now fail the complete-batch preflight before any tool
  effect. Four focused checks and the 968-test provider-free hardening suite
  passed.

- [x] 2026-07-24: Require a closed ThreadKeeper tool-call batch/record shape
  on commit `896f0bf`. Non-list batches and records other than exact
  `(name, arguments)` tuples now fail before tuple unpacking or any earlier
  valid tool effect. Four focused checks and the 962-test provider-free
  hardening suite passed.

- [x] 2026-07-24: Reject internal U+1680 OGHAM SPACE MARK in ThreadKeeper
  file-tool and task-contract paths on commit `bd58fac`. This visually blank
  Unicode space is the only non-ASCII `Zs` character that survives NFKC
  without becoming ASCII space, so it previously bypassed compatibility-space
  rejection inside path components. Four focused checks and the 965-test
  provider-free hardening suite passed.

- [x] 2026-07-24: Add a separately implemented strict Node.js motivational-
  registry consumer. Both byte-distinct fixtures reproduce candidate-set
  SHA-256 `7ee23bac6d9e82c263039bff9f9015c65a457a844e9538aba22396727518804c`;
  three noncanonical numeric spellings, non-NFC text, a lone surrogate, and
  duplicate members at registry, candidate, and nested-contract depths fail
  before semantic hashing. Ten checks and syntax/direct replay pass at
  `artifacts/ggb-capacity-gates/20260724-motivation-strict-javascript-consumer/`.
  Candidate-only; ThreadKeeper effect `none`. The per-consumer raw-byte-
  preflight admission follow-on is complete.

- [x] 2026-07-24: Reject U+2800 BRAILLE PATTERN BLANK in ThreadKeeper
  file-tool and task-contract paths on commit `e74bcbe`. This visually empty
  symbol is neither a Unicode format character nor a compatibility space, so
  it previously bypassed the shared path guard. Thirty-six focused checks and
  the 961-test provider-free hardening suite passed.

- [x] 2026-07-24: Reject U+16FE4 KHITAN SMALL SCRIPT FILLER in ThreadKeeper
  file-tool and task-contract paths on commit `f03fcf0`. This visually empty
  combining mark is not a Unicode format character, so it previously bypassed
  the shared path guard. Thirty-two focused checks and the 957-test
  provider-free hardening suite passed.

- [x] 2026-07-24: Add an independent Python strict-JSON motivational-registry
  consumer. Both byte-distinct fixtures retain candidate-set SHA-256
  `7ee23bac6d9e82c263039bff9f9015c65a457a844e9538aba22396727518804c`;
  all five representation-preflight negatives and duplicate members at
  registry, candidate, and nested-contract depths fail before semantic
  hashing. Ten checks, direct replay, compilation, and diff check pass at
  `artifacts/ggb-capacity-gates/20260724-motivation-strict-json-consumer/`.
  Candidate-only; ThreadKeeper effect `none`. Next: decide by preregistered
  contract whether every admitted consumer or one shared byte validator owns
  duplicate-member rejection.

- [x] 2026-07-24: Reject visually empty Khmer inherent vowel controls in
  ThreadKeeper file-tool and task-contract paths on commit `f5e873d`.
  U+17B4/U+17B5 are combining marks rather than Unicode format characters, so
  the prior format guard did not catch them. Twenty-eight focused checks and
  the 953-test provider-free hardening suite passed.

- [x] 2026-07-24: Reject invisible Unicode fillers in ThreadKeeper file-tool
  and task-contract paths on commit `0cf8295`. COMBINING GRAPHEME JOINER,
  Hangul choseong/jungseong fillers, HANGUL FILLER, and HALFWIDTH HANGUL FILLER
  can no longer create visually empty filename text in prompts and audit
  records. Twenty focused checks and the 945-test provider-free hardening suite
  passed.

- [x] 2026-07-24: Preregister and enforce a motivational-registry
  representation preflight without changing the admitted candidate-set hash.
  Both byte-distinct fixtures retain SHA-256
  `7ee23bac6d9e82c263039bff9f9015c65a457a844e9538aba22396727518804c`;
  ordinal aliases `-0`, `0e0`, and `0.0`, a decomposed Unicode purpose, and a
  lone surrogate fail closed. Seven checks pass at
  `artifacts/ggb-capacity-gates/20260724-motivation-representation-preflight/`.
  Candidate-only; ThreadKeeper effect `none`. The non-JavaScript replay and
  duplicate-member boundary follow-on is complete.

- [x] 2026-07-24: Reject Unicode compatibility forms containing embedded path
  separators in ThreadKeeper file-tool and task-contract paths on commit
  `0dbd260`. The symbols ℀, ℁, ℅, and ℆ NFKC-normalize to strings containing
  `/` and now fail before worker LLM, contract authorization, audit, or
  filesystem effects. Twenty-eight focused checks and the 925-test
  provider-free hardening suite passed.

- [x] 2026-07-24: Reject Unicode compatibility spaces in ThreadKeeper
  file-tool and task-contract paths on commit `934d58e`. Characters such as
  NBSP, EN/EM SPACE, FIGURE SPACE, NARROW NO-BREAK SPACE, MEDIUM MATHEMATICAL
  SPACE, and IDEOGRAPHIC SPACE can no longer survive inside a component and
  later NFKC-normalize into a trailing ASCII-space alias. Twenty-eight focused
  checks and the 896-test provider-free hardening suite passed.

- [x] 2026-07-24: Add a third independent motivational-registry consumer
  using Node.js built-ins. Both byte-distinct producer fixtures reproduce
  candidate-set SHA-256
  `7ee23bac6d9e82c263039bff9f9015c65a457a844e9538aba22396727518804c`;
  semantic mutation, authority widening, unknown fields, reordering, and a
  fractional ordinal fail closed. Seven checks pass at
  `artifacts/ggb-capacity-gates/20260724-motivation-javascript-holdout/`.
  Candidate-only; ThreadKeeper effect `none`. The ambiguous Unicode/numeric
  representation preflight follow-on is complete.

- [x] 2026-07-24: Require NFC Unicode normalization for ThreadKeeper
  task-contract `allowed_paths` on commit `8403e06`. This closes the mismatch
  where file-tool paths rejected decomposed spellings but the authorization
  boundary admitted them. Invalid paths now fail before worker LLM, contract
  authorization, audit, or filesystem effects. Two focused checks and the
  868-test provider-free hardening suite passed.

- [x] 2026-07-23: Reject ThreadKeeper path components whose NFKC compatibility
  form becomes a canonical Windows device name on commit `3bd18da`.
  Fullwidth and subscript-digit aliases such as `ＣＯＮ.txt`, `ＣＯＭ１.log`,
  and `ＬＰＴ₉.txt` now fail in file-tool and task-contract paths before
  worker LLM, audit, contract authorization, or filesystem effects.
  Forty-four focused checks and the 867-test provider-free hardening suite
  passed.

- [x] 2026-07-23: Preregister and replay a motivational registry
  consumer-diversity admission rule. Two content-addressed consumers must
  differ in language, runtime, JSON library, and implementation path, import
  no other admitted consumer, and reproduce the exact candidate-set hash.
  Ten provider-free checks pass at
  `artifacts/ggb-capacity-gates/20260724-motivation-consumer-diversity/`.
  Candidate-only; adjudication required; ThreadKeeper effect `none`.

- [x] 2026-07-23: Reject Unicode compatibility forms that NFKC-normalize into
  `:`, `<`, `>`, `"`, `|`, `?`, or `*` in ThreadKeeper file-tool and
  task-contract paths on commit `3f2280a`. Fullwidth and small-form punctuation
  can no longer bypass alternate-stream and Windows-forbidden filename checks
  before worker LLM, audit, contract authorization, or filesystem effects.
  Thirty-six focused checks and the 864-test provider-free hardening suite
  passed.

- [x] 2026-07-23: Reject Unicode compatibility characters whose NFKC form
  contains ASCII dots in ThreadKeeper file-tool and task-contract paths on
  commit `6a26286`, including U+2024, U+2025, U+2026, U+FE52, and U+FF0E.
  These can no longer bypass audited traversal, extension, or Windows
  device-name spellings and later normalize to ASCII dots. Twenty focused
  checks and the 828-test provider-free hardening suite passed.

- [x] 2026-07-23: Reproduce the admitted motivational candidate-set hash with
  a separately implemented Perl/JSON::PP canonicalizer. Both byte-distinct
  registry fixtures independently reproduce
  `7ee23bac6d9e82c263039bff9f9015c65a457a844e9538aba22396727518804c`;
  semantic mutation, action-authority widening, and unknown fields fail
  closed. Five provider-free checks pass at
  `artifacts/ggb-capacity-gates/20260723-motivation-independent-canonicalizer/`.
  Candidate-only; ThreadKeeper effect `none`.

- [x] 2026-07-23: Reject Unicode separator lookalikes in ThreadKeeper
  file-tool and task-contract paths on commit `1a4f68d`. Fraction slash,
  division slash, big solidus, and big reverse solidus can no longer visually
  masquerade as path separators in prompts or audit records. Sixteen focused
  checks and the 795-test provider-free hardening suite passed.

- [x] 2026-07-23: Reject Unicode separator compatibility characters in
  ThreadKeeper file-tool and task-contract paths on commit `2f749e3`.
  U+FE68, U+FF0F, and U+FF3C can no longer be audited as filename text and
  later compatibility-normalized into `/` or `\`. Twelve focused checks and
  the 792-test provider-free hardening suite passed.

- [x] 2026-07-23: Compare two independently serialized motivational candidate
  registries under a strict canonicalization contract. Their raw JSON bytes
  differ but converge to the previously admitted candidate-set SHA-256;
  semantic mutation, action-authority widening, unknown fields, and candidate
  reordering fail closed. Five unit checks, compile, and JSON replay pass at
  `artifacts/ggb-capacity-gates/20260723-motivation-cross-producer-canonicalization/`.
  Candidate-only; ThreadKeeper effect `none`. Follow-on independent
  Perl/JSON::PP reproduction is complete.

- [x] 2026-07-23: Complete ThreadKeeper variation-selector path validation on
  commit `f8e9691` by rejecting Mongolian free variation selectors
  U+180B--U+180D and U+180F in file-tool and task-contract paths before worker
  LLM, audit, contract authorization, or filesystem effects. Twenty-eight
  focused checks and the 767-test provider-free hardening suite passed.

- [x] 2026-07-23: Reject Unicode variation selectors in ThreadKeeper file-tool
  and task-contract paths on commit `f9f04e0`. BMP selectors U+FE00--U+FE0F
  and supplementary selectors U+E0100--U+E01EF now fail before worker LLM,
  audit, contract authorization, or filesystem effects. Twelve focused checks
  and the 751-test provider-free hardening suite passed.

- [x] 2026-07-23: Independently ingest the sealed motivational candidate
  registry/checkpoint without importing or invoking producer sealing code.
  The consumer recomputes semantic, action, candidate-set, and checkpoint
  digests before suffix replay; semantic mutation, authority widening,
  substitution, and checkpoint mutation fail closed. Five unit checks,
  compile, and JSON replay pass at
  `artifacts/ggb-capacity-gates/20260723-motivation-candidate-contract-ingest/`.
  Candidate-only; ThreadKeeper effect `none`. The separately serialized
  cross-producer comparison is now complete.

- [x] 2026-07-23: Reject ThreadKeeper file-tool and task-contract path
  components exceeding the common 255-byte filesystem component limit on
  commit `a8d0311`. Validation counts UTF-8 bytes, so multibyte names fail
  before worker LLM, audit, contract authorization, or filesystem effects.
  Four focused checks and the 752-test provider-free hardening gate passed.

- [x] 2026-07-23: Reject Windows-forbidden filename characters in ThreadKeeper
  file-tool and task-contract paths on commit `638618b`. The characters `<`,
  `>`, `"`, `|`, `?`, and `*` now fail before worker LLM, audit, contract
  authorization, or filesystem effects. Twenty-four focused checks and the
  748-test provider-free hardening gate passed.

- [x] 2026-07-23: Bind each stable motivational candidate ID to semantic
  and action-contract digests before checkpoint resume. Semantic mutation,
  effect/authority widening, digest substitution, candidate reordering, and
  checkpoint mutation fail closed. Six unit checks, compile, and JSON replay
  pass at
  `artifacts/ggb-capacity-gates/20260723-motivation-candidate-contract-digests/`.
  Candidate-only; ThreadKeeper effect `none`. Next: independently ingest this
  registry/checkpoint rather than sealing and consuming it in one process.

- [x] 2026-07-23: Reject invisible Unicode joiners in ThreadKeeper file-tool
  and task-contract paths on commit `31e3cdd`. U+200C/U+200D now fail before
  worker LLM, audit, contract authorization, or filesystem effects. Eight
  focused checks and the 724-test provider-free hardening gate passed.

- [x] 2026-07-23: Reject superscript-digit Windows device aliases in
  ThreadKeeper file-tool and task-contract paths on commit `4d1fd33`.
  `COM¹`--`COM³` and `LPT¹`--`LPT³`, including names with extensions, now
  fail before worker LLM, audit, or filesystem effects. Twenty-eight focused
  checks and the 703-test provider-free hardening gate passed.

- [x] 2026-07-23: Bind a motivational checkpoint to an ordered, versioned
  three-candidate set and independently recompute a two-event suffix with two
  rank switches. Candidate mutation/reordering, stale version, unknown score
  keys, policy drift, and checkpoint mutation fail closed. Six unit checks,
  compile, and JSON replay pass at
  `artifacts/ggb-capacity-gates/20260723-motivation-candidate-set-resume/`.
  Candidate-only; ThreadKeeper effect `none`. Next: bind per-candidate
  semantic/action-contract digests.

- [x] 2026-07-23: Reject Windows-trimmed path components in ThreadKeeper
  file-tool and task-contract paths on commit `049939b`. Components ending in
  dots or spaces now fail before worker LLM, audit, contract authorization, or
  filesystem effects. Forty focused checks and the 691-test provider-free
  hardening gate passed.

- [x] 2026-07-22: Reject Windows reserved device names in ThreadKeeper
  file-tool and task-contract paths on commit `2e003c3`. Path components such
  as `NUL`, `CON.txt`, `COM1.log`, and `LPT9` now fail before worker LLM,
  audit, contract authorization, or filesystem effects. Twenty-three focused
  checks and the 679-test provider-free hardening gate passed.

- [x] 2026-07-22: Independently resume the scale-1000 motivational
  checkpoint from a preregistered suffix. The consumer verifies the admitted
  checkpoint and source hashes, recomputes the suffix from the pinned source,
  and ignores a deliberately falsified producer `resumed_trace`. Checkpoint
  mutation, suffix mutation, and cursor/scale/margin drift fail closed. Five
  unit checks, compile, JSON replay, and diff check pass at
  `artifacts/ggb-capacity-gates/20260723-motivation-fixed-point-resume/`.
  Candidate-only; ThreadKeeper effect `none`. Next: bind candidate-set
  identity before testing a multi-candidate suffix.

- [x] 2026-07-22: Reject Windows alternate-data-stream spellings in
  ThreadKeeper file-tool and task-contract paths on commit `a0df4fc`. Relative
  paths containing colons, including `safe.txt:hidden` and
  `safe.txt::$DATA`, now fail before LLM, audit, or filesystem effects.
  Seventeen focused checks and the 663-test provider-free hardening gate
  passed.

- [x] 2026-07-22: Reject drive-qualified ThreadKeeper file-tool and task-
  contract paths on commit `2204b86`. Spellings such as `C:/secret.txt` and
  `c:secret.txt`, which POSIX can treat as relative but Windows interprets as
  drive-qualified, now fail before LLM, audit, or filesystem effects. Ten
  focused checks and the 661-test provider-free hardening gate passed.

- [x] 2026-07-22: Independently ingest the scale-1000 motivational checkpoint.
  A separate consumer recomputes the checkpoint and source hashes and pins the
  schema, cursor, scale, margin, and trace prefix; mutation, stale source
  identity, and policy drift fail closed. Four unit checks, compile, JSON
  replay, and diff check pass at
  `artifacts/ggb-capacity-gates/20260722-motivation-fixed-point-ingest/`.
  Candidate-only; ThreadKeeper effect `none`. Next: preregister a bounded
  suffix event and prove the independent consumer resumes from the admitted
  checkpoint without trusting a producer-supplied resumed trace.

- [x] 2026-07-22: Reject cross-platform-ambiguous backslashes in ThreadKeeper
  file-tool and task-contract relative paths on commit `7c6b544`. Paths now
  require forward-slash separators before audit, provider, or filesystem
  effects. Seven focused checks and the 659-test provider-free
  subagent/budget gate passed.

- [x] 2026-07-22: Require canonical ThreadKeeper relative path spellings on
  `agent/threadkeeper-hardening-next` commit `3ca23e7`. File tools and task
  contract `allowed_paths` now reject dot components, repeated separators,
  and trailing separators before audit or filesystem effects, so the recorded
  spelling equals the normalized path used. Twenty-six focused checks and the
  652-test provider-free subagent/budget gate passed.

- [x] 2026-07-22: Compare decimal and integer fixed-point motivational replay.
  Scale-1000 integers derived after pinned three-place round-half-even preserve
  the below/above/exact hysteresis trace; a two-case self-hashed checkpoint
  resumes to the uninterrupted trace. Four unit checks, compile, and JSON
  replay pass at `artifacts/ggb-capacity-gates/20260722-motivation-fixed-point/`.
  Candidate-only; ThreadKeeper effect `none`. Next: independently ingest the
  checkpoint and fail closed on mutation, stale source identity, or policy drift.

- [x] 2026-07-22: Reject ambiguous ThreadKeeper run-control paths on
  `agent/threadkeeper-hardening-next` commit `8402cad`. Queued-task
  `cancel_file` and async-worker `stop_file` inputs with leading/trailing
  ASCII or Unicode whitespace or non-NFC spellings now fail before queue
  claims, worker locks, or LLM calls. Eight focused checks and the 640-test
  provider-free subagent/budget gate passed.

- [x] 2026-07-22: Require NFC normalization for ThreadKeeper audited tool
  arguments on `agent/threadkeeper-hardening-next` commit `16a7776`. Canonically equivalent but
  byte-distinct file paths, external queries, and optional-shell commands now
  fail before filesystem, prompt, subprocess, or audit effects; file contents
  remain unrestricted by this single-line rule. Two focused checks and the
  634-test provider-free subagent/budget gate passed.

- [x] 2026-07-22: Probe motivational quantization at a preregistered
  hysteresis boundary. Decimal-string inputs with three-place round-half-even
  preserve the below/exact/above decisions, while a two-place lossy control
  suppresses the just-above-boundary switch. Unpinned rounding, invalid
  precision, non-string/non-finite scores, changed expectations, and unpinned
  provenance fail closed. Five unit checks, compile, and JSON replay pass at
  `artifacts/ggb-capacity-gates/20260722-motivation-quantization/`.
  Candidate-only; ThreadKeeper effect `none`. Next: compare decimal replay to
  an integer fixed-point representation across boundary and restart fixtures.

- [x] 2026-07-22: Reject boundary whitespace in ThreadKeeper query and shell
  arguments on `agent/threadkeeper-hardening-next` commit `192ccd2`. Search,
  Tavily, technical-analysis, and optional-shell inputs with leading or
  trailing ASCII or Unicode whitespace now fail before prompt, provider,
  subprocess, or audit effects. Focused boundary-whitespace checks: 28 passed;
  provider-free subagent/budget gate with LLM call limiting disabled: 632
  passed.

- [x] 2026-07-22: Reject boundary whitespace in ThreadKeeper file-tool paths
  on `agent/threadkeeper-hardening-next` commit `e972609`. Read, write, and
  append paths with leading or trailing ASCII or Unicode whitespace now fail
  before audit or filesystem effects, avoiding visually ambiguous filenames.
  Focused checks: 13 passed; provider-free subagent/budget gate with LLM call
  limiting disabled: 616 passed.

- [x] 2026-07-22: Preregister inclusive finite numeric domains for the v0.1
  motivational fields. Probability deltas are bounded to `[-1, 1]` and
  resource-fraction cost to `[0, 1]`; exact endpoints pass, while just-outside,
  NaN, infinity, overflow, boolean, string, and null values fail closed. Five
  unit checks, compile, and JSON replay pass at
  `artifacts/ggb-capacity-gates/20260722-motivation-field-ranges/`.
  Candidate-only; ThreadKeeper effect `none`. Next: test quantization and
  rounding sensitivity near a preregistered selection boundary.

- [x] 2026-07-22: Reject Unicode noncharacters at ThreadKeeper tool argument
  boundaries on `agent/threadkeeper-hardening-next` commit `cc1e306`. Paths,
  queries, and optional shell commands now reject U+FDD0--FDEF and every
  plane-ending FFFE/FFFF code point before filesystem, prompt, subprocess, or
  audit use. Focused checks: 5 passed; provider-free subagent/budget gate with
  LLM call limiting disabled: 604 passed.

- [x] 2026-07-22: Reject unknown OpenAI-compatible SDK/Pydantic fields on
  `agent/threadkeeper-hardening-next` commit `fd927f8`. Non-empty
  `model_extra` at the response, choice, message, or usage layer now fails
  closed as `provider_response_invalid` without retry, including extras whose
  values are null or falsey. Focused checks: 24 passed; provider-free
  subagent/budget gate with LLM call limiting disabled: 603 passed.

- [x] 2026-07-22: Reject OpenAI-compatible top-level response `metadata` on
  `agent/threadkeeper-hardening-next` commit `ed7283c`. Non-null metadata,
  including explicit falsey values, now fails closed as an authenticated
  `provider_response_invalid` outcome without retry. Focused checks: 4 passed;
  provider-free subagent/budget gate with LLM call limiting disabled: 579
  passed.

- [x] 2026-07-21: Reject OpenAI-compatible top-level `error` payloads on
  `agent/threadkeeper-hardening-next` commit `063ae25`. Non-null error payloads,
  including explicit falsey values, now fail closed as authenticated
  `provider_response_invalid` outcomes without retry. Focused checks: 4 passed;
  provider-free subagent/budget gate with rate limiting disabled: 575 passed.

- [x] 2026-07-21: Pin explicit motivational field units independently of
  semantic identity. `competence_gain` and `uncertainty_gain` deliberately
  share a dimension, but semantic relabeling still fails closed; missing,
  extra, empty, and non-string unit metadata also fail. Four unit checks,
  compile, and JSON replay pass at
  `artifacts/ggb-capacity-gates/20260721-motivation-field-units/`.
  Candidate-only; ThreadKeeper effect `none`. Next: preregister admissible
  numeric ranges per field and test boundary/overflow negatives.

- [x] 2026-07-21: Reject OpenAI-compatible usage token-detail payloads on
  `agent/threadkeeper-hardening-next` commit `b990113`. Non-null
  `prompt_tokens_details` and `completion_tokens_details`, including explicit
  falsey values, now fail closed as authenticated `provider_response_invalid`
  outcomes without retry. Focused checks: 8 passed; provider-free
  subagent/budget gate with rate limiting disabled: 571 passed.

- [x] 2026-07-21: Reject OpenAI-compatible assistant `parsed` payloads on
  `agent/threadkeeper-hardening-next` commit `f711a73`. Non-null parsed
  structured outputs, including explicit falsey values, now fail closed as an
  authenticated `provider_response_invalid` outcome without retry. Focused
  checks: 4 passed; provider-free subagent/budget gate with rate limiting
  disabled: 567 passed.

- [x] 2026-07-21: Bind motivational affine metadata per score field. Distinct
  scales/origins for `competence_gain`, `uncertainty_gain`, and `cost` preserve
  the preregistered trace after field-specific normalization; missing/extra
  metadata, invalid scales, score mismatch, and field swaps fail closed. Five
  unit checks, compile, and JSON replay pass at
  `artifacts/ggb-capacity-gates/20260721-motivation-per-field-affine/`.
  Candidate-only; ThreadKeeper effect `none`. Next: bind explicit unit labels
  and test same-dimension field swaps before freezing a feature schema.

- [x] 2026-07-21: Reject OpenAI-compatible top-level
  `prompt_filter_results` metadata on `agent/threadkeeper-hardening-next`
  commit `de49e1c`. Non-null prompt-filter metadata, including explicit
  falsey values, now fails closed as an authenticated
  `provider_response_invalid` outcome without retry. Focused checks: 4
  passed; provider-free subagent/budget gate with rate limiting disabled:
  563 passed.

- [x] 2026-07-21: Reject OpenAI-compatible choice `content_filter_results`
  metadata on `agent/threadkeeper-hardening-next` commit `3030a6a`. Non-null
  content-filter metadata, including explicit falsey values, now fails closed
  as an authenticated `provider_response_invalid` outcome without retry.
  Focused checks: 4 passed; provider-free subagent/budget gate with rate
  limiting disabled: 559 passed.

- [x] 2026-07-21: Probe affine-origin sensitivity of the dimensionless
  motivation contract. Centering common declared origins `0.0`, `0.05`, and
  `0.10` before scale normalization preserves the preregistered trace;
  invalid, missing/mismatched, and candidate-specific offsets fail closed.
  Five unit checks, compile, and JSON replay pass at
  `artifacts/ggb-capacity-gates/20260721-motivation-affine-origin/`.
  Candidate-only; ThreadKeeper effect `none`. Next: test per-field
  scale/origin metadata and field-swap negatives before freezing a feature
  schema.

- [x] 2026-07-21: Reject OpenAI-compatible choice `logprobs` metadata on
  `agent/threadkeeper-hardening-next` commit `af147ac`. Non-null log
  probabilities, including explicit falsey values, now fail closed as an
  authenticated `provider_response_invalid` outcome without retry. Focused
  checks: 4 passed; provider-free subagent/budget gate with rate limiting
  disabled: 555 passed.

- [x] 2026-07-21: Reject OpenAI-compatible provider `service_tier` metadata
  on `agent/threadkeeper-hardening-next` commit `ef2b8f4`. Non-null tiers,
  including explicit falsey values, now fail closed as an authenticated
  `provider_response_invalid` outcome without retry. Focused checks: 4
  passed; provider-free subagent/budget gate with rate limiting disabled:
  551 passed.

- [x] 2026-07-21: Preregister a dimensionless motivational normalization
  contract. Declared score scales `1.0`, `0.5`, and `0.25` reproduce the same
  four-step trace after normalization; invalid and score-mismatched scale
  metadata fail closed. Five unit checks, compile, and JSON replay pass at
  `artifacts/ggb-capacity-gates/20260721-motivation-normalization-contract/`.
  Candidate-only; ThreadKeeper effect `none`. Next: probe affine-offset
  sensitivity before freezing any operational score contract.

- [x] 2026-07-21: Reject OpenAI-compatible provider `system_fingerprint`
  metadata on `agent/threadkeeper-hardening-next` commit `2c44571`. Non-null
  fingerprints, including explicit falsey values, now fail closed as an
  authenticated `provider_response_invalid` outcome without retry. Focused
  checks: 4 passed; provider-free subagent/budget gate with rate limiting
  disabled: 547 passed.

- [x] 2026-07-21: Reject OpenAI-compatible assistant message metadata on
  `agent/threadkeeper-hardening-next` commit `087b369`. Non-null `metadata`,
  including explicit falsey values, now fails closed as an authenticated
  `provider_response_invalid` outcome without retry. Focused checks: 4 passed;
  provider-free subagent/budget gate with rate limiting disabled: 543 passed.

- [x] 2026-07-21: Test motivational hysteresis score-scale sensitivity. A
  fixed absolute margin `0.05` preserves the intended switch at scale `1.0`
  but suppresses it at `0.5` and `0.25`; scaling the margin with the declared
  score scale preserves the preregistered trace across all three. Five unit
  checks, compile, and JSON replay pass at
  `artifacts/ggb-capacity-gates/20260721-motivation-score-scale/`. Candidate-only;
  ThreadKeeper effect `none`. Next: preregister a dimensionless normalization
  contract and reject zero, negative, non-finite, or mismatched scale metadata.

- [x] 2026-07-21: Reject OpenAI-compatible assistant message names on
  `agent/threadkeeper-hardening-next` commit `78d6224`. Non-null `name`
  metadata, including explicit falsey values, now fails closed as an
  authenticated `provider_response_invalid` outcome without retry, preventing
  alternate message identity metadata beside validated text. Focused checks:
  4 passed; provider-free subagent/budget gate with rate limiting disabled:
  539 passed.

- [x] 2026-07-21: Reject OpenAI-compatible assistant `reasoning_content` on
  `agent/threadkeeper-hardening-next` commit `49a8a17`. Non-null hidden
  reasoning payloads, including explicit falsey values, now fail closed as
  authenticated `provider_response_invalid` outcomes without retry. Focused
  checks: 4 passed; provider-free subagent/budget gate with rate limiting
  disabled: 535 passed.

- [x] 2026-07-21: Replay provisional motivation hysteresis on a structurally
  different three-candidate topology. Margin `0.05` permits exactly one useful
  clarification-to-reversible-plan switch and holds it across two
  perturbations; control margin `0.10` suppresses the switch. Five unit checks,
  compile, and JSON replay pass at
  `artifacts/ggb-capacity-gates/20260721-motivation-candidate-topology/`.
  Candidate-only; ThreadKeeper effect `none`; this corroborates but does not
  freeze a runtime default. Next: test scale/normalization sensitivity before
  considering a v0.1 default freeze.

- [x] 2026-07-21: Reject OpenAI-compatible assistant annotation payloads on
  `agent/threadkeeper-hardening-next` commit `3beac3b`. Non-null annotations,
  including explicit falsey values, now fail closed as authenticated
  `provider_response_invalid` outcomes without retry, closing an ignored
  alternate output channel beside validated text. Focused checks: 4 passed;
  provider-free subagent/budget gate with rate limiting disabled: 531 passed.

- [x] 2026-07-20: Reject OpenAI-compatible assistant audio payloads on
  `agent/threadkeeper-hardening-next` commit `1f6cb4c`. Non-null audio fields,
  including explicit falsey values, now fail closed as authenticated
  `provider_response_invalid` outcomes without retry, closing an ignored
  alternate output channel beside validated text. Focused checks: 5 passed;
  provider-free combined gate with rate limiting disabled: 532 passed.

- [x] 2026-07-21: Preregister and replay an independent provider-free
  hysteresis-margin holdout. A distinct three-event sequence makes margin
  `0.00` oscillate twice, margin `0.05` preserve exactly one useful switch,
  and margins `0.10`/`0.20` suppress the switch. Five unit checks, compile,
  and JSON replay pass at
  `artifacts/ggb-capacity-gates/20260721-motivation-margin-holdout/`.
  Margin `0.05` is provisional and offline-only; ThreadKeeper effect remains
  `none`. Next: replay it on a structurally different candidate set before
  freezing a v0.1 default.

- [x] 2026-07-20: Reject unknown native Ollama top-level response fields on
  `agent/threadkeeper-hardening-next` commit `b059a8d`. Explicit null, falsey,
  and populated unrecognized fields now fail closed as authenticated
  `provider_response_invalid` outcomes without retry, closing ignored payload
  channels outside the validated message/accounting schema. Focused checks: 8
  passed; provider-free combined gate with rate limiting disabled: 522 passed.

- [x] 2026-07-20: Reject unknown native Ollama message fields on
  `agent/threadkeeper-hardening-next` commit `a450d82`. Explicit null, falsey,
  and populated unrecognized fields now fail closed as authenticated
  `provider_response_invalid` outcomes without retry, preventing ignored
  alternate payload channels beside validated content. Focused checks: 12
  passed; provider-free combined gate with rate limiting disabled: 518 passed.

- [x] 2026-07-20: Preregister and replay four separate provider-free
  hysteresis-margin runs. Margins 0.00, 0.05, and 0.10 preserve the intended
  single switch; 0.20 suppresses it. Each run binds the pinned source digest,
  margin, expected switch count, trace, and run digest; changed expectations,
  duplicate margins, and unpinned sources fail closed. Gate: 5/5 unit tests,
  compile, and JSON replay at
  `artifacts/ggb-capacity-gates/20260720-motivation-margin-sensitivity/`.
  Candidate-only; ThreadKeeper effect `none`. Next: preregister an independent
  holdout event sequence before selecting a default margin.

- [x] 2026-07-20: Reject native Ollama `message.images` payloads on
  `agent/threadkeeper-hardening-next` commit `ba95d0c`. Explicit falsey and
  populated image fields fail closed as authenticated
  `provider_response_invalid` outcomes without retry, closing an ignored
  alternate provider payload channel. Focused checks: 12 passed; provider-free
  combined gate with rate limiter disabled: 514 passed.

- [x] 2026-07-20: Reject unexpected native Ollama `message.thinking` content
  on `agent/threadkeeper-hardening-next` commit `9865540`. Nonempty strings
  and malformed non-string values fail closed as authenticated
  `provider_response_invalid` outcomes without retry; omission, null, and the
  provider's empty disabled-thinking marker remain compatible. Focused checks:
  6 passed; provider-free combined gate: 510 passed.

- [x] 2026-07-20: Bind motivational incumbent and hysteresis-policy identity
  into a self-hashed provider-free checkpoint. Restarted replay exactly matches
  uninterrupted selection and terminal state; checkpoint mutation, policy
  drift, and invalid rehashed incumbent fail closed. Gate: 7/7 unit tests plus
  compile and JSON replay; evidence at
  `artifacts/ggb-capacity-gates/20260720-motivation-hysteresis-checkpoint/`.
  Outputs remain candidate-only, adjudication-required, and ThreadKeeper effect
  `none`. Next: preregister separate bounded margin-sensitivity runs.

- [x] 2026-07-20: Make native Ollama message-role metadata
  presence-sensitive on `agent/threadkeeper-hardening-next` commit `5bb8af3`.
  Explicit JSON null now fails closed as authenticated
  `provider_response_invalid` without retry; omission remains compatible.
  Focused regression: 1 passed; provider-free combined gate: 504 passed.

- [x] 2026-07-20: Make native Ollama `done_reason` metadata
  presence-sensitive on `agent/threadkeeper-hardening-next` commit `16100b6`.
  Explicit JSON null now fails closed as authenticated
  `provider_response_invalid` without retry; omission remains compatible.
  Focused checks: 4 passed; combined provider-free gate: 503 passed.

- [x] 2026-07-20: Add a provider-free competing-needs rank-switch gate for
  `motivation-state-v0.1`. One pinned uncertainty-resolution event causes
  exactly one preregistered switch from bounded evidence inspection to
  answering; a 0.05 hysteresis margin prevents a small counter-perturbation
  from oscillating selection. Gate: 7/7 unit tests plus compile; evidence at
  `artifacts/ggb-capacity-gates/20260720-motivation-rank-switch/`. Outputs
  remain candidate-only, adjudication-required, and ThreadKeeper effect
  `none`. Next: checkpoint incumbent and hysteresis-policy identity.

- [x] 2026-07-20: Make native Ollama `created_at` metadata presence-sensitive
  on `agent/threadkeeper-hardening-next` commit `4cc9c7b`. Explicit JSON null
  now fails closed as authenticated `provider_response_invalid` without retry;
  omission remains compatible. Focused checks: 11 passed; combined
  provider-free gate: 493 passed.

- [x] 2026-07-20: Make native Ollama model metadata presence-sensitive on
  `agent/threadkeeper-hardening-next` commit `4d04499`. Explicit JSON null and
  other mismatched/malformed model values fail closed as authenticated
  `provider_response_invalid` outcomes without retry; omission remains
  compatible. Focused checks: 7 passed; combined provider-free gate: 500
  passed.

- [x] 2026-07-20: Extend `motivation-state-v0.1` with a provider-free
  three-event temporal replay. Explicit elapsed time applies bounded decay; a
  self-hashed two-event checkpoint resumes to the same terminal state and
  ranking as uninterrupted replay; checkpoint mutation and non-monotonic time
  fail closed; a clock-only step preserves the top-ranked candidate. Gate:
  6/6 unit tests plus compile; evidence at
  `artifacts/ggb-capacity-gates/20260720-motivation-temporal-replay/`. Outputs
  remain candidate-only, adjudication-required, and ThreadKeeper effect
  `none`. Next: competing-needs rank-switch/hysteresis fixture.

- [x] 2026-07-20: Validate explicitly supplied native Ollama `context`
  metadata on `agent/threadkeeper-hardening-next` commit `8cee8c2`. Context
  must be a list of non-negative integer token IDs; null, scalar, mapping,
  boolean-containing, negative, and fractional values fail closed as
  authenticated `provider_response_invalid` outcomes without retry. Focused
  checks: 10 passed; combined provider-free gate: 497 passed.

- [x] 2026-07-20: Validate explicitly supplied native Ollama duration metadata
  on `agent/threadkeeper-hardening-next` commit `bcbae5e`. The
  `total_duration`, `load_duration`, `prompt_eval_duration`, and
  `eval_duration` fields must be non-negative integers when present; boolean,
  negative, fractional, string, and null values fail closed as authenticated
  `provider_response_invalid` outcomes without retry. Focused checks: 8
  passed; combined provider-free gate: 479 passed.

- [x] 2026-07-20: Materialize the provider-free `motivation-state-v0.1`
  replay gate from the Bach/MetaMo assessment. One pinned synthetic
  `petta-memory`-shaped snapshot updates two bounded needs and six modulators,
  then ranks three GoalChainer-shaped candidates as adjudication-required
  ThreadKeeper candidates with effect `none`. Evidence mutation, stale or
  missing temporal provenance, and invalid/non-finite state fail closed;
  record ordering is invariant and uncertainty urgency is monotonic. Gate:
  7/7 unit tests plus compile; evidence at
  `artifacts/ggb-capacity-gates/20260720-motivation-state-replay/`.

- [x] 2026-07-20: Validate explicitly supplied native Ollama `created_at`
  metadata on `agent/threadkeeper-hardening-next` commit `b4bb993`. Boolean,
  numeric, empty, malformed, collection, and timezone-free values fail closed
  as authenticated `provider_response_invalid` outcomes without retry;
  omitted and timezone-aware ISO/RFC 3339 timestamps remain compatible.
  Focused checks: 10 passed; combined provider-free subagent/budget gate: 471
  passed.

- [x] 2026-07-19: Validate explicitly supplied OpenAI-compatible completion
  timestamps on `agent/threadkeeper-hardening-next` commit `67f3576`.
  Negative, boolean, fractional, string, list, and mapping values fail closed
  as authenticated `provider_response_invalid` outcomes without retry;
  omitted and non-negative integer timestamps remain compatible. Focused
  checks: 9 passed; combined provider-free subagent/budget gate: 469 passed.

- [x] 2026-07-19: Evaluate Joscha Bach's AAAI 2018 “Modeling Emotion and
  Motivation” tutorial against the OmegaSelf/Hyperseed emotion-regime model.
  Acceptance: preserve and hash the source PDF, extract page-addressable text,
  identify the tutorial's actual need/modulator/emotion claims, and deliver a
  concise evidence-backed assessment of agreements, tensions, and concrete
  OmegaClaw design implications. Next command: download the canonical PDF and
  run `pdfinfo`/`pdftotext`. Evidence path:
  `library/bach-aaai2018-modeling-emotion-motivation/`. PDF and extracted text
  are preserved and hashed; `pdfinfo` reports 132 pages. The page-addressed
  assessment is in `notes/2026-07-19-bach-motivation-assessment.md` and defines
  the next provider-free `motivation-state-v0.1` replay gate. The canonical
  download URL, source hash, page-addressable extraction, visual-inspection
  notes, and regime-layer comparison are preserved in
  `library/bach-aaai2018-modeling-emotion-motivation/SOURCE.md`.

- [x] 2026-07-19: Validate explicitly supplied OpenAI-compatible response IDs
  on `agent/threadkeeper-hardening-next` commit `681d256`. Empty,
  whitespace-only, boolean, numeric, list, and mapping IDs fail closed as
  authenticated `provider_response_invalid` outcomes without retry; omitted
  IDs remain compatible. Focused checks: 8 passed; combined provider-free
  subagent/budget gate: 460 passed.

- [x] 2026-07-19: Bind explicitly supplied OpenAI-compatible response object
  metadata to `chat.completion` on `agent/threadkeeper-hardening-next` commit
  `f7df01a`. Wrong-type, empty, boolean, numeric, list, and mapping values fail
  closed as authenticated `provider_response_invalid` outcomes without retry;
  omitted metadata remains compatible. Focused checks: 8 passed; combined
  provider-free subagent/budget gate: 457 passed.

- [x] 2026-07-19: Add a provider-free synthetic disposition split-adequacy
  gate. Exact corpus/assignment identity, minimum partition size, and all four
  authorized disposition labels per partition are required before scoring;
  missing/duplicate identities, unknown labels/splits, underfilled partitions,
  and incomplete label coverage fail closed. Gate: 8 unit tests plus compile.
  No operational corpus selection, scorer fitting, runtime wiring, or canary.

- [x] 2026-07-19: Make provider-native tool-call fields presence-sensitive on
  `agent/threadkeeper-hardening-next` commit `4e06b2d`. Explicit falsey
  `tool_calls` and deprecated `function_call` values fail closed as
  authenticated `provider_response_invalid` outcomes without retry;
  omission/null remains compatible. Focused checks: 8 passed; combined
  provider-free subagent/budget gate: 444 passed.

- [x] 2026-07-19: Bind an explicitly indexed single OpenAI-compatible
  completion to choice zero on `agent/threadkeeper-hardening-next` commit
  `5127c89`. Nonzero, negative, boolean, string, and fractional indices fail
  closed as authenticated `provider_response_invalid` outcomes without retry;
  omitted indices remain compatible. Focused checks: 8 passed; combined
  provider-free subagent/budget gate: 436 passed.

- [ ] 2026-07-19: Diagnose and repair ProtoMegaBot's repeated long-form
  generation-without-delivery failure in the Bot Philosophy group. Acceptance:
  identify the failing layer from session/runtime logs, apply a scoped fix with
  focused regression coverage, restart only the verified ProtoMegaBot runtime
  if required, and obtain a successful bounded end-to-end response canary.
  Root cause fixed in OmegaClaw-Core commit `bd6130b`; 5/5 focused tests pass
  and the verified supervisor is healthy after restart. Remaining acceptance
  check: one live addressed complex-turn retry must deliver both acknowledgement
  and substantive answer. Evidence path:
  `projects/omegaclaw/artifacts/protomegabot-generation-repair-20260719.md`.

- [x] 2026-07-19: Bind the provider-free disposition split report to its exact
  canonical synthetic input using `input_corpus_sha256`. Assignment remains
  independent of labels, reviewer metadata, and record ordering, while any
  change to those fields is now visible in report provenance. Gate: 12/12 unit
  tests, fixture replay, compile, JSON parse, and diff checks pass. No
  operational collection, runtime wiring, or canary is authorized.

- [x] 2026-07-19: Bind provider response messages to the assistant role on
  `agent/threadkeeper-hardening-next` commit `e01fb92`. Explicit
  user/system/tool, empty, boolean, and numeric message roles fail closed as
  authenticated `provider_response_invalid` outcomes without retry; omitted
  roles remain compatible. Focused checks: 12 passed; combined provider-free
  subagent/budget gate: 428 passed.

- [x] 2026-07-19: Bind OpenAI-compatible responses to the requested model on
  `agent/threadkeeper-hardening-next` commit `0c44829`. Explicit mismatched,
  empty, boolean, and numeric model values fail closed as authenticated
  `provider_response_invalid` outcomes without retry; omitted metadata remains
  compatible. Focused checks: 8 passed; combined provider-free
  subagent/budget gate: 416 passed.

- [x] 2026-07-19: Harden the provider-free disposition-corpus split
  preregistration against malformed provenance and correlated duplicates. The
  gate now requires the pinned input schema and canonical hexadecimal SHA-256
  task digests, and rejects duplicate task-version provenance before assigning
  deterministic 60/20/20 splits. Gate: 11/11 unit tests, fixture replay,
  compile, and diff check pass. This grants no authority to collect operational
  evidence, wire runtime behavior, or run a canary.

- [x] 2026-07-19: Bind native-provider responses to the requested model on
  `agent/threadkeeper-hardening-next` commit `476a475`. Explicit mismatched,
  empty, boolean, and numeric response model values now fail closed as
  authenticated `provider_response_invalid` outcomes without retry; omitted
  model metadata remains compatible. Focused checks: 6 passed; combined
  provider-free subagent/budget gate: 412 passed.

- [x] 2026-07-19: Reject explicitly truncated native-provider completion
  reasons on `agent/threadkeeper-hardening-next` commit `a83f0a4`. Ollama
  responses with `done=true` but non-`stop` `done_reason` now fail closed as
  authenticated `provider_response_invalid` outcomes without retry. Missing
  `done_reason` remains compatible for older providers. Focused checks: 8
  passed; combined provider-free subagent/budget gate: 408 passed.

- [x] 2026-07-19: Reject explicit provider refusal/error signals on
  `agent/threadkeeper-hardening-next` commit `b9b547c`. Native Ollama
  `error` responses and OpenAI-compatible message `refusal` responses now
  fail closed as authenticated `provider_response_invalid` outcomes without
  retry, even when they carry tool-shaped content. Focused checks: 2 passed;
  combined provider-free subagent/budget gate: 406 passed.

- [x] 2026-07-19: Require explicit provider completion markers on
  `agent/threadkeeper-hardening-next` commit `533f671`. Native Ollama must
  return `done=true`, and OpenAI-compatible responses must return
  `finish_reason=stop`; omitted/null markers fail closed as authenticated
  `provider_response_invalid` outcomes without retry. Focused checks: 6
  passed; combined provider-free subagent/budget gate: 404 passed.

- [x] 2026-07-19: Harden disposition-corpus reviewer independence before any
  operational evidence selection. Reviewer/adjudicator identities must now be
  distinct, nonempty scoped pseudonyms; empty, non-string, and unscoped values
  fail closed. Gate: 15/15 unit tests, fixture replay, compile, and diff check
  pass. This does not authorize corpus collection, runtime wiring, or a canary.

- [x] 2026-07-19: Reject explicitly unfinished provider responses on
  `agent/threadkeeper-hardening-next` commit `5bfa906`. Native Ollama
  `done=false` and OpenAI-compatible non-`stop` finish reasons now become
  authenticated `provider_response_invalid` outcomes without retry, so
  truncated partial text cannot enter the worker tool protocol. Focused
  checks: 4 passed; combined provider-free subagent/budget gate: 400 passed.

- [x] 2026-07-18: Reject deprecated provider-native `function_call` payloads
  on `agent/threadkeeper-hardening-next` commit `a25d20d`. Native Ollama and
  OpenAI-compatible compatibility payloads now fail as authenticated
  `provider_response_invalid` outcomes without retry instead of bypassing the
  existing `tool_calls` rejection. Focused checks: 4 passed; combined
  provider-free subagent/budget gate: 403 passed.

- [x] 2026-07-18: Harden the synthetic disposition-corpus preregistration
  against cross-record provenance leakage. Task-version, checkpoint, and
  evidence-packet digests must now be globally unique, preventing correlated
  duplicates from crossing a later evaluation split or inflating sample size.
  Gate: 12/12 unit tests, fixture replay, compile, and diff check pass. This
  does not authorize operational corpus collection, runtime wiring, or a
  canary.

- [x] 2026-07-18: Reject provider-native tool calls on
  `agent/threadkeeper-hardening-next` commit `99622d0`. Ollama-native and
  OpenAI-compatible tool-call payloads now fail as authenticated
  `provider_response_invalid` outcomes without retry instead of being silently
  ignored beside textual content. Focused checks: 10 passed; combined
  provider-free subagent/budget gate: 396 passed.

- [x] 2026-07-18: Validate OpenAI-compatible provider total-token accounting on
  `agent/threadkeeper-hardening-next` commit `cb5ea32`. When supplied,
  `usage.total_tokens` must be a non-negative integer equal to prompt plus
  completion tokens; malformed/contradictory totals fail as authenticated
  `provider_response_invalid` outcomes without retry. Focused checks: 7
  passed; combined provider-free subagent/budget gate: 394 passed.

- [x] 2026-07-18: Reject ambiguous OpenAI-compatible provider choice sets on
  `agent/threadkeeper-hardening-next` commit `e41d33f`. Responses now require
  exactly one choice; multiple choices cannot be silently reduced to the first
  or enter worker protocol. Focused checks: 3 passed; combined provider-free
  subagent/budget gate: 390 passed.

- [x] 2026-07-18: Reject missing native-provider message content on
  `agent/threadkeeper-hardening-next` commit `45239b2`. Omitted
  `message.content` now returns authenticated `provider_response_invalid`
  after one call instead of entering the worker protocol as an empty response.
  Focused checks: 5 passed; combined provider-free subagent/budget gate: 389
  passed.

- [x] 2026-07-18: Preregister the disposition operational-evidence corpus
  contract without collecting operational data. The synthetic-only validator
  binds task/checkpoint/evidence digests, requires independent reference-label
  review and redaction audit, and rejects target contamination, incomplete
  redaction, non-independent adjudication, and operational records. Evidence:
  `artifacts/ggb-capacity-gates/20260718-disposition-corpus-preregistration/`.
  This does not authorize corpus collection, runtime wiring, or a canary.

- [x] 2026-07-18: Reject falsey malformed native-provider token counters on
  `agent/threadkeeper-hardening-next` commit `486f7e8`. Explicit `false` and
  empty-string counters can no longer be normalized into valid zero usage;
  they return authenticated `provider_response_invalid` after one call.
  Focused checks: 3 passed; combined provider-free subagent/budget gate: 388
  passed.

- [x] 2026-07-18: Reject malformed native-provider JSON/UTF-8 at the trusted
  ThreadKeeper boundary on `agent/threadkeeper-hardening-next` commit
  `848f8a2`. Invalid response bytes now return authenticated
  `provider_response_invalid` after one call rather than consuming retry
  allowance. Focused provider checks: 5 passed; combined provider-free
  subagent/budget gate: 386 passed.

- [x] 2026-07-18: Run bounded disposition-score perturbation calibration on
  five preregistered synthetic admitted-evidence archetypes. The exhaustive
  `{-0.03, 0, +0.03}^4` grid covered 405 samples: four clear archetypes were
  stable in 81/81 samples each; the ambiguous stop/hold archetype adjudicated
  72/81 and otherwise resolved only to its nominal top action. No decisive
  cross-action flip occurred. Gate: 15/15 checks; 4 unit tests. Evidence:
  `artifacts/ggb-capacity-gates/20260718-disposition-perturbation-calibration/`.
  This is synthetic robustness evidence only, with no runtime authority.

- [x] 2026-07-18: Validate ThreadKeeper OpenAI-compatible response structure
  on `agent/threadkeeper-hardening-next` commit `0c26daf`. Empty/non-list
  choices and incomplete usage objects now return authenticated
  `provider_response_invalid` outcomes after one call rather than consuming
  retry allowance as transport failures. Focused provider checks: 8 passed;
  combined provider-free subagent/budget gate: 384 passed; draft PR #1
  safety-floor ancestry remains intact.

- [x] 2026-07-18: Validate ThreadKeeper provider payload types at the trusted
  boundary on `agent/threadkeeper-hardening-next` commit `9b5dc2a`. Native and
  OpenAI-compatible responses now require string content and non-negative
  integer token counters before worker parsing or quota accounting. Malformed
  content/counters return authenticated `provider_response_invalid` outcomes.
  Focused provider regressions: 4 passed; combined provider-free
  subagent/budget gate: 382 passed; draft PR #1 ancestry remains intact.

- [x] 2026-07-18: Preregister disposition-appraisal confidence/margin edge
  cases and deterministic counterexample shrinking. Five exact/adjacent cases,
  a canonical checksummed two-score counterexample to unsafe confidence-only
  selection, 8/8 gate checks, and 4 unit tests pass provider-free. Evidence:
  `artifacts/ggb-capacity-gates/20260718-disposition-threshold-counterexamples/`.
  No runtime/disposition authority; next offline slice is bounded score
  perturbation/calibration on representative admitted-evidence distributions.

- [x] 2026-07-18: Authenticate remaining ThreadKeeper provider-boundary
  failures on `agent/threadkeeper-hardening-next` commit `78a05b9`. Oversized
  native HTTP responses and missing OpenAI-compatible clients now return
  private structured provider errors rather than ordinary worker text.
  Oversized bytes cannot reach tool parsing, and the persistent transcript
  records `provider_response_invalid`. Combined provider-free subagent/budget
  gate: 380 passed; draft PR #1 safety-floor ancestry remains intact.

- [x] 2026-07-18: Authenticate ThreadKeeper provider-control outcomes at the
  structured-return boundary on `agent/threadkeeper-hardening-next` commit
  `21b8883`. Dispatch now trusts a private internal marker rather than
  worker-controlled string prefixes for cancellation, rate limits,
  concurrency limits, deadlines, and terminal retry failure. A provider-free
  regression proves control-shaped worker text cannot forge a cancelled
  parent return or transcript. Combined subagent/budget gate: 382 passed;
  draft PR #1 safety-floor ancestry remains intact.

- [x] 2026-07-18: Make ThreadKeeper provider retry/backoff cancellation
  responsive on `agent/threadkeeper-hardening-next` commit `fccaac8`.
  Cancellation is checked before every attempt and polled during configured
  backoff, preventing a cancelled dispatch from starting another provider
  call. Structured parent returns and persistent transcripts retain
  `status=cancelled`. Combined provider-free subagent/budget gate: 381 passed;
  draft PR #1 safety-floor ancestry remains intact.

- [x] 2026-07-17: Make ThreadKeeper task-contract `forbidden_actions`
  fail closed on unenforceable identifiers. Commit `3353e80` centralizes the
  enforced tool/action aliases and rejects unknown or misspelled actions before
  worker/provider setup. Focused contract tests: 7 passed; combined provider-
  free subagent/budget gate: 379 passed. Draft PR #1 safety-floor ancestry
  remains intact.

- [x] 2026-07-17: Reject unsupported ThreadKeeper Markdown tilde-fence
  markers before tool effects on `agent/threadkeeper-hardening-next` commit
  `3175ab4`. A response containing a tilde fence now fails complete-batch
  preflight, including when a valid write appears earlier in the same batch.
  Focused fence regressions: 7 passed; combined provider-free subagent/budget
  gate: 372 passed. Draft PR #1 safety-floor ancestry remains intact.

- [x] 2026-07-17: Implement the provider-free handoff-blocked disposition appraisal gate
  specified in `GGB_DISPOSITION_APPRAISAL_GATE.md`: five synthetic fixtures,
  exact task/manifest/checkpoint and selected-memory provenance, deterministic
  GoalChainer-style four-action ranking, ambiguity-to-adjudicated-`hold`, and
  proof that appraisal cannot write ThreadKeeper state or memory. The archived
  artifact at `artifacts/ggb-capacity-gates/20260717-threadkeeper-disposition-appraisal/`
  passes 18/18 checks and 5 unit tests, including content-digest-bound
  evidence provenance and effect negatives.
  This is an artifact-only recommendation path, not a runtime bridge or live canary.

- [x] 2026-07-17: Reject malformed ThreadKeeper Markdown fence envelopes
  before tool effects on `agent/threadkeeper-hardening-next` commit `79bfd4d`.
  Unclosed, nested, ambiguous bare, and unsupported fence markers can no
  longer expose tool-shaped lines to the tolerant parser, and a final `emit`
  inside an unclosed fence is rejected. Well-formed fenced calls remain
  compatible. Six provider-free regressions added; combined subagent/budget
  gate: `370 passed`.

- [x] 2026-07-17: Add explicit auditable operator dispositions for a
  persistent task blocked by a missing formal handoff. Commit `f09c621` adds
  bounded immutable self-hashed `hold`, `request_cancel`, `fail_terminal`, and
  `expire` records bound to the exact task version, manifest, newest opaque
  checkpoint, actor, rationale, and evidence references. Records precede any
  lifecycle effect, survive event-write crashes, replay idempotently, and can
  neither fabricate a handoff nor enqueue work. Lifecycle suite: `62 passed`;
  combined provider-free gate: `375 passed`; evidence:
  `experiments/20260717T210750Z-threadkeeper-operator-dispositions/`.

- [x] 2026-07-17: Prove that a crash-before-handoff task remains fail-closed
  across repeated ThreadKeeper supervisor passes. Commit `8c106b6` adds a
  provider-free regression in which two passes return the same
  `handoff_required` outcome, leave the task `FAILED_RETRYABLE`, and cause zero
  enqueue effects. Lifecycle suite: `57 passed`; combined gate: `370 passed`;
  evidence:
  `experiments/20260717T193500Z-threadkeeper-handoff-restart-stability/`.
  Next bounded gate is an explicit operator recovery/disposition policy; do
  not fabricate a handoff or silently reuse an older checkpoint.

- [x] 2026-07-17: Require the current attempt's newest formal handoff before
  ThreadKeeper resumes a `WAITING_INPUT` task from an inbox item. Commit
  `50aaaa2` verifies the full checkpoint chain before enqueue or consumption-
  receipt replay; missing handoffs and a newer opaque checkpoint fail without
  a queue effect and leave the task waiting. Combined provider-free gate:
  `369 passed`; evidence:
  `experiments/20260717T190841Z-threadkeeper-waiting-input-handoff/`.

- [x] 2026-07-17: Incorporate formal resume/handoff records into ThreadKeeper
  persistent workers. The first bounded slice adds strict
  `threadkeeper.persistent-worker.handoff.v1` snapshots inside immutable
  checkpoint chains, deterministic latest-handoff projection,
  manifest/checkpoint/handoff digest binding, resume exposure, and
  provider-free positive/negative tests. The handoff records role, observed
  model identity, current state, exact pickup point, constraints, hazards,
  completed work, next steps, blockers, and evidence references; it is
  evidence, not authority. Local commit `b6be4ea`; combined provider-free gate
  `364 passed`; evidence:
  `experiments/20260717T154004Z-threadkeeper-formal-handoff-v1/`.

- [x] 2026-07-17: Require a formal handoff at ThreadKeeper persistent retry
  requeue boundaries and test full process-death reconstruction. Commit
  `35bf3b1` rejects an empty checkpoint chain or a newest generic checkpoint
  before enqueue, surfaces `handoff_required` while retaining
  `FAILED_RETRYABLE`, and preserves generic checkpoints during an active
  attempt. A provider-free three-interpreter fixture reconstructs the next
  action only from the verified manifest/checkpoint/handoff chain and the
  handoff-referenced project file. Combined lifecycle/subagent/budget gate:
  `367 passed`; evidence:
  `experiments/20260717T171207Z-threadkeeper-handoff-requeue-resume/`.

- [x] 2026-07-17: Stop ProtoMegaBot's repeated 503 channel spam without an
  automatic Fable fallback. Commits `fb36d35`, `a9c0060`, and `74e46d2` drop
  sibling/unaddressed bot traffic at ingress, suppress transient diagnostics,
  add a five-minute model cooldown, and use only the healthy inexpensive
  `protomegabot-simple` route for automatic overload fallback. Focused tests:
  4 overload-policy and 8 address/ingress cases; Python compilation, shell
  syntax, and diff checks passed. Live supervisor restarted with one worker.

- [x] 2026-07-17: Reject malformed ThreadKeeper `<think>` envelopes before
  tool effects on `agent/threadkeeper-hardening-next` commit `5ce53aa`.
  Unclosed, stray, and nested reasoning markers can no longer expose a
  tool-shaped line to the tolerant parser, and an `emit` inside an unclosed
  block is rejected. Well-formed blocks remain compatible. Five provider-free
  regressions added; combined subagent/budget gate: 369 passed.

- [x] 2026-07-17: Make over-quota ThreadKeeper worker batches effect-free on
  `agent/threadkeeper-hardening-next` commit `4fa20bc`. Complete-batch
  preflight now rejects responses that exceed the per-turn or remaining
  dispatch/task-contract tool quota before an earlier valid mutation can run.
  Provider-free quota regressions updated; combined subagent/budget gate: 364
  passed.

- [x] 2026-07-17: Make unauthorized ThreadKeeper worker batches effect-free on
  `agent/threadkeeper-hardening-next` commit `63a63d3`. Complete-batch
  preflight now rejects later tools outside the dispatch subset and file calls
  outside task-contract `allowed_paths` before an earlier valid write can run.
  Provider-free regressions updated/added; combined subagent/budget gate: 359
  passed.

- [x] 2026-07-17: Reject unknown ThreadKeeper worker tool names during
  complete-batch preflight on `agent/threadkeeper-hardening-next` commit
  `8936cab`. A valid earlier `write-file` no longer runs before a later
  invented tool is rejected. Direct and dispatch regressions are provider-free;
  combined subagent/budget gate: 357 passed.

- [x] 2026-07-17: Make malformed ThreadKeeper tool batches effect-free on
  `agent/threadkeeper-hardening-next` commit `1ef286a`. The full batch's
  argument shapes are preflighted before the first tool call, and malformed
  parenthesized records that parsing would otherwise skip now reject the turn.
  Two provider-free regressions prove an earlier valid `write-file` is not
  applied when a later call is malformed. Combined subagent/budget gate: 355
  passed.

- [x] 2026-07-16: Preserve rejected malformed ThreadKeeper worker evidence
  safely on `agent/threadkeeper-hardening-next` commit `5342db5`. Lone Unicode
  surrogates in provider responses/tool results are converted to visible
  literal escapes before bounded history, the next prompt, structured returns,
  or UTF-8 transcript/checksum persistence. A two-turn provider-free regression
  proves a rejected `write-file` payload has no filesystem effect and the
  recovered run retains its auditable transcript. Combined subagent/budget
  gate: 353 passed.

- [x] 2026-07-17: Archive the artifact-only ProtoMegaBot2 persistent-worker
  canary contract at
  `artifacts/ggb-capacity-gates/20260717-protomegabot2-persistent-canary-contract/`.
  The draft pins artifact-local roots, a fake loopback provider, zero egress,
  one synthetic task, strict attempt/token/tool/runtime caps, cancel/stop
  paths, expected evidence, rollback, and production-root exclusions. Contract
  validation plus six negative tests pass; launch preflight intentionally
  fails closed because explicit Ben approval/scope is absent. No launch or
  runtime wiring occurred.

- [x] 2026-07-16: Reject non-encodable surrogate code points in all
  ThreadKeeper tool arguments on `agent/threadkeeper-hardening-next` commit
  `31e2ebf`. This closes the remaining `write-file` / `append-file` content
  gap before tool, audit, or filesystem effects while preserving valid
  multiline content. Two focused no-effect regressions added; combined
  provider-free subagent/budget gate: 352 passed.

- [x] 2026-07-16: Bind ThreadKeeper worker LLM retries to the dispatch
  wall-clock deadline on `agent/threadkeeper-hardening-next` commit `4b4524a`.
  Provider timeouts now use the smaller per-call/remaining-dispatch budget,
  retry backoff is capped by the remaining deadline, no new attempt begins
  after expiry, and late provider results fail as `dispatch_timeout` rather
  than being accepted. Focused timeout/retry tests: 7 passed; combined
  provider-free subagent/budget gate: 350 passed.

- [x] 2026-07-16: Close ThreadKeeper persona configuration schemas on
  `agent/threadkeeper-hardening-next` commit `150b185`. Unknown/misspelled
  fields now fail during config load before escalation/provider setup, while
  the existing `notes` metadata field remains supported only as bounded,
  control-free text. Focused persona-config tests: 39 passed; combined
  provider-free subagent/budget gate: 347 passed.

- [x] 2026-07-16: Enforce exclusive persistent-supervisor ownership on
  isolated ThreadKeeper commit `e7e997e`. Every bounded reconciliation pass
  takes a non-blocking root-scoped OS file lock before preflight/callbacks;
  concurrent callers and hosts without locking fail closed before effects. A
  two-interpreter contention fixture proves the loser emits no queue/runner
  effect and the owner emits exactly one enqueue. Combined provider-free gate:
  362 passed. Next: a deployed wrapper/canary only under separate approval.

- [x] 2026-07-16: Add a provider-free persistent-supervisor subprocess restart
  harness on isolated ThreadKeeper commit `c06725e`. Three independent Python
  interpreters create an expired claimed attempt, recover/requeue it, and
  restart with cancellation asserted. The gate verifies durable `QUEUED`
  state, exactly one enqueue, and zero runner effects; combined gate: 361
  passed. Next: exclusive supervisor ownership/concurrent invocation.

- [x] 2026-07-16: Tighten ThreadKeeper persona resource/tool defaults on
  `agent/threadkeeper-hardening-next` commit `619e223`. Persona
  `max_output_tokens` is now a strict positive integer capped by
  `OMEGACLAW_SUBAGENT_MAX_OUTPUT_TOKENS` (default 8,192), and configured
  `default_tool_subset` values must be non-empty bounded lists of safe,
  registered v1-callable tools. Invalid values fail during config load before
  escalation/provider setup. Combined provider-free subagent/budget gate: 342
  passed.

- [x] 2026-07-16: Implement the first bounded persistent-worker supervisor
  reconciliation pass on isolated ThreadKeeper commit `3673e94`. It preflights
  all durable state before callbacks and passes synthetic restart/requeue,
  cancellation-before-effect, corrupt-state fail-closed, and exhausted-budget
  fixtures. Combined provider-free/focused gate: 360 passed. Next: a separate
  subprocess restart harness; no ProtoMegaBot/ProtoMegaBot2 wiring yet.

- [x] 2026-07-15: Implement the first focused Phase 1 slice of the multi-agent chat-room identity/routing design in OpenClaw. Pinned OpenClaw `v2026.7.1`, added Telegram `InboundEnvelope`/`SelfContext`, deterministic `DIRECT|SECONDARY|GROUP|INCIDENTAL` classification, and structured prompt injection with resolved workspace. Local branch `agent/chat-room-identity-phase1`, commits `4c8cc1f5`, `4d234b80`, and `2e0ed9e0`. Parent review corrected mention/reply conflict handling so explicit mentions win, fixed extension-lint findings, and removed an unconditional `INCIDENTAL` pre-generation skip that contradicted the v2 always-attending contract. Thirty-two focused Telegram tests and 75 inbound-metadata tests pass; core type check, extension lint, formatting, and diff check pass. No push/deploy. Remaining Phase 1 work: decide whether `SECONDARY`/`GROUP` need a new trusted runtime policy seam before Phase 2 introduces `SUPPRESS`.

- [x] 2026-07-15: Accept the bounded communication topology and redesign the
  channel watchdog without widening tree-scoped session visibility. Added a
  read-only local-journal scanner with five synthetic regressions; forced cron
  validation returned `ok`/silent. The separate allowlisted Telegram bot and
  adjudication-gated ThreadKeeper queue/GoalChainer sidecar remain the approved
  boundaries; no unrestricted direct bridge was enabled.
- [ ] Evolve ThreadKeeper into a native persistent-worker system while preserving existing bounded synchronous `delegate` semantics. Accepted mandate 2026-07-15. Architecture/spec: `worktrees/threadkeeper-persistent-workers/docs/persistent-workers.md`; isolated branch/worktree: `agent/threadkeeper-persistent-workers` at base `a2c62eb`. Provider-free lifecycle/status records and MeTTa policy are committed at `7aa49e1`; durable manifests/events/status APIs at `f82d168`; spawn/cancel and causal intervention surfaces at `aa33f7a`; immutable attempt leases, bounded hash-linked checkpoints, and fail-closed/idempotent stale-attempt recovery recording at `43d34fe`; separate explicit lineage-verified requeue effect at `9727ad7`; verified checkpoint-to-next-attempt handoff at `1b2d670`; bounded immutable manifest-bound enqueue receipts at `29948e9`; durable task-level budget ledger and pre-effect exhaustion gates at `4b7399e`; crash-retry-safe completed-attempt token accounting at `fed6c2a`; bounded immutable inbox storage at `66b249a`; explicit crash-retry-safe inbox consumption/requeue receipts at `dc8dd79`; bounded event-bound terminal-result delivery and idempotent parent acknowledgement at `bf5cf10`. Delivery polling verifies the current terminal event, exact result payload digest, immutable delivery receipt, and any separate self-hashed acknowledgement; stale events, substitution, conflicts, and tampering fail closed. Mechanically observed token/tool/runtime accounting is implemented at `c1f7b57` and documented at `a756315`; immutable result receipts bind all five counters before one idempotent ledger append. Bounded supervisor reconciliation is implemented at `3673e94`; subprocess restart persistence is tested at `c06725e`; fail-closed exclusive ownership and concurrent-process exclusion are implemented at `e7e997e`. The provider-free lifecycle suite passes 49 tests and the combined lifecycle/subagent/budget gate passes 362 tests. Next: an isolated ProtoMegaBot2 canary only under separate approval. ProtoMegaBot production, shared mutable state, paid compute, and live providers are out of scope without separate authorization.

- [x] Harden ProtoMegaBot's model-output and Telegram-delivery pipeline after the 2026-07-14 silent Ship-of-Theseus reply loss. Implemented a versioned JSON reply/action envelope plus strict legacy compatibility, full-batch allowlist/arity validation, one bounded formatter repair, visible failure when a human reply is required but absent, correlation-ID message identity, untrusted history separation, continuation-safe queueing, delivery-success deduplication, chunk retry progress, and poll-independent sends. Archived the 5.6-sol consultation and implementation specification under `docs/`. Coherent isolated commit: `a16e714` on `agent/protomega-output-pipeline-hardening`; integrated and deployed to the live dirty runtime without disturbing unrelated edits. Validation: helper assertions, Python compile, MeTTa parse, and all 31 focused test bodies passed; only the repository's unconditional Docker cleanup hook errored because Docker is unavailable. Runtime restarted cleanly with no poll/send/traceback errors. The supervisor's stale MTProto-only readiness check was also made transport-aware and now correctly reports the active one-worker/zero-bridge Bot API topology as process-ready. Remaining reliability work is durable inbound journaling and crash-persistent delivery receipts, followed by a human Telegram canary.
- [x] Adopt Gödel Oruži's GGB Capacities Curriculum v0.1 as a rough medium-term roadmap for upgrading `@Protomegabot` intelligence step by step. First pass recorded in `GGB_CAPACITIES_ROADMAP.md`: maps 25 working capacities to OmegaClaw/ThreadKeeper/PeTTa-memory/`petta-chem` anchors, near-term empirical gates, and next implementation tasks. Keep each upgrade empirical/testable rather than aspirational. 2026-07-01 12:30 PDT cron updates added `GGB_CAPACITY_GATE_TEMPLATE.md`, refreshed the roadmap with local ThreadKeeper hardening / `petta-memory` / `petta-chem` progress, archived the ThreadKeeper partial gate at `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/RUN.md`, the `petta-memory` bounded prompt/index/PLN partial gate at `artifacts/ggb-capacity-gates/20260701-petta-memory-prompt-view/RUN.md`, and the `petta-chem` run-contract reuse partial gate at `artifacts/ggb-capacity-gates/20260701-petta-chem-run-contract/RUN.md`. 2026-07-01 16:30 PDT cron added `.metta` sibling fixture files (`CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`) for the `20260701-petta-chem-run-contract` gate following the `GGB_GATE_RUN_CONTRACT_MAPPING.md` field mapping; verified required-files check, single `run-summary`, `ggb-check` coverage against `RUN.md`, and re-ran source checks (`run_exp02.sh`, `test_exp02_contract_files.sh`, `git diff --check` all pass). 2026-07-01 20:42 PDT cron added `local/check-ggb-gate-fixtures.py` and archived `artifacts/ggb-capacity-gates/20260702-ggb-fixture-smoke/RUN.md`; the checker passes on the `petta-chem` GGB fixture (required files balanced, one top-level `run-summary`, 3 `RUN.md` checks covered by 4 `ggb-check` atoms), and the roadmap now reflects `petta-memory` 53-test/PeTTaChainer-candidate status plus `petta-chem` seed-37/twenty-seven-record folded-summary progress. 2026-07-02 00:38 PDT cron applied the same `.metta` sibling fixture pattern to the ThreadKeeper hardening gate (`CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`) and verified both fixtures with `local/check-ggb-gate-fixtures.py`; ThreadKeeper focused mock pytest also passes locally via `local/threadkeeper-pytest-venv` (`28 passed`). 2026-07-02 04:39 PDT cron applied the same sibling fixture pattern to the `petta-memory` OmegaClaw-style prompt/index fixture gate and improved the checker to recognize both `## Checks run` and `## Checks`; checker passes across all three gate fixtures, and `petta-memory` unittest passed 64 tests. 2026-07-02 08:37 PDT cron refreshed the roadmap/gate fixture with ThreadKeeper head `c3e836b` provider-fail-closed evidence (focused mock pytest now 31 passing tests) and current `petta-memory` PeTTaChainer profiling status (67 stdlib tests; compile/add bottleneck is the next narrow task). 2026-07-03 00:35 PDT cron refreshed the roadmap and ThreadKeeper gate fixture for Phase 3 audit/accounting evidence at head `554fb85`: dispatch wall-clock timeout plus `worker_token_usage` are now mapped to GGB capacities 3.2/3.5/5.2, focused mock pytest passes 40 tests, and the sibling-fixture checker passes across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gates. 2026-07-03 02:21 PDT cron added ThreadKeeper head `d0c887d` hash-chained `index.jsonl` audit entries (`previous_entry_sha256` / `entry_sha256`), refreshed the roadmap/gate fixture, and verified focused mock pytest at 41 passing tests plus the same four-gate fixture checker. 2026-07-03 04:37 PDT cron refreshed the roadmap/gate fixture for ThreadKeeper head `f77ac1b` patch-proposal-only task contracts, mapping it to GGB capacity 4.5; focused mock pytest passes 43 tests and the four-gate fixture checker passes. 2026-07-03 08:38 PDT cron refreshed the roadmap/gate fixture again for ThreadKeeper queue-only dispatch (`a33b1e3`), optional adjudicator gate (`09899a0`), and documentation head `1c001e4`; focused mock pytest passes 47 tests and the four-gate fixture checker passes. 2026-07-03 12:37 PDT cron refreshed the roadmap/gate fixture for queued-worker primitive (`8eae787`) and bounded operator-supervised queue drain (`ec17402`); focused mock pytest passes 51 tests and the four-gate fixture checker passes. 2026-07-03 14:03 PDT cron pushed ThreadKeeper commit `5a472cd` to retain failed queued-worker claims as `*.failed` plus compact `*.failed.result.json` audit sidecars, refreshed the roadmap/gate fixture, and verified focused mock pytest at 52 passing tests. 2026-07-03 16:03 PDT cron pushed ThreadKeeper commit `38ae193` to ignore retained `*.done.result.json` / `*.failed.result.json` audit sidecars when listing/counting pending queue tasks, preventing false drain/backpressure after failed-claim retention; focused mock pytest still passes 52 tests. 2026-07-03 16:39 PDT cron added ThreadKeeper commit `ee883ce` (`Add subagent candidate review helper`), later pushed with commit `b14ade5` (`Add subagent run index verifier`): `review_subagent_candidate(transcript_path)` verifies transcript checksum sidecars and reports patch-proposal/adjudication gates without applying patches, accepting outputs, calling an LLM, draining queues, daemonizing, or changing runtime behavior; `verify_subagent_run_index(index_path=None)` now validates the compact `index.jsonl` hash chain plus recorded local transcript SHA-256s without repairing/replacing files or expanding transcripts into parent context; focused mock pytest now passes 57 tests. 2026-07-03 20:38 PDT cron refreshed the roadmap/gate fixture to head `d0d1dfa`, mapped explicit queued-worker result-sidecar rejection into capacity 4.5/5.2 audit discipline, and incorporated current `petta-memory` static-import microbenchmark evidence (88 stdlib tests, selected-space runtime fact-membership check) plus current `petta-chem` exp02/exp03 evidence (seed-107/75 exp02 records and exp03 dynamic aggregate/export atoms); focused mock pytest passes 58 tests and the four-gate fixture checker passes.
- [ ] ThreadKeeper upgrade coordination: reconcile Lila/Gödel Oruzi feedback (forwarded screenshots from Ben, 2026-06-30) with draft PR https://github.com/hlgreenblatt/ThreadKeeper/pull/1. Current PR already addresses the top safety floor: path sandbox, fail-closed budget fallback, disabled/allowlisted argv-only shell execution, and tests. Next code work should avoid duplicating that branch and target the still-open hardening items below.
- [ ] ThreadKeeper next hardening branch candidate: LLM/subagent call timeout + retry/backoff; bounded history/digesting for long-running subagents; structured returns (`summary`, `files_changed`, `tests_run`, `uncertainty`, `next_action`, `transcript_path`); persistent run/task records with full child transcript saved locally and digest returned to parent. 2026-06-30 local branch `agent/threadkeeper-hardening-next` commit `f79891c` started from PR #1 safety-floor head and implemented the timeout/retry/backoff slice with focused tests; later 2026-06-30 work added deterministic bounded history digests, JSON structured dispatch returns, and persistent local subagent transcript records under `memory/subagent-runs`/`OMEGACLAW_SUBAGENT_RUN_DIR`. 2026-07-01 pushed commit `970b519` closed the remaining early-failure record gap: setup/config/contract/provider/escalation-denial failures now return bounded JSON parent digests and persist minimal transcript records without calling worker LLMs. 2026-07-01 commit `caf3f9b` then closed the no-tool-subset/default-subset setup gap with the same structured return + transcript path. Pytest remains unavailable locally, direct assertion replay passed.
- [ ] ThreadKeeper governance/safety follow-up: per-dispatch quotas and cancellation token; task contracts (`objective`, `allowed_paths`, `forbidden_actions`, `done_criteria`); atomic file writes; make `escalation.metta` read-only or integrity-checked; validate tool-call arguments with strong types/safety checks; replace fragile cloud/local model string heuristics with explicit model/provider metadata. 2026-06-30 local branch also implemented atomic subagent `write-file`, stricter tool argument validation, per-dispatch tool-call quotas, file-based cancellation, and optional SHA-256 integrity pinning for `escalation.metta` before cloud delegation. 2026-07-01 local commit `68d7bc5` added the first task-contract enforcement slice: JSON/persona contracts are prompted, persisted, and enforced for `allowed_paths` and `forbidden_actions`, with focused tests. Local commit `f6df5ef` then made subagent `append-file` atomic too (read existing content, write temp file, fsync, `os.replace`) and added a focused test. Local commit `0b185a4` replaced the remaining base-url/model-string worker classification with explicit `node_role` and `endpoint_kind`/provider metadata, including focused tests for missing `node_role` rejection and transport selection without localhost heuristics. Local commit `2fcb0ba` added persona key validation plus optional `persona_sha256` prompt-file integrity pinning, failing closed before worker calls on mismatch. Local commit `5fdd131` aligned the committed persona examples/README with those stricter requirements and added a regression check that example configs have explicit metadata and valid prompt pins. Local commit `9b6439c` added an atomic per-endpoint worker LLM calls/minute guard with structured `rate_limited` returns. Local commit `07c8742` added a cross-process per-endpoint in-flight worker LLM concurrency guard with structured `concurrency_limited` transcript status. Local commit `34c96b4` strengthened file-write atomicity with per-target `fcntl` locks around `write-file`/`append-file` updates and refreshed the subagent reference docs. Pushed commit `a4a9b87` tightened task-contract shape further by persisting/bounding the objective and rejecting unsafe `forbidden_actions` identifiers before worker calls. Pushed commit `f1a8a70` sandboxed persona prompt paths under `PERSONA_DIR`, closing prompt-file path/symlink escape risk before worker calls. Pushed commit `0d1d0af` added transcript checksum sidecars and returns `transcript_sha256` in the structured parent digest, giving persistent run records a cheap local integrity check. Pushed commit `1d30b4b` lets task contracts include strict non-negative `max_tool_calls` to narrow the global per-dispatch tool quota, with focused tests and docs. Pushed commit `d8b922f` adds a compact locked `index.jsonl` audit listing for finished subagent run records, keyed to each transcript path and SHA-256 sidecar. Pushed commit `c3e836b` makes OpenAI-compatible provider setup fail closed before the worker loop if the local client/SDK cannot initialize, returning a structured `provider_invalid` record instead of burning turns on repeated no-client pseudo-responses. Pushed commit `24bf6bf` hardens numeric env parsing for timeout/retry, quota, digest, contract, and validation knobs: malformed values use safe defaults and below-minimum values clamp instead of crashing import or accidentally disabling guards. Pushed commit `893a0e3` fixes optional allowlisted subagent shell commands to run from `OMEGACLAW_SUBAGENT_WORKSPACE`, closes stdin, and fails closed when the workspace directory is missing, preserving argv-only/no-shell execution while tightening workspace containment. Pushed commit `8e12b18` further tightens the optional shell tool by rejecting explicit executable paths even when the basename is allowlisted, so subagents must use allowlisted command-name tokens only. Pushed commit `01fe0d8` sanitizes inherited `PATH` for optional subagent shell commands, removing empty/`.` entries and workspace-contained path entries so an allowlisted command name cannot be hijacked by a workspace-controlled executable after `cwd` is pinned to the workspace. Pushed commit `b828ebf` scrubs the optional shell child environment so allowlisted subprocesses get only sanitized `PATH`, workspace-pinned `HOME`, and locale/timezone vars rather than inherited API keys/tokens/session env; focused mock pytest now passes 36 tests. Pushed commit `94d57c9` adds a per-worker-response tool-call cap (`OMEGACLAW_SUBAGENT_MAX_TOOL_CALLS_PER_TURN`, default 3) with structured `TURN_QUOTA_EXCEEDED` / transcript status `turn_quota_exceeded`; focused mock pytest now passes 37 tests. Pushed commit `f880c50` bounds subagent `read-file` output via `OMEGACLAW_SUBAGENT_MAX_READ_FILE_CHARS` (default 20000) with explicit truncation markers and focused coverage; focused mock pytest now passes 38 tests. Pushed commit `209da6c` adds configurable JSON audit/task read cap `OMEGACLAW_SUBAGENT_MAX_JSON_FILE_BYTES` for queued task/transcript JSON reads, with focused mock pytest now passing 146 tests. Pushed commit `a258c73` adds `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_AUDIT_BYTES` to bound transcript hash reads during run-index verification; pushed commit `82f490b` adds bounded reverse-tail scanning for run-index append/rotation so finished-run appends no longer read a long unrotated `index.jsonl` into memory; focused mock pytest now passes 157 tests. Local commit `a1a1bce` makes compound invalid dispatch boundaries fail closed as one persistent structured record, so a malformed integer limit combined with non-string goal/tool subset/persona can no longer reach transcript path construction with unsafe scalar types.
- [ ] ThreadKeeper Phase 3 hardening: pushed commit `d9b9b56` adds `max_consecutive_errors` to the bounded async worker loop: the loop now tracks consecutive `queue_worker_error` results and exits early when the cap (`OMEGACLAW_SUBAGENT_ASYNC_WORKER_MAX_CONSECUTIVE_ERRORS`, default 3) is reached, preventing wasted work on a poisoned queue; `0` disables; structured returns and lock metadata now include `consecutive_errors` and `error_count`; focused mock pytest now passes 86 tests. Pushed commit `85145ea` bounds worker env-file parsing in the bounded async worker runner: env files must be regular non-symlink files, stay under 64 KiB, and have bounded line/value lengths before any env is applied or `subagent` is imported; focused mock pytest now passes 82 tests. Earlier work: pushed commit `554fb85` adds a dispatch-level wall-clock timeout (`OMEGACLAW_SUBAGENT_DISPATCH_TIMEOUT_S`, default 600s) checked before each LLM call and tool execution, returning structured `dispatch_timeout` records; adds worker token accounting (`worker_token_usage` with `input_tokens`/`output_tokens`/`total_tokens`) aggregated across all worker LLM calls per dispatch and included in both transcript records and structured parent digests; `_call_subagent_llm` now returns `(text, in_tokens, out_tokens)` tuples. Pushed commit `d0c887d` adds hash-chained compact run-index entries (`previous_entry_sha256` / `entry_sha256`) for stronger audit-list integrity; focused mock pytest now passes 41 tests. Pushed commit `f77ac1b` adds task-contract `patch_proposal_only` mode so child `write-file`/`append-file` calls record full proposed changes in transcripts without mutating workspace files, while parent digests expose bounded `{action,path}` proposal metadata; focused mock pytest passes 43 tests. Pushed commit `a33b1e3` adds queue-only subagent dispatch mode (`OMEGACLAW_SUBAGENT_QUEUE_ONLY`) with durable `queue/*.json` task records, `queue_path`/`queue_sha256` parent digests, cancellation-before-queue, and fail-closed `queue_backpressure`; focused mock pytest passes 45 tests. Pushed commit `09899a0` adds optional `requires_adjudication` task contract mode: the subagent runs normally but its final emit is treated as a candidate, returning `status=needs_adjudication` with bounded `adjudication` metadata and persisting transcript status `adjudication_required`, so a parent/supervisor can route high-stakes outputs to a review step before accepting it; focused mock pytest passes 47 tests. Pushed commit `8eae787` adds the first queued-worker primitive, `subagent.run_queued_dispatch(queue_path)`, with atomic claim, queue-record validation, queue-only suppression around the actual worker dispatch, compact result records, and `.done` audit retention; focused mock pytest passes 49 tests. Pushed commit `ec17402` adds bounded operator-supervised queue draining via `subagent.drain_queued_dispatches(max_tasks=1)`, which drains explicit queued tasks oldest-first without daemonizing/self-scheduling, while preserving queue-only env state; pushed commit `5a472cd` retains queued-worker failures after atomic claim as `*.failed` plus `*.failed.result.json` audit records; pushed commit `ee883ce` adds read-only candidate transcript review for patch/adjudication gates; pushed commit `b14ade5` adds read-only run-index hash-chain plus transcript-SHA verifier; pushed commit `d0d1dfa` rejects explicit queued-worker attempts to run retained result sidecars such as `*.done.result.json` / `*.failed.result.json`, preserving the sidecar instead of renaming it into claim/failure state; focused mock pytest passes 58 tests. Pushed commit `76bd2c4` preserves queued task contracts during worker execution; pushed commit `f916dfe` adds required checksum sidecars for queued tasks and fails closed before worker LLM calls on missing/mismatched sidecars; focused mock pytest now passes 61 tests. Ben explicitly said on 2026-07-04 that ThreadKeeper should have a real async worker loop; pushed commit `cc3cd1e` (`Add bounded queued worker loop`) adding `subagent.run_queued_worker_loop(...)`, a supervised bounded polling loop with max-task, idle-poll, runtime, stop-file, and local-lock controls. Focused mock pytest now passes 75 tests. Pushed commit `c4ae8a8` adds `scripts/run-subagent-worker-loop` as the conservative operator entrypoint for the worker loop, with a script no-claim smoke test. Pushed commit `bb6c8c7` adds focused tests for `max_runtime_s` wall-clock timeout and worker-error-continuation during the loop. Pushed commit `61bce9c` validates async-worker stop-file config before lock acquisition/queue claim and returns structured `worker_config_invalid` for unsafe values; focused mock pytest now passes 76 tests. Pushed commit `10f69bf` validates explicit worker-loop bounds before lock acquisition/queue claim, returning structured `worker_config_invalid` for boolean/string/fractional integer task/idle limits, non-finite poll intervals, or negative runtime caps; focused mock pytest then passed 77 tests. Pushed commit `4812345` adds the artifact-local one-task worker-loop smoke helper plus subprocess coverage; focused mock pytest now passes 78 tests and archived direct smoke evidence shows one queued mock task drained with durable result/checksum/transcript/index records. Pushed commit `120d689` adds conservative `--env-file` support to `scripts/run-subagent-worker-loop`, with fail-closed malformed-env handling, docs, focused tests, and an archived non-live env-file runner smoke (`20260705-threadkeeper-worker-env-runner`) returning `worker_idle` / zero tasks attempted; focused mock pytest now passes 80 tests. Pushed commit `9e9dda2` rejects process-control keys (`PATH`, `PYTHONPATH`, `PYTHONHOME`, `LD_*`, `DYLD_*`, `BASH_ENV`, `ENV`, `HOME`, `IFS`, `SHELL`) from runner env files before importing `subagent`, with subprocess regression coverage; focused mock pytest now passes 81 tests. Pushed commit `225d441` bounds the worker loop returned results list via `OMEGACLAW_SUBAGENT_ASYNC_WORKER_MAX_RESULTS` (default 16, 0 disables) with `results_truncated` count, and adds live `tasks_attempted`/`tasks_completed`/`consecutive_errors`/`error_count` to the running lock metadata updated after each task; focused mock pytest now passes 89 tests. Next live step: staged install/smoke under @Protomegabot config, initially conservative/supervised.
- [ ] Optional/recommended: rotate the `@Protomegabot` token in BotFather when convenient. Ben explicitly accepted skipping rotation on 2026-06-27, so this is no longer a blocker for supervised testing.
- [ ] Review/adjust local Landlock policy before any non-mock long-running OmegaClaw session.

## Next

- [x] Refresh the GoalChainer↔ThreadKeeper contract against the proven canary boundary and extract a concise empirical work queue. `docs/GOAL_TASK_STATE_CONTRACT.md` v0.2 now requires patch-proposal-only/adjudication-required candidates, excludes forbidden/non-actionable/malformed results before queueing, and treats offline acceptance as evidence-only. `GGB_NEXT_GATES.md` prioritizes artifact-only adapter conformance, immutable memory→appraisal replay, then a neutral cross-domain gate schema. Focused canary policy tests pass (`3 passed`). Next implementation: add malformed/duplicate action-ID and missing-evidence negatives to the artifact-only adapter validator; no live queue/provider/Telegram/runtime path.

- [x] GoalChainer real petta-memory replay gate: archived `artifacts/ggb-capacity-gates/20260709-goalchainer-real-petta-memory-replay/`, replacing the prior private-task sidecar's Python-constructed synthetic STV/EC dictionaries with a bounded production `MediumMemoryStore.goalchainer_handoff_cache()` export. A 1,273-byte copy of the previously archived petta-memory journal yielded two allowlisted provenance-bearing STV/EC items for one archived Protomegabot decision candidate; local deterministic `solve_incident(memory_items=...)` passed 9/9 checks, recommended `publish_redacted_summary`, kept raw logs forbidden/blocked, and left the journal hash unchanged. Verification: petta-memory focused 53/full 430 tests; GoalChainer focused 52 tests; compile, JSON, fixture, and diff checks passed. No live bridge, Telegram/provider/supervisor, queue claim, memory write/promotion, secrets, paid compute, or push.

- [ ] GoalChainer future semantic-memory phase (not implemented): design an explicitly bounded/reviewed LLM step that maps selected task text to logical expressions for AtomSpace insertion, then add ECAN-like attention allocation and long-term-importance/staleness-based retention/removal. Keep all provider calls, memory writes, and live wiring separately approval-gated.

- [ ] OmegaClaw late-extension follow-up: implement a truly bounded/lazy live loader for deontic/directive/GoalChainer paths. Current `lib_extensions.metta` status hook is installed and reports configured heavy extensions as `deferred`, because an opt-in smoke showed in-loop `import!` can still pin SWI even though top-level deontic tests pass. Prefer a Prolog-backed API route or subprocess-bounded/lazy import before enabling live in-process deontic/directive loading.
- [x] Test Telegram adapter in a private/direct chat before any group use.
- [x] Inspect MesTTo `OmegaClaw-GoalChainer` (`https://github.com/MesTTo/OmegaClaw-GoalChainer`) as a possible goal/motivation and norm-aware decision layer for `@Protomegabot`, potentially alongside `petta-memory` and PeTTaChainer. Produced `GOALCHAINER_INTEGRATION_MAP.md` and archived intake gate `artifacts/ggb-capacity-gates/20260702-goalchainer-intake/RUN.md` at inspected commit `23f49515b1556ce04981f74bde4b56ee0a4375c6`. Result: architecture is relevant, but not live-ready; local tests reproduce PeTTaChainer `compileadd` stack-limit failure and one directive ready-task assertion failure. No runtime integration made.
- [x] GoalChainer next non-live gate: built a bounded local incident-decision harness with explicit local PeTTa/SWI paths and a documented heuristic acceptability fallback instead of live PeTTaChainer compile/add. Archived `artifacts/ggb-capacity-gates/20260702-goalchainer-incident-harness/RUN.md` and `report.json`. Result: recommends `publish_redacted_summary`, relation-level deontic-to-task-state classification maps it to `ready`, but local `derive_deontic` produced unregulated statuses so the harness used the documented policy fallback, and full OmegaClaw `lib_directive` generated-plan status/next/claim remains failing/empty. No live integration made. 2026-07-06 cron fixed deontic/directive runtime seams (cloned `omegaclaw-deontic`, installed into OmegaClaw-Core, created PeTTa symlink) and then bypassed the PeTTaChainer `compileadd` bottleneck entirely with `heuristic_beliefs.py`: a heuristic PLN belief grader using subjective-logic fusion on the same rule semantics. Full `solve_incident` pipeline now runs end-to-end: `publish_redacted_summary` recommended/obligated, `publish_raw_log` blocked/forbidden, `hold_external_update` weak/permitted. All 35 tests pass (0 failures, up from 9 failures). Archived `artifacts/ggb-capacity-gates/20260706-goalchainer-deontic-directive-fix/` and `artifacts/ggb-capacity-gates/20260706-goalchainer-heuristic-pln-bypass/`.
- [x] GoalChainer OmegaClaw skill surface non-live smoke: ran the full pipeline through both the Python CLI skill surface (`omegaclaw_skill.py` for `goalchainer-decision`, `goalchainer-solve`, `goalchainer-directive`) and the actual MeTTa skill surface via PeTTa/SWI (`run_in_omegaclaw.metta` with `(eval (goalchainer-decision ...))` and `(eval (goalchainer-solve ...))`). All four entry points produce correct outputs: `publish_redacted_summary` recommended (obligated, score 1.010), `publish_raw_log` blocked (forbidden), `hold_external_update` weak (permitted); solve produces redacted artifact with leak check safe=True; directive maps to ready/blocked/backlog task states with responder claim. Test suite: 35 passed, 6 skipped, 0 failed. Archived `artifacts/ggb-capacity-gates/20260706-goalchainer-skill-surface-smoke/` with `.metta` sibling fixtures; GGB fixture checker passes across all 18 gate fixtures.
- [x] GoalChainer petta-memory evidence bridge: implemented `grade_beliefs_heuristic_with_memory()` in `heuristic_beliefs.py` that accepts `petta-memory` handoff cache items (STV atoms and EvidencePacket EC atoms) and fuses them with keyword-derived ground facts using subjective-logic combination. Added `parse_memory_evidence()` and `MemoryEvidenceItem` dataclass. Extended `reason_over_hyperbase()` and `solve_incident()` with optional `memory_items` parameters. 18 new tests pass; full suite 53 passed, 6 skipped, 0 failed (up from 35/6/0). `petta-memory` 6 passed, 0 failed (no regressions). Archived `artifacts/ggb-capacity-gates/20260706-goalchainer-memory-evidence-bridge/` with `.metta` sibling fixtures; GGB fixture checker passes across all 19 gate fixtures. No live Telegram/OmegaClaw runtime integration, secrets/access/security changes, paid compute, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.
- [x] GoalChainer read-only sidecar gate: archived `artifacts/ggb-capacity-gates/20260707-goalchainer-readonly-sidecar-private-task/` over one captured/private ThreadKeeper OpenClaw smoke fixture plus synthetic read-only `petta-memory` STV/EC evidence. Harness passed 8/8 checks; focused GoalChainer memory tests passed (`52 passed`) with explicit local PeTTa/SWI env; redacted summary remained recommended, raw log remained forbidden/blocked, and memory shifted belief strengths without live runtime integration. Follow-on queue-mediated/adjudicated contract gate is archived at `artifacts/ggb-capacity-gates/20260707-goalchainer-queue-sidecar-contract/`. Follow-on queue artifact harness is now archived at `artifacts/ggb-capacity-gates/20260707-goalchainer-queue-sidecar-artifact/`: materialized a ThreadKeeper queue task, wrote checksum sidecar, ran GoalChainer locally over selected read-only memory evidence, patched `subagent.dispatch` in-process to avoid provider/runtime side effects, and exercised `run_queued_dispatch` claim/done/result/checksum path returning `needs_adjudication`. Harness passed 9/9; fixture checker and compile passed. Follow-on offline adjudicator gate is archived at `artifacts/ggb-capacity-gates/20260708-goalchainer-sidecar-offline-adjudicator/`: 12/12 artifact checks accepted the redacted-summary candidate for offline evidence only while explicitly not approving Telegram posting, memory writes, provider calls, supervisor launch, or runtime bridge changes. Next: replay the reusable reviewer policy/threshold fixture on a second candidate when available, or ask Ben for explicit private Telegram opt-in approval with stop conditions before live bridge changes.
- [ ] ThreadKeeper @Protomegabot staged install/smoke: wire the new bounded async worker loop (`cc3cd1e`, `subagent.run_queued_worker_loop(...)`) into a conservative supervisor/config path, then run local non-Telegram smoke, private-chat smoke, and supervised group/channel smoke before calling it live-ready. 2026-07-04 21:02 PDT cron completed the first non-live no-claim operator-script smoke at `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-loop-smoke/`: focused mock pytest passed 77 tests at head `10f69bf`, and `scripts/run-subagent-worker-loop --max-tasks 0 --max-idle-polls 1 --poll-interval-s 0 --max-runtime-s 1` returned `worker_idle` with zero tasks attempted/completed. 2026-07-04 22:06 PDT cron completed the next one-task artifact-local mock gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-loop-one-task/`: pushed ThreadKeeper commit `4812345` adding `Autotests/mock/run_worker_loop_one_task_smoke.py` plus subprocess coverage; focused mock pytest now passes 78 tests, and the direct artifact smoke returned `worker_drained` with one queued task attempted/completed, zero remaining tasks, and persisted `.done`/result/checksum/transcript/index evidence. 2026-07-05 00:03 PDT cron pushed ThreadKeeper commit `120d689` adding `--env-file` support to the worker-loop runner and archived `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-env-runner/`; focused mock pytest passes 80 tests and the env-file no-claim smoke returned `worker_idle` with zero tasks attempted. 2026-07-05 00:35 PDT cron completed that conservative non-Telegram @Protomegabot-config local wrapper/config smoke at `artifacts/ggb-capacity-gates/20260705-threadkeeper-protomegabot-config-smoke/`: added `local/run-threadkeeper-worker-loop-smoke.sh`, non-secret `protomegabot-worker.env`, `.metta` sibling fixture files, and `report.json`; the wrapper returned `worker_idle` with `max_tasks=0`, zero tasks attempted/completed, and no worker LLM/runtime integration. 2026-07-05 02:07 PDT cron completed the follow-on one-task non-live gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-protomegabot-one-task-smoke/`: added `local/run-threadkeeper-worker-loop-one-task-smoke.py`, loaded the same non-secret staging env, queued one checksum-sidecar mock task, drained it through `subagent.run_queued_worker_loop(max_tasks=1)` with a deterministic in-process fake worker response, and recorded one task attempted/completed with zero pending queue tasks. Still no live Telegram/runtime wiring, provider call, secrets, paid compute, daemon, or scheduler install. Next staged gate: adjudicate the private OpenClaw smoke candidate output, then consider staged Telegram-private integration with explicit stop conditions. Alternatively, run a multi-task or multi-persona supervisor smoke. 2026-07-05 04:36 PDT cron added `local/threadkeeper-worker-loop-supervisor.sh` and archived `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-supervisor-boundary/`: the supervisor launches the worker-loop runner with no-claim defaults, start/status/stop/log all function correctly, focused mock pytest passes 81 tests, and the GGB fixture checker passes on all 8 gate fixtures. 2026-07-05 06:03 PDT cron added the follow-on supervisor-boundary cancellation smoke at `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-supervisor-cancelled-task/`: one checksum-sidecar queued task was claimed by the separate supervised process and finished `cancelled` before worker LLM/provider use; the supervisor launch path now uses argv-array `setsid` instead of a shell-constructed command string. Focused mock pytest remains 81 passing tests. 2026-07-05 08:52 PDT, after Ben approved the ThreadKeeper smoke, completed the next controlled private/non-group provider-boundary gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-private-openclaw-smoke/`: one queued task was claimed by `run_queued_worker_loop(max_tasks=1)`, made one real local OpenClaw Gateway `/v1/chat/completions` worker call, returned `needs_adjudication` as intended, recorded 16,756 worker tokens, and retained `.done`/result/checksum/transcript evidence. No Telegram group/private message, paid compute, daemon/scheduler install, or broad live enablement. 2026-07-05 12:37 PDT cron adjudicated the private OpenClaw smoke candidate output (`ADJUDICATION.md` under that gate): all 10 adjudication checks passed, candidate accepted. Then completed a multi-task non-live gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-multi-task-smoke/`: queued 3 tasks, drained all through `subagent.run_queued_worker_loop(max_tasks=3)`, all returned `needs_adjudication`, 0 errors, hash-chain index intact, per-task transcripts/checksums/sidecars retained, worker token usage recorded per task. `.metta` sibling fixtures and GGB fixture checker pass across all 14 gate fixtures. Next staged gate: Telegram-private integration (requires explicit Ben approval and stop-condition plan) or multi-persona supervisor smoke.
- [ ] Decide real communication topology beyond private smoke: OmegaClaw ↔ Benjamin via Telegram, OmegaClaw ↔ ZeroBot/OpenClaw, and optional Telegram group.
- [x] 2026-07-02: Clean multi-chat Telegram fix for `@Protomegabot`: source `OmegaClaw-Core/channels/telegram.py` branch `agent/telegram-multi-chat` accepts multiple chat IDs, channel posts, and replies to source/default chat; live vendored adapter was patched for channel-post/no-`from` handling while preserving existing attachment/preack/custom logic. Verified source and live adapters with `python3 -m py_compile`, smoke assertions, and `git diff --check`; restarted the Telegram supervisor, whose log shows targets `-1003983157420,-5437945421`.
- [ ] Test one controlled OmegaClaw ↔ ZeroBot/OpenClaw exchange through the chosen bridge.
- [ ] Consider filing upstream issue/patch for `maxNewInputLoops=0` leaving `&nextWakeAt` uninitialized.
- [ ] Consider upstream/local config patch to make non-Docker policy paths easier.

## Waiting or blocked

- [ ] Communication boundaries for OmegaClaw and ZeroBot - owner: Benjamin/ZeroBot - 2026-06-26

## Someday or exploratory

- [ ] Docker-based install comparison, if system Docker becomes available/desired.
- [ ] Run OmegaClaw autotests locally without Docker assumptions.
- [ ] Integrate OmegaClaw lessons into `petta-chem` PeTTa runtime planning where appropriate, without merging the projects.

## Done recently

- [x] 2026-07-15: ThreadKeeper task-contract tool-quota validation. Branch
  `agent/threadkeeper-hardening-next` commit `e4481a8`. `max_tool_calls` now
  fails closed when it exceeds the global dispatch quota, and arbitrarily long
  decimal strings are rejected before Python integer conversion can escape the
  structured `contract_invalid` path. Verification: PR #1 safety-floor
  ancestry, focused quota pytest (`5 passed`), full subagent/budget hardening
  pytest (`313 passed`), Python compilation, and `git diff --check`. The lagging
  nested OmegaClaw runtime copy was not synced. No provider, live queue/runtime,
  Telegram, subprocess, paid compute, push, merge, force-push, or remote-ref
  deletion.

- [x] 2026-07-13: ThreadKeeper non-empty task-contract field hardening. Branch `agent/threadkeeper-hardening-next` commit `a2c62eb`. Blank/whitespace-only objectives and blank entries in `allowed_paths`, `forbidden_actions`, or `done_criteria` now fail closed as `contract_invalid` before provider setup or worker LLM calls instead of yielding meaningless tasks or disappearing during normalization. Verification: PR #1 ancestry, compile, focused validation pytest (`19 passed`), full focused hardening pytest (`310 passed`), and `git diff --check`. The active nested OmegaClaw runtime tree was not modified. No live runtime/provider/queue/subprocess activity, secrets/access changes, paid compute, push, merge, force-push, or remote-ref deletion.

- [x] 2026-07-13: ThreadKeeper persona/task-contract object-shape hardening. Branch `agent/threadkeeper-hardening-next` commit `22a8ade`. Persona configuration roots and persona/inline nested `task_contract` values now must be JSON objects. Non-object values fail closed before provider setup or worker LLM calls instead of raising during normalization or silently falling back to the outer goal object; malformed inline values remain in structured `contract_invalid` transcripts for audit. Verification: PR #1 ancestry, compile, focused shape pytest (`15 passed`), full focused hardening pytest (`298 passed`), and `git diff --check`. The active nested OmegaClaw runtime tree was not modified. No live runtime/provider/queue/subprocess activity, secrets/access changes, paid compute, push, merge, force-push, or remote-ref deletion.

- [x] 2026-07-13: ThreadKeeper typed task-contract objective hardening. Branch `agent/threadkeeper-hardening-next` commit `55bf691`. Inline JSON task-contract `objective` values now must be strings; null, booleans, numbers, arrays, and objects fail closed as `contract_invalid` before any worker LLM call instead of being silently stringified into prompt text. Verification: PR #1 ancestry, compile, focused hardening pytest (`283 passed`), and `git diff --check`. The active nested OmegaClaw runtime tree was not modified. No live runtime/provider/queue/subprocess activity, secrets/access changes, paid compute, push, merge, force-push, or remote-ref deletion.

- [x] 2026-07-13: Cross-project keyword GGB fixture PeTTa runtime gate. Extended `local/check-ggb-gate-petta-runtime.py` from one ThreadKeeper keyword shape to the independent `20260709-goalchainer-real-petta-memory-replay` shape: `gate-slug` summaries and unkeyed `ggb-check (name ...)` atoms now load/query exactly within the structurally checked five-file fixture. Positional regression returned four checks, ThreadKeeper returned six, GoalChainer+`petta-memory` returned eight, and a missing-`METRICS.metta` negative failed closed. Refreshed `artifacts/ggb-capacity-gates/20260713-ggb-keyword-petta-runtime-smoke/` and the roadmap. This remains representative schema coverage only; no live runtime/provider/Telegram/queue/memory-write activity or authority change.

- [x] 2026-07-13: ThreadKeeper non-empty final-return hardening. Branch `agent/threadkeeper-hardening-next` commit `93d6b8f`. Empty or whitespace-only `(emit ...)` values now fail closed as `EMIT_PROTOCOL_VIOLATION`, preventing a successful structured return with no meaningful summary. Verification: PR #1 ancestry, compile, focused emit tests (`14 passed`), full focused hardening pytest (`278 passed`), and `git diff --check`. The active nested OmegaClaw runtime tree was not modified. No live runtime/provider/queue/subprocess activity, secrets/access changes, paid compute, push, merge, force-push, or remote-ref deletion.

- [x] 2026-07-13: ThreadKeeper final-emit envelope hardening. Branch `agent/threadkeeper-hardening-next` commit `99aebc0`. A successful `(emit ...)` must now be the only non-empty protocol record after thinking-block/fence removal, so ignored narration or malformed extra call lines cannot ride beside a valid emit into the parent digest. Verification: PR #1 ancestry, compile, focused emit tests (`12 passed`), full focused hardening pytest (`276 passed`), and `git diff --check`. No live runtime/provider/queue/subprocess activity, runtime-tree edit, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-13: GGB keyword-shaped fixture real-PeTTa runtime gate. Extended `local/check-ggb-gate-petta-runtime.py` while preserving the canonical positional regression: one current keyword-shaped ThreadKeeper sibling fixture now loads in local PeTTa and returns exact status `pass` plus all six expected checks. Archived `artifacts/ggb-capacity-gates/20260713-ggb-keyword-petta-runtime-smoke/`; compile, positional regression, keyword runtime query, missing-file fail-closed, fixture, and diff checks passed. This remains representative schema coverage only; no live runtime/provider/Telegram/queue/memory-write activity or authority change.

- [x] 2026-07-13: ThreadKeeper final-emit Unicode/control hardening. Branch `agent/threadkeeper-hardening-next` commit `842792b`. Final `(emit ...)` values now reject unsafe Unicode controls, separators, formatting characters, and lone surrogates before a successful parent digest is accepted; parser line splitting no longer treats hidden Unicode separators as protocol record boundaries, and failed-input transcript evidence is escaped visibly. Verification: PR #1 ancestry, compile, focused emit tests (`8 passed`), full focused hardening pytest (`274 passed`), and `git diff --check`. The nested OmegaClaw runtime tree was intentionally not modified because it contains active unrelated runtime work. No live runtime/provider/queue/subprocess activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-13: GGB sibling fixture real-PeTTa runtime gate. Added `local/check-ggb-gate-petta-runtime.py` and archived `artifacts/ggb-capacity-gates/20260713-ggb-petta-runtime-smoke/`. The bounded checker first runs the existing structural fixture check, then loads all five canonical `20260701-petta-chem-run-contract` sibling files in local PeTTa and queries `run-summary` plus passed `ggb-check` labels. It returned `(partial true)` and exactly four expected labels; compile, negative missing-file fail-closed, new-gate fixture, and workspace diff checks passed. No live runtime/provider/Telegram/queue/memory-write activity, secrets/access changes, paid compute, push, merge, or force-push.

- [x] 2026-07-13: ThreadKeeper Unicode run-control path gate refresh. Verified existing branch commit `6e0e49b` extends the shared unsafe-Unicode/lone-surrogate guard from file/query/shell arguments to queued-dispatch, worker-stop, and queued-task cancellation paths before queue claim or worker-lock creation. Refreshed `artifacts/ggb-capacity-gates/20260713-threadkeeper-unicode-control-arg-hardening/` and the GGB roadmap. Checks: PR #1 ancestry, clean ThreadKeeper status, compile, focused hardening pytest (`268 passed`), diff check, and six-check GGB fixture. No live/runtime/provider/queue/subprocess activity, runtime-tree edit, secrets/access changes, paid compute, merge, push, or force-push.

- [x] 2026-07-12: ThreadKeeper unsafe Unicode format/surrogate tool-argument hardening. Branch `agent/threadkeeper-hardening-next` commit `cf0db9a`. File paths, external queries, and optional-shell commands now reject unsafe Unicode `Cf` formatting characters and lone surrogate code points before filesystem/provider/subprocess handling, while preserving U+200C/U+200D linguistic and emoji joiners. Pushed to `fork/agent/threadkeeper-hardening-next` and synced nested runtime source. Verification: PR #1 ancestry, compile, focused hardening pytest (`266 passed`), diff check, runtime source cmp. No live wiring, provider/queue/subprocess activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-12: ThreadKeeper bidirectional-control tool-argument hardening. Branch `agent/threadkeeper-hardening-next` commit `5624013`. File paths, external queries, and optional-shell commands now reject Unicode bidi formatting/isolate controls before filesystem/provider/subprocess handling, preventing visually reordered audit/prompt arguments while preserving benign Unicode joiners. Pushed to `fork/agent/threadkeeper-hardening-next` and synced nested runtime source. Verification: compile, focused hardening pytest (`265 passed`), diff check, runtime source cmp. No live wiring, provider/queue/subprocess activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-12: ThreadKeeper Unicode line-separator tool-argument hardening. Branch `agent/threadkeeper-hardening-next` commit `8de75d5`. File paths, external queries, and optional-shell commands now reject C1 controls plus Unicode line/paragraph separators before filesystem/provider/subprocess handling, preventing hidden prompt/audit line injection beyond ASCII controls. Pushed to `fork/agent/threadkeeper-hardening-next` and synced nested runtime source. Verification: compile, focused hardening pytest (`263 passed`), diff check, runtime source cmp. No live wiring, provider/queue/subprocess activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-12: GoalChainer→ThreadKeeper canary review-boundary gate. Found that the generic default canary could queue/accept a permitted raw-log action and skip adjudication for recommended outputs. Hardened the exploratory non-live canary so forbidden norms are checked first, all queued outputs require adjudication and remain patch-proposal-only, and the offline reviewer accepts only `publish_redacted_summary`. Added 3 focused tests; isolated fake replay queued/accepted one redacted summary, deferred hold, and did not queue forbidden raw logs. Archived `artifacts/ggb-capacity-gates/20260712-goalchainer-canary-review-boundary/`. No live/provider/Telegram/runtime change.

- [x] 2026-07-12: ThreadKeeper unquoted file-content trailing-call hardening. Branch `agent/threadkeeper-hardening-next` commit `08e7f39`. Legacy unquoted `write-file` / `append-file` content now rejects spaced or compact `)(` trailing-call payloads by surfacing a third argument before workspace mutation, while ordinary parenthesized prose remains accepted. Pushed to `fork/agent/threadkeeper-hardening-next` and synced nested runtime source. Verification: compile, focused hardening pytest (`262 passed`), diff check, runtime source cmp. No live wiring, provider/queue/subprocess activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-12: ThreadKeeper compact unquoted trailing-call hardening. Branch `agent/threadkeeper-hardening-next` commit `3a296ad`. One-argument calls now reject compact `)(` trailing-call payloads as well as spaced `) (` payloads before execution/final emit. Pushed to `fork/agent/threadkeeper-hardening-next` and synced nested runtime source. Verification: compile, focused hardening pytest (`260 passed`), diff check, runtime source cmp. No live wiring, provider/queue/subprocess activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.


- [x] 2026-07-12: ThreadKeeper unquoted trailing-call protocol hardening. Branch `agent/threadkeeper-hardening-next` commit `6a62c97`. Unquoted single-argument calls now reject ambiguous same-line `) (` trailing calls before optional shell, provider-backed query, file-read, or final-emit handling, while preserving ordinary parenthesized prose. Pushed to `fork/agent/threadkeeper-hardening-next` and synced nested runtime source. Verification: PR #1 ancestry, compile, focused hardening pytest (`260 passed`), diff check, and runtime source cmp. No live wiring, provider/queue/subprocess activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-12: GoalChainer-ThreadKeeper OpenClaw Gateway canary. Extended canary with `--mode openclaw` (commit `697da8e`): uses real local OpenClaw Gateway `/v1/chat/completions`. Created `canary-worker` persona (ThreadKeeper commit `5f790fe`). Worker LLM produced real reasoning: recommended proceeding with redacted summary, cautioned against raw log. All adjudications passed. No Telegram, paid compute, or live wiring.

- [x] 2026-07-12: GoalChainer-ThreadKeeper supervised canary (fake worker). Committed GoalChainer implementation (commit `ea72984`: heuristic PLN belief grader, memory evidence bridge, multi-scenario tests, fixed local PeTTa/SWI paths; 87 passed, 6 skipped). Drafted `docs/GOAL_TASK_STATE_CONTRACT.md`. Built and ran `canary/goalchainer_threadkeeper_canary.py` (commit `3b4e49c`): 2 accepted, 1 deferred, 0 forbidden.

- [x] 2026-07-12: ThreadKeeper quoted file-content protocol hardening. Branch `agent/threadkeeper-hardening-next` commit `dd3f7e5`. Quoted `write-file` / `append-file` content now rejects unterminated closing quotes and same-line trailing payloads by argument-count validation before workspace mutation. Pushed to `fork/agent/threadkeeper-hardening-next` and synced nested runtime source. Verification: compile, focused hardening pytest (`258 passed`), diff check, and runtime source cmp. No live wiring, provider/queue/subprocess activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-12: ThreadKeeper unterminated quoted tool argument hardening. Branch `agent/threadkeeper-hardening-next` commit `0781f57`. Malformed single-argument worker calls beginning with an unterminated quote now fail closed by argument-count validation before optional shell, provider-backed query, file-read, or final-emit handling. Pushed to `fork/agent/threadkeeper-hardening-next` and synced nested runtime source. Verification: compile, focused hardening pytest (`257 passed`), diff check, and runtime source cmp. No live wiring, provider/queue/subprocess activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-12: ThreadKeeper optional-shell command argument GGB gate. Archived `artifacts/ggb-capacity-gates/20260712-threadkeeper-shell-arg-hardening/` for head `76ec6b6`, mapping the dedicated `OMEGACLAW_SUBAGENT_MAX_SHELL_ARG_CHARS` pre-parse/pre-execution cap to capacities 1.3/3.2/4.5/5.2/5.3/5.4. Verification: PR #1 ancestry, source compile, focused hardening pytest (`256 passed`), diff check, runtime source `cmp`, and GGB fixture checker. No live wiring, subprocess/provider/queue activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-12: ThreadKeeper external query argument cap. Branch `agent/threadkeeper-hardening-next` commit `73b6b7b`. `search`, `tavily-search`, and `technical-analysis` now reject inputs over dedicated `OMEGACLAW_SUBAGENT_MAX_QUERY_ARG_CHARS` (default 4096) before provider execution, retaining the broader tool-argument cap as a second ceiling. Pushed to `fork/agent/threadkeeper-hardening-next` and synced nested runtime source. Verification: PR #1 ancestry, compile, focused hardening pytest (`255 passed`), diff check, runtime source cmp. No live wiring, provider/queue activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-12: ThreadKeeper technical-analysis argument GGB gate. Archived `artifacts/ggb-capacity-gates/20260712-threadkeeper-technical-analysis-arg-hardening/` for current head `35c0c98`, mapping bounded market-symbol validation to capacities 1.3/3.2/4.5/5.2/5.3/5.4. Verification: PR #1 ancestry, source compile, focused hardening pytest (`254 passed`), `git diff --check`, runtime source `cmp`, and GGB fixture checker. No live wiring, provider/queue activity, secrets/access changes, paid compute, merge, or force-push.

- [x] 2026-07-11: ThreadKeeper append-file streaming read cap. Branch `agent/threadkeeper-hardening-next` commit `67032df`. Atomic `append-file` now re-enforces `OMEGACLAW_SUBAGENT_MAX_FILE_SIZE_CHARS` while reading the already-open no-follow fd (cap plus sentinel), not only via pre-read `fstat`, preventing concurrent/post-stat file growth from causing an unbounded read or oversized replacement. Pushed to `fork/agent/threadkeeper-hardening-next` and synced the nested OmegaClaw runtime source. Verification: `py_compile`, focused hardening pytest (`253 passed`), `git diff --check`, and runtime source `cmp`. No paid compute, live wiring, secrets/access/security changes, queue/provider activity, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper worker env streaming read cap. Branch `agent/threadkeeper-hardening-next` commit `6a9452d`. The operator runner now enforces the 64 KiB env-file cap during the opened-fd read (cap plus one-byte sentinel), not only via pre-read `fstat`, and rejects invalid UTF-8 before parsing. This closes post-`fstat` growth/unbounded-read risk before `subagent` import. Pushed to `fork/agent/threadkeeper-hardening-next`. Verification: PR #1 ancestry, `py_compile`, focused runner pytest (`5 passed, 234 deselected`), focused hardening pytest (`252 passed`), and `git diff --check`. No paid compute, live wiring, secrets/access/security changes, queue enqueue/claim outside tests, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper worker env-file loading hardening. Branch `agent/threadkeeper-hardening-next` commit `10dad06`. The operator runner `scripts/run-subagent-worker-loop --env-file` now opens env files with no-follow semantics when available, validates regular-file status and size on the opened fd with `fstat`, and reads/parses from that fd before importing `subagent`, narrowing env-file symlink/swap/size-check races while preserving the existing conservative key/value caps and blocked process-control keys. Updated docs and pushed to `fork/agent/threadkeeper-hardening-next`. Verification: `py_compile`, focused worker-loop script pytest (`5 passed, 233 deselected`), focused hardening pytest (`238 passed`), `git diff --check`; broader mock-suite attempt passed 243 tests but 3 Docker-dependent integration tests failed because `docker` is unavailable. No paid compute, live wiring, secrets/access changes, queue enqueue/claim outside tests, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper run-control path GGB gate. Archived `artifacts/ggb-capacity-gates/20260711-threadkeeper-run-control-path-hardening/` for current ThreadKeeper head `be5ea1f`, mapping queued-dispatch path bounding plus worker-loop `stop_file` / queued-task `cancel_file` control-character rejection to GGB capacities 1.1/1.3/3.2/4.5/5.2/5.3/5.4. Refreshed `GGB_CAPACITIES_ROADMAP.md` to 250-test/head `be5ea1f` evidence. Verification: PR #1 ancestry check, source/runtime `py_compile`, focused mock pytest (`250 passed`), ThreadKeeper `git diff --check`, runtime source `cmp`, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim outside local tests, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper run-control path argument hardening. Branch `agent/threadkeeper-hardening-next` commit `be5ea1f`. Worker-loop `stop_file` and queued-task `cancel_file` control-token paths now reject NUL/control characters before run-dir resolution, worker-lock acquisition, queue claim validation, cancellation checks, or worker LLM setup, preventing forged multiline status/audit text in operator/task control-plane inputs. Updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: PR #1 safety-floor ancestry check, `py_compile`, focused run-control pytest (`9 passed, 228 deselected`), focused mock pytest (`250 passed` for subagent + budget hardening), `git diff --check`, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim outside local tests, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper queued-dispatch path argument hardening. Branch `agent/threadkeeper-hardening-next` commit `c2f299e`. `subagent.run_queued_dispatch(queue_path)` now rejects oversized path strings and NUL/control characters before queue-dir resolution, claim, rename, checksum verification, or worker LLM setup, preventing operator-supplied queue paths from creating multiline audit/status ambiguity or oversized argument handling. Updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: PR #1 safety-floor ancestry check, `py_compile`, focused queued-dispatch pytest (`3 passed, 232 deselected`), focused mock pytest (`248 passed` for subagent + budget hardening), `git diff --check`, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim outside local tests, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper workspace/command-argument GGB gate. Archived `artifacts/ggb-capacity-gates/20260711-threadkeeper-workspace-command-arg-hardening/` for current ThreadKeeper head `9b00e38`, mapping symlink workspace-root rejection plus shell/query argument control-character rejection to GGB capacities 1.1/1.3/3.2/4.5/5.2/5.3/5.4. Refreshed `GGB_CAPACITIES_ROADMAP.md` to 246-test/head `9b00e38` evidence. Verification: PR #1 ancestry check, source/runtime `py_compile`, focused mock pytest (`246 passed`), ThreadKeeper `git diff --check`, runtime source `cmp`, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper command/query argument control-character hardening. Branch `agent/threadkeeper-hardening-next` commit `9b00e38`. Subagent `shell` command strings and external query tool arguments (`search`, `tavily-search`, `technical-analysis`) now fail closed on control characters before subprocess/provider execution, keeping tool calls single-line and avoiding transcript/audit line-forging ambiguity. Updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: PR #1 ancestry check, `py_compile`, focused tool-argument pytest (`10 passed, 223 deselected`), focused mock pytest (`246 passed` for subagent + budget hardening), `git diff --check`, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper symlink workspace-root hardening. Branch `agent/threadkeeper-hardening-next` commit `b25d763`. Existing `OMEGACLAW_SUBAGENT_WORKSPACE` roots now fail closed unless they are real non-symlink directories before file-tool resolution or optional allowlisted shell execution, preventing a symlinked workspace root from redirecting tool effects outside the intended root. Updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: PR #1 ancestry check, `py_compile`, focused symlink-workspace pytest (`4 passed, 227 deselected`), focused mock pytest (`244 passed` for subagent + budget hardening), `git diff --check`, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper persona/emit protocol GGB gate. Archived `artifacts/ggb-capacity-gates/20260711-threadkeeper-persona-emit-protocol-hardening/` for current ThreadKeeper head `bf65398`, mapping fail-closed persona config scalar validation plus unquoted final-emit trailing-payload rejection to GGB capacities 1.1/1.3/3.2/4.5/5.2/5.3/5.4. Refreshed `GGB_CAPACITIES_ROADMAP.md` to 242-test/head `bf65398` evidence. Verification: local PR ancestry check, source/runtime `py_compile`, focused mock pytest (`242 passed`), ThreadKeeper `git diff --check`, runtime source `cmp`, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim outside local tests, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper unquoted emit trailing-payload validation. Branch `agent/threadkeeper-hardening-next` commit `bf65398`. Legacy unquoted final emits now reject same-line trailing payloads such as `(emit done) (write-file ...)` as structured `EMIT_PROTOCOL_VIOLATION` before any successful digest/adjudication candidate is accepted. Updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused emit/protocol pytest (`6 passed, 223 deselected`), focused mock pytest (`242 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper persona config scalar validation. Branch `agent/threadkeeper-hardening-next` commit `78c43f2`. Persona config control fields now fail closed before worker prompt/provider setup unless they are bounded non-empty strings (`persona_file`, `provider`, `model`, `api_key_env`, `node_role`, `endpoint_kind`, optional `base_url`); `api_key_env` must be a safe environment-variable identifier and optional `persona_sha256` must be a 64-character hex SHA-256. Updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`241 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper audit/accounting read-cap GGB gate. Archived `artifacts/ggb-capacity-gates/20260711-threadkeeper-audit-readcap-hardening/` for current ThreadKeeper head `bedfadb`, mapping run-index/transcript audit read bounding plus budget accounting/config fd read-cap hardening to GGB capacities 1.3/3.2/3.5/4.5/5.2/5.3/5.4. Refreshed `GGB_CAPACITIES_ROADMAP.md` to 237-test/head `bedfadb` evidence. Verification: PR #1 ancestry check, source/runtime `py_compile`, focused mock pytest (`237 passed`), ThreadKeeper `git diff --check`, runtime source `cmp`, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper budget accounting/config read-cap hardening. Branch `agent/threadkeeper-hardening-next` commit `bedfadb`. `src/threadkeeper_budget.py` now rechecks budget config and usage-log sizes on the opened fd with `fstat`, then reads with the existing bounded caps (`THREADKEEPER_MAX_BUDGET_CONFIG_BYTES`, `THREADKEEPER_MAX_BUDGET_LOG_BYTES`), preventing local post-stat growth/swap races from turning budget accounting/config checks into unbounded reads. Added focused regressions, updated README, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `threadkeeper_budget.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`237 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper transcript audit size-check nofollow hardening. Branch `agent/threadkeeper-hardening-next` commit `6a6916f`. `verify_subagent_run_index()` no longer uses path-based `os.path.getsize()` for referenced transcript size prechecks; it now uses `lstat` to reject symlink/non-regular transcript records before hashing, while the existing no-follow streamed hash reader still enforces `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_AUDIT_BYTES` during reads. Added a focused regression, updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`235 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-11: ThreadKeeper budget audit-log parent hardening. Branch `agent/threadkeeper-hardening-next` commit `4034064`. `src/threadkeeper_budget.py` usage/escalation audit appends now create parent directories component-by-component with `lstat` checks instead of `os.makedirs(..., exist_ok=True)`, rejecting symlink/non-directory log ancestors before any budget audit write and best-effort fsyncing parent directories after file fsync. Added focused regression tests, updated README, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `threadkeeper_budget.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`234 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper run-index audit read bounding. Branch `agent/threadkeeper-hardening-next` commit `e7ae245`. `verify_subagent_run_index()` now enforces `OMEGACLAW_SUBAGENT_MAX_INDEX_AUDIT_BYTES` while streaming `index.jsonl` through the no-follow opener, not just before open, preventing post-stat index growth from creating an unbounded audit read. Added focused regressions, updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`231 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper task-contract path hardening GGB gate. Archived `artifacts/ggb-capacity-gates/20260710-threadkeeper-task-contract-path-hardening/` for current ThreadKeeper head `558c3dc`, mapping strict task-contract `allowed_paths` validation and file-tool control-character rejection to capacities 1.1/1.3/3.2/4.5/5.2/5.3/5.4. Refreshed `GGB_CAPACITIES_ROADMAP.md` to 230-test/head `558c3dc` evidence. Verification: PR #1 ancestry check, source/runtime `py_compile`, focused mock pytest (`230 passed`), ThreadKeeper `git diff --check`, runtime source `cmp`, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper task-contract path validation hardening. Branch `agent/threadkeeper-hardening-next` commit `558c3dc`. Task-contract `allowed_paths` now shares the strict workspace-relative path validator used by file tools, rejecting absolute paths, parent traversal, oversized paths, empty strings, and control characters before worker LLM calls or audit/file-tool handling. File-tool path arguments now also reject control characters. Updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`230 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.


- [x] 2026-07-10: ThreadKeeper setup-file size-check nofollow hardening. Branch `agent/threadkeeper-hardening-next` commit `b424f9e`. Pinned `escalation.metta` integrity checks and persona prompt reads now perform size checks from the already-open regular non-symlink fd instead of a separate path-based `getsize()`, narrowing setup-file TOCTOU/symlink-swap races before worker LLM calls. Added focused regression tests proving the path-based size checker is not used, updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`227 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, and runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper file-tool relative-path validation. Branch `agent/threadkeeper-hardening-next` commit `23ebb66`. Subagent `read-file` / `write-file` / `append-file` tool-call validation now rejects absolute paths and any parent-directory traversal component (`..`) before workspace resolution, contract checks, audit paths, or file-tool execution. Updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, synced `subagent.py` to the nested OmegaClaw-Core runtime tree, and archived GGB gate `artifacts/ggb-capacity-gates/20260710-threadkeeper-file-tool-guardstate-hardening/` covering this plus guard-state parent hardening. Verification: `py_compile`, focused mock pytest (`225 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper LLM guard-state parent symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `2350afa`. Per-endpoint worker LLM rate-limit/concurrency guard-state setup now validates `OMEGACLAW_SUBAGENT_RUN_DIR` as a real non-symlink directory before creating `.llm-rate-*` / `.llm-inflight-*` state files, preventing a symlinked run dir from redirecting guard-state writes outside the run directory. Updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`223 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper queue-directory symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `ff24af5`. Queued-worker listing/count/claim now validates `OMEGACLAW_SUBAGENT_RUN_DIR/queue` as a real non-symlink directory before treating files as pending queue tasks, preventing a local symlinked queue directory from redirecting worker claims outside the run dir. Archived GGB gate `artifacts/ggb-capacity-gates/20260710-threadkeeper-queue-dir-symlink-hardening/`, refreshed `GGB_CAPACITIES_ROADMAP.md` to 222-test/head `ff24af5` evidence, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: source/runtime `py_compile`, focused mock pytest (`222 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim outside local tests, provider call, supervisor/daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper audit ancestor-directory symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `1cbc15b`. Shared audit/run directory creation now validates each parent component with `lstat` before creating or using it, avoiding `os.makedirs(..., exist_ok=True)` following a symlink ancestor such as `run-dir/link/nested`; worker `usage.jsonl` setup uses the same path. Updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`221 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper append-file size-check nofollow hardening. Branch `agent/threadkeeper-hardening-next` commit `aec4c9b`. `append-file` now checks existing-file size from the already-open regular non-symlink fd used for content reads, avoiding a separate path-based `getsize()` TOCTOU/symlink-swap gap; new-file append size checks include the trailing newline. Updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`211 passed` subagent hardening; `219 passed` with budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper accounting/protocol hardening GGB gate. Archived `artifacts/ggb-capacity-gates/20260710-threadkeeper-accounting-protocol-hardening/` for current ThreadKeeper head `25d96c8`, covering quoted-final-emit trailing-payload rejection plus worker usage-log parent hardening across GGB capacities 1.3/3.2/3.5/5.2/5.3/5.4. Refreshed `GGB_CAPACITIES_ROADMAP.md` to 218-test/head `25d96c8` evidence. Verification: PR #1 ancestry check, source/runtime `py_compile`, focused mock pytest (`218 passed`), ThreadKeeper `git diff --check`, runtime source `cmp`, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, supervisor/daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper worker usage-log parent hardening. Branch `agent/threadkeeper-hardening-next` commit `25d96c8`. Worker LLM accounting appends to shared `usage.jsonl` now validate the parent directory as a real non-symlink directory before opening the log, and best-effort fsync the parent directory after append, closing a local symlink-parent redirection gap in cost/accounting audit writes. Added focused regression coverage, updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`218 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper quoted-emit trailing-payload validation. Branch `agent/threadkeeper-hardening-next` commit `33d79a5`. Single-argument quoted calls now require the closing quote to end the argument modulo whitespace, so same-line trailing payloads after a final `emit` become structured `EMIT_PROTOCOL_VIOLATION` instead of accepted successful digests. Added focused regression coverage, updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`217 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper parent-directory symlink hardening GGB gate. Archived `artifacts/ggb-capacity-gates/20260710-threadkeeper-parent-symlink-hardening/` for current ThreadKeeper head `28adabf`, covering audit/run/queue parent-directory validation (`b567ad9`) plus workspace `write-file`/`append-file` parent revalidation (`28adabf`) across GGB capacities 1.3/3.2/4.5/5.2/5.3/5.4. Refreshed `GGB_CAPACITIES_ROADMAP.md` to 216-test/head `28adabf` evidence. Verification: PR #1 ancestry check, source/runtime `py_compile`, focused mock pytest (`216 passed`), ThreadKeeper `git diff --check`, runtime source `cmp`, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, supervisor/daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper workspace write-parent symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `28adabf`. Workspace `write-file` / `append-file` atomic replacements now revalidate parent directories as real non-symlink trees under `OMEGACLAW_SUBAGENT_WORKSPACE` immediately before lock/temp-file creation, closing a local parent-directory swap gap after path containment resolution. Added focused parent-swap regression tests, updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`216 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper audit parent-directory symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `b567ad9`. Atomic JSON audit writes, transcript checksum sidecars, queued-run/index setup, and async-worker run-dir setup now validate required parent directories as real non-symlink directories before temp-file creation, lock/index writes, or queue claims; unsafe worker run dirs fail closed as structured `worker_config_invalid`. Added focused symlink-parent tests, updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the nested OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`214 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-10: ThreadKeeper workspace file tool no-follow hardening. Branch `agent/threadkeeper-hardening-next` commit `14d7f90`. `_tool_read_file` and `_tool_append_file` now open workspace files through `_open_workspace_file_read(path)` which uses `O_NOFOLLOW` and `fstat` regular-file validation, closing a TOCTOU symlink-swap gap between `_resolve_workspace_path`'s `realpath` containment check and the actual file read. Added 4 focused tests (direct symlink rejection, regular-file acceptance, symlink-escape rejection in read-file and append-file via existing `realpath` containment). Updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, synced `subagent.py` to the nested OmegaClaw-Core runtime tree, and archived GGB gate `artifacts/ggb-capacity-gates/20260710-threadkeeper-workspace-file-nofollow-hardening/`. Verification: `py_compile`, focused mock pytest (`212 passed` for subagent + budget hardening), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper durable audit-write fsync hardening. Branch `agent/threadkeeper-hardening-next` commit `78a15bc`. Atomic JSON audit writes, transcript checksum-sidecar writes, run-index rotation rewrites, and workspace `write-file`/`append-file` atomic replacements now fsync the replacement file and best-effort fsync the parent directory after `os.replace`; budget usage/escalation JSONL appends now flush/fsync before returning. Added focused regression tests, updated README/subagent docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py`/`threadkeeper_budget.py` to the nested OmegaClaw-Core runtime copy. Verification: `py_compile`, focused mock pytest (`208 passed`), `git diff --check`, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper Telegram-private default-boundary hardening. Patched `local/omegaclaw-telegram-private-supervisor.sh` so the private supervisor now defaults to `TG_PRIVATE_ONLY=true`, `TG_CHAT_ID=402314199`, and `TG_CHAT_IDS=402314199`, and updated usage text to keep group/channel targets as a separate explicit gate. Archived `artifacts/ggb-capacity-gates/20260710-threadkeeper-telegram-private-defaults-hardening/`; `bash -n`, the existing preflight checker, supervisor status inspection, targeted `git diff --check`, and GGB fixture checker ran. Result is partial: default-boundary checks now pass (preflight 11/12), but an already-active supervisor (`active pid 822634` during the gate) remains a live-smoke blocker. No Telegram/provider call, secret read, queue enqueue/claim, supervisor start/stop, daemon/scheduler install, paid compute, push, merge, or force-push.

- [x] 2026-07-09: ThreadKeeper budget config read hardening. Branch `agent/threadkeeper-hardening-next` commit `b9298dd`. `src/threadkeeper_budget.py` now treats budget config/policy inputs as local control files: `threadkeeper.config.yaml` reads reject symlink/non-regular paths, use no-follow regular-file opens, and are capped by `THREADKEEPER_MAX_BUDGET_CONFIG_BYTES` (default 64 KiB); the lazy MeTTa escalation-policy loader rejects symlink/non-regular policy paths before loading. Added focused tests, updated README, pushed to `fork/agent/threadkeeper-hardening-next`, and synced the nested OmegaClaw-Core runtime copy. Verification: `py_compile`, focused budget pytest (`7 passed`), focused subagent + budget hardening pytest (`207 passed`), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper budget audit log hardening. Branch `agent/threadkeeper-hardening-next` commit `5b5c6d9`. `src/threadkeeper_budget.py` now treats usage/escalation logs as local audit files: appends reject pre-existing symlink/non-regular targets and use no-follow regular-file opens; usage-log reads reject symlink/non-regular sources and skip oversized logs via `THREADKEEPER_MAX_BUDGET_LOG_BYTES` (default 1 MiB). Added focused tests, updated README, pushed to `fork/agent/threadkeeper-hardening-next`, and synced the nested OmegaClaw-Core runtime copy. Verification: `py_compile`, focused mock pytest (`204 passed` for budget hardening + subagent hardening tests), `git diff --check`, runtime source cmp. Full `Autotests/mock` attempt timed out at 300s after showing failures, so it was not a pass gate. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: GoalChainer reviewer policy real-memory replay. Archived `artifacts/ggb-capacity-gates/20260709-goalchainer-reviewer-policy-real-memory-replay/` as a second replay of the offline reviewer policy, this time over the real `petta-memory` handoff replay candidate. Validator passed 15/15 checks, accepted the redacted-summary candidate for offline evidence only, preserved raw-log blocking, verified bounded/unchanged real memory evidence, and kept Telegram/provider/queue/supervisor/runtime/memory-write/paid-compute scope false. Verification: validator, JSON parse, Python compile, GGB fixture checker, targeted diff check. No live wiring, secrets/access changes, queue claim, provider call, Telegram message, memory write/promotion, daemon/scheduler install, push, merge, or force-push.

- [x] 2026-07-09: ThreadKeeper persona setup symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `0f0b2cc`. Persona config JSON and persona prompt setup files now require regular non-symlink paths and are opened through the shared no-follow helper before JSON parsing, prompt SHA-256 pinning, or prompt construction. Added focused symlink regression tests, updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`200 passed`), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper no-follow audit read hardening. Branch `agent/threadkeeper-hardening-next` commit `1220907`. Read-only run-index audits now open `index.jsonl` through the shared regular non-symlink no-follow helper for the actual scan, and async-worker stale-lock metadata reads use the same helper after lstat/size validation. Added focused opener-regression tests, updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`198 passed`), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper audit-write target hardening. Branch `agent/threadkeeper-hardening-next` commit `c54d6ca`. Atomic JSON audit writes and transcript checksum-sidecar writes now fail closed when the pre-existing destination is a symlink or non-regular file, extending the no-follow audit discipline from read paths to write targets. Added focused symlink tests, updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, synced `subagent.py` to the OmegaClaw-Core runtime tree, and archived GGB gate `artifacts/ggb-capacity-gates/20260709-threadkeeper-audit-write-hardening/`. Verification: PR #1 ancestry check, `py_compile`, focused mock pytest (`196 passed`), `git diff --check`, runtime source cmp/compile, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper escalation policy symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `55160f7`. Pinned cloud-delegation `escalation.metta` integrity checks now require the explicit/auto-detected policy path to be a regular non-symlink file, fail closed for unsafe explicit `OMEGACLAW_ESCALATION_METTA_PATH` values instead of silently falling back, and read policy bytes through the shared no-follow regular-file opener before hashing. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`194 passed`), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper worker usage accounting symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `7f3a70e`. Worker LLM usage accounting writes to shared `usage.jsonl` now append through the regular non-symlink no-follow opener, so a local pre-existing symlink cannot redirect worker accounting/audit writes outside the configured memory directory. Added focused regular-file and symlink-target tests, updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`193 passed`), `git diff --check`, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper transcript/guard-state hardening GGB gate. Archived `artifacts/ggb-capacity-gates/20260709-threadkeeper-transcript-guard-hardening/` for current ThreadKeeper head `4c73526`, covering per-endpoint worker LLM guard-state symlink/non-regular rejection (`3a31e25`) plus transcript audit symlink/non-regular rejection for candidate review/run-index verification (`4c73526`) across GGB capacities 1.3/3.2/4.5/5.2/5.3/5.4. Verification: PR #1 ancestry check, source/runtime `py_compile`, focused mock pytest (`191 passed`), ThreadKeeper `git diff --check`, runtime source cmp/compile, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper transcript audit symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `4c73526`. Transcript JSON reads for candidate review and transcript hashing for run-index verification now use the shared regular non-symlink no-follow opener; transcript path resolution still enforces run-dir realpath containment but returns the original absolute path so symlink transcript records fail closed instead of being followed. Updated docs/tests, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`191 passed`), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper LLM guard-state symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `3a31e25`. Per-endpoint worker LLM rate-limit and concurrency state files are now opened through the shared regular non-symlink no-follow helper, so local `.llm-rate-*.json` / `.llm-inflight-*.json` guard files cannot redirect reads/writes outside `OMEGACLAW_SUBAGENT_RUN_DIR`. Added focused symlink coverage, updated docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`189 passed`), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper audit-path hardening GGB gate. Archived `artifacts/ggb-capacity-gates/20260709-threadkeeper-audit-path-hardening/` for current ThreadKeeper head `59140ac`, covering workspace lock symlink/non-regular rejection (`6c281bc`) plus run-index tail/rotation write hardening (`59140ac`) across GGB capacities 1.3/3.2/4.5/5.2/5.3/5.4. Verification: PR #1 ancestry check, source/runtime `py_compile`, focused mock pytest (`188 passed`), ThreadKeeper `git diff --check`, runtime source cmp, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, queue enqueue/claim, provider call, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper run-index tail/rotation write hardening. Branch `agent/threadkeeper-hardening-next` commit `59140ac`. Run-index tail reads now reject symlink/non-regular `index.jsonl` and open through the shared no-follow regular-file helper; index rotation now rewrites via random local `mkstemp` files instead of predictable `index.jsonl.tmp.<pid>` names, avoiding temp-symlink redirection during bounded audit-log rotation. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`188 passed`), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper workspace file-lock symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `6c281bc`. Per-target workspace lock files used by atomic `write-file`/`append-file` updates now open through the shared regular non-symlink no-follow path, rejecting existing symlink/non-regular `.target.lock` paths before file-tool synchronization can be redirected outside the workspace. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`186 passed`), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper integrity-sidecar hardening GGB gate. Archived `artifacts/ggb-capacity-gates/20260709-threadkeeper-integrity-sidecar-hardening/` to map current branch head `7387f40` onto GGB capacities 1.3/3.2/4.5/5.2/5.3/5.4. Evidence: PR #1 ancestry check, source/runtime `py_compile`, focused mock pytest (`185 passed`), ThreadKeeper `git diff --check`, runtime source cmp, and GGB sibling fixture files. Required `.sha256` audit sidecars now reject symlink/non-regular paths before digest reads; roadmap evidence updated to 185 tests/head `7387f40`. No live runtime change, Telegram/provider call, queue enqueue/claim, secret read, access/security change, daemon/scheduler install, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-09: ThreadKeeper checksum sidecar symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `7387f40`. Required local `.sha256` integrity sidecars now fail closed if they are symlinks or non-regular files before digest reads, using the existing no-follow regular-file open path plus the configured sidecar byte cap. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`185 passed`), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper run-index symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `372e336`. Finished-run `index.jsonl` appends and read-only `verify_subagent_run_index()` audits now reject symlink/non-regular `index.jsonl` and `index.jsonl.lock` paths, using no-follow opens where available for newly created audit files. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`184 passed`), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper task-contract validation refresh GGB gate. Archived `artifacts/ggb-capacity-gates/20260709-threadkeeper-contract-validation-refresh/` to map current branch head `cbe37d3` onto GGB capacities 1.1/1.3/3.2/4.5/5.2/5.3/5.4. Evidence: PR #1 ancestry check, source/runtime `py_compile`, focused mock pytest (`181 passed`), ThreadKeeper `git diff --check`, runtime source cmp, and GGB fixture files. The gate records fail-closed preservation/validation of malformed inline/persona task-contract list fields before worker LLM calls and keeps Telegram-private smoke blocked on the existing private-only/default-chat boundary. No live runtime change, Telegram/provider call, queue enqueue/claim, secret read, access/security change, daemon/scheduler install, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper inline task-contract list validation. Branch `agent/threadkeeper-hardening-next` commit `cbe37d3`. Inline/persona task-contract string-list fields (`allowed_paths`, `forbidden_actions`, `done_criteria`) now preserve malformed scalar/non-string shapes so validation fails closed before any worker LLM call instead of stringifying them into accepted constraints. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`181 passed`), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper async worker signal-state cleanup. Branch `agent/threadkeeper-hardening-next` commit `2258f6a`. The bounded async worker loop now clears its module-local SIGTERM/SIGINT stop flag after each run, so a graceful stop handled by one same-process supervised worker-loop invocation cannot poison a later invocation into exiting before queue checks. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`179 passed`), `git diff --check`, `origin/pr-1` ancestor check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper Telegram-private preflight blocker. Archived non-live gate `artifacts/ggb-capacity-gates/20260708-threadkeeper-telegram-private-preflight/`: checker inspected supervisor/runner defaults, staged private-smoke RUN, current supervisor status, and ThreadKeeper source/runtime `subagent.py` sync without starting/stopping supervisors, calling Telegram/providers, enqueuing tasks, reading secrets, or changing runtime behavior. Result: blocked, 9/12 checks passed; blockers are `DEFAULT_TG_PRIVATE_ONLY=false`, default group/channel-style `DEFAULT_TG_CHAT_IDS=-5437945421,-1003983157420,-5459676079`, and an already active supervisor status (`active pid 679631`). Positive: source/runtime `subagent.py` are byte-identical. Verification: preflight checker, fixture checker, targeted `git diff --check`. Next: resolve private-only/default-chat boundary or require explicit safe env overrides before any live private Telegram smoke; keep group/channel targets separate.

- [x] 2026-07-08: ThreadKeeper async worker consecutive-error cap fix. Branch `agent/threadkeeper-hardening-next` commit `9b6fb3c`. The bounded queued worker loop now stops when `consecutive_errors >= max_consecutive_errors` instead of only after exceeding the configured cap, preventing one extra failed queue claim/worker attempt on poisoned queues. Updated focused regression expectations/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`178 passed`), `git diff --check`, PR #1 ancestry check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper queued task symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `df483df`. Queue listing/backpressure now count only regular non-symlink `queue/*.json` records, oldest-first sorting uses `lstat`, and `run_queued_dispatch()` rejects symlink/non-regular queued-task paths before atomic claim or JSON/sidecar reads. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`178 passed`), `git diff --check`, `origin/pr-1` ancestor check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper worker-lock hardening GGB gate. Archived `artifacts/ggb-capacity-gates/20260708-threadkeeper-worker-lock-hardening/` to map async-worker lock metadata read caps (`76587eb`) plus symlink/non-regular lock rejection (`db834ce`) onto GGB capacities 1.3/3.2/4.5/5.2/5.3/5.4. Verification: PR #1 ancestry check, source/runtime `py_compile`, focused mock pytest (`177 passed`), runtime source cmp, and GGB fixture checker. Updated `GGB_CAPACITIES_ROADMAP.md` to current head `db834ce`. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper async worker lock symlink hardening. Branch `agent/threadkeeper-hardening-next` commit `db834ce`. The bounded async-worker loop now ignores symlink/non-regular `.async-worker.lock` files while reading stale-lock metadata and rejects symlink/non-regular lock paths before worker acquisition, using `O_NOFOLLOW` where available plus `fstat` regular-file validation. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`177 passed`), `git diff --check`, `origin/pr-1` ancestor check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper worker lock metadata read cap. Branch `agent/threadkeeper-hardening-next` commit `76587eb`. Async worker stale-lock metadata reads from `.async-worker.lock` are now bounded by `OMEGACLAW_SUBAGENT_ASYNC_WORKER_LOCK_METADATA_BYTES` before UTF-8/JSON parsing; oversized/corrupt local lock metadata is ignored rather than parsed as stale-lock evidence. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`175 passed`), `git diff --check`, `origin/pr-1` ancestor check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper bounded-read refresh gate. Archived `artifacts/ggb-capacity-gates/20260708-threadkeeper-bounded-read-refresh/` to map the latest setup/audit read caps and streamed transcript audit hashing (`062ee72`) onto GGB capacities 1.3/3.2/4.5/5.2/5.3/5.4. Verification: PR #1 ancestry check, `py_compile`, focused mock pytest (`174 passed`), runtime source cmp, ThreadKeeper `git diff --check`, and GGB fixture checker. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper streamed transcript audit hashing. Branch `agent/threadkeeper-hardening-next` commit `062ee72`. `verify_subagent_run_index()` now hashes transcript audit targets through a bounded streaming helper instead of one whole-file `read()`, while still enforcing `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_AUDIT_BYTES` during the read. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`174 passed`), `git diff --check`, `origin/pr-1` ancestor check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper worker LLM state read cap. Branch `agent/threadkeeper-hardening-next` commit `63bc0bc`. Per-endpoint worker LLM rate-limit/concurrency guard state files are now bounded by `OMEGACLAW_SUBAGENT_MAX_LLM_STATE_BYTES` before JSON parsing; oversized/corrupt local state resets under the existing lock instead of using unbounded `json.load()`. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`173 passed`), `git diff --check`, `origin/pr-1` ancestor check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-08: GoalChainer reviewer policy/threshold fixture. Archived `artifacts/ggb-capacity-gates/20260708-goalchainer-reviewer-policy-thresholds/` with `reviewer_policy.json`, `validate_reviewer_policy.py`, `policy_report.json`, and `.metta` sibling fixtures. The validator replayed the accepted queue-sidecar candidate against explicit offline reviewer criteria and passed 14/14 checks: adjudication-gated status, redacted-summary recommendation, raw-log block, leak safety, bounded candidate text, evidence IDs, non-actions, live-scope false flags, and belief thresholds. Verification: validator, JSON parse, py_compile, fixture checker, targeted `git diff --check`. No Telegram/live runtime/provider/memory/queue/supervisor changes, paid compute, secrets/access/security changes, push/merge/force-push.

- [x] 2026-07-08: ThreadKeeper persona setup read caps. Branch `agent/threadkeeper-hardening-next` commit `6e790ba`. Persona config and prompt setup now bounds local reads with `OMEGACLAW_SUBAGENT_MAX_PERSONA_CONFIG_BYTES` and `OMEGACLAW_SUBAGENT_MAX_PERSONA_PROMPT_BYTES` before JSON parsing, prompt hashing, or prompt construction; oversized persona artifacts fail closed before worker LLM calls and avoid absolute path echoes. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`171 passed`), `git diff --check`, `origin/pr-1` ancestor check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper escalation policy integrity read cap. Branch `agent/threadkeeper-hardening-next` commit `313664a`. Cloud-delegation `escalation.metta` SHA-256 pinning now bounds policy reads with `OMEGACLAW_SUBAGENT_MAX_ESCALATION_POLICY_BYTES` before hashing, denies oversized pinned policies before worker LLM calls, and avoids absolute path echoes in integrity mismatch/read errors. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `py_compile`, focused mock pytest (`169 passed`), `git diff --check`, `origin/pr-1` ancestor check, runtime source cmp/compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-08: ThreadKeeper candidate review checksum sidecar cap. Branch `agent/threadkeeper-hardening-next` commit `ef89b40`. The non-mutating `review_subagent_candidate()` helper now verifies optional transcript `.sha256` files with the shared bounded sidecar reader (`OMEGACLAW_SUBAGENT_MAX_SHA256_SIDECAR_BYTES`) instead of an unbounded text read, and candidate-review setup errors no longer echo absolute local paths. Updated focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, kept `subagent.py` synced to the OmegaClaw-Core runtime tree, and archived GGB gate `artifacts/ggb-capacity-gates/20260708-threadkeeper-sidecar-read-cap-refresh/`. Verification: `git diff --check`, `py_compile`, focused mock pytest (`168 passed`), `pr-1` ancestor check, runtime source cmp, fixture checker. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-07: ThreadKeeper checksum sidecar read cap. Branch `agent/threadkeeper-hardening-next` commit `77197df`. Required local `.sha256` integrity sidecars are now read with `OMEGACLAW_SUBAGENT_MAX_SHA256_SIDECAR_BYTES` (default 4096, minimum 128) before digest parsing, so tampered queue/task sidecars cannot force unbounded local reads; missing/oversized/malformed sidecar failures no longer echo absolute local paths. Added focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`167 passed`), runtime-tree compile/source cmp. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-07: GoalChainer sidecar offline adjudicator. Archived `artifacts/ggb-capacity-gates/20260708-goalchainer-sidecar-offline-adjudicator/`. The artifact-only reviewer inspected the prior queue-sidecar candidate/result/contract and prior accepted private-smoke adjudication, passed 12/12 checks, and accepted `Checkout payment retries are timing out.` as a redacted-summary candidate for offline evidence only. Boundaries remain explicit: no Telegram post, provider call, memory write, runtime bridge enablement, queue claim, supervisor launch, paid compute, secrets/access change, push/merge/force-push. Verification: `python3 -m json.tool review_report.json`, GGB fixture checker, targeted `git diff --check`.

- [x] 2026-07-07: ThreadKeeper shell output memory capture cap. Branch `agent/threadkeeper-hardening-next` commit `d29f462`. The optional allowlisted `shell` tool now redirects combined stdout/stderr to a temporary file and reads only `OMEGACLAW_SUBAGENT_SHELL_OUTPUT_CAP + 1` bytes back into memory before returning the existing truncation marker, replacing `capture_output=True` while preserving argv-only/no-shell execution, sanitized env, workspace cwd, timeout, and output-cap behavior. Added focused coverage/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`165 passed`), `pr-1` ancestor check, runtime-tree compile/source cmp. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-07: ThreadKeeper patch-proposal transcript content cap. Branch `agent/threadkeeper-hardening-next` commit `c784765`. Patch-proposal-only `write-file`/`append-file` records now persist bounded proposal content via `OMEGACLAW_SUBAGENT_MAX_PATCH_PROPOSAL_CHARS` (default 20000) with an explicit truncation marker, while parent digests continue to expose only `{action,path}` metadata. Added focused regression/docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`164 passed`), `origin/pr-1` ancestor check, runtime-tree compile/source cmp. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-07: GoalChainer queue-sidecar artifact harness. Archived `artifacts/ggb-capacity-gates/20260707-goalchainer-queue-sidecar-artifact/`. The harness materializes the prior queue-sidecar contract as a ThreadKeeper queued task with checksum sidecar, runs GoalChainer `solve_incident(memory_items=...)` over the archived private OpenClaw smoke and selected read-only `petta-memory` evidence, then patches `subagent.dispatch` in-process to return that candidate through `run_queued_dispatch` without provider calls or runtime behavior changes. Result: `needs_adjudication`, `publish_redacted_summary` recommended, `publish_raw_log` forbidden/blocked, `.done`/result/checksum artifacts retained. Verification: harness 9/9, `py_compile`, fixture checker, targeted diff-check. No Telegram message, provider call, live runtime bridge, memory write, secrets/access change, paid compute, supervisor/daemon/scheduler install, push/merge/force-push.

- [x] 2026-07-07: ThreadKeeper worker control-token path confinement. Branch `agent/threadkeeper-hardening-next` commit `3f94350`. Worker stop-file and queued dispatch cancel-file paths are now resolved under `OMEGACLAW_SUBAGENT_RUN_DIR` (relative paths interpreted there, absolute paths required to stay there), and token checks only honor regular non-symlink files so operator/task control arguments cannot probe arbitrary host paths. Added focused queue/worker-loop regressions plus docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`163 passed`), `origin/pr-1` ancestor check, runtime-tree compile/source cmp. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-07: ThreadKeeper final emit type validation. Branch `agent/threadkeeper-hardening-next` commit `52a9bc9`. `_extract_final_emit()` now rejects non-string final `emit` arguments before they can become successful summaries/adjudication candidates, matching the stricter tool-argument policy rather than coercing JSON objects/lists/numbers with `str()`. Added direct and dispatch-level regression tests plus docs, pushed to `fork/agent/threadkeeper-hardening-next`, and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`160 passed`), `origin/pr-1` ancestor check, runtime-tree compile/source cmp. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-07: GoalChainer queue-mediated sidecar contract gate. Created `artifacts/ggb-capacity-gates/20260707-goalchainer-queue-sidecar-contract/` with `sidecar_contract.json`, `validate_sidecar_contract.py`, `report.json`, and `.metta` sibling fixtures. The draft contract fits ThreadKeeper's existing queued-task validator, accepts only bounded candidate text plus selected read-only `petta-memory` evidence/artifact paths, excludes live Telegram/secrets/unbounded raw transcripts/writeable memory, and requires `needs_adjudication` output with `requires_adjudication=true`, `patch_proposal_only=true`, one worker turn, and `max_tool_calls=2`. Verification: py_compile, validator (`10/10`), fixture checker, targeted diff-check. No queue task enqueued, worker/supervisor launch, provider call, Telegram message, memory write, secrets/access change, paid compute, daemon/scheduler install, push/merge/force-push.

- [x] 2026-07-07: ThreadKeeper strict tool argument type validation. Branch `agent/threadkeeper-hardening-next` commit `25435f2`. `_validate_tool_args()` now rejects non-string tool arguments before execution instead of coercing JSON arrays/objects/numbers/booleans with `str()`, tightening validation for file, shell, search, tavily-search, and technical-analysis tools. Added focused tests/docs and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`158 passed`), `origin/pr-1` ancestor check, runtime-tree compile/source cmp. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-07: ThreadKeeper bounded run-index append tail reads. Branch `agent/threadkeeper-hardening-next` commit `82f490b`. Added bounded reverse-tail scanning for `index.jsonl` so finished-run appends and entry rotation no longer read an intentionally unrotated index file into memory just to find the previous hash or retain the newest N entries. Hash-chain linking/rotation semantics are preserved for normal indexes. Added focused tests/docs and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`157 passed`), `origin/pr-1` ancestor check, runtime-tree compile/source cmp. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-07: GoalChainer read-only sidecar over private ThreadKeeper task. Created `artifacts/ggb-capacity-gates/20260707-goalchainer-readonly-sidecar-private-task/` with `run_readonly_sidecar.py`, `.metta` sibling fixtures, and `report.json`. It reads the archived private OpenClaw ThreadKeeper smoke, injects read-only `petta-memory` STV/EC evidence, and calls `solve_incident(memory_items=...)` without Telegram/provider/runtime effects. Verification: harness `8/8`, focused GoalChainer memory tests (`52 passed`) with explicit local PeTTa/SWI env, fixture checker, py_compile, targeted diff-check. No live runtime/Telegram integration, memory write, supervisor launch, secrets/access changes, paid compute, push/merge/force-push.

- [x] 2026-07-07: ThreadKeeper transcript hash audit read cap. Branch `agent/threadkeeper-hardening-next` commit `a258c73`. Added `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_AUDIT_BYTES` (default 1048576, 0 disables) so read-only `verify_subagent_run_index()` size-checks each referenced transcript before reading it for SHA-256 verification; oversized transcripts return structured `transcript_too_large` audit issues without unbounded memory reads. Added focused tests/docs and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`155 passed`), `origin/pr-1` ancestor check, runtime-tree compile/source cmp. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-07: ThreadKeeper native worker HTTP response cap. Branch `agent/threadkeeper-hardening-next` commit `ddf9aae`. Added `OMEGACLAW_SUBAGENT_MAX_LLM_HTTP_RESPONSE_BYTES` (default 1048576, `0` disables) so native Ollama-compatible urllib worker calls bound the raw HTTP response body before JSON decoding; OpenAI-compatible SDK calls remain bounded after parsed content by `OMEGACLAW_SUBAGENT_MAX_RESPONSE_CHARS`. Added focused tests/docs and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`153 passed`), `origin/pr-1` ancestor check, runtime-tree compile/source cmp. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-07: ThreadKeeper audit/cap refresh GGB gate. Refreshed `GGB_CAPACITIES_ROADMAP.md` for ThreadKeeper head `080ed28` and archived `artifacts/ggb-capacity-gates/20260707-threadkeeper-audit-cap-refresh/` with `.metta` sibling fixtures mapping final emit/raw response/JSON audit/run-index audit/non-finite numeric hardening to GGB capacities 1.3, 3.2, 3.5, 4.5, 5.2, 5.3, and 5.4. Verification: focused mock pytest (`151 passed`), nested OmegaClaw-Core runtime `subagent.py` sync/compile, fixture checker, targeted `git diff --check`. No live runtime/Telegram/worker-supervisor launch, secrets/access changes, paid compute, daemon/scheduler install, push/merge/force-push.

- [x] 2026-07-07: ThreadKeeper run-index audit read cap. Branch `agent/threadkeeper-hardening-next` commit `080ed28`. Added `OMEGACLAW_SUBAGENT_MAX_INDEX_AUDIT_BYTES` (default 1048576, 0 disables) so read-only `verify_subagent_run_index()` returns structured `index_audit_too_large` before scanning oversized `index.jsonl` or transcript files. Added focused coverage/docs and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`151 passed`), `origin/pr-1` ancestor check, runtime-tree compile/source cmp. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-07: ThreadKeeper raw worker response cap. Branch `agent/threadkeeper-hardening-next` commit `fc34757`. Added `OMEGACLAW_SUBAGENT_MAX_RESPONSE_CHARS` (default 50000, minimum 1) so oversized raw worker responses return structured `response_too_large` before tool parsing/execution and transcript expansion; transcript stores a bounded preview and token accounting is preserved. Added focused coverage/docs and synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`149 passed`), `origin/pr-1` ancestor check, runtime-tree compile/source cmp. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-07: OmegaClaw/ZeroBot topology boundary review. Drafted `docs/omegaclaw_zerobot_topology_decision_note.md` and archived `artifacts/ggb-capacity-gates/20260707-topology-boundary-review/`. Recommendation: supervised queue-mediated bridge first; GoalChainer stays a read-only decision sidecar over bounded task text plus selected `petta-memory` evidence; ThreadKeeper remains delegation/audit/adjudication; direct group/direct recursive OpenClaw bridges deferred. Verification: doc exists, GGB fixture checker passed, targeted `git diff --check` passed. No live runtime behavior, secrets/access/security settings, paid compute, daemon/scheduler install, push/merge/force-push.

- [x] 2026-07-07: ThreadKeeper non-finite numeric env hardening. Branch `agent/threadkeeper-hardening-next` commit `2f0a10b`. `_env_float()` now rejects `nan`/`inf`/`-inf` env values and uses safe defaults for retry backoff, shell timeout, async worker poll/runtime, queued-task max age, and dispatch timeout knobs instead of allowing non-finite bounds into runtime control flow. Added focused reload test coverage and docs; synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`148 passed`), `origin/pr-1` ancestor check, runtime-tree compile/source cmp. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-06: PeTTa grounder specializer failed-memo fix. Branch `agent/specializer-failed-memo-fable` local commit `4ce1d0e`. Implemented Fable-tweaked conservative core in `src/specializer.pl`: failed-specialization memoization keyed by `(HV, Arity, normalized_bind_set)`, `copy_term`/`numbervars` variant-normalized specialization keys, failure cleanup via `forget_symbol(SpecName)` plus parent mapping retraction, and conservative global failed-memo invalidation. Added four repro fixtures and `tests/regression/test_specializer_regressions.sh`. Verification: regression script passed (repro2 linear 11 attempts vs 2047 pre-patch; repro3 no `&self` leak; repro4 normalized key), `sh run.sh examples/fib.metta` passed, full `timeout 180s sh test.sh` exited 0, Python `py_compile` passed, `git diff --check` passed. Not pushed. No live runtime wiring, secrets/access changes, paid compute, daemon/scheduler install, force-push, merge, or remote-ref deletion.
- [x] 2026-07-06: ThreadKeeper final emit size cap. Branch `agent/threadkeeper-hardening-next` commit `4d7d4f4`. Added `OMEGACLAW_SUBAGENT_MAX_EMIT_CHARS` (default 20000, minimum 1) so oversized worker `(emit ...)` final answers fail closed as `EMIT_PROTOCOL_VIOLATION` before becoming successful summaries or adjudication candidates. Added focused test coverage, env clamp/reload coverage, and docs; synced `subagent.py` to the OmegaClaw-Core runtime tree. Verification: `git diff --check`, `py_compile`, focused mock pytest (`147 passed`), runtime-tree compile. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.
- [x] 2026-07-06: OmegaClaw late-extension registry and context-overflow hardening. OmegaClaw-Core commit `98e8883` pushed to GitHub remote `fork` branch `agent/telegram-runtime-mods-checkpoint` (`bgoertzel-sing/ThreadKeeper`). Added context-overflow escalation/chunk fallback in `lib_llm_ext.py`, Telegram pending-message FIFO in `channels/telegram.py`, `lib_extensions.metta`/`src/extensions.py` status/config hook, and versioned the MesTTo `omegaclaw-deontic` bundle files/tests/docs. Live deontic/directive import remains deferred because in-loop `import!` can still hang SWI; local runner default keeps `OMEGACLAW_LATE_EXTENSIONS` empty. Verification: py_compile, diff-check, deontic core tests 10/10, integration tests 7/7, late-loader smoke reports deferred instead of hanging; local install has one supervised native Telegram runner with low/stable CPU.

- [x] 2026-07-06: ThreadKeeper configurable JSON audit/task read cap. Branch `agent/threadkeeper-hardening-next` commit `209da6c`. Added `OMEGACLAW_SUBAGENT_MAX_JSON_FILE_BYTES` (default 262144, minimum 1024) so queue records and reviewable transcript JSON use a tunable local read cap instead of an untunable hard-coded limit. `_read_json_file()` still supports explicit per-call caps, but default reads now use the knob; oversized-file errors no longer echo the local path. Added 2 focused tests plus env reload coverage. Verification: `git diff --check`, `py_compile`, focused mock pytest (`146 passed`), `origin/pr-1` ancestor check via existing local ref, sync to OmegaClaw-Core runtime tree with zero diff. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-06: GoalChainer multi-scenario memory-evidence smoke. Created `tests/test_multi_scenario_memory_bridge.py` (34 tests) covering 4 baseline incident types (PII standard, public data, unverified facts, public+unverified) and 4 conflicting-memory variants. Key findings: (1) deontic layer is never overridden by memory evidence — `publish_raw_log` stays blocked when privacy is at stake even with STV 0.99/0.99 + EC 99:1 memory evidence; (2) all 4 baseline scenarios produce distinct belief-strength profiles; (3) memory evidence shifts beliefs in expected direction — confirming memory increases strength, conflicting memory decreases it; (4) memory evidence is action-local (memory for `publish_raw_log` does not affect `publish_redacted_summary` belief); (5) EC (EvidencePacket) atoms also correctly shift beliefs. Full suite: `87 passed, 6 skipped, 0 failed` (up from 53/6/0). Archived gate at `artifacts/ggb-capacity-gates/20260706-goalchainer-multi-scenario-smoke/` with `.metta` sibling fixtures; GGB fixture checker passes across all 20 gate fixtures. Updated `GGB_CAPACITIES_ROADMAP.md`, `GOALCHAINER_INTEGRATION_MAP.md`. No live Telegram/OmegaClaw runtime integration, secrets/access/security changes, paid compute, push/merge/force-push, daemon/scheduler install, or remote-ref deletion.

- [x] 2026-07-06: ThreadKeeper workspace file size cap for write-file/append-file. Branch `agent/threadkeeper-hardening-next` commit `c6f9708`. Added `OMEGACLAW_SUBAGENT_MAX_FILE_SIZE_CHARS` (default 100000, 0 disables) to cap resulting file size for write-file and append-file. For write-file, content exceeding the cap is rejected before any disk write. For append-file, existing file size is checked via `os.path.getsize()` before reading into memory (preventing memory exhaustion from very large files grown through repeated appends), and resulting size is checked before writing. 7 focused tests added (144 total). Verification: `git diff --check`, `py_compile`, focused mock pytest (`144 passed`), `origin/pr-1` ancestor check (76 commits ahead), sync to OmegaClaw-Core runtime tree with zero diff. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.
- [x] 2026-07-06: ThreadKeeper search/tavily-search/technical-analysis output size cap. Branch `agent/threadkeeper-hardening-next` commit `ee894d3`. Added `OMEGACLAW_SUBAGENT_MAX_SEARCH_OUTPUT_CHARS` (default 4000, 0 disables) to cap external tool output at the tool level, matching the defense-in-depth pattern already used by `_tool_read_file` (`_SUBAGENT_MAX_READ_FILE_CHARS`) and `_tool_shell` (`_SHELL_OUTPUT_CAP`). External search/tavily-search/technical-analysis API responses can be arbitrarily large; while `run_tools` clips results to 2000 chars for the prompt, the full unbounded response was in memory before clipping. Added `_bound_tool_output()` helper that reads the module-level config at call time (not default-arg time) so monkeypatching works in tests. All three search-type tool registrations in `_build_tool_registry()` are now wrapped with `_bound_tool_output()`. 6 focused tests added (137 total): large result truncation with marker, small result preservation, cap disabled when 0, non-string result handling, search registry wrapping, tavily/technical-analysis registry wrapping. Verification: `git diff --check`, `py_compile`, focused mock pytest (`137 passed`), `origin/pr-1` ancestor check (75 commits ahead), sync to OmegaClaw-Core runtime tree with zero diff. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-06: ThreadKeeper empty search/tavily-search/technical-analysis query rejection. Branch `agent/threadkeeper-hardening-next` commit `86cc243`. Extended `_validate_tool_args` to reject empty or whitespace-only query arguments for `search`, `tavily-search`, and `technical-analysis` tools, matching the existing pattern for `shell` commands and file paths. This prevents wasted external API calls from malformed or adversarial worker responses that pass an empty query. 2 focused tests added (131 total): empty/whitespace query rejection across all three search-type tools and non-empty query acceptance. Verification: `git diff --check`, `py_compile`, focused mock pytest (`131 passed`), `origin/pr-1` ancestor check (74 commits ahead), sync to OmegaClaw-Core runtime tree with zero diff. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-06: ThreadKeeper run index entry bounding with rotation. Branch `agent/threadkeeper-hardening-next` commit `ca98d36`. Added `OMEGACLAW_SUBAGENT_MAX_INDEX_ENTRIES` (default 0 = disabled) to cap the number of entries in `index.jsonl`. When non-zero, the index is rotated after each append to keep only the most recent N entries, with the hash chain recomputed for retained entries (first retained entry gets `previous_entry_sha256=""`). This prevents unbounded audit log growth in long-running @Protomegabot deployments. `verify_subagent_run_index` still passes on the retained portion after rotation. 5 focused tests added (129 total): rotation truncates to cap, disabled when 0, no rotation under cap, rotated index verifies correctly, single-entry cap. Verification: `git diff --check`, `py_compile`, focused mock pytest (`129 passed`), `origin/pr-1` ancestor check (73 commits ahead), sync to OmegaClaw-Core runtime tree with zero diff. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-06: ThreadKeeper transcript summary bounding and empty shell command rejection. Branch `agent/threadkeeper-hardening-next` commit `fb60ebf`. Added `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_SUMMARY_CHARS` (default 0 = disabled) to cap the transcript record's `summary` field with an explicit truncation marker, complementing existing turn-count and per-field bounding. Strengthened `_validate_tool_args`: shell commands must be non-empty after stripping whitespace, closing a gap where `(shell "")` passed validation but produced a confusing runtime error. 5 focused tests added (124 total). Verification: `git diff --check`, `py_compile`, focused mock pytest (`124 passed`), `origin/pr-1` ancestor check (72 commits ahead), sync to OmegaClaw-Core runtime tree with zero diff. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-06: ThreadKeeper per-task duration and total runtime in worker loop results. Branch `agent/threadkeeper-hardening-next` commit `1c6c0c6`. Worker loop result items now include `task_duration_s` (wall-clock seconds) for each drained task (both successful and error). Structured return now includes `total_runtime_s` across all return paths. 5 focused tests added (119 total). Verification: `git diff --check`, `py_compile`, focused mock pytest (`119 passed`), `origin/pr-1` ancestor check (71 commits ahead), sync to OmegaClaw-Core runtime tree with zero diff. No paid compute, live wiring, secrets/access changes, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-06: GoalChainer heuristic PLN bypass for PeTTaChainer `compileadd` bottleneck. Created `src/goal_chainer/heuristic_beliefs.py` implementing `grade_beliefs_heuristic()` that mirrors PLN rule semantics from `evidence_chainer.py` using subjective-logic fusion on the same ground-fact strengths and rule STV values. Modified `metta_reasoner.py` with automatic heuristic fallback via `_pettachainer_available()` quick check and module-level failure cache. Added 30s subprocess timeout to `petta_runtime.py` `run_metta()`. Results: full test suite `35 passed, 6 skipped, 0 failed` (up from 26/6/9); full `solve_incident` pipeline returns correct decision (`publish_redacted_summary` recommended/obligated, `publish_raw_log` blocked/forbidden, `hold_external_update` weak/permitted). Archived gate `artifacts/ggb-capacity-gates/20260706-goalchainer-heuristic-pln-bypass/` with `.metta` sibling fixtures. Updated `GOALCHAINER_INTEGRATION_MAP.md`, `GGB_CAPACITIES_ROADMAP.md` Bundle D, `NOTES.md`, `TASKS.md`. Verification: `py_compile`, full pytest, `solve_incident` end-to-end, GGB fixture checker. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, push/merge/force-push, daemon/scheduler install, or remote-ref deletion.

- [x] 2026-07-06: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `1c6c0c6` (`Add per-task duration and total runtime to worker loop results`): each result item in the worker loop output now includes `task_duration_s` (wall-clock seconds from task start to completion) for both successful and error results, and the structured return now includes `total_runtime_s` across all return paths (`worker_idle`, `worker_drained`, `worker_config_invalid`, `worker_already_running`). Added 5 focused tests. Verification: `git diff --check`, `python3 -m py_compile`, focused mock pytest (`119 passed`), `origin/pr-1` remains an ancestor (71 commits ahead). Synced `subagent.py` to OmegaClaw-Core runtime tree. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.
- [x] 2026-07-06: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `1f4d70b` (`Add completion fields and queue depth to worker loop lock metadata`): the finished lock metadata now includes `tasks_completed`, `consecutive_errors`, and `remaining_queue_tasks`, matching fields present in the running lock metadata. Previously the finished metadata dropped `tasks_completed` and `consecutive_errors`, leaving operators without completion counts in the final lock file. `remaining_queue_tasks` is also now included in both the pre-task and post-task running lock metadata, giving operators live queue depth visibility while the worker is actively processing. Added 3 focused tests: (1) finished lock metadata includes completion fields after a clean `worker_idle` exit; (2) running lock metadata includes `remaining_queue_tasks` during task execution with decreasing queue depth across multiple tasks; (3) finished lock metadata reflects errors after worker failures. Verification: coordinated against PR #1 (`origin/pr-1` remains an ancestor, 70 commits ahead), `git diff --check`, `python3 -m py_compile`, focused mock pytest (`114 passed`). Synced `subagent.py` to OmegaClaw-Core runtime tree. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-06: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `41f863c` (`Add current-task tracking to worker loop lock metadata`): the bounded async worker loop now writes `current_task_started_at` and `current_task_queue_path` into the lock metadata before calling `run_queued_dispatch`, then clears them after the task completes. This improves stale-lock crash diagnostics: when a worker crashes mid-task (SIGKILL/OOM), the `stale_lock` metadata now shows exactly which task was being processed and when it started. The initial and finished lock metadata both set `current_task_*` to `None`. Added 3 focused tests: lock metadata during task execution includes current-task fields, stale lock from crashed mid-task worker includes current-task fields, finished lock metadata has null current-task fields after clean exit. Verification: coordinated against PR #1 (`origin/pr-1` remains an ancestor, 69 commits ahead), `git diff --check`, `python3 -m py_compile`, focused mock pytest (`111 passed`). Synced `subagent.py` to OmegaClaw-Core runtime tree. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-06: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `6bbf76d` (`Detect stale worker lock from crashed previous worker`): the bounded async worker loop now reads existing lock metadata before acquiring the flock; if the file shows `status=running` but the flock can be acquired (meaning the previous worker died via SIGKILL/OOM/etc.), the structured return includes `stale_lock` audit metadata (pid, started_at, max_tasks, tasks_attempted, etc.) so operators and supervisors can detect crashed workers. The `stale_lock` field is included in all return paths (early no-claim, already-running, and normal) for consistency. Added 3 focused tests: stale lock from simulated crash, no stale lock on fresh start, no stale lock after clean shutdown. Verification: coordinated against PR #1 (`origin/pr-1` remains an ancestor, 68 commits ahead), `git diff --check`, `python3 -m py_compile`, focused mock pytest (`108 passed`). Synced `subagent.py` to OmegaClaw-Core runtime tree. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-05: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `25483fb` (`Sanitize absolute paths from tool error messages`): tool error messages (read-file, write-file, append-file, shell) and `_resolve_workspace_path` errors no longer leak absolute filesystem paths to the worker LLM or into persisted transcripts. A new `_sanitize_error_msg()` helper replaces the workspace root with `<workspace>` and remaining absolute Unix paths with `<path>`, keeping non-path messages unchanged. Also removed workspace root from the `_resolve_workspace_path` escape error and the shell missing-workspace error to prevent leaking at the source. Added 4 focused tests: path escape in read/write/append tools, `_resolve_workspace_path` error content, `_sanitize_error_msg` replacement behavior, and shell missing-workspace error sanitization. Verification: coordinated against PR #1 (`origin/pr-1` remains an ancestor, 67 commits ahead), `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`105 passed`). No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-05: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `c8a14e4` (`Add graceful SIGTERM/SIGINT handling to worker loop`): the bounded async worker loop now registers SIGTERM/SIGINT handlers that set a module-level flag instead of raising, so the loop exits cleanly with `stop_reason="signal"` at the next iteration check rather than dying abruptly mid-task. This prevents orphaning a `.claimed` queue record and leaving the lock file in `running` state when a supervisor sends SIGTERM. Prior signal handlers are restored in the `finally` block. Added 2 focused tests: graceful signal shutdown and signal handler restoration. Verification: coordinated against PR #1 (`origin/pr-1` remains an ancestor, 66 commits ahead), `git diff --check`, `python3 -m py_compile`, and focused mock pytest (`101 passed`). No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-05: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `14ec2ee` (`Add dispatch-level token budget cap`): `OMEGACLAW_SUBAGENT_MAX_TOKENS_PER_DISPATCH` (default 0 = disabled) caps total accumulated worker LLM tokens (input + output) per dispatch. When non-zero, the dispatch loop checks after each worker LLM call and returns a structured `token_budget_exceeded` record if the cap is exceeded, with `worker_token_usage` persisted to the transcript. This complements the existing per-turn/per-dispatch tool-call quotas and wall-clock timeout, adding a direct cost-control ceiling that prevents runaway token spend across many turns. Added 3 focused tests: cap exceeded after second LLM call, cap disabled when zero, and normal completion under the cap. Verification: coordinated against PR #1 (`origin/pr-1` remains an ancestor, 65 commits ahead), `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`99 passed`). No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-05: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `ec96332` (`Bound transcript turn records and add retry backoff jitter`): the local transcript run record is now bounded via `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_TURNS` (default 0 = disabled; when set, keeps most recent N turns with `transcript_truncated` marker) and `OMEGACLAW_SUBAGENT_MAX_TRANSCRIPT_FIELD_CHARS` (default 0 = disabled; when set, truncates per-field strings — prompt, raw_response, tool_results — with explicit truncation markers). This prevents unbounded disk writes from long-running or runaway dispatches. Retry backoff in `_call_with_retries` now adds jitter (up to 25% of the exponential base delay) to prevent thundering-herd retry storms when multiple subagents hit the same endpoint simultaneously. Added 5 focused tests (turn cap, field size cap, disabled cap, non-string field preservation, retry jitter). Verification: coordinated against PR #1 (`origin/pr-1` remains an ancestor), `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`94 passed`). No paid compute, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-05: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `225d441` (`Bound worker loop results and add live lock metadata`): the bounded async worker loop now caps the returned results list via `OMEGACLAW_SUBAGENT_ASYNC_WORKER_MAX_RESULTS` (default 16, 0 disables). When the cap is exceeded, older entries are dropped and counted as `results_truncated` in the structured return, preventing unbounded structured returns when draining many queued tasks. The running lock metadata now includes `tasks_attempted`, `tasks_completed`, `consecutive_errors`, and `error_count`, updated after each task for operator visibility. Added focused tests for results truncation, truncation disabled, and live lock metadata counters. Verification: coordinated against PR #1 (`origin/pr-1` remains an ancestor), `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`, and focused mock pytest (`89 passed`). No paid compute, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-05: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `d9b9b56` (`Add max_consecutive_errors to worker loop`): the bounded async worker loop now tracks consecutive `queue_worker_error` results and exits early when the cap is reached, preventing wasted work on a poisoned queue. The limit is configurable via `OMEGACLAW_SUBAGENT_ASYNC_WORKER_MAX_CONSECUTIVE_ERRORS` (default 3) and the explicit `max_consecutive_errors` parameter (0 disables). The structured return and lock metadata now include `consecutive_errors` and `error_count`. Added focused tests for the cap triggering, error reset on success, disabled limit, and malformed-arg rejection. Verification: coordinated against PR #1 (`origin/pr-1` remains an ancestor), `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`, and focused mock pytest (`86 passed`). No paid compute, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-05: After Ben approved the ThreadKeeper smoke, completed two gated smokes:
  1. **Supervisor/provider-boundary smoke** (`artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-supervisor-provider-smoke/`): added `local/run-threadkeeper-worker-loop-supervisor-provider-smoke.py`; it starts a local fake Ollama-compatible `/api/chat` server, queues one checksum-sidecar task, launches the supervisor as a separate process with `max_tasks=1`, and verifies the worker claims, calls the fake provider once, writes `.done`/result sidecars, and exits `worker_drained`. Result: `smoke_passed`, 1 fake provider call, 0 remaining queue tasks. Added `.metta` sibling fixtures.
  2. **Private/non-group OpenClaw smoke** (`artifacts/ggb-capacity-gates/20260705-threadkeeper-private-openclaw-smoke/`): one queued task was claimed by `run_queued_worker_loop(max_tasks=1)`, made one real local OpenClaw Gateway `/v1/chat/completions` call (HTTP 200), returned `needs_adjudication` as intended, recorded 16,756 worker tokens, and retained `.done`/result/checksum/transcript evidence. Added `.metta` sibling fixtures.
  Verification for both: harness `py_compile`, supervisor `bash -n`, smoke runs, focused ThreadKeeper pytest (`82 passed`), `git diff --check`, and GGB fixture checker on both gates. No Telegram, OmegaClaw runtime, external provider, secrets, paid compute, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.

- [x] 2026-07-05: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `85145ea` (`Bound worker env file parsing`): `scripts/run-subagent-worker-loop --env-file` now rejects symlink env files, non-regular files, files larger than 64 KiB, and overlong env lines/values before importing `subagent`, extending the staged async-worker config hardening without touching live Telegram/OmegaClaw runtime wiring. Verification: coordinated against PR #1 (`origin/pr-1` remains an ancestor of the branch), `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`, and focused mock pytest (`82 passed`). No paid compute, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-05: Completed a non-live ThreadKeeper supervisor-boundary cancellation gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-supervisor-cancelled-task/`. Tightened `local/threadkeeper-worker-loop-supervisor.sh` to launch the runner as an argv array via `setsid` rather than a shell-constructed `bash -c` string, then added `local/run-threadkeeper-worker-loop-supervisor-cancel-smoke.py`. The harness queued one checksum-sidecar task, created its cancellation token before supervisor claim, and verified the separate supervised worker process returned `worker_drained` with one task attempted/completed, zero remaining queue tasks, `.done`/result/checksum/transcript evidence, and task result `cancelled` before worker LLM/provider use. Verification: harness `py_compile`, supervisor `bash -n`, smoke run, focused ThreadKeeper pytest (`81 passed`), `git diff --check`, and the GGB fixture checker for the new gate. No Telegram/OmegaClaw runtime wiring, model/provider call, secrets, paid compute, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.

- [x] 2026-07-05: Added `local/threadkeeper-worker-loop-supervisor.sh` (start/stop/status/log) as a non-live staging supervisor for the ThreadKeeper bounded async worker-loop, modeled on the existing Telegram supervisor pattern. Archived gate `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-supervisor-boundary/` with `RUN.md`, `protomegabot-worker.env`, `.metta` sibling fixtures, and `report.json`. The supervisor launches the worker-loop runner with no-claim defaults (`max_tasks=0`), the runner produced `status=worker_idle` with zero tasks attempted/completed, and start/status/stop/log all function correctly. Verification: `bash -n`, runner `py_compile`, supervisor start/status/stop/log, focused ThreadKeeper pytest (`81 passed`), `git diff --check`, and GGB fixture checker on the new gate (9 checks, 9 ggb-check atoms) plus all 7 prior gate fixtures. No paid compute, live OmegaClaw/Telegram/runtime wiring, secrets/access/security settings, scheduler/daemon install, worker LLM call, or queued task claim.

- [x] 2026-07-05: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `9e9dda2` (`Reject unsafe worker env-file keys`): `scripts/run-subagent-worker-loop --env-file` now rejects process-control keys (`PATH`, `PYTHONPATH`, `PYTHONHOME`, `LD_*`, `DYLD_*`, `BASH_ENV`, `ENV`, `HOME`, `IFS`, `SHELL`) before importing `subagent`, keeping staged operator config files from changing interpreter/subprocess loading behavior. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`, and focused mock pytest (`81 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-05: Completed the follow-on non-live @Protomegabot-config ThreadKeeper one-task worker-loop smoke at `artifacts/ggb-capacity-gates/20260705-threadkeeper-protomegabot-one-task-smoke/`. Added `local/run-threadkeeper-worker-loop-one-task-smoke.py`; it loads the same non-secret staging env, creates artifact-local persona/workspace/run records, queues exactly one checksum-sidecar mock task, monkeypatches the worker LLM call to a deterministic in-process emit, and drains via `subagent.run_queued_worker_loop(max_tasks=1)`. Verification: harness/runner `py_compile`, one-task smoke (`smoke_passed`, worker `worker_drained`, one attempted/completed, zero pending queue tasks), wrapper `bash -n`, focused ThreadKeeper pytest (`80 passed`), `git diff --check`, and GGB fixture checker. No Telegram/OmegaClaw runtime wiring, OpenClaw Gateway/model/provider call, secrets, paid compute, daemon/scheduler install, force-push, merge, or remote-ref deletion.

- [x] 2026-07-05: Added a conservative non-live @Protomegabot-config ThreadKeeper worker-loop wrapper at `local/run-threadkeeper-worker-loop-smoke.sh` plus archived gate `artifacts/ggb-capacity-gates/20260705-threadkeeper-protomegabot-config-smoke/`. The non-secret `protomegabot-worker.env` pins OmegaClaw-local workspace/persona paths and bounded worker defaults; the wrapper invokes `scripts/run-subagent-worker-loop` with explicit no-claim bounds. Verification: `bash -n`, runner `py_compile`, wrapper smoke (`worker_idle`, `max_tasks=0`, zero tasks attempted/completed), `git diff --check`, focused mock pytest (`80 passed`), and the GGB fixture checker for the new gate. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, scheduler/daemon install, worker LLM call, or queued task claim.

- [x] 2026-07-05: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `120d689` (`Load env files in worker loop runner`): `scripts/run-subagent-worker-loop` now accepts repeatable `--env-file` operator config files parsed as shell-free `KEY=VALUE` before importing `subagent`, with malformed lines/unsafe keys failing closed and `--run-dir` staying the explicit final override. Archived non-live runner smoke at `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-env-runner/`; direct `--max-tasks 0` smoke returned `worker_idle` with zero tasks attempted. Verification: `git diff --check`, `python3 -m py_compile`, focused mock pytest (`80 passed`), and direct env-file runner smoke. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `4812345` (`Add artifact-local worker loop smoke`): added `Autotests/mock/run_worker_loop_one_task_smoke.py`, a non-live deterministic smoke that queues one artifact-local mock task and drains it through the real bounded async worker loop with a local fake worker response; added subprocess pytest coverage and archived the staged gate at `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-loop-one-task/`. Verification: `git diff --check`, `python3 -m py_compile`, focused mock pytest (`78 passed`), and direct artifact smoke (`worker_drained`, one task attempted/completed, zero remaining, persisted queue/result/checksum/transcript/index evidence). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `10f69bf` (`Validate worker loop explicit bounds`): `subagent.run_queued_worker_loop(...)` now fail-closes with structured `worker_config_invalid` before lock acquisition or queue claim when explicit operator/Python bounds are malformed (boolean/string/fractional integer task/idle limits, non-finite poll intervals, or negative runtime caps). Env defaults still parse defensively at import. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`, and focused mock pytest (`77 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `61bce9c` (`Validate worker loop stop file config`): the bounded async worker loop now validates explicit/env stop-file values before acquiring `.async-worker.lock` or claiming any queued task, returning structured `worker_config_invalid` for NUL-containing or overlong paths. Added focused regression coverage and updated the subagent reference docs. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py scripts/run-subagent-worker-loop`, and focused mock pytest (`76 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

- [x] 2026-07-05: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `c7beaf0` (`Reject expired queued tasks before worker LLM calls`): queued-worker validation now checks `time.time() - queued_at` against `OMEGACLAW_SUBAGENT_MAX_QUEUED_TASK_AGE_S` (default 0 = disabled) and rejects expired tasks before any worker LLM call, failing closed as `queue_worker_error` with `.failed` retention and audit sidecars. Added focused tests for expired task rejection and fresh task acceptance. Verification: `git diff --check`, `python3 -m py_compile`, focused mock pytest (`96 passed`), GGB fixture checker across all 14 gates. No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.
- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `bb6c8c7` (`Add worker loop runtime-cap and error-continuation tests`): two new focused tests cover the `max_runtime_s` wall-clock timeout exit path (first task completes, clock jumps past cap, second task remains pending) and the worker-error-continuation path (first queued task raises a simulated exception, loop records `queue_worker_error` and continues to the second task which succeeds). Focused mock pytest now passes 75 tests. Verification: `git diff --check`, `python3 -m py_compile`, focused mock pytest (`75 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.
- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `c4ae8a8` (`Add bounded subagent worker loop runner`): added `scripts/run-subagent-worker-loop` as a conservative operator/supervisor entrypoint for the async worker loop. It imports `subagent` after applying an optional `--run-dir`, invokes one bounded `run_queued_worker_loop(...)` run, and prints the structured JSON result. `--max-tasks 0` is the intended no-claim smoke for install/supervisor wiring checks. Added a script smoke test to the focused mock suite, and updated `docs/reference-skills-subagent.md`. Verification: `git diff --check`, `python3 -m py_compile`, direct script invocation (`--max-tasks 0` returns `worker_idle`), and focused mock pytest (`73 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.
- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `90f42f5` (`Add queued worker loop lock metadata`): the bounded async worker loop now writes compact JSON owner/status metadata into `.async-worker.lock` while running, returns readable `worker_lock` metadata on `worker_already_running`, and leaves final `finished`/`stop_reason`/attempt metadata for operator/supervisor audit. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`72 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

- [x] 2026-07-04: Ben explicitly approved adding a real ThreadKeeper async worker loop. ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `cc3cd1e` (`Add bounded queued worker loop`): `subagent.run_queued_worker_loop(...)` now repeatedly claims queued dispatch records until explicit bounds are reached (`max_tasks`, `max_idle_polls`, `max_runtime_s`, or `stop_file`) and uses a best-effort `.async-worker.lock` to avoid concurrent local drain loops. It still does not self-start from parent `dispatch` and remains supervisor/operator launched. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`71 passed`). No paid compute, live OmegaClaw/Telegram/runtime install, secrets/access/security settings, force-push, merge, or remote-ref deletion.

- [x] 2026-07-04: Refreshed the GGB roadmap and reusable ThreadKeeper hardening gate fixture to ThreadKeeper head `c041d24`: capacities 3.2/4.5/5.2 now include queued-task coerced-integer rejection (`ac7dfd4`) and queued cancellation-token preservation into worker execution (`c041d24`). Verified ThreadKeeper `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, focused mock pytest (`68 passed`), and the GGB sibling-fixture checker across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gates. No live OmegaClaw/Telegram/runtime integration, secrets/access/security changes, paid compute, push/merge, daemon, or live async worker loop.

- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `c041d24` (`Preserve queued subagent cancellation token`): queued-worker execution now carries the queued task `cancel_file` into the synchronous worker dispatch while suppressing queue-only mode, so a cancellation token created after enqueue but before worker claim stops the task before any worker LLM call. The worker restores the prior module cancellation state afterward and still retains the claimed task as `*.done` plus compact result audit sidecar when cancellation is the final dispatch result. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`68 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `ac7dfd4` (`Reject coerced queued task integers`): queued-worker validation now rejects checksum-valid queue records whose integer metadata is only coercible rather than actually JSON-integer typed (`max_turns: 1.5`, `max_chars: "1000"`) before any worker LLM call. Bad claimed tasks still fail closed as `queue_worker_error` and are retained as `*.failed` plus compact audit sidecars. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`67 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

- [x] 2026-07-04: Added fail-closed per-day Fable cost-limit enforcement to the enabled local `intent-model-router` plugin. Fable routing now checks today's local-Pacific ledger spend before selecting `anthropic/claude-fable-5`; the default daily limit is `$0` unless `fableDailyBudgetUsd` is set, and same-day overrides require `fableDailyBudgetOverride` with `approvedBy` beginning `human`, a reason, date, and higher `limitUsd`. Deprecated `allowExplicitOverBudget` is ignored. Ledger entries now carry `day` and daily budget summaries. Verification: `node --check`, transformed helper self-test for daily budget/off/explicit/override behavior, `jq` schema validation, and `openclaw plugins list` confirmed the router remains enabled. No Anthropic/Fable paid call, key change, or Gateway restart.

- [x] 2026-07-04: Prepared the local `intent-model-router` plugin for Ben's expected Anthropic API key and added cost telemetry. The plugin now supports routine/deep/Anthropic routing tiers, conservative OmegaClaw/ProtomegaTron routing, configurable `anthropicModel` guarded by `enableAnthropic`, optional long-prompt Anthropic routing, and `llm_output` JSONL usage/cost records that omit prompt/assistant content. Verification: `node --check`, helper self-test for classification/cost estimation, `jq` schema validation, and `openclaw plugins list` showing the router and Anthropic provider enabled. No key installed, Gateway restart, secret change, or paid call.

- [x] 2026-07-04: Refreshed the GGB roadmap plus the reusable ThreadKeeper hardening gate fixture to ThreadKeeper head `7628f49`: capacities 3.2/4.5/5.2 now explicitly include queued-task checksum/schema validation, strict queued task-contract list/numeric validation, and fail-closed retention of bad claimed tasks before worker LLM calls. Verification: ThreadKeeper `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, focused mock pytest (`66 passed`), and the GGB sibling-fixture checker across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gates. No live OmegaClaw/Telegram/runtime integration, secrets/access/security changes, paid compute, push/merge, daemon, or live async worker loop.

- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `7628f49` (`Tighten queued task contract schema`): queued-worker validation now rejects checksum-valid queue records with non-finite/boolean numeric metadata (`queued_at`, `max_turns`, `max_chars`) and malformed task-contract list fields before any worker LLM call. Bad claimed tasks still fail closed as `queue_worker_error` and are retained as `*.failed` plus compact result sidecars. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`66 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `7a1866d` (`Validate queued subagent task schema`): queued-worker validation now rejects checksum-valid but schema-invalid queue records before any worker LLM call, including unexpected fields, unsafe/unbounded `run_id`, invalid `queued_at`, and malformed/oversized/NUL-containing `cancel_file` metadata. This tightens queue/task contract integrity while retaining bad claimed tasks as `*.failed` plus compact result audit sidecars. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`64 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `0cde0c7` (`Bound subagent shell output controls`): the optional allowlisted subagent `shell` tool now defensively parses `OMEGACLAW_SUBAGENT_SHELL_OUTPUT_CAP` (default 4000) and `OMEGACLAW_SUBAGENT_SHELL_TIMEOUT_S` (default 30.0), and capped stdout/stderr returns carry an explicit truncation marker instead of silent slicing. This tightens strict tool-argument/resource validation while preserving disabled-by-default, command-name-only executable allowlist, argv-list/no-shell execution, workspace cwd, sanitized PATH/env, no stdin, argv cap, timeout, and output cap behavior. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`63 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `30adb54` (`Bound optional subagent shell argv`): the optional allowlisted subagent `shell` tool now has a defensively parsed `OMEGACLAW_SUBAGENT_SHELL_MAX_ARGV` cap (default 32) and rejects overlong argv lists plus NUL-containing argv tokens before launching subprocesses. This tightens strict tool-argument validation while preserving disabled-by-default, argv-only/no-shell, workspace cwd, sanitized PATH/env, no stdin, output cap, and executable allowlist behavior. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`62 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

- [x] 2026-07-04: Refined `GGB_CAPACITY_GATE_TEMPLATE.md` to make source-grounding and claim/evidence separation explicit for future capacity gates: mutable state must be inspected from current files/commands, external exploratory sources need path/URL plus commit/date when available, untrusted content must be marked, and gate evidence now separates direct observations/check outputs from inferences and excluded untested claims. Refreshed `GGB_CAPACITIES_ROADMAP.md` capacities 2.1 and 5.4 accordingly. Verification: template/roadmap inspection plus GGB sibling-fixture checker passed across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gates. No live OmegaClaw/Telegram/runtime integration, secrets/access/security changes, paid compute, push/merge, daemon, or live async worker loop.

- [x] 2026-07-04: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `f916dfe` (`Verify queued subagent task checksums`): queue-only dispatch now writes a required `<queue-task>.sha256` sidecar and returns `queue_sha256_path`; `subagent.run_queued_dispatch(queue_path)` verifies the claimed task checksum before queued-task validation or any worker LLM call, failing closed and retaining bad/tampered tasks as `*.failed` plus compact result/checksum audit sidecars. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`61 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.

- [x] 2026-07-03: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `76bd2c4` (`Preserve queued subagent task contracts`): queued-worker execution now validates the queued `task_contract` and re-injects it into the synchronous worker dispatch, so queue-only tasks do not drop `allowed_paths`, `forbidden_actions`, quota narrowing, patch-proposal, or adjudication constraints when later consumed. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`59 passed`). No paid compute, live OmegaClaw/Telegram/runtime integration, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.
- [x] 2026-07-03: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `d0d1dfa` (`Reject queue result sidecars as worker tasks`): explicit `subagent.run_queued_dispatch(...)` calls now accept only live pending `queue/*.json` task records and reject retained audit sidecars such as `*.done.result.json` / `*.failed.result.json` before any atomic claim/rename. This closes an operator-error path where a result sidecar could be consumed and moved into failed state if passed directly to the worker primitive. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`58 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.
- [x] 2026-07-03: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `b14ade5` (`Add subagent run index verifier`) after prior candidate-review commit `ee883ce`: added `subagent.verify_subagent_run_index(index_path=None)` as a bounded read-only audit helper for the compact `index.jsonl` run index. It verifies `previous_entry_sha256`/`entry_sha256` hash-chain integrity plus recorded local transcript SHA-256s and returns compact JSON (`index_verified`, `index_tampered`, `index_missing`, `index_audit_error`) without repairing/replacing files, draining queues, calling an LLM, daemonizing, self-scheduling, changing live runtime behavior, or expanding transcripts into parent context. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`57 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, remote-ref deletion, or live async worker loop.
- [x] 2026-07-03: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `ee883ce` (`Add subagent candidate review helper`): added `subagent.review_subagent_candidate(transcript_path)` as a non-mutating parent/operator review harness for `patch_proposal_only` and `requires_adjudication` transcripts. It constrains review to `OMEGACLAW_SUBAGENT_RUN_DIR`, verifies optional `.sha256` sidecars, returns compact JSON gates (`patch_proposal_review`, `adjudication_required`), and deliberately does not apply patches, accept final answers, call an LLM, drain queues, daemonize, self-schedule, or change live runtime behavior. Verification was included in the subsequent `57 passed` focused mock pytest gate. No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, remote-ref deletion, or live async worker loop.

- [x] 2026-07-03: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `38ae193` (`Ignore queue result sidecars when draining`): pending queue listing/backpressure now count only live `queue/*.json` task records and ignore retained `*.done.result.json` / `*.failed.result.json` audit sidecars, so failed/done result records are not re-drained or counted as false backpressure. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`52 passed`). Refreshed the GGB roadmap/gate fixture to head `38ae193`. No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, remote-ref deletion, daemon, or live async worker loop.
- [x] 2026-07-03: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `5a472cd` (`Retain failed queued subagent claims`): queued-worker failures after atomic claim now retain the task as `*.failed` and write `*.failed.result.json`, preventing malformed claimed tasks from lingering or vanishing without audit evidence. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`52 passed`). Refreshed the GGB roadmap/gate fixture to head `5a472cd`. No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.
- [x] 2026-07-03: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `ec17402` (`Add bounded queued dispatch drain helper`): `subagent.drain_queued_dispatches(max_tasks=1)` now wraps the queued-worker primitive in a bounded operator-supervised drain call, selecting pending `queue/*.json` tasks oldest-first, running at most the requested/clamped count, returning compact JSON drain metadata, preserving `OMEGACLAW_SUBAGENT_QUEUE_ONLY`, and deliberately not daemonizing/polling/self-scheduling. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`51 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.
- [x] 2026-07-03: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `8eae787` (`Add queued subagent worker primitive`): `subagent.run_queued_dispatch(queue_path)` now atomically claims one queued `queue/*.json` task, revalidates task shape/path, suppresses queue-only mode only around the actual worker dispatch, writes compact `*.result.json`, and leaves the consumed task as `*.done` for audit. Malformed/escaping queue paths return structured `queue_worker_error` before any worker LLM call. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`49 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.
- [x] 2026-07-03: Refreshed the GGB roadmap plus ThreadKeeper hardening gate fixture for queue-only dispatch/adjudication evidence: `a33b1e3` queue-only mode persists durable `queue/*.json` task records with `queue_sha256` and fail-closed `queue_backpressure` before worker LLM calls; `09899a0` optional `requires_adjudication` marks high-stakes emits as candidate outputs; `1c001e4` documents the adjudication contract field. Verification: ThreadKeeper evidence inspection, `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, focused mock pytest (`47 passed`), checker `py_compile`, and GGB sibling-fixture checker across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gates all passed. No live OmegaClaw/Telegram/runtime integration or security/access change was made.
- [x] 2026-07-03: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `09899a0` (`Add optional adjudicator gate for high-stakes subagent outputs`): JSON/persona task contracts may now set boolean `requires_adjudication`; when true, the subagent runs its normal loop but the final `emit` is treated as a candidate output. The transcript records `status=adjudication_required` with `candidate_summary`, and the structured parent digest returns `status=needs_adjudication` with bounded `adjudication` metadata (`required`, `status`, `candidate_summary`). No second LLM call is made inside the dispatch loop—the parent/supervisor must route the candidate to an adjudicator before accepting it. Pushed follow-up `1c001e4` to document the new field in `docs/reference-skills-subagent.md`. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`47 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.
- [x] 2026-07-03: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `a33b1e3` (`Add queue-only subagent dispatch mode`): optional `OMEGACLAW_SUBAGENT_QUEUE_ONLY=1` now validates a dispatch and persists a durable `OMEGACLAW_SUBAGENT_RUN_DIR/queue/*.json` task record without initializing or calling the worker LLM; parent digests include `status=queued`, `queue_path`, and `queue_sha256`, while full transcripts/index entries remain local. Queue capacity is bounded by `OMEGACLAW_SUBAGENT_MAX_QUEUED_DISPATCHES`; full queues fail closed as `queue_backpressure`, and cancellation is checked before enqueue. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`45 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.
- [x] 2026-07-03: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `f77ac1b` (`Add subagent patch proposal mode`): JSON task contracts may set boolean `patch_proposal_only`; subagent `write-file`/`append-file` calls then record full proposed changes in the local transcript without mutating workspace files, and the structured parent digest includes bounded `{action,path}` proposal metadata for review/test/apply by the parent. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest (`43 passed`). No paid compute, runtime/Telegram, secrets/access/security settings, force-push, merge, or remote-ref deletion.
- [x] 2026-07-03: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `d0c887d` (`Hash-chain subagent run index`): compact `index.jsonl` subagent run records now carry `previous_entry_sha256` and `entry_sha256`, preserving locked append behavior while making truncation/reordering/rewrite drift cheap to detect from the audit listing. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, focused mock pytest (`41 passed`), and refreshed GGB sibling-fixture checker across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gates. No live OmegaClaw/Telegram/runtime integration or security/access change was made.
- [x] 2026-07-03: Refreshed the GGB roadmap plus ThreadKeeper hardening gate fixture for Phase 3 audit/accounting evidence at ThreadKeeper head `554fb85`: dispatch wall-clock timeout and worker token accounting are now mapped into capacities 3.2, 3.5, and 5.2. Verification: ThreadKeeper branch/evidence inspection, `git diff --check`, `py_compile`, focused mock pytest (`40 passed`), and GGB sibling-fixture checker across ThreadKeeper, `petta-memory`, `petta-chem`, and GoalChainer gates all passed. No live OmegaClaw/Telegram/runtime integration or security/access change was made.
- [x] 2026-07-02: Added `.metta` sibling fixture files for the non-live GoalChainer incident harness gate (`CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`) under `artifacts/ggb-capacity-gates/20260702-goalchainer-incident-harness/`. The GGB fixture checker now passes on four gate fixtures: GoalChainer, `petta-chem`, ThreadKeeper, and `petta-memory`. Verification: checker/harness `py_compile` and multi-gate `local/check-ggb-gate-fixtures.py` passed. No live GoalChainer/OmegaClaw/Telegram integration or behavior change was made.
- [x] 2026-07-02: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `f880c50` (`Bound subagent read-file output`): subagent `read-file` now reads at most `OMEGACLAW_SUBAGENT_MAX_READ_FILE_CHARS + 1` characters (default 20000) and returns an explicit truncation marker, preventing arbitrarily large file reads from bloating worker context/tool results. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest from `projects/omegaclaw/local/threadkeeper-pytest-venv` (`38 passed`).
- [x] 2026-07-02: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `94d57c9` (`Cap subagent tool calls per turn`): subagent tool execution now has a defensively parsed per-response cap (`OMEGACLAW_SUBAGENT_MAX_TOOL_CALLS_PER_TURN`, default 3), returning structured `TURN_QUOTA_EXCEEDED` and persisting transcript status `turn_quota_exceeded` before executing extra parsed calls from one worker response. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest from `projects/omegaclaw/local/threadkeeper-pytest-venv` (`37 passed`).
- [x] 2026-07-02: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `b828ebf` (`Scrub subagent shell environment`): the optional subagent `shell` tool now launches allowlisted argv-list subprocesses with a minimal non-secret environment rather than inheriting the parent agent env, keeping sanitized `PATH`, workspace-pinned `HOME`, and locale/timezone only. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest from `projects/omegaclaw/local/threadkeeper-pytest-venv` (`36 passed`).
- [x] 2026-07-02: Built non-live GoalChainer incident harness `local/run-goalchainer-incident-harness.py` and archived gate `artifacts/ggb-capacity-gates/20260702-goalchainer-incident-harness/RUN.md` plus `report.json`. The bounded report recommends `publish_redacted_summary`; uses explicit PeTTa/SWI paths; bypasses known PeTTaChainer compile/add failure with a documented heuristic acceptability projection; confirms relation-level Prolog directive mapping (`obligated -> ready`); and records remaining runtime seams: local `derive_deontic` returned unregulated statuses and generated `lib_directive` plan status/next/claim stayed empty/erroring. Verification: harness `py_compile` and harness run passed. No OmegaClaw/Telegram runtime integration or behavior change.

- [x] 2026-07-02: GoalChainer intake completed: cloned/inspected MesTTo `OmegaClaw-GoalChainer` at commit `23f49515b1556ce04981f74bde4b56ee0a4375c6`, wrote `GOALCHAINER_INTEGRATION_MAP.md`, and archived `artifacts/ggb-capacity-gates/20260702-goalchainer-intake/RUN.md`. Verification: Python source compile passed; pytest diagnostics showed `22 passed, 8 skipped, 11 failed` without runtime env, `25 passed, 6 skipped, 10 failed` with local PeTTa/SWI, and `25 passed, 6 skipped, 10 failed` with local PeTTa/SWI plus local PeTTaChainer, where the evidence path hits a PeTTaChainer `compileadd` 8 GB stack-limit failure. No live OmegaClaw/Telegram integration or runtime behavior change was made.
- [x] 2026-07-02: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `01fe0d8` (`Sanitize subagent shell PATH`): the optional subagent `shell` tool now sanitizes inherited `PATH` before argv-list subprocess launch, removing empty/`.` entries and workspace-contained path entries so an allowlisted command name cannot be hijacked by a workspace-controlled executable after `cwd` is pinned to `OMEGACLAW_SUBAGENT_WORKSPACE`. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest from `projects/omegaclaw/local/threadkeeper-pytest-venv` (`35 passed`).
- [x] 2026-07-02: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `893a0e3` (`Run subagent shell commands in workspace`): the optional subagent `shell` tool now keeps disabled-by-default + executable allowlist + argv-list execution, but also runs with `cwd` fixed to `OMEGACLAW_SUBAGENT_WORKSPACE`, closes stdin, and fails closed if the workspace is missing. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest from `projects/omegaclaw/local/threadkeeper-pytest-venv` (`33 passed`).
- [x] 2026-07-02: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `24bf6bf` (`Harden subagent numeric env parsing`): timeout/retry, quota, digest, contract, and validation env knobs now parse defensively with safe defaults/clamps so bad operator config does not crash import or disable guards. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest from `projects/omegaclaw/local/threadkeeper-pytest-venv` (`32 passed`); refreshed ThreadKeeper GGB roadmap/gate fixture evidence.
- [x] 2026-07-02: Refreshed `GGB_CAPACITIES_ROADMAP.md` plus the ThreadKeeper hardening gate fixture after latest related-project progress. ThreadKeeper gate now records branch head `c3e836b` and focused mock pytest evidence of 31 passing tests; memory roadmap now reflects local SWI/Janus/PeTTaChainer smoke/profiling progress, 67 `petta-memory` stdlib tests, and the current compile/add bottleneck next task. Verification: ThreadKeeper `git diff --check`, `py_compile`, focused pytest (`31 passed`), `petta-memory` unittest (`67 passed`), GGB fixture checker across all three sibling fixtures, checker `py_compile`, and whitespace scan on touched OmegaClaw files.
- [x] 2026-07-02: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `c3e836b` (`Fail closed on missing subagent cloud client`): OpenAI-compatible subagent providers now fail closed during setup when the local client/SDK cannot initialize, producing a structured `provider_invalid` transcript record without calling the worker LLM; native Ollama endpoints still avoid the OpenAI SDK. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest from `projects/omegaclaw/local/threadkeeper-pytest-venv` (`31 passed`).
- [x] 2026-07-02: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `d8b922f` (`Index subagent run records`): finished subagent transcripts now also append compact JSONL audit entries to `OMEGACLAW_SUBAGENT_RUN_DIR/index.jsonl`, guarded by an `fcntl` sidecar lock, carrying run id/status/timestamps/transcript path/transcript SHA-256 for cheap local listing without expanding parent context. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest from `projects/omegaclaw/local/threadkeeper-pytest-venv` (`30 passed`).
- [x] 2026-07-02: Added `.metta` sibling fixture files for the `20260701-petta-memory-omegaclaw-fixture` GGB gate under `artifacts/ggb-capacity-gates/20260701-petta-memory-omegaclaw-fixture/`: `CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`. Updated `local/check-ggb-gate-fixtures.py` to recognize both `## Checks run` and plain `## Checks` sections plus common code-block commands. Verification: checker passes on all three current sibling fixtures (`petta-chem`, ThreadKeeper, `petta-memory`), `python3 -m py_compile` passes for the checker, and `petta-memory` stdlib unittest passes locally (`64 passed`).
- [x] 2026-07-02: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `1d30b4b` (`Allow task contracts to narrow subagent tool quotas`): JSON/persona task contracts can now set strict non-negative `max_tool_calls`, which is validated before worker LLM calls, persisted in transcripts, shown in child prompts, and clamped to only narrow the global per-dispatch tool quota. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest from `projects/omegaclaw/local/threadkeeper-pytest-venv` (`30 passed`).
- [x] 2026-07-02: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `0d1d0af` (`Add subagent transcript checksums`): finished subagent transcript records now get a local `<transcript>.sha256` sidecar and the structured parent digest returns `transcript_sha256` for later audit verification. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and focused mock pytest from `projects/omegaclaw/local/threadkeeper-pytest-venv` (`28 passed`).
- [x] 2026-07-02: Added `.metta` sibling fixture files for the `20260701-threadkeeper-hardening` GGB gate under `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/`: `CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`. Verification: `local/check-ggb-gate-fixtures.py` passes on both the existing `petta-chem` fixture and the new ThreadKeeper fixture; ThreadKeeper focused mock pytest passes from `projects/omegaclaw/local/threadkeeper-pytest-venv` (`28 passed`).
- [x] 2026-07-02: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `f1a8a70` (`Sandbox subagent persona prompts`): persona prompt paths now resolve under `PERSONA_DIR` and fail closed on empty values, `..` escapes, symlink escapes, or absolute paths outside the persona directory before any worker LLM call, preserving SHA-256 prompt pinning for in-directory prompts. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct persona-prompt sandbox/structured transcript assertions passed. Follow-up commit `ca872e4` (`Skip Docker cleanup when unavailable in mock pytest gate`) makes Docker-dependent post-session cleanup skip cleanly on non-Docker hosts; pytest now runs from `projects/omegaclaw/local/threadkeeper-pytest-venv` and `python -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` passes 28 tests.
- [x] 2026-07-01: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `caf3f9b` (`Structure no-tool subagent setup errors`): dispatches with neither explicit tools nor a persona `default_tool_subset` now return the bounded JSON parent digest and persist a minimal transcript record with status `tool_subset_invalid`, without calling the worker LLM. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct no-tool-subset assertion replay passed; pytest remains blocked by missing local pytest.
- [x] 2026-07-01: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `970b519` (`Record subagent setup failures`): early setup/config failures, invalid task contracts, invalid tool subsets, persona prompt/hash failures, provider setup failures, and escalation-policy denials now use the same bounded JSON structured parent return shape and persist minimal transcript records with explicit statuses (`setup_error`, `contract_invalid`, `tool_subset_invalid`, `persona_prompt_invalid`, `provider_invalid`, `escalation_denied`). Updated focused tests and docs. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and targeted direct structured-error/transcript assertions passed; pytest remains blocked by missing local pytest.
- [x] 2026-07-01: ThreadKeeper branch `agent/threadkeeper-hardening-next` pushed commit `a4a9b87` (`Tighten subagent task contract validation`): normalized task contracts now persist `objective` in transcripts, bound objective length via `OMEGACLAW_SUBAGENT_MAX_CONTRACT_OBJECTIVE_CHARS`, and reject unsafe `forbidden_actions` identifiers before any worker LLM call. Updated focused tests and docs. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct contract-validation assertions passed; pytest remains blocked by missing local pytest.
- [x] 2026-07-01: ThreadKeeper local branch `agent/threadkeeper-hardening-next` commit `8b35a91` added a task-contract validation follow-up: normalized contracts now fail closed before worker LLM calls when `allowed_paths` escape the workspace, and contract list size/item length are bounded via `OMEGACLAW_SUBAGENT_MAX_CONTRACT_ITEMS` / `OMEGACLAW_SUBAGENT_MAX_CONTRACT_ITEM_CHARS`. Updated focused tests and docs. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct validation assertions passed; pytest remains blocked by missing local pytest.
- [x] 2026-07-01: ThreadKeeper local branch `agent/threadkeeper-hardening-next` commit `5f33c8b` added emit-protocol integrity and stricter tool-argument bounds: subagent dispatch now rejects mixed `(emit ...)` + tool-call or conflicting final responses with structured `EMIT_PROTOCOL_VIOLATION`, persists transcript status `emit_protocol_violation`, and bounds path/per-argument size via `OMEGACLAW_SUBAGENT_MAX_PATH_ARG_CHARS` / `OMEGACLAW_SUBAGENT_MAX_TOOL_ARG_CHARS`. Updated focused tests and docs. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct assertion replay passed; pytest remains blocked by missing local pytest.
- [x] 2026-07-01: Added offline smoke checker `local/check-ggb-gate-fixtures.py` for GGB gate `.metta` sibling fixtures and archived `artifacts/ggb-capacity-gates/20260702-ggb-fixture-smoke/RUN.md`. Verification passed on `20260701-petta-chem-run-contract`: all 5 required fixture files exist and have balanced text syntax, exactly one top-level `run-summary` is present, and 3 `RUN.md` checks are covered by 4 `ggb-check` atoms. `python3 -m py_compile` and trailing-whitespace scan passed. The second archived-gate application was completed on 2026-07-02 for `20260701-threadkeeper-hardening`.
- [x] 2026-07-01: Added `.metta` sibling fixture files for the `20260701-petta-chem-run-contract` GGB gate under `artifacts/ggb-capacity-gates/20260701-petta-chem-run-contract/`: `CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`. These follow the field mapping in `GGB_GATE_RUN_CONTRACT_MAPPING.md` and serialize the GGB gate metadata itself (not the chemistry experiment) as PeTTa-shaped atoms. Verification: required-files check passed (all 5 files present), exactly one top-level `run-summary` present, every `RUN.md` check has a corresponding `ggb-check` atom. Source evidence re-verified in `petta-chem` on `main` commit `f83cd62`: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, and `git diff --check` all passed.
- [x] 2026-07-01: Added GGB-to-PeTTa run-contract mapping artifact `GGB_GATE_RUN_CONTRACT_MAPPING.md` and archived gate `artifacts/ggb-capacity-gates/20260701-ggb-run-contract-mapping/RUN.md`. It maps `GGB_CAPACITY_GATE_TEMPLATE.md` fields to the `petta-chem` v0.1 `run-config`/`run-manifest`/`run-summary`/`run-record` pattern with GGB companion atoms for non-chemistry evidence. Verification: required source files/headings and roadmap reference checks passed; trailing-whitespace scan passed for touched OmegaClaw files. Next small task is an optional `.metta` sibling fixture for one archived GGB gate.
- [x] 2026-07-01: ThreadKeeper local branch `agent/threadkeeper-hardening-next` commit `34c96b4` strengthened file-write atomicity: subagent `write-file` and `append-file` now share a temp-file + fsync + `os.replace` helper and take a per-target `fcntl` lock while updating workspace files, closing the concurrent append lost-update race. Updated subagent reference docs for structured returns, transcripts, timeout/retry/backoff, quotas/cancellation, rate/concurrency guards, workspace sandbox, and escalation hash pin. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct multiprocessing concurrent-append assertion passed; pytest remains blocked by missing local pytest.
- [x] 2026-07-01: Archived follow-up GGB Bundle B gate for `petta-memory` OmegaClaw-style prompt/index context at `artifacts/ggb-capacity-gates/20260701-petta-memory-omegaclaw-fixture/RUN.md`. Added a non-live fixture and regression test that exercises `OmegaClawMemoryBridge.prompt_view_metta()` plus `MediumMemoryStore.index_view()` together under a bounded, read-only policy. Verification in `projects/petta-memory/repos/petta-memory`: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 45 tests; `git diff --check` passed.
- [x] 2026-07-01: ThreadKeeper pushed branch `agent/threadkeeper-hardening-next` commit `07c8742` added a cross-process per-endpoint worker LLM concurrency guard: `_call_with_retries` now reserves/releases in-flight slots through an `fcntl`-locked state file under `SUBAGENT_RUN_DIR`, defaults to `OMEGACLAW_SUBAGENT_MAX_CONCURRENT_LLM_CALLS=4`, prunes dead/stale owners, and returns structured `concurrency_limited` transcript status instead of piling up long worker calls. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct concurrency assertion replay passed; pytest remains blocked by missing local pytest.
- [x] 2026-07-01: ThreadKeeper local branch `agent/threadkeeper-hardening-next` commit `9b6439c` added a cross-process worker LLM calls/minute guard: `_call_with_retries` atomically reserves calls in a per-endpoint-label `fcntl`-locked state file under `SUBAGENT_RUN_DIR`, defaults to `OMEGACLAW_SUBAGENT_LLM_CALLS_PER_MINUTE=60`, and returns structured `rate_limited` transcript records instead of making extra worker calls when exhausted. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct rate-limit assertion replay passed; pytest remains blocked by missing local pytest.
- [x] 2026-07-01: ThreadKeeper local branch `agent/threadkeeper-hardening-next` commit `5fdd131` hardened committed persona scaffolding: example configs and README now use explicit `node_role`, explicit `endpoint_kind`, and `persona_sha256` prompt pins rather than relying on provider/model/base-url inference. Added a focused test that all committed `*.json.example` persona configs have valid metadata and prompt pins. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct persona-example metadata assertions passed; pytest remains blocked by missing local pytest.
- [x] 2026-07-01: Archived GGB Bundle C partial gate for `petta-chem` scientific run-contract reuse at `artifacts/ggb-capacity-gates/20260701-petta-chem-run-contract/RUN.md` and refreshed the roadmap. Verification in `projects/petta-chem/repos/petta-chem` on `main` commit `4a80388`: `scripts/run_exp02.sh`, `scripts/test_exp02_contract_files.sh`, and `git diff --check` passed. Next useful bridge is a thin mapping sketch from `GGB_CAPACITY_GATE_TEMPLATE.md` fields to PeTTa run-contract atoms.
- [x] 2026-07-01: ThreadKeeper local branch `agent/threadkeeper-hardening-next` commit `2fcb0ba` added persona integrity hardening: persona lookup keys must be simple identifiers, and persona configs can pin prompt files with optional `persona_sha256`; mismatches fail closed before worker LLM calls. Verification: `git diff --check`, `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py`, and direct persona-integrity assertions passed; pytest remains blocked by missing local pytest.
- [x] 2026-07-01: Archived GGB Bundle B partial gate for `petta-memory` bounded prompt/index/PLN views at `artifacts/ggb-capacity-gates/20260701-petta-memory-prompt-view/RUN.md` and updated the roadmap. Verification in `projects/petta-memory/repos/petta-memory`: `PYTHONPATH=src python3 -m unittest discover -s tests -v` passed 34 tests; `git diff --check` passed. Live OmegaClaw memory integration remains intentionally disabled.
- [x] 2026-07-01: ThreadKeeper local branch `agent/threadkeeper-hardening-next` commit `0b185a4` replaced fragile worker cloud/local and local-Ollama detection heuristics with explicit persona metadata: `node_role` is now required for budget classification, and `endpoint_kind`/provider metadata selects `ollama_native` vs OpenAI-compatible transport without inspecting base-url/model strings. Added focused tests. Verification: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed; direct metadata/dispatch assertions passed; pytest remains blocked by missing local pytest.
- [x] 2026-07-01: ThreadKeeper local branch `agent/threadkeeper-hardening-next` commit `f6df5ef` closed the remaining file-tool atomicity gap by making subagent `append-file` use temp-file + fsync + `os.replace`, matching `write-file`; added focused regression coverage. Verification: `python3 -m py_compile src/subagent.py Autotests/mock/test_subagent_hardening_mock.py` passed; direct append atomic assertion passed; pytest remains blocked by missing local pytest.
- [x] 2026-07-01: Updated the GGB roadmap artifact with concrete post-first-pass status: ThreadKeeper Bundle A is implemented locally on `agent/threadkeeper-hardening-next` and now has a partial gate record; `petta-memory` prompt/index/PLN promotion progress and `petta-chem` run-contract/exp02 progress are mapped into next gates. Added reusable `GGB_CAPACITY_GATE_TEMPLATE.md` and archived `artifacts/ggb-capacity-gates/20260701-threadkeeper-hardening/RUN.md`. Verification: ThreadKeeper `py_compile` passed; pytest remains blocked by missing local pytest.
- [x] 2026-06-30: Continued ThreadKeeper next-hardening branch after commit `f79891c`: added bounded subagent history digestion, JSON structured returns with `summary`/`files_changed`/`tests_run`/`uncertainty`/`next_action`/`transcript_path`, persistent local subagent run transcript records written atomically, per-dispatch tool-call quotas, file-based cancellation, and optional `escalation.metta` SHA-256 integrity pinning before cloud delegation. Added focused tests and direct assertion replay; `py_compile` passed, while `python3 -m pytest Autotests/mock/test_subagent_hardening_mock.py -q` is blocked by missing pytest.
- [x] 2026-06-30: Began ThreadKeeper next-hardening work on local branch `agent/threadkeeper-hardening-next` commit `f79891c` from PR #1 safety-floor head. Added configurable subagent LLM timeout/retry/backoff, atomic subagent `write-file`, strict tool argument validation, and focused tests. `py_compile` passed; pytest is unavailable in the base environment, so the test assertions were replayed directly and passed.
- [x] 2026-06-30: Created `projects/omegaclaw/GGB_CAPACITIES_ROADMAP.md`, a concise capacity-by-capacity roadmap for `@Protomegabot` upgrades. It coordinates against ThreadKeeper PR #1, `petta-memory`, and `petta-chem`; identifies first gate bundles for ThreadKeeper reliability/records, read-only memory prompt-view smoke, and scientific run-contract reuse; and leaves only topology/exact-label confirmation as Ben decisions.
- [x] 2026-06-28: Diagnosed and patched `@Protomegabot` deep-call stalls/crashes. Root causes: fixed OpenClaw Gateway `user` session had ballooned to about `998k/272k` tokens, old HTTP/subprocess timeouts were too short for slow GPT-5.5 calls, LLM backend failures were converted to silent empty output, and the Telegram supervisor's `set -e` made nonzero runner exits kill the supervisor. Fixes: enable per-call Gateway sessions, raise aligned HTTP/subprocess timeouts to 900s, return user-visible `(send ...)` diagnostics on backend failure/empty output, and make the supervisor restart after nonzero runner exits. Verified py_compile, shell syntax, failed-backend diagnostic smoke, healthy OpenClaw provider smoke, `openclaw status`, and active supervisor restart.
- [x] 2026-06-28: Added interface-level auto-ack for long/deep Telegram messages to `@Protomegabot`, because prompt-only acknowledgement was insufficient when OpenClaw returned an empty response to Ben’s 12:00 formalization request. Also raised default `maxOutputToken` to 2048. Verified py_compile, runner syntax, auto-ack smoke, and active supervisor restart.
- [x] 2026-06-28: Tuned ProtomegaTron conversational pragmatics after Ben noted a long/hard question got no quick acknowledgement. Added prompt instruction to send a brief ack before longer thinking and use `continue-thinking` when needed; raised default `maxOutputToken` from 128 to 512 for more substantive Telegram replies; restarted the supervised group run and verified active status.
- [x] 2026-06-28: Upgraded the runtime OmegaClaw Telegram adapter to ingest attachments: documents are downloaded to `/home/openclaw/tmp/omegaclaw-telegram-attachments`, text-like files are inserted into the inbound message with untrusted-content markers, and PDFs are converted with local `pdftotext` subject to byte/character caps. Added chunking for large extracted attachments: full text is saved as `.extracted.txt`, split into `.chunkNNN.txt` files, and the prompt receives a first-chunk preview plus chunk paths for `read-file`. Restarted the supervised group run and verified syntax, text extraction, PDF extraction, chunking, and active supervisor status.
- [x] 2026-06-27: Patched OmegaClaw response normalization to suppress exact `No response from OpenClaw.` outputs as no-ops, including raw plain text and `send` command forms; restarted the private Telegram supervisor and verified it is active without idle backend calls.
- [x] 2026-06-26: Created project notebook `projects/omegaclaw/`.
- [x] 2026-06-26: Cloned OmegaClaw-Core, PeTTa, and `petta_lib_chromadb` into project layout.
- [x] 2026-06-26: Built local SWI-Prolog 9.3.36 with required packages under `projects/omegaclaw/local/swipl-9.3.36`.
- [x] 2026-06-26: Created PeTTa venv and installed OmegaClaw Python dependencies.
- [x] 2026-06-26: Downloaded/load-tested local embedding model `intfloat/e5-large-v2`.
- [x] 2026-06-26: PeTTa fib smoke test passed.
- [x] 2026-06-26: OmegaClaw mock startup/loop smoke passed via `projects/omegaclaw/local/run-omegaclaw-mock.sh`.
- [x] 2026-06-26: Wrote `projects/omegaclaw/RUNBOOK.md` with layout, environment, checks, and known issues.
- [x] 2026-06-26: Enabled OpenClaw Gateway HTTP endpoints in config for `/v1/chat/completions` and `/v1/responses`; validation passed, but runtime application requires Gateway restart.
- [x] 2026-06-26: Confirmed OpenClaw Gateway HTTP endpoints active after restart; authenticated `/v1/chat/completions` tiny prompt returned `omega-ok`.
- [x] 2026-06-26: Added local `OpenClaw` provider and smoke wrapper; `projects/omegaclaw/experiments/20260627T063559Z-openclaw-proxy-smoke/` confirmed OmegaClaw can call OpenClaw Gateway (`HTTP/1.1 200 OK`) under mock channel/local embeddings, with expected timeout for the continuous loop.
- [x] 2026-06-26: Added local start/stop/status/log supervisor script `projects/omegaclaw/local/omegaclaw-openclaw-supervisor.sh`; syntax check passed and `status` currently reports inactive.
- [x] 2026-06-27: Saved separate OmegaClaw Telegram token to local secret env file with `0600` permissions, validated bot username `Protomegabot`, and started private Telegram supervisor allowlisted to Telegram user/chat `402314199`.
- [x] 2026-06-27: Reproduced and fixed Telegram polling DNS failure under Landlock by allowing read-only `/run/systemd/resolve`, added `TG_SKIP_INITIAL_OFFSET=true` support to preserve pending Telegram updates during diagnostics, and patched response normalization so natural-language replies to fresh human messages are wrapped as `send` commands.
- [x] 2026-06-27: Private/direct Telegram smoke succeeded: Benjamin reported receiving a reply from `@Protomegabot` / ProtomegaTron. Stopped the smoke supervisor afterward to avoid idle backend calls.
- [x] 2026-06-27: Diagnosed no-reply from `@protomegabot`: local supervisor inactive, no log, and no OmegaClaw Telegram token in local environment. Updated runner/supervisor/validator to auto-load `/home/openclaw/.openclaw/omegaclaw-telegram.env`; syntax checks passed and validator still correctly refuses without a token.
- [x] 2026-06-27: Patched local Telegram adapter with `TG_ALLOWED_USER_ID(S)` and `TG_PRIVATE_ONLY` guard; added private/direct Telegram runner, supervisor, and token validator. Local checks passed; start correctly refuses without a separate token.

## ProtomegaTron Hyperseed mandate follow-up

- [ ] Rotate the `@Protomegabot` BotFather token and update `/home/openclaw/.openclaw/omegaclaw-telegram.env`; a 2026-07-06 debug env inspection printed the token in tool output. Do not block current native smoke on this, but treat it as the next maintenance/security cleanup.
- [x] 2026-07-06: Implemented first PeTTa bounded higher-order specialization fix from Fable-reviewed proposal: failed-specialization memoization, variant-normalized keys, failed-cleanup via `forget_symbol`, conservative failed-memo invalidation, and four regression repros. PeTTa commit `4ce1d0e` pushed to `bgoertzel-sing/PeTTa:agent/specializer-failed-memo-fable`; draft upstream PR https://github.com/trueagi-io/PeTTa/pull/191 . Verification: specializer regression passed; PeTTa `test.sh` 144 examples OK; OmegaClaw deontic 10/10; OmegaClaw integration 7/7.
- [ ] Follow up on PeTTa specializer belt-and-braces hardening: counters, env-configured specialization budgets, function-level backoff, and library-level `NoSpecialize` annotation for known generic grounders/dispatchers.
- [ ] Decide stale-update policy for smoke tests. Use `TG_SKIP_INITIAL_OFFSET=false` for ordinary fresh tests so old pending messages are dropped; use `true` only when deliberately preserving pending updates for diagnostics.
- [x] Tune idle/no-input loop so OmegaClaw does not repeatedly call the OpenClaw backend while waiting for Telegram input. Patched `src/loop.metta` on 2026-06-27 and verified 0 backend calls during idle receive iterations after restart.
- [ ] Re-smoke `memory/prompt_OpenClaw.txt` after prompt calibration and stale-update handling.
- [ ] GGB Bundle B follow-up: choose/confirm/use PeTTaChainer for the first normalized `MM-PLN*` inference smoke once local SWI/Janus/`petta` availability is resolved, or draft the reviewed live OmegaClaw memory-integration boundary. The non-live OmegaClaw-style prompt/index fixture now passes with live OmegaClaw writes still disabled.
- [ ] Design shared Telegram group topology for Ben + ZeroBot + ProtomegaTron, including boundaries for who acts, who observes, and what gets formalized.

- [x] 2026-07-29: Implemented the separately bound, provider-free motivation
  score-policy v0.2 generator primitive gate without materializing its sealed
  dataset. Exact digest encoding, retained-word scan, four family transforms,
  duplicate rejection, deterministic replay, and bounded no-output exhaustion
  pass 7/7 checks plus Python compilation. Next: independent formula/vector
  review before any request to authorize 64/32 split materialization.

- [x] Monitor `@Protomegabot` stability after SWI/Janus segfault mitigation; 2026-06-27/28 fresh group pings verified full Telegram receive → OpenClaw subprocess → Telegram send path.
- [x] 2026-06-28: Replaced the very-short-term `maxNewInputLoops=1` cap with a code-level loop mitigation: after a completed OpenClaw turn, clear `&loops` so the runner does not blindly spend backend calls on repeated `DO NOT RE-SEND OR SPAM!` prompts. Restored runner default `maxNewInputLoops=50`; verified normal idle iterations advance without `CHARS_SENT`/OpenClaw subprocess calls.
- [x] 2026-06-28: Implemented explicit `continue-thinking` protocol for OmegaClaw continuation turns so multi-step thinking does not rely on blind anti-spam loop iterations. Remaining future work: richer scheduled/background job orchestration.

- [x] 2026-07-05: Synced ThreadKeeper `subagent.py` to latest head `c8a14e4` (graceful SIGTERM/SIGINT handling) in the OmegaClaw-Core runtime tree at `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core/src/subagent.py`. The prior copy was at `14ec2ee` and missing the signal-handler-based graceful shutdown. Verification: `python3 -m py_compile src/subagent.py src/threadkeeper_budget.py src/helper.py src/agentverse.py src/rag.py` OK; diff between ThreadKeeper and OmegaClaw-Core copies is now zero; ThreadKeeper focused mock pytest (`101 passed`); GGB sibling-fixture checker passes across all 5 gates including the new `20260705-threadkeeper-telegram-private-integration` gate. Created `.metta` sibling fixtures (`CONFIG.metta`, `MANIFEST.metta`, `EVENTS.metta`, `METRICS.metta`, `SUMMARY.metta`) for the Telegram-private integration gate. Updated `GGB_CAPACITIES_ROADMAP.md` to reflect head `c8a14e4`, 101 tests, SIGTERM/SIGINT handling, dispatch token budget cap, and the pending Telegram-private supervisor smoke. No paid compute, secrets/access/security settings, daemon/scheduler install, push/merge/force-push, or remote-ref deletion.
- [x] 2026-07-07: Fixed separate `@Protomegabot` Telegram/runtime loop bug in OmegaClaw-Core commit `c8ad2cd` (`Fix Telegram routing and compact skill feedback`) on branch `agent/telegram-runtime-mods-checkpoint`. Root fixes: source-chat binding for dequeued Telegram messages via `_active_chat_id`, no pre-ack rebinding of the active chat, and `compact_skill_results()` deduplication of repeated `COMMAND_RETURN` blocks before storing `LAST_SKILL_USE_RESULTS`, preventing stale skill-result replay/prompt ballooning. Focused regression coverage added in `Autotests/mock/test_runtime_feedback_and_telegram_routing.py`. Verification: `py_compile` for `src/helper.py` and `channels/telegram.py`; focused pytest `4 passed`; scoped `git diff --check` passed for patched files; live Telegram supervisor restarted and initialized with targets `-1003983157420,-5437945421,-5459676079`. Whole-worktree `git diff --check` remains blocked by pre-existing whitespace in `memory/history.metta`. Push note: commit was pushed to configured `fork` remote, but that remote is misconfigured to `bgoertzel-sing/ThreadKeeper`; direct push to canonical `asi-alliance/OmegaClaw-Core` failed with GitHub 403 for `bgoertzel-sing`, and `bgoertzel-sing/OmegaClaw-Core` does not yet exist.

- [x] 2026-07-12: ThreadKeeper technical-analysis argument validation. Branch `agent/threadkeeper-hardening-next` commit `35c0c98`. The provider-facing `technical-analysis` tool now requires a bounded 1-32 character market-symbol argument instead of accepting arbitrary free-form text. Pushed to `fork/agent/threadkeeper-hardening-next` and synced the nested OmegaClaw runtime source. Verification: `py_compile`, focused hardening pytest (`254 passed`), `git diff --check`, and runtime source `cmp`. No paid compute, live wiring, secrets/access/security changes, queue/provider activity, daemon/scheduler install, force-push, merge, or remote-ref deletion.
- [x] 2026-07-12: ThreadKeeper optional shell command argument cap. Branch `agent/threadkeeper-hardening-next` commit `76ec6b6`. The allowlisted argv-only `shell` tool now rejects command strings over dedicated `OMEGACLAW_SUBAGENT_MAX_SHELL_ARG_CHARS` (default 4096) before parsing or subprocess execution, retaining the broader tool-argument cap as a second ceiling. Pushed to `fork/agent/threadkeeper-hardening-next` and synced nested runtime source. Verification: PR #1 ancestry, compile, focused hardening pytest (`256 passed`), diff check, runtime source cmp. No live wiring, provider/queue activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.

- [x] 2026-07-12: ThreadKeeper unquoted trailing single-argument call hardening. Branch `agent/threadkeeper-hardening-next` commit `6a62c97`. Ambiguous same-line unquoted trailing calls now fail argument-count validation for all single-argument worker tools before execution; ordinary parenthesized prose remains accepted. Verification: compile, focused hardening pytest (`260 passed`), diff check, and nested runtime source cmp. No live wiring/provider/subprocess/queue activity, paid compute, secrets/access changes, merge, force-push, or remote-ref deletion.

- [x] 2026-07-12: Archived GGB gate `artifacts/ggb-capacity-gates/20260713-threadkeeper-unicode-control-arg-hardening/` for ThreadKeeper head `5624013`. The gate maps C1/Unicode line-separator/bidi-control rejection in file, query, and optional-shell arguments to capacities 1.3/3.2/4.5/5.2/5.3/5.4. Verification: PR #1 ancestry, source compile, focused hardening pytest (`265 passed`), diff check, and sibling-fixture checker. No live/runtime/provider/queue/subprocess activity, push, merge, or security change. Next: coordinate PR/update posture rather than continuing parser micro-gates absent a concrete failing fixture.

## ProtoMegaBot reliability repair (2026-07-12)

- [x] 2026-07-15: Machintel v2 Phase 1/early Phase 2 source implementation. OpenClaw commit `e54d3356` adds a typed bot-registry configuration, registry-derived v2 identity fields, mention-first conflict/reinforcement semantics, and `SUPPRESS` interception; focused classifier tests pass 9/9 and silent-token tests pass 60/60, with core type check passing. ProtoMegaBot2 canary commit `9a03011` adds the same v2 envelope/classification boundary, inspectable `src/governance/addressee.metta` relations, and a transport publish gate; focused provider-free tests pass 7/7 and Python compilation passes. No live restart or secret access occurred.
- [x] 2026-07-17: Broader ProtoMegaBot2/PeTTa mock-loop gate. The Python classifier/publish suite passed 7/7, then the pinned PeTTa runtime executed the candidate `addressee.metta` relations for five classifications and two reinforcement cases. The gate found a real overlapping fallback: `True True` yielded both `true` and `false`. Scoped correction replaces the generic fallback with three explicit non-reinforced cases; rerun passed all seven assertions with a harness that rejects PeTTa's otherwise-zero exit on failed assertions. Evidence: `projects/protomegabot2/experiments/20260718T053609Z-machintel-v2-petta-mock-loop/`. No live restart, Telegram, provider, or secret access.
- [ ] Deploy Machintel v2 to the live agents: announce the ProtoMegaBot restart to Ben, copy the reviewed source to the live checkout, restart/verify controlled Telegram behavior, and separately ask Ben to restart the OpenClaw gateway for `e54d3356`.

- [x] Convert direct evidence and GPT-5.6-sol recommendations into `PROTOMEGABOT_REPAIR_PLAN_20260712.md` with staged gates, rollback conditions, immutable-envelope routing, honest health semantics, and separate native-crash classification.
- [ ] Review/package the existing source-only P0 Telegram transport/bridge-ownership patch as one deployable and rollback-safe unit.
- [ ] Obtain explicit live-change approval, then stop the unhealthy generation, clean only verified project bridges, and start exactly one patched generation.
- [ ] Verify one owner/worker/owned bridge/global bridge, MTProto-only receive, no Bot API `getUpdates`, and mode-0600 lock/session files.
- [ ] Run fixed-response private-chat canary, then one bounded real-provider canary, with correlation and correct source-chat send.
- [ ] Replace ordinary reply routing through mutable `_active_chat_id` with immutable per-message envelopes and two-chat concurrency tests.
- [ ] Add signal-11 core/backtrace capture and independent exit-137/OOM/watchdog/operator classification before claiming native stability.

- [x] 2026-07-13: ThreadKeeper Unicode run-control path hardening. Branch `agent/threadkeeper-hardening-next` commit `6e0e49b`. Explicit queued-dispatch paths plus worker stop/queued-task cancellation paths now reject Unicode separators, bidi/unsafe invisible formatting characters, and lone surrogates before claim/rename, lock acquisition, token checks, or worker setup. Pushed to `fork/agent/threadkeeper-hardening-next` and synced nested runtime source. Verification: PR #1 ancestry, compile, focused control-path pytest (`4 passed`), focused hardening pytest (`268 passed`), diff check, runtime source cmp. No live wiring, provider/queue/subprocess activity, secrets/access changes, paid compute, merge, force-push, or remote-ref deletion.
- [x] 2026-07-15: ThreadKeeper closed-schema task contracts. Branch `agent/threadkeeper-hardening-next` commit `0fc6efb`, pushed normally to `fork/agent/threadkeeper-hardening-next`. Nested and persona task contracts now reject unknown or misspelled fields before worker setup instead of silently discarding them. Focused tests passed (`6 passed`); combined subagent/budget hardening tests passed (`315 passed`), with Python compilation, diff check, and PR #1 ancestry. No provider/live queue/runtime/Telegram activity, merge, force-push, or remote-ref deletion.
- [x] 2026-07-15: ThreadKeeper direct dispatch-limit validation. Branch `agent/threadkeeper-hardening-next` commit `6b71b45`, pushed normally to `fork/agent/threadkeeper-hardening-next`. Direct `max_turns`/`max_chars` now reject booleans, floats, malformed strings, and excessively long integer strings with a persistent `dispatch_args_invalid` record before persona/provider setup; bounded decimal integer strings remain compatible. Focused tests passed (`6 passed`); combined subagent/budget hardening tests passed (`320 passed`), with Python compilation, diff check, and current PR #1 ancestry. No paid compute, provider/live queue/runtime/Telegram activity, merge, force-push, or remote-ref deletion.
- [x] 2026-07-16: ThreadKeeper direct dispatch scalar validation. Branch `agent/threadkeeper-hardening-next` commit `ae99ed3`, pushed normally to `fork/agent/threadkeeper-hardening-next`. Direct dispatch now rejects non-string goals, persona keys, and explicit tool subsets plus blank goals with persistent `dispatch_args_invalid` records before setup; malformed values are neither stringified nor allowed to raise during `.strip()`. Focused scalar/limit tests passed (`9 passed`); combined subagent/budget hardening tests passed (`329 passed`), with Python compilation, diff check, and PR #1 ancestry. No paid compute, provider/live queue/runtime/Telegram activity, access/security change, merge, force-push, or remote-ref deletion.
- [x] 2026-07-16: ThreadKeeper persona-config control-text validation. Branch `agent/threadkeeper-hardening-next` commit `4528c41`, pushed normally to `fork/agent/threadkeeper-hardening-next`. Required persona scalars and optional `base_url` now reject Unicode separators, bidi/invisible formatting controls, ASCII controls, and lone surrogates before prompt/provider setup. Focused config tests passed (`11 passed`); combined subagent/budget hardening tests passed (`331 passed`), with Python compilation and diff check. No paid compute, provider/live queue/runtime/Telegram activity, access/security change, merge, force-push, or remote-ref deletion.

## OmegaClaw iterative-LLM task-series executor (Ben directive 2026-08-06 23:01 PDT)

Ben directive (verbatim): "WE NEED THE OMEGACLAW AGENTS TO BE ABLE TO LAUNCH PROCESSES TO ITERATIVELY INVOKE LLMS TO EXECUTE TASK SERIES".

- [x] Build `worker-executor` for OmegaClaw-Core: launches a bounded subprocess loop that iteratively invokes the configured LLM provider (OpenClaw route first) to execute a task series from an exact JSON directive plan, checkpointing through the existing persistent-worker adapter (`worker-create`/`worker-checkpoint`/`worker-control` lifecycle, immutable manifest, hash-chained events).
  - Delivered: `worker_executor.py` + MeTTa skills `worker-start` and `worker-executor-status` + provider-free fake-dispatch tests. ProtoMega commits `8505ba9`, `ff0a493`; ProtoCosmo2 commits `2ffd972`, `0315fc0`, `4cdefa9`, `d7f8e5d`.
  - Contract per worker manifest: explicit task list or plan-file path, max steps, max wall-clock, per-turn timeout, max tokens/cost cap, stop conditions, artifact root under the worker state dir, audit event per LLM turn (prompt hash, response hash, tokens, stop reason).
  - Acceptance test: provider-free run over a 3-task fixture plan completes all tasks with a verifiable hash-chained event log and checkpoints; a mid-series injected provider failure leaves the worker resumable from last checkpoint; exceeding max-steps halts with a typed `budget_exhausted` event.
  - Next command: create branch `agent/worker-executor` in `projects/omegaclaw/repos/PeTTa/repos/OmegaClaw-Core` and scaffold `src/worker_executor.py` against `Autotests/` fixtures.
  - Evidence: `projects/omegaclaw/experiments/20260807T062249Z-output-fixes-worker-executor/` (`34 passed`).

Related defects found during 2026-08-06 diagnosis (fix in same or sibling branch):
- [x] OmegaClaw `lib_llm_ext.OpenClawProvider._subprocess_call` suppresses OpenClaw failure-fallback boilerplate instead of relaying it to Telegram (`1286e9f`; provider-free regression passed).
- [x] ProtoMega's supervised runtime default is raised from 8192 to 32768 output tokens. Restart verification showed the live process running with `maxOutputToken=32768`; bounded iterative continuation is separately supplied by `worker-start`.
- [ ] Restore Protomega Telegram group ingress after the 2026-08-07 Bot API polling failure.
  - Deliverable: one authoritative live receive transport that ingests Ben's `@Protomegabot` group request and preserves reply routing to the source chat.
  - Acceptance test: the supervised runtime logs an addressed message from chat `-5437945421`, then Protomega posts a PDF document back to that chat.
  - Next command: switch the live deployment to the already-implemented owned MTProto bridge, restart through the supervisor, and verify one owner/worker/bridge topology before Ben retries.
  - Evidence path: `projects/omegaclaw/experiments/20260807T071447Z-protomega-telegram-ingress-repair/`.
- [ ] 2026-08-08: Deliver a sanitized ZIP snapshot of ZeroBot's current skill files for Ben's review and OmegaClaw portability analysis. Acceptance: archive contains an origin-preserving manifest and every active workspace/OpenClaw/Codex skill source, excludes caches and credentials, passes ZIP integrity plus secret-pattern scans, and is delivered through Telegram. Next command: inventory all configured skill roots. Evidence: `artifacts/skill-snapshots/20260808-zerobot-current-skills/`.
