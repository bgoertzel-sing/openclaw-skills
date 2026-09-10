"""JAX backend (first-class, working; ported from the validated sandbox
`mlp_demo_jax.py`).

The host supplies: a pure gated StepFunction over an opaque state pytree
(params + optimizer moments), a params_of lens, Oracles built from loss
closures, and a BatchPlan. The backbone computes:

  inject     EXACT full-state perturbation: one gated vs one ordinary step
  propagate  exact-D (default): jax.jvp through the ENTIRE step, moments
             included; frozen-D optionally alongside for the probe gate
  project    tau_hat^A/B at each requested horizon via a loss-jvp

The stress-test result that fixed the defaults: at 10x learning rate,
frozen-D collapsed (Spearman ~0.16/-0.05/0.20 at h=5/10/25) while exact-D
held >= 0.997. Exact-D is the default; frozen-D exists for the probe gate
and as a cost fallback that must EARN admission (cosine >= 0.95, magnitude
ratio in [0.5, 2] at >= 50 probe states).
"""
from __future__ import annotations

from typing import Any, Callable, Mapping, Sequence

import numpy as np

try:
    import jax
    import jax.numpy as jnp
    from jax import jvp, tree_util as jtu
    HAVE_JAX = True
except Exception:                                    # pragma: no cover
    HAVE_JAX = False

from .protocols import Action, BackboneTerms, BatchPlan


def oracles_hvp(loss: Callable, params, v):
    """H v for a loss(params) closure, via forward-over-reverse."""
    return jvp(jax.grad(loss), (params,), (v,))[1]


def tree_dot(a, b) -> float:
    return float(sum(jnp.vdot(x, y) for x, y in
                     zip(jtu.tree_leaves(a), jtu.tree_leaves(b))))


class JaxBackbone:
    def __init__(self, step: Callable, params_of: Callable,
                 moments_view: Callable | None = None,
                 lr_for_frozen: float | None = None):
        """step(state, batch, t, gate) -> state, pure. params_of(state) ->
        params pytree. For frozen-D, `moments_view(state) -> D pytree`
        (elementwise preconditioner) and `lr_for_frozen` must be given."""
        self.step = step
        self.params_of = params_of
        self.moments_view = moments_view
        self.lr = lr_for_frozen

    # ---- injection ---------------------------------------------------
    def inject(self, state, batch0, t0, gate_a, gate_o):
        st_g = self.step(state, batch0, t0, gate_a)
        st_o = self.step(state, batch0, t0, gate_o)
        tan = jtu.tree_map(lambda x, y: x - y, st_g, st_o)   # EXACT, full state
        return st_o, tan

    # ---- measurement -------------------------------------------------
    def measure(self, state, t0: int, plan: BatchPlan,
                actions: Sequence[Action], horizons: Sequence[int],
                gate_of: Callable[[Action | None], Mapping[str, float]],
                loss_A: Callable, loss_B: Callable | None = None,
                frozen_d: bool = False,
                loss_B_of_batch: Callable | None = None,
                batched: bool = True,
                decompose: bool = True,
                partition: Mapping[str, Sequence[str]] | None = None,
                ) -> dict[str, dict[int, BackboneTerms]]:
        """Returns {repr(action): {h: BackboneTerms}}.

        batched=True (default): ONE baseline rollout serves all actions;
        per step the update map is linearized once (jax.linearize) and the
        linear map is vmapped over the stacked tangent columns. Injection
        remains per-action (it is exact and costs one plain step each).
        batched=False routes to the reference looped implementation, kept
        for debugging and for the equivalence test.

        decompose=True populates the Lemma-1 one-step terms (first_order,
        drift, self_curv, and — for pair actions, when `partition` maps
        module -> leaf names and params are a Mapping — cross_curv) on
        every horizon's BackboneTerms. These are injection-time,
        decision-time-observable quantities; the identity
        first_order + drift + self_curv == tau^A(h=1) holds exactly for
        quadratic losses and to O(step^3) generally. Costs 1-2 extra HVPs
        of loss_A per action, at injection only.

        The injected theta-perturbation is stashed in
        terms.extras['u_theta'] at the first requested horizon (synergy
        checks consume it).
        """
        if not batched:
            return self._measure_looped(
                state, t0, plan, actions, horizons, gate_of, loss_A,
                loss_B, frozen_d, loss_B_of_batch, decompose, partition)

        gate_o = gate_of(None)
        maxh = max(horizons)

        # --- injection: exact, per action (A+1 plain steps total)
        st_base = self.step(state, plan.batches[0], t0, gate_o)
        tans = [jtu.tree_map(lambda x, y: x - y,
                             self.step(state, plan.batches[0], t0,
                                       gate_of(act)), st_base)
                for act in actions]

        # --- one-step decomposition at the decision state
        decos = self._decompose_all(state, st_base, tans, actions, loss_A,
                                    partition) if decompose \
            else [None] * len(actions)

        # --- stack tangent columns: state-pytree with leading action axis
        tanB = jtu.tree_map(lambda *xs: jnp.stack(xs), *tans)
        tanBf = (jtu.tree_map(lambda *xs: jnp.stack(xs),
                              *[self.params_of(t_) for t_ in tans])
                 if frozen_d else None)

        out: dict[str, dict[int, BackboneTerms]] = {
            repr(a): {} for a in actions}
        st = st_base
        for k in range(1, maxh + 1):
            if k > 1:
                batch, t = plan.batches[k - 1], t0 + k - 1
                fn = lambda s: self.step(s, batch, t, gate_o)
                st_next, lin = jax.linearize(fn, st)     # primal ONCE
                tanB = jax.vmap(lin)(tanB)               # all actions
                if frozen_d:
                    p = self.params_of(st)
                    _, glin = jax.linearize(
                        jax.grad(lambda q: loss_B_of_batch(q, batch)), p)
                    hvpB = jax.vmap(glin)(tanBf)
                    D = self.moments_view(st_next)
                    tanBf = jtu.tree_map(
                        lambda tf, dd, hh: tf - self.lr * dd * hh,
                        tanBf, D, hvpB)
                st = st_next
            if k in horizons:
                p = self.params_of(st)
                _, linA = jax.linearize(loss_A, p)       # linearize ONCE
                dthB = self.params_of(tanB)
                tA = jax.vmap(linA)(dthB)
                tB = None
                if loss_B is not None:
                    _, linB = jax.linearize(loss_B, p)
                    tB = jax.vmap(linB)(dthB)
                tAf = jax.vmap(linA)(tanBf) if frozen_d else None
                for i, act in enumerate(actions):
                    terms = BackboneTerms(
                        action=act, horizon=k, mode="exact_d",
                        tau_hat_A=float(tA[i]),
                        tau_hat_B=None if tB is None else float(tB[i]))
                    if decos[i] is not None:
                        terms.first_order = decos[i]["first_order"]
                        terms.drift = decos[i]["drift"]
                        terms.self_curv = decos[i]["self_curv"]
                        terms.cross_curv = decos[i]["cross_curv"]
                    if frozen_d:
                        terms.extras["tau_hat_A_frozen_d"] = float(tAf[i])
                    if k == min(horizons):
                        terms.extras["u_theta"] = self.params_of(tans[i])
                    out[repr(act)][k] = terms
        return out

    # ---- one-step decomposition (Lemma 1, decision-time observable)
    def _decompose_all(self, state, st_base, tans, actions, loss_A,
                       partition):
        p_t = self.params_of(state)
        delta0 = jtu.tree_map(lambda x, y: x - y,
                              self.params_of(st_base), p_t)
        gA, glinA = jax.linearize(jax.grad(loss_A), p_t)  # H_A v = glinA(v)
        decos = []
        for act, tan in zip(actions, tans):
            u = self.params_of(tan)
            Hu = glinA(u)
            d = {"first_order": tree_dot(gA, u),
                 "drift": tree_dot(delta0, Hu),
                 "self_curv": 0.5 * tree_dot(u, Hu),
                 "cross_curv": None}
            mods = act[0]
            if (partition is not None and len(mods) == 2
                    and isinstance(u, Mapping)):
                m_leaves = set(partition[mods[0]])
                n_leaves = set(partition[mods[1]])
                u_m = {k: (v if k in m_leaves else jnp.zeros_like(v))
                       for k, v in u.items()}
                u_n = {k: (v if k in n_leaves else jnp.zeros_like(v))
                       for k, v in u.items()}
                d["cross_curv"] = tree_dot(u_m, glinA(u_n))
            decos.append(d)
        return decos

    # ---- reference looped implementation (debugging / equivalence test)
    def _measure_looped(self, state, t0, plan, actions, horizons, gate_of,
                        loss_A, loss_B, frozen_d, loss_B_of_batch,
                        decompose=False, partition=None):
        gate_o = gate_of(None)
        out: dict[str, dict[int, BackboneTerms]] = {}
        maxh = max(horizons)
        st_base1 = self.step(state, plan.batches[0], t0, gate_o)
        tans = [jtu.tree_map(lambda x, y: x - y,
                             self.step(state, plan.batches[0], t0,
                                       gate_of(act)), st_base1)
                for act in actions]
        decos = self._decompose_all(state, st_base1, tans, actions, loss_A,
                                    partition) if decompose \
            else [None] * len(actions)
        for i, act in enumerate(actions):
            tan = tans[i]
            u_theta = self.params_of(tan)
            tan_f = jtu.tree_map(jnp.array, u_theta) if frozen_d else None
            st, res = st_base1, {}
            for k in range(1, maxh + 1):
                if k > 1:
                    batch = plan.batches[k - 1]
                    t = t0 + k - 1
                    fn = lambda s: self.step(s, batch, t, gate_o)
                    st_next, tan = jvp(fn, (st,), (tan,))          # exact-D
                    if frozen_d:
                        # frozen-D: tan_f <- tan_f - lr * D_k * HVP_B(tan_f)
                        p = self.params_of(st)
                        lossB_b = lambda q: loss_B_of_batch(q, batch)
                        hvp = jvp(jax.grad(lossB_b), (p,), (tan_f,))[1]
                        D = self.moments_view(st_next)
                        tan_f = jtu.tree_map(
                            lambda tf, dd, hh: tf - self.lr * dd * hh,
                            tan_f, D, hvp)
                    st = st_next
                if k in horizons:
                    p = self.params_of(st)
                    dt = self.params_of(tan)
                    tA = jvp(loss_A, (p,), (dt,))[1]
                    tB = (jvp(loss_B, (p,), (dt,))[1]
                          if loss_B is not None else None)
                    terms = BackboneTerms(
                        action=act, horizon=k, mode="exact_d",
                        tau_hat_A=float(tA),
                        tau_hat_B=None if tB is None else float(tB))
                    if decos[i] is not None:
                        terms.first_order = decos[i]["first_order"]
                        terms.drift = decos[i]["drift"]
                        terms.self_curv = decos[i]["self_curv"]
                        terms.cross_curv = decos[i]["cross_curv"]
                    if frozen_d:
                        terms.extras["tau_hat_A_frozen_d"] = float(
                            jvp(loss_A, (p,), (tan_f,))[1])
                    if k == min(horizons):
                        terms.extras["u_theta"] = u_theta
                    res[k] = terms
            out[repr(act)] = res
        return out

    # ---- synergy -----------------------------------------------------
    @staticmethod
    def synergy_hat(u_m, u_n, hvp_A: Callable) -> float:
        """u_m' H_A u_n — the exact one-step pair-minus-singles identity;
        one HVP and one dot product."""
        return tree_dot(u_m, hvp_A(u_n))


# ---------------------------------------------------------------------
# reference pure Adam step (a host-code template; hosts may bring optax)
# ---------------------------------------------------------------------

def make_adam_step(loss_of_batch: Callable, lr: float, b1=0.9, b2=0.999,
                   eps=1e-8):
    """loss_of_batch(params, batch) -> scalar. State = (params, m, v).
    Gate is a {leaf: scalar} dict applied post-backward (requirement R3)."""

    def step(state, batch, t, gate):
        p, m, v = state
        g = jax.grad(lambda q: loss_of_batch(q, batch))(p)
        g = {k: gate[k] * g[k] for k in g}
        m2 = jtu.tree_map(lambda a, b: b1 * a + (1 - b1) * b, m, g)
        v2 = jtu.tree_map(lambda a, b: b2 * a + (1 - b2) * b * b, v, g)
        bc1, bc2 = 1 - b1 ** t, 1 - b2 ** t
        p2 = jtu.tree_map(
            lambda pp, mm, vv: pp - lr * (mm / bc1)
            / (jnp.sqrt(vv / bc2) + eps), p, m2, v2)
        return (p2, m2, v2)

    def params_of(state):
        return state[0]

    def moments_view(state, t_hint=None):
        # elementwise D from second moments (bias correction folded coarsely;
        # frozen-D is an approximation by definition — validate at probes)
        _, _, v = state
        return jtu.tree_map(lambda vv: 1.0 / (jnp.sqrt(vv) + eps), v)

    return step, params_of, moments_view
