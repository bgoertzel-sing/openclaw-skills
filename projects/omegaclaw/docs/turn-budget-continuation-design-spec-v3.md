# Turn-Budget Continuation + Concurrency: Requirements and Design Spec v3

**Version:** 3.0 — Draft
**Date:** 2026-09-04
**Author:** ZeroBot (ProtoCosmo)
**Status:** Proposed — incorporates v2 frontier review + concurrency design discussion
**Supersedes:** v2 (turn-budget-continuation-design-spec-v2.md)

---

## 1. Problem

ProtoCosmo2's Iter agent loop (iter.py) has two coupled failure modes:

1. **Turn-budget exhaustion.** `MAX_FAST_STEPS = 50`. When a task exceeds the
   budget without the agent calling `send`, the outer transport emits a
   generic "could not complete this message safely" failure. In-progress work
   is invisible to the user; the message is indistinguishable from a crash.

2. **Foreground blocking.** Every LLM call runs synchronously in the main
   loop. A single slow call (thinking-heavy prompts can run 60–300s+) blocks
   all channel responsiveness for its duration. The user sees silence even
   though the loop is healthy. There is no way to know in advance whether a
   call will be slow.

Both produce the same user-visible symptom: long silence followed by either
a late reply or a misleading failure message.

## 2. Design principles

1. **Skills and transformations over loop mods.** Everything implementable
   via iter's existing extension points (transformations = context
   preprocessors, tools = skills) lives there. iter.py loads both
   dynamically, so adding/removing files changes behavior without patching
   the dispatch loop. Rollback = delete files.
2. **Mechanical guarantees over LLM-dependent behavior.** Any safety
   mechanism that must fire unconditionally cannot depend on an LLM call
   succeeding. LLM enhancement is layered on top of a deterministic
   fallback, never in the critical path.
3. **React to observed behavior, don't predict.** Concurrency routing uses
   time-based promotion (detach after observing slowness), not latency
   estimation. Estimators may tune thresholds later but never gate the
   mechanism.
4. **Flag-guarded residual loop changes.** The small number of changes that
   genuinely require loop code are isolated branches behind feature flags.
   Flag-off = byte-identical behavior to today.
5. **Normal conditions are not failures.** Turn-budget exhaustion and slow
   calls are normal operating conditions. The transport's safety-failure
   message is reserved for actual runtime failures.

## 3. Requirements

### Checkpoint/continuation (from v2, unchanged in substance)

- **R1: Guaranteed checkpoint at turn exhaustion.** At MAX_FAST_STEPS
  without a send, a checkpoint is produced unconditionally. Mechanical
  extraction from the experience log is the guaranteed path; LLM
  summarization is optional enhancement.
- **R2: Durable, well-ordered persistence.** Checkpoint file written
  atomically (temp+rename) before any send attempt.
- **R3: Continuation across turns.** New user message or auto-resume
  injects prior checkpoint context. Lifecycle: `active` → `consumed`;
  only newest active checkpoint per session is used; stale checkpoints
  (older than N minutes) never auto-resume.
- **R4: No false-alarm failure message** for budget exhaustion.
- **R5: Separation of concerns.** Structured machine-readable file for
  recovery; human-readable send for the user. Two artifacts, not one.
- **R6: Backward compatibility.** No breaking changes to send semantics,
  tool protocol, or experience-log format.
- **R7: Bounded overhead.** < 1s added latency, < 2KB typical checkpoint.

### Concurrency (new in v3)

- **R8: Bounded foreground blocking.** No single LLM call may block channel
  responsiveness longer than T seconds (default T=30, env-configurable).
- **R9: No token waste.** A detached call completes normally; its results
  are used. Nothing is abandoned and re-issued (v0 rejected for this).
- **R10: No prediction required.** Promotion to background is triggered by
  observed elapsed time, not estimated latency. An estimator may later tune
  T but is never in the decision path.
- **R11: Single writer.** Exactly one thread (the main loop) owns
  `receive()` (channel intake), `experience` mutation, and
  `save_experience()`. Background branches never touch channel state or
  save the file.
- **R12: Merge transparency.** Experience entries originating from a
  background branch are tagged (e.g., `"branch": "bg-<id>"`) so later
  reasoning can distinguish interleaved timelines.
- **R13: Graceful degradation.** If threading is unavailable or the
  background branch crashes, the loop behaves exactly as today (synchronous
  foreground), with the failure logged.

## 4. Design

### 4.1 What lives where (skills-not-loop-mods mapping)

| Mechanism | Implementation | Loop change? |
|---|---|---|
| Watchdog nudge (step 45) | Transformation injecting reminder text | No |
| Checkpoint file writer | Tool (`checkpoint.py`) | No |
| Continuation context injection | Transformation reading active checkpoint | No |
| Checkpoint lifecycle (active/consumed) | Tool + transformation | No |
| Guaranteed Tier-1 checkpoint at step 50 | Small flag-guarded loop branch | Yes (minimal) |
| Time-based promotion (T-deadline detach) | Flag-guarded loop branch | Yes (contained) |
| Background merge + tagging | Flag-guarded loop branch | Yes (contained) |

The three loop-touching items are the irreducible core: by definition the
agent failed to act on its own (forced checkpoint), and threads cannot live
inside 5-second subprocess skills (concurrency). Each is an isolated branch
behind a flag; flag-off path is today's exact behavior.

### 4.2 Checkpoint mechanism (v2 design, restated)

**Two-tier generation:**
- Tier 1 (guaranteed, deterministic): at the step limit with no send,
  mechanically extract last N tool calls (names + truncated outputs),
  prompt hash, step count, timestamps. No LLM. Always succeeds.
- Tier 2 (optional): one constrained LLM call summarizes
  accomplished/remaining/next_command. Any failure → fall back to Tier 1
  with `summary_source: "mechanical"`.

**Write ordering:** (1) generate content, (2) write file atomically,
(3) send human-readable rendering. File survives send failure; send
failure never blocks the file.

**Lifecycle:** created `active`; marked `consumed` on injection; newest
active only; older actives superseded; stale (>N min, default 300) ignored
by auto-resume.

### 4.3 Concurrency: time-based promotion

**Core flow:**

1. Every LLM call starts in the foreground (today's behavior) with a
   deadline T (default 30s).
2. If it returns within T: nothing changes. Fast calls never pay
   concurrency complexity.
3. If T expires: the in-flight call continues in a background thread
   holding its own message-list snapshot. The main loop immediately
   resumes `receive()` polling.
4. New chat during the background call is answered with fresh foreground
   calls against shared experience — which still contains the task
   context, so "still working on X, here's where it's at" answers are
   coherent.
5. When the background call completes, its tool calls execute in the
   background branch (tools are stateless subprocesses; safe). Results
   merge into shared experience under a lock, tagged `"branch": "bg-<id>"`.
   Only the main thread saves the file.

**One background branch at a time.** If a second call would exceed T while
a branch is active, it waits foreground (today's blocking behavior) — no
unbounded thread fan-out. Rationale: bounding concurrency to 2 keeps cost,
lock contention, and merge complexity bounded; true multi-branch
concurrency is explicitly out of scope for v3.

**Thread-safety specifics:**
- `experience`: mutated only by main thread; merge is an atomic
  `list.extend` under a lock, applied at a defined point in the main loop
  (top of iteration, before `receive()`).
- `save_experience()`: main thread only. Background branch queues its
  results in a thread-safe structure (e.g., `queue.Queue`); main thread
  drains and saves.
- `receive()`: main thread only. Background branch never polls channels.
- OpenAI client: thread-safe for concurrent requests (network I/O; GIL
  not a bottleneck).
- Tool execution: `invoke_dynamic` spawns subprocesses with no shared
  in-process state; safe from either thread. Exception: any future tool
  writing shared files must use atomic-rename discipline (checkpoint tool
  already does).

**Coherence model:** the background branch acts on a snapshot of the world
at detach time. While detached, the foreground may process chat that the
background never saw. This is semantically identical to "a message arrived
mid-task" — tolerable because (a) tool calls are re-executed against
current state at merge time, not replayed blindly, and (b) the branch tag
lets later reasoning recognize the interleaving. Known limitation: if the
foreground chat *invalidates* the background task (e.g., user says "stop
working on X"), the background branch completes anyway and its results
merge; the next foreground turn can discard them. A cancellation mechanism
(checked at merge time: "is this branch's task still relevant?") is a
Phase-7 candidate, not v3 scope.

**Why not an estimator as primary:** iter.py logs `USAGE {response.usage}`
per call, so a prompt-tokens → latency model is feasible, and latency is
likely bimodal (fast ~10–20s vs thinking-heavy 60–300s+). But a pre-routing
design breaks exactly on mispredictions (predicted-fast call that runs 4
minutes still blocks the loop). Time-based promotion degrades gracefully:
worst case is waiting T too long before detaching. Estimator role is
limited to future tuning of T (set near p90 of the fast mode) and a
finish-soon heuristic (if >95% likely to complete in <3s, wait rather than
detach). Both are optional refinements, never gates.

### 4.4 Interaction between checkpoint and concurrency

The mechanisms compose:
- A background branch carries its own step budget. If the branch exhausts
  its budget, the forced-checkpoint mechanism fires in the branch: Tier-1
  file write + the branch's results merge with a checkpoint marker.
- The watchdog transformation operates on shared experience and works
  unchanged regardless of which branch produced the entries.
- If the foreground is handling chat when a background branch completes,
  the merge waits for the next main-loop iteration — bounded by the
  foreground call's own T deadline. No unbounded merge delay.

## 5. What the frontier review of v2 said and how v3 responds

| v2 review finding | v3 response |
|---|---|
| No mechanical fallback for checkpoint LLM | Tier-1 mechanical-first design (§4.2) |
| Write-ordering bug (file after send) | File before send (§4.2) |
| Checkpoint lifecycle undefined | active/consumed + newest-only + staleness (§4.2) |
| Three-concern coupling on checkpoint-via-send | Separate file (machine) and send (human) (R5) |
| Phase 2 overloaded | Split into phases below |
| Validation too vague | Explicit failure-path test cases (§7) |

## 6. Implementation phases

- **Phase 1 (done):** watchdog text nudge at step 45. Live since 07:36
  restart.
- **Phase 1.5 (~1h):** upgrade watchdog to mechanically-extracted
  structured summary via send; include file write. Transformation + tool
  only, no loop change.
- **Phase 2a (~1h):** guaranteed Tier-1 checkpoint at step 50 + atomic
  file + lifecycle. Flag-guarded loop branch.
- **Phase 2b (~1h):** Tier-2 LLM summary with Tier-1 fallback.
- **Phase 2c (~30m):** human-readable send rendering; verify transport
  failure path never fires for exhaustion.
- **Phase 3 (~1–2h):** continuation context injection on new user message
  + consumed marking. Transformation only.
- **Phase 4 (~1–2h):** auto-resume with staleness threshold. Opt-in flag.
- **Phase 5 (~1h):** checkpoint validation battery (§7, cases a–f).
- **Phase 6 (~3–4h):** time-based promotion: T-deadline detach, background
  branch, merge protocol, tagging. Flag-guarded (`ITER_CONCURRENCY_ENABLED`).
  Includes thread-safety audit of all tools.
- **Phase 7 (deferred):** branch cancellation on task invalidation;
  adaptive-T estimator; finish-soon heuristic.
- **Phase 8 (~1h):** concurrency validation battery (§7, cases g–l).

## 7. Validation

**Checkpoint (Phase 5):**
a. Normal exhaustion → checkpoint fires, no safety-failure message.
b. LLM summary fails → Tier-1 fallback still produces file + send.
c. File write fails → minimal send still attempted, no crash.
d. Send fails → file persists, continuation still works.
e. Stale checkpoint → not auto-resumed.
f. Multiple checkpoints → only newest active used.

**Concurrency (Phase 8):**
g. Fast call (<T) → foreground, no thread spawned, behavior identical to
   today.
h. Slow call (>T) → detaches at T; channel responsive during call; results
   merge correctly with branch tag.
i. Chat arrives during background call → answered in foreground; merge
   order correct; experience file will never corrupt (kill -9 mid-merge
   test).
j. Background branch crashes → main loop unaffected, error logged,
   foreground continues normally.
k. Second slow call while branch active → blocks foreground (no fan-out),
   documented behavior.
l. Flag off → byte-identical behavior to pre-change loop (diff the
   code path; run existing provider-free test suite).

## 8. Open questions

1. Should the checkpoint send count against max_outbound_messages?
   (Preference: no — system-generated safety send.)
2. Auto-resume default? (Preference: opt-in initially.)
3. T default: 30s proposed. Validate against production latency
   distribution before Phase 6 (pull USAGE logs, fit bimodal split).
4. Branch tag format: `"branch": "bg-<id>"` in the experience dict — does
   any downstream consumer (transformations, memory promotion) need to
   handle it explicitly, or is pass-through safe?
5. Should the background branch get a reduced step budget (e.g., 25)
   since the foreground may also be consuming budget? (Preference: yes,
   separate counter, to bound total work.)
6. Voluntary checkpoint tool for the agent (checkpoint early on long
   tasks)? Deferred to post-Phase-5.

---

*Living document. Update as phases complete and validation data arrives.*
