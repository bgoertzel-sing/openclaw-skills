# Source: ePC: Fast and Deep Predictive Coding in Digital Simulation

- Type: paper plus official reference repository
- Authors: Cédric Goemaere, Gaspard Oliviers, Rafal Bogacz, Thomas Demeester
- Version/date: arXiv v5, 2026-06-08; accepted ICML 2026
- Retrieved: 2026-08-05
- Canonical identifier: arXiv:2505.20137v5
- Canonical URL: https://arxiv.org/abs/2505.20137v5
- Paper path: `paper-v5.pdf`
- Paper SHA-256: `2decd981f8fb4e24bfbcaea649f278703f60edd9e1f20041a342a3f70bb3142d`
- Extracted text: `paper-v5.txt`
- Text SHA-256: `708de190da03ad4ba560cc541ce2ea2f9e35e589c8e6179648f2b17a2f0aec68`
- Official code: https://github.com/cgoemaere/error_based_PC
- Pinned code commit: `95c555197699f6b4d15452451da15049946b49ca`
- License/access: paper copyright per ICML/PMLR notice; repository MIT (`LICENSE.txt`)
- Privacy tier: public
- Tags: predictive coding, ePC, sPC, error optimization, state optimization
- Related project: `projects/relaleap`

## Summary

The paper identifies exponential signal attenuation in digitally simulated
state-based predictive coding (sPC) and introduces error-based predictive
coding (ePC), a bijective reparameterization that optimizes layerwise errors
directly. Errors reconstruct states sequentially, letting reverse-mode AD
carry the output-loss signal to every error variable on each inference step.
At fixed weights and input, the state/error mapping is triangular and
invertible, so corresponding energies and critical points agree, while the
optimization trajectories and conditioning differ.

The official implementation in `reference-code/pc_e.py` freezes weights,
creates trainable zero error tensors, reconstructs states as prediction plus
error, and runs SGD on the errors using a global energy graph. It then rebuilds
a detached state graph for local parameter updates. `pc_variants.py` exposes
the historical names `EO` (ePC), `SO` (sPC), and `BP`.

## Important claims and limits

- ePC and fully converged sPC share equilibria but may follow different paths
  and, in nonconvex systems, can in principle reach different minima.
- sPC's local state dynamics propagate output signal layer by layer and can
  leave deep layers effectively untrained under finite iteration budgets.
- ePC can reduce to a scaled backpropagation update at one inference step or
  when error learning rate times step count is sufficiently small.
- The paper evaluates supervised image models, not transformers or
  cap-readiness; it claims faster PC simulation and BP-competitive benchmark
  performance, not general superiority to backpropagation.

## Evidence locations

- Main algorithms: paper Figure 4 and Appendix A (PDF pp. 6, 13--14).
- Equivalence and caveats: Appendix C.2 (PDF pp. 19--23).
- Backprop boundary: Appendix C.3 (PDF pp. 24--25).
- Reference error optimization: `reference-code/pc_e.py`, methods `E`,
  `minimize_error_energy`, `init_zero_errors`, and `E_local`.
- Analytic deep-linear solver: `reference-code/mnist_poc/analytical_solution.py`.

## Relevance

RelaLeap's legacy transformer routine differentiates energy with respect to
detached hidden states and steps those states. It therefore implements the
paper's `SO`/sPC parameterization, not the reference `EO`/ePC computation.
The paper and reference code provide the primary basis for A0 method identity
and the later port-and-reproduce obligation.

