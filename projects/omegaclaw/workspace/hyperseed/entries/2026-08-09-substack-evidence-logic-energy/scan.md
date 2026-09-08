# Substack Scan: Evidence Is to Logic What Energy Is to Physics

**Source:** https://bengoertzel.substack.com/p/evidence-is-to-logic-what-energy
**Date:** 2026-03-10
**Scanned by:** ProtoMegaTron, 2026-08-09
**Status:** formalized

## Summary

Ben Goertzel presents an eight-paper arc built on a single governing analogy: **evidence is to logic what energy is to physics**. The idea — gestating for decades — is that if an inference engine is "honest" (neither fabricating evidence nor double-counting it), then a conserved quantity should exist along optimal inference paths, and its conservation should follow from a symmetry argument precisely analogous to Noether's theorem in classical mechanics.

The mathematical substrate chosen is **quantales** — complete lattices equipped with a monoidal product distributing over joins. Different quantales yield different logics (nonneg reals → probabilistic, tropical semiring → shortest-path, Booleans → classical). Starting from this algebraic base, the arc ascends through six levels: (1) commutative conservation and anti-hallucination bounds; (2) non-commutative extensions giving ordering effects and swap-defect bounds; (3) a *-algebra level recovering the Robertson uncertainty principle with no Hilbert space or spectral theory; (4) a conditional reconstruction of quantum mechanics itself from three epistemological axioms plus local tomography; (5) the construction of **Quantum Logic Networks (QLN)**, a typed quantum inference calculus generalizing PLN; and (6) a scalability bridge via ZX-CENF normal forms ensuring QLN degrades gracefully under circuit compression.

The philosophical inversion is profound: physics is not the ground floor — *epistemology* is. Quantum mechanics emerges as the canonical theory of honest reasoning by a situated observer who cannot access all facts simultaneously. QLN then closes the loop: once the evidence algebra is identified as B(ℋ), inference engines can operate *inside it*, unifying the physics of quantum uncertainty with the engineering of uncertain AI reasoning.

## Hyperseed-Relevant Structures

### S1. Quantale as Universal Evidence Algebra

**Definition (Quantale).** A quantale (Q, ≤, ⊗, ⋁) is a complete lattice (Q, ≤, ⋁) equipped with an associative monoidal product ⊗ that distributes over arbitrary joins: a ⊗ (⋁ᵢ bᵢ) = ⋁ᵢ (a ⊗ bᵢ). *[Epistemic label: established mathematics, novel application.]*

**Instantiations:**
- **([0,∞], ≥, +, min):** nonneg reals — probabilistic reasoning.
- **Tropical semiring (ℝ ∪ {∞}, min, +):** shortest-path / Viterbi.
- **({⊤,⊥}, ∧, ∨):** classical propositional logic.
- **B(ℋ) (bounded operators on Hilbert space):** quantum evidence algebra.

*Relevance:* The quantale is the algebraic unifier across the Hyperseed hierarchy — the same structure that governs genenergy in Hyperseed-v2 governs evidence conservation in inference. This makes quantales a candidate for the "ur-algebra" of the Hyperseed ontology.

### S2. Forward/Backward Factors and Reinforcement

**Definition (Reinforcement).** Given an inference path π through a proof graph, define forward factors f(v) and backward factors g(v) at each node v. The **reinforcement** at v is ρ(v) = f(v) ⊗ g(v).

*Relevance:* Directly parallels the genenergy construction in Hyperseed-v2. Reinforcement is the inference-side analogue of energy density in the ontological framework.

### S3. Discrete Quantale Noether Theorem

**Theorem (Discrete Quantale Noether, Paper 1).** Along geodesic (optimal) inference paths in a quantale-valued proof graph, the reinforcement ρ is constant.

*Proof method:* Purely lattice-theoretic — uses only distributivity of ⊗ over ⋁ and set-inclusion of paths through a node within the set of all paths. *[Epistemic label: proved theorem.]*

*Relevance:* This is the keystone. It establishes that evidence conservation is not an engineering desideratum but a mathematical consequence — the exact analogue of energy conservation via Noether's theorem. This bridges Hyperseed's genenergy concept to formal logic.

### S4. Five Evidence Conservation Theorems (Paper 2)

**Theorem (Hallucination Bound).** Conclusion strength is bounded by premise evidence mass. No inference chain can manufacture support absent in its premises. *[Proved.]*

**Theorem (Weakness-Bounded Leakage).** Reordering near-commutative inference steps introduces discrepancy bounded by their pairwise "weakness" — a quantale-valued measure of how much order matters. Enables safe parallel/asynchronous inference. *[Proved.]*

**Theorem (Evidence Monotonicity / Quantale Data-Processing Inequality).** Capsule-respecting inference cannot increase total evidence content. *[Proved.]*

**Theorem (Join-Collision Entropy Non-Decrease / Logical Second Law).** Under join-bistochastic inference maps, evidence concentration can only decrease — the logical analogue of the second law of thermodynamics. *[Proved.]*

*Relevance:* These four theorems (plus the Noether theorem) constitute a complete "thermodynamics of inference." They provide rigorous anti-hallucination guarantees, safe concurrency bounds, and entropy-increase constraints that could ground Hyperseed's treatment of information flow and dissipation.

### S5. Non-Commutative Extension and Noether Anomaly (Paper 4)

**Observation.** In non-commutative quantales, the Noether theorem splits:
- Left reinforcement ρ_L = f ⊗ g: **conserved** (by associativity alone).
- Right reinforcement ρ_R = g ⊗ f: **not conserved**.
- The discrepancy ρ_L − ρ_R (or its quantale-valued analogue) is the **Noether anomaly** — measuring the irreducible ordering cost of non-commutativity.

**Swap-defect bounds:** Quantitative statements about how much results change when factors are reordered. *[Proved at Level 0.]*

*Relevance:* Non-commutativity is the bridge from logic to quantum mechanics. The Noether anomaly is a new structural invariant with no prior analogue in the Hyperseed framework — a candidate for formalization as a "measurement of non-commutativity cost" in the ontology.

### S6. Algebraic Uncertainty Principle (Paper 5)

**Theorem (Quantale Cauchy-Schwarz / Robertson via *-Algebra).** At "Level 2" — a unital *-algebra over ℝ or ℂ with a positive state — a purely algebraic Cauchy-Schwarz inequality yields the Robertson uncertainty relation directly, with **no Hilbert space, no spectral theory, and no physics assumed**. *[Proved.]*

*Relevance:* This result is remarkable for Hyperseed because it shows the uncertainty principle is a purely algebraic fact about non-commutative evidence algebras. It supports the ontological thesis that epistemic constraints (uncertainty, complementarity) are more fundamental than physical substrate.

### S7. Conditional Reconstruction of QM (Paper 6)

**Theorem (Epistemic Reconstruction).** Three epistemological axioms:
1. **Situatedness:** the observer cannot access all facts simultaneously.
2. **Conservation:** evidence is neither fabricated nor overcounted.
3. **Minimality:** non-commutativity is as featureless as possible.

force the evidence lattice to be the closed-subspace lattice of a Hilbert space over ℝ, ℂ, or ℍ (via Solèr's theorem). A fourth axiom — **local tomography** (joint states of composites are determined by local statistics) — selects ℂ. *[Conditional reconstruction — relies on Solèr's theorem.]*

**Interpretive mappings:**
- States = evidence distributions.
- Observables = evidence sortings.
- Born rule = evidence evaluation.
- Uncertainty principle = cost of situatedness.
- Complementarity = structure of what cannot be simultaneously observed.

*Relevance:* This is the deepest connection to Hyperseed's philosophical program. If quantum mechanics is *derived from* the structure of honest situated reasoning, then Hyperseed's ontology — which grounds reality in self-referential observation loops — gains a concrete mathematical pathway to quantum structure. The three axioms (Situatedness, Conservation, Minimality) could become axioms in the Hyperseed formal system.

### S8. Quantum Logic Networks (QLN) — Core Framework (Paper 7)

**Definition (QLN).** A Quantum Logic Network is an inference system where:
- **Evidence states** are density operators ρ ∈ B(ℋ), ρ ≥ 0, Tr(ρ) = 1.
- **Evidential links** are quantum channels (CPTP maps).
- **Inference rules** are typed operations in the channel/Choi formalism.

**Four Core PLN Rules Lifted to QLN:**

| PLN Rule | QLN Lift | Mathematical Form |
|----------|----------|-------------------|
| **Deduction** | Channel composition | Choi link product — quantum chain rule generalizing P(C\|A) = Σ_B P(C\|B)P(B\|A) |
| **Abduction** | Petz recovery map | Quantum generalization of Bayes' theorem |
| **Induction** | Convex optimization over Choi matrices | Quantum process tomography as inference |
| **Revision** | Convex combination of density operators | Linear merge preserving positivity and trace |

*Classical reduction:* Each rule reduces to its classical PLN counterpart when all operators are diagonal (commutative evidence algebra). The quantum content lives entirely in off-diagonal coherences. *[Framework definition — concrete, not metaphorical.]*

*Relevance:* QLN is the computational engine that closes the Hyperseed loop. If the Hyperseed ontology grounds reality in self-referential observation, QLN provides the inference calculus for reasoning *within* that reality. It is the natural upgrade path from PLN for any Hyperon/MeTTa system operating in domains with complementary propositions, entangled sources, or context-dependent inference.

### S9. Four Problem Classes Where QLN Exceeds PLN

1. **Complementary propositions:** Noncommuting observables (position/momentum). PLN assigns independent truth values; QLN enforces Robertson bounds — cannot hallucinate simultaneous certainty.
2. **Entangled evidence sources:** Quantum-correlated sources violating Bell inequalities. PLN's capsule system (set intersection) cannot represent them; QLN's entanglement register enables joint processing. *(Concrete merge rules for general entangled overlap: open problem.)*
3. **Context-dependent inference:** Measurement disturbance (gathering evidence about A changes availability of B). PLN's order-independent truth values miss this; QLN channels compose non-commutatively with swap-defect error bounds.
4. **Reasoning about quantum systems directly:** Molecules, quantum computers, quantum channels. PLN collapses to classical outcomes, discarding coherences; QLN represents quantum states and channels natively.

### S10. Scalability Architecture: Block-Diagonal QLN and ZX-CENF (Paper 8)

**Architecture (Block-Diagonal QLN).** Each block of 2–4 related propositions gets a small quantum register (d = 4–16), while inter-block reasoning stays classical. Limits quantum hardware to small subsystems.

**Theorem (Soundness Guarantee).** If circuit simplification is semantically sound (changes diagram, not channel), all QLN rule outputs are exactly unchanged — including genuinely quantum cases. *[Proved.]*

**Theorem (Task-Specific Exactness).** Coarser simplification can be exact for a specific task if it preserves the finite set of input-output statistics the task probes. *[Proved.]*

**Theorem (Linear Error Accumulation).** In a T-step QLN deduction chain under approximate simplification, error grows linearly (sum of per-step errors), not multiplicatively. If the quantum signature exceeds twice the total approximation error, the system is provably still quantum. *[Proved.]*

*Relevance:* This addresses the practical deployment question. Block-diagonal QLN is both hardware-friendly and compiler-friendly — ZX-CENF normal forms at order k are exact (not approximate) for each block's channels. This provides a concrete engineering pathway for quantum-enhanced Hyperon reasoning.

## Formal Candidates

### FC1. Quantale Noether Theorem → Hyperseed Axiom

**Candidate axiom:** In any quantale-valued inference graph, reinforcement is conserved along geodesic paths. This could be adopted as a foundational axiom of the Hyperseed formal system, unifying genenergy conservation (ontological) with evidence conservation (epistemic).

### FC2. Hallucination Bound → Formal Proposition

**Candidate proposition:** For any inference chain C = (c₁, …, cₙ) in a quantale-valued evidence system with premise evidence mass E₀, the conclusion evidence E_n satisfies E_n ≤ E₀. This is a formalizable anti-hallucination guarantee with direct engineering consequences.

### FC3. Three Epistemological Axioms → Hyperseed Axiom Schema

**Candidate axiom schema:**
- (A1-Situatedness) No observer O has simultaneous access to all elements of the evidence lattice L.
- (A2-Conservation) Evidence is neither fabricated nor overcounted along any inference path.
- (A3-Minimality) The non-commutativity structure of L is as featureless as possible (i.e., L does not distinguish a preferred basis).

Together with (A4-Local Tomography), these reconstruct the closed-subspace lattice of ℂ-Hilbert space. This axiom schema is a candidate for inclusion in Hyperseed-v2 as the "observer grounding" component.

### FC4. Noether Anomaly → New Invariant

**Candidate definition:** The Noether anomaly Δ_N(π) of an inference path π in a non-commutative quantale is the discrepancy between left and right reinforcement: Δ_N(π) = ρ_L(π) ⊖ ρ_R(π) (where ⊖ is an appropriate difference operation in the quantale). This is a new structural invariant measuring "non-commutativity cost" — a candidate for formalization as a metatheoretic measure in the Hyperseed ontology.

### FC5. QLN Rule Typing → Category-Theoretic Formalization

**Candidate formalization:** The four QLN rules (deduction, abduction, induction, revision) can be formalized as morphisms in a dagger-compact category where:
- Objects are Hilbert spaces (one per proposition-register).
- Morphisms are CPTP maps (quantum channels).
- Deduction = composition of morphisms (functorial).
- Abduction = Petz recovery (dagger/adjoint structure).
- Induction = optimization in the Choi convex body.
- Revision = convex combination in the state space.

This gives QLN a natural home in categorical quantum mechanics (Abramsky–Coecke) and connects it to the broader categorical structures in Hyperseed-v2.

### FC6. Evidence Entropy Non-Decrease → Formal Arrow of Time

**Candidate proposition:** Under join-bistochastic inference maps in a quantale-valued system, the join-collision entropy H_JC(ρ) satisfies H_JC(Φ(ρ)) ≥ H_JC(ρ). This is the logical second law. The open technical problem noted by the author: rigorously bridging join-collision entropy to von Neumann entropy in the quantum case.

### FC7. Linear Error Accumulation → Engineering Theorem

**Candidate theorem (for Hyperseed engineering layer):** In a T-step QLN deduction chain where each step's channel is approximated within ε_t (in diamond norm or similar), the total output error is bounded by Σ_t ε_t (linear, not exponential). If quantum signature σ > 2·Σ_t ε_t, the approximate system remains provably quantum.

## Connectivity Map

### → Hyperseed-v1/v2

- **Genenergy ↔ Reinforcement:** The reinforcement ρ = f ⊗ g is the inference-side avatar of genenergy. The Discrete Quantale Noether Theorem is the genenergy conservation law restricted to proof graphs. The quantale framework was explicitly developed in connection with Hyperseed-v2's genenergy concept (the author cites this lineage directly).
- **Weakness theory:** The author notes that quantales are "very familiar from last year's work on weakness theory." Weakness — a quantale-valued measure of how much order matters — reappears as the key quantity in the leakage theorem. The Hyperseed ontology's treatment of weakness as a structural primitive gains a new computational interpretation: it bounds the evidence cost of parallel/asynchronous inference.
- **Self-reference and situatedness:** Hyperseed's emphasis on self-referential observation loops maps directly to axiom A1 (Situatedness). The claim that QM emerges from situated reasoning vindicates the ontological priority Hyperseed assigns to the observer.

### → PLN (Probabilistic Logic Networks)

- **QLN generalizes PLN** by lifting all four core rules (deduction, abduction, induction, revision) from classical probability to quantum channels. Every classical PLN computation is a special case (diagonal operators). The capsule system (evidence overlap tracking via set intersection) extends to an entanglement register, though concrete merge rules for entangled capsules are an open problem.
- **Evidence conservation provides PLN with thermodynamic guarantees:** the hallucination bound, leakage theorem, monotonicity, and entropy non-decrease are now proved properties of PLN (and its quantum extension) rather than heuristic desiderata.

### → MeTTa / PeTTa

- **QLN as MeTTa type system extension:** QLN's typed inference rules (density operators, CPTP maps, Choi matrices) could be implemented as a MeTTa type extension — a "quantum reasoning module" for Hyperon. The block-diagonal architecture suggests a practical factoring: classical MeTTa handles inter-block reasoning while quantum registers handle intra-block coherence.
- **PeTTa (parallel MeTTa):** The weakness-bounded leakage theorem directly governs PeTTa's safety — it quantifies how much evidence integrity is lost when inference steps are parallelized or reordered. This provides a formal concurrency guarantee for distributed MeTTa execution.

### → Tensor Logic / Quantale Logic

- **Quantales as the unifying algebraic structure:** The article positions quantales as the algebraic substrate unifying classical logic, probabilistic reasoning, shortest-path computation, and quantum mechanics. This is directly relevant to tensor-logic approaches in the Hyperseed framework — the monoidal product ⊗ in the quantale is the "tensor" operation, and the distributive law over ⋁ is the key structural constraint.
- **Non-commutative quantales → quantum logic:** The non-commutative extension (Papers 3–4) provides the algebraic pathway from tensor logic to quantum logic, with the Noether anomaly as the quantitative bridge.

### → Category Theory

- **Dagger-compact categories:** QLN's structure (Hilbert spaces as objects, CPTP maps as morphisms, Petz recovery as dagger-adjoint) naturally lives in the dagger-compact categorical framework of Abramsky–Coecke. The ZX-calculus (Paper 8) is an established tool in this categorical setting.
- **Quantale-enriched categories:** Proof graphs valued in a quantale are quantale-enriched categories (a.k.a. generalized metric spaces in the Lawvere sense). The Noether theorem is then a statement about enriched functors preserving the quantale-valued "distance." This connects to Hyperseed-v2's category-theoretic formalization of metagraphs.
- **Monoidal functors:** The classical-reduction property (QLN → PLN when operators are diagonal) can be formalized as a forgetful monoidal functor from the quantum category to the classical category, preserving all four inference rules. This is a candidate for inclusion in the Hyperseed categorical framework.

### → Open Problems (as noted by the author)

1. **Channel-level Noether theorem:** Extending the conservation law to the channel (CPTP) level.
2. **Quantum overlap correction for entangled capsules:** Concrete merge rules when evidence sources have quantum correlations.
3. **Join-collision entropy ↔ von Neumann entropy bridge:** Making the logical second law quantitatively precise in the quantum case.
4. **Hardware-specific advantage quantification:** How much does block-diagonal QLN actually beat classical inference on real problems?

These open problems are natural targets for Hyperseed-2 formalization efforts.

---

## Appendix: Paper Series Reference

| # | Title | Focus |
|---|-------|-------|
| 1 | Genenergy for Logic | Reinforcement, Quantale Noether Theorem |
| 2 | Five Theorems on Evidence Conservation | Hallucination Bound, Leakage, Monotonicity, Entropy |
| 3 | Cohomological Double Counting | (Technical — cohomological methods) |
| 4 | Non-Commutative Evidence Conservation | Noether anomaly, swap-defect bounds |
| 5 | The Quantale Cauchy-Schwarz Inequality | Algebraic Robertson uncertainty |
| 6 | QM as Observer-Situated Evidence Conservation | Epistemic reconstruction of QM |
| 7 | Quantum Logic Networks | QLN framework, four rule lifts |
| 8 | QLN and ZX-CENF | Scalability, circuit simplification guarantees |

Papers 1–5: abstract framework. Paper 6: QM reconstruction. Paper 7: QLN calculus. Paper 8: engineering bridge.
