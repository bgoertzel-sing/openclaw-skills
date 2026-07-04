# Internal reading program: SLT residual layers → Hyperseed synthesis

Created: 2026-07-02

Objective: come to an interesting, nontrivial Hyperseed-oriented perspective on Ben's SLT/weakness papers and the residual-layer experiment mandate, suitable for later formalization in `projects/hyperseed-formalizations/repos/hyperseed-formalizations`.

## Pass 1 — Map the shared invariant

Question: What object is held fixed across the papers?

Working answer to test: the central invariant is not a representation basis, goal text, or module boundary, but a local evidence geometry: neighborhoods, factorizations, and refinement moves are judged by free energy, LLC, additivity deviation, and interaction complexity.

Outputs:
- glossary: weakness=evidence, LLC, additivity deviation, dominated interaction, refinement DAG, causal fingerprint, regime signature;
- cross-paper table: where each invariant appears and what operational estimator is proposed.

## Pass 2 — Hyperseed conceptual mapping

Question: In Hyperseed terms, what kind of seed/process is a residual layer?

Candidate frame: a residual layer is a finite family of local corrective seeds attached to a base model's failure manifold. A good residual factorization is one whose seeds have approximately separable evidence-geometric support, commute under finite updates, and refine/split/merge under context shift through a refinement DAG.

Outputs:
- informal Hyperseed explanation;
- formal objects: Context, BaseProcess, ResidualSeed, EvidenceNeighborhood, Factorization, RefinementMove, CausalFingerprint;
- candidate predicates/atoms for later AtomSpace/PLN import.

## Pass 3 — Transformer/AGI interpretation

Question: Why should this matter beyond one RelaLeap experiment?

Candidate answer: SLT-guided residual learning is a microcosm of AGI adaptation: instead of forcing the whole learner into one global disentangled representation, keep a base generative/predictive process plus a controlled ecology of weak, modular, evidence-tested corrections. The structure controller is the embryo of a reasoning layer over learned factorizations.

Outputs:
- relation to incremental compression;
- relation to causal/predictive coding;
- relation to SubRep goal/subgoal decomposition;
- relation to regime-change and goal-stability monitoring.

## Pass 4 — Mathematical claims to scrutinize

1. When does evidence-ratio soft accuracy really inherit an interpretable O(lambda/n) correction?
2. Which approximations make finite transformer residual-layer LLC estimates meaningful?
3. Are mixed-Hessian/commutator proxies sufficient for dominated interaction, or only warning indicators?
4. How should LLC interaction information be estimated in small experimental arms?
5. What Hyperseed axiom schema captures refinement DAG dynamics without overclaiming semantic faithfulness?

## Pass 5 — Coding-agent translation

Produce concrete implementation guidance for the RelaLeap/pregate coding agents:
- data structures for arms, factorizations, evidence estimates, interaction audits;
- promotion/demotion/split/merge rules;
- minimal smoke tests and synthetic counterexamples;
- experiment-ledger schema.
