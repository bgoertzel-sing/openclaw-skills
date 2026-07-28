# Source: The Commutator Critic, v1.1

- Type: `PDF + source-code/archive bundle`
- Authors/organization: Ben Goertzel; draft acknowledges Claude Fable 5
- Publication/version date: `July 2026, v1.1`
- Retrieved: `2026-07-27`
- Canonical URL or identifier: supplied directly by Ben in the Protobots Telegram group
- Local source path: `originals/` (PDF and three ZIP archives); searchable PDF text at
  `commutator_critic_v1_1.txt`; unpacked bundle at `extracted/`
- SHA-256: see `SHA256SUMS`
- License/access constraints: no license supplied; preserve locally and do not redistribute
- Privacy tier: `local-private`
- Tags: `RelaLeap`, `continual learning`, `commutator`, `counterfactual critic`,
  `linear response`, `HVP`, `JAX`, `PyTorch`, `CAROM`, `HDC`, `CGCCT`
- Related projects: `relaleap`, `hdc-cgcct-transformers`, `carom`

## Summary

The proposal replaces the V1--V3 black-box causal critic with a grey-box
measurement backbone. It computes the counterfactual effect of attenuating a
module's incoming-task gradient from the exact injected optimizer-state
perturbation, local gradient/curvature terms, and a tangent propagated through
the common-random-number baseline rollout. A small learned head is permitted
only for the residual. The package includes a PDF, checked-in toy results,
NumPy/JAX demos, a standalone `comcrit` skeleton, and a v0.1.1 patch bundle.

## Key claims or contents

- The V2 feature map is not sufficient for the horizon-dependent estimand
  because it discards curvature-weighted coordinate information (PDF Sections
  3--4; sandbox D6).
- Fixed family orderings are not trajectory invariant; intervention margins
  decay as the incoming gradient contracts (PDF Proposition 2; sandbox D5).
- The exact-D tangent must include optimizer moments under Adam; the supplied
  JAX run reports near-perfect rank agreement while frozen-D collapses in the
  high-learning-rate stress family (PDF Sections 3.2, 3.5, 10.3).
- Pair-action non-additivity is a cross-curvature term
  `u_m^T H_A u_n` at one step (PDF Lemma 2; sandbox D3).
- C0--C3 are proposed as local CPU gates, C4 as the first GPU gate, and all
  downstream policy claims remain contingent (PDF Appendix A).

## Methods or implementation details

- `extracted/quadratic_demo.py`: NumPy float64 block-quadratic fixture with
  closed-form counterfactual truth.
- `extracted/mlp_demo_jax.py`: nonlinear MLP/Adam sandbox using full-state JAX
  forward-mode propagation.
- `extracted/comcrit_v0.1.1.tar.gz`: standalone package containing the patched
  JAX backbone, quadratic fixture, PyTorch optimizer replicas, tests, and
  acceptance notes.
- The related audit ledger is
  `../../projects/relaleap/experiments/20260727T080552Z-commutator-critic-v1-1-audit/`.

## Limitations and uncertainties

- External citations in the manuscript are explicitly memory-recalled and
  require verification.
- The checked-in sandbox is toy-scale; it does not establish validity on the
  existing RelaLeap learner, a Transformer, CAROM, or a policy.
- JAX was not installed in the base workspace at ingestion time. Any JAX/Adam
  reproduction remains pending unless a reviewed isolated dependency setup is
  created.
- The manuscript's cost estimates for batched JVP/HVP propagation need measured
  profiling on the intended learner.
- The supplied package has no canonical repository history or license.
- Local audit on Torch 2.12.1 found `5 passed, 4 failed, 1 skipped`; all four
  failures were the package's own bit-exact functional optimizer-replica gate.
  See the linked experiment record. Therefore the Torch backend is not
  admitted on this host.

## Relevance to current work

This is a direct, structurally motivated successor to RelaLeap V1--V3. It also
offers a concrete measurement instrument for the CGCCT confusion graph and
commutator loss, while HDC footprints are proposed only as a sparse pair-edge
proposal mechanism rather than as evidence of causal interaction.

## Quotations or excerpts

No quotation is required; use the local PDF and extracted text for exact wording.

## Follow-up questions

- Does the packaged quadratic run reproduce exactly in the current environment?
- Do the patched package tests pass, especially the PyTorch optimizer-replica
  admission gate?
- Is a reviewed isolated JAX environment justified to reproduce the nonlinear
  exact-D claims before integrating anything into RelaLeap?
- Which proposal claims are identities, which are Taylor approximations, and
  which depend on future empirical validity-radius gates?
