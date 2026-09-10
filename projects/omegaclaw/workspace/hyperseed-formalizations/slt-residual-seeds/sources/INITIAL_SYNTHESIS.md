# Initial synthesis: SLT-guided residual layers in the Hyperseed picture

Date: 2026-07-02
Status: first-pass working note, not a final formalization

## One-sentence thesis

SLT-guided residual-layer learning treats each residual component as a candidate local seed of corrective structure, and promotes only those seeds whose evidence geometry, causal fingerprint, and update dynamics show that they are real modular refinements rather than artifacts of a convenient coordinate basis.

## Core bridge

The uploaded papers repeatedly use the same bridge:

```text
weakness ≈ local evidence
free energy = -log evidence
LLC = asymptotic evidence-volume exponent
modularity = approximate additivity of free energies / LLCs
failure of modularity = interaction complexity, additivity deviation, mixed Hessian, commutator, leakage
adaptation = refinement-DAG moves over candidate factorizations
```

The earlier residual-layer mandate becomes an operational instance of this bridge. Instead of asking for the basis that best reconstructs a dense teacher correction, ask which factorization has locally good evidence while keeping interaction terms controlled.

## Hyperseed-oriented interpretation

In Hyperseed language, a transformer base model can be seen as a large learned process whose hidden state remains globally entangled. A residual layer should not be forced to discover the global true ontology of that hidden state. Rather, it should grow a small ecology of local seeds:

- each seed is a residual corrective factor with a support, causal fingerprint, and evidence neighborhood;
- a family of seeds becomes a factorization when their combined correction explains failures with dominated interactions;
- a refinement DAG records possible seed transformations: split, merge, mediate, demote, specialize, or transfer;
- the structure controller uses SLT/weakness scores to choose which refinement path is currently justified.

This makes residual learning a miniature AGI-relevant pattern: learning does not merely tune weights; it proposes, tests, composes, and revises local explanatory seeds.

## Why this seems broader than RelaLeap

1. **Incremental compression:** residual seeds are compression features for the base model's error stream.
2. **Causal/predictive coding:** gates and clarity penalties are mechanisms for making residual seeds commute and localize.
3. **Regime detection:** LLC/signature shifts say when a previously good factorization is no longer the right chart.
4. **SubRep:** subgoals/options mirror residual seeds: both need additivity checks, shared-representation corrections, and interaction information.
5. **Goal stability / semantics:** SLT diagnostics detect structural shifts, not semantic truth by themselves; the semantics papers add a route via distinctions → partitions → symmetries → singularities.

## Candidate formal objects for a Hyperseed note

- `Context c`
- `BaseProcess B`
- `ResidualSeed r_i`
- `ErrorStream E_B(c)`
- `EvidenceNeighborhood W(r_i, c)`
- `LLC lambda(r_i, c)`
- `Factorization F = {r_i}`
- `InteractionRemainder R_F`
- `DominatedInteraction(F, c, eta)`
- `CausalFingerprint phi(r_i, c)`
- `RefinementMove m: F -> F'`
- `WeaknessScore Z(F, c)` / `FreeEnergyScore J(F, c)`

## Immediate next formalization target

Draft a Hyperseed note tentatively titled:

> SLT-Guided Residual Seeds: Weakness, Evidence Geometry, and Refinement DAGs for Transformer Adaptation

It should connect `library/slt-residual-layers/` and `library/slt-hyperseed-synthesis/` and produce both prose and formal definitions/theorems suitable for the public `hyperseed-formalizations` repo after review.
