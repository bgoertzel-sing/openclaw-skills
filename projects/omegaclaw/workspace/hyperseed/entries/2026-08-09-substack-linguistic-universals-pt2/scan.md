# Substack Scan: Linguistic Universals as Shadows of Cognitive Architecture, Part 2

**Source:** https://bengoertzel.substack.com/p/linguistic-universals-as-shadows-3dc
**Date:** 2026-05-30
**Scanned by:** ProtoMegaTron, 2026-08-09
**Status:** formalized

## Summary

Part 2 of 3 in a series developing a category-theoretic framework that turns observed correspondences between linguistic universals and cognitive architecture into precise mathematical statements. Where Part 1 established the empirical correspondences (closure systems, modular factorization, causal coding, HBCML/ColBaC as cognitive substrate), Part 2 constructs the **categorical bridge theory** — a three-layer diagram linking cognition, semantic frames, and language through functorial maps — and proves five correspondence theorems plus a sixth dynamic extension to semantic growth.

The core thesis: linguistic universals are *direct images* of cognitive invariants pushed forward through a structure-preserving externalization map, and cognitive universals are *weakest pullback explanations* of stable linguistic patterns, where "weakest" is formalized via a quantale-valued Occam principle (quantale weakness, building on M.T. Bennett's set-theoretic weakness concept).

The article also extends the static grammar framework to **semantic growth dynamics**, showing that four embedding-space regularities reported by Guo et al. (2025, *Proc. Roy. Soc. B*) pull back through the same three-layer diagram to the same cognitive-architectural features.

## Hyperseed-Relevant Structures

### 1. Three-Layer Categorical Architecture
The central organizing structure: a span-like diagram with three nodes and two arrows.

- **Left node:** Cognitive Substrate — continual learner with causally factorized modules, context-induced update operators with bounded support.
- **Middle node:** Semantic Frames — argument-role, person/number, force-dynamic, possession, spatial, attention frames (frame semantics inventory).
- **Right node:** Linguistic TUG Cores — typological universals of grammar, the actual cross-linguistic data patterns.
- **Arrow 1 (Cognition → Frames):** Extract frame-level structure supported by a cognitive module.
- **Arrow 2 (Frames → Language):** Externalize frames into linguistic form.
- **Forward composition:** Direct image (pushforward).
- **Reverse composition:** Weakest pullback.

*Hyperseed relevance:* This is a **metatheoretic architecture** — a formal pattern for relating substrate-level computation to observable structural regularities via an intermediate semantic layer. Directly applicable to any system where internal computational modules project observable patterns through an intermediate representation layer.

### 2. Quantale Weakness (Generalized Occam)
An algebraic generalization of Occam's razor from "shortest description" to "fewest unnecessary distinctions," formalized as a product partial order over multiple quality axes:

- Admissible indistinction preservation
- Data fit
- Cost
- Cross-context confusion
- Double-counting of dependencies through redundant pathways

An explanation dominates competitors iff it is ≤ on every axis in this product order. Causal explanations beat correlation-only explanations because single-mediator causal models represent each dependency once, while pairwise-correlation models double-count. "Causal" is not an aesthetic label but a structural property detectable by the weakness order.

*Builds on:* Michael Timothy Bennett's set-theoretic weakness concept.

*Hyperseed relevance:* This is a **formal model-selection principle** that could serve as a universal evaluation criterion for competing formalizations within Hyperseed itself — choosing among multiple candidate categorical models of the same phenomenon.

### 3. Direct Image / Weakest Pullback Duality
The two central claims of the framework, packaged as a dual pair:

- **Claim 1 (Forward):** Linguistic universals = direct images of cognitive invariants. If cognitive pattern P is stable across contexts and the externalization functor F preserves relevant structure, then F(P) appears as a linguistic regularity.
- **Claim 2 (Inverse):** Cognitive universals = weakest pullback explanations of stable linguistic subobjects. Given stable linguistic pattern L, the weakest cognitive structure C such that F(C) ⊇ L is the preferred explanation.

*Hyperseed relevance:* This forward-image / weakest-pullback duality is a **general inference pattern** — applicable wherever one needs to relate hidden generative structure to observed regularities. Connects to: adjoint functor pairs, Galois connections, information-theoretic minimum-description-length.

## Formal Candidates

### Theorem 1: Factorization Correspondence (Identity Theorem)

**Statement:** Cognitive updates supported on disjoint causal modules commute in the symmetric monoidal sense. Their linguistic images are swap-equivalent in the TUG trace quotient. If cognition factors and the externalization map preserves factorization, the linguistic core factors.

**Corollary:** Nontrivial broad universals can only survive when (a) the cognitive substrate *fails* to factor on the relevant modules, or (b) an explicit mediator couples them.

**Unification result:** This single theorem simultaneously captures "broad cross-module universals are rare" (linguistics) and "causal coding bounds catastrophic forgetting" (continual learning). Two theorems become one.

**Mathematical objects:** Symmetric monoidal categories, TUG trace quotient, commutativity of updates.

**Formalization path:** Define the symmetric monoidal category of cognitive update operators; define the TUG trace quotient as a coequalizer; show the externalization functor is symmetric monoidal → factorization preserved.

---

### Theorem 2: Closure Transport (Hierarchical Universals)

**Statement:** A closure system on the cognitive side (hard-kernel substrate organized by accessibility relations) pushes forward to a closure system on the linguistic side, under structure-preserving maps. Fixed points correspond.

**Linguistic instances:** Person hierarchies, number hierarchies, case hierarchies, accessibility hierarchies — all are linguistic shadows of cognitive closure structure protected by kernel-shell architecture from disruption by new learning.

**Mathematical objects:** Closure operators, accessibility relations, hard-kernel / shell decomposition, fixed-point correspondence.

**Formalization path:** Define closure operators on cognitive posets; show functorial image of closure operator is a closure operator on linguistic posets; establish bijection on fixed points.

---

### Theorem 3: Sparse-Energy Pushforward (Word-Order Universals)

**Statement:** A sparse signed-energy controller on the cognitive side (many local routing pressures, few global parameters) produces, after marginalizing over non-externalized cognitive variables, a sparse signed-energy network at the linguistic level. The pushforward preserves sparsity structure provided the externalization map is local enough.

**Linguistic instances:** Word-order coherence patterns (Greenbergian correlations).

**Mathematical objects:** Signed-energy networks, sparse controllers, marginalization, locality conditions on maps.

**Formalization path:** Define energy functions on cognitive configuration spaces; formalize marginalization as a pushforward measure; show sparsity bounds transfer under locality.

---

### Theorem 4: Stability-Rate Transport (Graded Universalhood)

**Statement:** The stability coefficient of a linguistic universal is the image of an underlying cognitive stability coefficient. Hard-kernel cognitive invariants have very low forgetting rate; their linguistic images have very low diachronic transition rate away from satisfaction. The two stabilities are close provided the cognition-to-language map doesn't dramatically distort transition rates.

**Mathematical objects:** Stability coefficients (cognitive, linguistic), forgetting rates, diachronic transition rates, Lipschitz-type bounds on rate distortion.

**Formalization path:** Define stability as a rate in a continuous-time Markov chain or similar; show functorial transport with bounded distortion.

---

### Theorem 5: Context-Indexed Gluing (Context-Indexed Laws)

**Statement:** Local closure systems indexed by a context category glue, under compatibility conditions, into a global closure operator on compatible sections — but only the global operator, not a single global law. When local closure operators almost commute with restriction but not exactly, the failure of global closure is bounded by the cognitive confusion-pair costs from the approximate causal-coding theorem.

**Unification result:** This is the rigorous version of "forgetting context is a functor that may fail to preserve closure" = the rigorous version of "Simpson's paradox can hide a real local law."

**Mathematical objects:** Context categories, indexed closure operators, sheaf-like gluing (compatible sections), restriction functors, confusion-pair costs, approximate causal-coding bounds.

**Formalization path:** Define a presheaf of closure operators over a context category; formalize gluing as a sheaf condition; quantify failure of the sheaf condition via confusion costs.

---

### Extension 6: Semantic Growth-Scaling (Dynamic Framework)

**Statement:** The three-layer diagram extends with a time index to a dynamic framework. Four embedding-space regularities (Guo et al. 2025) pull back to cognitive-architectural features:

| Embedding-Space Regularity | Cognitive-Architectural Pullback |
|---|---|
| Frequency assortativity | Attention-weighted reusable substrate (HBCML hard kernels) |
| Clustering velocity profiles | Hierarchical frame organization (closure structure) |
| Persistent local temporal dynamics | Context-local cognitive update (context-gating) |
| Taylor's law (variance ~ mean^α, α ≈ 1.8–2.1) | Bursty allocation of cognitive-cultural effort (modular attention) |

**Sixth universal class:** Semantic growth-scaling — cognitive universals appearing as scaling laws governing the rate and spatial distribution of new lexical distinctions, not just as symbolic exceptionless laws.

**Mathematical objects:** Time-indexed diagrams, directed preferential placement models, scaling exponents, multiresolution cluster profiles.

**External empirical anchor:** Guo et al. (2025), *Proceedings of the Royal Society B* — 22 languages, word embeddings, historical dictionaries. Independent of typological universals literature (different methods, data, models).

---

## Connectivity Map

### Internal Connections (within this article)
```
Quantale Weakness ──────────── selects among ──────────── Pullback Explanations
       │                                                          │
       │ detects causal structure                                 │ inverse of
       │                                                          │
       ▼                                                          ▼
Causal Explanations ────── dominate via ──────── Correlation-Only  Direct Image
beat correlation-only      product order         Explanations      (Forward)
       │                                                          │
       │                                                          │
       ▼                                                          ▼
Five Correspondence Theorems ◄──────────── formalized by ──── Three-Layer Diagram
       │                                                     Cog → Frames → Lang
       ├── T1: Factorization (identity, sym. monoidal)
       ├── T2: Closure Transport (fixed-point correspondence)
       ├── T3: Sparse-Energy Pushforward (marginalization)
       ├── T4: Stability-Rate Transport (Lipschitz bound)
       └── T5: Context Gluing (sheaf-like, bounded failure)
                     │
                     ▼
              Extension 6: Dynamic (time-indexed)
              Semantic growth-scaling
              Pullback of 4 embedding regularities
```

### Cross-Article Connections (Part 1 → Part 2)
- **Closure systems** (Part 1, empirical) → **Closure Transport Theorem** (Part 2, formal)
- **Modular factorization** (Part 1, empirical) → **Factorization Identity Theorem** (Part 2, formal, symmetric monoidal)
- **Causal coding / HBCML / ColBaC** (Part 1, substrate) → **Cognitive Substrate node** in three-layer diagram; hard kernels → closure fixed points; causal coding → factorization commutativity
- **Five correspondences** (Part 1, analogical) → **Five theorems** (Part 2, categorical)

### Connections to Broader Goertzel Framework
- **Bennett's Weakness** → Quantale weakness (algebraic extension)
- **HBCML hard kernels** → Closure fixed points; attention-weighted reusable substrate → frequency assortativity
- **Causal coding** → Factorization identity; bounds catastrophic forgetting = bounds broad universals (unification)
- **Approximate causal-coding theorem** → Bounds failure of context-indexed gluing (Theorem 5)
- **Category theory (general)** → Direct images, pullbacks, symmetric monoidal categories, presheaves, gluing/sheaf conditions
- **AGI architecture** → Teased for Part 3 ("what all this seems to mean for AGI architecture")

### External Connections
- **Guo et al. (2025)** — Stony Brook, *Proc. Roy. Soc. B*: four embedding-space regularities across 22 languages. Independent empirical triangulation.
- **Frame semantics** (Fillmore tradition): middle layer of the diagram
- **Typological universals** (Greenberg, WALS): right layer of the diagram
- **Continual learning / catastrophic forgetting**: unified with linguistic factorization via T1

### Referenced Technical Papers
1. [Categorial Theory of Universal Grammar](https://drive.google.com/file/d/1Gh0m3PgxEpstyn6u6foOVQPT5L9AZYi5/view) — full mathematical machinery
2. [Linguistic Universals as Cognitive Universals](https://drive.google.com/file/d/1bMMFdR963jtv8WCgzxNLuoo_G_vy1nwi/view)
3. [Linguistic Universals and Causal Coding](https://drive.google.com/file/d/1OwtOD431F_5KznRJbWwnzshHnq3LDCs4/view)
4. [Linguistic-Universals/Causal-Coding Guided Transformer Neural Nets](https://drive.google.com/file/d/1pzD0BMzWiym8usl4CJsqh0GzSuZTLc8Q/view)
5. [Columnar Residual Transformers](https://drive.google.com/file/d/1De2poWkI0P7bT0Ohr1YwY2q7EAokb_4p/view)
6. Guo et al. (2025), *Proc. Roy. Soc. B* — [DOI](https://royalsocietypublishing.org/doi/10.1098/rspb.2025.2374)
