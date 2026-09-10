# ProtoMegaBot Reliability Repair Plan

Date: 2026-07-12
Basis: direct runtime/source inspection plus the independently recorded GPT-5.6-sol architecture review.
Scope: repair reliability without conflating Telegram transport defects, native SWI/Janus crashes, and model-provider routing.

## Current evidence

- The deployed process generation is unhealthy: one SWI worker, no bridge owned by that worker, and two global MTProto bridge processes were observed before this plan was written.
- The source-only P0 patch enforces one receive transport, removes silent MTProto receive fallback, couples bridge lifetime to its parent, adds singleton/session-file protections, and improves topology status.
- Focused validation passed: 14 transport-invariant pytest checks with `--noconftest`, four address-filter unittests, Python compilation, shell syntax checks, and `git diff --check`.
- The patch is not deployed. No current ProtoMegaBot process has been stopped or restarted by this repair effort.
- Signal 11 and exit 137 remain separate, unclassified failure classes.

## Safety invariants

1. Exactly one authoritative service generation owns receive ingress and the SWI worker.
2. Exactly one Telegram receive transport is enabled; MTProto mode cannot call Bot API `getUpdates`.
3. Exactly one bridge exists, and it is owned by the current generation.
4. Startup fails closed if ownership, lock, authentication, handler installation, or consumer readiness fails.
5. Every reply carries immutable source-message routing context; ordinary replies never depend on global latest-chat state.
6. Queue overflow, restart loss, and send failure are explicit and observable, never silently discarded.
7. Topology liveness, component readiness, and end-to-end health are reported separately.
8. Signal 11, signal 9/exit 137, watchdog termination, timeout, operator stop, and normal exit are classified separately.

## Step-by-step execution plan

### 1. Freeze and inventory the current generation

- Record owner PID, worker PID, all project bridge PIDs and parent PIDs, process start times, command lines, open session/lock files, and relevant log offsets.
- Record source commit/diff and launcher/supervisor checksums.
- Capture current status without changing processes.

Gate: a complete rollback/inventory record exists and contains no secrets.

### 2. Package the P0 transport/ownership patch as one reviewable change

- Review the existing source-only diff for transport exclusivity, fail-closed behavior, bridge parent fencing, lock permissions, and topology reporting.
- Preserve unrelated local work; do not mix immutable-envelope or crash-instrumentation changes into this deployment unit.
- Add a rollback pointer to the exact pre-patch files/commit.

Gate: focused tests, `py_compile`, `bash -n`, and `git diff --check` pass from the intended deployment tree.

### 3. Add pre-deployment negative tests

- Prove `_poll_once()` and synchronous `getLastMessage()` cannot reach Bot API polling in MTProto mode.
- Prove MTProto startup error does not activate Bot API receive fallback.
- Prove a second bridge instance cannot acquire the lock.
- Prove parent-PID mismatch/parent death causes bridge exit.
- Prove status fails readiness for zero, duplicate, orphaned, or foreign-generation bridges.

Gate: all negative tests pass deterministically without Telegram network access.

### 4. Prepare a controlled cleanup/restart runbook

- Define exact stop order: prevent supervisor respawn, stop the authoritative owner, terminate only project-matching unmanaged bridges, verify all old-generation PIDs are gone, then start one patched generation.
- Define rollback: stop the patched generation, restore the recorded source/launcher state, remove only stale project locks after PID verification, and start one previous generation.
- Define stop conditions: duplicate bridge, any `getUpdates` call, bridge not owned by worker generation, repeated restart, wrong-chat send, signal 11, or unexplained exit 137.

Gate: Ben approves this live-process operation before execution.

### 5. Execute one-generation cleanup and startup

- Stop the current unhealthy generation through the supervisor path.
- Clean only verified project bridge processes; do not use broad process-name killing.
- Start exactly one patched generation.
- Verify one supervisor/owner, one SWI worker, one owned bridge, one global project bridge, correct parent chain, mode-0600 session/lock files, and no old-generation process.

Gate: topology is stable for a bounded observation period with no restart loop.

### 6. Verify transport exclusivity at runtime

- Confirm effective `TG_RECEIVE_TRANSPORT=mtproto` and `TG_SYNC_POLL=false`.
- Inspect logs/network instrumentation for absence of Bot API `getUpdates`.
- Confirm Bot API remains available only for approved send/download operations.
- Force a bounded bridge-start failure in a non-live fixture and verify fail-closed behavior.

Gate: MTProto is the sole receive path and failure does not switch transports.

### 7. Run a bounded private-chat canary

Use a unique correlation ID and a fixed/stub response first, not an unrestricted model call.

- Receive one private Telegram message.
- Verify bridge authentication, handler installation, event receipt, queue consumption, and source-chat envelope.
- Send one correlated fixed response to the originating chat/message.
- Verify no duplicate receive, duplicate response, unrelated-chat send, or stale fallback.
- Repeat once through the real provider path only after the stub path succeeds.

Gate: receive-to-reply succeeds exactly once with correct source routing; otherwise stop and roll back.

### 8. Replace mutable `_active_chat_id` routing with immutable envelopes

Define an immutable envelope containing at least:

- `run_id`
- `generation_id`
- `update_id`
- `source_chat_id`
- `source_message_id`
- `sender_id`
- `correlation_id`
- `response_policy`
- receive timestamp

Pass it through dequeue, model/stub invocation, retries, continuations, tool/skill calls, and send. Remove ordinary-reply dependence on `_active_chat_id` and generic fallback IDs. Make sends reject missing/ambiguous envelopes except explicitly declared administrative broadcasts.

Gate: concurrency tests interleave two chats and delayed/retried responses without cross-chat delivery.

### 9. Introduce bounded framed IPC and backpressure

- Move toward separately supervised Telethon ingress with framed Unix-domain-socket IPC rather than stdout plus best-effort FIFO.
- Add protocol version, generation ID, message length cap, acknowledgement, bounded queue depth, and explicit overflow policy.
- Persist accepted-but-not-yet-consumed envelopes or reject them visibly; never silently drop on restart.

Gate: restart, malformed frame, consumer disconnect, and queue-saturation tests have deterministic outcomes.

### 10. Split liveness, readiness, and end-to-end health

- Liveness: authoritative owner exists and is not restart-looping.
- Readiness: SWI initialized; exactly one owned bridge authenticated with handler installed; ingress consumer connected; outbound provider/send probes pass.
- End-to-end health: a bounded synthetic canary traverses ingress, queue, stub/provider, and source-chat send.

Do not treat a bridge PID or stale last-message timestamp as health.

Gate: each deliberately broken state fails the correct layer without producing a false `ok`.

### 11. Add structured, privacy-safe event journaling

Record correlation ID, generation/component IDs, timestamps, state transitions, queue outcomes, send outcomes, and exit classifications. Do not record message bodies, tokens, session credentials, or secret-bearing environment values.

Gate: one canary can be reconstructed end-to-end from metadata alone, and a secret scan is clean.

### 12. Instrument native crashes before further semantic changes

- Enable controlled core-dump capture for the ProtoMegaBot service subject to disk limits and privacy-safe storage.
- Record exact SWI-Prolog, Janus, Python, Telethon, native extension, kernel, and loaded-library versions.
- Capture native backtrace/all-thread stacks for every signal 11.
- Capture cgroup/kernel OOM evidence and supervisor action for every exit 137.
- Classify normal stop, timeout, watchdog escalation, operator kill, OOM/SIGKILL, and SIGSEGV independently.

Gate: the next abnormal exit produces an attributable record rather than only a numeric status.

### 13. Run a one-variable-at-a-time crash matrix

Test bounded variants:

1. fixed response with no Gateway;
2. reader thread disabled/enabled;
3. Bot API fixture versus MTProto fixture;
4. polling disabled/enabled in isolated tests only;
5. bridge connected with no event delivery;
6. one event versus bounded load;
7. normal teardown versus forced SWI crash.

Gate: a minimal reproducer or evidence-backed exclusion table exists; do not label signal 11 solved without a reproduced fix.

### 14. Controlled soak and gradual expansion

- Private chat only, bounded duration and message count.
- Then two-chat concurrency canary.
- Then supervised scheduled-updates channel if routing and crash gates remain clean.
- Group/channel use comes last, with immediate rollback conditions.

Gate: no duplicate receivers, wrong-chat sends, unexplained exits, queue loss, or false health during the agreed soak window.

### 15. Closeout and readiness decision

- Re-run focused and broader available tests.
- Record deployment generation, exact code revision, configs, canary evidence, crash evidence, and rollback result.
- Update project tasks/decisions and the architecture report if implementation differs materially.
- Declare unattended multi-chat readiness only if all invariants and soak gates pass.

## Recommended order

Immediate priority is Steps 1-7: deploy and verify the already-tested P0 transport/ownership patch under an explicit live-change approval. Steps 8-11 establish a correct message transaction boundary and honest health model. Steps 12-13 investigate the native crash independently. Steps 14-15 expand service only after evidence supports it.
