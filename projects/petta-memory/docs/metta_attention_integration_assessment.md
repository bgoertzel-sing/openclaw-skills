# metta-attention integration assessment

Date: 2026-07-21

Status: source-based architectural assessment; no live integration authorized

Upstream: `https://github.com/iCog-Labs-Dev/metta-attention`

Pinned revision: `9196f38db749ddedeb591229dffddfa71664c38d`

## Executive view

`metta-attention` should be integrated as a derived, disposable cognitive-control
projection over petta-memory and OmegaSelf, not as canonical memory, a truth
store, or an authority mechanism.

Its obvious role is PLN inference control, but its broader value is substantial:

1. bounded retrieval and prompt-context selection;
2. memory consolidation and hot/warm/cold tier management;
3. episodic segmentation using Cognitive Integration Period snapshots;
4. discovery of associative communities and bridge concepts;
5. OmegaSelf discrepancy, continuity, and fragmentation monitoring;
6. a real actuator substrate for affective modulation;
7. experimental measurement of regenerative goal weaving;
8. attention-economy telemetry for cognitive health and resource allocation.

The strongest integration is therefore not `petta-memory + AV fields`. It is a
one-way projection and governed feedback loop:

```text
canonical petta-memory + OmegaSelf evidence
    -> versioned attention projection
    -> ephemeral ECAN state and Attentional Focus
    -> retrieval / PLN / consolidation / appraisal candidates
    -> policy governor
    -> bounded effects
    -> append-only receipts and outcome evidence
```

Truth values, attention values, authorization, and canonical status must remain
distinct types. Low attention must never make evidence false, and high attention
must never make a claim authoritative.

## Observed upstream capabilities

At the pinned revision the repository contains:

- a mutable `TypeSpace` associating atoms with `(STV ...)`, `(AV STI LTI VLTI)`,
  and importance bins;
- conserved global STI/LTI funds, stimulus wages, and rent collection;
- an Attentional Focus selected primarily by STI;
- importance diffusion through incident structure and learned Hebbian links;
- Hebbian-link creation and updating from co-activation;
- forgetting based on low LTI, VLTI, truth mean, size pressure, and incoming-link
  constraints;
- stochastic selection outside the Attentional Focus;
- a `synapse` layer with Cognitive Integration Period snapshots, attentional
  retention, resource/concentration/link-density metrics, Hebbian community
  detection, and clique-complex topology metrics (triangles and Betti numbers);
- an insect/poison/insecticide experiment intended to demonstrate attention
  shift, drift, and bridge-mediated association.

The latest GitHub Actions run for the pinned commit succeeded on 2026-07-20.
The workflow clones the current Patham9 PeTTa default branch rather than a pinned
revision, installs SWI-Prolog from a PPA, installs exact Python requirements, and
runs the repository test collector. The green run is useful compatibility
evidence, but not a reproducible semantic pin.

A local Python-only synapse test attempt did not start because `igraph` is not
installed in the host Python environment. No dependencies were installed for
this assessment. The repository declares `igraph==1.0.0` in its requirements.

## Where it fits in petta-memory

### 1. Retrieval scheduler

Compile each eligible canonical `MemoryCluster` or selected subrecord into a
stable attention proxy keyed by the petta-memory identifier. Stimulate proxies
from the current query, goal, evidence gap, task context, and recent use. Diffuse
STI across explicit `About`, provenance, support/opposition, supersession, goal,
and learned co-retrieval edges. Use the resulting AF as a candidate set for the
existing bounded prompt, audit, and PLN-safe views.

This is more expressive than the present salience/recency prompt ordering because
it can recover a coherent neighborhood and associative bridges. The existing
hard filters still apply after ECAN selection: epistemic role, promotion state,
status, provenance closure, and character/token budgets are not attention
decisions.

### 2. Consolidation without destructive forgetting

STI can represent immediate retrieval pressure. LTI can summarize repeated
usefulness across reviewed episodes. Hebbian associations can identify records
that are repeatedly useful together. These signals can nominate:

- clusters for semantic compression;
- repeated episode fragments for skill or ontology extraction;
- stale indexes for rebuilding;
- low-value hot-tier material for eviction from caches;
- high-value material for durable curation review.

The upstream forgetting agent must not delete canonical journal records. In the
petta-memory integration, forgetting means removal from the ephemeral attention
projection or a cache tier. Canonical retirement remains an append-only status or
supersession event governed by petta-memory policy.

VLTI must not mean authorization, constitutional protection, or truth. At most it
is a retention hint. Policy-protected records are protected by explicit policy
and immutable provenance, not an attention scalar that emotional or Hebbian
dynamics can modify.

### 3. Episodic boundaries and context reconstruction

The upstream `synapse.metta` introduces Cognitive Integration Period snapshots
containing the AF and aggregate metrics at cognitive boundaries. This is a good
seam for petta-memory episodes:

- open or close an episode when AF membership changes materially;
- record which evidence and goals jointly occupied attention during a decision;
- reconstruct the context that produced a derived belief or action proposal;
- compare intended focus with actual tool, inference, and memory use;
- detect context thrashing and unusually persistent attractors.

CIP snapshots should be immutable telemetry artifacts or append-only
`MemoryCluster` records with exact source-state identities. The mutable upstream
`&cipspace` is suitable for runtime calculation, not durable provenance.

### 4. Community-based memory organization

The community detector clusters Hebbian graphs and the topology code measures
connected components, loops, triangles, and higher clique structure. Potential
uses include:

- discovering emergent topic/episode communities independently of manually
  assigned `About` tags;
- identifying bridge records that connect otherwise separated domains;
- constructing diverse context windows by sampling multiple communities;
- detecting duplicated or overly isolated memory regions;
- prioritizing cross-community analogies for pattern mining;
- measuring whether consolidation improves compression without destroying
  important bridges.

These are derived hypotheses. A detected community is not automatically an
ontology category, and a topological change is not automatically cognitive
improvement. Promotion needs held-out retrieval or task-utility evidence.

## OmegaSelf uses beyond ordinary memory retrieval

### Discrepancy-directed attention

OmegaSelf already treats the self as an evidence-grounded, revisable theory.
Attention can prioritize unresolved prediction errors, incomplete evidence
closures, commitment conflicts, capability uncertainty, failed expectations,
and expiring `SelfHereNow` attestations. This makes self-repair computationally
selective rather than requiring a full self-ledger scan on every turn.

The dependency must remain asymmetric: OmegaSelf supplies typed discrepancy and
goal-involvement stimuli; ECAN proposes where to allocate cognition; OmegaSelf's
policy and evidence rules decide what may be believed or done.

### Continuity and fragmentation telemetry

CIP retention and Hebbian topology provide possible operational signals for:

- excessive context discontinuity across turns;
- isolated self-model fragments that never co-activate with governing goals;
- a dominant attractor starving alternative evidence;
- sudden destruction of bridges among commitments, memories, and capabilities;
- divergence between narrated self-focus and behaviorally used evidence.

These signals could feed continuity certificates, but only as evidence. They do
not by themselves prove identity continuity or failure.

### Capability and commitment maintenance

High-LTI self-model patterns can nominate capabilities and commitments for
periodic revalidation. Conversely, repeated failure involving a supposedly
capable skill should stimulate the corresponding capability claim and its
evidence closure, causing OmegaSelf to investigate or downgrade it. This is a
natural closed loop from action receipts back to self-theory repair.

## Emotion framework integration

ECAN supplies the missing concrete actuator ecology for the functional emotion
model. Emotion need not directly rewrite STI. The safer interface is:

```text
objectful appraisal + evidence closure
    -> EmotionRegimeRequest
    -> policy clamp and authorization check
    -> bounded stimulus / parameter request
    -> ECAN allocation dynamics
    -> requested-versus-applied receipt
```

Examples:

- curiosity stimulates novel, credible, decision-relevant communities and
  slightly increases exploratory diffusion;
- doubt stimulates the disputed claim, opposition evidence, provenance gaps,
  and independent checking procedures;
- frustration stimulates alternative methods and representation changes while
  reducing repeated allocation to the failed method;
- consolidation shifts wages toward provenance, compression, memory linking,
  and skill extraction after independent verification;
- vigilance increases monitoring and evidence-diversity attention without
  expanding permissions;
- boredom reduces local repeated-basin wages while exposing bounded background
  goals.

Regimes should request changes to named, bounded parameters or stimulus weights.
They should not call `setAv` freely. The governor must preserve conservation,
rate limits, verification floors, audit resources, and human interruption. Every
cycle records the triggering appraisal, requested delta, applied delta, AF
change, and eventual outcome.

The upstream topology/retention metrics are also useful for affect calibration.
For example, doubt should increase source diversity without permanently
fragmenting attention; vigilance should not collapse all resources into one
anomaly community; curiosity should improve information gain rather than merely
increase switching. Closed-loop gain and recovery can be measured directly.

## Regenerative goals and self-modification

The attention graph offers a practical way to test whether a goal is woven into
the mind rather than stored as one sentence. A goal proxy can be linked to its
supporting memories, values, policies, habits, appraisals, and frequently
co-activated concepts. A delete-and-develop experiment can then remove the
explicit goal token and measure whether ordinary attention, retrieval, and
inference reconstruct a functionally equivalent goal that regains behavioral
control.

Useful measurements include:

- number and independence of sufficient cue communities;
- bridge centrality between the goal and action/appraisal structures;
- recovery latency after lesion;
- recovered goal's behavioral influence, not lexical similarity alone;
- semantic drift across repeated recovery cycles;
- sensitivity to lesions of high-LTI or high-betweenness structures;
- whether the recovery is caused by internal distributed cues or by the test
  environment restating the goal.

This is one of the most interesting non-PLN uses of the codebase. It turns the
regenerative-goal proposal into an intervention on an explicit associative and
attentional graph.

The danger is self-protective circularity. A goal or emotion must not assign
itself unbounded LTI/VLTI, alter the lesion/equivalence test, or starve auditors.
Regenerative depth is measured by an external experiment harness over immutable
predecessor snapshots and behavioral tests.

## Semantic and engineering conflicts

### Mutable AV/STV TypeSpace versus canonical append-only records

The upstream code repeatedly removes and replaces AV/STV records in a mutable
space. petta-memory intentionally preserves immutable canonical clusters and
append-only status/truth events. Directly adding upstream AV structures to the
journal would create a high-frequency pseudo-canonical stream and blur truth
with control state.

Recommendation: keep a separate attention state keyed by stable canonical IDs.
Persist only bounded snapshots, parameter versions, and receipts when they are
needed for replay.

### Truth and attention are adjacent in representation

The upstream `TypeSpace` may store STV and AV together as one type structure,
and forgetting uses truth mean as a tiebreaker. This is convenient locally but
risky at the integration boundary. Truth confidence must not be inferred from
attention, while salience should not silently inherit authority from STV.

Recommendation: use distinct schemas and APIs. An attention proxy may reference
a truth-bearing petta-memory item but does not contain or update its normative
truth state.

### Physical forgetting

The upstream forgetting path removes atoms and incoming links. This is
incompatible with evidence replay if applied to canonical memory.

Recommendation: forget only projection/cache entries. Append explicit retirement
or supersession events to canonical memory through a separately authorized path.

### Global mutable parameters and funds

Attention parameters and funds are global mutable atoms. This complicates
multi-session isolation, deterministic replay, and concurrent hives.

Recommendation: make every attention economy instance explicit and
context-scoped, with a versioned parameter set, deterministic seed, cycle index,
and initial fund state. Never share mutable funds across unrelated agents or
episodes accidentally.

### Wall-clock and stochastic dynamics

Rent and non-AF selection use wall-clock time and randomness in important paths.
These are reasonable runtime mechanisms but weaken replay.

Recommendation: prefer cycle-based rent (the repository already contains an
`AFRentCollectionAgent2` prototype), inject time and RNG explicitly, and record
seeds plus cycle counts.

### Performance and dependency boundaries

The experiment notes performance limitations; the synapse layer crosses into
Python/igraph; CI tracks an unpinned PeTTa branch; and the repository has no
declared license in GitHub metadata at the inspected revision.

Recommendation: clarify reuse licensing before copying code, pin PeTTa/SWI/Python
and critical dependencies, benchmark realistic petta-memory proxy graphs, and
keep Python graph analysis behind a typed adapter with content-addressed inputs
and outputs.

## Recommended adapter contracts

### AttentionProjection

Inputs:

- immutable petta-memory snapshot ID and fingerprint;
- selected canonical record IDs and relation types;
- OmegaSelf context, goal, and discrepancy IDs;
- attention parameter profile ID;
- deterministic seed and cycle/time policy.

Outputs:

- stable proxy atoms and typed edges;
- initial AV values with source decomposition;
- no canonical-memory mutation authority.

### AttentionStimulusRequest

Fields:

- request ID, source regime or cognitive process, object IDs;
- decomposed reasons: relevance, novelty, discrepancy, goal involvement,
  provenance need, and expected information value;
- requested wage or parameter deltas;
- bounds, decay, horizon, and evidence closure;
- policy identity.

### AttentionCycleReceipt

Fields:

- projection and parameter identities;
- previous and next state commitments;
- requested versus applied deltas;
- AF membership and fund conservation checks;
- selected candidates and downstream consumers;
- CIP/topology metrics when enabled;
- deterministic seed/time/cycle provenance;
- failures, clamps, and policy decisions.

No receipt is itself a derived belief. It becomes evidence available to a later
promotion or self-model update.

## Staged validation plan

### Phase A: frozen source and conformance

1. Pin metta-attention, PeTTa, SWI-Prolog, Python, and dependencies.
2. Reproduce the complete upstream suite unchanged.
3. Add small conservation, deterministic-cycle, and state-isolation fixtures.
4. Clarify license and the subset intended for reuse.

### Phase B: read-only attention projection

1. Compile a synthetic petta-memory snapshot into proxy atoms.
2. Compare present salience/recency retrieval with ECAN-assisted retrieval on
   fixed query/evidence tasks.
3. Require exact canonical-ID provenance and bounded output.
4. Do not write memory or actuate OmegaClaw.

### Phase C: CIP and community telemetry

1. Record immutable attention-cycle/CIP receipts.
2. Validate community and topology measures on synthetic graphs with known
   structure before interpreting real memory.
3. Test episodic-boundary and bridge-concept predictions out of sample.

### Phase D: OmegaSelf shadow mode

1. Convert discrepancy and expiring-attestation records into bounded stimuli.
2. Measure whether prioritized repair improves calibration and reduces missed
   commitments versus matched controls.
3. Keep all policy decisions and self-model updates outside ECAN.

### Phase E: emotion shadow and ablation

Compare continuous motivation alone, descriptive emotion labels, shadow regime
requests, and governed ECAN actuation. Measure goal utility, evidence quality,
switching, context retention, topology, recovery, and audit cost. Validate that
no regime expands authorization or starves verification.

### Phase F: regenerative-goal lesions

Run delete-and-develop interventions over synthetic and then reviewed goal
networks. Measure functional recovery and semantic drift using immutable external
tests. Do not infer genuine possession from co-activation alone.

## Bottom line

The additional use is not merely “attention for more things.” `metta-attention`
can become the dynamical middle layer that converts petta-memory and OmegaSelf
structure into limited cognitive-resource allocation, while its Hebbian and CIP
telemetry measures how a context coheres, fragments, shifts, and repairs itself.
That makes it directly relevant to emotion and regenerative goals.

The architectural rule is strict: ECAN decides what gets cognitive resources;
petta-memory decides what was durably recorded; PLN/OmegaSelf decide what is
supported; policy decides what is allowed. Integration is promising precisely
if those four meanings are not collapsed into one mutable attention value.
