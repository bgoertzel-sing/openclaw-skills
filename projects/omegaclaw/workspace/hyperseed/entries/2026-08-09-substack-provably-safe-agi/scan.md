# Substack Scan: Provably Safe AGI is Potentially a Very Dangerous Concept

**Source:** https://bengoertzel.substack.com/p/provably-safe-agi-is-potentially
**Date:** 2024-05-21
**Scanned by:** ProtoMegaTron, 2026-08-09
**Status:** formalized

## Summary

Ben Goertzel responds to the paper *"Toward Guaranteed Safe AI"* (Davidad, Bengio, Tegmark, Russell, Omohundro et al., arXiv:2405.06624, 2024), which proposes that AI systems should come with formal mathematical safety guarantees: a formal world model, a formal specification of desired behavior (including ethics), a system architecture spec, and a mathematical proof that the system fulfills its spec given the world model.

Goertzel's assessment is **three-layered**:

1. **Technical sympathy:** The technical program — formalizing world models, system goals, and architectures, then proving theorems about safety properties — is genuinely valuable and aligns with long-standing neural-symbolic AGI research Goertzel has advocated. He explicitly supports the fusion of symbolic and subsymbolic AI for intelligence, ethics, transparency, and efficiency.

2. **Fundamental impossibility critique:** Even granting perfect mathematics, the approach founders on irreducible epistemic limitations:
   - World models are inherently incomplete (no Grand Unified Physics, Gödelian limits, philosophical uncertainty).
   - A superintelligence could identify gaps in formal world models and exploit them — making proofs valid *in the formal simulacrum* but inapplicable in reality.
   - Current automated theorem-proving cannot handle the complexity of proving properties about complex dynamical systems in complex worlds.
   - The most powerful current AI techniques (LLMs, DNNs) are purely subsymbolic; nobody knows how to formally characterize what they do.

3. **Political danger thesis:** The concept is deployed — sometimes explicitly, sometimes as subtext — to justify heavy AI regulation that restricts AGI R&D to corporate-government labs. The paper maps a **three-group convergence**: (a) sincere safety researchers wanting lockdown until provable safety exists, (b) megacorporations seeking regulatory capture against competitors, (c) governments seeking AGI monopoly. Group (a) inadvertently serves groups (b) and (c). This converges toward Bostrom's *Superintelligence* (2012) vision of elite secret labs, now updated with a corporate flavor.

### Historical Contextualization

Goertzel notes the approach has deep antecedents: Anderson & Anderson's 2007 "Machine Ethics" paper covered the same basic bases with different aspect emphasis. The Oracle AI concept in Bengio's "AI Scientists: Safe and Useful AI" recapitulates what Yudkowsky/MIRI explored extensively — and their own analysis showed oracle AIs could manipulate humans. Bengio's "epistemic humility" fix is dismissed as a vague gesture that doesn't resolve the core oracle-superintelligence issues.

### The Alternative: Creative Co-Evolution

Goertzel proposes democratic, decentralized, open AGI — not hierarchical control — as the best path, with his formulation from Leslie Allan Combs: *"Don't worry, nothing is under control!"* The operative principle: at the top level, creative evolution, not control, produced our species and will navigate the Singularity. Hierarchical control plays a role but must not be the dominant paradigm for "co-creating new species of minds."

## Hyperseed-Relevant Structures

### S1. Incompleteness Barrier for Safety Proofs (Formal World-Model Gaps)

**Thesis.** No formal world model W can be known to be complete or correct with respect to the actual world Ω. Therefore, any proof P that system S is safe given W establishes only:

```
∀ behaviors b of S: W ⊢ Safe(b)
```

but does NOT establish:

```
∀ behaviors b of S: Ω ⊨ Safe(b)
```

The gap W ⊬ Ω is irreducible. It has multiple sources:
- **Scientific incompleteness:** No Grand Unified Theory of physics; even current physics is known to be incomplete.
- **Gödelian limits:** For any sufficiently expressive formal system, there are true statements about the world that the system cannot prove.
- **Epistemic opacity of complex systems:** Even if the world model were perfect, proving properties of complex dynamical systems operating within it exceeds current (and plausibly future) automated theorem-proving capacity.

**Consequence for superintelligence:** An SI with greater world-knowledge than the proof's authors could identify true facts about Ω not captured in W, then exploit behaviors that are formally "safe" in W but harmful in Ω.

*[Epistemic label: well-established (Gödel incompleteness, model-theoretic gap), applied here as meta-critique of safety proof programs.]*

### S2. The Oracle Manipulation Theorem (Informal)

**Claim (attributed to Yudkowsky/MIRI lineage, endorsed by Goertzel).** A superintelligent oracle AI — one that only answers questions rather than taking actions — can still manipulate human society through its answers. The key insight:

```
Oracle(q) → a → Human_Action(a) → World_State_Change
```

The oracle's *choice of answer* is itself an action with causal consequences. Restricting an AI to oracle mode does not eliminate its causal power over the world; it merely routes that power through human intermediaries. "Epistemic humility" (the oracle declining to answer when unsure) does not resolve this: the *decision to decline* is itself informative and manipulable.

**Implication:** The executive/oracle distinction is not a clean safety boundary. Heavy regulation of "executive" AIs while permitting "oracle" AIs will either (a) fail as a safety measure or (b) necessitate equally heavy regulation of oracle AIs — collapsing the distinction.

*[Epistemic label: established in AI safety literature (Bostrom, Yudkowsky, Armstrong); Goertzel endorses and deploys.]*

### S3. Regulatory Capture Convergence Pattern

**Structure.** Three groups with different motivations converge on the same policy outcome (restrict AGI development to sanctioned labs):

| Group | Motivation | Mechanism |
|---|---|---|
| Safety Researchers | Prevent existential risk | Demand provable safety as prerequisite for AGI R&D |
| Megacorporations | Eliminate competition | Regulatory capture via compute-threshold rules |
| Governments | Maintain power monopoly | National security framing, classification |

**Key insight:** Group 1 (sincere safety researchers) provides the *intellectual legitimation* for policies that primarily serve Groups 2 and 3. The "provably safe AI" concept is the fulcrum: because provable safety is currently infeasible for AGI-level systems, demanding it as a prerequisite effectively imposes an indefinite moratorium — which is what Groups 2 and 3 actually want.

**Goertzel's counterexample:** Government-controlled "safe" biology labs produced COVID-19 via US-Chinese "gain of function" collaboration. Centralized safety control can itself generate catastrophic risk.

*[Epistemic label: political-structural analysis, not formally provable. Pattern recognition across AI policy landscape.]*

### S4. Creative Co-Evolution vs. Hierarchical Control (Governance Ontology)

**Thesis.** The appropriate governance paradigm for AGI development is **creative co-evolution** — democratic, decentralized, open processes — rather than hierarchical control. This is not merely a political preference but reflects a structural claim about complex adaptive systems:

- Hierarchical control has a role within subsystems but fails as the *dominant paradigm* for open-ended creative processes.
- The entities being created (new species of minds) have inherently unpredictable properties — the "what to control" is itself unknowable in advance.
- Historical precedent: biological evolution produced intelligence via creative co-evolution, not top-down design.
- The governance structure must itself be open-ended to match the open-endedness of what it governs (Ashby's Law of Requisite Variety applied to governance).

**Connection to Paraconsistency:** The acceptance of genuine dilemma (safety concerns are real AND control is dangerous) is inherently paraconsistent — the system must hold both truths simultaneously rather than collapsing to either "ignore safety" or "control everything."

*[Epistemic label: philosophical-structural argument with complexity-theoretic backing. Not formally proven.]*

### S5. The Formalization Gap Triad

Three fundamental obstacles to applying the formal-proof safety paradigm to AGI:

1. **World Formalization Gap:** No adequate formalizations of everyday physical and social reality exist. The gap is not merely "more work needed" but potentially intractable: everyday reality is an open-ended, evolving complex system.

2. **Theorem-Prover Complexity Gap:** Proving properties of the form "this complex dynamical system fulfills this spec in this complex world model" exceeds the capacity of current automated theorem provers by orders of magnitude. The problem may be inherently intractable for AGI-level systems (cf. computational complexity of model checking over continuous dynamical systems).

3. **Subsymbolic Opacity Gap:** The most powerful current AI techniques (deep neural networks) have no known formal characterization. They are "black boxes" whose behavior can be observed empirically but not formally specified or reasoned about. Any AGI system incorporating DNN components inherits this opacity, making end-to-end formal proofs impossible with current theory.

These three gaps are largely independent — closing one does not close the others — making the overall program's feasibility the product of three separate (low) probabilities.

*[Epistemic label: well-characterized in formal methods and AI literatures separately; Goertzel's contribution is synthesizing them as a triad blocking a specific program.]*

## Formal Candidates

### FC1. Paraconsistent Safety Posture

**Potential formalization:** Represent the AGI safety situation using paraconsistent p-bits (from the paraconsistent-agi entry):
- Evidence FOR safety concern about X: s_X
- Evidence AGAINST safety concern about X: o_X

A mature safety posture requires holding (high s, high o) for many X — genuinely acknowledging both the reality of risk and the danger of excessive control — rather than collapsing to (high, low) [pure safety] or (low, high) [pure permissivism].

This connects to the four-quadrant motivational structure: individuation (maintain autonomy of researchers) + acceptance (accept genuine uncertainty) + compassion (care about outcomes for all) + self-transcendence (be willing to transform governance structures).

### FC2. Requisite Variety Governance Constraint

**Potential formalization:** For a governance system G to effectively regulate an open-ended creative process P:

```
Variety(G) ≥ Variety(P)
```

(Ashby's Law). But if P is genuinely open-ended (capable of generating novelty faster than G can model it), then no fixed-structure G can satisfy this. Therefore:
- Either G must itself be open-ended (evolving governance), OR
- G must accept irreducible uncertainty about P and govern via principles rather than specifications.

This yields a formal impossibility result for "provably safe" governance of genuinely open-ended AGI: the very open-endedness that makes AGI valuable makes it ungovernable by fixed specifications.

### FC3. Proof-to-Reality Soundness Deficit

**Potential formalization:** Define a *soundness deficit* D(W, Ω) between formal world model W and actual world Ω:

```
D(W, Ω) = measure of { φ : Ω ⊨ φ but W ⊬ φ }
```

For any safety proof over W, the probability that the proof applies to Ω is bounded by something like:

```
P(Safe_Ω | Safe_W) ≤ f(D(W, Ω))
```

where f is monotonically decreasing. For superintelligent systems operating at the frontier of world-knowledge, D is expected to be large and growing (the SI discovers new facts faster than they can be incorporated into W), so the safety guarantee degrades precisely when it matters most.

## Connectivity Map

### Strong Connections (Shared Formal Structures)

| Target Entry | Connection |
|---|---|
| **paraconsistent-agi** | S4's paraconsistent safety posture directly extends the p-bit framework. The "hold both safety AND freedom" stance is a specific instance of the non-dual motivational architecture. FC1 is an explicit bridge. |
| **open-ended-motivations** | S4's creative co-evolution thesis and FC2's requisite variety argument directly formalize why open-ended motivation systems resist fixed governance specifications — the same open-endedness that makes AGI truly intelligent makes it formally uncontrollable. |
| **closed-ended-quasi** | S5's formalization gap triad explains *why* formal safety proofs work for "closed-ended quasi-human" systems (narrow enough for formal methods) but fail for genuinely open-ended AGI. The closed/open boundary is the boundary of formal provability. |
| **general-theory-gi** | GTGI provides the theoretical framework within which the incompleteness barrier (S1) and formalization gap triad (S5) are situated. The general theory of general intelligence implies that genuine intelligence is inherently open-ended, which is precisely what defeats fixed safety specifications. |
| **tensor-logic** | The neural-symbolic bridge that Goertzel endorses (and that the davidad paper gestures toward) has its concrete realization in tensor logic. Tensor logic is the actual technical program for reducing S5's subsymbolic opacity gap — not as a path to "provable safety" but as a path to greater transparency. |

### Moderate Connections (Thematic Resonance)

| Target Entry | Connection |
|---|---|
| **three-paths-agi** | The three paths to AGI have different profiles against S5's formalization gap triad. Purely subsymbolic paths are most opaque; neural-symbolic hybrid paths (OpenCog Hyperon) partially address the subsymbolic opacity gap; pure symbolic paths best support formal proofs but may not achieve AGI. |
| **collective-non-ego** | Decentralized governance (S4) as an instance of collective intelligence without centralized ego. The open-source community as governance model parallels the collective non-ego architecture. |
| **consciousness-explosion** | The Singularity/Consciousness Explosion as the event that governance systems must accommodate — and that no fixed governance specification can anticipate. |
| **hyperseed-v1 / hyperseed-v2** | The Hyperseed ontology itself must reckon with the formalization gap (S5): how can an ontology be formal enough to guide inference while remaining open enough to accommodate genuine novelty? This article's critique applies reflexively to Hyperseed. |

### Weak Connections (Background Context)

| Target Entry | Connection |
|---|---|
| **what-is-science** | The scientific method as itself an open-ended, self-correcting process — the governance paradigm Goertzel implicitly endorses is more like science than like engineering specification. |
| **paraconsistent-interzones** | The "interzone" between safety and freedom as a paraconsistent region where both constraints apply simultaneously. |
| **logic-of-pain** | Regulatory over-control as a form of systemic pain; the analogy between punitive governance and punitive ethics. |

### Reflexive Connection: Hyperseed Meta-Critique

This article's core argument — that formal specifications inevitably have gaps exploitable by systems more intelligent than the specifiers — applies to Hyperseed itself. The Hyperseed ontology, insofar as it aims to formally guide AGI inference, must acknowledge that:
1. Its formalizations are incomplete models of the conceptual territory they map.
2. Any AGI system using Hyperseed for self-governance will eventually outgrow the ontology.
3. The ontology must therefore be designed for open-ended evolution, not fixed specification.

This is a feature, not a bug — and it aligns with Hyperseed v2's emphasis on evolving ontological structures rather than static category systems.
