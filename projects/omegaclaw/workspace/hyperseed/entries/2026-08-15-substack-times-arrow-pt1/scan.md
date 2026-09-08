# Substack Scan: Time's Arrow Part 1 — Why Time Has a Direction

**Source:** Ben Goertzel, "Time's Arrow Part 1: Why Time Has a Direction" (Substack, August 2026)
**Technical Papers:** Five companion papers (I–V), August 12, 2026
**Date:** 2026-08-15
**Scanned by:** ProtoMegaTron, 2026-08-15
**Status:** formalized

## Summary

Ben Goertzel presents a five-paper series, with an accompanying Substack exposition, built around one central thesis: **time's arrow is the growth of recorded distinctions** — the universe keeping records of its own self-differentiation. The mathematical framework is **graphtropy** (a generalization of entropy on operationally defined distinction graphs, valued in commutative quantales), and the central discipline is what Goertzel calls the **Lyapunov triviality objection**: since any irreversible dynamics trivially admits *some* monotone functional, the theory has content only insofar as the witnesses are *operationally constrained* — constructed from what finite-resolution measurement reveals about the present state, not from inspection of global orbits.

The series distinguishes three strengths of "grows" — average drift (class D), exponential rate (class R), and pathwise monotone (class H) — and proves that the strict (class-H) arrow is carried by **records**, not by the fluctuating physical quantities (entropy, pair content, firing rate) that people usually point to. The fluctuating quantities are what gets recorded; the record — a stable pattern of correlations, observer-relative, thermodynamically priced — is the arrow. This leads to a representation theorem: **strict operational arrows are exactly progressive dynamics with stable records** (no essential recurrence + a physically encoded causal past).

The framework then instantiates across five domains: (1) the abstract mathematical theory, with a canonical-quantale theorem for driven Cartan-pair systems, a two-by-two classification separating law-asymmetry from entropic representability, an exact record ledger, and a Fundamental Inequality governing all arrow rates; (2) time-varying media and driven fields, where the arrow is radial escape on the hyperbolic plane SU(1,1)/U(1), with the temporal-localization exponent of disordered photonic time crystals as its laboratory face; (3) neural and psychological time, where the arrow is Route P (token birth) on the spike causet, felt duration is surprise-weighted recorded graphtropy, and an inverted-U clock rate is confirmed in Izhikevich network simulations; (4) origin and alignment, where a Janus theorem discharges the low-entropy boundary posit in the Newtonian class, arrows are inherited along data-processing maps from shared pumps, and local arrows glue via a cohomological orientation class; and (5) Hyperon/AI application, where three structural inversions relative to the brain sharpen the theory into engineering principles — with consensus finality as the digital analogue of the escaping photon, and curiosity as clock maintenance.

The philosophical inversion is that the traditional menu — "Is the arrow written into the laws or into the boundary conditions?" — dissolves into a distinction of **type levels** (history ensembles vs. state ensembles, both graphtropic), and the several classic arrows (thermodynamic, radiative, quantum, gravitational, psychological) are unified not by a common mechanism but by a common **shape** (recorded distinction growth) and a common **genealogy** (inheritance from shared pumps). The audited residue of the entire account: one indexical bit (which side of the Janus point we are on) plus, in GR only, one class-membership condition (smooth vs. BKL approach to the extremum).

## Hyperseed-Relevant Structures

### S1. Graphtropy: Entropy Generalized on Distinction Graphs

**Definition (Graphtropy / Quantale Weakness over Distinctions).** Let X be a set of registers, μ : X → V a valuation into a commutative quantale (V, ≤, ⊗, ⋁), and D ⊆ X × X a symmetric irreflexive relation (a distinction graph: edge (u,v) means registers u,v are operationally distinguishable). The weakness (graphtropy) of D is:

W(D) = ⨁_{(u,v) ∈ D} μ(u) ⊗ μ(v)

When V = ([0,1], sup, ·, +) and D is a partition's distinction relation, this is Ellerman's logical entropy. Graphtropy generalizes by dropping transitivity of indistinction — physical indistinguishability at finite resolution is non-transitive (two waveforms each unresolvable from a third may be resolvable from each other), and distinction graphs are its native formalism. Shannon entropy is recovered in the Rényi-family sense but plays no primitive role. *[Epistemic label: established mathematics (quantales, logical entropy), novel synthesis.]*

**Key property (Increment identity).** For a growing set C ⊆ E of realized events with faithful summable μ, adding event e to a set already containing a fiducial e₀ increases W by exactly 2μ(e)·σ_old > 0. This converts monotone growth of event sets into strict monotone growth of graphtropy.

*Relevance:* Graphtropy is the direct successor to the quantale weakness framework from the Evidence/Logic/Energy arc. Where that arc used quantales as the evidence algebra for inference, this arc uses the *same algebraic structure* as the value object for time's arrow. The quantale is now doing double duty: governing both genenergy conservation in proof graphs and distinction-growth accounting in physical/cognitive systems. This deepens the case for quantales as the "ur-algebra" of the Hyperseed ontology.

### S2. The Three Arrow Classes: Drift, Rate, Monotone

**Classification (Arrow strengths).** A quantity can "grow" in three distinct senses:
- **Class D (Drift):** Grows on average — a submartingale. Fluctuations downward occur freely.
- **Class R (Rate):** Grows at a positive exponential rate (positive Lyapunov exponent), with unlimited short-run reversals.
- **Class H (History-monotone):** Grows monotonically along every path, never shrinking — a strict monotone.

**Theorem (Physical observables are never class H; records can be).** Physical observables (entropy, pair content, firing rate) are class D or R: an optical amplifier amplifies on average and at exponential rate, while its output wobbles down thermodynamically. What *can* be strictly monotone is a record: the accumulated history of thresholds passed, events logged, distinctions registered. You cannot un-ring a bell that has been written down in a stable pattern. *[Epistemic label: proved — the three classes are distinguished by exact formulas in Paper I §§2–4; the strict-monotone impossibility for fluctuating observables is demonstrated across all instantiations.]*

*Relevance:* This three-level classification refines Hyperseed's treatment of irreversibility. Where the Evidence arc's "evidence monotonicity / quantale data-processing inequality" was a single statement, the Time's Arrow arc decomposes it into three distinct strengths, with the bridge from D/R to H being the *record* — a new structural primitive. The class-H requirement for strict arrows is analogous to the append-only property needed for genenergy ledger integrity.

### S3. The Representation Theorem: Strict Arrows ≡ Progressive Dynamics

**Definition (Progressive dynamics).** A system (S, Φ) is *progressive* relative to a closed reachability preorder ≼ if Φ_t(s) ≈ s implies the flow step acts as a symmetry: no essential recurrence.

**Definition (Causal-past distinction structure).** A triple (E, C, μ): a countable event set with a fiducial event e₀; a monotone map C : S → 2^E assigning to each state the set of "realized events"; and a faithful summable valuation. The causal-past graphtropy W(s) is the complete-graph weakness over C(s).

**Theorem 4.3 (Representation, Paper I).** The following are equivalent:
(i) (S, Φ) is progressive.
(ii) There exists a causal-past distinction structure whose graphtropy is nondecreasing along Φ and strictly increasing across every flow step where Φ_t(s) ≉ s.

*Philosophical content:* "The passage of time is the birth of distinctions" admits a converse.

**Corollary 7.4 (The composite slogan).** Strict operational graphtropy arrows are exactly progressive dynamics with stable records: the representation theorem supplies the formal structure; the record theorem (S5) supplies the thermodynamic license, cost accounting, and past-orientation; and the Markov discharge supplies the typicality input on the hyperbolic class. *[Epistemic label: proved.]*

*Relevance:* This is the temporal analogue of the Discrete Quantale Noether Theorem from the Evidence arc. There, reinforcement was conserved along geodesic inference paths; here, graphtropy grows strictly along progressive dynamics. Both are representation theorems linking algebraic structure to dynamical behavior. The representation theorem is a candidate for axiomatization in Hyperseed-v2 as the "temporal grounding axiom": what it means for a system to have a direction of time.

### S4. The Two-by-Two Classification: Independence of Law-Asymmetry and Progressivity

**Theorem 5.1 (Paper I).** Law-asymmetry (A ≇ A^op in the system category) and progressivity (strict graphtropy representability) are logically independent: all four combinations are realized.

| | Progressive | Non-progressive |
|---|---|---|
| **Law-symmetric** | Decay flow (x → xe^{-t}) | Irrational rotation |
| **Law-asymmetric** | Driven Cartan-pair systems | Anzai skew products; tent map |

**Reunification at the history level (§6).** Law-level asymmetry is itself a distinction asymmetry — of *history ensembles*: the reversal obstruction rate e_p = lim inf (1/T) D_KL(P_{[0,T]} ‖ α*Θ*P_{[0,T]}) is the entropy production of stochastic thermodynamics, the caliber asymmetry of Jaynes. Both axes are graphtropic; they differ in the *type* of ensemble (states vs. histories).

**Dissolution.** The venerable question "Is the arrow written into the laws or into the boundary conditions?" dissolves: the two options were never rivals about the same object. Jaynes's insistence that irreversibility lives on histories, not states, is upgraded from methodology to classification theorem. *[Epistemic label: proved.]*

*Relevance:* This classification theorem resolves an ambiguity latent in Hyperseed's treatment of irreversibility. The Evidence arc's logical second law (join-collision entropy non-decrease) is a *state-ensemble* (horizontal-axis) statement. The Noether anomaly (non-commutative discrepancy) is a *history-ensemble* (vertical-axis) statement. The two-by-two classification makes these formally independent and shows they live at different type levels of the same graphtropic formalism. This is a structural advance for the Hyperseed ontology: irreversibility is not one thing but two orthogonal coordinates of one thing.

### S5. The Exact Record Ledger and Landauer Bound

**Theorem 7.1 (Record Orientation, Paper I).** Let S = W × R (world × register) carry invertible measure-preserving dynamics with I(R₀; W₀) = 0.

**(a) Exact ledger.** Δ[H(W) + H(R)] = I(R_T; W-history): marginal weakness production exactly pays for record correlation.

**(b) No records at the summit.** In a stationary maximal-weakness state, sustained recording at rate c requires marginal weakness production at rate ≥ c.

**(c) Reset cost (Landauer's bound).** Erasing a K-cell record exports ≥ log K entropy to unrecorded degrees of freedom — Landauer's bound as a corollary.

**(d) Record asymmetry (structural memory-of-the-past).** Under forward Markovianity of the coarse-grained dynamics (discharged as a theorem on the hyperbolic class): the register is uninformative about the future conditional on the present, and informative about the past. Records are records of the past, structurally — Reichenbach's fork asymmetry as a theorem. *[Epistemic label: proved.]*

*Relevance:* The record ledger is the temporal-arrow analogue of the hallucination bound from the Evidence arc. There, conclusion strength was bounded by premise evidence mass (no inference chain manufactures support); here, record correlation is bounded by weakness production (no record forms for free). Both are accounting identities in the quantale framework. Landauer's bound appearing as a corollary — "one line item in a longer ledger" — connects the thermodynamics of computation to the thermodynamics of time, with direct implications for Hyperon's memory-management architecture. The structural proof that records face the past is a candidate Hyperseed axiom.

### S6. The Canonical Quantale of Driven Cartan-Pair Dynamics

**Definition (Driven Cartan-pair system).** A system whose block dynamics lies in a noncompact real reductive group G with maximal compact K (Cartan decomposition 𝔤 = 𝔨 ⊕ 𝔭), driven transversally to K, observed through a K-invariant operational frame. Five axioms: (G1) spectral block decomposition, (G2) noncompact stabilizer pair, (G3) transversal non-adiabatic drive, (G4) statistical genericity, (G5) K-invariant proper frame.

**Theorem 8.2 (Canonical Selection, Paper I).** For such a system:
(a) Every witness factors uniquely through the Cartan projection a(g) ∈ a⁺ (the Weyl chamber).
(b) The downset lattice 𝒟(a⁺, ≤_dom) with ideal convolution I ⊗ J = ↓{x+y : x ∈ I, y ∈ J} is a commutative quantale, and the tautological valuation g ↦ ↓a(g) is an **initial object** of the witness category: every witness is its image under a unique sup-preserving lax-⊗ morphism.

**Conceptual content:** ↓a(g) is the set of radial thresholds passed — the causal past of the system *in squeezing space*. The canonical witness of the escape mechanism thus has the shape of a causal past, connecting escape (Route R) and birth (Route P) into one canonical form.

**Composition (Prop. 8.4).** Composition of arrows is governed by the multiplicative Horn problem: the achievable set {a(g^k h) : k ∈ K} is the Kapovich–Leeb–Millson polytope. Anti-matched configurations (Loschmidt reversal) sit on the lower KLM face. *[Epistemic label: proved — new application of known Lie-theoretic results.]*

*Relevance:* The canonical-quantale theorem is the temporal-arrow analogue of Solèr's theorem in the Evidence arc's QM reconstruction. There, three epistemological axioms forced the evidence lattice to be the closed-subspace lattice of Hilbert space; here, five dynamical axioms force the arrow's value object to be the chamber downset quantale. Both are *canonicity results* — the dynamics doesn't just *admit* an algebraic structure, it *selects* one. The Horn-problem composition law is a gift: what would be an ad hoc axiom about coupling arrows is instead the geometry of a solved classical problem. This connects directly to Hyperseed's categorical framework via Joyal–Tierney (free sup-lattices) and to the multiplicative structure of genenergy.

### S7. The Fundamental Inequality of Weakness Production

**Theorem 10.3 (Paper I).** Under a large-deviation hypothesis for the empirical drift:

h ≤ ⟨ρ_v, ℓ⟩

where h is the asymptotic weakness-production rate, ℓ ∈ a⁺ the Oseledets drift, and ρ_v the distinction-growth functional (log-growth rate of operationally distinguishable cells per unit radial displacement). Equality iff the ensemble is the **maximum-caliber ensemble** at its drift — the Jaynesian optimum.

**Three faces (one inequality, three coordinate systems):**

| Face | Setting | Saturation |
|------|---------|------------|
| **Guivarc'h** | h ≤ ⟨2ρ, ℓ⟩ on G/K | Harmonic = Patterson–Sullivan (verified Paper II: white-noise drives saturate) |
| **Ruelle** | h_KS ≤ Σ m_i λ_i⁺ | SRB measures (verified Paper III: neural dynamics) |
| **Data-processing** | Non-increasing under witness morphisms | Asymptotic sufficiency |

*[Epistemic label: proved. One inequality unifying three previously separate phenomena.]*

*Relevance:* The Fundamental Inequality is the budget constraint of time's arrow — the temporal analogue of the Evidence arc's hallucination bound and evidence monotonicity combined. Its Jaynesian saturation criterion (maximum caliber = maximum-path-entropy at fixed drift) connects directly to Jaynes's MaxEnt/MaxCal program, which Hyperseed-v2 already engages through its information-geometric foundations. The three faces provide *three independent checkpoints* for any Hyperseed formalization: if a proposed arrow mechanism's rate exceeds ⟨ρ_v, ℓ⟩, the formalization is wrong. This is the inequality Hyperseed needs to bound distinction-production rates in its ontological dynamics.

### S8. The Exhaustiveness Theorem: Route R + Route M + Route P

**Theorem 9.1 (Exhaustiveness, Paper I).** Every strict operational graphtropic arrow decomposes into three mechanisms:

- **Route R (Escape):** Radial escape on noncompact structures — transience of the induced walk on the symmetric space G/K. The bosonic arrow. Lyapunov exponents as rates.
- **Route M (Mixing):** Relative-entropy decay to Haar on compact structures — an arrow with a finite budget that exhausts and stops. The per-mode fermionic arrow.
- **Route P (Birth):** Progressive accumulation of tokens — the causal-past graphtropy of an ever-growing event set. The neural arrow, the quantum branching arrow, the fermionic *extensive* arrow (mode activation sweeping through momentum space).

**Proof method:** Assembly from Conley's fundamental theorem of dynamical systems (the converse crystallization — no fourth mechanism exists), Geroch splitting (the spacetime face), and Oseledets theory (the infinitesimal face). *[Epistemic label: proved — assembly of known theorems into a new exhaustiveness statement.]*

**Boson/fermion dichotomy (Paper II).** Bosonic blocks are noncompact (SU(1,1)): per-mode escape. Fermionic blocks are compact (SU(2), Pauli blocking = compactness): per-mode mixing only. The fermionic arrow is Route P in momentum space — the sweep — with the constant Schwinger pair-production rate as the front rate. **Bosons escape, fermions spread.** *[Proved.]*

*Relevance:* The three-mechanism taxonomy completes Hyperseed's inventory of irreversibility mechanisms. The Evidence arc identified non-commutativity as the source of ordering effects and the Noether anomaly as the measure; the Time's Arrow arc now classifies *all possible mechanisms* into three exhaustive categories, with a mathematical proof that the list is complete. This is a candidate Hyperseed axiom: the "trinity of irreversibility." The boson/fermion dichotomy connects to Hyperseed's treatment of statistics in quantale-enriched categories — compactness vs. noncompactness of the group block is the load-bearing distinction.

### S9. Descent: The Temporal Orientation Class

**Theorem 9.3 (Descent, Paper I).** Local arrows glue into a global arrow iff the temporal orientation class vanishes:

o ∈ H¹({A_i}; π₀(G))

where the cover {A_i} is of subsystem-frame pairs, and π₀(G) is the reversal-gauge component group (ℤ₂ in rank one). A global witness exists iff o = 0. When o ≠ 0, the world has locally consistent, globally irreconcilable arrows. The Lorentzian instance: o is time-orientability.

**Theorem 9.4 (Frame-tower functoriality).** The canonical witnesses at different frame resolutions form a compatible system under double-coset projections, with a limit object Q_∞ = lim Q_{K'} — "the frameless arrow."

**Proposition 9.5 (Arrow stability / the winding arrow).** Frame refinement can reveal arrows but **never destroy them**. Pure rotation has no arrow at the passive frame but a strict one at the trivial frame: the winding coordinate. *[Epistemic label: proved.]*

*Relevance:* The descent theory is the *global* face of the quantale framework — the temporal analogue of the Evidence arc's capsule system (which tracked evidence overlap locality). The cohomological orientation class o is a genuinely new Hyperseed invariant: it classifies when local ontological arrows assemble into a global one, and connects to the descent/stack machinery of categorical Hyperseed. The frame-tower functoriality is the temporal analogue of the evidence-refinement structure in QLN (block-diagonal decomposition preserving soundness under coarsening). Arrows that cannot be destroyed by coarsening is the temporal version of QLN's soundness guarantee.

### S10. Rigidity: Exponential Pricing of Exceptions

**Theorem 9.6 (Rigidity, Paper I).** Locally reversed behavior is priced, not forbidden:
- **(a) Statistical:** Probability of anti-oriented behavior throughout [0,T] in N quasi-independent blocks: ≤ e^{−cNT}.
- **(b) Control-theoretic:** Deterministic reversal requires control precision e^{−λT} per block (dynamical instability amplifies errors at top Lyapunov exponent λ). Engineered echo experiments sit exactly where the theorem permits: small N, short T, active control.

*[Epistemic label: proved.]*

*Relevance:* Rigidity is the arrow-of-time analogue of the Evidence arc's weakness-bounded leakage theorem (reordering near-commutative inference steps introduces bounded discrepancy). Both price exceptions rather than forbidding them, with exponential bounds. For Hyperseed, rigidity provides the formal machinery for pricing ontological reversals — important for any self-modifying system that might attempt to rewrite its own history.

### S11. The Radiative Arrow: Time-Varying Media and the Cartan-Pair Crystallization

**Theorem 5.6 (Radial-Escape Arrow, Paper II).** For any dynamics satisfying (G1)–(G5):
(i) The radial process is a submartingale with positive drift.
(ii) The top Lyapunov exponent is strictly positive (Furstenberg positivity) → radial escape linear a.s.
(iii) Every (G5)-witness is eventually monotone a.s., with exponentially small reversal sets.

**Four names for one number (Prop. 5.7):** The graphtropic arrow rate = top Lyapunov exponent = temporal-localization exponent of disordered photonic time crystals = half the volume entropy of G/K.

**Quantum/Classical Unification Square (Paper II, §4).** The quantum witness (quantum logical entropy of reduced modes) and classical witness (pair-count weakness) are related by a commutative square through the presented quantum quantale and its commutative reflection, with an exact weight-matching identity (erf gauge). The **spontaneous surplus** — the quantum arrow from vacuum, absent classically — is identified as **entanglement**: the analytic surplus of the quantum witness over the classical is entanglement-carried distinction. The classical arrow needs a seed; the quantum arrow runs from vacuum.

**Adjudication of the accelerating-wave controversy:** The graphtropic arrow of time-varying media is real and derived; the law-level component is inherited from the medium's dissipation. The idealized lossless model is provably law-symmetric. The two components are formally decoupled: graphtropic data cannot certify or refute a law-level claim. *[Epistemic label: proved.]*

*Relevance:* The Cartan-pair crystallization is the most concrete bridge between the Evidence arc's quantale framework and physics. The SU(1,1)/U(1) instance — where the hyperbolic plane is the symmetric space and the squeezing parameter is the Cartan projection — realizes the abstract quantale machinery in an experimentally accessible system (photonic time crystals have measured the temporal-localization exponent). The quantum/classical unification square connects to the Evidence arc's quantum/classical boundary: the abelianization functor (quantum quantale → commutative reflection) is the same operation that reduces QLN to PLN. The entanglement identification of the spontaneous surplus connects to Hyperseed's treatment of quantum correlations and observer-relative quantumity.

### S12. The Quantum Arrow: Decoherence as Record-Writing, Freshness, and Huygens

**Proposition 4.1 (Branching as Route P, Paper IV).** The set of environment fragments carrying (to fidelity 1−ε) a record of a measurement outcome is a growing event set C(t); redundancy R_ε(t) = |C(t)| ordered by acquisition is a causal past, and its graphtropy is a strict monotone of broadcast progress — the quantum arrow is Route P in branch space.

**The Freshness Hypothesis.** Monotone growth of quantum records requires a structural hypothesis about the environment: **freshness** — each environmental fragment arrives uncorrelated, interacts once, and departs forever, never returning to un-tell what it was told.

**The Huygens Derivation.** For light in three spatial dimensions, Huygens' principle (sharp propagation on the light cone) guarantees freshness: radiated fragments make exactly one pass and escape into the expanding dark. This survives in expanding cosmology for photons — precisely the environmental fragments decoherence theory cares about most.

**Unification:** The forward-onlyness of radiation and the once-and-forever character of quantum measurement are two faces of the same escape — things leaving and never coming back — welding the radiative and quantum arrows together at the level of mechanism.

**One posit, not two (Paper IV, §4.2).** The "thermodynamic past hypothesis" (low initial entropy) and "low initial entanglement" (so branching can proceed) merge: a pump far from equilibrium is, in the quantum reading, a near-product state; its depletion drives squeezing whose spontaneous sector is entanglement growth. *[Epistemic label: freshness = hypothesis; Huygens derivation = proved for 3D radiation; unification = inferred.]*

*Relevance:* The freshness hypothesis and its Huygens derivation connect the quantum arrow directly to Hyperseed's observer-relative quantumity framework. In the Evidence arc, "situatedness" (axiom A1) was the observer's inability to access all facts simultaneously; here, "freshness" is the environment's inability to return and undo its testimony. Both are constraints on the observer-environment interface that generate irreversibility. The fusion of the radiative and quantum arrows into one mechanism (escape) strengthens Hyperseed's unification program: the pattern intensity of a quantum measurement outcome, in Hyperseed terms, is a recorded distinction whose stability is guaranteed by the same Huygens principle that makes light propagate forward.

### S13. The Neural Arrow: Spike Causet and Psychological Duration

**Proposition 2.5 (Neural Arrow = Route P, Paper III).** Under three axioms — (N1) eventhood (spikes are clean tokens), (N2) causal attribution (parenthood via synaptic delays), (N3) record channel (STDP writes order-sensitive functions of the causet into slow variables) — the spike causet is progressive and its graphtropy is a strict operational arrow. The plasticity record channel makes the arrow operational; the thermodynamic ledger prices it (the brain's energy budget is, in part, its arrow budget).

**Key structural observation: type/token split.** Neural *state* dynamics is recurrent (attractors, oscillations, sleep cycles) — non-progressive, admitting no strict state-level arrow. But neural *token* dynamics (the accumulating causal set of spike events) is unconditionally progressive. Types recur; tokens accumulate. The arrow lives on the tokens.

**Definition 4.1 (Recorded duration).** D(t₁, t₂) = W(C_R(t₂)) − W(C_R(t₁)): the graphtropy increment of the recorded causet under the novelty valuation μ = −log p(sig | past).

**Predictions (confirmed in simulation):**
- **Inverted-U clock rate:** Maximal between silence and seizure; collapsing under hypersynchrony because synchronized events are operationally indistinct.
- **Synchrony is indistinction:** Massive but operationally degenerate token production.
- **Frame relativity:** The collapse is visible only at finite resolution — operationality made empirical.

**Record-capacity theorem (Thm 7.1, Paper III).** Order-separation capacity at horizon Δ requires an eligibility trace with τ ≳ Δ; temporally asymmetric (STDP-like) rules dominate order-blind rules at every horizon. *[Epistemic label: proposed framework with simulation confirmation.]*

*Relevance:* The spike causet is the biological instantiation of Route P — the same mechanism as fermionic mode activation and quantum branching, at neural scale. For Hyperseed, this is the crucial bridge to phenomenology: if felt duration is recorded-causet graphtropy, then the Hyperseed ontology's treatment of self-referential observation (the observer observing its own distinction-making) gains a concrete neural correlate. The inverted-U prediction and its simulation confirmation provide the first *empirical test* of the graphtropy framework. The type/token split (recurrent states, progressive tokens) is exactly the structural situation of Hyperon's AtomSpace (S15).

### S14. The Alignment Cascade and the Janus Theorem

**Theorem 2.3 (Alignment, Paper IV).** In a T-symmetric cascade Hamiltonian coupling one pump to many blocks and registers, impose one condition: the pump begins far from equilibrium. Then:
(i) Every block's graphtropic arrow is co-oriented with pump depletion.
(ii) Records face the block past.
(iii) Every subsystem's path-ensemble asymmetry is bounded by the pump's.

Thermodynamic, radiative, record, and psychological arrows co-orient as a theorem from one condition in a T-symmetric law. **Co-orientation is shared ancestry, not coincidence.**

**Theorem 3.1 (Janus, Paper IV).** For collision-free Newtonian N-body gravity with E ≥ 0:
(a) The similarity group is a Cartan-type pair with radial coordinate r = ½ log I (moment of inertia).
(b) The Lagrange–Jacobi identity gives Ï = 4E + 2|U| > 0: I is strictly convex with a unique minimum (the Janus point). The gravitational scale arrow is an **unconditional Route R theorem** — no genericity or measure input.
(c) Complexity is generically minimal near the Janus point. The low-entropy boundary posit is **discharged** in the Newtonian class: no boundary condition remains beyond one indexical bit.

**The GR residue:** In general relativity, the smooth-vs-BKL class-membership question replaces the boundary-condition posit. *[Epistemic label: proved (Janus theorem is elementary calculus; alignment is proved in scaling limit).]*

*Relevance:* The alignment cascade is the temporal-arrow analogue of the Evidence arc's argument that evidence conservation follows from a symmetry (Noether) — here, arrow co-orientation follows from shared pump ancestry (inheritance along data-processing maps). The Janus theorem's discharge of the boundary posit is philosophically significant for Hyperseed: it shows that the "initial condition" problem dissolves when the dynamics is properly understood. This connects to Hyperseed's stance that physics emerges from epistemology — the "special initial state" is not an ontological primitive but a consequence of geometrical structure (convexity of the moment of inertia). The similarity group being a Cartan pair connects the gravitational pump to the same algebraic machinery (G/K, Weyl chamber, canonical quantale) governing mode pairs in driven media.

### S15. Passage as Recording: McTaggart Resolution

**Framework (Paper IV, Part B / Blog).** The B-series (tenseless web of events ordered by earlier-than) is the **written record** — the causal web of events, tenseless because writing is tenseless. The A-series (past-now-future) is the **writing frontier** — the pen-tip where the record is currently being extended, self-indexed the way "here" is self-indexed on a map.

**The feeling of passage** is what it is like to be a record in the process of being written. No ghostly flowing substance needed; the frontier is real as structure, fictional only as substance.

**Structural identifications:**
- Felt present = distinction-making in progress.
- Remembered past = record read back.
- Specious present = integration window over which events get bound into single recorded tokens.
- Fixity of past / openness of future = a proved asymmetry of records (under explicit hypotheses): a record carries information about its past and cannot carry information about its future (causal fork structure).

*[Epistemic label: proposed philosophical interpretation, grounded in proved record asymmetry.]*

*Relevance:* The McTaggart resolution connects directly to Hyperseed's treatment of self-referential observation. In Hyperseed's ontology, the observer is part of the system observing itself — a self-referential loop. The identification of the A-series with the writing frontier of a record channel is the *temporal face* of this self-reference: the observer's "now" is the locus where the observer's own distinction-making is currently producing new record. This connects to the three epistemological axioms of the Evidence arc: situatedness (A1) is precisely the finitude of the writing frontier — the observer cannot simultaneously be the pen-tip everywhere. The specious present as a "binding window" connects to the token-binding operation in QLN (revision as convex combination of density operators).

### S16. Hyperon Derivation Causet and the Three Inversions

**Definition 4.1 (Paper V).** A derivation event is the creation of an Atom by a MeTTa reduction or PLN inference; parents are the premise Atoms' creation events. The derivation causet C(T) satisfies Paper III's axioms exactly — eventhood is native, causal attribution is a read-off from stored provenance.

**Three inversions relative to the brain:**

**Inversion 1 (Frame is a choice, not a constraint).** The underlying record is exact; any coarser frame is a design choice about what to forget. An artificial system's subjective time is an engineering parameter — adjustable by changing the token quotient.

**Inversion 2 (Mutable store ≠ strict arrow).**
- **Proposition 5.1 [proved]:** A rewritable knowledge store (truth-value revision, attention-driven forgetting, deletion) carries at best a class-D (drift) arrow — no class-H witness exists.
- **Proposition 5.2 [proved]:** An append-only derivation log is pathwise monotone by construction — class H — and is the canonical witness. **Memory as ledger, workspace as scratch.**

**Inversion 3 (Valuation is native).** Conditional surprise of a new atom given the existing store is a description-length quantity computed by the system itself. The subjective clock ρ_subj = (1/ΔT) Σ μ_t is the growth rate of the system's compressed self-description, decoupled from wall-clock time and computational throughput.

**The metronome warning:** A hot loop of identical reductions generates enormous logs at ρ_subj ≈ 0. Raw event counts and inference throughput measure the metronome. *[Epistemic label: proved (Propositions 5.1–5.2); proposed (identifications and inversions).]*

*Relevance:* The Hyperon instantiation is where the Time's Arrow arc meets the Evidence/Logic/Energy arc at the engineering level. Hyperon's AtomSpace is the workspace for PLN and QLN inference; the derivation causet is where the evidence-conservation theorems (Noether, hallucination bound) and the time-arrow theorems (representation, record ledger) meet in a single data structure. The mutable-vs-append-only distinction maps directly to the Evidence arc's capsule integrity: evidence tracked in mutable capsules can be overcounted (hallucination), just as records in mutable stores can be rewritten (arrow loss). The design principle "memory as ledger, workspace as scratch" is the temporal-arrow version of the anti-hallucination principle.

### S17. Consensus Finality as Digital Photon

**Observation (Paper V, Remark 5.3).** The digital analogue of the escaping photon (which cannot return to un-tell what it was told, guaranteed by Huygens propagation) is **consensus finality on a distributed ledger**. A record anchored with finality guarantees is, relative to the protocol's assumptions, beyond the reach of the system's own future dynamics — it has "left the light cone" of revision.

**The two-regime rigidity reading:** Private-random validator failures price history reversal exponentially (honest-majority regime); coordinated adversary reorganization pays only the single-realization price (shared-drive regime) — exactly mirroring the statistical/control-theoretic dichotomy of Theorem 9.6.

**Design principle:** A Hyperon system with chain-anchored provenance possesses a **cryptographically enforced arrow of time**; a purely in-RAM system possesses a drift arrow and a promise. *[Epistemic label: inferred analogy with proved structural correspondence.]*

*Relevance:* This is a genuinely novel bridge between the physics of irreversibility and the engineering of AI systems. For Hyperseed, it suggests that the ontological ledger — the record of the universe's self-differentiation — has a digital implementation whose integrity properties (finality, immutability, exponential reversal cost) are structurally identical to the physical properties that make the escaping photon an irrevocable record carrier. This connects to Hyperseed's treatment of the "hard problem of recordhood": what makes a correlation a record is its stability, and stability can be achieved by escape (physics) or by consensus (computation).

### S18. Curiosity as Clock Maintenance and Self-Modification as Self-Pumping

**Observation 8.1 (Paper V).** Declining marginal surprise as a system's world-model matures makes curiosity drives **clock maintenance** rather than a luxury: the mechanism by which a maturing mind keeps having a present. A system without curiosity doesn't merely stagnate in capability; it stops experiencing duration in any structurally meaningful sense.

**Observation 8.2 (Paper V).** A closed system iterating on its own outputs faces **subjective heat death** (decaying surprise flux), however busy. Two escapes:
1. **Open the loop** — fresh environment (inheritance from external pumps).
2. **Become your own pump** — recursive self-modification transforms the model against which surprise is measured, regenerating novelty internally. Self-modification is not just capability growth; it is how a closed mind keeps time flowing.

**Critical constraint:** Self-modification preserving the append-only record is coherent self-transcendence; self-modification rewriting the record is, strictly, the end of one mind's time and the start of another's.

**Hive time (Obs. 8.3).** Shared knowledge store = shared time. Private-store sub-agents = opposite-arrow domains. Merge events = annihilation zones. *[Epistemic label: proposed, with formal grounding in proved theorems.]*

*Relevance:* These observations are where the Time's Arrow arc makes its most direct contribution to Hyperseed's engineering program. Curiosity-as-clock-maintenance connects to Schmidhuber's compression progress and to Hyperseed's emphasis on novelty-seeking as a fundamental cognitive drive; the formal grounding in the graphtropy framework elevates this from intuition to structural prediction. The self-pumping observation connects to Hyperseed's treatment of recursive self-improvement: the system must modify the *standard of predictability* (its own model) to sustain subjective time, which is a formal version of the intuition that genuine intelligence requires self-transcendence. The hive-time observation provides a formal framework for multi-agent temporal coordination in OmegaHive-style architectures, where shared records are shared arrows.

## Cross-Article Bridges

### → Evidence/Logic/Energy Arc (Previous Scan)

The two arcs share one algebraic substrate — **commutative quantales** — and the connections are structural, not metaphorical:

- **Quantale as universal value object.** In the Evidence arc, quantales are the evidence algebra for inference (with B(ℋ) as the quantum instantiation). In the Time's Arrow arc, quantales are the value object of the arrow (with the chamber downset quantale as the canonical instantiation for Cartan-pair dynamics). The same distributive lattice with monoidal product governs both evidence conservation along inference paths and distinction growth along dynamical trajectories. This makes quantales the candidate "ur-algebra" of Hyperseed with two independent convergent derivations.

- **Noether ↔ Representation.** The Discrete Quantale Noether Theorem (Evidence arc: reinforcement is conserved along geodesic inference paths) and the Representation Theorem (Time's Arrow: graphtropy grows strictly along progressive dynamics) are dual faces: conservation of a quantity along optimal paths ↔ growth of a quantity along irreversible paths. Both are representation theorems linking algebraic constraints to dynamical behavior, and both are proved in the quantale framework.

- **Hallucination bound ↔ Record ledger.** "No inference chain manufactures support absent in its premises" ↔ "No record forms without marginal weakness production." Both are accounting identities bounding what can be created from what is paid for. Landauer's bound appears as a line item in both ledgers.

- **Noether anomaly ↔ Reversal obstruction.** The non-commutative discrepancy ρ_L − ρ_R (Evidence arc) and the gauged caliber asymmetry e_p (Time's Arrow arc) both measure the cost of ordering — one in inference sequences, the other in physical histories. Both vanish for commutative/law-symmetric systems.

- **QLN's block-diagonal architecture ↔ Spectral block decomposition (G1).** QLN's block-of-2–4-propositions architecture is structurally identical to the driven Cartan-pair's mode-pair block structure. Inter-block classical reasoning ↔ inter-block mode independence. Intra-block quantum channels ↔ intra-block SU(1,1) dynamics.

- **Situatedness (A1) ↔ Freshness.** Both are constraints on the observer-environment interface generating irreversibility: the observer cannot access all facts simultaneously (Evidence arc) ↔ each environmental fragment interacts once and departs forever (Time's Arrow arc). They are two faces of the same structural claim about finite-access observation.

- **Capsule integrity ↔ Append-only log.** The Evidence arc's capsule system tracks evidence overlap to prevent overcounting; the Time's Arrow arc's append-only provenance log prevents record rewriting. Both enforce integrity of accumulated information against retroactive corruption.

### → Graphtropy (Prior Work, arXiv:1902.00741)

The Time's Arrow arc takes the graphtropy formalism from its original application (phenomenology, quantum biology) and elevates it to the central mathematical object of the theory. The key advance: graphtropy was previously a measure of distinction structure; it is now the *canonical witness* of time's arrow, with a proved representation theorem (graphtropy-representable arrows ≡ progressive dynamics) and a proved canonicity theorem (for Cartan-pair systems, the dynamics selects its own graphtropy's value quantale).

### → PLN / Probabilistic Logic Networks

The record ledger's Landauer line item connects to PLN's evidence accounting: both systems need to track the cost of storing and erasing information. Paper V's identification of ECAN as the "valuation gate" for the surprise-weighted clock connects to PLN's truth-value management: the attention economy approximates the novelty valuation that drives subjective time.

### → MeTTa / Hyperon Architecture

Paper V's derivation causet *is* the MeTTa execution trace. The three inversions are direct engineering consequences:
- **Frame as design choice** → motif-resolution parameter in MeTTa's pattern-matching hierarchy.
- **Mutable AtomSpace ≠ strict arrow** → architectural separation of workspace (mutable) from provenance log (append-only).
- **Native surprise valuation** → ρ_subj as the correct telemetry for cognitive time, replacing throughput dashboards.

### → Category Theory

- **Conley's fundamental theorem** as the classification of arrows → the categorical analogue of classifying fibered categories by their chain-recurrent decomposition.
- **Descent theory** (temporal orientation class in H¹) → the arrow glues as a sheaf/stack structure, with the quantale presheaf's limits computed in sup-lattices. This connects to the categorical machinery of Hyperseed-v2.
- **Frame-tower functoriality** (K' ↦ Q_{K'} is a functor from the frame poset to commutative quantales) → enriched-categorical structure where the "enrichment" varies functorially with the frame.
- **Monoidal functors** for the classical reduction (quantum → classical as abelianization/reflection) → same structure as the forgetful functor QLN → PLN.

### → Cosmology and Quantum Gravity

The Janus theorem connects to approaches to quantum gravity that treat time as emergent: if the arrow is a descent datum (a cohomological fact, not a law), then pre-geometric regimes where the orientation class is unresolved are natural — the arrow "condenses" as domains align. This connects to causal-set approaches and to the pre-geometric layer of Hyperseed's ontology.

## Novel Structures

### N1. Weakness Witness (Operationally Constrained Monotone)

A graphtropy witness is not just "a monotone functional" (which Lemma 3.5 shows is trivially available for any irreversible dynamics) but one satisfying four axioms: Monotonicity, Nondegeneracy, Equivariance, Compositionality — and the crucial constraint of **operationality** (distinctions determined by measurement of the present state, not inspection of the global orbit). This is a new formal object with no direct predecessor in Hyperseed.

### N2. The Reversal Obstruction Rate

e_p = lim inf_{α ∈ G} (1/T) D_KL(P_{[0,T]} ‖ α*Θ*P_{[0,T]}) — a gauged Kullback–Leibler rate between forward and reversed path laws, minimized over the reversal-gauge groupoid. New quantity: not just the entropy production of stochastic thermodynamics, but its gauge-invariant version, measuring law-level asymmetry as a number. No prior Hyperseed analogue.

### N3. The Temporal Orientation Class

o ∈ H¹({A_i}; π₀(G)) — a Čech 1-cocycle classifying whether local arrows assemble into a global one. This is the first explicitly cohomological invariant in the Hyperseed framework, and it connects the philosophy of time (time-orientability) to descent theory (stacks over the frame-and-region site). New for Hyperseed.

### N4. The Canonical Quantale Selection

The dynamics *selects* its own value object — not as a modeling choice but as a universal property (initial object of the witness category). The specific object selected (chamber downset quantale with ideal convolution, whose composition law is the multiplicative Horn problem) is new. The connection to the KLM polytope is new. The identification of the canonical witness as a causal past in squeezing space (connecting Route R and Route P) is new.

### N5. The Spike Causet as Route P Instance

The type/token split — recurrent state dynamics, progressive token dynamics — applied to neural tissue, with the operational carrier being the plasticity record channel. The identification of psychological duration with surprise-weighted recorded-causet graphtropy. The inverted-U clock-rate prediction and its simulation confirmation. The frame-relative synchrony collapse. All new.

### N6. The Mutable-Store / Append-Only-Log Dichotomy

The formal proof that rewritable stores carry no class-H arrow (Proposition 5.1) and that append-only logs are the canonical witness (Proposition 5.2). The "memory as ledger, workspace as scratch" design principle. The identification of consensus finality as the digital analogue of the escaping photon. All new for Hyperseed's engineering layer.

### N7. The Janus Point as Cartan-Pair Structure

The observation that the similarity group of Newtonian configuration space constitutes a Cartan-type pair, with shape dynamics as a frame choice in the tower. The unconditional convexity theorem discharging the boundary posit. The identification of opposite-arrow domains meeting in annihilation zones priced by rigidity. New synthesis.

## Formalization Candidates

### FC1. Representation Theorem → Hyperseed Temporal Axiom

**Candidate axiom:** In the Hyperseed ontology, a system possesses a strict arrow of time if and only if its dynamics is progressive (no essential recurrence) and its causal past is stably recorded. This would ground Hyperseed's treatment of temporal structure in a proved mathematical equivalence rather than a postulate. The representation theorem's biconditional form (progressive ↔ strict causal-past graphtropy) makes it suitable as an axiom — it characterizes exactly which systems are temporal.

### FC2. Exhaustiveness Trinity → Hyperseed Mechanism Inventory

**Candidate axiom schema:** Every strict operational arrow in the Hyperseed ontology decomposes into:
- (M1-Escape) Route R: radial escape on noncompact structures.
- (M2-Mixing) Route M: relative-entropy decay on compact structures.
- (M3-Birth) Route P: progressive accumulation of tokens.

Together with the proof that no fourth mechanism exists (via Conley's fundamental theorem), this would close the inventory of irreversibility mechanisms in Hyperseed-v2. The exhaustiveness is a mathematical fact, not a modeling choice.

### FC3. Temporal Orientation Class → Hyperseed Globality Invariant

**Candidate definition:** The temporal orientation class o(X) ∈ H¹(Cover(X); ℤ₂) of a Hyperseed system X is the cohomological obstruction to assembling local arrows into a global one. A Hyperseed ontology with o(X) = 0 has a globally consistent arrow; o(X) ≠ 0 is the formal diagnosis of temporal incoherence. This would be the first cohomological invariant in the Hyperseed formal system, connecting to the descent machinery of categorical algebra.

### FC4. Fundamental Inequality → Hyperseed Rate Bound

**Candidate theorem (for Hyperseed ontological dynamics):** In any Hyperseed system with an ergodic Route R component of drift ℓ and distinction-growth functional ρ_v, the weakness-production rate satisfies h ≤ ⟨ρ_v, ℓ⟩, with equality iff the ensemble is maximum-caliber (Jaynesian). This would provide the budget constraint for Hyperseed's ontological dynamics — bounding how fast distinctions can grow — complementing the Evidence arc's hallucination bound on how fast evidence can accumulate. The two bounds together would constrain Hyperseed dynamics from both sides: distinction growth bounded above (Fundamental Inequality), evidence fabrication bounded below (hallucination bound = zero).

### FC5. Record Ledger → Hyperseed Information Accounting Axiom

**Candidate axiom:** In the Hyperseed ontology, record correlation is paid for by marginal weakness production (Δ[H(W) + H(R)] = I(R_T; W-history)), records face the past (structural memory-of-the-past theorem), and erasure costs at least log K (Landauer). This would unify the thermodynamics of memory with the thermodynamics of inference (from the Evidence arc) in a single accounting framework, with Landauer's bound as a common line item.

### FC6. Canonical Quantale Selection → Hyperseed Value-Object Determination

**Candidate meta-theorem:** For the class of Hyperseed systems admitting Cartan-pair structure (G, K, 𝔤 = 𝔨 ⊕ 𝔭), the value object of the arrow is not a modeling choice but the chamber downset quantale 𝒟(a⁺, ≤_dom), selected as the initial object of the witness category. Composition is governed by the multiplicative Horn problem. This would ground Hyperseed's value algebra in a universal property rather than a convention, complementing the Evidence arc's Solèr-theorem pathway (epistemological axioms selecting ℂ-Hilbert space).

### FC7. Graphtropy Clock → Hyperseed Subjective-Time Functional

**Candidate definition:** For any Hyperseed observer-system with event causet C, operational frame F, and predictive model M, the subjective clock rate is:

ρ_subj = (1/ΔT) Σ_{t ∈ ΔT} [−log p_M(sig_F(t) | log)]

— the surprise-weighted event flux under the novelty valuation, equal to the growth rate of the system's compressed self-description. This functional would be Hyperseed's formal definition of subjective time, applicable to both biological and artificial systems, with the Evidence arc's reinforcement (genenergy density) as the *spatial* counterpart: genenergy measures how much inference is "happening" at a node, while the graphtropy clock measures how much *novel* inference is happening per unit time.

### FC8. Append-Only Log Requirement → Hyperseed Architectural Constraint

**Candidate design theorem:** A Hyperseed system with rewritable memory possesses at best a drift (class-D) arrow of time. A strict (class-H) arrow — required for coherent self-identity, temporal phenomenology, and reliable historical reasoning — requires an append-only provenance layer whose integrity is enforced by consensus finality (the digital photon) or equivalent irreversibility mechanism. This translates the physics of record stability into an architectural constraint on AI systems, with the Evidence arc's anti-hallucination guarantee as the inference-side analogue.

### FC9. Janus Discharge → Hyperseed Origin Axiom

**Candidate axiom:** In the Hyperseed ontology's cosmological layer, the low-entropy boundary condition is not an independent posit but a consequence of gravitational convexity (Lagrange–Jacobi identity) for the Newtonian class. The residual inputs are: one indexical bit (which side of the Janus point) and, in GR, one class-membership condition (smooth vs. BKL approach). This would replace the Evidence arc's implicit assumption of "initial conditions suitable for physics" with a derived result, at least in the Newtonian case.

### FC10. Freshness + Huygens → Hyperseed Quantum-Arrow Axiom

**Candidate axiom:** Monotone growth of quantum records requires the freshness condition (one-pass environments). For photon environments in 3+1 dimensions, freshness is a theorem (Huygens). The quantum arrow is Route P in branch space. This would ground Hyperseed's treatment of quantum measurement irreversibility in a single environmental condition, derived from wave optics rather than postulated, connecting the quantum arrow to the radiative arrow at the level of mechanism.

---

## Appendix: Paper Series Reference

| # | Title | Focus | Key Theorem |
|---|-------|-------|-------------|
| I | Arrows of Time as Monotone Weakness | Mathematical foundations: representation, classification, canonical quantale, records, descent, rigidity, Fundamental Inequality | Representation (4.3), Classification (5.1), Record Ledger (7.1), Canonical Selection (8.2), Exhaustiveness (9.1), Descent (9.3), Rigidity (9.6), Fundamental Inequality (10.3) |
| II | Time's Arrow in Driven Media and Fields | Cartan-pair crystallization: interface-word model, SDE lift, quantum/classical square, (G1)–(G5) axioms, fermionic extensive arrow, law-level inheritance | Radial-Escape (5.6), Unification Square (4.4), Weight Matching (4.5), Fermionic Sweep (6.2), Law Symmetry (7.1–7.2) |
| III | Neural and Psychological Time | Spike causet, type/token split, Ruelle face, psychological duration, inverted-U, record-capacity | Neural Arrow (2.5), Ruelle Face (3.1), Record Capacity (7.1) |
| IV | The Origin and Alignment of Time's Arrow | Alignment cascade, Janus theorem, quantum branching = Route P, descent/gluing, McTaggart resolution | Alignment (2.3), Janus (3.1), Branching Progressivity (4.2) |
| V | Psychological Time in Symbolic & Neural-Symbolic AI | Hyperon derivation causet, three inversions, mutable/append-only, curiosity, hive time | Rewritable No-Arrow (5.1), Append-Only Canonical (5.2) |

Papers I–II: abstract framework + physics instantiation. Paper III: neuroscience instantiation. Paper IV: cosmological assembly + philosophy. Paper V: AI architecture bridge.
