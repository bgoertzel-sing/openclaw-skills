# Source: The Causal Memory and Credit Protocol

- Type: `PDF`
- Authors/organization: Ben Goertzel
- Publication/version date: Working draft, July 2026
- Retrieved: `2026-07-24`
- Canonical URL or identifier: User-supplied Telegram document; no public canonical URL recorded
- Local source path: `library/causal-memory-credit-protocol-2026/source.pdf`
- Extracted text: `library/causal-memory-credit-protocol-2026/source.txt`
- SHA-256: `a053f55c98d53f7d44de42b6d63f7954dbd26f7b0c51cc3325bc88912443f181`
- License/access constraints: Author-supplied working draft; do not publish without author direction
- Privacy tier: `local-private`
- Tags: causal memory, credit assignment, continual learning, information geometry, Fisher information, conditional information, holonomy, modular learning, evidence accounting
- Related projects: `causal-fibres-ladder`, `carom`, `omegaclaw`, `hyperseed-formalizations`

## Summary

CMCP proposes a protocol layer for adaptive systems that separates:

1. computational reuse of persistent shared mechanisms;
2. causal assignment and sparse transport of credit;
3. geometric alignment of a mechanism across representational frames; and
4. statistical assimilation of genuinely new evidence.

The architecture has three planes: a representation/data plane, a credit
plane, and an evidence-ledger/write plane. Shared mechanisms are read-many but
write-gated. A credit-only highway addresses long-range credit starvation
without becoming another forward dependency. An evidence ledger decides
whether a signal is redundant, independent new evidence about an existing
mechanism, a local exception, a new mechanism, or mechanism drift.

The central technical refinement is that novelty has two components.
Directional novelty detects new mechanism directions, while conditional
information distinguishes exact or correlated duplicates from independent
new observations in an already-known direction. The proposed local estimator
is the Schur complement of stored and incoming score covariances.

## Key claims or contents

- Broadly readable shared knowledge must be narrowly writable, while globally
  observable error must remain locally actionable (pp. 2, 5--7).
- Mechanism identity should be defined up to a metric-preserving coordinate
  transform using tuples of local information operators, not raw parameter or
  activation similarity (pp. 8--9).
- Trace-word fingerprints provide coordinate-invariant retrieval keys;
  approximate operator intertwiners provide transport maps (pp. 8--9).
- Symmetric information geometry records contraction and precision, while
  antisymmetric commutators and holonomy record order-dependent re-encoding
  and interference (pp. 9--11).
- Projection onto the complement of a stored mechanism subspace is not a valid
  evidence-novelty test: independent repeated evidence may lie in the same
  direction and should still increase precision (pp. 11--13).
- Conditional score residualization using
  `F_c|M = F_cc - F_cM F_MM^† F_Mc` suppresses exact duplicates and predictable
  descendants while retaining independent repeated evidence (pp. 11--12).
- “Exactly once” applies per causal innovation, not per sample presentation
  (p. 13).
- The protocol exposes testable contracts for causal idempotence,
  independent-evidence accumulation, commutation of independent mechanisms,
  coordinate equivariance, path consistency, write provenance, and bounded
  interference (pp. 15--16).
- The proposed synthetic benchmark contains eleven ground-truth regimes,
  including duplicates, descendants, independent repeats, rotated
  representations, orthogonal mechanisms, local exceptions, new mechanisms,
  drift, regime change, nuisance correlations, and adversarial writes
  (p. 23).

## Methods or implementation details

- Memory records contain mechanism state, information subspace, accumulated
  precision, invariant fingerprint, provenance, and lifecycle/version state.
- A credit encoder factorizes discrepancy; a geometric matcher retrieves and
  aligns candidate mechanisms; an intervention-sensitive responsibility
  router gates writes; a sparse credit-only highway delivers approved
  innovation packets.
- Shared writes use two-stage commitment: provisional assimilation followed by
  promotion after recurrence, intervention, transport, and interference tests.
- Geometry may use Fisher, generalized Gauss--Newton, empirical Fisher,
  Hessian, Jacobian Gram, controllability, or linearized-dynamics operators.
- Matrix-free Hessian/vector products, nested commutator actions, Hutchinson
  trace estimates, and low-rank/block metrics are proposed for scale.
- The paper specifies a coarse-to-fine retrieval path: semantic shortlist,
  low-degree geometric filter, then local alignment.
- The eight-arm factorial experiment isolates memory, raw versus causal
  highways, semantic versus geometric matching, conditional information, and
  intervention responsibility (pp. 23--24).

## Limitations and uncertainties

- Second-order signatures are local and can fail to distinguish mechanisms
  that diverge at higher order (p. 25).
- Geometry identifies shared sensitivity but cannot establish causal
  direction without intervention or credible invariance evidence (p. 25).
- The conditional-Fisher Schur complement captures linear conditional
  predictability; nonlinear redundancy can remain and stored summaries may
  discard dependence information (p. 25).
- Symmetric/interchangeable modules create non-identifiable ownership and
  unstable transports (p. 25).
- Write gating risks memory ossification; drift requires reversible versioning
  and adaptive thresholds (p. 25).
- Responsibility routing can become self-confirming without randomized,
  held-out intervention tests (p. 25).
- Curvature sketches, probes, and provenance impose compute, storage, and
  privacy costs (p. 25).
- Intervention-useful modules need not correspond to unique ontological
  causes (p. 25).

## Relevance to current work

- `causal-fibres-ladder`: the sparse, mechanism-indexed credit highway and
  transport geometry are natural downstream consumers of ePC frontier/fibre
  diagnostics, but CMCP adds a separate evidence-multiplicity ledger not yet
  tested by ePC.
- `carom`: trajectory/controller work concerns how credit and computation are
  routed; CMCP suggests separating controller reuse from permission to
  assimilate evidence into shared operator mechanisms.
- `omegaclaw`: agent memory currently needs exactly the read-versus-write and
  duplicate-versus-independent-evidence distinctions formalized here.
- `hyperseed-formalizations`: the protocol contracts and negative-result
  branches are suitable for an evidence-gated formalization after empirical
  estimator validation.

The smallest decisive prototype should focus on the evidence ledger before
the complete geometric stack: use a known linear-Gaussian or exponential-family
mechanism, construct exact duplicates, deterministic descendants, independent
repeats, partial redundancy, and rotated coordinates, and compare directional
projection against the Schur-complement conditional-information rule. This
directly tests the paper's distinctive claim without conflating it with causal
routing or approximate Hessian transport.

## Quotations or excerpts

> Shared knowledge should be broadly readable but narrowly writable; error
> should be globally observable but locally actionable.

> Each causally distinct innovation should contribute once to the shared
> evidence ledger, while each conditionally independent measurement may
> contribute its own information.

## Follow-up questions

1. Does the Schur-complement estimator remain calibrated under finite samples,
   rank deficiency, nonlinear descendants, and approximate stored summaries?
2. What minimal sufficient-statistic/provenance representation makes duplicate
   idempotence possible without retaining raw private observations?
3. Can operator alignment and conditional-information accounting be validated
   independently before combining them?
4. Which responsibility intervention gives a clean positive control without
   making routing trivial?
5. Should CMCP become a standalone project, or first enter as a bounded
   evidence-ledger experiment linked to causal-fibres?
