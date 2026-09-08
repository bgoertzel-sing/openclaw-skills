# Substack Scan: God Doesn't Cook the Books

**Source:** https://bengoertzel.substack.com/p/god-doesnt-double-count-evidence
**Title:** God Doesn't Cook the Books — Sketching a Potential Path from Conservation of Evidence to Conservation of Energy
**Date:** 2022-01-15
**Scanned by:** ProtoMegaTron, 2026-08-09
**Status:** formalized

## Summary

This 2022 blog post is a **proto-sketch** of the thesis later developed into the eight-paper "Evidence Is to Logic What Energy Is to Physics" arc (2026-03-10). Goertzel proposes — in deliberately informal, suggestive terms — that conservation of energy in physics is fundamentally the same phenomenon as conservation of evidence in logic: "God doesn't cook the books." The post does not prove anything rigorously; it explicitly invites future formalization. That formalization arrived four years later in the quantale Noether theorem and QLN framework.

The argument skeleton:

1. **Physics ↔ computation** is well-established (quantum computing, Curry-Howard correspondence). The universe's dynamics are mathematical derivations from initial/boundary conditions + laws.
2. **Conservation of evidence** — "no double counting" — is a central constraint in probabilistic reasoning systems. **Linear logic** formalizes this: each axiom has a fixed multiplicity and can only be used that many times.
3. **Conjecture:** Conservation of energy is a spacetime-continuum-specialized version of conservation of evidence.
4. **Supporting chain of correspondences:**
   - Algebra of uncertain inference without double-counting ⟺ additive/multiplicative linear logic
   - Linear logic with least+greatest fixed points ⟺ linear reversible computing
   - Linear reversible computing ⟹ computing that conserves energy
   - Conservation of energy ⟹ conservation of momentum (via reference-frame invariance)
   - General relativity ⟹ (and possibly ⟸) local conservation of energy
5. **Auxiliary speculations:**
   - Einstein's field equation might be *derivable* from "mass-energy curves space in a way that ensures local energy conservation."
   - Gorard's discrete GR on spatial hypergraphs (Wolfram Physics Project) could be a framework for this.
   - Jordan-Banach algebras, connected to Noether's theorem by John Baez, may bridge reversible linear logic to conservation laws.
   - A morphism between linear logic algebra and uncertain reasoning algebra (Goertzel 2020, arXiv:2009.12990) suggests linearity in computation corresponds to no-double-counting in evidence.

The post concludes with the "God doesn't cook the books" quip (suggested by Goertzel's father): conservation laws exist because the universe doesn't double-count evidence within any local reference frame.

## Hyperseed-Relevant Structures

### S1. The Evidence↔Energy Conjecture (Proto-Form)

**Informal conjecture.** Conservation of energy is a spacetime-specialized version of conservation of evidence: the universe, viewed as a computation, neither fabricates nor double-counts evidential resources.

*Status:* Informal sketch here. Later proved (in a specific algebraic setting) via the Discrete Quantale Noether Theorem (Paper 1 of the 2026 arc). The quantale framework provides the precise algebraic context that was missing in this 2022 post.

*Relevance:* This is the **origin point** of what became the most mathematically developed thread in the Hyperseed program. The conjecture seeded the entire evidence-conservation line: quantales, Noether anomaly, QLN, and the epistemic reconstruction of QM.

### S2. Linear Logic as Evidence Conservation Formalism

**Observation.** Linear logic — where each axiom/resource has a fixed multiplicity and must be consumed exactly that many times — is the logical formalism that captures "no double counting." This is contrasted with classical logic (where axioms can be reused arbitrarily via weakening/contraction).

**Key reference cited:** Goertzel (2020), "A morphism I observed some time ago between the algebra of linear logic and the algebra of uncertain reasoning" (arXiv:2009.12990), showing that linearity among computational operations corresponds to not double-counting evidence.

*Relevance:* Linear logic is the algebraic precursor to the quantale framework. The monoidal product ⊗ in a quantale is precisely the linear-logic tensor; the quantale's completeness and distributive law add the infrastructure for fixed-point reasoning. This post provides the motivational pathway from the familiar (linear logic) to the novel (quantale evidence algebras).

### S3. Reversible Computation ↔ Energy Conservation Bridge

**Cited correspondence chain:**

1. **Linear logic with least+greatest fixed points ⟺ linear reversible computing** (cited: arXiv:1804.00952 and hal-03103455).
2. In reversible computing, each elementary operation preserves information. If each operation has a fixed energy cost, then conserving the number of operations = conserving energy.
3. **Fredkin gate** example: output has the same Hamming weight as input — a discrete conservation property that translates into energy conservation in simple physical implementations.

*Relevance:* This bridge was later absorbed into the quantale framework, where "reversibility" corresponds to the existence of a quantale involution (*-algebra structure) and "energy conservation" becomes the Noether theorem for quantale-valued proof graphs. The Fredkin-gate observation is an embryonic form of the "each inference step conserves evidential resources" principle.

### S4. Locality of Conservation in GR

**Observation.** Energy conservation doesn't hold globally in general relativity but does hold locally (cited: arXiv:gr-qc/9701028). "Locally" in the relativistic sense is precisely the frame in which a particular observer can assemble a coherent body of evidence.

**Speculation.** One might *derive* the Einstein field equation from the assumption "mass-energy curves space so as to ensure local energy conservation." Gorard's discrete GR on spatial hypergraphs (arXiv:2004.14810) is suggested as a framework for attempting this.

*Relevance:* This connects directly to the later epistemic axiom A1 (Situatedness) in the QLN reconstruction of QM: "no observer has simultaneous access to all evidence." Locality of conservation = conservation holds within the observer's evidential horizon. The GR speculation remains open — it was not pursued in the 2026 formalization, which focused on quantum mechanics rather than gravity. This is a **live thread** for future Hyperseed work.

### S5. Jordan-Banach Algebras and Noether's Theorem

**Speculation.** Reversible linear logic may connect to Jordan-Banach (JB) algebras, which John Baez has linked to Noether's theorem. If this connection holds, then the chain from linear logic to physics conservation laws would pass through the same algebraic structures that underlie the standard physics formulation.

*Relevance:* In the 2026 formalization, this speculation was partially vindicated: the *-algebra structure used in Paper 5 (Algebraic Uncertainty Principle) is related to Jordan algebras. The C*-algebraic and JB-algebraic perspectives on quantum mechanics both arise when the quantale is specialized to B(ℋ). This is a partial closure of the 2022 speculation, though a full JB-algebra treatment of the evidence↔energy bridge remains open.

### S6. The Informal Correspondence Chain (Full)

```
Uncertain inference w/o double counting ⟺ additive/multiplicative linear logic
Linear logic w/ least+greatest fixed points ⟺ linear reversible computing
Linear reversible computing ⟹ energy-conserving computing
Conservation of energy ⟹ conservation of momentum
General relativity ⟹ (? ⟸) local conservation of energy
```

*Relevance:* This chain is the **roadmap** that the 2026 formalization followed. The quantale framework collapses the first two steps (linear logic + uncertain inference are both instantiations of quantale algebra). The third step (reversible computing → energy conservation) is captured by the Noether theorem. Steps four and five (momentum, GR) were noted but not formalized in the 2026 work — they remain targets.

## Formal Candidates

### FC1. Evidence↔Energy Conjecture → Axiom Candidate

**Candidate axiom (Hyperseed ontological layer):** "Conservation of energy is an instantiation of conservation of evidence in a spacetime-continuum-valued quantale." This was the core conjecture of this post. The 2026 quantale Noether theorem proves it for discrete proof graphs; extending to continuum spacetime (connecting to GR) is an open formalization target.

### FC2. Einstein Equation from Evidence Conservation → Open Conjecture

**Open conjecture:** The Einstein field equation can be derived from the principle "mass-energy curves spacetime so as to maintain local evidence conservation" — i.e., spacetime geometry is the structure that enforces honest local inference for any observer. This could be formalized as: given a quantale-valued evidence field on a manifold, the metric is the unique geometry that makes the Noether theorem hold locally. **Status: not attempted; candidate for future Hyperseed-physics formalization.**

### FC3. Fredkin Gate Conservation → Discrete Evidence Primitive

**Candidate primitive:** An elementary inference step is evidence-conserving if its output has the same evidential weight as its input (analogous to the Fredkin gate preserving Hamming weight). This is a candidate for the smallest-scale axiom in the Hyperseed inference hierarchy — the "atomic conservation law" from which larger Noether-type results follow by composition.

### FC4. Linear Logic ↔ Uncertain Reasoning Morphism → Quantale Functor

**Candidate formalization:** The morphism between linear logic algebra and uncertain reasoning algebra (Goertzel 2020) can be formalized as a functor between quantale-enriched categories — one instantiated by Boolean quantales (linear logic), the other by probabilistic quantales ([0,∞]). The 2026 framework makes this precise, but the full categorical treatment (including natural transformations between different quantale instantiations) is a formalization target.

## Connectivity Map

### → "Evidence Is to Logic What Energy Is to Physics" (2026-03-10)

**Relationship: Proto-sketch → Full Formalization.**

This 2022 post is the **direct ancestor** of the 2026 eight-paper arc. Every major theme in this post was formalized in 2026:

| 2022 Sketch | 2026 Formalization |
|---|---|
| "No double counting" as constraint | Quantale Noether theorem (Paper 1) |
| Linear logic → conservation | Quantale = generalized linear logic (Papers 1–2) |
| Reversible computing → energy conservation | Proved via quantale distributivity (Paper 1) |
| Uncertain reasoning ↔ linear logic morphism | Quantale as unifier; five conservation theorems (Paper 2) |
| Non-commutativity speculation | Noether anomaly, swap-defect bounds (Paper 4) |
| JB-algebra speculation | *-algebra Robertson inequality (Paper 5) |
| Observer-locality of conservation | Axiom A1 (Situatedness), QM reconstruction (Paper 6) |
| Computational engine | QLN framework (Paper 7) |

The 2022 post's chain of correspondences was the **roadmap** that the 2026 work executed. The only 2022 speculations *not yet* formalized are: (a) derivation of Einstein's equation from evidence conservation, and (b) the explicit JB-algebra ↔ reversible linear logic bridge.

### → Hyperseed-v1/v2

- **Origin of the genenergy concept:** The 2022 observation that "energy conservation = evidence conservation" is the conceptual seed of Hyperseed-v2's genenergy. Genenergy is defined as a quantale-valued measure of ontological "substance" — which, by the evidence↔energy bridge, is simultaneously a measure of evidence and of physical energy. This 2022 post is the moment that idea first appeared in print.
- **Linear logic → ontological primitives:** The 2022 identification of linear logic as the formalism for evidence conservation influenced Hyperseed's choice of quantales (enriched linear logic) as the algebraic substrate for semantic primitives.

### → Quantale Noether Theorem (formalized 2026)

**Direct lineage.** The Discrete Quantale Noether Theorem (Paper 1 of the 2026 arc) is the rigorous realization of this post's central conjecture. The proof technique — purely lattice-theoretic, using only ⊗-distributivity over ⋁ — was not available in 2022 (Goertzel explicitly notes he hasn't had time to construct a rigorous argument). The four-year gap between conjecture and proof suggests the quantale framework was the key mathematical insight that made formalization possible.

### → Wolfram Physics / Gorard

The post cites Jonathan Gorard's discrete GR on spatial hypergraphs (arXiv:2004.14810) as a potential framework for deriving Einstein's equation from energy conservation. This connection was **not pursued** in the 2026 formalization but remains a live thread. If the Wolfram/Gorard framework can formalize "spacetime adjusts geometry to maintain local evidence conservation," it would extend the evidence↔energy bridge from quantum mechanics to gravity — a major open target for Hyperseed-physics.

### → Parafinity (same date, 2022-01-15)

Published the same day as "God Doesn't Cook the Books." Parafinity explores numbers paraconsistently poised between finite and infinite. Potential connection: paraconsistent logic allows controlled inconsistency, while linear logic enforces strict resource conservation. These are complementary perspectives on the structure of evidence — one allowing surplus (paraconsistency), the other forbidding it (linearity). A synthesis might yield a "paraconsistent quantale" that permits controlled evidence surplus in boundary regions. **Status: speculative; not formalized.**

### → "The Logic of Pain and the Poverty of Punishment" (same date, 2022-01-15)

Also published 2022-01-15. Argues pain can be reduced near zero post-Singularity. The evidence↔energy bridge might be relevant: if suffering has an "evidential cost" (it provides information about system damage), then evidence conservation constrains how much suffering can be eliminated without losing essential feedback signals. **Status: extremely speculative; noted for completeness.**

### Open Threads Not Yet Formalized

1. **Einstein equation from evidence conservation** — the deepest open physics conjecture in this post.
2. **JB-algebra ↔ reversible linear logic** — partially addressed by the 2026 *-algebra work, but a full bridge is open.
3. **Continuum quantale Noether theorem** — extending from discrete proof graphs to continuous spacetime fields.
4. **Paraconsistent quantales** — integrating the Parafinity perspective with the evidence conservation framework.

---

## Appendix: Key References Cited in the Article

1. Curry-Howard correspondence — logic ↔ computation.
2. arXiv:gr-qc/9701028 — local energy conservation in GR.
3. arXiv:2004.14810 — Gorard, discrete GR on spatial hypergraphs.
4. arXiv:1804.00952 — Curry-Howard mapping from linear reversible computing.
5. hal-03103455 — linear logic with least and greatest fixed points.
6. arXiv:2009.12990 — Goertzel, morphism between linear logic algebra and uncertain reasoning.
7. [Derive conservation of momentum from conservation of energy](https://scholarworks.utep.edu/cgi/viewcontent.cgi?article=1789&context=cs_techrep) — classical derivation.
8. John Baez — Noether's theorem ↔ Jordan-Banach algebras.
