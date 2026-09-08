# Decision Log

## D-20260814-protomega-plugin-path: Make migrated memory plugins explicit in staging launch paths

- Date: `2026-08-14`
- Status: `accepted production-free staging rule`
- Decision: A clean OmegaClaw runtime using the separately pinned
  `petta_lib_chromadb` checkout must include that exact copied checkout in its
  scrubbed Python module path. Do not infer availability from the current
  directory or a developer shell.
- Rationale: direct recall passed under an explicit module path while the
  continuous loop failed with `ModuleNotFoundError: lib_chromadb`. Adding only
  the disposable plugin path passed the two-process exact-recall gate.
- Boundary: this authorizes only credential-free isolated staging launch
  configuration. It does not authorize production stores, identities,
  Telegram, or cutover.
- Evidence:
  `experiments/20260814T173641Z-protomega-full-loop-instrumentation/RUN.md`.

## D-20260814-telegram-durable-ingest-ack: Acknowledge only with a durable local inbox

- Date: `2026-08-14`
- Status: `accepted by Ben; implemented production-free at b8c99e5`
- Decision: Do not advance the Telegram cursor merely because an update was
  returned by acquisition, and do not wait for full model/reply handling.
  Atomically persist the complete update and its inbox classification together
  with the advanced cursor. Resume unfinished local inbox work after restart;
  use event IDs and the delivery ledger to prevent duplicate dispatch.
- Rationale: raw-acquisition acknowledgement can silently lose a message if
  the process crashes before handling. Full-handling acknowledgement needlessly
  holds Telegram's cursor and invites refetch. Durable-ingest acknowledgement
  separates reliable intake from potentially long model processing.
- Boundary: this decision and its fixture implementation grant no real
  Telegram, credential, production identity, or cutover authority.
- Evidence: `experiments/20260814T170500Z-telegram-durable-ingest/`.

## D-20260814-review-independence-labels: Separate model diversity from constitutional independence

- Date: `2026-08-14`
- Status: `accepted; supersedes ambiguous current review labels`
- Decision: A review performed by a different model or subagent under the same
  OpenClaw agent/runtime control is **model-diverse internal adversarial
  review**, not a functionally independent review under Constitution Articles
  XIII--XIV. Reserve **functionally independent external review** for a
  separately controlled reviewer that can inspect evidence without depending
  on the proponent's framing and can block advancement through a separately
  controlled mechanism.
- Consequence: Existing Fable receipts remain useful scoped engineering
  evidence, but do not establish constitutional independent concurrence.
  Preserve historical experiment wording as provenance and append this
  superseding classification where those receipts affect current gates. No
  production or cutover authority follows from same-control review.
- Evidence: constitutional note received 2026-08-14 08:03 PDT;
  `docs/constitution/constitution_draft_0.7.md`, Articles XIII--XIV.

## D-20260814-addressed-routing-requires-core-envelope: Do not patch Telegram alone

- Date: `2026-08-14`
- Status: `accepted diagnosis; minimal production-free implementation reviewed`
- Decision: Unchanged pinned upstream cannot meet immutable private/group reply
  routing because its core transports only message text and Telegram delivery
  uses global destination state. Require the smallest explicit event-ID seam
  through receive, turn processing, and send; fail closed on missing/expired
  IDs. Do not implement a mutable last/current-chat adapter.
- Review correction: pinned Telegram drops non-bound origins; the misroute is a
  model of a hypothetical mutable-route shim, not observed pinned behavior.
  The seam must also preserve one event per receive, key novelty and send dedup
  by event ID, and authenticate per origin.
- Evidence: `experiments/20260814T123400Z-full-loop-addressed-concurrency/`.

Implementation review confirms the core object handoff and event-keyed send
primitive, but does not resolve routing authority. Do not treat an LLM-echoed
event ID as equivalent to loop-bound authority: persisted history can expose
still-pending IDs. Choose and test the pending-event/turn-binding model before
any concrete channel migration. The LLM action signature mismatch was a
critical blocker and is corrected in the isolated seam worktree.
The reviewed incomplete state is durably frozen as local unpushed commit
`6dbbbb3`; this commit is a checkpoint, not an accepted adapter or runtime.

### D1 routing-authority resolution before full-loop acceptance

Destination authority is loop/channel-bound; an LLM-emitted event ID is only a
selector. Channels mint opaque IDs at acquisition and resolve destinations
only from immutable acquisition-time envelopes. A selector is valid only for a
live, unfinalized event previously presented in the current agent session.
Unknown, empty, finalized, expired, foreign, or never-presented IDs must produce
a visible bounded failure with no default/fallback delivery. This permits the
frozen reverse-completion test while preventing model text from constructing or
altering transport destinations. The remaining possibility of selecting the
wrong still-live authorized conversation is an explicit risk to probe; future
adapters must enforce per-origin authorization and bounded retention before
Telegram work.

Strict current-turn-only authority is rejected for this gate because it cannot
satisfy the preregistered reverse-completion requirement. Per-origin auth,
route expiry/caps, proactive/wake sends, startup version delivery, and adapter
exactly-once acquisition are explicitly deferred design obligations, not
silently accepted behavior.

The complete generic production-free mock gate is accepted and frozen at local
unpushed commit `744a7c1`. Real-loop reverse routing, scoped invalid-selector
handling, controlled pending-route restart, history isolation, and zero
descendants passed model-diverse internal Fable review. This acceptance applies only to
the synthetic in-memory adapter. Any concrete transport requires a new phase
covering per-origin authorization, bounded/durable route state, startup and
proactive sends, and exactly-once acquisition before Telegram staging.

### Concrete Telegram-shaped phase boundary

The next authorized phase is schema-shaped and entirely in-process, not real
Telegram staging. Build a new event-native sibling channel; never wrap
upstream Telegram's global message/chat/outbox state. Its Bot-API-shaped
transport is an injected callable, while URL and socket creation actively fail
and Telegram/token/proxy environment fields are rejected. Persist only the
monotone acquisition cursor; pending in-memory routes intentionally become
stale across restart and fail visibly. Require per-chat/per-user allowlists,
ignore edits, hard-cap live routes, use single-attempt sends, and forbid
startup/proactive sends. Durable routes/outbox and real Telegram remain future
decisions.

Authorized route overflow must be checked before durable cursor advancement.
An update rejected for capacity remains unacknowledged and eligible for later
acquisition after capacity frees; silently dropping it is rejected. For the
fixture timeout seam, a reported timeout is an uncertain single-attempt outcome
because its daemon call may complete late. Never retry that event. This
ambiguity, per-chunk deadlines/partial delivery, and unbounded stalled threads
are accepted only as recorded synthetic limitations and must be redesigned
before any real transport phase.

## D-20260814-disposable-full-loop-fault-adapter: Keep failure injection staging-only

- Date: `2026-08-14`
- Status: `accepted for staging evidence only`
- Decision: Use a disposable Test-provider copy to prove bounded correlated
  error/stall behavior through the full loop. Do not port the injector into
  pinned source or production. Treat addressed concurrency as still open until
  a thin channel with immutable origin envelopes passes the full loop.
- Evidence: `experiments/20260814T121646Z-full-loop-provider-faults/`.

## D-20260814-protocosmo2-canonical-skill-bindings: Reference canonical KEEP skills

- Date: `2026-08-14`
- Status: `accepted for isolated staging`
- Decision: Bind the nine KEEP-classified skills by canonical workspace path
  and SHA-256. Do not copy stale snapshot versions or add a runtime loader.
  REIMPLEMENT items require separate thin specs/tests; DROP and excluded
  runtime components remain absent.
- Evidence: `experiments/20260814T120200Z-protocosmo2-skill-port-manifest/`.

## D-20260813-omegaclaw-clean-install-pivot: Rebuild upstream first; migrate assets by value

- Date: `2026-08-13`
- Status: `accepted; Ben-directed strategic pivot`
- Decision owner: Benjamin Goertzel
- Pivot evidence: `experiments/20260814T053851Z-clean-install-pivot/`

Stop the generalized Phase-0 privileged-inspector effort after its current
safe evidence checkpoint; retain its artifacts, but remove it from the repair
critical path. Build one clean, pinned current-upstream OmegaClaw runtime and
instantiate three isolated bot configurations from it. Prove ordinary private
conversation and lifecycle behavior before porting custom Telegram-group
behavior or skills.

Asset priority is asymmetric. Protomega's preserved pre-dysfunction Chroma
corpus is the highest-value recovery asset because it may contain accumulated
Hyperseed-oriented memories from processed texts. Test only disposable copies
against upstream, preserving the original byte-for-byte. ProtoCosmo2 has little
memory but a valuable curated skill assemblage; inventory and selectively port
those skills without copying coupled runtime machinery. Protomega2 is an
experimental/test identity and is rebuilt last with no assumption that its
state is valuable.

Default DROP remains the private-canary/deferred-job stack, synchronous
OpenClaw file bridge, phase5/phase6 case machinery, acceptance controller, and
bespoke nested supervisors. Fable reviews the clean-install/migration plan and
each production promotion boundary. Production identities remain stopped
until autonomous staging passes and Ben explicitly authorizes cutover.

The accepted non-Docker baseline uses only upstream runtime controls: Janus is
given the pinned venv and repository module paths explicitly, `silent` avoids
per-clause rendering, the Docker-path Landlock profile is disabled with the
documented empty configuration value, and numeric YAML defaults are retained
because upstream command-line parsing preserves numeric overrides as strings.
These settings are staging-only evidence, not production policy or cutover
approval. Cold startup exceeding 300 seconds remains a recorded limitation.

Pinned `petta_lib_chromadb` commit `2184848` under ChromaDB `1.5.9` directly
opens an ordinary disposable copy of the preserved Protomega store and exactly
recalls its known dimension-384 record by ID and stored-vector query, including
after a fresh-process restart. Therefore the smallest preservation decision is
direct attachment of a disposable/staging copy; do not design or execute a
one-way migration unless a later full-loop integration test exposes a concrete
incompatibility. The authoritative source remains never-attached and immutable.
Evidence: `experiments/20260814T111500Z-protomega-chroma-upstream-recall/`.

The later exact-document text-query probe is the concrete incompatibility
that activates the new-store-only migration contingency: upstream text
embeddings are 1024-dimensional while the preserved collection is
384-dimensional. Its first execution stopped before target creation because
the upstream-forced offline model was not cached; do not substitute a model or
enable an unrecorded download. Evidence:
`experiments/20260814T113500Z-protomega-text-embedding-compatibility/` and
`experiments/20260814T114759Z-protomega-reembedding/`.

## D-20260813-omegaclaw-review-model-provenance: Review identity must be proven from runtime metadata

- Date: `2026-08-13`
- Status: `accepted for recovery governance`
- Evidence:
  `experiments/20260814T025329Z-upstream-recovery-phase0-privileged-inspector-v6/`
  and
  `experiments/20260814T031631Z-upstream-recovery-phase0-secure-capture-v7/`

A reviewer label, prompt role, or requested model is not evidence that the
required independent model actually ran. Every phase review must record and
verify the session key/ID plus effective provider/model from runtime session
metadata. The v6 reviewer requested as Fable actually ran on
`openai/gpt-5.6-sol`; its useful NO-GO findings remain evidence, but it cannot
satisfy the mandated Fable gate. The repaired unbound reviewer route later
produced start and end reviews whose runtime metadata prove effective
provider/model `anthropic/claude-fable-5`; both identities and exact reports
are retained in the v7 ledger. Phase 0 still stays open because that end GO
applies only to unprivileged capture primitives, not an integrated inspector,
preservation fence, snapshot, Phase 1, or production.

The v6 candidate also remains permanently unexecuted because its reviewed
bytes and capture command have critical TOCTOU and output-clobber defects.
Neither human privilege authorization nor urgency would cure defective exact
bytes; a successor requires a fresh hash-bound review.

## D-20260813-omegaclaw-session-restart-fence: Fence live sessions, not only schedules

- Date: `2026-08-13`
- Status: `accepted for recovery Phase 0`
- Evidence:
  `experiments/20260814T015539Z-upstream-recovery-phase0-snapshot-v3/`

Disabling a legacy cron schedule is not sufficient production restart
fencing. Before Omega state preservation or staging begins, every scheduled,
queued, or already-running session capable of invoking a production launcher
must be proven terminal or mechanically denied production launch authority.
The fence must remain effective for the full capture/copy interval and must be
revalidated afterward.

This decision follows a direct counterexample: an already-running execution of
the disabled Chroma-repair cron started all three production private-canary
receivers after the replacement recovery job took ownership. Production
transport state changed during that interval. The current bytes must be
preserved; no rollback or inferred reconstruction is authorized. Snapshot v3
is NO-GO and unexecuted.

Fence-v4 and the v5 exact-inventory recheck establish that observation alone
cannot close this invariant in the current sandbox. User crontab/at contents
and ptrace-protected same-UID fd trees require a bounded read-only
administrator inspection. A temporary production-identity denial may be
considered only through the explicit exception protocol, with exact scope,
rollback, expiry, and independent review; it must not modify legacy worktrees
or imply snapshot/cutover approval. Evidence:
`experiments/20260814T023547Z-upstream-recovery-phase0-admin-exception-v5/`
and
`experiments/20260814T023748Z-upstream-recovery-phase0-live-stop-recheck-v5/`.

## D-20260806-protocosmo2-ambient-context: Observe all group traffic, respond only when addressed

- Date: `2026-08-06`
- Status: `accepted and active`
- Decision owner: Benjamin Goertzel
- Implementation: commit `4da168b`
- Evidence: `experiments/20260807T011248Z-protocosmo2-telegram-context-ingestion/`

Retain a bounded, durable, same-chat context window for all Telegram group
messages delivered to ProtoCosmo2, including bot-authored discussion and
bounded PDF/text extraction. Do not invoke the model or send output for
ambient traffic; include recent context only when a human mentions the bot or
replies to it, and label the entire context as external and untrusted. This
resolves the prior mismatch where Telegram privacy was disabled but the
transport discarded the surrounding discussion needed for awareness.
Relevant Research Rules: 2, 5, and 7.

## D-20260806-capacity-1-1-r4-v04: Accept empirical replay; keep harness closed

- Date: `2026-08-06`
- Status: `R4 empirical replay passed; R1/R2 required before harness adoption`
- Evidence:
  `artifacts/ggb-capacity-gates/20260806-request-to-contract-os-sandbox-v04-independent-replay/`

Accept the v0.4 generic-failure sandbox as the passing empirical R4 replay for
the frozen externally observable-effect contract. All twelve independently
replayed cases pass, cover E1--E6, and hide candidate-controlled stderr behind
the exact message `sandbox candidate failed`. Do not adopt the 26-case
generator harness yet: executable R1 cases and an independently committed R2
holdout are still missing. This decision grants no generator, integration,
dispatch, memory-write, provider, Telegram, or other runtime authority.

## D-20260806-capacity-1-1-r4-stderr: Keep R4 open after independent replay

- Date: `2026-08-06`
- Status: `revision required before harness adoption`
- Evidence:
  `artifacts/ggb-capacity-gates/20260806-request-to-contract-os-sandbox-v03-independent-replay/`

Do not adopt the OS sandbox into the generator-acceptance harness. The
independent twelve-case replay finds that `sandbox_gate.run_candidate()`
returns bounded child stderr verbatim in `RuntimeError`; a private sentinel
therefore crosses the boundary despite E6. Preserve the existing no-effect
authority and revise the failure channel to a generic result before another
content-bound independent replay. This is not a network escape, and it grants
no generator or runtime authority.

## D-20260805-protocosmo2-persistent-worker-adapter: Adopt bounded state-only v1

- Date: `2026-08-05`
- Status: `accepted and integrated offline; no autonomous executor authorized`
- Decision owner: Benjamin Goertzel
- Implementation: OmegaClaw-Core commit `5c64918` on
  `agent/protocosmo2-phase6-live`
- Evidence:
  `experiments/20260805T160618Z-protocosmo2-persistent-worker-adapter-r6/`,
  `experiments/20260805T160646Z-protocosmo2-persistent-worker-adapter-core-load/`,
  and
  `experiments/20260805T160829Z-protocosmo2-persistent-worker-adapter-configured-smoke/`

Adopt the v1 OmegaClaw-native durable orchestration adapter. It exposes exact
JSON MeTTa skills for create, status, checkpoint, pause/resume/cancel, and
standing-approval checks. Manifests are immutable and digest-bound; events are
bounded, hash-chained, atomically appended, and projected through an explicit
state machine. Exact operator-installed approvals remain actionable across
activations until revoked, superseded, expired, completed, or exhausted.

The model-visible adapter cannot install/change/consume approvals, spawn an
agent or process, schedule itself, call providers, use Telegram or shell, or
perform remote compute. A later executor/consumption-receipt seam requires its
own specification and authorization. This boundary makes the improved policy
available to ProtoCosmo2 without silently granting the missing effects that
originally caused the skill to be classified as deferred.

Verification: 44 provider-free tests passed, the modified Core loaded through
pinned PeTTa and returned the exact deterministic answer, and the configured
mode-0700 state-root smoke failed closed canonically for an absent task.
Research Rules applied: 2, 5, and 7.


## D-20260804-protocosmo2-phase6: Begin bounded private Telegram canary

- Date: `2026-08-04`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related evidence: Protobots message 16261; runtime commit `bebe357`;
  `experiments/20260804T211817Z-protocosmo2-phase5-retrieval-repair/`

### Decision

Accept Phase 5's G5/go-no-go gate and proceed to Phase 6. Start with a distinct
ProtoCosmo2 private Telegram canary bound to Ben, with bounded outbound traffic,
no autonomous schedules, no state-changing extras, and no group enrollment
until the private-canary evidence is reviewed.

### Rationale and consequences

The pinned runtime completed the unchanged ten-case suite 10/10, all seven
critical cases met frozen intent, and no crash or outbound delivery occurred.
Ben then explicitly instructed the project to move to Phase 6. Relevant rules:
2 (routed-system invariants), 5 (reproducible evidence), and 7 (transport
seams). Live sending still requires a dedicated ProtoCosmo2 identity/config;
existing bot credentials must not be reused. The canary must preserve hashes,
incidents, latency/cost evidence, and a separate go/no-go before group use.


## D-20260717-protomega-overload-routing: Keep overload internal and Fable opt-in

- Date: `2026-07-17`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related commits: `fb36d35`, `a9c0060`, `74e46d2`

### Decision

Group traffic authored by another bot, or explicitly addressed only to another
bot, is dropped before OmegaClaw enqueue unless ProtoMegaBot is explicitly
mentioned. HTTP 429/502/503/504 overload is logged locally, places the failing
route on a five-minute cooldown, and may try exactly one automatic fallback:
`openclaw/protomegabot-simple`. Fable is never automatic and requires an
explicit operator choice.

### Rationale

The prior context-only enqueue depended on a later mutable skip flag and still
incurred triage/model calls. A failed Opus continuation then serialized its
traceback as Telegram content, multiplying one upstream outage into repeated
channel spam. The earliest reliable boundary is Telegram ingress; overload
belongs inside provider routing rather than chat output. Longer timeouts cannot
repair explicit upstream 503 responses, and automatic Fable routing hides the
outage at high cost. Relevant research rules: Rule 2 (stateful routing
invariants) and Rule 7 (separate ingress and provider-routing seams).

### Evidence

`docs/protomegabot-overload-control-20260717.md`; 4 overload-policy tests;
8 address/ingress tests; compilation, shell syntax, and diff checks passed.

## D-20260714-protomega-action-envelope: Make replies explicit and fail closed

- Date: `2026-07-14`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `docs/protomega-output-pipeline-hardening.md`; isolated commit `a16e714`

### Context

ProtoMegaBot generated substantive prose for a human Telegram message but mixed it
with parenthesized internal actions. A permissive repair/evaluation path executed
three valid `pin` forms, discarded the prose, and delivered no reply. The prompt,
parser, and executor described incompatible output syntaxes, while raw history
strongly primed MeTTa-shaped output.

### Decision

Prefer a versioned JSON envelope (`omegaclaw.action.v1`) with a first-class
`reply` and separately validated `actions`. Keep legacy S-expressions only as a
strict compatibility grammar. Validate the complete batch before any action,
allow at most one bounded formatting repair, treat history/runtime feedback as
untrusted context, and emit a fixed visible diagnostic whenever a fresh human
message requires a reply but the output contains none. Raw model output must not
reach permissive `sread`/evaluation paths.

### Alternatives considered

- Keep the permissive S-expression repair path and strengthen the prompt only.
- Convert arbitrary nonempty prose directly into a Telegram send even when it
  resembles malformed tool syntax.
- Remove all legacy output compatibility immediately.

### Rationale and evidence

The selected contract makes delivery intent explicit, prevents partial side
effects, and provides a staged migration path. Focused tests cover JSON and
legacy acceptance, unknown/mixed-form rejection, missing-reply repair/fallback,
context separation, message correlation, dedup-after-success, and chunk retry.
All 31 focused test bodies passed; helper assertions, Python compilation, and
MeTTa parsing also passed.

### Consequences

Malformed or ambiguous output now fails visibly instead of being partially
executed or silently lost. The live runtime carries the hardening, while the
coherent implementation remains reviewable in isolated commit `a16e714`.
Durable inbound journaling and crash-persistent delivery receipts remain future
work; current partial-chunk retry state is process-local.

### Revisit trigger

Revisit after structured envelopes have soaked in live use, before removing the
legacy grammar, or if a human Telegram message can again be acknowledged without
a corresponding reply or visible failure.

### Supersedes or superseded by

Supersedes the implicit permissive model-output/eval contract.

## D-20260704-threadkeeper-async-worker-loop: Add supervised real async worker loop

- Date: `2026-07-04`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `projects/omegaclaw/repos/ThreadKeeper` commit `cc3cd1e` (`Add bounded queued worker loop`) on branch `agent/threadkeeper-hardening-next`; Telegram instruction from Ben: "We definitely want a real async worker loop".

### Context

ThreadKeeper Phase 3 already had queue-only dispatch, atomic queued-worker claim/finish, bounded manual drain, checksum sidecars, strict queued-task validation, cancellation preservation, patch-proposal mode, adjudication-required mode, persistent transcripts, and hash-chain audit. The remaining design question was whether to stop at operator-supervised bounded drains or add a real polling worker loop.

### Decision

Add a real async worker-loop primitive, but keep it explicitly supervised: it must be launched by an operator/supervisor, not self-started from parent `dispatch`.

### Alternatives considered

- Keep only `run_queued_dispatch(queue_path)` and `drain_queued_dispatches(max_tasks=...)` until after live @Protomegabot smoke.
- Add an unbounded daemon/self-scheduling loop immediately.

### Rationale and evidence

Ben explicitly preferred the real async worker loop. The implemented compromise, `subagent.run_queued_worker_loop(...)`, repeatedly polls and claims queued records, but exits on explicit bounds (`max_tasks`, `max_idle_polls`, `max_runtime_s`, or `stop_file`) and uses a best-effort local lock to prevent two local worker loops draining the same queue concurrently. Focused mock tests cover multi-task drain-to-idle, stop-file preservation before worker LLM calls, and concurrent-loop rejection. Verification: `git diff --check`, Python compile, and focused mock pytest (`71 passed`).

### Consequences

ThreadKeeper is closer to staged @Protomegabot pilot use, but the loop still needs a local install/smoke under @Protomegabot config before any live group/channel use. Defaults and supervisor wrapper policy should stay conservative.

### Revisit trigger

Revisit after the first @Protomegabot-config local smoke and controlled private/group smoke, or if the worker loop shows queue starvation, duplicate claims, runaway cost, stop-file failure, or audit gaps.

### Supersedes or superseded by

Supersedes the earlier Phase 3 "only add a live async worker loop if/when Ben explicitly wants supervised live dispatch" open question.

## D-20260705-threadkeeper-smoke-gates: ThreadKeeper supervisor/provider and private OpenClaw smoke

- Date: `2026-07-05`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `artifacts/ggb-capacity-gates/20260705-threadkeeper-worker-supervisor-provider-smoke/` and `artifacts/ggb-capacity-gates/20260705-threadkeeper-private-openclaw-smoke/`

### Context

ThreadKeeper branch `agent/threadkeeper-hardening-next` at commit `85145ea` has 82 passing focused mock tests and has progressed through supervisor-boundary, cancellation, env-file, and config smokes. Ben approved the ThreadKeeper smoke in Protobots message 2724 at 2026-07-05 08:48 PDT.

### Decision

Run two controlled non-live smokes: (1) a supervisor/provider-boundary smoke with a local fake Ollama endpoint to exercise the full worker→provider call path without external dependencies, and (2) a private/non-group OpenClaw smoke using the real local OpenClaw Gateway to exercise a genuine worker LLM call with `needs_adjudication` task-contract mode.

### Alternatives considered

- Skip the fake-provider smoke and go directly to live OpenClaw Gateway.
- Skip the private OpenClaw smoke and go directly to Telegram-private integration.

### Rationale and evidence

Both smokes passed. The fake-provider smoke verified the supervisor launches, the worker claims/calls/writes/exits cleanly, and exactly one provider call was made. The private OpenClaw smoke verified a real local Gateway `/v1/chat/completions` call returned HTTP 200, the worker used 16,756 tokens, and the task returned `needs_adjudication` as intended. No Telegram, external provider, secrets, paid compute, daemon, or scheduler was involved.

### Consequences

The next staged gate should adjudicate the private OpenClaw smoke candidate output, then consider staged Telegram-private integration with explicit stop conditions. Alternatively, run a multi-task or multi-persona supervisor smoke.

### Revisit trigger

Revisit if adjudication reveals worker output quality issues, if the Gateway call pattern changes, or before any Telegram-private or group integration.

### Supersedes or superseded by

None.

## D-20260715-bounded-communication-topology: Keep Telegram identity separate and direct bridging bounded

- Date: `2026-07-15`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related records: `docs/omegaclaw_zerobot_topology_decision_note.md`; `artifacts/ggb-capacity-gates/20260707-topology-boundary-review/`; queue/sidecar gates from 2026-07-07--09

### Decision

Keep ProtomegaTron as a distinct Telegram bot/account, using the local OpenClaw
Gateway as its model provider and explicit chat allowlists as routing boundaries.
Do not add an unrestricted direct OmegaClaw--ZeroBot session bridge. Cross-agent
work first uses authenticated/checksummed ThreadKeeper queue records, bounded
task contracts, read-only GoalChainer/`petta-memory` evidence, candidate-only
outputs, and explicit adjudication. Private Telegram canaries and broader group
behavior remain separately bounded gates.

### Rationale

This preserves visible identity/routing, limits recursive authority, and reuses
the already tested ThreadKeeper audit, quota, checksum, transcript, and
adjudication seams. It also avoids widening OpenClaw's tree-scoped session
visibility merely to make automation convenient.

### Consequences

The existing distinct allowlisted Telegram service may continue. Passing
offline queue/sidecar gates are evidence for the bounded path, not permission
for raw worker egress, memory writes, or silent cross-session actions. Any new
direct bridge must have its own contract, authentication, audit record, stop
conditions, and canary approval.

## D-<YYYYMMDD>-<short-slug>: <Decision title>

- Date: `<YYYY-MM-DD>`
- Status: `proposed | accepted | superseded | rejected`
- Decision owner: Benjamin Goertzel or delegated role
- Related task/run/commit: `<pointer>`

### Context

### Decision

### Alternatives considered

### Rationale and evidence

### Consequences

### Revisit trigger

### Supersedes or superseded by
# D-20260715-threadkeeper-persistent-workers: Make persistent workers a native ThreadKeeper delegation mode

- Date: `2026-07-15`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `worktrees/threadkeeper-persistent-workers/docs/persistent-workers.md`; branch `agent/threadkeeper-persistent-workers`, base `a2c62eb`

### Context

ThreadKeeper's existing `delegate` is a synchronous, bounded specialist call. Its hardened queue and supervised worker primitives provide much of the necessary effects substrate, but they do not yet constitute a durable, queryable persistent-subagent lifecycle. Ben explicitly requested that OmegaClaw persistent subagents evolve from ThreadKeeper rather than becoming a separate orchestration system.

### Decision

Add a distinct asynchronous persistent-worker mode to ThreadKeeper. Reuse ThreadKeeper routing, personas, budget/escalation, accounting, task contracts, audit trail, and optional adjudication. Preserve bounded `delegate` behavior and tests. Put meaning-bearing lifecycle and governance policy in MeTTa where feasible and keep Python responsible for process/session/storage effects. Require durable identity, state/checkpoints, restart recovery, status/progress, cancellation, scoped permissions, model/resource budgets, inbox/result delivery, and failure/audit records.

### Alternatives considered

- Create a separate persistent-subagent orchestration stack.
- Remove or greatly increase `delegate`'s eight-turn cap.
- Deploy experimental persistence directly into ProtoMegaBot.

### Rationale and evidence

ThreadKeeper already has validated queue-only dispatch, atomic claim/retention, bounded supervised drains, cancellation controls, task contracts, quotas, transcripts, checksum/hash-chain audit, and adjudication primitives. Extending those seams avoids duplicated authorities. Persistence has lifecycle and recovery semantics that a larger turn cap cannot supply. Production ProtoMegaBot is useful and stateful, so live validation belongs in isolated ProtoMegaBot2 after provider-free gates pass.

### Consequences

ThreadKeeper will expose two clearly separated delegation modes. Persistent tasks need versioned state, attempts, leases, checkpoints, monotone budgets, idempotent inbox/results, and recovery tests. ProtoMegaBot production paths/processes/credentials remain out of bounds. No paid compute or provider calls are authorized by this decision.

### Revisit trigger

Revisit before enabling external-effect tools, recursive delegation, live Telegram/provider access, or deployment outside ProtoMegaBot2; also revisit if MeTTa transition parity cannot be made fail-closed.

### Supersedes or superseded by

None.
# 2026-07-15 - Keep Phase 1 transport mechanics Telegram-owned and routing facts generic

For the chat-room identity/routing design, Telegram entity/reply extraction and deterministic addressee classification live in the Telegram plugin. Generic OpenClaw message context carries the resulting `InboundEnvelope`, `SelfContext`, and classification into structured user-role context; the resolved agent workspace is added only at agent-run assembly, where it is authoritative. Phase 1 classifies `INCIDENTAL` but does not reject it before generation: Ben's v2 always-attending contract requires a model turn for every room message, while role-aware incidental pre-filtering is deferred to Phase 4. Phase 1 does not invent the Phase 2 `SUPPRESS` control result, so `DIRECT`, `SECONDARY`, `GROUP`, and `INCIDENTAL` currently rely on the existing room-event/visible-reply policy plus explicit structured classification. This preserves the plugin boundary and avoids coupling transport parsing to core.

Evidence: OpenClaw branch `agent/chat-room-identity-phase1`, implementation commit `4c8cc1f5` plus review corrections `4d234b80` and `2e0ed9e0`, based on `v2026.7.1` (`2d2ddc43`). The corrections make explicit mentions authoritative when mention and reply context disagree and preserve always-attending model turns for incidental messages. Relevant research rules: Rule 2 (explicit routed-system invariants) and Rule 7 (modular abstraction seams).

# 2026-07-15 - Registry is authoritative and always-attending is distinct from speaking

The Revision-2 bot registry, not Telegram's per-update `is_bot` flag or prose, is authoritative for bot identity in both tracks. Explicit mentions outrank reply ancestry and agreeing mention/reply signals are recorded as reinforced. ProtoCosmoBot and ProtoMegaBot default to `always-attending`: incidental classification is visible to policy but does not skip the full turn; publishing remains separately controlled. `SUPPRESS` and legacy bare `NO_REPLY` are intercepted at the transport boundary, and acknowledgement-only or silence-explanation output is rejected. Evidence: OpenClaw `e54d3356`; ProtoMegaBot2 `9a03011`; experiments `20260715T174019Z-machintel-v2-openclaw-phase1-phase2` and `20260715T174019Z-machintel-v2-protomegabot2-canary`. Rules 2, 5, and 7 apply.

# D-20260717-threadkeeper-formal-handoffs: Make resume state a first-class ThreadKeeper artifact

- Date: `2026-07-17`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `worktrees/threadkeeper-persistent-workers/docs/persistent-workers.md`; `b6be4ea`; `experiments/20260717T154004Z-threadkeeper-formal-handoff-v1/`; Ben's Protobots directive that the formal handoff mechanism should be incorporated into ThreadKeeper

### Context

ThreadKeeper already persisted immutable manifests, events, attempts,
checkpoints, receipts, budgets, inbox items, results, and checkpoint payloads
used as bounded resume context. Those primitives preserved machine state but did
not require or expose a standardized human-readable record of role, hazards,
constraints, exact pickup point, and provenance. Isolated cron workers therefore
reconstructed state from broad project files and prompts rather than consuming a
single formal handoff artifact.

### Decision

Formal resume/handoff state is a native ThreadKeeper persistent-worker artifact,
implemented as a strict versioned snapshot inside the existing immutable,
hash-linked checkpoint chain. It is selected from verified checkpoint lineage
and bound to the task manifest, attempt, checkpoint, and its own content digest.
It records role, observed model identity, state summary, exact pickup point,
constraints, hazards, completed work, next steps, blockers, and evidence
references. It is evidence and continuation context, never authorization.

### Alternatives considered

- Maintain one mutable `CURRENT_HANDOFF.md` per worker.
- Keep arbitrary opaque checkpoint payloads and rely on prompt conventions.
- Build a second resume store outside ThreadKeeper.

### Rationale and evidence

Using the checkpoint chain reuses ThreadKeeper's established atomicity,
integrity, lineage, idempotency, recovery, and authorization boundaries. An
immutable sequence avoids pointer drift and preserves every superseded handoff.
A strict human-readable schema prevents opaque cursors from masquerading as a
complete resume record. Focused provider-free tests cover hash-bound creation,
restart resume exposure, and rejection before write on schema ambiguity.
Relevant Research Rules: 2 (specify stateful invariants first) and 7 (reuse a
modular effects seam rather than create a parallel authority).

### Consequences

ThreadKeeper can now carry the structured resume protocol described in the
multi-agent swarm guide without weakening current task contracts or budgets.
Existing generic checkpoints remain compatible. The next integration step is
to make persistent workers write handoffs at meaningful pause/requeue boundaries
and prove full process-death reconstruction from durable state.

### Revisit trigger

Revisit before making handoffs mandatory for all checkpoints, exposing them to
live ProtoMegaBot/Telegram paths, or allowing handoff content to influence
authorization or policy decisions.

### Supersedes or superseded by

Extends `D-20260715-threadkeeper-persistent-workers`; supersedes no existing
decision.

# D-20260729-protomegabot2-staging-approval: Approve staging without credential rotation

- Date: `2026-07-29`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related task/run/commit: `TASKS.md` ProtoMegaBot2 staging task; staging run record pending

### Context

Daily status messaging incorrectly retained rotated-credential attestation as
a prerequisite for ProtoMegaBot2 staging, although the existing local
credential configuration is already the intended staging substrate.

### Decision

Ben approves ProtoMegaBot2 staging and withdraws the token-rotation and
rotated-credential-attestation prerequisites. Use the existing local
credential configuration. Do not read, reveal, copy, log, rotate, or otherwise
alter that credential as part of the staging work.

### Consequences

The next authorized action is bounded staging preflight/launch with a visible
health record and rollback path. This authorization does not approve production
deployment, broader access, credential changes, or removal of other runtime
safety gates.

### Revisit trigger

Revisit on a staging failure, evidence of credential exposure, or before any
production rollout.
## 2026-07-22 - Audited relative paths use one canonical spelling

- Decision: require accepted ThreadKeeper file-tool paths and task-contract
  path prefixes to equal their platform-normalized relative spelling.
- Rationale: audit and authorization records must identify the exact path
  spelling consumed by filesystem helpers; redundant dot components,
  separators, or trailing separators create avoidable ambiguity.
- Scope: bounded synchronous ThreadKeeper hardening only; file contents and
  valid normalized relative paths are unchanged.

# D-20260802-protocosmo2-phase0-phase1: Freeze a sanitized snapshot before any target runtime

- Date: `2026-08-02`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related evidence: `docs/protocosmo2-phase0-freeze-2026-08-02.md`;
  `experiments/20260803T045142Z-protocosmo2-phase1-sanitized-snapshot-rerun/`

### Decision

Execute only Phase 0 and Phase 1 of the ProtoCosmo2 migration first: pin a
candidate baseline, capture an explicit allowlisted read-only source snapshot,
and validate its manifest. Do not provision or run ProtoCosmo2 yet.

### Rationale and consequences

The source environment contains durable research records alongside live
OpenClaw state and unrelated artifacts. A content-addressed snapshot preserves
provenance while preventing raw session, credential, runtime, and cache copies.
The first audited attempt failed closed on overly broad path logic and a
symlink; the refined policy captures the intended 639 files with documented
exclusions. The next step is a clean detached, mock-only target checkout.
Telegram, provider credentials, network listeners, writable shared memory,
ThreadKeeper/GoalChainer activation, and cross-agent bridges remain separately
gated.

# D-20260805-protocosmo2-phase6-private-canary-closeout: Accept the bounded private canary; retain wider gates

- Date: `2026-08-05`
- Status: `accepted`
- Decision owner: Benjamin Goertzel (Phase-6 authorization); ZeroBot records acceptance evidence
- Related evidence: `experiments/20260805T235502Z-protocosmo2-phase6-acceptance-provider-free/`;
  `experiments/20260805T235543Z-protocosmo2-phase6-live-restart-recovery/`

### Decision

Accept ProtoCosmo2 Phase 6 only as a completed, stopped Ben-only private
Telegram canary. Do not treat this as authorization for group enrollment,
attachments, autonomous schedules, state-changing extras, or continuous
service operation.

### Evidence and rationale

Two fresh authorized DMs each produced one reply, while the durable state
recorded no pending transaction or incident. The focused contract/transport
suite passed 17/17, including duplicate, crash recovery, allowlist,
attachment, depth, and fixed-failure controls. A live controlled restart kept
the state SHA-256 unchanged, retained both committed deliveries and cursor
`387571971`, and made no new send; shutdown was clean.

### Revisit trigger

Require a separate Phase-7 decision and a new staged acceptance plan before
any group, wider-user, attachment, background, or executor capability.

# D-20260806-protocosmo2-universal-groups: Continuous operation in all Telegram groups

- Date: `2026-08-06`
- Status: `accepted`
- Decision owner: Benjamin Goertzel
- Related evidence: `experiments/20260806T224725Z-protocosmo2-universal-group-operation/`

### Decision

Authorize ProtoCosmo2 for continuous text operation in every Telegram group
where Telegram delivers it messages. Any human group member may invoke the bot
by mentioning `@Protocosmo2bot` or replying to it; direct messages remain
Ben-only. Keep durable delivery deduplication/recovery, reply-depth control,
bot-author exclusion, and a high emergency rate ceiling. Attachments,
autonomous schedules, and state-changing extras remain disabled until their
runtime paths exist and are separately reviewed.

### Attachment revision authorized by Ben, 2026-08-06

Ben subsequently requested repair of Telegram group attachment visibility.
Permit bounded read-only extraction for addressed PDF and text documents: at
most 10 MB downloaded and 60,000 extracted characters, labeled external
untrusted content, with no attachment egress. Unsupported or malformed media
fail closed. Unaddressed group attachments remain skipped. Evidence:
`experiments/20260807T003656Z-protocosmo2-telegram-document-ingestion/`.

### Evidence and operational note

The focused suite passes 25/25 and Telegram reports group join/read-all
capability. During the first broad-start probe, a bot-authored group update was
incorrectly admitted and crash recovery sent one fixed failure reply (receipt
`267`). The worker was stopped; explicit bot filtering, cursor advancement for
ignored updates, and a regression were added. A second pending bot message was
closed without output. The repaired supervisor is active with no pending
transaction and no further delivery.

## 2026-08-04 - Task-contract configuration has finite hard maxima

- Decision: cap each ThreadKeeper task-contract list field at 256 entries,
  each list item at 8,192 characters, and the objective at 65,536 characters,
  even when environment configuration requests larger values.
- Rationale: task contracts cross dispatch, queue, prompt, and durable-record
  boundaries; operator-tunable validation limits must not permit unbounded
  memory, parsing, prompt, or persistence work.
- Scope: validation ceilings only. Existing defaults remain 32 entries, 512
  characters per item, and 4,000 objective characters; no provider or runtime
  activation is authorized.
# D-20260806-protomega-native-document-egress: Use an explicit OmegaClaw action

- Date: `2026-08-06`
- Status: `accepted and live`
- Evidence: OmegaClaw-Core commit `d914aaf`; Telegram delivery receipt `9471`

Protomega attachments use the native `send-document absolute_path caption`
action, not OpenClaw's textual `MEDIA:` convention. OmegaClaw consumes the raw
model response as an action program and calls its Telegram transport directly;
therefore a gateway-only convention is the wrong abstraction boundary. The
transport accepts only regular `.pdf`, `.tex`, and `.latex` files below
`/home/openclaw/research-agent`, limits files to 50 MB and captions to 1,024
characters, binds delivery to the active inbound envelope, and requires a
Telegram receipt. Six focused tests and a live group delivery passed.

# D-20260806-iterative-worker-execution: Enable bounded resumable task-series execution

- Date: `2026-08-06`
- Status: `accepted and live`
- Decision owner: Benjamin Goertzel
- Evidence: `experiments/20260807T062249Z-output-fixes-worker-executor/`

OmegaClaw agents may launch a detached local executor that iteratively invokes
the configured LLM route over an exact, bounded directive plan. Execution is
bound to the persistent-worker manifest: finite steps, runtime and token caps,
explicit tools/effects and allowed paths, immutable request digest, per-step
prompt/response hashes and token receipts, hash-chained checkpoints, and
pause/resume/cancel states. Completed receipts are not replayed after a crash.

This authorization does not grant remote-compute spend, destructive effects,
or external messaging. Those remain subject to their existing explicit
authority gates. Provider-free acceptance passed 34/34; both Telegram
supervisors were restarted after loading the executor.
# D-20260814-clean-mock-isolation-reopened: Verify opened history, not declared roots

- Date: `2026-08-14`
- Status: `accepted`
- Evidence: `experiments/20260814T100700Z-restart-persistence/RUN.md`

The clean-install three-configuration gate is reopened. Upstream
`memoryDirectory` did not redirect the history path actually opened by
`src/memory.metta`; the three successful per-identity exchanges shared the
disposable runtime's `memory/history.metta`. Distinct declared state roots are
insufficient until the actual conversational-history file is identity-local.
The unchanged Test/test mocks are prerequisite smoke mechanisms, not frozen
failure/concurrency acceptance: they expose neither fault injection/provider
timeout nor addressed session envelopes. Prefer isolated runtime layouts and
disposable thin test adapters; this decision authorizes no clean-source edit.

# D-20260814-separate-disposable-upstream-runtimes: Isolate library-relative history by runtime

- Date: `2026-08-14`
- Status: `accepted for staging`
- Evidence: `experiments/20260814T102825Z-corrected-three-runtime-isolation/RUN.md`

Use one disposable same-commit upstream runtime copy per staging identity.
This makes upstream's library-relative `memory/history.metta` path genuinely
identity-local without editing the clean pinned source. Declared external
state roots remain separate as defense in depth. Structural inode evidence is
necessary but not conversational acceptance; each runtime must still pass
fresh turns with negative cross-history assertions before the isolation gate
closes. This decision grants no production identity or preserved-Chroma use.

The conversational condition passed on 2026-08-14: all three runtimes
completed two fresh turns and each actual history contained two own markers
and zero foreign markers. Evidence:
`experiments/20260814T103800Z-corrected-three-runtime-conversations/RUN.md`.

# D-20260814-protomega-disposable-direct-attachment: Preserve source; defer migration

- Date: `2026-08-14`
- Status: `accepted for staging evidence only`
- Evidence: `experiments/20260814T111500Z-protomega-chroma-upstream-recall/RUN.md`

Pinned `petta_lib_chromadb` `2184848` with ChromaDB `1.5.9` can directly read
and exactly recall the sole known Protomega record from a disposable ordinary
copy. Therefore no schema/vector migration is justified unless later
full-loop integration demonstrates a concrete incompatibility. The
authoritative store remains preservation-only and must never be attached:
review confirmed that Chroma attachment can change the disposable copy's
SQLite bytes. Independent Fable review closed only the one-record disposable
compatibility/exact-recall gate; text-query embedding compatibility,
multi-record behavior, writes, full-loop use, production attachment, and
cutover remain open.
# D-20260814-protomega-reembedding-required: Do not directly attach for text recall

- Date: `2026-08-14`
- Status: `accepted for staging design`
- Evidence: `experiments/20260814T113500Z-protomega-text-embedding-compatibility/`

Pinned upstream local text embeddings are 1,024-dimensional, while preserved
Protomega Chroma is 384-dimensional; exact-document query was rejected.
Direct attachment is therefore preservation evidence only. Any staging use
must re-embed one-way from a verified copy into a new store, reconcile all
records, pass restart/full-loop recall, and retain path-selection rollback.
The authoritative source remains unopened and immutable.

# D-20260814-telegram-shaped-timeout-is-uncertain-final: Do not retry timed-out sends

- Date: `2026-08-14`
- Status: `accepted for injected-fixture phase only`
- Evidence: `experiments/20260814T145500Z-telegram-shaped-addressed-adapter/RUN.md`

The production-free injected transport has an adapter-enforced deadline.
An acquisition timeout may be retried because it has no acknowledged cursor
advance. A delivery timeout finalizes its event and must not be retried: the
daemon fixture call cannot be cancelled and may have completed its external
side effect after the caller's deadline. Surface this as an uncertain bounded
failure rather than risking duplicate delivery. Commit `6082d60` extends the
same conservative classification to all post-dispatch failures. Binding phase-
end Fable review reproduced the late side effect and accepted this policy only
for freezing the injected-fixture phase. It is not approval of a real Telegram
transport. Before any such phase, fix the ledger-pruning route-restoration
defect and explicitly decide whether acquire-time cursor acknowledgement and
possible restart loss are acceptable.
# D-20260814-protomega-crash-is-loop-specific: Stop widening component probes

- Date: `2026-08-14`
- Status: `accepted for diagnostic scope`
- Evidence: `experiments/20260814T182200Z-protomega-repeat-isolation/RUN.md`,
  `experiments/20260814T183300Z-protomega-repeated-petta-eval/RUN.md`

Repeated offline E5/Chroma calls pass in Python, and twelve repeated exact
recalls pass through one fresh PeTTa/SWI/Janus process (six direct `query` and
six loop-style wrapped `eval(query)`). Do not widen generalized E5, Chroma, or
standalone PeTTa investigation without new contradictory evidence. The next
critical-path discriminator is a fresh nonce-separated OmegaClaw two-phase
soak with response-anchored non-empty recall checks and isolated evidence.
This decision grants no Telegram, production identity, or cutover authority.

# D-20260814-protomega-soak-needs-exclusive-copy: Fence each acceptance copy

- Date: `2026-08-14`
- Status: `accepted for successor evidence`
- Evidence: `experiments/20260814T184300Z-protomega-successor-soak/RUN.md`

The nonce-separated successor again crashed on continuous-loop turn 3 after
two genuine recalls, but its canonical migrated-copy manifest also changed
during the run from overlapping access outside the harness. Future acceptance
runs must create and exclusively reference a per-attempt ordinary copy. The
authoritative original remains hash-only and unopened by the runtime. Do not
require an attached Chroma 1.5.9 copy to remain byte-identical across open/read;
the HNSW files may change. Instead preserve and hash the immutable input copy,
permit mutations only in a separate runtime attachment, and verify recalled
content plus rollback/disposal evidence.
# 2026-08-14 11:56 PDT - Canonical-copy overlap is not the Protomega crash cause

A fresh phase-1 discriminator used a uniquely named immutable migration input
and a separate mutable runtime attachment. It still produced two exact recalls
and crashed with SWI/Janus SIGSEGV on turn 3. Protected manifests, network
denial, and zero-descendant teardown all held. Therefore canonical migrated-
copy overlap and ordinary Chroma open-time mutation are excluded as causes of
the reproducible third-turn failure. Keep soak NO-GO; next separate send-only
from query-only conversational turns before altering code.
# 2026-08-14 — Treat accumulated history as the next Protomega crash discriminator

**Decision:** Keep production and Telegram unauthorized and investigate only
disposable history copies. Stop extending Chroma/plugin diagnostics unless the
history bisection contradicts the current separation.

**Evidence:** Run `20260814T191100Z-protomega-history-discriminator` used the
same pinned clean runtime and send-only transport shape. Empty history passed
three turns; accumulated history acknowledged two turns and crashed on turn 3
inside SWI/Janus. Kernel egress denial, protected-store byte stability, and
zero-descendant teardown held.

**Rationale:** This is the smallest observed variable that separates a passing
three-turn loop from the repeated failure. It narrows but does not yet prove a
specific history record, size threshold, logging defect, or Janus root cause.
## 2026-08-14 — Treat Protomega's 21/22-record boundary as localization, not a repair

- **Observed:** isolated prefix bisection and replay pass at 21 records / 4,201
  bytes and reproduce SWI/Janus SIGSEGV at 22 records / 4,396 bytes.
- **Decision:** keep production-free soak NO-GO. Do not truncate valuable
  history as a putative fix; first distinguish boundary-record content from a
  prompt/history-size threshold using disposable equal-size substitutions.
- **Evidence:**
  `experiments/20260814T192400Z-protomega-history-prefix-bisection/`.

## 2026-08-14 — Exclude original record 22 content; cross count against bytes

- **Observed:** original records 21 and 22 are both 195 bytes. Replacing record
  21 with record 22 passes at 21 records / 4,201 bytes twice; replacing record
  22 with a duplicate of record 21 still crashes at 22 records / 4,396 bytes
  twice.
- **Decision:** do not edit, truncate, or discard valuable accumulated history
  as a repair. The next production-free discriminator independently crosses
  record count and serialized byte size using disposable valid histories.
- **Evidence:**
  `experiments/20260814T193954Z-protomega-history-equal-size-substitution/`.
