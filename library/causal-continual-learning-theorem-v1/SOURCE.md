# Source: Causal Coding and the General Causal-Continual-Learning Theorem

- Type: `PDF manuscript`
- Authors/organization: Ben Goertzel
- Publication/version date: 2025-12-01, v1
- Retrieved: `2026-07-25`
- Canonical URL or identifier: supplied directly by the author via Telegram; no public identifier recorded
- Local source path: `library/causal-continual-learning-theorem-v1/source.pdf`
- Text extraction: `library/causal-continual-learning-theorem-v1/extracted.txt`
- SHA-256: `5e7c86c810e36a8276acbacebc3cfe8777e9b66c0edbc203d0fca46920e93b82`
- License/access constraints: author-supplied manuscript; publication/reuse terms not stated
- Privacy tier: `local-private`
- Tags: causal coding, continual learning, commutators, predictive coding, modularity, category theory, incremental compression
- Related projects: `relaleap`, `carom`, `petta-memory`

## Summary

The manuscript proposes that continual-learning robustness follows when
context-conditioned learning updates are localized to causally meaningful
modules. In the smooth specialization, small off-support gradients and mixed
Hessian blocks are intended to imply small Lie brackets between context
gradient fields. A Baker-Campbell-Hausdorff expansion then relates small
brackets to small order dependence between sequential and mixture training.
Discrete and metric-enriched categorical versions express the same idea using
approximately local endomorphisms and pairwise "confusion costs." Applications
are sketched for causal-coding predictive networks, PC Transformers, and
incremental compression.

The strongest practically useful contribution is a testable diagnostic
program: measure update locality, finite-update A→B/B→A commutators, mixed
Hessian or HVP surrogates, and the sparsity of a context-confusion graph.

## Key claims or contents

- Causal modularity suppresses parts of the Lie bracket contributed by
  cross-support Hessians and off-support gradients (Sections 3.1–3.2,
  pp. 7–9).
- Sequential gradient flows differ from the flow of the summed field at
  second order through pairwise Lie brackets (Section 3.3, pp. 9–10).
- An approximate categorical construction bounds permutation/path dependence
  by a sum of pairwise locality and commutator defects (Appendix A.7,
  pp. 31–35).
- Causal gates and clarity penalties are proposed as mechanisms that may
  reduce off-support gradients, cross-module Hessians, and confusion-graph
  density in predictive-coding networks and Transformers (Sections 6–7,
  pp. 14–17).
- An incremental-compression specialization defines module influence by the
  compression penalty under module deletion and proposes context-local feature
  refinement plus learned clarity penalties (Section 8, pp. 17–26).

## Methods or implementation details

The paper is theoretical and schematic. Its empirical observables map naturally
to existing RelaLeap instrumentation:

1. finite-update commutator defect between matched A→B and B→A updates;
2. off-support gradient leakage under a frozen support estimator;
3. cross-block Hessian-vector-product norms;
4. causal intervention selectivity and support stability;
5. functional retention/plasticity outcomes under matched update budgets.

These should be evaluated jointly. A low commutator alone measures order
dependence, not retention or useful learning.

## Limitations and uncertainties

- **Theorem 1 needs stronger regularity for learned update fields.** A uniform
  value bound `||X̃_t-X_t||≤δ` does not by itself bound the perturbation of Lie
  brackets; a `C1`/Jacobian bound (or direct bracket bound) is needed.
- **Commutativity does not by itself rule out forgetting.** Two commuting
  updates may both change parameters in a way that worsens an earlier loss.
  Small commutators control order/path dependence relative to a reference
  composition; a forgetting guarantee additionally needs invariance,
  cross-loss directional-derivative bounds, or a joint-update retention
  premise. This affects Theorem 1(3), Theorem 4's interpretation, and the
  informal claims.
- **Theorem 2 is false as stated without an overlap restriction or explicit
  commutator premise.** Exact locality outside support (`ε=0`) permits two
  arbitrary, highly noncommuting maps on the same support. Non-expansiveness
  does not repair that counterexample.
- **The categorical result is chiefly a metric-monoid permutation bound.**
  Theorem 5 validly bounds distance between update orderings under its strong
  non-expansiveness and ideal-map assumptions, but it does not establish
  closeness to a separately defined joint-training operator or bounded
  task loss unless those links are added.
- The proposed metrics and update operators are assumed non-expansive; this is
  not established for ordinary gradient, AdamW, predictive-coding, or
  incremental-compression updates.
- The causal-gating-to-small-Hessian step is a proposed mechanism, not a
  proved consequence for the concrete neural architectures.
- The PAC discussion is currently a sketch: expectation/tail bounds require
  specified sampling, dependence, coverage, and concentration assumptions.
- No empirical results accompany the manuscript.

## Relevance to current work

This is a direct theoretical framing for RelaLeap's existing commutator,
off-support leakage, HVP, causal-fingerprint, and functional continual-learning
battery. It also clarifies the interpretation of the 2026-07-25 CMCP–ePC
negative: improved Task-B adaptation with worse Task-A forgetting is evidence
that the tested mechanism did not reach the required joint structural regime,
regardless of whether some representation or evidence-routing metrics improved.

The next scientifically clean test is not another broad causal-coding claim.
It is a constructed-control validation of the commutator/locality estimators,
followed by a matched intervention showing that reducing those quantities
predicts reduced forgetting without eliminating plasticity.

## Quotations or excerpts

Central hypothesis, summarized rather than quoted: causal factorization should
make context-conditioned updates approximately commute, so sequential learning
approaches a suitable joint-training reference.

## Follow-up questions

1. Can the smooth theorem be restated with `C1` control and an explicit
   cross-loss retention condition?
2. Should Theorem 2 require disjoint supports, bounded overlap commutators, or
   the pairwise confusion-cost premise from Appendix A?
3. What is the exact joint-update operator in the discrete/categorical setting,
   and how is its old-context loss controlled?
4. On RelaLeap fixtures, does experimentally reducing finite-update
   commutators causally reduce forgetting at matched Task-B adaptation?
