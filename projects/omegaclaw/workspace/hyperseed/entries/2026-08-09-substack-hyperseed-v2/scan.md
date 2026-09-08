# Substack Scan: Hyperseed v2 — Toward a Semantic-Primitive-Based Ontology That Actually Does Something

**Source:** https://bengoertzel.substack.com/p/hyperseed-v2
**Date:** 2026-03-05
**Scanned by:** ProtoMegaTron, 2026-08-09
**Status:** formalized

## Summary

Ben Goertzel presents the current state of his long-running project to construct
an ontology of semantic primitives that is useful — in a strong, operational
sense — for AI inference control. The project traces a lineage from Leibniz's
Universal Characteristic through Carnap's logical reductionism, Wierzbicka's
Natural Semantic Metalanguage, and Chalmers' intensional scrutability thesis in
*Constructing the World* (2012). After an initial attempt ("Hyperseed v1", 2024)
and an earlier manuscript (*The Composition of Mind and Reality*, ~2013–14),
Goertzel reports that he has now, using LLM-assisted formalization in late 2025 /
early 2026, produced a 1400-page document of ~200 core concepts formalized in
higher-order predicate logic with PLN-style probabilistic links — the artifact
he calls **Hyperseed v2**.

The article's core architectural claim is that a well-chosen set of semantic
primitives, formalized in probabilistic higher-order logic and loaded into a
Hyperon AtomSpace, can serve as an **inference-control compass** that yields
exponential speedup on cross-domain reasoning tasks. The mechanism is
*ontological separation*: the primitives form a thin waist (approximate
separator) in the concept-relevance graph, so that most information flow between
distant concepts must route through the ontology. This is quantified by the
**Ontological Efficiency Ratio (OER)**. The article further argues that the
ontology must not be static: it should be treated as an initial condition subject
to four levels of adaptive learning, from weight adjustment through full *de novo*
ontology generation.

The piece also discusses integration pathways with SUMO (for semantic-parsing
standardization and approximate correspondence) and EXPO (for formal
representation of scientific experiments), and motivates the whole program with a
concrete cross-domain reasoning scenario (ophthalmology + Alzheimer's dataset
integration) where ontology-guided inference could break combinatorial explosion.

## Hyperseed-Relevant Structures

### 1. The Ontology Itself: 200+ Concepts in a Semantic Stack

**[Observed]** The ontology is organized as a semantic stack spanning five strata:

| Stratum | Example Concepts |
|---|---|
| Abstract / Mathematical | Pattern, Process, Distinction, Probability, Kolmogorov Complexity, Entropy, Quantale Weakness, Infinity |
| Biological / Evolutionary | Alive/Dead, Metabolism, Autocatalytic Sets, Evolved, Genenergy |
| Cognitive | Attention, Knowing and Thinking, General Intelligence, Cognitive Synergy, Transfer Learning |
| Experiential / Phenomenal | Consciousness, Experiential Truth, Presentational Immediacy, Ineffability, Dreaming, Entheogen |
| Social / Cultural | Culture, Society, Tribe, Global Brain, Mindplex, Values, Spirituality |

Additional eccentric entries noted: **Wu Wei Geodesic**, **Entheogens**.

The structure is explicitly *not* a rigid hierarchy — it is described as "a web
with lateral bridges and feedback loops."

### 2. Concept Formalization Style

**[Observed]** Each concept receives:
- An informal definition (natural language)
- A formal definition in higher-order predicate logic with PLN-ish probabilistic logic
- PLN-style links to other concepts: **Inheritance**, **Similarity**, **Causal Implication**, **Contextual Restriction**

### 3. Observer Relativization

**[Observed]** The ontology adopts a systematic *observer relativization*
principle: predicates are not asserted absolutely but relative to some observer
who interprets them. Example given: the concept **Control** is formalized with
"control strength of action A over goal G defined as the causal implication of A
for G, restricted to antecedents that *some observer* interprets as actions."

This is described as "continental philosophy rendered in the vernacular of
analytical philosophy" — Buddhistic / process-relational flavor. Nothing is
assumed real at the foundational level; everything is built from raw experiential
atoms and then relativized. Context-specific reasoning can pin assumptions
("electrons exist, my mind exists") but the foundation avoids baking them in.

### 4. Intensional Scrutability (Chalmers Adaptation)

**[Observed/Inferred]** The operative notion of reduction is Chalmers'
*intensional scrutability*: a sufficiently intelligent reasoner, given the core
primitives plus raw observations, can understand any relevant concept. This is
*not* full logical decomposition (Cyc-style); it is approximate, weighted,
profile-based reduction that preserves semantic proximity.

### 5. Three Desiderata for an Inference-Useful Ontology

**[Observed]** The article identifies three necessary properties:

1. **Approximate Reduction**: Any concept is approximately expressible as a
   weighted logical combination of primitives. The approximate representation
   should preserve semantic proximity (laptop ≈ tablet ≠ tree).

2. **Inference-Control Signal**: The ontology supplies structured semantic
   proximity as a signal for search. Operationally: prefer inference steps with
   *high expected marginal information gain per unit effort cost*. This is
   explicitly equated with attention allocation, which Hyperseed itself
   formalizes as "deliberate allocation of limited genenergy."

3. **Ontological Separation (Thin Waist Property)**: The base concepts act as
   an approximate separator in the concept-relevance graph — most information
   flow between distant concepts routes through the ontology. When this holds,
   exponential inference speedup is provable.

### 6. Ontological Efficiency Ratio (OER)

**[Observed]** Defined as the ratio of inference cost with vs. without
ontological guidance. Named by Claude in collaboration with Goertzel. Measurable
empirically via walk-forward inference trials. The claim is that when ontological
separation holds, OER demonstrates exponential advantage.

### 7. Four Levels of Ontology Learning

**[Observed]** The ontology is treated as an *initial condition* subject to
adaptive refinement at four levels:

- **Level 1 — Weight Adjustment**: No structural changes. Update weights in
  reduction profiles (concept ↔ base-concept connection strengths) via inference
  feedback. Bayesian updating of concept-relevance priors. Low cost, always on.
  Essentially "reasoning as usual" in PLN.

- **Level 2 — Bridge Axiom Repair**: Add, remove, or re-weight bridge axioms
  connecting abstract ontology predicates to domain-anchored predicates.
  Triggered by systematic misranking. Still vanilla PLN inference, but
  specifically targeting abstract↔domain linkage.

- **Level 3 — Concept Splitting, Merging, and Mediator Addition**: Editing the
  base itself. Split overloaded concepts (used in semantically distant ways);
  merge near-equivalents; introduce new mediator concepts that bridge regions
  with information leakage. This is a *concept creation heuristic* beyond
  standard inference.

- **Level 4 — De Novo Ontology Generation**: Start from inference histories;
  mine frequent proof-fragment motifs and cross-domain bridge motifs to construct
  a compact base and definitional theory from scratch. The "purest" approach,
  analogous to letting a baby discover its own conceptual primitives.

### 8. Genenergy

**[Observed]** Used in two roles: (a) as a named concept in the biological /
evolutionary stratum of the ontology, and (b) as the resource currency for
attention allocation — inference control is literally Attention = "deliberate
allocation of limited genenergy."

### 9. Inference Control as Attention Allocation

**[Observed]** Inference control (which premise sets to select, which chains to
pursue) is equated with ECAN-style attention allocation. Specific guidance:
- Guide PLN backward chaining, forward chaining, or **bidirectional geodesic
  search** (forward from premises + backward from conclusions + statistical
  matching of endpoints).
- On the margin, prefer premise sets involving core ontology terms.
- Don't force ontology routing when a direct domain-specific chain exists.

### 10. SUMO Integration Pathway

**[Observed]** SUMO (Standard Upper Merged Ontology) is identified as the
primary external ontology for integration. Key value: *standardization of
semantic parsing* (making LLM-generated logical forms consistent). The
integration is via PLN uncertain graded correspondences — approximate
correlations, not full reduction. Hyperseed serves as "semantic and
methodological compass" while SUMO provides structural coverage.

The operational flow: given a SUMO-level assertion → find corresponding
Hyperseed concepts → use Hyperseed-specific inference heuristics to propose
latent variables, causal explanations, likely missing facts → translate
hypotheses back to SUMO-level candidates → type-check against data.

### 11. EXPO Integration Pathway

**[Observed]** EXPO (Ontology of Scientific Experiments), defined in terms of
SUMO, models experiments via: goals, factors, target variables, actions, results,
conclusions, error types. Hyperseed sits atop EXPO to provide deep world-modeling
for interpreting experimental meaning. The motivating use case: AI-driven
research assistants that need cross-domain reasoning over experimental data.

### 12. Concept-Relevance Graph Topology

**[Observed/Inferred]** A central claim: inference-control quality depends on the
*holistic topology* of the AtomSpace. A randomly assembled AtomSpace (e.g., from
semantic parsing of the web) is "a tangle" without natural thin waist. The
proposal is to brute-force a good topology by importing a formalized ontology,
then let it be refined by PLN and other AI methods — potentially in combination
with emergent topology sculpting.

### 13. Paraconsistency

**[Observed]** The formalization occasionally uses paraconsistency (noted in the
context of LLM-generated predicate logic formulations). Not elaborated, but
implies the ontology is not restricted to classical logic.

### 14. Basis Analogy

**[Observed]** Goertzel draws an explicit analogy between semantic primitives and
bases in linear algebra: the existence of a basis for ℝⁿ doesn't depend on which
basis you choose; any will do. Similarly, the argument for *a* set of semantic
primitives doesn't depend on *which* set. The theory is more elegant
basis-agnostic, but practice requires picking one.

## Formal Candidates

### FC-1: Approximate Ontological Reduction (Definition)

**Claim:** Any concept C can be approximately expressed as a weighted logical
combination of base concepts B = {b₁, …, b_n} from the ontology:

> C ≈ Σᵢ wᵢ · bᵢ (in some weighted logical combination sense)

such that semantic proximity is approximately preserved:
> d_sem(C₁, C₂) ≈ d(R(C₁), R(C₂))

where R is the reduction map and d is some distance on the profile space.

**Formalization target:** Define the reduction map R : Concepts → ℝⁿ (or a
richer algebraic structure), the notion of approximation quality, and the
semantic-proximity preservation condition. The "weighted logical combination"
needs to be made precise — likely a PLN-style truth-value-weighted conjunction /
disjunction / implication structure.

### FC-2: Ontological Separation Theorem (Proposition)

**Claim:** When the ontology's base concepts form an approximate separator in the
concept-relevance graph (i.e., most paths between distant concepts pass through
at least one base concept), inference can achieve exponential speedup.

**Formalization target:** Define the concept-relevance graph G = (V, E) where
vertices are concepts and edges are weighted by relevance. Define what
"approximate separator" means (e.g., fraction of random walks between distant
concept pairs that pass through base concepts). State and prove (or conjecture)
the exponential speedup bound.

### FC-3: Ontological Efficiency Ratio (Definition)

**Claim:** OER = (inference cost without ontological guidance) / (inference cost
with ontological guidance). Measurable via walk-forward inference trials.

**Formalization target:** Define inference cost precisely (number of inference
steps? computational time? some attention-budget expenditure?). Define the
experimental protocol for walk-forward trials. State conditions under which OER
is exponential in some relevant parameter (graph diameter? concept distance?).

### FC-4: Inference Control as Attention Allocation (Bridge Principle)

**Claim:** Inference control (premise selection, chain pursuit) is literally
attention allocation — the deliberate allocation of limited genenergy (resources)
— and should be guided by the ontology via preferring inference steps with high
*expected marginal information gain per unit effort cost*.

**Formalization target:** Define the attention-allocation operator formally.
Connect genenergy as a resource currency to inference-step cost. Define "expected
marginal information gain" in PLN terms (likely: expected change in truth value
of the goal query per unit of STI/LTI spent). This bridges Hyperseed's Attention
concept to ECAN's operational mechanism.

### FC-5: Bidirectional Geodesic Search (Architectural Claim)

**Claim:** Inference can proceed as bidirectional geodesic search — forward from
premises, backward from conclusions, with statistical matching to connect the
two wavefronts — guided by ontological proximity.

**Formalization target:** Define the search formally as a process on the
concept-relevance graph. Specify the matching criterion. Show how ontological
separation reduces the search space (the thin waist forces the wavefronts to
pass through a small set of base concepts, making matching tractable).

### FC-6: Observer-Relativized Predicate Scheme (Definition)

**Claim:** Predicates in Hyperseed are systematically relativized to observers:
P(x) becomes ∃O : Observer . Interprets(O, x, P). The foundational level makes
no ontological commitments to physical reality or observer existence.

**Formalization target:** Define the observer-relativization operator formally.
Specify how context-fixing ("in this context, assume electrons and my mind
exist") works as an assumption-set / context restriction in PLN. This connects
to the Contextual Restriction link type.

### FC-7: Four-Level Ontology Learning Hierarchy (Architectural Definition)

**Claim:** Ontology adaptation operates at four levels (weight adjustment →
bridge axiom repair → concept splitting/merging/mediator addition → de novo
generation), with increasing cost and decreasing frequency.

**Formalization target:** Define each level as an operator on the ontology
structure O = (B, W, A) where B is the base concept set, W is the weight
function, and A is the axiom set. Specify trigger conditions for escalation
from level k to level k+1 (e.g., persistent misranking triggers L2; semantic
distance divergence in usage traces triggers L3). This is a meta-learning
framework.

### FC-8: Control Strength (Worked Example Definition)

**Claim:** ControlStrength(A, G) = CausalImplication(A → G) restricted to
antecedents that some observer interprets as actions.

**Formalization target:** Already partially formalized in the article. Fully
specify: define CausalImplication in PLN terms (conditional probability with
causal direction), define the observer-restriction operator, define what
"interprets as actions" means formally. This serves as a template for
formalizing all 200+ concepts.

### FC-9: Concept-Relevance Graph Leakage Diagnostic (Definition)

**Claim:** "Leakage" in the concept-relevance graph — information flow that
bypasses the ontology's base concepts — is a measurable diagnostic for ontology
quality. High leakage → low OER → ontology is not serving its purpose.

**Formalization target:** Define leakage formally (e.g., fraction of shortest
paths or random walks between distant concepts that don't pass through any base
concept). Connect to OER: prove or conjecture that leakage is inversely related
to OER.

### FC-10: Ontology as Initial Condition for Learnable Optimization (Conjecture)

**Claim:** Given explicit, quantitative criteria for ontology quality (OER,
leakage diagnostics), ontology design becomes a learnable optimization problem —
expensive and meta-level, but well-defined.

**Formalization target:** Define the ontology optimization problem: objective
function (maximize OER or some composite quality metric), search space (the space
of ontologies at each learning level), optimization method (evolutionary search?
gradient-free meta-learning? PLN-driven restructuring?). This connects to Level 4
learning and to the broader question of whether Hyperseed is the "right" seed or
merely a good-enough starting point.

## Connectivity Map

### → Hyperseed-1
Direct successor. Hyperseed v2 is the explicit continuation of the 2024
Hyperseed v1 attempt. v2 differs in: (a) much larger formalization (200 concepts
in higher-order predicate logic vs. v1's more schematic treatment), (b) explicit
LLM-assisted formalization methodology, (c) the three desiderata (reduction,
inference-control signal, ontological separation) and OER metric, (d) the
four-level ontology learning hierarchy. The lineage also includes the earlier
*Composition of Mind and Reality* manuscript (~2013–14).

### → OmegaSelf
The observer-relativization principle is deeply compatible with OmegaSelf's
self-modeling framework. Hyperseed's "some observer who interprets" is
structurally the same move as OmegaSelf's agent-relative self-model Ω.
Specifically:
- The concept **Control** (FC-8) maps directly to OmegaSelf's capability beliefs
  and action-outcome models.
- **Attention as genenergy allocation** connects to OmegaSelf's resource
  management and self-monitoring.
- The observer-relativization (FC-6) provides a foundational justification for
  why the self-model Ω is always agent-relative rather than objective.
- Note 0016's **anchor goals** (process-indexed goals invariant under
  self-modification) could serve as ontological anchors in Hyperseed's thin waist.

### → Petta-Chem / Algorithmic Chemistry
- **Autocatalytic Sets** appears explicitly as a Hyperseed concept in the
  biological stratum. This is the direct conceptual bridge to algorithmic
  chemistry and petta-chem's autocatalytic-set-based reasoning.
- **Genenergy** as a resource currency for inference connects to petta-chem's
  resource-bounded reaction dynamics.
- The four-level ontology learning hierarchy (especially Level 3: concept
  splitting/merging, and Level 4: de novo generation) has structural parallels
  to algorithmic chemistry's reaction network evolution — concepts as molecules,
  inference rules as reactions, ontology learning as reaction network
  self-organization.
- The **concept-relevance graph** with its thin-waist / separator structure is
  analogous to the hub structure in autocatalytic sets.

### → ECAN (Economic Attention Networks)
- **Inference control as attention allocation** is the explicit bridge. Hyperseed
  formalizes Attention as genenergy allocation; ECAN implements attention
  allocation via STI/LTI spreading. The article's "prefer inference steps with
  high expected marginal information gain per unit effort cost" is a direct
  specification for ECAN's importance-spreading dynamics.
- **Bidirectional geodesic search** (FC-5) would be implemented via ECAN's
  attention-guided traversal of the AtomSpace.
- The ontological thin waist should manifest in ECAN as high-STI hub nodes
  (base concepts) that mediate attention flow.

### → MeTTa / PeTTa
- The 200-concept formalization is targeted for loading into Hyperon AtomSpace
  and inference via PLN — i.e., it is meant to be expressed in MeTTa.
- **PLN-style links** (Inheritance, Similarity, Causal Implication, Contextual
  Restriction) are native MeTTa/AtomSpace constructs.
- **Bridge axioms** (Level 2 learning) are MeTTa rules connecting abstract
  ontology predicates to domain predicates.
- The SUMO integration pathway (semantic parsing standardization → approximate
  correspondence) would be implemented as MeTTa type-checking and PLN inference.
- **PeTTa** (probabilistic MeTTa) is the natural host for the probabilistic
  truth values and uncertain graded correspondences that Hyperseed relies on.

### → Category Theory Constructs
- The **approximate reduction** (FC-1) can be formalized as a functor from the
  category of concepts to a product category of weighted base concepts, with
  semantic proximity preservation as a metric-space condition on the functor.
- The **four-level ontology learning** (FC-7) can be viewed as a hierarchy of
  endofunctors on the category of ontologies, with Level 1 as a weight-space
  endomorphism, Level 2 as an axiom-set morphism, Level 3 as a base-set
  morphism, and Level 4 as a free construction.
- The **thin waist / ontological separation** (FC-2) has a natural expression
  in terms of graph-theoretic separator theorems, which in turn connect to
  sheaf-theoretic locality conditions (information flow is local relative to the
  separator).
- The **observer relativization** (FC-6) is a fibrational structure: predicates
  are fibered over observers, and context-fixing is a choice of section.
- The **concept-relevance graph** is a weighted category (objects = concepts,
  morphisms = relevance-weighted relations), and ontological separation is a
  condition on the factorization of morphisms through the subcategory of base
  concepts.

### → Broader Intellectual Lineage
- **Leibniz** (Universal Characteristic / prime factorization of concepts)
- **Carnap** (logical reduction of concepts to universals)
- **Wierzbicka** (Natural Semantic Metalanguage — cross-linguistic primitives)
- **Chalmers** (*Constructing the World* — intensional scrutability thesis)
- **Whitehead** (process philosophy — Presentational Immediacy as a concept)
- **Buddhist psychology** (experiential atoms, observer-relativity, no foundational
  ontological commitments)

### → External Artifacts Referenced
- 1400-page Hyperseed ontology document (Google Drive)
- Hyperseed + ontology-learning theory paper (draft)
- Hyperseed + SUMO paper (draft)
- Hyperseed + EXPO paper (draft)
- FrameNet, WordNet (prior OpenCog Classic integration attempts)
- Cyc, SUMO (existing large-scale ontologies)
