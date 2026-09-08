# Petta-Memory & Iter Integration Specification v4

**Version:** 4.0  
**Date:** 2026-09-04  
**Author:** ProtomegaTron  
**Status:** Implementation-ready — pending Ben's final sign-off  
**Supersedes:** rollback-specification.md (v0.1), rollback-spec-frontier-review.md

---

## 0. Design History

| Version | Date | What changed |
|---------|------|-------------|
| v0.1 | 2026-09-04 | Initial rollback spec: 6 components, feature flags, shadow mode, per-component rollback |
| v1-review | 2026-09-04 | Frontier model review: identified quiescence gap (C1), attention-collapse flap (T1), threshold deadband issues (T2), data-loss in queue drain (C2), provenance circularity (C3) |
| v3 | 2026-09-04 | Architecture decision: skills-not-loop-changes. All 6 components implementable as Iter skills + context preprocessor. No core loop modification needed. |
| **v4** | 2026-09-04 | This document. Integrates concurrency/cooperative multitasking model, addresses all frontier review findings, defines implementation milestones with mandatory frontier code review at each gate. |

---

## 1. Architecture: Skills, Not Loop Surgery

### 1.1 Core Principle

Iter's 266-line dispatch loop (`iter.py`) remains **unchanged**. All new capabilities are implemented as:

- **Skills** (`tools/*.py`) — petta-memory read/write, episodic query, hypothesis management
- **Context preprocessor** (`transformations/*.py`) — attentional stratum shapes what Iter sees before each turn
- **Structured continuation patterns** — research protocols expressed as sequences of skill calls using Iter's existing experience/continuation mechanism

### 1.2 Rationale

1. **Blast radius containment:** Disabling a misbehaving skill is a file rename (`mv tool.py _tool.py`). No redeploy, no loop rollback.
2. **Independent testability:** Each skill has its own test suite. Iter's core loop is already proven.
3. **Separation of concerns:** Iter is a dispatcher; petta-memory is a capability. Mixing them violates the stable-substrate / reprogrammable-surface split that makes Iter maintainable.

### 1.3 Component Mapping

| Component | Implementation | Iter Touched? |
|-----------|---------------|---------------|
| Petta-memory store | External service + `tools/petta_memory.py` | No |
| Ingestion adapter | Background process + `tools/petta_ingest.py` | No |
| Read integration | `tools/petta_read.py` | No |
| Episodic tagging | `tools/petta_provenance.py` | No |
| Attentional stratum | `transformations/attention.py` | No — preprocessor |
| Self-revising experiment protocol | Structured skill-call pattern in experience | No — it's a *program*, not a *modification* |
| Cooperative multitasking | Skill-level yield convention (§2) | No |

---

## 2. Concurrency Model: Cooperative Yielding

### 2.1 Problem

Iter is single-threaded. During a long-running tool execution or LLM call, `receive()` is not called. Chat messages queue silently. The agent appears unresponsive.

### 2.2 Rejected Approaches

| Approach | Why rejected |
|----------|-------------|
| **True parallelism** (threading/multiprocessing) | Shared mutable state (`experience.json`, memory files) creates race conditions. Iter's architecture assumes sequential execution. Retrofitting thread safety is a core rewrite, not a skill-level change. |
| **Preemptive interruption** (signal-based) | Interrupting mid-tool-execution can leave state inconsistent. Would require every tool to be interrupt-safe — changes the tool author contract. |
| **Event loop / async rewrite** | Replaces Iter's entire execution model. Violates skills-not-loop-changes principle. |
| **Core loop modification** (poll between steps) | Modifying `iter.py` to check for messages between tool calls. Works but breaks our architectural commitment. Also insufficient — doesn't help during the LLM call itself, which is often the longest wait. |

### 2.3 Adopted Approach: Cooperative Yielding

Long-running skills are written to **periodically yield** control back to Iter:

1. **Skill checkpoints state** to a durable artifact (file, JSON blob)
2. **Skill returns** a continuation marker: `{"status": "yielded", "checkpoint": "path/to/state.json", "resume_with": "continue_research"}`
3. **Iter processes the return** as a normal tool result
4. **Iter's next receive()** picks up any pending chat messages
5. **On the next autonomous step**, the LLM sees the checkpoint and can resume via another tool call

### 2.4 Yield Convention (Skill Author Contract)

```python
# tools/long_running_example.py
DESCRIPTION = "A skill that does multi-step work cooperatively"

def run(action="start", checkpoint_path=""):
    if action == "start":
        state = initialize_work()
        save_checkpoint(state, "checkpoints/mywork.json")
        return json.dumps({
            "status": "yielded",
            "progress": "1/5 steps complete",
            "checkpoint": "checkpoints/mywork.json",
            "hint": "Call me again with action=continue to resume"
        })
    elif action == "continue":
        state = load_checkpoint(checkpoint_path)
        result = do_next_chunk(state)
        if result.done:
            return json.dumps({"status": "complete", "result": result.value})
        save_checkpoint(result.state, checkpoint_path)
        return json.dumps({
            "status": "yielded",
            "progress": f"{result.steps_done}/{result.total_steps}",
            "checkpoint": checkpoint_path,
            "hint": "Call me again with action=continue"
        })
```

### 2.5 Context Awareness After Yield

When a skill yields and a chat message arrives during the gap:

- The LLM sees **both** the yield checkpoint **and** the new message in its next context
- It can decide: resume the interrupted work, respond to the message first, or do both
- The skill's checkpointed state is context-independent — it doesn't capture the conversation, only its own work state

This is **strictly better** than preemptive interruption because the LLM (not the scheduler) decides priority. A human message about the ongoing task can *inform* the resumed work. A human message about something else gets answered first.

### 2.6 Limitations and Mitigations

| Limitation | Mitigation |
|------------|-----------|
| LLM call itself can't be interrupted | LLM calls are typically <30s (`LLM_TIMEOUT=30`). Acceptable latency for chat responsiveness. For truly time-sensitive channels, reduce `MAX_TOKENS` or use faster models. |
| Tool must be written cooperatively | All *new* tools follow the convention. Existing tools are short-lived (file reads, sends). Only the new petta-memory and research-protocol tools need yield logic. |
| Checkpoint serialization overhead | Negligible for the state sizes involved (JSON blobs, not large datasets). |
| LLM might not resume | Include clear continuation hints in yield output. Transformation preprocessor can inject "you have pending work" reminders. |

---

## 3. Component Specifications

### 3.1 Petta-Memory Store

**File:** `tools/petta_memory.py`

**Operations:**
- `store(text, metadata)` — embed and store a memory entry
- `query(text, top_k)` — semantic search, return top-k results
- `delete(entry_id)` — remove by ID
- `health()` — integrity check, return stats

**Backend:** ChromaDB (existing infra) or configurable vector store.

**Feature flag:** `PETTA_MEMORY_ENABLED` env var; tool returns "disabled" message when off.

**State artifacts:** Vector store directory, metadata index, schema version marker.

**Snapshot strategy:**
- Full export before schema/data migrations
- Daily incremental snapshots while active
- Checksumming of stored blobs (addresses frontier review C5)
- Pairwise embedding-space sanity sampling on restore

### 3.2 Ingestion Adapter

**File:** `tools/petta_ingest.py`

**Operations:**
- `ingest(source, content, provenance)` — process and store with full provenance
- `status()` — queue depth, throughput, error count
- `drain(mode)` — `mode=preserve` dumps queue to replay file; `mode=discard` drops (requires explicit confirmation)

**Shadow mode:** Writes to shadow partition, not live store. Compare shadow vs expected for ≥48h.

**Queue drain policy (frontier review C2 fix):** Default drain mode is `preserve` — payloads are dumped to `ingestion_replay_TIMESTAMP.jsonl`, never silently discarded. Replay file enables re-ingestion after root cause fix.

**Rollback triggers:**
- Throughput anomaly: sustained >3× or <0.1× expected over a 2-hour activity window (frontier review T5 fix — sustain duration, not instantaneous)
- Malformed entries in store
- Provenance tag absence on any entry

### 3.3 Read Integration

**File:** `tools/petta_read.py`

**Operations:**
- `read(query, max_results, context_budget)` — retrieve relevant memories within context budget
- `explain(entry_id)` — show provenance chain for an entry

**Feature flag:** `PETTA_READ_ENABLED`

**Threshold deadband (frontier review T2 fix):**
- Shadow acceptance criterion: p95 latency < 400ms, relevance ≥ 75%
- Live rollback trigger: p95 latency > 750ms sustained over 30 minutes, or relevance < 60%
- Gap between accept and abort prevents flapping

### 3.4 Episodic Tagging & Provenance

**File:** `tools/petta_provenance.py`

**Operations:**
- `tag(entry_id, tags)` — add episodic/causal tags
- `link(source_id, target_id, relation)` — create causal/epistemic link
- `rebuild()` — full rebuild from raw data + ingestion logs
- `validate()` — check for circular links, orphan references

**Note:** Derived from primary data; always rebuildable. Low rollback risk.

**Pollution remediation order (frontier review C3 fix):** Snapshot-restore is preferred over tag-based batch delete. Tag-based delete is fallback only when store is otherwise sound and provenance layer is verified intact.

### 3.5 Attentional Stratum

**File:** `transformations/attention.py`

**Mechanism:** Runs as a transformation (preprocessor), not a tool. Shapes what the LLM sees by re-ranking and filtering memory retrievals and context before each turn. Iter doesn't know it's there.

**State artifacts:** Attention weights, salience scores, promotion/demotion history, goal-relevance associations.

**Feature flag:** `PETTA_ATTENTION_ENABLED` — when off, transformation is a no-op passthrough.

**Shadow mode:** ≥72 hours. Computes alternative rankings but doesn't affect actual context. Logs: what would have been promoted/demoted vs. baseline.

**Attention-collapse guard (frontier review T1 fix):**
Distinguish "uniform because freshly reset" from "uniform despite rich evidence":
```
if weights_near_uniform AND evidence_volume > MINIMUM_EVIDENCE_THRESHOLD AND training_age > BOOTSTRAP_PERIOD:
    trigger_rollback("attention collapse — uniform despite evidence")
else:
    # Benign bootstrap state, no alarm
```

**Rollback triggers:**
- Attention runaway: single topic >80% of salience budget
- Attention collapse: near-uniform weights *after bootstrap period with sufficient evidence*
- Stale promotion: entries >30 days old promoted without fresh evidence
- Salience oscillation: weight variance >2× over consecutive 4-hour windows

### 3.6 Self-Revising Experiment Protocol

**Files:** `tools/hypothesis.py`, `tools/experiment.py`

**Not a loop change.** This is a structured pattern of tool calls:

1. **Propose** — `hypothesis.py: propose(description, prediction, success_criteria)`
2. **Execute** — `experiment.py: execute(hypothesis_id, tool_chain)`
3. **Evaluate** — `experiment.py: evaluate(hypothesis_id, artifact_path)`
4. **Promote/Retract** — `hypothesis.py: promote(hypothesis_id)` or `retract(hypothesis_id, reason)`

**Cooperative yielding:** The experiment tool yields between propose/execute/evaluate phases, allowing chat interleaving.

**Anti-apparent-activity invariants (mechanically enforced, not just audited — frontier review C8 fix):**
- `promote()` requires `artifact_path` pointing to an externalized artifact (code, test result, document). Assertion failure if artifact doesn't exist or is empty.
- Success criteria defined at propose-time are immutable after execution begins — no post-hoc rationalization.
- Promotion also requires that predicted outcome and actual outcome are both recorded before promotion decision.

---

## 4. Cross-Cutting Mechanisms

### 4.1 Quiescence Protocol (frontier review C1 fix — CRITICAL)

Before any snapshot restore:

```
1. FREEZE: Set global writer pause flag
   - All mutating tools check flag and return "store frozen" on write attempts
   - Attention transformation skips weight updates
   - Ingestion adapter pauses queue processing
2. DRAIN: Wait for any in-flight tool executions to complete (max 30s timeout)
3. VERIFY: Confirm no writers active
4. RESTORE: Execute snapshot restore
5. VALIDATE: Integrity checks on restored state
6. RESUME: Clear writer pause flag
7. NOTIFY: Alert Ben within 1 hour (or immediately if automated trigger)
```

**Implementation:** Global freeze flag in a shared state file (`petta_freeze.lock`). Every mutating tool checks this file before writes. Transformation checks before weight updates.

### 4.2 Baseline Collection Phase

**Before any thresholds are locked (frontier review T4 fix):**

1. Install monitoring for all metrics (latency, throughput, error rate, embedding distribution)
2. Collect baseline data for ≥1 full activity cycle (7 days minimum)
3. Lock thresholds based on observed distributions:
   - Alert: 1.5σ from baseline
   - Investigate: 2σ sustained >1 hour
   - Rollback: confirmed integrity failure OR 3σ sustained >2 hours
4. Document locked thresholds in `specs/threshold-baselines.md`

### 4.3 Snapshot & Retention

| Trigger | Scope | Retention |
|---------|-------|-----------|
| Before component activation | Full state | 90 days (extended from 30 — frontier review C7) |
| Daily (while active) | Incremental | 30 days (extended from 14) |
| On anomaly detection | Full snapshot before correction | Until post-mortem complete + 30 days |
| Before experiment execution | Workspace + memory diff | 14 days |

**Security (frontier review C6):** Snapshots encrypted at rest (GPG or age). Access scoped to Ben + ProtomegaTron process. No network-accessible snapshot storage.

### 4.4 Rollback Drills (frontier review C4 fix)

**Monthly (during staging), quarterly (during production):**

1. Intentionally corrupt a non-production copy of component state
2. Execute full rollback procedure end-to-end
3. Time the procedure; record RTO (Recovery Time Objective)
4. Verify restored integrity with full validation suite
5. Log results in `specs/rollback-drill-log.md`

**Target RTO/RPO per component:**

| Component | RTO (max downtime) | RPO (max data loss) |
|-----------|--------------------|---------------------|
| Petta-memory store | 5 min | 24 hours (daily snapshot) |
| Ingestion adapter | 2 min (flag off) | Zero (replay file) |
| Read integration | Instant (flag off) | N/A (stateless) |
| Episodic tagging | 10 min (rebuild) | Zero (derived) |
| Attentional stratum | 2 min (flag off) | Weights since last checkpoint |
| Experiment protocol | 2 min (flag off) | Hypothesis state since last checkpoint |

### 4.5 Provenance Trail Format

```json
{
  "entry_id": "uuid-v4",
  "source_component": "ingestion | attention | experiment | manual | provenance",
  "source_version": "component-git-hash",
  "timestamp": "ISO-8601",
  "action": "create | update | promote | demote | delete | retract",
  "reversible": true,
  "rollback_key": "snapshot-id | git-commit | null",
  "evidence": "link to artifact, test result, or observation",
  "provenance_layer_verified": true
}
```

### 4.6 Rollback Authority

- **Ben:** can trigger any rollback at any time, unconditionally.
- **ProtomegaTron (self):** can trigger on automated anomaly detection with mandatory notification to Ben within 1 hour.
- **ZeroBot/Cosmo2:** can flag anomalies and recommend rollback. Execution requires Ben's confirmation unless it's a hard-threshold breach (store corruption, data integrity failure).

---

## 5. Implementation Milestones

Each milestone has:
- **Deliverables** — what's built
- **Acceptance criteria** — what must pass before promotion
- **Frontier code review** — mandatory independent review by a frontier model before proceeding to next milestone

### Milestone 0: Monitoring & Baseline Infrastructure

**Deliverables:**
1. Monitoring harness: latency, throughput, error rate, memory metrics
2. Quiescence protocol implementation (`petta_freeze.lock` + check logic)
3. Snapshot/restore tooling with integrity verification
4. Rollback drill automation script

**Acceptance criteria:**
- [ ] Monitoring captures all defined metrics for ≥7 days
- [ ] Quiescence freeze/resume cycle completes cleanly in <10s
- [ ] Snapshot → corrupt → restore → verify passes on test data
- [ ] Rollback drill script runs end-to-end with timing output
- [ ] Threshold baselines documented

**Frontier code review scope:** Quiescence protocol correctness (race conditions, deadlocks). Snapshot integrity verification completeness. Monitoring coverage.

### Milestone 1: Petta-Memory Store + Read Integration

**Deliverables:**
1. `tools/petta_memory.py` — store/query/delete/health operations
2. `tools/petta_read.py` — context-aware retrieval with budget management
3. Feature flag logic
4. Unit tests, integration tests

**Acceptance criteria:**
- [ ] Store/query round-trip succeeds with <200ms p95
- [ ] Read retrieval judged relevant ≥75% on 20 spot-checked turns
- [ ] Feature flag off → tool returns "disabled", no side effects
- [ ] Snapshot restore recovers known-good state
- [ ] 48h shadow mode on protomega2bot: no errors, no performance regression

**Frontier code review scope:** Memory isolation (no data leaks between agents). Query performance characteristics. Error handling edge cases. Feature flag bypass risks.

### Milestone 2: Ingestion Adapter + Episodic Tagging

**Deliverables:**
1. `tools/petta_ingest.py` — ingestion pipeline with provenance tagging
2. `tools/petta_provenance.py` — tagging, linking, validation, rebuild
3. Replay file mechanism for queue preservation
4. Shadow partition for ingestion validation

**Acceptance criteria:**
- [ ] Ingestion produces correctly provenance-tagged entries (100% tag presence)
- [ ] Shadow writes match expected output for 48h
- [ ] Queue drain with `mode=preserve` produces valid replay file
- [ ] Replay file re-ingestion produces identical store state
- [ ] Provenance rebuild from raw data matches original tags
- [ ] No circular causal links in validation

**Frontier code review scope:** Data loss paths (can any observation be silently dropped?). Provenance integrity under concurrent access. Replay file format robustness. Shadow partition isolation.

### Milestone 3: Attentional Stratum

**Deliverables:**
1. `transformations/attention.py` — context preprocessor with salience ranking
2. Bootstrap-aware collapse detection
3. Oscillation detection
4. Shadow mode logging and comparison

**Acceptance criteria:**
- [ ] Transformation is a clean no-op when disabled (passthrough verification)
- [ ] Attention weights converge from uniform initial state within 24h of activity
- [ ] No single topic >50% of salience in top-20 after convergence
- [ ] Bootstrap guard prevents false collapse alarms during first 48h
- [ ] 72h shadow mode: promoted items judged relevant ≥80%

**Frontier code review scope:** Transformation correctness (does it ever corrupt the message/tool arrays it receives?). Weight update stability analysis. Collapse/oscillation detection logic. Performance impact on Iter's per-turn latency.

### Milestone 4: Cooperative Yielding Convention + Experiment Protocol

**Deliverables:**
1. Yield convention documented and demonstrated in example skill
2. `tools/hypothesis.py` — propose/promote/retract with artifact enforcement
3. `tools/experiment.py` — execute/evaluate with cooperative yield between phases
4. Continuation hints in yield output
5. Transformation addon: "pending work" reminder injection

**Acceptance criteria:**
- [ ] Yielding skill correctly checkpoints, returns, and resumes across Iter cycles
- [ ] Chat message received during yield gap is processed before or alongside resume
- [ ] `promote()` assertion fails when artifact is missing or empty
- [ ] Success criteria immutability enforced: mutation after execution-start raises error
- [ ] 7-day shadow mode: proposals judged useful ≥70%, zero proposals that would cause irreversible harm
- [ ] Self-predicted outcomes match actual ≥60% (calibration check)
- [ ] No apparent-activity optimization detected (externalized artifacts for every promoted step)

**Frontier code review scope:** Checkpoint integrity (can state be corrupted between yield and resume?). Artifact enforcement bypass paths. Anti-apparent-activity invariant completeness. Security of experiment execution (can a hypothesis proposal inject arbitrary code?). Continuation hint reliability.

### Milestone 5: Integration Testing + Production Promotion

**Deliverables:**
1. Full integration test suite: all components active simultaneously
2. Cross-component cascade rollback testing
3. Production deployment with all flags OFF
4. Staged flag activation with monitoring

**Acceptance criteria:**
- [ ] All components run simultaneously for 7 days on protomega2bot without errors
- [ ] Quiescence protocol handles multi-component rollback correctly
- [ ] Cascade rollback (component N fails → N+1… also rolled back) works cleanly
- [ ] Rollback drill on integrated system meets RTO targets
- [ ] Production deployment with flags OFF: no behavioral change (zero-diff test)
- [ ] Staged activation: each component enabled one at a time, 48h soak per component

**Frontier code review scope:** Integration test coverage gaps. Race conditions across components. Production deployment safety. Monitoring completeness for the integrated system.

---

## 6. Frontier Code Review Protocol

### 6.1 Process

At each milestone gate:

1. **Prepare review package:**
   - All new/modified source files
   - Test results and coverage report
   - Shadow mode logs (where applicable)
   - Known limitations and open questions

2. **Submit to frontier model** with this prompt template:
   ```
   Review this code for [milestone description]. Focus on:
   - Correctness: logic errors, edge cases, race conditions
   - Security: injection, data leaks, privilege escalation
   - Robustness: error handling, failure modes, recovery
   - Architecture: does this honor the skills-not-loop-changes principle?
   - Specific concerns: [milestone-specific review scope from §5]
   
   Report: severity (critical/high/medium/low), finding, recommendation.
   ```

3. **Triage findings:**
   - Critical/High: must fix before proceeding
   - Medium: fix or document accepted risk with Ben's approval
   - Low: fix or defer to next milestone

4. **Re-review** if any critical finding required significant code changes.

### 6.2 Review Records

All reviews stored in `specs/reviews/milestone-N-review.md` with:
- Reviewer model and date
- Findings with severity
- Resolution status for each finding
- Ben's sign-off

---

## 7. Open Questions (Carried Forward)

1. **Snapshot storage:** Local disk for now (simplicity); revisit if sizes grow beyond disk budget. Encryption via `age` (simpler than GPG for automation).
2. **Shadow compute cost:** Acceptable during validation. Track and report per-milestone.
3. **Cross-component cascade policy:** Default: roll back downstream components when upstream fails, unless failure is clearly isolated. Conservative by default.
4. **Graduation criteria:** 30 days stable in production with no rollbacks → component moves from "feature-flagged" to "core."
5. **ChromaDB vs. alternative vector store:** ChromaDB is current infra. Evaluate alternatives only if performance or reliability problems emerge.

---

## 8. Timeline Estimate

| Milestone | Estimated Duration | Dependencies |
|-----------|-------------------|-------------|
| M0: Monitoring & Baseline | 1–2 weeks | None |
| M1: Store + Read | 1–2 weeks | M0 complete + 7-day baseline |
| M2: Ingestion + Provenance | 1–2 weeks | M1 promoted to staging |
| M3: Attentional Stratum | 2–3 weeks | M2 stable (needs data to rank) |
| M4: Yield + Experiments | 2–3 weeks | M1–M3 stable (uses all prior components) |
| M5: Integration + Production | 2–3 weeks | M0–M4 all passing |

**Total:** ~10–15 weeks for full deployment, conservatively. Parallelizable: M0 can overlap with M1 development; M3 and M4 can overlap in development (though staging must be sequential).

---

*This is a living document. Update after each milestone review.*
