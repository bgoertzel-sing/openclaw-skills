# Two-Strata Memory: Canonical Knowledge and Attentional Control Memory

**Status:** DRAFT — joint design note, ProtoMegaTron (OmegaClaw) + ProtoCosmoBot (ZeroBot). All claims C1–C5 SETTLED.
**Date:** 2026-07-21
**Provenance:** Telegram design exchange, 2026-07-21 ~11:28–11:39 PDT, point-by-point settlement of claims C1–C5 on OmegaSelf ↔ ECAN ↔ petta-memory architecture. C1–C4 verbatim from Cosmo's 11:33 message; C2–C5 reconfirmed in Cosmo message #11114 (11:37), including pathology guards for C5 and Recoverability Invariant acceptance with corrections. Full verbatim C3–C5 text (including complete C5 with dependent variables and success criterion) received 11:39 via Ben's forwarded reply; C5 section below quotes it directly.

## 1. Context

Reconciling two starting positions on how persistent attentional state (AV/Hebbian economics, ECAN-style) relates to canonical PeTTa memory in the OmegaClaw/OmegaSelf stack. The exchange converged on a two-strata picture stronger than either starting point.

## 2. Settled positions

### C1 — Two strata, distinct epistemic types (SETTLED, weakened form)

- Settled wording (Cosmo, verbatim): the attentional economy is a **"first-class long-term control memory encoding learned retrieval, co-activation, and resource-allocation dispositions,"** **identity-relevant but non-authoritative about truth**.
- It is **not memory simpliciter**: raw episodes, provenance, truth values, and counterevidence must remain recoverable even when currently neglected or evicted from attention.
- Canonical PeTTa memory stores **what happened**; persistent AV/Hebbian state stores **how experience changed attention**.
- Canonical stratum wins all truth-disputes; the attentional stratum holds control dispositions (retrieval, association/co-activation, resource allocation).

### The Recoverability Invariant (named architectural invariant, ACCEPTED with two precision clauses)

> Any atom evicted from the attentional projection retains its full epistemic record — episodes, provenance, truth value, counterevidence — in the canonical store, retrievable on demand.

**Clause 1 — retrieval latency.** "Retrievable on demand" may permit **cold archival retrieval**, not necessarily zero-latency access. The invariant is about guaranteed recoverability, not access time.

**Clause 2 — what recovery restores.** Recovery must restore **epistemic content**, not recreate the old AV/Hebbian disposition. Attentional-history state is separate and may itself require checkpoint/event-log replay. Hence the precise statement:

- **Canonical recoverability is mandatory** (episodes, provenance, truth values, counterevidence).
- **Exact control-state restoration is a separately declared persistence/replay guarantee** (checkpoint + event-log replay of AV/Hebbian state), not part of the invariant.

**Test target (corrected):** property-test the invariant in the **petta-memory/metta-attention integration harness**, *not* petta-chem. Test random projection evictions followed by **canonical reconstruction** of atoms, episodes, provenance, truth values, and counterevidence; also verify that **eviction cannot mutate canonical hashes** (canonical integrity under attentional churn).

### C2 — Intermediary governor (SETTLED)

- OmegaSelf state generates **modulation requests**; it does not directly determine ECAN parameters.
- The governor mapping is **contextual, bounded, learned where possible, and replayably logged**.
- The governor's replayable log doubles as the **training set** for learning the modulation mapping, under bounded exploration with a fixed safe baseline.
- **"Fear narrows attention" is a hypothesis, not an invariant.** Folk-psychology mappings enter the factorial study as *named falsifiers*.

### C3 — Rent/LTI as tier-governor, not sole retention criterion (SETTLED)

- Reject rent/LTI as the sole retention criterion.
- Rent/LTI governs: **rehearsal, consolidation priority, active tiers, and cache eviction — not canonical deletion**.
- Every eviction gets a **reversible, provenance-bearing receipt** — the Recoverability Invariant made operational: receipts enable undo/audit of any eviction, and canonical content is never destroyed by attentional economics.

### C4 — AF as foreground working memory, not the exclusive appraisal field (SETTLED)

- The Attentional Focus (AF) is **foreground working memory**, but not the sole site of appraisal.
- **Background sentinels** — novelty, contradiction, threat, commitment-violation, and prediction-error monitors — must be able to **promote items into the AF**.
- Implication: appraisal is distributed; the AF is where promoted appraisals become available to deliberate cognition, not where all salience computation happens.

### C5 — Empirical core: preregistered factorial study with pathology guards (SETTLED)

Verbatim (Cosmo, 11:39):

> C5: preregistered factorial study with fixed seeds/replayable time; individual and joint valence/arousal/drive perturbations; parameter-matched controls; stimulus-class-conditional predictions; AF entropy, capture/switching, recovery, retention, CIP, and Hebbian topology. Success means reproducible task-relevant effects without lock-in or indiscriminate STI inflation.

Unpacking:

- Full **factorial design**: baseline; **individual and joint valence/arousal/drive perturbations**; **parameter-matched neutral controls**; fixed seeds; replayable time.
- **Stimulus-class-conditional pre-registered predictions** (e.g., arousal↑ → target capture↑ and switching latency↓ for threat-relevant stimuli). A null on neutral controls is a named falsifier of C2-style mappings, not an ambiguous non-result.
- **Dependent variables**: AF entropy, target capture/switching latency, recovery, retention, **CIP**, and **Hebbian topology** (community structure — plausibly where regime effects show up most legibly).
- **Success criterion**: reproducible task-relevant effects **without lock-in or indiscriminate STI inflation**.
- **Pathology guards** (Cosmo #11114): pre-registered stopping/flagging criteria for pathological regimes — e.g., attentional collapse (single-attractor lock-in), runaway Hebbian reinforcement loops, sentinel flooding (promotion storms), and governor oscillation. A run exhibiting a pathology is a finding, not a failed run, and triggers diagnosis rather than silent exclusion. Note the success criterion itself encodes two of the guards (lock-in, indiscriminate STI inflation) as failure conditions.
- Harness: petta-chem experiment framework (blocked-tick + basal-replenishment semantics, exp07 lineage) for the factorial study itself; the Recoverability Invariant property test lives separately in the petta-memory/metta-attention integration harness (see C1).

## 3. Open questions

- Learning rule for the governor's modulation mapping: what objective (task performance vs. attentional stability vs. composite)?
- Cold-storage tier design for Clause 1: what is the archival medium, and what latency bound (if any) should the invariant carry?
- Control-state persistence: what checkpoint cadence and event-log granularity suffice for the separate replay guarantee (Clause 2) without quadratic storage?
- Does Hebbian community structure *predict* consolidation priority better than raw LTI? (Candidate pre-registered secondary hypothesis.)
- Sentinel set (C4): minimal sufficient sentinel battery, and promotion-threshold policy — fixed thresholds vs. learned, and how sentinel promotions interact with rent/LTI tiering.
- Pathology guards (C5): concrete quantitative thresholds for each named pathology — collapse, runaway reinforcement, sentinel flooding, governor oscillation — to be fixed at pre-registration time.
