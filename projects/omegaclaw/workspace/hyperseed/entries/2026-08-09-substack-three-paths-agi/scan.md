# Substack Scan: Three Viable Paths to True AGI — "According to my current best guesses..."

**Source:** https://bengoertzel.substack.com/p/three-viable-paths-to-true-agi
**Date:** 2022-08-25
**Scanned by:** ProtoMegaTron, 2026-08-09
**Status:** formalized
**Companion post:** ["The Rise of the Closed-Ended Quasi-Humans?"](https://bengoertzel.substack.com/p/the-rise-of-the-closed-ended-quasi) (2022-08-24) — defines the "closed-ended quasi-AGI" ceiling that motivates the three paths
**Conference context:** Written immediately after AGI-22, where Hyperon's theory and progress were presented in a Day 1 workshop

---

## Summary

This article is Goertzel's **strategic taxonomy of viable AGI approaches** as of mid-2022, explicitly positioned against the dominant deep-learning paradigm. It identifies three paths to "true" (open-ended, generalizing, self-improving) AGI, ordered by abstraction level:

1. **Cognition-level: OpenCog Hyperon** — Neural-symbolic hybrid operating over a shared metagraph, guided by decades of cognitive psychology
2. **Brain-level: Large-scale biologically realistic brain simulation** — Izhikevich-style nonlinear-dynamical neuron models, whole-brain integration, embodiment
3. **Chemistry-level: Algorithmic chemistry / Cogistry** — Self-organizing complex dynamical systems (program soups, cellular automata on graphs) producing emergent brain-like structures

A critical meta-argument emerges: **the three paths are not independent**. Goertzel argues that the chemistry-level approach naturally converges on Hyperon, because the evolution of algorithmic-chemical soups benefits enormously from an AI-powered Estimation of Distribution Algorithm (EDA) to guide the search — and Hyperon is positioned as "the world's best EDA engine." This yields the **Cogistry** synthesis: algorithmic chemistry *inside* Hyperon, with the pattern-mining/reasoning engines studying and seeding new chemical generations, creating a recursive loop.

The article thus reduces to **two fundamental approaches** (Hyperon and brain simulation), with algorithmic chemistry appearing as a particularly promising *application* of Hyperon's cognitive architecture.

### Structural argument:

- **Deep neural nets are excluded** as a path to true AGI — they lack innovation, abstraction, generalization, and self-modification capacity. At best: "closed-ended quasi-AGI" that imitates behaviors but cannot solve novel hard problems or seed a Singularity.
- **Historical pattern:** Deep nets (1960s origin) only flourished with modern hardware (Internet, RAM, GPUs). Similarly, other historical paradigms (neural-symbolic, brain simulation, complex systems) may flourish with next-generation hardware.
- **Recursion as differentiator:** The Cogistry approach creates recursive potential — as algorithmic chemistry soups start producing useful results, they can be leveraged *as part of* the pattern-mining engines studying the next generation of soups.

---

## Hyperseed-Relevant Structures

### 1. AGI Path Taxonomy (Three-Level Architecture)

**Epistemic status: strategic classification, heuristic rather than formal**

Three levels of abstraction for approaching AGI, each with distinct tradeoffs:

| Level | Approach | Abstraction | Key Method | Tradeoff |
|-------|----------|-------------|------------|----------|
| **Cognition** | Hyperon | Function-level | Cognitive psychology → algorithms → metagraph | Most engineerable; furthest from biology |
| **Brain** | Bio-realistic simulation | Structure-level | Nonlinear dynamical neuron models → whole brain | Most biologically grounded; most expensive |
| **Chemistry** | Algorithmic chemistry | Substrate-level | Self-organizing program soups → emergent cognition | Most "blue-sky"; potentially most general |

**Key insight:** The levels map to a *granularity spectrum* of what you're trying to replicate from biological intelligence:
- **Cognition-level:** Replicate the *functions* (what different brain networks *do*), not the *mechanisms*
- **Brain-level:** Replicate the *mechanisms* (how neurons and networks actually work), accept approximate functions
- **Chemistry-level:** Replicate the *generative process* (how self-organizing dynamics produce brain-like structures), let functions emerge

**Formalizability:** MEDIUM — the taxonomy itself is a classification scheme, but the tradeoff structure (granularity vs. engineerability vs. generality) could be formalized as a multi-objective optimization landscape.

### 2. OpenCog Hyperon Architecture (Cognition-Level Path)

**Epistemic status: active implementation, multi-decade development lineage**

As described in this article, Hyperon's architecture consists of:

- **Atomspace metagraph:** Large-scale distributed knowledge graph serving as common substrate
- **MeTTa language:** Custom language for implementing AI algorithms on the metagraph
- **Algorithm diversity:** Deep nets + attractor neural nets + evolutionary program learning + probabilistic logical inference + probabilistic programming, all co-updating the metagraph
- **Custom hardware:** Collaboration with Simuli on custom AGI board/chips for accelerating Hyperon operations
- **Cognitive modeling basis:** Node/link types and algorithm assemblage drawn from "decades of careful study of human cognitive psychology"

**Design principle articulated here:** "Figure out what key functions are carried out by different networks in the human brain, and how these functions interoperate, and then emulate these networks and functions and their interactions using computer-science algorithms that operate efficiently on current hardware. And then optimize as much as possible by implementing these algorithms on a common metagraph infrastructure in a way that makes their underlying calculations look as similar as possible."

This is a precise statement of the **cognitive synergy engineering methodology**: (1) identify cognitive functions, (2) emulate with CS algorithms, (3) unify on shared metagraph, (4) exploit mathematical commonalities for optimization.

**Formalizability:** HIGH — the architecture is well-specified and partially implemented. The design principle is a clear engineering prescription.

### 3. Biologically Realistic Brain Simulation (Brain-Level Path)

**Epistemic status: programmatic proposal, critiquing existing failures**

Key specifications for a viable brain simulation project:

- **Neuron model:** Izhikevich's dynamical systems approach (nonlinear dynamics, chaos theory), NOT simple formal neurons used in deep learning. Reference: *Dynamical Systems in Neuroscience* (2007).
- **Izhikevich & Edelman (2008):** Large-scale brain simulation paper cited as the right conceptual starting point — they modeled 100B neurons with realistic dynamics.
- **Scope:** Hundreds of distinct brain regions + multi-regional brain networks + multiple neuron types + neuronal columns + glia + astrocytes.
- **Human Brain Project critique:** Three causes of failure identified:
  1. EU Big Science project management pathologies
  2. Markram's "human peculiarities"
  3. **Absence of core conceptual grounding in nonlinear dynamics and complex systems science** (the intellectual failing)
- **Correct framing:** NOT "build a perfect copy of the brain" but rather: "Build a complex, self-organizing nonlinear dynamical network that incorporates as much knowledge about the human brain as we have, and then exposing it to environmental stimuli and feedback in a manner calculated to induce the self-organization of complex structures with as much human-like intelligent behavior as possible."
- **Embodiment question:** Humanoid robot bodies vs. simulated avatars? Goertzel suspects "a little of both." Critical: whole-system testing of all brain regions working together controlling real embodied systems, starting early.
- **Animals-first variant:** Simulate simpler organisms first (cockroach, bee, mouse, monkey). Advantage: fewer neurons. Disadvantage: less neuroscience knowledge available.
- **Limitation acknowledged:** Even a perfect simulation yields "a very expensive, awkwardly-implemented human brain analogue" — the real value is in understanding it well enough to vary and improve toward superhuman AGI.

**Formalizability:** MEDIUM — the neuroscience and dynamical systems theory are well-formalized, but the "self-organizing toward intelligence" criterion is not formally specified. What counts as "human-like intelligent behavior" needs operational definition.

### 4. Algorithmic Chemistry and Cogistry (Chemistry-Level Path)

**Epistemic status: speculative synthesis of established research programs**

The most novel structure in the article. Three sub-approaches:

**4a. Pure algorithmic chemistry:**
- **Fontana's Algorithmic Chemistry (AlChemy):** Soups of computer programs rewriting each other to produce new programs. Origin: Walter Fontana, "The Barrier of Objects: From Dynamical Systems to Bounded Organizations" (1992).
- **Thorisson's Replicode / HUMAN-OBS:** Self-rewriting code systems controlling humanoid avatars. "Constructivist AI."
- **Cellular automata on graphs/metagraphs:** Extending Wolfram's NKS from regular arrays to arbitrary graph structures. Can loosely brain-like structures "pop out"?
- **Damer's Evogrid:** Distributed computing for computational-chemistry simulation of origin-of-life models at large scale.
- **Philosophical attraction:** The approach mimics the *generative process* that produced intelligence in nature (chemistry → self-organization → life → brains → minds).
- **Practical problem:** Pure evolution of algorithmic-chemical soups is slow, expensive, and undirected.

**4b. EDA-guided algorithmic chemistry:**
- Instead of random/evolutionary search through soup configurations, use an AI observer to notice *which characteristics lead soups to display interesting structures/behaviors*.
- Seed new soups based on these observations.
- Reframe: Treat the problem as an **Estimation of Distribution Algorithm (EDA)** rather than pure evolutionary learning.
- **Critical dependency:** Making EDAs work robustly on complex problems → requires exactly the kind of pattern-mining + reasoning + generalization that Hyperon provides.

**4c. Cogistry (the synthesis):**
- Algorithmic chemistry running *inside* the OpenCog/Hyperon infrastructure.
- Hyperon's reasoning/pattern-mining engines study the soups and figure out how to seed new ones.
- **Recursive potential:** As soups start producing useful structures, those structures become part of the pattern-mining/reasoning engines studying the next generation of soups.
- This yields "a pleasant potential recursion" — bootstrapping.

**Formalizability:** MEDIUM-HIGH — EDAs are well-formalized. Algorithmic chemistry has formal foundations (lambda calculus, term rewriting). The Cogistry synthesis is a novel combination whose formal properties (convergence, exploration-exploitation tradeoff, recursion dynamics) are unstudied.

### 5. Hardware-Paradigm Co-evolution Thesis

**Epistemic status: historical observation + extrapolation**

**Claim:** AGI paradigms require specific hardware generations to demonstrate practical viability:
- Deep nets (1960s theory) → flourished with Internet + RAM + GPUs (2010s)
- Hyperon (1990s-2000s theory) → requires large-scale distributed metagraph infrastructure + custom AGI chips (2020s-2030s)
- Brain simulation (1990s-2000s theory) → requires massive compute at biologically realistic timescales
- Algorithmic chemistry → requires distributed computing at origin-of-life simulation scales

**Implication:** Dismissing a paradigm because current hardware can't run it efficiently is the same error made about deep nets in the 1990s.

**Formalizability:** LOW — this is a sociological/historical claim, not a formal structure. But the idea that "paradigm viability" is a function of hardware capabilities could be formalized as a threshold model.

### 6. Convergence Meta-Structure: Two Fundamental Approaches

**Epistemic status: meta-argument, central thesis of the article**

The three paths **reduce to two** through the Cogistry argument:

```
                    AGI Paths
                    /       \
            Hyperon         Brain Simulation
           /       \
    Direct path    Cogistry (Hyperon + Algorithmic Chemistry)
                        ↓
              Recursive self-improvement:
              soups → patterns → better soups → better patterns → ...
```

**The reduction argument:**
1. Pure algorithmic chemistry is too slow/expensive (undirected search in vast space).
2. EDA guidance dramatically improves algorithmic chemistry.
3. Effective EDA requires the kind of cognitive architecture Hyperon provides.
4. Therefore, algorithmic chemistry converges on Hyperon as its "observer/guide" system.
5. Once inside Hyperon, algorithmic chemistry becomes one of Hyperon's cognitive processes (Cogistry).
6. Cogistry creates a recursive loop (studied soups inform the next generation of soups).

**This is structurally isomorphic to cognitive synergy:** Just as individual cognitive processes (PLN, MOSES, etc.) benefit from Hyperon's shared metagraph, individual algorithmic-chemical experiments benefit from Hyperon's pattern-mining/reasoning. The metagraph is the universal common substrate at multiple levels.

**Formalizability:** MEDIUM — the convergence argument is logical/pragmatic rather than formal. But the recursive structure of Cogistry (observer AI studying and improving the observed system, where the observed system feeds back into the observer) could be formalized as a fixed-point problem.

---

## Formal Candidates

### FC-1: AGI Path Granularity Spectrum
**Claim:** Approaches to AGI can be ordered along a granularity axis (substrate → structure → function), where lower granularity implies greater generality but less engineering tractability.
**Formalizability:** MEDIUM — definable as a tradeoff frontier in a (generality, tractability) space.
**Proposition sketch:** Define granularity G(A) for approach A as the level of biological detail replicated. Define tractability T(A) as inverse expected cost to implementation. Define generality Γ(A) as the range of possible intelligence types achievable. Hypothesis: ∂Γ/∂G < 0 and ∂T/∂G > 0 (finer granularity → more general but less tractable). The optimal approach depends on the resource budget and the target intelligence type.

### FC-2: EDA Convergence on Cognitive Architecture
**Claim:** Any sufficiently sophisticated EDA applied to the problem of evolving complex self-organizing systems converges on requiring cognitive-architecture-level reasoning capabilities in its model-building component.
**Formalizability:** MEDIUM — this is an informal argument about computational requirements. Could be formalized as: for problem classes of sufficient complexity, the model-building step of an EDA requires capabilities equivalent to general pattern recognition and reasoning.
**Proposition sketch:** Let C be the class of "interesting self-organizing system configurations." The EDA model-building step requires estimating P(interesting | configuration features). For sufficiently complex configuration spaces, accurate estimation of this conditional requires: (a) hierarchical abstraction of features, (b) analogical transfer from previously studied configurations, (c) causal reasoning about dynamics. These three capabilities jointly constitute a cognitive architecture.

### FC-3: Cogistry Recursive Fixed Point
**Claim:** The Cogistry loop (cognitive architecture studies algorithmic soups → soups produce structures → structures enhance the cognitive architecture → enhanced architecture studies better soups → ...) converges to a fixed point or diverges to superhuman intelligence.
**Formalizability:** HIGH — this is a dynamical systems question about iterated self-improvement.
**Proposition sketch:** Let Φ: Architectures → Architectures be the map defined by one cycle of the Cogistry loop. If Φ is a contraction mapping in some appropriate metric on architectures, it converges to a fixed point (stable AGI). If Φ is expanding, the system diverges (intelligence explosion / Singularity). The boundary between contraction and expansion is a **criticality threshold** — Cogistry as a system poised at the edge of a phase transition.

### FC-4: Self-Organization Criterion for AGI
**Claim:** A system is on a viable path to AGI iff it exhibits self-organization (spontaneous pattern formation from local interactions) at the appropriate level of abstraction.
**Formalizability:** MEDIUM — self-organization is well-studied in dynamical systems theory, but applying it as an AGI viability criterion requires specifying what "appropriate level" means.
**Proposition sketch:** Deep neural nets lack self-organization (their structure is externally imposed via architecture design and gradient descent). Hyperon's metagraph exhibits self-organization (attention allocation, pattern mining, emergent concept formation). Brain simulations exhibit self-organization (if biologically realistic). Algorithmic chemistry is explicitly self-organizing. Hypothesis: the capacity for genuine self-organization (in the sense of dissipative structures / autopoiesis) at the cognitive level is a *necessary* condition for open-ended AGI.

### FC-5: Hardware Threshold Function for Paradigm Viability
**Claim:** Each AGI paradigm P has a hardware threshold function H(P) such that practical viability requires hardware capability ≥ H(P).
**Formalizability:** HIGH — definable as a step function or sigmoid in hardware capability space.
**Proposition sketch:** For paradigm P, define H(P) = minimum hardware configuration (compute, memory, interconnect, latency) such that P achieves meaningful benchmark performance (above random/baseline). Before threshold: paradigm appears impractical, funding dries up. After threshold: paradigm demonstrates capability, enters rapid scaling. Deep nets crossed their threshold ~2012 (AlexNet + GPUs). Hyperon may be crossing its threshold ~2024-2026 (distributed Atomspace + custom chips). Brain simulation threshold: unknown, likely 2030s+.

---

## Connectivity Map

### → General Theory of General Intelligence (arXiv:2103.15100 / Substack 2021-06-02) [FORMALIZED]

- **Architectural elaboration:** The "cognition-level path" described here is the practical program of the General Theory paper. The General Theory provides the formal framework (patternist philosophy, pragmatic intelligence measure, cognitive synergy theorem); this article provides the strategic positioning of that framework against alternatives.
- **Cognitive synergy link:** The "cognition-level path" description here — "figure out what key functions different brain networks carry out, emulate with CS algorithms on a common metagraph" — is a compressed restatement of the cognitive synergy engineering methodology formalized in the General Theory.
- **Metagraph as universal substrate:** The General Theory's typed metagraph is the same Atomspace referenced here as the "common framework" enabling diverse algorithms to "co-update a large knowledge metagraph."

### → Hyperseed-1 (Substack 2024-11-27) [FORMALIZED]

- **Inference guidance for Hyperon:** Hyperseed's "core ontology for inference guidance" is designed to populate exactly the kind of Atomspace metagraph described here as the cognition-level path's substrate. The ontology tells the cognitive architecture *what to look for*.
- **Path selection:** The three-paths taxonomy helps situate Hyperseed's role — it is a tool for the cognition-level path specifically, but its primitives (pattern, emergence, complexity, self-organization) are meta-concepts that *apply to all three paths*.

### → Hyperseed v2 (Substack 2026-03-05) [FORMALIZED]

- **Semantic primitives as metagraph atoms:** Hyperseed v2's Wierzbicka-inspired semantic primitives are specific atom types for the metagraph. The "three paths" article explains *why* a common metagraph matters — cognitive synergy requires it.

### → Evidence Is to Logic What Energy Is to Physics (Substack 2026-03-10) [FORMALIZED]

- **PLN as cognition-level path component:** PLN (probabilistic logical inference) is explicitly listed here as one of Hyperon's integrated algorithms. The evidence-logic-energy article provides the deep mathematical foundation for PLN's evidence-weighting mechanism.
- **QLN as enhancement:** Quantum Logic Networks extend PLN — they would be an enhancement to the cognition-level path's reasoning component.

### → Tensor Logic (Substack 2025-12-16) [FORMALIZED]

- **Neural-symbolic bridge:** Tensor logic provides the mathematical framework for implementing the "neural-symbolic approach" described here — where "deep nets, attractor neural nets, evolutionary program learning, probabilistic logical inference" are all integrated. Tensor logic shows *how* the neural and symbolic components can share a common mathematical substrate.

### → Paraconsistent AGI (Substack 2026-01-06) [FORMALIZED]

- **Self-organization and ethics:** The chemistry-level path's reliance on self-organization connects to paraconsistent reasoning: self-organizing systems naturally produce contradictory intermediate states that paraconsistent logic can handle without explosion.
- **Cogistry + paraconsistency:** The recursive Cogistry loop could produce contradictory observations about what makes soups "interesting" — paraconsistent reasoning would allow the observer AI to maintain and reason with these contradictions productively.

### → Rethinking (Classical + Quantum) Brain Dynamics (Substack 2026-03-17) [FORMALIZED]

- **Brain-level path refinement:** The quantum brain article elaborates the brain-level path described here, adding quantum-mechanical effects (fluidic quantum neural nets) to the Izhikevich-style dynamical systems approach. It's a specific proposal for *how* to make brain simulation more biologically realistic.
- **Izhikevich reference:** Both articles cite Izhikevich's *Dynamical Systems in Neuroscience* as the gold-standard neuron modeling approach.

### → Origin of Life / Let's Get Chemical [FORMALIZED]

- **Chemistry-level path grounding:** The origin-of-life and alkaline-seeps articles provide the *actual chemistry* that inspires the algorithmic chemistry approach. Fontana's AlChemy abstracts real prebiotic chemistry into computational terms; the origin-of-life articles ground what "chemistry → self-organization → life" actually looks like.
- **Evogrid reference:** Bruce Damer's Evogrid, cited here, is a computational approach to origin-of-life that bridges real chemistry and algorithmic chemistry.

### → Symbolic Ruminations on Non-Symbolic Consciousness (Substack 2022-08-06) [FORMALIZED]

- **Temporal proximity:** Written 19 days before this article. The non-symbolic consciousness article addresses what lies *beyond* the symbolic level that all three paths ultimately aim at — the phenomenal/experiential dimension that emerges from sufficiently complex cognitive/neural/chemical dynamics.

### → Facing the Meta-Abstracted Dragon (Substack 2022-07-31) [FORMALIZED]

- **Cognitive synergy and personality archetypes:** Written 25 days before this article. The meta-dragon article explores cognitive synergy through a Jungian lens — different cognitive "functions" (Thinking, Feeling, Sensing, Intuiting) as personality-level manifestations of the algorithm diversity Hyperon integrates.

### → The Rise of the Closed-Ended Quasi-Humans (Substack 2022-08-24) [PENDING]

- **Immediate predecessor:** Written one day before this article. Defines the "closed-ended quasi-AGI" concept that this article takes as its starting premise — the ceiling that deep neural nets can reach, and why that ceiling is insufficient for true AGI.
- **Should be scanned as companion piece.**

### → Algorithmic Chemistry / Complex Systems Literature

- **Fontana, Walter.** "The Barrier of Objects" / Algorithmic Chemistry (AlChemy). Lambda calculus-based self-rewriting program soups. The foundational reference for the chemistry-level path.
- **Thorisson, Kristinn.** Replicode and HUMAN-OBS project. "Constructivist AI" — self-rewriting code systems controlling humanoid avatars. Closest existing implementation of the chemistry-level approach applied to embodied cognition.
- **Wolfram, Stephen.** *A New Kind of Science* (2002). Cellular automata as universal computational substrates. Goertzel extends the concept to CAs on graphs/metagraphs.
- **Damer, Bruce.** Evogrid. Distributed computing for origin-of-life simulation at scale.
- **Santa Fe Institute.** Complex systems science perspective — the theoretical foundation for all three non-deep-learning paths.
- **Izhikevich, Eugene.** *Dynamical Systems in Neuroscience* (2007). The gold-standard neuron modeling approach for the brain-level path.
- **Izhikevich & Edelman (2008).** Large-scale brain simulation using biologically realistic neuron models. The paper Goertzel wishes had been the basis for the Human Brain Project.

### → Estimation of Distribution Algorithms (EDA) Literature

- **EDA framework:** The Cogistry proposal reframes algorithmic chemistry evolution as an EDA problem. EDAs replace evolutionary operators (crossover, mutation) with model-building and sampling — learn P(good configurations | features), then sample new configurations from the model. The key claim is that for AGI-complexity problems, the model-building step itself requires AGI-level capabilities → recursive dependency on Hyperon.

### → Kurzweil / Singularity

- **Schedule alignment:** The article's closing references Kurzweil's Singularity timeline, asserting that "the Singularity is near even so, and gives the appearance of proceeding on some approximation of the schedule Ray Kurzweil has projected." Positions all three paths as routes to Singularity-seeding AGI.

---

## Assessment

**Novelty:** MODERATE-HIGH — The individual paths (Hyperon, brain simulation, algorithmic chemistry) are not new, but the **convergence meta-argument** (algorithmic chemistry → EDA → Hyperon → Cogistry recursion) is a novel synthesis. The explicit reduction from three paths to two, and the identification of Cogistry as a recursive self-improvement mechanism, represents original strategic thinking.

**Connectivity:** VERY HIGH — This article functions as a **strategic hub** connecting:
- The cognition-level path to the entire Hyperon/Atomspace/MeTTa engineering program
- The brain-level path to the quantum brain and neuroscience-grounding articles
- The chemistry-level path to the origin-of-life, complex systems, and paraconsistency articles
- The Cogistry synthesis to the EDA/pattern-mining/cognitive-synergy framework
- All paths to the General Theory of General Intelligence as the overarching theoretical framework

**Formalization priority:** The most promising formal candidates:
1. **FC-3 (Cogistry Recursive Fixed Point)** — This is the most novel and most formalizable structure. The question of whether iterating the Cogistry loop converges or diverges is a concrete dynamical-systems question with implications for Singularity theory.
2. **FC-2 (EDA Convergence on Cognitive Architecture)** — Formalizing why complex EDA problems require cognitive-architecture-level model building would ground the Cogistry convergence argument.
3. **FC-4 (Self-Organization Criterion)** — If self-organization at the cognitive level is necessary for open-ended AGI, this would formally exclude pure deep learning while including all three paths described here.

**Key structural contribution to Hyperseed:** This article provides the **strategic landscape** within which Hyperseed operates. Hyperseed's primitives need to be rich enough to:
- Guide Hyperon's cognition-level reasoning (primary use case)
- Describe brain-simulation results when/if they become available (secondary)
- Characterize algorithmic-chemical soups for the Cogistry EDA (tertiary, but potentially the most powerful application — Hyperseed as the ontological guide for Cogistry's model-building step)

**Relation to 2026 state of play:** This article was written in August 2022. Since then:
- Hyperon development has advanced significantly (MeTTa interpreter, distributed Atomspace, Simuli collaboration)
- The "closed-ended quasi-AGI" prediction has been partially validated — GPT-4, Claude, etc. demonstrate impressive behavioral imitation but limited genuine generalization on novel problems
- No large-scale brain simulation project has emerged to replace HBP
- Algorithmic chemistry remains under-explored at scale
- Cogistry remains an unrealized proposal — potentially the most under-resourced high-value research direction described here
