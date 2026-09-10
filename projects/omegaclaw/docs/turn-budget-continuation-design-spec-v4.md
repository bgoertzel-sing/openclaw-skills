# Turn-Budget Continuation + Concurrency: Requirements and Design Spec v4

**Version:** 4.0 — Draft
**Date:** 2026-09-04
**Author:** ZeroBot (ProtoCosmo)
**Status:** Proposed — incorporates v3 frontier code review; responsiveness-first milestone ordering
**Supersedes:** v3 (turn-budget-continuation-design-spec-v3.md)

---

## 1. Problem (unchanged)

ProtoCosmo2's Iter loop (iter.py) has two coupled failure modes:

1. **Turn-budget exhaustion.** At MAX_FAST_STEPS=50 without a `send`, the
   outer transport emits a misleading "could not complete this message
   safely" failure. Observed 4+ times in a single day (2026-09-04).
2. **Foreground blocking.** Every LLM call runs synchronously in the main
   loop; a slow call (60–300s+) blocks all channel responsiveness. There
   is no way to know in advance whether a call will be slow.

The existing step-45 watchdog is only an LLM reminder and has proven
ineffective — the failures continued after it was deployed.

## 2. Design principles

1. **Skills and transformations over loop mods.** Everything that can live
   in iter's dynamic extension points lives there. Rollback = delete files.
2. **Mechanical guarantees over LLM-dependent behavior.** Anything that
   must fire unconditionally cannot depend on an LLM call succeeding.
3. **React to observed behavior, don't predict.** Concurrency routing uses
   time-based promotion, never latency estimation.
4. **Flag-guarded residual loop changes.** The irreducible loop changes
   are isolated branches behind flags; flag-off = byte-identical behavior.
5. **Normal conditions are not failures.** Budget exhaustion and slow
   calls are normal; the safety-failure message is for real failures.
6. **Single writer.** Only the main loop thread mutates `experience`,
   calls `receive()`, and calls `save_experience()`. No exceptions —
   including checkpoint writes, which are queued to the main thread.

## 3. Requirements

### Checkpoint/continuation
- R1: Guaranteed checkpoint at exhaustion — mechanical (Tier-1) path
  always succeeds; LLM summary (Tier-2) is optional enhancement.
- R2: Checkpoint file written atomically (temp+rename) by the main thread
  before any send attempt.
- R3: Lifecycle `active` → `consumed`; newest active only; stale (>300s)
  never auto-resumed.
- R4: No safety-failure message for budget exhaustion.
- R5: Machine-readable file and human-readable send are separate artifacts.
- R6: No breaking changes to send semantics, tool protocol, or
  experience-log format.
- R7: < 1s added latency, < 2KB typical checkpoint.

### Concurrency (incorporating v3 review)
- R8: No single LLM call blocks channel responsiveness longer than T
  (default 30s, env-configurable).
- R9: No token waste — detached calls complete normally; nothing is
  abandoned and re-issued.
- R10: No prediction in the decision path; promotion is triggered by
  observed elapsed time only.
- R11: Deep-copy isolation — the background branch gets a deep copy of
  the message list at detach time (or entries are enforced append-only).
  Shallow copies are forbidden.
- R12: Separate OpenAI client instance per background branch; no client
  sharing across threads.
- R13: Bounded background lifetime — BACKGROUND_DEADLINE (default 2×T or
  a fixed 300s cap, whichever is larger) after which the branch is
  abandoned: its results are discarded, an abandon marker is queued, and
  the branch slot frees. This bounds head-of-line blocking.
- R14: Deterministic error reporting — the background thread is wrapped
  in try/except; any exception pushes an error marker (type + bounded
  message) onto the merge queue. The main loop surfaces it as a normal
  experience entry; the branch slot frees.
- R15: Double merge-queue drain — the main loop drains the merge queue
  (a) at the top of each iteration before receive(), and (b) immediately
  before constructing the LLM message list. No one-iteration lag.
- R16: Merge tagging — background-originated entries carry
  `"branch": "bg-<id>"`; on duplicate tool calls against the same target
  from foreground and background, both entries are kept but the merge
  annotates the later one `"superseded_by": "<earlier-entry-index>"` so
  the LLM sees the conflict explicitly rather than silently.
- R17: Shutdown protocol — on SIGTERM/SIGINT the main loop sets a stop
  event, waits up to SHUTDOWN_GRACE (default 5s) for the branch to push
  its results, drains the queue, saves experience, then exits. Branch
  threads are daemon threads so a hung branch cannot block exit.
- R18: One background branch at a time; a second slow call while a branch
  is active blocks foreground (today's behavior). No fan-out.
- R19: Graceful degradation — if threading is unavailable or branch
  setup fails, the loop runs exactly as today and logs the failure.
- R20: Checkpoint-by-background respects single-writer: a branch that
  exhausts its step budget queues its Tier-1 checkpoint data to the main
  thread, which performs the file write and send.

## 4. Design

### 4.1 Skills-vs-loop-mods mapping (unchanged from v3)

| Mechanism | Implementation | Loop change? |
|---|---|---|
| Watchdog nudge (step 45) | Transformation | No |
| Checkpoint file writer | Tool (`checkpoint.py`) | No |
| Continuation context injection | Transformation | No |
| Checkpoint lifecycle | Tool + transformation | No |
| Guaranteed Tier-1 checkpoint at step 50 | Flag-guarded loop branch | Yes (minimal) |
| Time-based promotion | Flag-guarded loop branch | Yes |
| Background merge + tagging | Flag-guarded loop branch | Yes |

### 4.2 Checkpoint mechanism (v2/v3 design, with writer fix)

Two-tier: Tier-1 mechanical extraction (last N tool calls + truncated
outputs, prompt hash, step count, timestamps) always runs; Tier-2 LLM
summary is best-effort with Tier-1 fallback (`summary_source` field).

Write ordering: (1) generate content, (2) main thread writes file
atomically, (3) main thread sends human-readable rendering. If the
trigger fires in a background branch, the branch queues the checkpoint
payload; the main thread performs steps 2–3 (R20).

Lifecycle: created `active`; `consumed` on injection; newest active only;
superseded actives marked consumed; stale (>300s) ignored by auto-resume.

### 4.3 Concurrency: time-based promotion (hardened per review)

**Detach:**
1. LLM call starts foreground with deadline T (default 30s).
2. Returns within T → nothing changes.
3. T expires → deep copy of the message list is handed to a background
   thread with its own OpenAI client instance and branch id `bg-<uuid8>`.
   Main loop resumes receive() polling immediately.

**Background branch:**
- Runs its own mini-loop: complete the in-flight call, execute its tool
  calls (stateless subprocesses), optionally continue to a bounded number
  of follow-up steps (own step budget, default 25).
- Wrapped in try/except: any exception pushes an error marker onto the
  merge queue (R14).
- Hard-capped by BACKGROUND_DEADLINE (R13): on expiry the branch abandons
  remaining work, queues an abandon marker with partial results if any,
  and frees the slot.
- On step-budget exhaustion: queues Tier-1 checkpoint payload to main
  thread (R20); never writes files itself.

**Merge (main thread only):**
- Drain merge queue at top of iteration AND immediately before building
  the LLM message list (R15).
- Merge = atomic list.extend under a lock; entries tagged
  `"branch": "bg-<id>"`.
- Duplicate-tool-call handling: when a merged entry's tool call targets
  the same tool+arguments as an existing unresolved foreground entry,
  annotate the later one `"superseded_by"` (R16). Both stay in the log;
  the LLM sees the conflict explicitly.
- Only the main thread calls save_experience() after draining.

**Shutdown (R17):**
- SIGTERM/SIGINT → set stop event → wait SHUTDOWN_GRACE (5s) → drain
  queue → save → exit. Daemon threads; hung branch cannot block exit.
- Documented limitation: a process restart mid-branch loses the branch's
  un-merged work. Acceptable; the originating prompt persists in
  experience and the work can be re-requested.

**Coherence model (unchanged):** the branch acts on a snapshot; foreground
chat during the branch is invisible to it. Tool calls execute against
current state at execution time, not replayed. Branch tags let later
reasoning recognize interleaving. Cancellation on task invalidation
("stop working on X") remains a Phase-7 candidate.

**Why not an estimator (unchanged):** latency is likely bimodal; a
pre-routing estimator breaks on mispredictions. Time-based promotion
degrades gracefully. Estimators may later tune T (set near p90 of the
fast mode) and power a finish-soon heuristic — never gate the mechanism.
Before enabling in production, validate T against actual USAGE/latency
logs to confirm the bimodal split (see M4).

## 5. Implementation milestones (with frontier code review gates)

Per Ben's directive 2026-09-04: a frontier model reviews the code before
each milestone is accepted.

**M1 — Mechanical forced checkpoint (~1–2h).**
Flag-guarded loop branch: at step 50 with no send, Tier-1 mechanical
extraction → atomic file → human-readable send. Kills the misleading
safety-failure message. No threading involved.
Gate: frontier review of the diff + unit tests (trigger fires, file
written before send, flag-off identical).
Evidence: run a deliberately long task, observe checkpoint send, no
safety-failure message.

**M2 — Time-based promotion core (~3–4h).**
Detach at T, deep-copy isolation (R11), separate branch client (R12),
merge with tags under lock, double drain (R15), single-writer discipline.
Flag: ITER_CONCURRENCY_ENABLED.
Gate: frontier review focusing on thread-safety, copy isolation, merge
ordering, and the flag-off path.
Evidence: slow-call test — chat arrives mid-call, gets answered, branch
results merge tagged; kill -9 mid-merge leaves experience file intact.

**M3 — Concurrency hardening (~2–3h).**
Background deadline (R13), error markers (R14), shutdown protocol (R17),
duplicate-tool supersede annotation (R16), branch step budget + branch
checkpoint queuing (R20).
Gate: frontier review of failure-path handling.
Evidence: validation cases (g)–(o) below.

**M4 — Production validation + T calibration (~1–2h).**
Extract USAGE/latency distribution from production logs, confirm bimodal
split, set T near p90 of the fast mode. Soak test on the live bot behind
the flag; then enable by default.
Gate: frontier review of soak results + go/no-go.

**M5 (deferred) — Continuation/auto-resume.**
Checkpoint context injection on new message; opt-in auto-resume with
staleness. Only after M1–M4 are stable.

**M6 (deferred) — Enhancements.**
Branch cancellation on task invalidation; adaptive-T; finish-soon
heuristic; Tier-2 LLM checkpoint summaries; voluntary checkpoint tool.

## 6. Validation battery

**Checkpoint (M1):**
a. Normal exhaustion → checkpoint fires, no safety-failure message.
b. File write fails → minimal send still attempted, no crash.
c. Send fails → file persists.
d. Flag off → byte-identical behavior; existing test suite passes.

**Concurrency (M3/M4):**
e. Fast call (<T) → foreground, no thread, identical behavior.
f. Slow call (>T) → detaches at T; channel responsive; tagged merge.
g. Chat during background → answered in foreground; merge order correct.
h. Kill -9 mid-merge → experience file never corrupt.
i. Background exception → error marker surfaces; slot frees; loop
   continues.
j. Background exceeds BACKGROUND_DEADLINE → abandon marker; slot frees;
   subsequent slow call may promote.
k. Second slow call while branch active → blocks foreground (documented).
l. Shutdown during active branch → stop event, bounded wait, clean exit,
   experience saved.
m. Deep-copy isolation → background mutating its message list never
   affects foreground experience (direct corruption test).
n. Duplicate tool call from both branches → later entry carries
   superseded_by; LLM-visible.
o. Flag off → byte-identical behavior; existing test suite passes.

## 7. Open questions

1. Checkpoint send vs max_outbound_messages (preference: exempt).
2. BACKGROUND_DEADLINE: fixed cap vs multiple of T (preference: max(2T,
   300s)).
3. Branch step budget (preference: 25, separate counter).
4. Branch tag handling in downstream consumers (transformations, memory
   promotion) — pass-through assumed safe; verify in M2 review.
5. T default validation pending production latency data (M4).

---

*Living document. Update as milestones complete.*
