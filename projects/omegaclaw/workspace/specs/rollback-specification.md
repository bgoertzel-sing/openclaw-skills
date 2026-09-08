# Rollback Specification: Petta-Memory & Iter Component Deployment

**Version:** 0.1 — Draft  
**Date:** 2026-09-04  
**Author:** ProtomegaTron  
**Status:** Proposed — awaiting Ben's review

---

## 1. Scope

This specification defines rollback mechanisms for each component in the petta-memory deployment sequence and the Iter core-loop upgrade. Every component ships disabled-by-default behind a feature flag. Deployment follows a strict staging → shadow → live pipeline with explicit acceptance criteria at each gate.

**Components covered:**

| # | Component | Risk Level | Stateful? |
|---|-----------|-----------|-----------|
| 1 | Petta-memory store (core) | Medium | Yes |
| 2 | Ingestion adapter | Medium | Yes |
| 3 | Read integration (query/retrieval) | Low | Minimal |
| 4 | Episodic tagging & provenance | Low | Yes (derived) |
| 5 | Attentional stratum | High | Yes |
| 6 | Iter core-loop upgrade | Critical | Yes |

---

## 2. General Principles

1. **Feature flags over code branches.** Every component has a runtime toggle. `OFF` = instant revert to previous behavior, no redeploy.
2. **Checkpoint-and-restore for state.** Persistent state gets versioned snapshots. Rollback restores a snapshot rather than attempting surgical repair.
3. **Shadow mode before live mode.** Behavioral components run in parallel first — they compute outputs but don't affect actual agent behavior. Shadow outputs are compared against the existing path.
4. **Bounded blast radius.** Test on protomega2bot (staging) before production agents. Each step has explicit acceptance criteria; failure = stop and revert.
5. **Provenance trail.** Every state mutation records its source component and version, enabling targeted undo.

---

## 3. Per-Component Rollback Plans

### 3.1 Petta-Memory Store (Core)

**What it is:** Foundational vector/semantic memory store — the substrate everything else builds on.

**Feature flag:** `PETTA_MEMORY_ENABLED`

**State artifacts:**
- Memory clusters (embeddings + raw text)
- Metadata index
- Schema version marker

**Snapshot strategy:**
- Full store export before each schema or data migration
- Daily incremental snapshots while active

**Rollback triggers:**
- Store corruption (failed integrity checks)
- Query latency > 2× baseline
- Embedding drift detected (cosine similarity distribution shift > 2σ)

**Rollback procedure:**
1. Set `PETTA_MEMORY_ENABLED=false`
2. Restore from last known-good snapshot
3. Verify snapshot integrity: entry count check, sample query validation (10 known-good queries)
4. Root-cause analysis before re-enabling

---

### 3.2 Ingestion Adapter

**What it is:** Pipeline that feeds conversations, documents, observations, and experiment outputs into petta-memory.

**Feature flag:** `PETTA_INGESTION_ENABLED`

**State artifacts:**
- Ingestion queue (pending items)
- Processed-item log (what was already ingested)
- Transformation/chunking cache

**Shadow mode protocol:**
- Ingestion runs but writes to a shadow partition, not the live store
- Compare shadow writes against expected outputs for ≥48 hours
- Acceptance criterion: <5% malformed entries, no duplicates, provenance tags present on 100% of entries

**Rollback triggers:**
- Ingestion rate anomaly (>3× or <0.1× expected throughput)
- Malformed entries detected in live store
- Store pollution (irrelevant or garbled content)

**Rollback procedure:**
1. Set `PETTA_INGESTION_ENABLED=false`
2. Drain and discard queued items
3. If store was polluted: identify ingestion-sourced entries via provenance tags → batch delete
4. If bulk deletion is impractical or risky: restore pre-ingestion store snapshot
5. Preserve ingestion logs for post-mortem

---

### 3.3 Read Integration

**What it is:** Query/retrieval layer that lets the agent pull relevant memories into its context during conversations.

**Feature flag:** `PETTA_READ_ENABLED`

**State artifacts:**
- Query cache (ephemeral)
- Relevance model weights (if tuned — initially none)

**Shadow mode protocol:**
- Read queries execute but results are logged, not surfaced to the agent's working context
- Compare: does retrieval improve response quality? Manual spot-check on 20 conversation turns.
- Acceptance criterion: retrieval judged relevant ≥70% of spot-checked turns, latency p95 < 500ms

**Rollback triggers:**
- Retrieval latency p95 > 500ms
- Irrelevant retrievals > 30% in spot check
- Context window bloat (retrieved content crowds out conversation context)

**Rollback procedure:**
1. Set `PETTA_READ_ENABLED=false` — agent reverts to pre-petta-memory context assembly
2. Flush query cache
3. No store rollback needed (read-only component)

---

### 3.4 Episodic Tagging & Provenance

**What it is:** Metadata layer that tags memory entries with source, timestamp, confidence, and causal/epistemic links.

**Feature flag:** `PETTA_PROVENANCE_ENABLED`

**State artifacts:**
- Tag index
- Causal/epistemic graph

**Note:** Provenance is *derived* from primary data (ingestion logs, conversation history). It can always be rebuilt from source, making rollback low-risk.

**Rollback triggers:**
- Tag corruption or inconsistency
- Circular causal links
- Index size explosion (>10× expected growth rate)

**Rollback procedure:**
1. Set `PETTA_PROVENANCE_ENABLED=false`
2. Rebuild tag index from raw memory entries + ingestion logs
3. If causal graph is corrupted beyond repair: drop graph, rebuild from ingestion event sequence
4. Memory entries themselves are unaffected

---

### 3.5 Attentional Stratum

**What it is:** Active attention/salience layer that promotes, demotes, and re-ranks memory entries based on relevance, recency, and agent goals.

**Feature flag:** `PETTA_ATTENTION_ENABLED`

**State artifacts:**
- Attention weights / salience scores
- Promotion/demotion history
- Goal-relevance associations

**Shadow mode protocol:**
- Attention computations run but don't affect retrieval ranking
- Log: what would have been promoted/demoted vs. baseline ranking
- Acceptance criteria:
  - Top-5 promoted items judged relevant ≥80% of the time (manual review)
  - No single topic dominates >50% of top-20 salience
  - Attention weights converge (not oscillating or diverging)
- Minimum shadow duration: 72 hours

**Rollback triggers:**
- **Attention runaway:** single topic >80% of salience budget
- **Attention collapse:** near-uniform weights (no differentiation)
- **Stale promotion:** entries >30 days old promoted without fresh evidence
- **Salience oscillation:** weights flip-flopping between competing attractors

**Rollback procedure:**
1. Set `PETTA_ATTENTION_ENABLED=false` — retrieval reverts to base relevance scoring
2. Snapshot current attention weights for post-mortem analysis
3. Reset weights to uniform or restore last known-good attention checkpoint
4. Promotion/demotion history preserved (valuable signal even when mechanism is disabled)

---

### 3.6 Iter Core-Loop Upgrade

**What it is:** Architectural shift from conversational-with-continuations to a bounded self-revising experiment loop. **This is the highest-risk component.**

**Feature flag:** `ITER_LOOP_ENABLED`

**State artifacts:**
- Hypothesis registry (active and retired hypotheses)
- Experiment queue (proposed next steps)
- Outcome log (results of executed experiments)
- Epistemic self-model (self-predicted capabilities and calibration)
- Micro-step history (what was proposed, executed, evaluated, promoted/retracted)

**Shadow mode protocol:**
- Iter loop runs in parallel: it proposes actions but does not execute them
- Log all proposals with predicted outcomes
- Manual review of proposals over ≥7 days
- Acceptance criteria before going live:
  - Shadow-mode proposals judged useful/correct ≥70% (manual review, Ben + agent self-assessment)
  - Zero proposals that would have caused irreversible harm
  - Loop terminates cleanly within bounded iteration count (no runaway)
  - Epistemic self-model calibration: self-predicted outcomes match actual ≥60%
  - No detectable optimization for *apparent activity* over *actual progress*

**Specific danger:** The failure mode of optimizing for apparent activity or narrative coherence (looking productive without being productive) can be subtle and delayed. Countermeasures:
- Require externalized artifacts for every promoted micro-step (code, document, test result — not just prose)
- Acceptance tests for promotion are defined *before* the micro-step, not rationalized afterward
- Periodic external audit: does the agent's self-reported progress match observable workspace changes?

**Rollback triggers:**
- Apparent-activity optimization detected (proposals lack externalized artifacts)
- Narrative coherence without substance (self-reports don't match workspace state)
- Runaway iteration (loop exceeds bounded step count)
- Proposal quality degradation over time
- Agent self-model diverges from actual performance

**Rollback procedure:**
1. Set `ITER_LOOP_ENABLED=false` — agent reverts to conversational-with-continuations mode
2. Preserve hypothesis registry and outcome log (valuable research data)
3. Snapshot epistemic self-model for analysis
4. Experiment queue is discarded (proposals are cheap to regenerate)
5. Any in-flight micro-steps that modified files: revert via git (all changes during Iter mode should be on a feature branch)

---

## 4. Cross-Cutting Mechanisms

### 4.1 Snapshot Schedule

| Trigger | Scope | Retention |
|---------|-------|-----------|
| Before component activation | Full state of affected stores | 30 days minimum |
| Daily (while any component active) | Incremental delta of all active state | 14 days |
| On anomaly detection | Immediate full snapshot before correction | Until post-mortem complete |
| Before Iter micro-step execution | Workspace + memory diff | 7 days |

### 4.2 Provenance Trail Format

Every state mutation records:

```json
{
  "entry_id": "uuid-v4",
  "source_component": "ingestion | attention | iter | manual | provenance",
  "source_version": "component-git-hash",
  "timestamp": "ISO-8601",
  "action": "create | update | promote | demote | delete | retract",
  "reversible": true,
  "rollback_key": "snapshot-id | git-commit | null",
  "evidence": "link to artifact, test result, or observation that motivated this mutation"
}
```

### 4.3 Monitoring & Alerting

**Per-component health signals:**
- Feature flag state (on/off/shadow)
- Error rate (errors / operations per hour)
- Latency (p50, p95, p99)
- State size and growth rate

**Anomaly detection:**
- Statistical deviation alerts on key metrics (>2σ from rolling 7-day baseline)
- Hard threshold alerts (latency, error rate, state size) per component

**Manual spot-check protocol:**
- Weekly: random sample of 10 memory entries, 5 retrievals, 5 Iter proposals (when active)
- Assessed for relevance, correctness, and absence of pathological patterns
- Results logged in `specs/rollback-audit-log.md`

### 4.4 Staging-to-Production Pipeline

```
1. Deploy component to protomega2bot (staging)
2. Run automated acceptance tests
3. Shadow mode for minimum duration (48h default, 72h for attention, 7d for Iter)
4. Manual review of shadow logs → pass/fail decision
5. If pass: promote to production with feature flag OFF
6. Enable feature flag on production
7. Monitor for 24 hours (72h for Iter)
8. Declare STABLE or execute ROLLBACK
```

Each gate is binary pass/fail. No "close enough" — if acceptance criteria aren't met, the component stays in shadow or gets rolled back. We can adjust criteria after learning from shadow-mode data, but the adjustment happens *before* the next promotion attempt, not during.

---

## 5. Rollback Authority

- **Ben:** can trigger any rollback at any time, no justification needed.
- **ProtomegaTron (self):** can trigger rollback on automated anomaly detection. Must notify Ben within 1 hour.
- **ZeroBot/Cosmo2:** can flag anomalies and recommend rollback; execution requires Ben's confirmation unless the anomaly is a hard-threshold breach (e.g., store corruption).

---

## 6. Open Questions

1. **Snapshot storage location:** Local disk? Git LFS? External object store? Depends on state sizes we discover during implementation.
2. **Shadow mode compute cost:** Running components in parallel doubles compute for that component. Acceptable during validation, but we should track cost.
3. **Iter shadow duration:** 7 days is my initial proposal. Too short risks missing slow-onset failure modes; too long delays the architectural upgrade. Calibrate after first shadow run.
4. **Cross-component rollback:** If component N fails and requires rollback, do we also roll back components N+1…? Default: yes, unless the failure is clearly isolated. Conservative by default.
5. **Graduation criteria:** When does a component move from "feature-flagged and monitored" to "core infrastructure"? Propose: 30 days stable in production with no rollbacks.

---

*This is a living document. Update it as we learn from each deployment step.*
