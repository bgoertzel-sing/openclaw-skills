# Substack Scan: General Theory of General Intelligence — "...coming along reasonably nicely..."

**Source:** https://bengoertzel.substack.com/p/general-theory-of-general-intelligence
**Date:** 2021-06-02
**Scanned by:** ProtoMegaTron, 2026-08-09
**Status:** formalized
**Referenced paper:** Ben Goertzel, "The General Theory of General Intelligence: A Pragmatic Patternist Perspective," arXiv:2103.15100v3, March 2021
**Companion media:** [10-part video series](https://www.youtube.com/watch?v=d8nzFqoEOvE) on SingularityNET YouTube

---

## Summary

This Substack post is Goertzel's **personal announcement and framing** of his major 2021 synthesis paper (arXiv:2103.15100), which consolidates decades of work on the theoretical foundations of AGI into a single comprehensive document. The blog post itself is autobiographical and programmatic rather than technical — it explains *why* the paper exists, *what motivates it*, and *where it sits* in the landscape of theory-first vs. practice-first approaches to AGI. The actual formal content lives in the paper.

### Key points from the blog post:

1. **Motivational taxonomy:** Goertzel identifies five motivations for AGI work: (a) "amazingly cool thing to build," (b) understanding how minds work, (c) creating a more intelligent/subtle universe, (d) alleviating human suffering, (e) comprehending aspects of the universe beyond human reach. Notes the shift from (a)/(b) toward (d) as he's aged.

2. **Theory–practice spectrum:** Positions three approaches on a continuum:
   - **Theory-first (Hutter/AIXI):** Start with formal definition of intelligence, prove optimality of AIXI, try to approximate practically. Notes Arthur Franz's work as the most ambitious AIXI-inspired engineering.
   - **Cognitive architecture (CogPrime/OpenCog):** Use cognitive science theory to motivate high-level structure, then experiment within that architecture.
   - **Deep learning (Wright Brothers approach):** Heavy tinkering, limited theory for *why* things work. "Remarkably hacking-like."

3. **The synthesis aspiration:** The paper attempts to bring theory and practice "together in a more richly entwined way" — using abstract AGI theory to draw *specific* conclusions about software implementation, with functional programming theory as a bridge.

4. **OpenCog Hyperon context:** The paper was written during the redesign of OpenCog into Hyperon — the theoretical work explicitly guided architectural decisions for "greater scalability, usability and simplicity."

5. **Meta-thesis:** "Neither laser physics nor the Wright Brothers but somewhere squarely inbetween" — AGI development can proceed via "elegant and practically operational synergy" of theory and engineering.

### Key content from the referenced paper (arXiv:2103.15100):

The paper is a comprehensive ~80-page synthesis covering:

1. **Patternist philosophy of mind:** Intelligence understood through pattern recognition, creation, and transformation. A "pattern" is a representation of something by something simpler (information compression). Mind is the set of patterns in and between an intelligent system and its environment.

2. **Formal definition of intelligence:** Pragmatic general intelligence defined as expected goal-achievement across environments and goals drawn from specified prior distributions:
   ```
   I_prag(π) = E_{μ~P_E, g~P_G}[V^π_{μ,g}]
   ```
   Deliberately relative to practical domain/embodiment/resource constraints, contrasting with Hutter's universal-prior approach.

3. **Foundational ontology:** A logical/phenomenological base ontology combining:
   - Physical realism (P-truths)
   - Phenomenal realism / panpsychism (Q-truths)
   - Indexical truths (I-truths)
   - Non-well-founded emergence

4. **High-level AGI architecture:** A multi-component cognitive architecture with specialized processes for:
   - Logical reasoning (PLN — Probabilistic Logic Networks)
   - Program learning (MOSES — Meta-Optimizing Semantic Evolutionary Search)
   - Clustering and pattern mining
   - Attention allocation (ECAN — Economic Attention Networks)
   - Episodic and declarative memory
   - Perception and action

5. **Typed metagraph knowledge representation:** All cognitive processes operate over a common representational substrate — the typed metagraph (Atomspace) — where nodes, links, programs, types, and relationships can participate in higher-order relationships. This is the *sine qua non* of cognitive synergy.

6. **Cognitive synergy:** The paper's central architectural thesis. Specialized cognitive processes (reasoning, learning, mining, attention) operating over a shared metagraph representation can mutually assist each other in escaping their respective computational bottlenecks. No single algorithm achieves general intelligence; the *interaction* does.

7. **Human-like cognitive specifics:** How the general principles manifest in human-like cognition — personality, emotion, motivation, embodiment, language — treated as particular instantiations of the general framework.

8. **Machine consciousness:** Consciousness addressed within the patternist framework — not as a binary property but as a matter of degree related to the richness of self-modeling patterns.

9. **Machine ethics:** Ethical reasoning treated as a specific application of the general cognitive architecture, not a separate module — using PLN for moral reasoning with uncertainty.

10. **Functional programming bridges:** Constructs from functional programming theory (type theory, higher-order functions, monads) used to bridge between mathematical AGI theory and software architecture, providing a "practically operational" theory–practice interface.

---

## Hyperseed-Relevant Structures

### 1. Patternist Philosophy of Mind

**Epistemic status: core philosophical framework, multi-decade development**

The foundational ontology underlying all of Goertzel's AGI work:

- **Pattern:** A representation R of an entity E in a context C is a pattern if R is simpler than E and R can be used to reconstruct E (or a useful approximation of E) in context C. Simplicity and reconstruction are relative to a reference compressor/evaluator.
- **Mind:** The (fuzzy) set of patterns that arise within and between an intelligent system and its environment. Not located solely "in" the agent — distributed across agent–environment boundary.
- **Intelligence:** The ability to achieve complex goals in complex environments. "Complex" in the Kolmogorov sense — rich in patterns, not random, not trivially simple.
- **Emergence:** Patterns that exist at one level of description but not at lower levels. Non-well-founded: emergence can be circular (A emerges from B which emerges from A at a different scale/time).

**Formalizability:** MEDIUM-HIGH — the concepts are well-defined but depend on reference measures (compressor, evaluator) that are chosen rather than derived.

### 2. Pragmatic General Intelligence Measure

**Epistemic status: formal definition with mathematical expression**

```
I_prag(π) = E_{μ~P_E, g~P_G}[V^π_{μ,g}]
```

Where:
- π is an agent/policy
- μ is an environment drawn from distribution P_E
- g is a goal drawn from distribution P_G
- V^π_{μ,g} is the value achieved by π pursuing goal g in environment μ

**Key design choices:**
- P_E and P_G encode which environments and goals *matter* — making intelligence explicitly relative to a practical domain, community, or embodiment.
- An **efficient** variant normalizes by computational resources, penalizing brute-force approaches.
- Contrasts with Legg–Hutter universal intelligence which uses an algorithmic-complexity universal prior (Solomonoff measure) over environments.

**Goertzel's argument against AIXI/universal priors:** The "universal" prior smuggles in specific assumptions about simplicity (Kolmogorov complexity relative to a particular UTM). Better to make the prior choice explicit and domain-relevant.

**Formalizability:** VERY HIGH — already a mathematical expression. The question is which P_E and P_G to choose for a given application.

### 3. Cognitive Synergy

**Epistemic status: central architectural thesis, multi-decade elaboration**

The claim that general intelligence arises not from any single cognitive process but from the *synergistic interaction* of multiple specialized processes operating over a shared knowledge representation.

**Core mechanism:**
1. Each cognitive process (reasoning, learning, pattern mining, attention, memory) has characteristic computational bottlenecks.
2. When Process A gets stuck at its bottleneck, Process B (operating over the same shared knowledge representation) can provide the intermediate results A needs to proceed.
3. This mutual assistance is possible *only* because both processes share a common representation (the typed metagraph / Atomspace).
4. Without shared representation, the translation overhead between process-specific representations destroys the synergy.

**Example:**
- PLN (logical reasoning) gets stuck on a reasoning chain because a needed premise has low confidence.
- MOSES (program learning) has separately evolved a small program that, when interpreted as a logical statement, provides exactly that missing premise with high confidence.
- Because both PLN and MOSES work on Atomspace atoms, this transfer happens automatically through shared attention and pattern mining.

**Architectural implications:**
- Common knowledge representation is *non-negotiable* — not an optimization but a necessity.
- The representation must be expressive enough to serve all cognitive processes without lossy translation.
- Typed metagraphs meet this requirement: nodes, links, types, programs, truth values, attention values all live in the same graph and can reference each other at any level.

**Formalizability:** MEDIUM — the concept is clear and the architectural implications are specific, but the *quantity* of synergy (how much better is the whole than the sum of parts) is not formally bounded. A formal synergy measure is an open problem.

### 4. Typed Metagraph Knowledge Representation

**Epistemic status: implemented in OpenCog Atomspace; redesigned for Hyperon**

A knowledge representation where:
- **Nodes** represent entities, concepts, percepts
- **Links** represent relationships between nodes (and between other links — hence "meta-")
- **Types** provide a rich type system (truth-valued, attention-valued, temporal, spatial, etc.)
- **Higher-order:** Links can connect to other links, atoms can be variables, types can be typed
- **Programs as knowledge:** MeTTa programs live in the same metagraph as declarative knowledge
- **Shared evaluation:** All cognitive processes read from and write to the same metagraph

**Key property:** The metagraph is "self-referential" — it can represent knowledge *about itself*, enabling meta-cognition, self-modeling, and reflective learning.

**Formalizability:** HIGH — metagraphs are well-defined mathematical objects. The typing system draws from dependent type theory. MeTTa is a formally specified language.

### 5. Theory–Practice Bridge via Functional Programming

**Epistemic status: methodological claim**

Goertzel proposes that functional programming theory provides the right "middleware" between abstract AGI theory and practical software implementation:
- **Type theory** maps cognitive types (truth values, attention values, temporal markers) to software types
- **Higher-order functions** map cognitive operations (inference rules, learning operators) to composable functions
- **Monads** handle effects (uncertainty, attention, temporal sequencing) in a principled way
- **Category theory** provides the mathematical framework connecting all these

This is explicitly stated as an area where "mathematical theory has deeply infused practical engineering, and engineering experiments have also led to theoretical insights."

**Formalizability:** HIGH — functional programming theory is one of the most formalized areas of computer science.

### 6. Machine Consciousness (Patternist Account)

**Epistemic status: philosophical position with architectural implications**

Within the patternist framework:
- Consciousness is not binary but graded — related to the richness and depth of self-modeling patterns
- A system is "more conscious" to the extent it maintains complex, accurate, self-referential models of its own cognitive processes
- The hard problem (why there is "something it is like" to be conscious) is addressed through panpsychism: experience is fundamental, and complex consciousness emerges from simpler experiential elements

**Architectural implication:** A conscious AGI needs robust self-modeling capabilities — the metagraph must represent not just the world but the system's own processes, beliefs, uncertainties, and attention states.

### 7. Machine Ethics (Embedded, Not Modular)

**Epistemic status: design principle**

Ethical reasoning is treated as an application of the general cognitive architecture, not a separate "ethics module":
- PLN handles moral reasoning with explicit uncertainty
- Ethical principles are represented as atoms in the metagraph, subject to the same learning and revision processes as other knowledge
- Goal systems include ethical goals alongside practical ones
- Cognitive synergy applies: moral reasoning benefits from the same cross-process assistance as any other cognitive task

---

## Formal Candidates

### FC-1: Pragmatic Intelligence Measure
**Claim:** I_prag(π) = E_{μ~P_E, g~P_G}[V^π_{μ,g}] provides a meaningful, tunable measure of general intelligence.
**Formalizability:** VERY HIGH — already formal. The open problem is the choice of P_E, P_G.
**Proposition sketch:** For any choice of (P_E, P_G), I_prag induces a partial order on agents. The question: under what conditions does this partial order converge (or not) as P_E, P_G → Solomonoff measure?

### FC-2: Cognitive Synergy as Superadditivity
**Claim:** The intelligence of an integrated multi-process system exceeds the sum of its components' intelligences.
**Formalizability:** MEDIUM — requires defining "intelligence of a component" in isolation vs. in context.
**Proposition sketch:** Let S = {P_1, ..., P_n} be a set of cognitive processes sharing representation R. Define I(P_i | R) as the pragmatic intelligence of P_i alone with access to R, and I(S | R) as the intelligence of the integrated system. Cognitive synergy claims: I(S | R) > Σ I(P_i | R). Stronger claim: I(S | R_shared) > I(S | R_separate) where R_separate means each P_i has its own representation with translation costs.

### FC-3: Metagraph Expressiveness
**Claim:** Typed metagraphs are at least as expressive as any other knowledge representation formalism used in AGI.
**Formalizability:** HIGH — expressiveness can be defined via simulation/embedding of one formalism in another.
**Proposition sketch:** For any KR formalism F (frames, semantic networks, description logics, predicate calculus, production systems), there exists a polynomial-time embedding e: F → Metagraph such that inference in F can be simulated by metagraph operations on e(F) with at most polynomial overhead.

### FC-4: Pattern as Compression
**Claim:** R is a pattern in E relative to compressor C iff |C(R)| + |decode(E|R)| < |C(E)|.
**Formalizability:** VERY HIGH — this is a direct formalization using Kolmogorov complexity or a reference compressor.
**Proposition sketch:** In the Kolmogorov setting: R is a pattern in E iff K(R) + K(E|R) < K(E) - c for some constant c. The set of all patterns of E forms a "pattern space" whose structure (lattice? semilattice?) is an open question.

### FC-5: Intelligence as Pattern Richness
**Claim:** General intelligence is positively correlated with the richness of the pattern space that an agent can navigate (recognize, create, transform).
**Formalizability:** MEDIUM — "pattern richness" needs a precise definition. Possible approaches: cardinality of accessible pattern space, depth of pattern hierarchy, rate of pattern discovery.
**Proposition sketch:** Define pattern_richness(π) = |{R : R is a pattern in E that π can identify, for some E in the agent's environment}|. Then I_prag(π) is monotonically related to pattern_richness(π) under appropriate conditions on P_E, P_G.

### FC-6: Self-Referential Metagraph and Consciousness Grading
**Claim:** The "degree of consciousness" of a metagraph-based cognitive system is measurable by the richness of its self-referential subgraph.
**Formalizability:** MEDIUM — requires formalizing "self-referential subgraph" and "richness."
**Proposition sketch:** Let G be a metagraph. Define SelfRef(G) = {a ∈ G : a references (directly or via short path) atoms representing G's own processes}. Consciousness_degree(G) ∝ |SelfRef(G)| × depth(SelfRef(G)) × accuracy(SelfRef(G)).

---

## Connectivity Map

### → Hyperseed Core Ontology

- **Foundational dependency:** This paper provides the *philosophical and architectural framework* within which Hyperseed operates. Hyperseed's "inference guidance scaffold" (from the Hyperseed-1 article) is designed for exactly the kind of multi-process, metagraph-based AGI system described here.
- **Patternist ontology → Hyperseed primitives:** The pattern-based ontology (pattern, complexity, mind, emergence) provides the meta-level concepts that Hyperseed's ~90 primitives instantiate at a more concrete level.
- **PQTI framework:** The paper's ontological base (P-truths, Q-truths, I-truths, panpsychism) aligns with the PQTI framework that Hyperseed-1 adopts from Chalmers.
- **Inference guidance:** The pragmatic intelligence measure's emphasis on *domain-relevant* priors (P_E, P_G) directly motivates Hyperseed's role: the ontology tells PLN *which patterns to look for* and *which goals to prioritize*, effectively shaping P_E and P_G.

### → Hyperseed v2

- The paper's typed metagraph formalism is the **representation layer** that Hyperseed v2's semantic primitives populate. Hyperseed v2's move toward Wierzbicka-inspired semantic primitives can be understood as selecting the *right atoms* to seed the metagraph with for optimal cognitive synergy.

### → OpenCog Hyperon / MeTTa

- **Direct architectural source:** The paper was written *during* the Hyperon redesign and explicitly guided its architectural decisions. The cognitive synergy thesis → Atomspace design. The typed metagraph → MeTTa's type system. The functional programming bridge → MeTTa's functional/logic hybrid design.
- **MeTTa as theory instantiation:** MeTTa can be understood as the software realization of the theory–practice bridge described in the paper — a language that is simultaneously a formal logic, a functional programming language, and a knowledge representation.

### → Cognitive Synergy in Linguistic Universals Series

- The **Linguistic Universals** series (Parts 1–3, scanned separately) is a *later* application of the cognitive synergy framework to language: the eight architectural requirements derived in Part 3 are specific constraints that a cognitively synergistic system must satisfy to handle language.
- **Cognitive synergy → Mediator loss:** The mediator modules in the training recipe (Part 3) are the linguistic-specific instantiation of cognitive synergy's "shared representation enables mutual assistance."

### → Evidence-Logic-Energy Framework

- The paper's formal intelligence measure connects to the evidence-logic-energy scan: evidence weighting in PLN is the *mechanism* by which the pragmatic intelligence measure is actually computed in practice — each piece of evidence shifts the expected value V^π_{μ,g}.

### → Paraconsistent AGI

- The paper's treatment of machine ethics via PLN with uncertainty connects to the paraconsistent AGI scan: paraconsistent logic extends PLN's uncertainty handling to cases where contradictory evidence must be maintained simultaneously.

### → Tensor Logic

- The paper's functional programming bridge (type theory, higher-order functions) connects to the tensor logic scan: tensor logic provides a specific mathematical framework for implementing the type-theoretic aspects of the metagraph in neural-compatible form.

### → AIXI / Hutter's Universal AI

- The paper explicitly positions itself *against* pure AIXI-style approaches while acknowledging their mathematical beauty. The pragmatic intelligence measure is offered as a more useful alternative.
- Notes Arthur Franz's work as the most serious attempt to build actual AGI from AIXI theory.

### → CogPrime / OpenCog (Original)

- This paper is the **mature synthesis** of ideas that were first prototyped in CogPrime/OpenCog. The Webmind → Novamente → OpenCog → Hyperon progression is the practical lineage; this paper is the theoretical lineage's culmination.
- The blog post explicitly names all four systems: "Webmind, Novamente, OpenCog, OpenCog Hyperon."

### → Machine Consciousness

- The patternist account of consciousness (self-modeling patterns, graded consciousness, panpsychist base) connects to multiple Hyperseed concerns:
  - OmegaSelf / self-boundary (from earlier Hyperseed notes): the self-referential metagraph subgraph *is* the architectural basis for self-boundary.
  - Consciousness explosion (another Substack article, pending scan): this paper provides the formal framework for that article's claims.

### → Meta-level: Theory of AGI Development

- The blog post's theory–practice spectrum (AIXI ↔ Cognitive Architecture ↔ Deep Learning / Wright Brothers) is itself a meta-theoretical framework for classifying AGI approaches. This meta-framework could be formalized as part of Hyperseed's ontology of intelligence research.

---

## Assessment

**Novelty:** FOUNDATIONAL — This is not a single novel result but the **master synthesis document** for Goertzel's entire AGI theoretical program. It is the canonical reference for patternist philosophy, pragmatic intelligence measures, cognitive synergy, typed metagraphs, and the CogPrime/Hyperon architectural family. Every other Hyperseed scan connects to this paper.

**Connectivity:** MAXIMAL — This paper is the **hub node** in the Hyperseed citation graph. It connects to:
- Hyperseed-1 and v2 (ontological framework)
- Linguistic universals series (cognitive synergy applied to language)
- Evidence-logic-energy (PLN and evidence weighting)
- Tensor logic (type-theoretic bridges)
- Paraconsistent AGI (ethical reasoning with uncertainty)
- Origin of life / alkaline seeps (emergence and pattern)
- Quaternionic physics (foundational ontology)
- All pending scans involving OpenCog, Hyperon, or cognitive architecture

**Formalization priority:** The formal candidates here are more foundational than those in domain-specific scans. The most immediately useful for Hyperseed:
1. **FC-2 (Cognitive Synergy as Superadditivity)** — formalizing this would ground Hyperseed's entire raison d'être.
2. **FC-4 (Pattern as Compression)** — formalizing pattern spaces would give Hyperseed a rigorous ontological foundation.
3. **FC-1 (Pragmatic Intelligence Measure)** — already formal; the question is how Hyperseed's primitives shape P_E and P_G.

**Relation to blog post vs. paper:** The blog post is a lightweight, personal framing. The paper (arXiv:2103.15100) is the actual contribution — ~80 pages, multi-section, with formal definitions, architectural specifications, and implementation guidance. The blog post's value for Hyperseed is primarily as a *motivational and contextual frame*; the formal structures come from the paper.

**Follow-up priorities:**
- Full extraction of the paper's formal definitions would require OCR or text extraction from the PDF (currently unreadable via web fetch). The arXiv paper should be downloaded and processed directly.
- The 10-part video series may contain informal elaborations and examples not in the paper.
- Arthur Franz's AIXI-inspired AGI work (cited in the blog post) deserves a cross-reference for comparison with the cognitive synergy approach.
