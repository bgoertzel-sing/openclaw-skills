# Decisions

## 2026-07-24: Multi-depth beam ancestry is explicit

Beam retention is not final scientific acceptance. Nodes carry canonical
state, parent, proposal, and depth identities; public integration must accept
only the selected final path and label all other generated valid proposals
`beam_pruned`. Greedy remains the default and E0--E8 remain unauthorized.

No implementation decisions yet.


## 2026-07-03: Pure Python first, Hyperon-ready architecture

**Decision:** Implement CLA first as a pure-Python `chaoslang` library with a stable domain core and replaceable reasoning backends. Hyperon/Atomspace integrations should be optional adapters behind backend-neutral Protocols and a Fact layer, not core dependencies.

**Rationale:** Ben wants clustering/categorization and grammar-learning steps modular enough to Hyperon-ize later, but simple Python is the right first implementation substrate. The architecture document explicitly warns against making Hyperon a day-one runtime dependency.

**Implementation implications:** Keep `chaoslang.core` backend-neutral; represent chunks and categories as distinct types; make miners/inducers/searchers return typed `Proposal` objects; apply state changes only through `EditApplier`; add fact projection and `MemoryFactStore` before any Hyperon adapter.

## 2026-07-03: Pause OmegaSim until CLA detector exists

**Decision:** Pause OmegaSim as the active implementation lane until CLA or a similar attractor-grammar detector is working robustly across known strange attractors.

**Rationale:** Ben observed that OmegaSim cannot proceed sensibly if we cannot detect whether a simulated OmegaHive has complex strange-attractor structure.

**Next implication:** CLA should test on a range of strange attractors first, including dimensionalities comparable to initial OmegaSim vector traces; high-dimensional cases are deferred until a dimension-reduction step is designed.

## 2026-07-24 — Composite acceptance is one durable transaction

For M-D, ordered category/chunk sub-proposals are applied to immutable
intermediate states but a successful composite exposes exactly one durable
`Composite` edit. Nested composites are rejected in v1. Any failing sub-edit
discards the intermediate value, leaving the input state and edit log
unchanged. This matches the frozen atomicity and one-ledger-record invariants;
exact official-score acceptance remains the next separate wiring slice.

## 2026-07-24 — Mixed evidence fails closed for dependent components

Composite ranking estimates never authorize acceptance. The exact official
score and exact reconstruction are the only acceptance authority. Four-state
mixed-second-difference evidence is recorded only when both component edits
also apply independently to the same base state; dependent or invalid
components retain an exact atomic composite delta but use null mixed totals and
residuals rather than a fabricated counterfactual.
