# PATCHES.md — tangent-column batching + Lemma-1 term decomposition

For the coding agents integrating into `comcrit` (or `relaleap.critic`).
Two patches, shipped as unified diffs against v0.1.0 plus a new acceptance
test file. Both were applied and verified in a live environment before
shipping: **13 passed, 1 skipped** (torch gate, no torch installed),
`selftest()` PASSED, `examples/mlp_jax_example.py` numerically unchanged
(exact-D Spearman 1.0000 / 0.9999 / 0.9997 at h = 1/5/10).

```
patches/0001-tangent-column-batching-and-term-decomposition.diff   -> src/comcrit/backbone_jax.py
patches/0002-fixture-decompose-onestep.diff                        -> src/comcrit/fixture_quadratic.py
tests/test_patches.py                                              -> new file (the acceptance gate)
```

Integration order: apply 0002, then 0001, then add the test file, then run
the acceptance checklist at the bottom. Nothing else in the tree changes;
`protocols.py` already carried the `BackboneTerms` fields these patches
populate (that was deliberate — the contract predates the implementation).

---

## Patch 1 — tangent-column batching in `JaxBackbone.measure`

### What changes

`measure()` keeps its exact signature and return type, and gains three
keyword arguments:

```python
batched: bool = True          # new default path
decompose: bool = True        # Patch 2 (below)
partition: Mapping[str, Sequence[str]] | None = None   # Patch 2
```

The old per-action loop survives verbatim as `_measure_looped()` — it is
the reference implementation, the debugging path, and one side of the
equivalence test. Do not delete it.

### The design, and why it is shaped this way

The un-batched cost was: per action, one full baseline re-propagation with
one `jvp` per step — i.e. the primal (the baseline step itself) was
recomputed `A` times, and each `jvp` retraced the step function. Three
decisions fix this:

1. **One baseline, `A` tangent columns.** Injection stays *per action*
   (`A + 1` plain gated/ordinary steps — injection is exact by definition
   and each is a single cheap step; there is nothing to batch there and
   batching it would trade exactness for nothing). The resulting full-state
   tangents are then stacked into a single state-pytree whose leaves carry
   a leading action axis:
   `tanB = jtu.tree_map(lambda *xs: jnp.stack(xs), *tans)`.

2. **`jax.linearize` once per step, `vmap` the linear map.** The naive
   batched form — `vmap(lambda t: jvp(fn, (st,), (t,)))` — recomputes the
   primal `A` times inside the vmap and retraces `fn` besides. The correct
   tool is:

   ```python
   st_next, lin = jax.linearize(fn, st)   # primal + linearization ONCE
   tanB = jax.vmap(lin)(tanB)             # A cheap linear applications
   ```

   This is the load-bearing line of the patch. If you refactor, preserve
   the invariant *one linearization per (step, decision-state), never per
   action*. The same trick is applied at projection time
   (`jax.linearize(loss_A, p)` once, `vmap` over the stacked theta-
   tangents) and to the frozen-D HVP
   (`jax.linearize(jax.grad(loss_B_batch), p)` once, `vmap` over the
   frozen tangent columns).

3. **Frozen-D batches identically.** The frozen-D tangent block stacks the
   theta-only tangents the same way; its update
   `tanBf <- tanBf - lr * D_k * HVP_B(tanBf)` uses `D` from the *post-step
   baseline* moments, matching the looped path and the sandbox exactly.
   (Do not "improve" this to pre-step moments; the equivalence test will
   catch you.)

### Measured effect

Un-jitted CPU, 12 actions, h = 10, ~5.7k-parameter MLP: **3.86 s -> 1.28 s
per call (3.0x)**. The ratio grows with the action count (the linearize
cost amortizes across columns) and grows substantially again under `jit`,
which is deliberately NOT applied inside `measure()` — jit placement
belongs to the host loop, where `state`/`plan` shapes are stable across
decision states. First natural follow-up at Transformer scale: wrap the
per-step `linearize`+`vmap` body in a host-jitted function keyed on the
step signature.

### Semantics guaranteed (and tested)

`batched=True` and `batched=False` agree to `rel=1e-9` on every
`tau_hat_A`, every frozen-D value, and every decomposition term, for
single AND pair actions, across horizons (`test_batched_equals_looped`).
Any future edit to either path must keep this test green — the two paths
are each other's oracle.

---

## Patch 2 — Lemma-1 term decomposition (`first_order`, `drift`,
`self_curv`, `cross_curv`)

### What changes

Two implementations of the same mathematics, one per substrate:

- `QuadFixture.decompose_onestep(th, action, noise0)` (NumPy fixture) —
  where the identity is *exact* and therefore testable at 1e-10;
- `JaxBackbone._decompose_all(...)` — called from `measure()` when
  `decompose=True`, populating the previously-`None` fields of
  `BackboneTerms` on **every** horizon's object.

### The mathematics being implemented (sign conventions matter)

With `u = theta_gated(t+1) - theta_ordinary(t+1)` (the exact injected
perturbation; note the sign — the gated arm subtracts *less* of the
incoming gradient, so it sits at ordinary-plus-`u`) and
`delta0 = theta_ordinary(t+1) - theta_t` (the ordinary step displacement):

```
tau^A(h=1) = <g_A(theta_t), u>            # first_order
           + delta0' H_A u                # drift
           + 1/2 u' H_A u                 # self_curv
           + O(step^3)
```

and for a pair action `{m, n}`:

```
tau(pair) - tau(m) - tau(n) = u_m' H_A u_n        # cross_curv
```

where `u_m`, `u_n` are `u` restricted to each module's leaves. Because
modules are **disjoint leaf sets**, restriction of the *pair's own* `u`
recovers the singles' perturbations exactly — no extra injection steps are
needed for `cross_curv`, only one extra HVP. This disjointness assumption
is real: if a future partition scheme ever shares a leaf between modules,
`cross_curv` must revert to computing the singles' injections explicitly.

### Semantics and placement decisions an integrator must know

1. **The terms are injection-time quantities.** They are properties of
   `(S_t, a)`, not of the horizon; they are copied onto every horizon's
   `BackboneTerms` for consumer convenience (gates and residual features
   index by horizon). Do not recompute them per horizon and do not expect
   `first_order` at h = 10 to be `<g_A(theta_{t+10}), Phi u>` — that
   quantity is `tau_hat_A` itself.

2. **Relationships you can (and the tests do) rely on:**
   - quadratic fixture: `first_order + drift + self_curv == tau_exact(h=1)`
     to 1e-10 (`test_decompose_onestep_exact_on_quadratic`);
   - real MLP: same sum approximates the *true paired* `tau^A(h=1)` to
     ~15% relative on non-degenerate actions
     (`test_terms_populated_and_onestep_identity`) — this is the
     O(step^3) remainder plus minibatch curvature, i.e. exactly the
     residual head's food;
   - `cross_curv` on the pair equals
     `JaxBackbone.synergy_hat(u_m, u_n, hvp_A)` computed from the singles'
     stashed `u_theta` to 1e-9 (`test_pair_cross_curv_matches_synergy`),
     and equals `QuadFixture.synergy_hat` at h = 1 on the fixture.

3. **Cost accounting.** One `jax.linearize(jax.grad(loss_A), p_t)` per
   decision state (shared across all actions — this also supplies `g_A`
   for free as the linearization point value), then one HVP application
   per action plus one more per pair action. At injection only; nothing is
   added to the propagation loop.

4. **`cross_curv` prerequisites.** Params must be a `Mapping` (leaf-name
   dict) and `partition` (module -> leaf names; `ModulePartition.modules`
   works directly) must be passed. When either is absent the field stays
   `None` — per the `BackboneTerms` contract, unpopulated means `None`,
   never silent zero. Consumers must treat `None` as "not measured", not
   as "no synergy".

5. **`drift` uses the *ordinary* step's displacement** (`delta0` from the
   already-computed `st_base`), not the gated one. This matches Lemma 1;
   swapping arms changes the term at second order and will fail the
   fixture exactness test.

### Downstream consumers to wire next (not in this patch)

- `gates.ValidityGate` reporting can now break error down by term;
- residual-head features consume the four terms directly (they were
  designed as the feature vector's backbone block);
- `ConfusionGraph.add_cross_curvature` can be fed from pair-action
  `cross_curv` instead of recomputing via `synergy_hat` (the example still
  recomputes — updating it is optional and equivalent by the test above).

---

## Acceptance checklist (run all; all must pass)

```
python -m pytest -q tests/                 # expect 13 passed, 1 skipped (torch)
python -c "import comcrit; assert comcrit.selftest(verbose=False)['passed']"
python examples/mlp_jax_example.py         # Spearman unchanged: 1.0000/0.9999/0.9997
```

Plus the benchmark sanity: `batched=True` must beat `batched=False` by
>= 2x at 12 actions, h = 10, at example scale. If it does not, the
linearize-once invariant has been broken somewhere.

## Known deferred items (unchanged by these patches)

Preview-mode `measure` on the JAX path (fixture has it; backbone gains it
with the C2 comparison arm); jit placement at the host loop; torch backend
still gated on `test_torch_exactness.py` running on a torch install; the
`drift`/`self_curv` analogues for the *frozen-D* tangent are intentionally
not computed (frozen-D is a probe-gated fallback, not a first-class mode).
