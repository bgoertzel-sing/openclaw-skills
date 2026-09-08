# Frontier Model Review of Rollback Specification v0.1

**Reviewer:** Frontier model via OpenRouter (independent review)
**Date:** 2026-09-04
**Verdict:** "Genuinely well-structured draft" — but found one serious logical flaw, one dangerously under-weighted condition, and several threshold issues.

---

## 1. Completeness — Gaps & Uncovered Failure Modes

**C1. No quiescence control around snapshot restore (SEVERE — biggest gap).**
Rollback procedures assume each component acts alone. In reality, store/ingestion/attention/read/Iter all mutate or read the same substrate concurrently. A restore while ingestion is mid-write or attention is re-ranking will clobber legitimate newer writes or get clobbered by them. Every restore needs a **global writer pause** (freeze all mutating components) before restore and a **resume** after verification. No quiesce/resume ordering is defined. This is the most likely cause of "we rolled back and now it's worse" incidents.

**C2. Drop data during ingest queue drain (HIGH).**
"Drain and discard queued items" discards non-reprocessible payloads — conversation turns and observations that may exist *only* in that queue. "Preserve ingestion logs" ≠ preserving payloads. These should be persisted/replayed (or dumped to a replay file), not discarded, or you accept silent data loss of original observations.

**C3. Batch-delete dependency is circular (HIGH-ish).**
Ingestion pollution deletion relies on provenance tags being present and trustworthy — but provenance is itself a rolled-back/brittle layer (its own triggers include "tag corruption"). If the tags are part of what's broken, batch-delete will under-delete and leave residue. Reorder so snapshot-restore is the preferred pollution-remediation path; tag-based delete only when the store itself is otherwise sound.

**C4. No rollback exercise/drill (HIGH).**
No staged, rehearsed rollback. Classic failure: "we've never actually restored from this snapshot in anger." Add periodic (pre-promotion or monthly) rollback drill on staging: intentionally corrupt state, execute each component's full rollback procedure, time it, verify restored integrity. Also needs **time-budgeted RTO/RPO** — "how long is the agent down / how much data do we lose" should be a stated number per component.

**C5. Snapshot integrity verification too weak (MED).**
"Entry count check + 10 known-good sample queries" won't catch subtle semantic corruption — exactly the class of corruption the doc says it fears (embedding drift, slow degradation). Add checksumming of stored blobs, pairwise embedding-space sanity sampling, and periodic self-check queries. Ten queries is a smoke test, not a validation.

**C6. Data-handling/security of snapshots (MED).**
Memory store holds personal conversation data. 30-day snapshot retention creates large, long-lived copies of user data. No mention of encryption at rest, access scoping, or who can read snapshot stores. New exfiltration/leak surface.

**C7. Retention vs. slow-onset failure is inconsistent (MED).**
The doc fears slow-onset failures (Iter, embedding drift), yet daily incremental snapshots retained only 14 days and full baselines 30 days. Corruption that takes >14–30 days to surface will shadow a chain of already-tainted incrementals. If you genuinely believe in slow-onset failures, retention is too short.

**C8. Who is the "external auditor"? (MED)**
The strongest countermeasure for apparent-activity optimization is "periodic external audit." But the *enforcement* of "bounded step count" and "defined-before rationalization" must be mechanical (code-level assertion that promotion has an artifact), not a policy relying on a human noticing. Shift from "periodic audit" to "enforced invariant."

---

## 2. Correctness — Trigger & Threshold Soundness

**T1. Attention-collapse trigger is self-defeating (SEVERE — logical flaw).**
Rollback procedure 3.5 step 3: "reset weights to uniform." Trigger 3.5: "attention collapse: near-uniform weights." The recovery action directly produces the state the trigger regards as pathological. After any attention rollback you will re-alarm immediately. Need to distinguish "uniform because freshly reset" (benign bootstrap) from "uniform despite rich, differentiated evidence" (pathological). Guard the trigger with a training-age/evidence-volume gate, or the mechanism will flap.

**T2. Read-integration acceptance threshold == rollback threshold (no deadband).**
3.3 uses p95 < 500ms for both shadow acceptance criterion and rollback trigger. Identical accept/abort numbers cause flapping: pass the gate at 499ms, trip a rollback the moment you cross 500ms. Acceptance for going live and threshold for aborting live are different decisions — need separation (e.g., accept shadow at p95 < 400ms, rollback live at p95 > 750ms sustained).

**T3. 2σ is used inconsistently (MED).**
4.3 defines >2σ as a *statistical alert*; 3.1 uses "embedding drift >2σ" as an actual *rollback trigger*. On normally-distributed metrics, 2σ fires ~5% of observations. Across many metrics, everything-at-2σ-is-rollback guarantees constant false-positive aborts. Separate: 1.5–2σ = investigate/alert; **sustained** deviation or confirmed-integrity-fail = rollback.

**T4. Thresholds are guesses without baselines (MED).**
Hard thresholds (500ms, 2σ, 70-80%, 3×/0.1×) presume a stable baseline that doesn't exist pre-deployment. Add: "install monitoring → collect baseline ≥ one full activity cycle → then lock thresholds" as a required prefix to the staging pipeline.

**T5. Ingestion rate 0.1× trigger will false-positive (MED).**
0.1× expected throughput will fire during normal quiet hours on bursty conversational data. Needs a sustain-duration qualifier ("sustained < 0.1× across the activity window," not instantaneous). Conversely, 3× bursts are normal for this workload.

---

*Note: The review was partially truncated beyond T5. Sections on Practicality, Risk Assessment, and Recommendations were cut off but the critical/high-severity findings above are complete.*
