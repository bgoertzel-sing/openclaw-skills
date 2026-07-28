# Decision Log

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
## 2026-07-22 - Audited relative paths use one canonical spelling

- Decision: require accepted ThreadKeeper file-tool paths and task-contract
  path prefixes to equal their platform-normalized relative spelling.
- Rationale: audit and authorization records must identify the exact path
  spelling consumed by filesystem helpers; redundant dot components,
  separators, or trailing separators create avoidable ambiguity.
- Scope: bounded synchronous ThreadKeeper hardening only; file contents and
  valid normalized relative paths are unchanged.
