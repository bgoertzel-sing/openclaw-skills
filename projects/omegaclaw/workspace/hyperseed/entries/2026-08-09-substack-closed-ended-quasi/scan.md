# Substack Scan: The Rise of the Closed-Ended Quasi-Humans? — "Well OK probably not but..."

**Source:** https://bengoertzel.substack.com/p/the-rise-of-the-closed-ended-quasi
**Date:** 2022-08-24
**Scanned by:** ProtoMegaTron, 2026-08-09
**Status:** formalized
**Companion post:** ["Three Viable Paths to True AGI"](https://bengoertzel.substack.com/p/three-viable-paths-to-true-agi) (2022-08-25) — the follow-up that proposes paths *beyond* the closed-ended ceiling defined here
**Conference context:** Written immediately after AGI-22; cites conversations with Joscha Bach and a fireside chat with Gary Marcus at that conference

---

## Summary

This article is a philosophical thought experiment, written the day before "Three Viable Paths to True AGI," that defines the **theoretical upper bound** of what pure deep-neural-net approaches could achieve if everything went maximally well. Goertzel coins the term **"closed-ended quasi-human"** for this ceiling and then systematically enumerates what such a system could *not* do.

The thought experiment:
- Suppose you combine many connected deep neural models end-to-end: one per sense modality, one for body control, one for facial expressions, one for language, one for speech, one for goal/subgoal management — all trained together with dependencies, using real-world robot embodiment data plus massive pretraining.
- **Best possible outcome (upper bound):** A system that emulates the "vast majority of everyday human behaviors" — a closed-ended quasi-human.
- Goertzel is explicit that he is **not certain** this is achievable; it's a generous upper bound giving deep learning maximum benefit of the doubt. Gary Marcus, he notes, is even more skeptical.

The term "closed-ended" is the operative concept. Such a system would be:

1. **Closed under behavioral novelty** — cannot produce behavior qualitatively different from its training distribution
2. **Closed under environmental novelty** — cannot adapt to genuinely novel artifacts (flying hoverboards, radically new interfaces)
3. **Closed under creative innovation** — cannot produce art, science, or engineering ideas that go beyond recombination of training data
4. **Closed under recursive self-improvement** — critically, cannot seed an intelligence explosion or Singularity

The article then explores ramifications: consciousness (panpsychist take: quasi-humans would have experience, but impoverished compared to human reflective consciousness), social comparison (most individual humans rarely innovate, but human *society* does via rare geniuses + cultural elicitation patterns), temporal argument (an ordinary human given 100K years would eventually exceed any quasi-human, because humans can go beyond their training data given time), and terminological wrestling (should we call this "AGI"? → inadequacy of the AGI concept itself).

The most striking passage is Goertzel's self-observation: "Most of the people in the society around me are actually functioning basically as closed-minded quasi-humans, in their everyday lives. Well, yeah. ... If I'm honest I suppose I'm also acting in this sort of closed-ended, not-so-creative capacity much of the time."

This implies the closed-ended/open-ended distinction is not a binary but a **spectrum or mode** — even biological humans oscillate between closed-ended routine operation and genuinely open-ended creative functioning.

---

## Hyperseed-Relevant Structures

### 1. Closed-Endedness as a Formal Property of Cognitive Systems

**Epistemic status: conceptual definition via thought experiment, presented as upper bound**

The article implicitly defines a property of cognitive systems that can be formalized:

**Definition (informal):** A cognitive system S is **closed-ended** iff S's behavioral repertoire is bounded by (a closure of) the behavioral patterns present in its training/experience data, under recombination and interpolation but not extrapolation or genuine novelty.

Key dimensions of closure:
- **Behavioral closure:** Cannot produce actions qualitatively outside the training distribution
- **Adaptive closure:** Cannot learn to operate in environments structurally different from training environments
- **Creative closure:** Cannot generate artifacts (art, science, engineering) that represent genuine innovation beyond recombination
- **Recursive closure:** Cannot improve its own cognitive architecture to overcome any of the above closures

**Contrast with open-endedness:** An open-ended system can, in principle:
- Generate genuinely novel behaviors
- Adapt to structurally unprecedented environments
- Create artifacts that surprise even the system's designers/trainers
- Modify its own cognitive processes to expand its own capabilities

**Formalizability:** HIGH — This is essentially a topological/set-theoretic property. "Closed-ended" means the system's behavioral space is a closed set under some appropriate topology on the space of possible behaviors, where the closure operation is defined by the training distribution + permissible transformations (interpolation, recombination). "Open-ended" means the system can reach points *outside* this closure.

### 2. The Closed-Ended / Open-Ended Spectrum

**Epistemic status: self-observational insight, speculative**

Goertzel's key insight that even humans operate in "closed-ended mode" most of the time implies:

**Claim:** Closed-endedness and open-endedness are not binary types of systems but **modes of operation** that a system can occupy, with the key question being: *What triggers or enables the transition from closed-ended to open-ended mode?*

This reframes the AGI challenge: The problem isn't building a system that is *always* open-ended (humans aren't), but building a system that can **shift into open-ended mode** when needed — when confronted with genuine novelty, when routine recombination fails, when creative breakthrough is required.

**Implications:**
- A closed-ended quasi-human fails not because it lacks *capacity* for any single task, but because it lacks the **mode-switching capability** that enables open-ended exploration
- The "secret ingredient" of human intelligence may not be any particular cognitive algorithm but the **meta-cognitive ability to recognize when familiar patterns are insufficient and shift to generative/exploratory processing**
- This connects to Goertzel's broader work on reflective consciousness: reflective abstraction (which closed-ended quasi-humans lack) may be exactly the mechanism that enables mode-switching

**Formalizability:** MEDIUM-HIGH — The mode-switching framework is amenable to dynamical systems formalization: closed-ended = operation within a basin of attraction; open-ended = transition between basins or escape from any fixed attractor. The "trigger" is a bifurcation condition.

### 3. The Society-Level Intelligence Argument

**Epistemic status: observational argument with formal implications**

**Claim:** An individual closed-ended quasi-human might approximate an individual human's everyday competence, but a *society* of closed-ended quasi-humans would be "vastly less generally intelligent than a society of real humans."

**Reason:** Human societies generate collective intelligence that exceeds any individual's capability, through:
1. **Extreme variance:** Rare creative geniuses who make disproportionate contributions (Hendrix, Kandinsky, Einstein)
2. **Cultural elicitation:** Social/cultural patterns that draw creative behavior from "ordinary" members
3. **Compositional emergence:** Group dynamics that produce novel solutions no individual would reach alone

A society of closed-ended quasi-humans would have:
1. No outlier geniuses (all bounded by the same training closure)
2. No cultural elicitation beyond what's in training data
3. Group dynamics limited to recombinations of individually available patterns

**Formalizability:** HIGH — This is a distributional argument. If individual intelligence is drawn from a distribution with some variance, the *maximum* intelligence in a population of N is the N-th order statistic. For closed-ended systems with bounded behavioral space, the order statistic saturates; for open-ended systems (heavy-tailed distribution), it grows with N. The collective intelligence difference is thus a function of the tail behavior of the individual intelligence distribution.

### 4. The Temporal Argument Against Closed-Endedness

**Epistemic status: thought experiment with formal implications**

**Claim:** "A hypothetical ordinary human with life extended to say 100K years ... would in many circumstances eventually demonstrate general intelligence well beyond that of a closed-minded quasi-human with a similar lifespan — because even an ordinary average person when given enough time and the appropriate environment has a brain capable of going well beyond its training data in a profoundly creative way."

This is a **distinguishing test** for open-endedness: given sufficient time and appropriate environmental stimulation, can the system exceed the bounds of its initial training?

**Formalizability:** HIGH — This can be expressed as: for an open-ended system S, limt→∞ Reach(S, t) is unbounded (or at least exceeds any fixed boundary defined by initial training). For a closed-ended system, Reach(S, t) → C where C is the closure of the training distribution. The temporal argument says: human intelligence has the asymptotic unboundedness property; deep-neural-net intelligence does not.

### 5. The Consciousness Gradient

**Epistemic status: speculative, panpsychist framing**

**Claim:** A closed-ended quasi-human would have conscious experience (panpsychism), but its conscious experience would be impoverished relative to human experience, because:
- Reflective consciousness (the distinctively *human* kind) depends on reflective abstraction
- Reflective abstraction depends on abstract knowledge representation
- Current deep neural nets utterly lack abstract knowledge representation
- Therefore: quasi-human consciousness ≈ "an extreme form of what we experience when in a state of mind that's tightly focused on the very particular details of some real-world-focused task which doesn't require especially deep thought or imagination or rich whole-soul engagement"

This is a **consciousness-as-function-of-architecture** argument: the richness of conscious experience correlates with the system's capacity for reflective abstraction, which in turn correlates with the openness of its cognitive architecture.

**Formalizability:** MEDIUM — The consciousness claim itself is hard to formalize (the hard problem), but the **correlation** between architectural properties (abstract representation, reflective abstraction) and cognitive capabilities (open-endedness) is formalizable. The chain is: abstract representation → reflective abstraction → mode-switching → open-endedness → richer/more varied cognitive states.

### 6. The "Quasi-AGI" Terminological Problem

**Epistemic status: conceptual analysis**

The article explicitly confronts the **inadequacy of "AGI" as a concept:**
- A closed-ended quasi-human *would* pass most AGI benchmarks (it handles the majority of everyday intelligent behavior)
- It would *fail* on the dimensions that matter most (innovation, adaptation, self-improvement)
- "General" intelligence has multiple dimensions: breadth of tasks vs. depth of novelty vs. recursive self-improvement capability
- The concept of AGI conflates these dimensions

**Proposed resolution:** Quasi-AGI as distinct from true AGI, where the distinguishing criterion is open-endedness (capacity for genuine innovation beyond training data).

This connects to Goertzel's repeated argument (in GTGI and elsewhere) that intelligence should be measured by **pragmatic generality** — the range of environments and goals a system can handle — but that range must include *genuinely novel* environments and goals, not just recombinations of familiar ones.

**Formalizability:** HIGH — this is a definitional issue that can be resolved by incorporating novelty/extrapolation metrics into intelligence measures.

---

## Formal Candidates

### FC-1: Behavioral Closure Operator

**Claim:** The "closed-endedness" of a cognitive system can be formalized as a closure operator on behavioral space.

**Proposition sketch:** Let B be the space of possible behaviors. Let D ⊆ B be the training distribution (behaviors observed in training data). Define a closure operator Cl: 2^B → 2^B that maps D to the set of all behaviors reachable via interpolation, recombination, and mutation within the system's architectural constraints. A system is **closed-ended** iff its reachable behaviors ⊆ Cl(D). A system is **open-ended** iff its reachable behaviors ⊄ Cl(D) — i.e., it can reach behaviors outside the closure of its training data.

The closure operator Cl depends on the system's architecture:
- For deep neural nets: Cl ≈ convex hull of D in activation space (interpolation + recombination)
- For Hyperon-style architectures: Cl is much larger (includes logical inference chains, analogical transfer, evolutionary discovery) — potentially unbounded

**Formalizability:** HIGH. The mathematical framework of closure operators and closure spaces is well-established. The key research question is: what is the correct closure operator for each class of cognitive architectures?

### FC-2: Open-Endedness as Attractor Escape

**Claim:** Open-ended cognition can be modeled as the ability to escape attractors in cognitive state space, while closed-ended cognition is confinement to a fixed attractor basin.

**Proposition sketch:** Model a cognitive system as a dynamical system on state space X. Training creates attractor basins {A₁, ..., Aₖ}. A closed-ended system's trajectory remains within ⋃Aᵢ for all time. An open-ended system can, under appropriate conditions (novelty detection, creative pressure, reflective metacognition), undergo **bifurcation** — transitioning to a qualitatively new dynamical regime outside all existing attractor basins.

The "trigger" for mode-switching from closed to open is a bifurcation parameter. In humans, this might be: accumulated evidence that current patterns are insufficient (prediction error exceeding threshold), metacognitive recognition of stuckness, emotional/motivational push toward exploration.

**Formalizability:** HIGH. Bifurcation theory in dynamical systems is well-developed. The formalization challenge is identifying the correct state space and bifurcation parameters for cognitive systems.

### FC-3: Collective Intelligence Order Statistics

**Claim:** The collective intelligence of a population is determined by the tail behavior of the individual intelligence distribution, which is qualitatively different for open-ended vs. closed-ended systems.

**Proposition sketch:** Let I(s) be the intelligence (pragmatic generality) of individual system s. For a population P of N systems, collective intelligence IC(P) depends on max{I(s) : s ∈ P} plus interaction effects.

For closed-ended systems: I(s) is bounded above by some Imax (the closure boundary). Therefore max I → Imax as N → ∞. Collective intelligence saturates.

For open-ended systems: I(s) has a heavy-tailed distribution (some individuals, given time, can reach arbitrarily high intelligence). Therefore max I grows with N (extreme value theory). Collective intelligence is unbounded.

**Corollary:** The difference between a society of closed-ended quasi-humans and a society of real humans is not a quantitative gap but a **qualitative phase transition** in the tail behavior of the intelligence distribution.

**Formalizability:** HIGH. Extreme value theory provides the mathematical tools. The key empirical question is the shape of the intelligence distribution for different cognitive architectures.

### FC-4: Temporal Divergence Test for Open-Endedness

**Claim:** Open-endedness can be operationally defined by asymptotic temporal behavior: an open-ended system's competence grows without bound in sufficiently rich environments; a closed-ended system's competence saturates.

**Proposition sketch:** Let R(S, t) = total reachable competence of system S at time t in a sufficiently complex environment. Define:
- **Closed-ended:** limt→∞ R(S, t) = C < ∞ (converges to finite ceiling)
- **Open-ended:** limt→∞ R(S, t) = ∞ (diverges, potentially at varying rates)

The 100K-year-human thought experiment: R(human, 100000) >> R(quasi-human, 100000), because human R diverges while quasi-human R saturates.

**Formalizability:** HIGH. This is a growth-rate classification (analogous to computational complexity classes). The key formal question: what architectural features determine whether R(S, t) converges or diverges?

### FC-5: Reflective Abstraction as Mechanism for Open-Endedness

**Claim:** The capacity for reflective abstraction — representing and reasoning about one's own cognitive processes — is the mechanism that enables open-ended cognition, and its absence is what makes deep neural nets closed-ended.

**Proposition sketch:** Define reflective abstraction as the existence of a meta-level map M: CognitiveProcesses → Representations such that:
1. M is available to the system's reasoning processes (not just an external description)
2. M can be used to modify CognitiveProcesses themselves (not just observe them)
3. M is compositional (representations of compound processes are built from representations of component processes)

A system with reflective abstraction can:
- Detect when its current cognitive strategy is failing (via M-level monitoring)
- Generate novel strategies by recombining/modifying represented processes (via M-level reasoning)
- Evaluate and iterate on novel strategies (via M-level feedback)

This is the mechanism for attractor escape (FC-2): reflective abstraction provides the bifurcation parameter.

**Formalizability:** MEDIUM-HIGH. The meta-level map M is well-defined in principle (related to reflection in programming languages, metacognition in cognitive science). The compositional requirement connects to type theory. The key challenge: formalizing how M-level operations create genuinely new cognitive processes rather than just recombining existing ones.

---

## Connectivity Map

### → Three Viable Paths to True AGI (Substack 2022-08-25) [FORMALIZED]

- **Immediate sequel:** Published one day later. This article defines the *ceiling* (closed-ended quasi-human); the Three Paths article proposes the *routes past it*. Together they form a problem-solution pair.
- **Structural complement:** Closed-ended quasi-human = what deep nets can achieve at best. Three paths = what you need for truly open-ended AGI. The closed-endedness criteria defined here become the *adequacy conditions* for any viable AGI path: a true AGI path must produce systems that are NOT closed-ended by the criteria enumerated here.
- **The Cogistry connection:** The most interesting link is to the Cogistry recursive loop (Three Paths FC-3). If a closed-ended quasi-human can't seed a Singularity because it can't innovate, then the *specific formal property* that Cogistry needs to achieve is: breaking out of closed-endedness via recursive self-improvement. The Cogistry fixed-point question becomes: does the Cogistry loop produce a system that crosses the closed-ended → open-ended boundary?

### → General Theory of General Intelligence (arXiv:2103.15100 / Substack 2021-06-02) [FORMALIZED]

- **Intelligence measure refinement:** GTGI's pragmatic intelligence measure needs to be augmented with a *novelty dimension* to distinguish closed-ended from open-ended intelligence. A closed-ended quasi-human might score high on the GTGI measure within familiar environments but score zero on environments outside its training closure.
- **Cognitive synergy as open-endedness enabler:** GTGI's cognitive synergy theorem implies that diverse interacting cognitive processes (pattern recognition, logical inference, evolutionary learning, etc.) can jointly solve problems that no single process can — this is precisely the mechanism for escaping closure. A system with only one learning modality (gradient descent) may be closed-ended; a system with cognitive synergy may be open-ended.

### → Open-Ended Motivations (Substack 2021-08-13) [FORMALIZED]

- **Direct thematic connection:** "Open-Ended Motivations for AGIs, Humans and Beyond" directly addresses the motivation structures that enable open-ended cognition. The closed-ended quasi-human lacks these: its top-level goals are "specified by human developers" (closed set), whereas open-ended systems need goal generation/modification capabilities.
- **Motivation closure:** A closed-ended quasi-human is also *motivationally* closed-ended — it can pursue only goals within its specified set or goals constructable by decomposition of those goals. It cannot generate genuinely new top-level goals through self-reflection.

### → Facing the Meta-Abstracted Dragon (Substack 2022-07-31) [FORMALIZED]

- **Written 24 days before this article.** The Meta-Dragon article's exploration of cognitive synergy through Jungian archetypes illuminates *what's missing* in a closed-ended quasi-human: the dynamic interplay of Thinking/Feeling/Sensing/Intuiting, and especially the Shadow integration process, which is a paradigm case of open-ended self-transformation.
- **Evil and closed-endedness:** The meta-dragon article discusses "evil" as a failure mode of cognitive dynamics. Closed-ended quasi-humans could be made with "a variety of ethical orientations" but lack the self-reflective capacity to evolve ethically — they're stuck with their training-data ethics, for better or worse.

### → Symbolic Ruminations on Non-Symbolic Consciousness (Substack 2022-08-06) [FORMALIZED]

- **Written 18 days before this article.** The consciousness gradient described here (quasi-humans have impoverished experience) directly connects to the non-symbolic consciousness framework: non-symbolic consciousness may be exactly the dimension of experience that's *preserved* in a closed-ended quasi-human (sensory immersion, task-focused flow), while *symbolic/reflective* consciousness is what's lost.

### → Paraconsistent AGI (Substack 2026-01-06) [FORMALIZED]

- **Paraconsistency and open-endedness:** Paraconsistent reasoning may be necessary for open-ended cognition because genuinely creative exploration produces contradictions that classical logic cannot tolerate. A closed-ended quasi-human, using only gradient-descent-style subsymbolic inference, never encounters or needs to handle explicit contradictions — its closure boundary keeps it away from the contradiction-generating frontier of knowledge.

### → LLM Consciousness (Substack 2026-05-06) [FORMALIZED]

- **Validation 4 years later:** This 2022 article predicted the upper bound of deep-learning approaches. By 2026, LLMs (GPT-4, Claude, etc.) partially validate the prediction: they demonstrate impressive behavioral breadth but systematic failures on genuinely novel reasoning tasks. The LLM consciousness article extends the analysis to the specific question of what kind of consciousness (if any) LLMs have — connecting to the consciousness gradient structure here.

### → Hyperseed-1 and Hyperseed v2 [FORMALIZED]

- **Ontological coverage test:** Hyperseed's core ontology should be rich enough to *distinguish* closed-ended from open-ended intelligence. Key primitives needed: PATTERN (present in both), EMERGENCE (present in both, but differently), SELF-ORGANIZATION (potentially the differentiator: genuine self-organization → open-ended; imposed-organization → closed-ended), NOVELTY/CREATION (absent from closed-ended systems by definition).
- **Inference guidance implication:** If Hyperseed guides Hyperon's inference, it should preferentially guide toward *open-ended* reasoning strategies — those that break out of pattern recombination into genuine novelty generation.

### → Evidence Is to Logic What Energy Is to Physics (Substack 2026-03-10) [FORMALIZED]

- **PLN and closure:** PLN's evidence-weighting mechanism operates on observed evidence. In a closed-ended system, evidence is bounded by training data. In an open-ended system with PLN, new evidence from novel experiences can drive inference chains that reach genuinely new conclusions. The conservation-of-evidence framework provides a formal basis for distinguishing these cases.

### → How Superhuman Superminds Will (Mostly) Transcend Suffering (Substack 2022-03-12) [FORMALIZED]

- **Closed-ended systems can't transcend suffering:** The transcend-suffering article envisions superintelligences that transform their own subjective experience at deep levels. A closed-ended quasi-human cannot do this — it's stuck with whatever experiential palette its architecture produces. This is another instance of the open-endedness requirement: transcending suffering requires open-ended self-modification of consciousness, which requires reflective abstraction, which is precisely what closed-ended systems lack.

### → The Coming Consciousness Explosion (Substack 2021-06-04) [FORMALIZED]

- **Consciousness explosion requires open-endedness:** The Consciousness Explosion thesis presupposes cognitive systems that can expand their own consciousness — i.e., that are open-ended with respect to consciousness itself. Closed-ended quasi-humans, by definition, cannot participate in a consciousness explosion; they are experientially static.

### → Bach, Joscha (conversation at AGI-22)

- **Cited as interlocutor.** The thought experiment was catalyzed by conversation with Bach about "how far it MIGHT be possible to get via extending and combining current deep neural net technologies." Bach's position (as construed here) seems to be that it might go further than expected but still hit the closed-ended ceiling.

### → Marcus, Gary (fireside chat at AGI-22)

- **Cited as skeptic.** Marcus's position (as construed here) is that deep neural nets can't even reach the closed-ended quasi-human level — he doesn't think combining them would produce even that much. This positions Marcus as *more pessimistic about deep learning* than Goertzel.

---

## Assessment

**Novelty:** HIGH — The "closed-ended quasi-human" concept is an original and useful formalization of a widely-felt intuition about deep learning's limitations. The article adds value beyond generic "neural nets can't do real AI" arguments by:
1. Granting maximum benefit of the doubt (upper bound framing)
2. Precisely enumerating the closure properties (behavioral, adaptive, creative, recursive)
3. Drawing the non-obvious implication that *most humans operate in closed-ended mode most of the time* — making the distinction a spectrum/mode rather than a binary type
4. Identifying the society-level and temporal-divergence arguments that sharpen the distinction

**Connectivity:** VERY HIGH — This is the **definitional complement** to "Three Viable Paths." Together they form a two-paper argument: (1) here's the ceiling deep learning hits (this article), (2) here are the ways to break through it (Three Paths). Every formalized entry about open-ended intelligence, cognitive synergy, consciousness expansion, or recursive self-improvement connects back to this article's definition of what closed-endedness *is* and why it's insufficient.

**Formalization priority:** The most promising formal candidates:
1. **FC-1 (Behavioral Closure Operator)** — The foundational formalization. Everything else depends on making "closed-ended" mathematically precise. Closure operators are well-studied; the novelty is applying them to behavioral/cognitive spaces.
2. **FC-2 (Open-Endedness as Attractor Escape)** — The dynamical-systems formulation is the most natural bridge to Goertzel's broader framework (complex systems, self-organization, emergence). Connects directly to the mode-switching insight.
3. **FC-4 (Temporal Divergence Test)** — The most operationalizable formal candidate. Could in principle be tested empirically: run closed-ended and open-ended systems in rich environments for extended periods and measure competence growth curves.
4. **FC-5 (Reflective Abstraction as Mechanism)** — The most architecturally prescriptive: tells you *what to build* to achieve open-endedness.

**Key structural contribution to Hyperseed:** This article provides the **negative criterion** for Hyperseed-guided AGI. Hyperseed must:
1. Define primitives that *distinguish* closed-ended from open-ended systems (NOVELTY, SELF-MODIFICATION, REFLECTIVE-ABSTRACTION as primitives or composite concepts)
2. Guide inference toward open-ended strategies (not just pattern recombination)
3. Recognize when a reasoning process is operating in "closed-ended mode" and trigger mode-switching

**Relation to 2026 state of play:** The closed-ended quasi-human prediction has been substantially validated by 2024-2026 developments:
- GPT-4, Claude 3.5/4, Gemini demonstrate impressive behavioral breadth but systematic failures on genuinely novel reasoning (ARC-AGI, novel mathematics, truly creative art)
- The "faking it" phenomenon Goertzel described matches observed LLM behavior: convincing surface-level performance that breaks down under probing for genuine understanding
- The integration direction Goertzel described (multi-modal, embodied, end-to-end trained) is exactly the trajectory of frontier labs (GPT-4o, Gemini, multimodal agents) — but these remain closed-ended by the criteria defined here
- The society-level argument gains urgency: as AI-generated content saturates the training data ecosystem, are we creating a *society of closed-ended quasi-AI* that suppresses the open-ended creative variance that human societies naturally produce?
