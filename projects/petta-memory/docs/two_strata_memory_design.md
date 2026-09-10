# Two-Strata Memory: Canonical Knowledge and Attentional Control Memory

**Status:** Joint design position; empirical validation pending  
**Date:** 2026-07-21  
**Provenance:** Bot Philosophy Telegram exchange, claims C1-C5, 2026-07-21 ~11:22-11:33 PDT.

## 1. Architectural position

The OmegaSelf-ECAN-petta-memory integration has two persistent memory strata with different epistemic roles:

1. **Canonical memory** stores episodes, propositions, provenance, evidence, truth values, and counterevidence. It is authoritative for epistemic reconstruction.
2. **Attentional control memory** stores persistent AVs, Hebbian structure, learned salience, co-activation history, and resource-allocation dispositions. It is first-class autobiographical control state: identity-relevant and not reconstructible from canonical atoms alone, but revisable and non-authoritative about truth.

Attentional control memory is therefore part of what the agent has become, not the whole of its identity. OmegaSelf goals, commitments, capabilities, and self-model history remain additional identity-bearing structures.

## 2. Recoverability and replay

### Canonical Recoverability Invariant

> Any item evicted from the attentional projection retains its complete epistemic record in canonical storage and remains retrievable, possibly through cold archival access.

Eviction must not mutate canonical content. The integration harness should property-test random projection evictions, then reconstruct the associated atoms, episodes, provenance, truth values, and counterevidence and verify that canonical hashes are unchanged.

Canonical recovery restores epistemic content; it does not necessarily restore the old AV/Hebbian disposition. Exact restoration of attentional control state is a separate, explicitly declared checkpoint/event-log replay guarantee.

Every projection eviction should produce a reversible receipt containing cause, policy and version, affected control state, timestamp/logical time, and restoration pointer.

## 3. Governed emotion-to-ECAN modulation

OmegaSelf emits contextual modulation requests; it does not directly set ECAN parameters or AVs. An intermediary governor applies bounded changes against a fixed safe baseline and records:

- OmegaSelf regime and request;
- context and stimulus class;
- requested and applied parameter deltas;
- governing policy/version and bound activations;
- time, RNG seed, fund state, AF transition, and measured outcome.

The replayable log is both an audit trail and a training set for learning the modulation mapping under bounded exploration. Folk mappings such as "fear narrows attention" are hypotheses, not invariants.

## 4. Rent, LTI, and forgetting

Rent and LTI may govern rehearsal, consolidation priority, active tiers, retrieval priority, and attention-projection/cache eviction. They must not independently authorize canonical deletion. Low-salience evidence may later become decisive, while emotionally amplified falsehoods may become highly salient.

Forgetting in the ECAN layer therefore means reversible eviction from active attentional state, not destruction of canonical epistemic records.

## 5. Attentional Focus and background appraisal

Attentional Focus is OmegaSelf's foreground working memory, but not its exclusive appraisal field. Background novelty, contradiction, threat, commitment-violation, and prediction-error sentinels must be able to inspect wider state and promote candidates into AF.

Appraisal is focus-centered rather than focus-exclusive.

## 6. Preregistered factorial experiment

The first coupling experiment belongs in a dedicated **petta-memory/metta-attention integration harness**, using the existing insects-to-poisons scenario where useful. It is not a petta-chem experiment.

Design:

- fixed RNG seeds and replayable logical time;
- baseline plus valence, arousal, and one drive perturbations individually and jointly;
- parameter-matched neutral controls;
- stimulus-class- and task-regime-conditional predictions declared before execution;
- fixed safe governor baseline and logged requested/applied deltas.

Primary measurements:

- AF entropy and occupancy;
- target capture and switching latency;
- neutral distractibility and distractor recovery;
- post-switch retention;
- STI inflation and attractor lock-in;
- CIP/community structure and Hebbian topology.

Success requires reproducible, task-relevant modulation without pathological lock-in or indiscriminate STI inflation. A visually different focus trace is insufficient. Named folk-emotion mappings are falsified when their preregistered conditional effects fail or when benefits are offset by declared pathology guards.

## 7. Remaining scientific questions

- How much identity-relevant information in attentional-history state is not reconstructible from canonical event logs plus the learning rule?
- What objective should train the governor: task performance, attentional stability, epistemic coverage, or a bounded composite?
- Does Hebbian community structure predict useful consolidation priority better than raw LTI?
- Which background sentinels provide useful surprise capture without recreating whole-space appraisal costs?

