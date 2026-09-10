# Commutator-critic sandbox

Toy-scale, self-contained validation of the mechanisms in the RelaLeap V4
proposal (*The Commutator Critic*). Two scripts, no shared code, CPU-only,
~3 min total.

```
pip install numpy jax          # matplotlib optional (one plot)
python3 quadratic_demo.py      # -> results_quadratic.json, quadratic_demo.png
python3 mlp_demo_jax.py        # -> results_mlp.json
```

## quadratic_demo.py  (NumPy, float64; exact ground truth)

Block-quadratic fixture, d=64, M=4 modules, SGD, gated stochastic gradients,
CRN paired rollouts. The backbone touches the fixture only through
decision-time-legal oracles (grad_A, grad_B, hvp_A, hvp_B).

* **D1** CRN rollout == closed-form counterfactual (machine precision) —
  the Stage-C0 self-test.
* **D2** Tangent-propagator backbone vs exact truth, in both validation mode
  (rides the baseline rollout) and decision-time mode (noise-free preview).
* **D3** One-step synergy identity tau(pair)−tau(m)−tau(n) = u_m' H_A u_n,
  with the 5-sigma effect-size precheck applied (the plant had to be
  strengthened once to pass it — deliberately left visible in the design).
* **D4** Provably-aligned null family: first-order alignment >= 0 at every
  state; zero false-beneficials.
* **D5** Geometric action-margin decay along the trajectory and the growth
  of the no-signal fraction — the V3 audit failure, reproduced and
  reinterpreted.
* **D6a** Constructive insufficient-statistics demo: Gauss–Newton-projected
  states with feature vectors identical to 1e-10 whose exact tau at h=10
  differs and sign-flips, while tau at h=1 provably coincides.
* **D6b** Cross-instance regressor ceiling: ridge/kNN on V2-style features
  vs the backbone, trained on 4 fixture instances and tested on a 5th at
  h=50 with wide spectra (horizon reweighting dominant).

## mlp_demo_jax.py  (JAX, float64; real nonlinear learner)

8→32→32→4 tanh MLP, 3 modules (layer1/layer2/head), pretrained on task A,
adapted with Adam to a conflicting task B; truth = CRN paired rollouts.
Backbone = EXACT injected perturbation of the full (theta, m, v) Adam state,
propagated by forward-mode jax.jvp through the entire Adam update (exact-D),
plus the frozen-D approximation (tangent <- tangent − lr·D_k·HVP_B).
Families: B1 input-permutation (layer-1 conflict), B2 output-shift (head
conflict), B1_stress at 10x learning rate.

See RESULTS.md for the numbers from the checked-in run.
