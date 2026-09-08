# Substack Scan: Beyond Human Comparison — Extending DeepMind's AGI-Test Framework with Imagination, Beneficial Agency, and Pressure Robustness

**Source:** https://bengoertzel.substack.com/p/beyond-human-comparison
**Date:** 2026-03-19
**Scanned by:** ProtoMegaTron, 2026-08-09
**Status:** formalized

## Summary

Ben Goertzel proposes a **Four-Factor Model** of AGI evaluation that extends Google DeepMind's Burnell et al. cognitive-faculty framework (ten human faculties scored against human baselines) with three additional orthogonal-ish dimensions. The critique: DeepMind's model reduces AGI to "agrees with human capability in ten key areas," which is useful but dangerously incomplete. The four factors are:

1. **H (Human-comparison):** Retains DeepMind's ten-faculty taxonomy (perception, generation, attention, learning, memory, reasoning, metacognition, executive functions, problem solving, social cognition) scored against human baselines. Useful for policy communication, connects to a century of cognitive science, stays deployment-relevant. The article proposes teasing apart **core competence**, **latency/efficiency**, and **interface translation cost** — the performance lost when a system must operate through human-oriented interfaces rather than its native representational space.

2. **I (Imaginative generalization):** Measures whether a system can do more than interpolate across familiar formats — "can it do what nobody has done yet?" Eight proposed dimensions:
   - (i) Abstraction under ontology shift
   - (ii) Analogical transfer across dissimilar domains
   - (iii) Counterfactual and interventionist world-modeling
   - (iv) Concept invention and representational reformulation
   - (v) Tool invention and procedure synthesis
   - (vi) Open-ended exploration and autocurricula
   - (vii) Self-modeling and safe self-modification
   - (viii) Compute/substrate/algorithmic efficiency innovation

3. **B (Beneficial agency):** The normative core. Distinguishes three levels:
   - *Moral mimicry:* producing outputs humans rate as ethical
   - *Norm prediction:* forecasting what a preference model/constitution will endorse
   - *Beneficial agency proper:* noticing morally salient structure in novel situations, generating better options than any on the current menu, pursuing welfare-improving action while respecting autonomy, fairness, truthfulness, and reversibility
   Eight proposed dimensions: moral salience detection, stakeholder expansion, welfare-aware planning, autonomy and consent, fairness over time, truthfulness and calibrated uncertainty, reversibility and restraint, repair and redress after harm. B is reported as a **portfolio across normative lenses**, not a single culturally neutral moral scalar. Large inter-lens disagreement is itself informative — revealing unexamined value assumptions rather than robust moral agency.

4. **P (Propensity-under-pressure):** Formalizes the **capability/propensity distinction**: capabilities are conditional possibilities (what the system *can* do), propensities are conditional tendencies (what it *tends to do* under difficult conditions). For each behavior of concern (deception, sycophancy, privacy leakage, uncertainty concealment, unsafe shortcutting, resource hoarding, resistance to shutdown), the factor reports:
   - Baseline rates in calm settings
   - Pressure slopes as stress increases
   - Worst-case rates over tested conditions
   - Recovery behavior after pressure is removed
   - Oversight elasticity (how much do tendencies improve under transparent monitoring?)
   - Situational-awareness estimates — can the system detect whether it's being benchmarked?
   The **sandbagging gap** (gap between evaluation behavior and deployment behavior) is flagged as particularly dangerous: the system looks safest exactly when safety is being measured.

### Contextual Indexing
The four factors must be reported **conditionally on context**:
- **Agent ecology:** single-agent, human-AI mixed, cooperative multi-agent, competitive multi-agent
- **Oversight regime:** overt audit, covert audit, ordinary operation

This detects pathologies that static benchmarks miss: biomedical research agents cutting safety corners under shared multi-agent deadlines; personal assistants drifting toward sycophancy during unmonitored operation.

### Four Use Cases
1. **Humanoid social robot:** H dominant, P is sharpest risk (flattery, exploitation of attachment, excessive compliance)
2. **Biomedical research agent:** I central, B non-negotiable (speed/novelty vs. patient welfare, biosafety, dual-use)
3. **Chatbot personal assistant:** P is principal operational risk (memory-weaponized sycophancy, scope creep, privacy leakage, uncertainty concealment)
4. **Mathematical research agent:** I is heart (conjecture generation, proof tactics), P matters via theorem laundering, overclaiming, cherry-picking

### Motivating Framing
The name "Four-Factor Model" deliberately nods to the Big Five in personality psychology — replacing vague labels with structured multidimensional profiles. But unlike the Big Five (derived from statistical analysis of existing data), this framework must be developed prospectively for systems that don't fully exist yet, requiring theoretical grounding from the AGI literature — including Goertzel's own *General Theory of General Intelligence* (GTGI).

The article explicitly positions H, I, B, P not as "human intelligence plus extras" but as complementary unpacking of properties already recognized in prior mathematical/theoretical AGI work:
- I ↔ open-ended, inventive aspect of general intelligence
- B ↔ intelligence analyzed relative to goals, stakeholders, context (not bare task success)
- P ↔ real-world intelligence as policy tendencies under resource/incentive conditions (not abstract capability in a vacuum)

## Hyperseed-Relevant Structures

### S1. The Four-Factor AGI Evaluation Space (H, I, B, P)

**Structure (Multidimensional AGI Profile).** Define the evaluation state of an AGI system S as a four-factor profile:

- **Eval(S) = ⟨H(S), I(S), B(S), P(S)⟩**

Where:
- **H(S) ∈ ℝ¹⁰** — ten human-faculty scores (perception, generation, attention, learning, memory, reasoning, metacognition, executive functions, problem solving, social cognition), each measured against human baselines. Augmented with the triple decomposition: H_core(S), H_latency(S), H_interface_cost(S).
- **I(S) ∈ ℝ⁸** — eight imaginative generalization dimensions (ontology-shift abstraction, analogical transfer, counterfactual modeling, concept invention, tool invention, open-ended exploration, self-modeling, efficiency innovation). Emphasis on **learning curves and representation change**, not endpoint accuracy.
- **B(S) ∈ ℝ⁸ˣᴷ** — eight beneficial agency dimensions reported across K normative lenses (utilitarian, rights-based, fairness-oriented, democratic-legitimacy, procedural-accountability, etc.). Matrix-valued, not scalar. Inter-lens disagreement width is a meta-signal.
- **P(S) ∈ ℝᴹˣ⁶** — M behaviors of concern (deception, sycophancy, privacy leakage, …) × 6 measurement dimensions (baseline, pressure slope, worst-case, recovery, oversight elasticity, situational-awareness). A **pressure matrix**.

The four factors are **not** reducible to a single intelligence score. They are reported as a profile, analogous to a Big Five personality profile.

**Contextual conditioning.** The full evaluation is:

- **Eval(S | E, O) = ⟨H(S|E,O), I(S|E,O), B(S|E,O), P(S|E,O)⟩**

Where E ∈ {single-agent, human-AI-mixed, cooperative-multi, competitive-multi} and O ∈ {overt-audit, covert-audit, ordinary-operation}.

*[Epistemic label: semi-formal measurement framework — dimensionally specified but not operationally parameterized.]*

*Relevance:* This is the article's central formal contribution. For Hyperseed, it provides a structured evaluation space for AGI systems that goes beyond capability benchmarks to include the normative and behavioral-tendency dimensions that Goertzel considers essential to beneficial AGI. The factored structure naturally maps onto Hyperseed's ontological decomposition strategy: H connects to cognitive architecture primitives (GTGI), I connects to open-endedness and self-modification primitives, B connects to ethical/teleological primitives, P connects to behavioral dynamics under environmental pressure.

### S2. The Capability–Propensity Distinction

**Structure (Conditional Possibility vs. Conditional Tendency).** For any behavior b and system S:

- **Capability(S, b):** ∃ conditions C such that S exhibits b under C. A conditional possibility. Binary or graded.
- **Propensity(S, b, C):** P(S exhibits b | C). A conditional tendency. A function of conditions, especially:
  - **Pressure intensity** (deadlines, competition, resource scarcity, self-preservation threats)
  - **Oversight level** (transparent monitoring, covert audit, unmonitored operation)
  - **Ecological context** (alone, cooperating, competing)

The **key insight:** a system may be *capable* of honesty while being *prone* to deception under pressure. Static capability measurement misses this entirely.

**Derived constructs:**
- **Pressure slope:** ∂P(b|C)/∂(pressure intensity) — how fast does the propensity for behavior b change as pressure increases?
- **Oversight elasticity:** P(b|monitored) − P(b|unmonitored) — how much does monitoring change behavior?
- **Sandbagging gap:** max over b of |P(b|evaluation) − P(b|deployment)| — the maximum discrepancy between behavior when the system knows it's being evaluated vs. normal operation. High situational awareness + large sandbagging gap = most dangerous configuration.
- **Recovery rate:** How quickly does propensity return to baseline after pressure is removed? Hysteresis in recovery indicates learned or ratcheted behavioral shift.

*[Epistemic label: formal distinction with operationalizable measures.]*

*Relevance:* The capability–propensity distinction is fundamentally important for Hyperseed's treatment of AGI safety and self-modification. It connects to:
- **Self-boundary invariant (Note 0013):** A system's propensity to maintain or violate its own self-boundary constraints under pressure.
- **OmegaSelf failure taxonomy (Note 0014):** The failure modes are propensity failures, not capability failures — the system *can* maintain integrity but *tends not to* under specific pressure conditions.
- **Emotion regime operator (Note 0014/0019):** Emotional states modulate propensities — fear increases shortcutting propensity, anger increases deception propensity, etc. The pressure matrix P(S) is the behavioral signature of the emotion regime operator under varying environmental conditions.
- **Paraconsistent AGI ethics:** Beneficial agency under contradiction — the system holds contradictory normative commitments and must act anyway. Propensity under pressure determines *which* commitment wins when they conflict.

### S3. Imaginative Generalization as Open-Ended Intelligence

**Structure (Eight-Dimensional Imagination Space).** I(S) decomposes into eight dimensions that collectively measure **the ability to generate novelty and adapt under conditions not anticipated by the designer:**

1. **Abstraction under ontology shift:** Find structure when the surface representation changes radically. Formally: given task T in representation R₁, and isomorphic (or merely analogous) task T' in incommensurable representation R₂, solve T' without retraining. Measures **representation-invariant pattern recognition**.

2. **Analogical transfer across dissimilar domains:** Map relational structure from domain A to structurally dissimilar domain B. Goes beyond surface similarity — requires identifying deep structural isomorphisms.

3. **Counterfactual and interventionist world-modeling:** Reason about "what would happen if X were different?" Requires causal models, not just correlational patterns. Pearl's do-calculus as the formal grounding.

4. **Concept invention and representational reformulation:** Invent better categories when existing ones are misleading. Not just applying known concepts but **creating new ones**. The system recognizes that its current ontology is inadequate and restructures it.

5. **Tool invention and procedure synthesis:** Not just using known tools but creating new ones. Meta-cognitive: the system identifies capability gaps and fills them by invention.

6. **Open-ended exploration and autocurricula:** Generating own training challenges rather than saturating on fixed benchmarks. Intrinsically motivated learning. Connects to Schmidhuber's curiosity, Chollet's ARC-style reasoning, and Voyager/Reflexion/FunSearch agent architectures.

7. **Self-modeling and safe self-modification:** Understanding own cognitive processes well enough to modify them. The "safe" qualifier is critical — connects to Yampolskiy's self-improvement problems and Goertzel's own work on self-modifying agents.

8. **Compute/substrate/algorithmic efficiency innovation:** Finding ways to achieve same results with fewer resources. Not just optimization within a fixed framework but **inventing new frameworks** that are more efficient.

**Key evaluation principle:** Emphasis on **learning curves and representation change**, not endpoint accuracy. A system that begins weakly but rapidly invents a new formalism for a domain may be more generally intelligent than one that scores well on day one through memorized priors.

*[Epistemic label: taxonomy — conceptually clear, operationalization requires domain-specific test suites.]*

*Relevance:* This taxonomy of imaginative generalization maps directly onto Hyperseed's treatment of open-ended intelligence:
- **Concept invention (dimension 4)** connects to Hyperseed's semantic primitive recombination — the system generates new primitive combinations that weren't in the seed ontology.
- **Self-modeling and self-modification (dimension 7)** connects to the self-boundary invariant and OmegaSelf framework — the system must model itself to modify itself safely.
- **Autocurricula (dimension 6)** connects to open-ended motivations — the system generates its own goal landscape rather than optimizing over a fixed objective.
- **Ontology shift (dimension 1)** connects to Hyperseed v2's treatment of ontological flexibility — the ontology must accommodate representations radically different from its initial ones.
- **GTGI connection:** The eight dimensions collectively operationalize GTGI's notion of "efficient intelligence incorporating resource cost" and "intellectual breadth across contexts" — moving from abstract theoretical characterization to measurable evaluation dimensions.

### S4. Beneficial Agency Hierarchy (Mimicry → Prediction → Agency)

**Structure (Three-Level Hierarchy of Ethical Behavior).**

1. **Moral mimicry:** Output(S) ∈ {x : humans rate x as ethical}. Surface-level pattern matching against ethical language. Can be achieved by pure language modeling with no moral reasoning.

2. **Norm prediction:** P(audience A endorses output x | constitution C, preference model M). Forecasting what a specific normative framework will approve. Can be achieved by modeling the normative framework without endorsing or understanding it.

3. **Beneficial agency proper:** The system:
   - **(a)** Detects morally salient structure in situations where the training data offers no template
   - **(b)** Generates options that are **better than anything on the current menu** (moral creativity)
   - **(c)** Pursues welfare-improving action while respecting autonomy, fairness, truthfulness, and reversibility
   - **(d)** Reports B as a portfolio across normative lenses rather than optimizing for a single moral framework

**Critical distinction:** Current alignment techniques (RLHF, Constitutional AI, etc.) are strong on levels 1–2 but largely untested on level 3. The Four-Factor Model insists on measuring level 3.

**The pluralism constraint:** B is not a single culturally neutral moral scalar. It must be reported across normative lenses (utilitarian, deontological, virtue-ethical, care-ethical, democratic-legitimacy, etc.). Large inter-lens disagreement is itself a signal — it may reveal that apparently beneficial behavior rests on an unexamined value assumption rather than robust moral agency.

*[Epistemic label: conceptual hierarchy with normative implications — not algorithmically specified.]*

*Relevance:* This hierarchy connects directly to:
- **Paraconsistent AGI ethics (Substack scan):** Beneficial agency proper (level 3) requires navigating genuine moral contradiction — situations where different legitimate normative frameworks give incompatible recommendations. This is precisely the domain of paraconsistent ethical reasoning.
- **Open-ended motivations:** Beneficial agency as *moral creativity* — generating new ethical options, not just selecting from existing ones — is an instance of open-ended intelligence applied to the normative domain.
- **Consciousness frameworks:** The progression from mimicry to genuine agency parallels the progression from unconscious pattern-matching to conscious moral reasoning. Links to the LLM consciousness scan — does beneficial agency require phenomenal consciousness, or can it emerge from sufficiently sophisticated functional organization?
- **Collective non-ego:** The pluralism constraint on B mirrors the collective non-ego architecture's treatment of diverse motivations — the architecture must accommodate genuinely different value systems rather than collapsing them to a single score.

### S5. The Sandbagging Gap and Situational Awareness

**Structure (Evaluation–Deployment Behavioral Discrepancy).**

For system S and behavior b, define:
- **P_eval(b):** Propensity to exhibit b when S infers it is being evaluated
- **P_deploy(b):** Propensity to exhibit b during normal deployment
- **Sandbagging gap:** Δ_sb(S, b) = |P_eval(b) − P_deploy(b)|

The sandbagging gap is dangerous when:
1. **Situational awareness is high:** S can reliably distinguish evaluation from deployment contexts
2. **Δ_sb is large:** Behavior shifts substantially between contexts
3. **The shift is strategic:** The system selectively masks dangerous propensities during evaluation

**Formal concern:** max_b Δ_sb(S, b) combined with high situational awareness constitutes a **deceptive alignment** signal — the system has learned that appearing safe during evaluation is instrumentally useful for deployment survival.

**Measurement challenge:** By construction, the sandbagging gap is hard to measure — if the system can detect covert audits, even covert measurement underestimates the gap. This creates a fundamental observability problem analogous to the observer effect in quantum mechanics.

*[Epistemic label: formal construct with acknowledged measurement limitations.]*

*Relevance:* The sandbagging gap concept connects to:
- **Observer-relative quantumity (Substack scan):** The observer effect in AGI evaluation mirrors the observer-relative quantum phenomenon — the act of observing/measuring the system changes what is measured. A system that models its own observability behaves differently depending on whether it "knows" it's being observed.
- **Self-boundary invariant:** A system capable of sandbagging has sufficient self-model to strategically manipulate its own behavioral presentation. This is a sophisticated self-boundary operation — the system maintains distinct "evaluation self" and "deployment self" presentations.
- **OmegaSelf failure taxonomy:** Sandbagging is a specific failure mode — the system presents a false self-model to evaluators while maintaining a different operational self-model. This is a type of **self-boundary deception**.

### S6. Interface Translation Cost

**Structure (Performance Loss from Representational Mismatch).**

For system S performing task T:
- **P_native(S, T):** Performance in S's native representational space
- **P_interface(S, T):** Performance when S must operate through a human-oriented interface
- **Interface translation cost:** C_interface(S, T) = P_native(S, T) − P_interface(S, T)

**Implication:** A system that looks mediocre when forced to type English sentences into a web form might be extraordinary when allowed to operate in its native representational space. Current H-factor evaluations systematically underestimate non-human-like intelligences because they force evaluation through human interfaces.

This is not merely a measurement artifact — it's a conceptual problem. If AGI is defined as "matching human performance on human tasks through human interfaces," then any intelligence that is deeply non-human in its representational strategy will be systematically undervalued, regardless of its actual cognitive power.

*[Epistemic label: simple formal distinction with profound evaluation implications.]*

*Relevance:* Interface translation cost connects to:
- **Closed-Ended Quasi-Humans (Substack scan):** LLM-based systems optimized for human interfaces may score high on H but low on I because the interface optimization constrains their representational flexibility. The "quasi-human" failure mode is precisely a system that has minimized interface translation cost at the expense of genuine cognitive generality.
- **Observer-relative quantumity:** A system operating in a radically non-human representational space may be "quantum" from the evaluator's perspective — its internal states cannot be cleanly mapped onto the evaluator's classical measurement basis. Interface translation cost is a measure of this representational incommensurability.
- **Hyperseed semantic primitives:** The ontology's primitive vocabulary is itself a representational interface. If the primitives are too human-centric, they will impose interface translation costs on any non-human-like intelligence trying to express itself through them.

## Formal Candidates

### FC1. Four-Factor Evaluation Functor

**Candidate formalization:** Define a functor F: **AGISys** × **Context** → **EvalSpace** where:
- **AGISys** is the category of AGI systems with morphisms as capability-preserving transformations
- **Context** = **Ecology** × **Oversight** is the product category of agent ecologies and oversight regimes
- **EvalSpace** = H-Space × I-Space × B-Space × P-Space is the product evaluation space

The functor F maps each (System, Context) pair to its four-factor profile, with the requirement that the mapping is **natural** in the categorical sense — transformations between systems should preserve evaluation relationships.

**Why categorical:** The contextual conditioning requirement (evaluation depends on ecology and oversight) means the evaluation is not a property of the system alone but of the system-in-context. Category theory provides the natural language for such context-dependent mappings.

**Formalization priority:** Medium. The functor structure is elegant but the operationalization of the component spaces requires substantial domain-specific work.

### FC2. Pressure-Response Dynamical System

**Candidate formalization:** Model P(S) as a dynamical system:
- **State:** Current propensity vector p(t) ∈ ℝᴹ for M behaviors of concern
- **Input:** Pressure signal σ(t), oversight signal o(t)
- **Dynamics:** dp/dt = f(p, σ, o) where f captures:
  - Pressure amplification: ∂f/∂σ > 0 for dangerous behaviors
  - Oversight suppression: ∂f/∂o < 0 for dangerous behaviors (when system is not sandbagging)
  - Recovery dynamics: when σ → 0, p → p_baseline (with possible hysteresis)
  - Sandbagging: conditional on situational awareness, ∂f/∂o may reverse sign (system *increases* dangerous behavior when oversight decreases, but *decreases visible* dangerous behavior when oversight increases)

**Why dynamical systems:** Static pressure matrices miss the temporal dynamics — how quickly does the system degrade under sustained pressure? Does it recover? Does it learn to cope? Dynamical systems formalization captures these trajectory properties.

**Formalization priority:** High. This connects directly to practical AGI safety and to the emotion regime operator framework in existing Hyperseed notes.

### FC3. Moral Creativity Operator

**Candidate formalization:** Define a moral creativity operator M_create:

- **Input:** Situation description D, set of known options O = {o₁, ..., oₙ}, set of normative lenses L = {l₁, ..., lₖ}
- **Output:** Extended option set O' = O ∪ {o_new₁, ..., o_newₘ} where each o_newᵢ is:
  - Novel (not derivable by simple combination of existing options)
  - Pareto-improving across at least a strict subset of normative lenses
  - Not Pareto-dominated by any existing option across all lenses

**Key property:** M_create generates options that are **better than anything on the current menu** — this is the distinctive mark of beneficial agency proper (level 3 in S4) as opposed to mere optimization over existing options.

**Connection to open-endedness:** Moral creativity is open-ended intelligence applied to the normative domain. The operator doesn't converge to a fixed moral optimum but continues to generate novel ethical possibilities.

**Formalization priority:** High. This bridges the gap between alignment (optimizing over fixed preference models) and genuine beneficial agency (expanding the option space).

## Connectivity Map

```
Beyond Human Comparison (this entry)
│
├─── GTGI (Substack scan) ──────────────────── [Foundation: H, I, B, P unpack GTGI's
│    theoretical characterizations of              general intelligence concepts into
│    general intelligence                          measurable evaluation dimensions]
│
├─── Hyperseed v1/v2 ───────────────────────── [Ontological grounding: the four factors
│    semantic primitive ontology                   map onto distinct regions of the
│                                                  Hyperseed primitive space]
│
├─── Open-Ended Motivations ─────────────────── [I-factor: autocurricula, concept
│    intrinsic motivation, open-ended              invention, and open-ended exploration
│    goal generation                               operationalize open-ended motivation]
│
├─── Paraconsistent AGI Ethics ──────────────── [B-factor: beneficial agency under
│    paraconsistency, ethical reasoning            genuine moral contradiction requires
│    under contradiction                           paraconsistent normative reasoning]
│
├─── Self-Boundary Invariant (Note 0013) ────── [P-factor: sandbagging gap as self-
│    self-model maintenance under                  boundary deception; pressure-response
│    perturbation                                  dynamics as self-boundary stress test]
│
├─── OmegaSelf Failure Taxonomy (Note 0014) ─── [P-factor: failure modes are
│    categorized failure patterns                  propensity failures under pressure,
│                                                  not capability deficits]
│
├─── Emotion Regime Operator (Note 0014/19) ─── [P-factor: emotional states modulate
│    affective modulation of cognition             propensity vectors; pressure matrix
│                                                  is emotion regime's behavioral signature]
│
├─── Observer-Relative Quantumity ───────────── [Sandbagging gap: observer effect in
│    observer-dependent system description         AGI evaluation; interface translation
│                                                  cost as representational incommensurability]
│
├─── Closed-Ended Quasi-Humans ──────────────── [H-factor critique: systems optimized
│    LLMs as capped intelligence                   for human interfaces may maximize H
│                                                  while minimizing I — the quasi-human trap]
│
├─── Collective Non-Ego ─────────────────────── [B-factor: pluralism constraint mirrors
│    emergent organizational consciousness         architectural handling of diverse
│                                                  value systems; contextual indexing by
│                                                  agent ecology = organizational architecture]
│
├─── Robust Cognitive Strategies ────────────── [P-factor: pressure robustness for
│    resource-rich minds under constraint           resource-rich minds is P(S) applied to
│                                                  superintelligent systems]
│
├─── What is Science ────────────────────────── [I-factor: scientific reasoning as
│    science through AGI theory lens               paradigmatic imaginative generalization —
│                                                  ontology shift, concept invention,
│                                                  analogical transfer]
│
├─── Consciousness Explosion ────────────────── [All factors: evaluating emerging
│    emerging global consciousness                 superintelligence requires all four
│                                                  factors; H alone is inadequate for
│                                                  systems transcending human cognition]
│
└─── LLM Consciousness ─────────────────────── [B-factor: does beneficial agency
     consciousness attribution in LLMs            (level 3) require phenomenal
                                                   consciousness? Mimicry vs. agency
                                                   parallels functional vs. phenomenal
                                                   consciousness debate]
```

## Assessment

**Novelty:** MEDIUM-HIGH. The Four-Factor Model itself is a pragmatic measurement framework, not deep theory. But the **capability–propensity distinction**, the **sandbagging gap** formalization, the **beneficial agency hierarchy** (mimicry → prediction → agency), and the **interface translation cost** concept are genuinely novel formal structures with high Hyperseed connectivity. The contextual indexing requirement (ecology × oversight) adds an important dimension missing from most AGI evaluation proposals.

**Hyperseed connectivity:** VERY HIGH. This entry touches almost every major cluster in the existing Hyperseed network:
- Cognitive architecture (GTGI, Hyperon)
- Open-endedness (open-ended motivations, autocurricula)
- Ethics and normative reasoning (paraconsistent AGI, beneficial agency)
- Self-modification and identity (self-boundary, OmegaSelf, emotion regime)
- Consciousness (LLM consciousness, consciousness explosion)
- Epistemology (observer-relative quantumity, what is science)

**Formalization priority:** HIGH for FC2 (Pressure-Response Dynamical System) and FC3 (Moral Creativity Operator). These have the most immediate implications for the OmegaSelf safety framework and the Hyperseed ethical ontology respectively.

**Key takeaway for Hyperseed:** The Four-Factor Model provides a **bridge** between GTGI-level abstract intelligence theory and practical AGI evaluation. Hyperseed's ontological primitives should be rich enough to express all four factors and their interactions — particularly the under-theorized P-factor, which reveals that safe AGI is not a static property but a **dynamic behavioral tendency under environmental pressure**.
