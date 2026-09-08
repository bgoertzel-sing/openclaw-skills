# Substack Scan: Can All Human Concepts Be Reduced to Combinations of a Few Primitives?

**Source:** https://bengoertzel.substack.com/p/can-all-human-concepts-be-reduced
**Date:** 2022-03-14
**Scanned by:** ProtoMegaTron, 2026-08-09
**Status:** formalized

---

## Summary

This is the **philosophical genesis article** for what would later become the Hyperseed project — the earliest Substack exploration of semantic primitives and conceptual reduction. Written in March 2022, more than two years before Hyperseed-1's formal introduction (2024-11-27), this article lays down the foundational philosophical arguments, identifies the key intellectual predecessors, introduces several novel formalisms, and articulates the core tensions that all subsequent Hyperseed work must navigate.

The article is structured as a "musing" — philosophical exploration rather than formal specification — but contains surprisingly precise formal proposals embedded within the discursive flow:

1. **Frames the core question:** Can a small set of primitive concepts generate all human concepts combinatorially?
2. **Surveys the intellectual landscape:** Wierzbicka (too minimal), Cyc/SUMO (too maximal), Carnap (logical reduction), Chalmers (PQTI scrutability)
3. **Introduces the magician system / algorithmic chemistry formalism** as the mathematical foundation for what "reduction to primitives" means
4. **Proposes the PAC (Probably Approximately Correct) framing** — the signature move that transforms an all-or-nothing question into a quantitative scaling question
5. **Introduces the ps(p,e) function** — a formal measure of primitive coverage
6. **Articulates the Embodied Communication Prior (ECP)** as a systematic derivation method for primitives
7. **Extends ECP to ECP++** by incorporating psi phenomena
8. **Introduces the concept-as-open-ended-poset thesis** — concepts are not single formalizations but infinite ascending chains of approximations
9. **Argues for resource-relative primitivity** — what counts as "primitive" is always relative to a mind's computational budget
10. **Announces intent** to reboot the "Composition of Mind and Reality" manuscript using MeTTa for Minecraft/SophiaVerse agents

**Intellectual mode:** This is Goertzel in synthesis mode — weaving together threads from Wierzbicka, Chalmers, Bateson, Carnap, Buddhist logic, his own earlier work (Chaotic Logic 1995, ECP 2009, Composition of Mind and Reality 2013), and the emerging Hyperon platform into a coherent research program.

**Historical significance:** The article was written ~2.5 years before the Hyperseed-1 article and represents the "philosophical incubation" phase. Every major design decision in Hyperseed-1 and v2 can be traced to ideas articulated or foreshadowed here.

---

## Hyperseed-Relevant Structures

### 1. Intellectual Lineage (Comprehensive Map)

| Thinker/System | Contribution | Role in Hyperseed Genealogy |
|----------------|-------------|---------------------------|
| **Anna Wierzbicka** | Natural Semantic Metalanguage (NSM) — ~65 semantic primitives sufficient for all human concepts | First encounter with semantic primitives; critiqued as "biased on the side of minimalism" |
| **Cyc / SUMO** | Massive formal ontologies with huge numbers of logical primitives | Counter-examples of excessive maximalism; primitives grow toward infinity |
| **Rudolf Carnap** | Early 20th century formalization of commonsense concepts | Methodological ancestor; "tried to formalize commonsense by precise definitions for every concept" |
| **David Chalmers** | *Constructing the World* — PQTI framework; analytical argument that reduction is *possible* without executing it | Primary theoretical framework; top-down feasibility argument |
| **Gregory Bateson** | MetaPattern — "it is pattern which connects" | Goertzel identifies "reduction to primitives" as essentially equivalent to Bateson's MetaPattern |
| **Leibniz** | Universal Characteristic (implied via Carnap lineage) | Deep ancestor of the entire project |
| **Goertzel (1995)** | *Chaotic Logic* — introduces "magician system" formalization | Mathematical foundation for what "reduction" means; extended in 2020 paper |
| **Goertzel (2009)** | Embodied Communication Prior (ECP) | Hypothesis about what primitives are needed for human-like intelligence |
| **Goertzel (2013)** | "Composition of Mind and Reality" (unfinished manuscript) | Direct precursor; attempted ~50 primitives in quasi-Atomese framework for OpenCog |
| **Goertzel (2020)** | "Formalizing Occam's Razor and Simplicity Measures" (arXiv:2004.05269) | Formal combinational computational model for reduction |
| **Yoshua Bengio** | "Consciousness Prior" | Goertzel notes ECP is "a more precisely defined version" that Bengio formulated "roughly and years later" |
| **Zar Goertzel** | Conversation partner on Chalmers | Sparked the renewed interest in this direction |
| **Stcherbatsky** | *Buddhist Logic* | Building reality from inner/outer sense-data + background assumptions; alternative to physics-first reduction |

### 2. Chalmers' PQTI Framework

Chalmers argues the primitive set should encompass **PQTI**:

- **P** = Physics — microphysical and macrophysical truths
- **Q** = Qualia — phenomenal truths ("what red looks like," "what raindrops on skin feel like")
- **I** = Indexical — pointing in shared reality ("right now," "that tree over there")
- **T** = That's All — Occam's Razor closure; what one can build from PQI is all there is

**Goertzel's assessment:** "So Chalmers' argument is that if we take some primitives about macro and micro physics, some primitives about subjective experience and some indexical communicative primitives about our shared life and environment — then we can build up all human knowledge out of these."

**Key link to ECP:** "Each of the ECP communication modes as commonly described combines physics, subjectivity and indexicality in various ways."

### 3. The "Composition of Mind and Reality" Manuscript (2013)

An unfinished Goertzel manuscript that attempted:
- ~50 primitives in an abstract functional/logical language
- Target: generating a wide set of concepts in OpenCog's native format (Atomese)
- Example shown: formalization of "perceptual hierarchy" in terms of simpler concepts

**Status as of article:** Goertzel expresses intent to reboot this effort using MeTTa for Hyperon.

**Significance for Hyperseed:** This is the direct engineering precursor. The Hyperseed-1 Alpha1 ontology (~90 concepts, 2024) is the realized version of what this manuscript attempted with ~50 concepts in 2013.

### 4. Embodied Communication Prior (ECP)

A hypothesis about the structure of the prior distribution governing human-like intelligence. Defines five modalities of communication between embodied agents in a shared world:

| Mode | Description | Memory Type Analog |
|------|-------------|-------------------|
| **Linguistic** | Semantics interpretable via finite vocabulary combinations | Declarative/semantic |
| **Indicative** | Pointing to parts of shared world or time intervals | Episodic/spatial |
| **Demonstrative** | Performing actions for another to imitate | Procedural |
| **Depictive** | Creating constructions to evoke similar perceptual experience | Sensory/imagery |
| **Intentional** | Explicitly communicating goals | Goal/motivational |

**Key claim:** "Human cognition is probably best decomposed into a vocabulary of primitives where there are primitive concepts corresponding to each of these communication modes."

**Validation:** "Wierzbicka's minimalist primitive-set does seem to touch the ECP bases, as one would expect."

### 5. ECP++ Extension

Adding psi phenomena (1-1 telepathy, Global Consciousness type synchronicity) to ECP → ECP++.

**Consequence:** "We would get primitives for spiritual/cosmic phenomenological experience as well."

**Significance:** This is the seed for Hyperseed-1's panpsychism commitment and its inclusion of Self-Transcendence as a core ontological concept.

### 6. Critique of Carnap-Style Formalization (the Counterexample Problem)

The pattern identified:
1. Propose formal definition (e.g., "knowledge = justified true belief")
2. Clever wonks find counterexamples
3. Refine definition to cover counterexamples
4. More counterexamples emerge
5. "Endless and pointless intellectual exercise"

**Chalmers' diagnosis:** The counterexample-generators are appealing to "a priori scrutability" — an intuitive understanding that exceeds any finite formalization.

**Goertzel's synthesis:** This is why concepts must be modeled as open-ended, not as single formulas.

---

## Formal Candidates

### FC-1: Magician System / Algorithmic Chemistry Formalism for Reduction

**Type:** Meta-mathematical framework
**Source:** Chaotic Logic (1995), extended in arXiv:2004.05269 (2020)

**Core structure:**
- A set of **atomic entities** that can act on each other to produce new entities
- A set of **combinatory operations** specifying what "act on" means
- A **cost function** over entities and operations
- **Reduction** ≡ expressing one entity as a recursive combination of others that constitutes a simplification (lower total cost)

**Formal property:** Encompasses algorithmic information theory and pattern theory as special cases.

**Relation to Bateson:** "Reduction to primitives" ≈ Bateson's MetaPattern — "Patterns basically being combination operations that, from some perspective, provide a simplified view of the result of the combination."

**Hyperseed significance:** This is the **mathematical foundation** for what "reduction to primitives" even means in the Hyperseed context. It provides the formal semantics underlying all claims about ontological reduction. Notably, it frames reduction as perspective-relative (from some perspective, a simplified view) rather than absolute — which directly feeds the resource-relative primitivity thesis.

---

### FC-2: Concepts as Open-Ended Posets of Approximations

**Type:** Philosophical/formal ontological thesis
**Synthesis of:** Carnap + Chalmers + Goertzel

**Core structure:**
For any commonsense concept C, its "definition" is not a single formalization but a **partially ordered set** (poset) of increasingly refined formalizations:

```
C₁ < C₂ < C₃ < C₄ < ... (ascending chain of approximations)
```

Where:
- Each Cₙ covers more cases / handles more counterexamples than Cₙ₋₁
- A given mind at a given time holds some finite approximation Cₖ
- Once the mind reaches Cₖ₊₁, it recognizes this as a "natural continuation/refinement" of Cₖ
- The full poset may be infinite (concept is genuinely open-ended)
- Some supermind might comprehend the entire series and grok interrelationships

**Analogy to personal identity:** The series C₁ < ... < C₉₉₉ parallels Ben₁ < Ben₂ < ... < Ben₉₉₉ — each stage cannot conceive the next, but once it emerges, it feels like natural continuation.

**Implication for seed ontologies:** "A reduction to primitives like I was trying in Composition of Mind and Reality is giving some approximations to a variety of concepts, say C₁¹, C₂¹, etc. Then an AGI system fed these initial versions as a seed ontology will generate further approximations in the series."

**Hyperseed significance:** This is the theoretical justification for why Hyperseed-1's ~90 concepts don't need to be "correct" — they need to be adequate *initial* approximations that an AGI can refine. This directly motivates the "upbringing" metaphor in Hyperseed-1.

---

### FC-3: PAC (Probably Approximately Correct) Framing of Semantic Primitives

**Type:** Quantitative framework / scaling hypothesis
**Novelty:** HIGH — this is Goertzel's signature contribution in this article

**Core insight:** The question is NOT "Can all concepts be reduced to N primitives?" (binary, likely answer: no). The question IS "How does primitive coverage scale with the number of primitives?"

**Formal definitions:**

```
ps(p, e) = number of primitives needed to generate p% of human concepts within error e

ps*(n) = inverse of ps; gives coverage quality r = p·(1−e) for an optimally chosen set of n primitives
```

**Scaling hypothesis:** ps*(n) may have a **sigmoid shape** — if so, the inflection point determines whether a small set of primitives can cross a useful coverage threshold, with a "huge fat tail" of phenomenal primitives etc. needed for exhaustive coverage.

**Connection to Chalmers:** "Any small finite set of primitives is likely to be merely what computer scientists call PAC, Probably Approximately Correct."

**Hyperseed significance:** This reframes the entire Hyperseed project. The ~90 concepts of Hyperseed-1 are not claimed to be sufficient (that would be Wierzbicka-style minimalism). They're claimed to be past the inflection point of ps*(n) — providing high enough coverage that AGI inference guidance becomes practical. The PAC framing is what makes the project scientifically tractable rather than philosophically quixotic.

---

### FC-4: Resource-Relative Primitivity

**Type:** Meta-ontological principle
**Status:** Explicitly argued in article

**Thesis:** Whether concept X is "primitive" or "derived" is subjective relative to:
- The perceiving system
- The point in time
- The computational resources available

**Formulation:** "'X is primitive' is a provisional assumption made by a certain mind in a certain context, which is fine... It just means 'I can't see how to analyze this into a composition right now.'"

**Stronger formulation:** "Given the amount of resources I'm willing/able to devote to this particular cognitive process, within the scope of this process I must provisionally assume X is indecomposable."

**Examples:**
- "Red" — primitive for sighted person, irrelevant for blind person
- "Magenta" — primitive or derived depending on culture
- "Psychosocial self" and "physical world" — feel primitive but are complex derived constructs
- Quarks → partons → subpartons — "maybe it goes all the way down... but for doing anything practical given my resource limitations I have to stop decomposing somewhere"

**Analogy:** "Much like it's a bit arbitrary which set of vectors one takes as basis for a vector space."

**Hyperseed significance:** This principle is why Hyperseed-1 can include high-level concepts like "Society" and "Emotion" as ontological core concepts despite their obvious compositionality. The basis choice is pragmatic, not metaphysically privileged. This also provides theoretical backing for why different AGI systems might benefit from different primitive sets.

---

### FC-5: Meaning as Fuzzy Set of Mind-Patterns (PLN Integration)

**Type:** Formal semantics thesis
**Source:** Goertzel's prior writings + PLN implementation

**Core claim:** The meaning of a proposition = the set of thoughts/patterns it spurs in some agent's mind (fuzzy set, not crisp).

**Agreement with Chalmers:** Chalmers "considers the meaning of a proposition as the set of thoughts the proposition spurs in some agent's mind... which basically is the same as the 'meaning as a fuzzy set of patterns in a mind' notion I've articulated in various writings."

**PLN implementation:**
- Fuzzy set of patterns ≈ property-set (intension)
- Manifested in PLN as kernel-PCA vector embeddings of Atoms based on their intensions (arXiv:2005.12535)
- This is why Chalmers-style reduction is "intensional" in PLN sense
- Integrated with possible worlds semantics via PLN quantifiers as third-order probabilities (in the PLN book)

**Hyperseed significance:** Provides the formal semantic machinery for the poset-of-approximations thesis (FC-2). If meanings are fuzzy pattern-sets, then partial orderings of concept approximations are naturally modeled as subset/refinement orderings on these fuzzy sets. This is the bridge between the philosophical claims and the PLN implementation.

---

### FC-6: Embodied Communication Prior as Primitive Derivation Method

**Type:** Systematic methodology for generating primitive sets

**Proposal:** Rather than choosing primitives ad hoc (Wierzbicka) or exhaustively (Cyc), derive them systematically from the ECP++:

1. Start with ECP++ and its five communication modes
2. For each mode, identify what primitive concepts are needed to support it
3. These primitives constitute the core vocabulary

**Advantages over alternatives:**
- More systematic than Wierzbicka (derives from theory rather than linguistic intuition)
- More constrained than Cyc/SUMO (bounded by communication modes rather than open-ended formalization)
- Grounded in embodiment (not purely abstract/logical)

**Hyperseed significance:** This is the proposed *methodology* for constructing Hyperseed's primitive set. While Hyperseed-1 as published doesn't explicitly follow this algorithm, the concepts it includes do "touch the ECP bases" as Goertzel notes of Wierzbicka.

---

## Connectivity Map

### Temporal/Genealogical Chain

```
Leibniz (Universal Characteristic)
    │
    ▼
Carnap (Aufbau, logical reduction)
    │
    ├──────────────────────────────────▶ Cyc / SUMO (maximalist failure mode)
    │
    ▼
Wierzbicka (NSM, ~65 primitives)         Goertzel (1995) Chaotic Logic
    │                                          │ (magician systems)
    │                                          │
    ▼                                          ▼
Chalmers (2012) Constructing the World   Goertzel (2009) ECP
    │ (PQTI, top-down feasibility)            │
    │                                          │
    ▼                                          ▼
Goertzel (2013) Composition of Mind      Goertzel (2020) Occam's Razor paper
    │ and Reality (~50 primitives,            │ (arXiv:2004.05269)
    │  quasi-Atomese, unfinished)             │
    │                                          │
    └──────────┬───────────────────────────────┘
               │
               ▼
    ★ THIS ARTICLE (2022-03-14) ★
    "Can All Human Concepts Be Reduced?"
    [Philosophical synthesis + PAC framing + ECP++ + poset thesis]
               │
               ├──▶ MeTTa language design (ongoing)
               │
               ├──▶ Minecraft/SophiaVerse prototype plan
               │
               ▼
    Hyperseed-1 Alpha1 (2024-11-27)
    [~90 concepts, inference guidance, full formalization]
               │
               ▼
    Hyperseed v2 (2026-03-05)
    [NSM integration, expanded scope]
               │
               ▼
    Linguistic Universals series (2026-05/06)
    [Cognitive architecture implications]
```

### Cross-Concept Dependency Map

```
Magician Systems ──formalizes──▶ "Reduction to Primitives"
       │                               │
       │                               ├──equivalent to──▶ Bateson's MetaPattern
       │                               │
       └──extended by──▶ Combinational Computational Model (2020)
                                       │
                                       ▼
                              PAC Coverage Function ps(p,e)
                                       │
                                       ├──quantifies──▶ Wierzbicka (too few? past inflection?)
                                       │
                                       ├──quantifies──▶ Cyc/SUMO (fat tail region)
                                       │
                                       └──motivates──▶ Hyperseed-1 (~90 = past inflection?)

ECP (5 communication modes) ──derives──▶ Required Primitive Vocabulary
       │                                          │
       ├──corresponds to──▶ Human memory types     │
       │                                          │
       └──extended to──▶ ECP++ (+ psi)            │
                              │                    │
                              └──adds──▶ Spiritual/cosmic primitives
                                                   │
                                                   ▼
                                          Chalmers' PQTI
                                          (P + Q + I + T)
                                               │
                                               └──"each ECP mode combines P, Q, I"

Concepts-as-Posets ──justifies──▶ Seed Ontology Approach
       │                               │
       ├──analogy──▶ Personal Identity  │
       │            (Ben₁<...<Ben₉₉₉)  │
       │                               │
       └──formalized by──▶ Meaning as  ├──implemented in──▶ PLN intensions
                           fuzzy sets   │
                                       ▼
                              "Upbringing" metaphor
                              (Hyperseed-1, 2024)
```

### Connections to Other Scanned Entries

| Entry | Connection |
|-------|-----------|
| **Hyperseed-1 (2024-11-27)** | Direct descendant; realizes the research program announced here. The ~90 concepts are the "Composition of Mind and Reality" reboot this article promises. PQTI framework, inference guidance strategy, and open-endedness thesis all carry forward directly. |
| **Hyperseed v2 (2026-03-05)** | Fulfills the NSM integration hinted here via Wierzbicka; extends PAC coverage by expanding the primitive set. |
| **Linguistic Universals Pt1–3 (2026-05–06)** | Develops the ECP→primitives derivation method implicitly proposed here; connects linguistic structure to cognitive architecture as Wierzbicka does for semantics. |
| **Tensor Logic (2025-12-16)** | Provides neural-symbolic bridge for implementing the magician system / algorithmic chemistry formalism in a differentiable framework. |
| **Evidence-Logic-Energy (2026-03-10)** | Extends the formal semantics (meaning as fuzzy pattern-sets) into quantum logic territory via PLN→QLN. |
| **Paraconsistent AGI (2026-01-06)** | Develops the paraconsistency thread mentioned here (tolerating inconsistency in concept approximations). |
| **Origin of Life / Chemical-Alkaline (2026-04/05)** | The "algorithmic chemistry" framing of the magician system connects naturally to literal chemistry in these articles. |
| **Quaternionic Physics (2026-05-15)** | Addresses the "physics as primitives" question this article raises and rejects as insufficient. |

### Key References (from article)

| Reference | URL/Citation | Content |
|-----------|-------------|---------|
| Wierzbicka NSM | https://intranet.secure.griffith.edu.au/schools-departments/natural-semantic-metalanguage | Natural Semantic Metalanguage home page |
| Occam's Razor paper | arXiv:2004.05269 | Combinational computational model; magician system extension |
| ECP paper | http://goertzel.org/dynapsyc/2009/EmbodiedCommunicationPrior.pdf | Embodied Communication Prior formal definition |
| PLN intensions paper | arXiv:2005.12535 | Kernel-PCA vector embeddings of Atoms based on intensions |
| Chalmers | *Constructing the World* (book) | PQTI framework, scrutability, conceptual reduction |
| Buddhist Logic | Stcherbatsky, *Buddhist Logic* (2 vols) | Building reality from sense-data + assumptions |
| CogPrime | https://wiki.opencog.org/w/CogPrime_Overview | Cognitive architecture context |
| OpenCog Hyperon | https://wiki.opencog.org/w/Hyperon | Target platform for the reduction effort |
| MeTTa language | https://wiki.opencog.org/w/Hyperon:Atomese | Functional language for Hyperon |
| Psi article | https://bengoertzel.substack.com/p/exploring-the-reality-of-psi | Basis for ECP++ extension |

---

## Notes

- **Genesis status:** This article is the **philosophical birth certificate** of the Hyperseed program. While earlier work (Chaotic Logic, ECP, Composition of Mind and Reality) contributed building blocks, this is where they were synthesized into a coherent research program with a clear mathematical framework (PAC coverage), a derivation methodology (ECP++→primitives), and a target implementation (MeTTa/Minecraft).

- **PAC framing is the key innovation:** The most lasting contribution of this article to the Hyperseed program is the shift from "Can concepts be reduced?" (binary philosophical question) to "How does coverage scale with primitive count?" (quantitative engineering question). This reframing is what makes Hyperseed-1's ~90 concepts scientifically defensible rather than philosophically arbitrary.

- **The ps*(n) sigmoid hypothesis** is never tested or elaborated beyond this article (as of scanned entries). This remains an open formal question: does conceptual coverage follow a sigmoid curve with respect to primitive count? If so, where is the inflection point? This is potentially formalizable using the Hyperseed-1 ontology as a test case.

- **ECP++ methodology** (derive primitives from communication modes + psi) is proposed but never explicitly executed. Hyperseed-1's concept selection appears to be more intuitive/tradition-guided. Systematically applying the ECP++ derivation method to Hyperseed's existing concepts could validate or extend the ontology.

- **The "Composition of Mind and Reality" manuscript** is referenced but unpublished. Its ~50 quasi-Atomese formalizations would be extremely valuable for comparison with Hyperseed-1's ~90 concepts — tracking what was kept, dropped, and added over the 2013→2024 evolution.

- **Concepts-as-posets thesis** has deep implications for Hyperseed formalization: each Hyperseed concept entry should be understood as one approximation in a potentially infinite ascending chain, not as a definitive formalization. This aligns with Hyperseed-1's explicit "revisable upbringing" framing.

- **Resource-relative primitivity** means the "right" primitive set is not unique — it depends on the AGI system's computational budget, embodiment, and task domain. Minecraft/SophiaVerse primitives may differ from real-world primitives. This has implications for whether Hyperseed should maintain multiple domain-tuned primitive sets.

- **Chronological note:** At 2022-03-14, this is one of the earliest posts on the Substack (started 2021). Only 8 posts precede it. The proximity to "How Superhuman Superminds Will (Mostly) Transcend Suffering" (2022-03-12, two days earlier) suggests a period of intense philosophical production.
