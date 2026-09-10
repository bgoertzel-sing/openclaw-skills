"""Acceptance tests for Patch 1 (tangent-column batching) and Patch 2
(Lemma-1 term decomposition). These are the integration gates: all must
pass before either patch is merged."""
import numpy as np
import pytest

from comcrit import fixture_quadratic as fq


# ---------------------------------------------------------------------
# Patch 2, numpy path: the identity is EXACT on quadratics
# ---------------------------------------------------------------------

@pytest.mark.parametrize("fam", ["null", "local", "chain", "synergy"])
def test_decompose_onestep_exact_on_quadratic(fam):
    fx = fq.make_family(fam, seed=1)
    states = fq.gen_states(fx, n_steps=40, every=8)
    acts = [(["m0"], 0.1), (["m2"], 0.5), (["m2", "m3"], 0.1)]
    for (_, th, cs) in states:
        nz = fq.noise_for(fx, cs, 1)
        for act in acts:
            d = fx.decompose_onestep(th, act, nz[0])
            t1 = fx.tau_exact(th, act, 1, nz)
            assert abs(d["total_onestep"] - t1) <= 1e-10 * max(abs(t1), 1e-12)


def test_decompose_cross_curv_equals_synergy_hat():
    fx = fq.make_family("synergy", seed=1)
    (_, th, cs) = fq.gen_states(fx, n_steps=20, every=4)[1]
    nz0 = fq.noise_for(fx, cs, 1)[0]
    d = fx.decompose_onestep(th, (["m2", "m3"], 0.1), nz0)
    assert d["cross_curv"] == pytest.approx(
        fx.synergy_hat(th, "m2", "m3", 0.1, 1, nz0), rel=1e-12)


# ---------------------------------------------------------------------
# Patch 1 + 2, jax path
# ---------------------------------------------------------------------

jax = pytest.importorskip("jax")


@pytest.fixture(scope="module")
def mini():
    import jax.numpy as jnp
    jax.config.update("jax_enable_x64", True)
    from comcrit.backbone_jax import JaxBackbone, make_adam_step
    from comcrit.protocols import BatchPlan

    key = jax.random.PRNGKey(3)
    k1, k2, k3 = jax.random.split(key, 3)
    p0 = {"W1": jax.random.normal(k1, (6, 12)) / jnp.sqrt(6.0),
          "b1": jnp.zeros(12),
          "W2": jax.random.normal(k2, (12, 3)) / jnp.sqrt(12.0),
          "b2": jnp.zeros(3)}
    mlp = lambda p, x: jnp.tanh(x @ p["W1"] + p["b1"]) @ p["W2"] + p["b2"]
    X = np.array(jax.random.normal(k3, (512, 6)))
    YA = np.array(mlp(p0, X))
    YB = np.array(mlp(p0, X[:, ::-1].copy()))
    mse = lambda p, Xb, Yb: jnp.mean((mlp(p, Xb) - Yb) ** 2)
    step, params_of, moments_view = make_adam_step(
        lambda p, b: mse(p, b[0], b[1]), lr=1e-3)
    rng = np.random.default_rng(0)
    batch = lambda Y: (lambda i: (jnp.array(X[i]), jnp.array(Y[i])))(
        rng.integers(0, 512, 32))
    st = ({k: 0.6 * v for k, v in p0.items()},
          {k: jnp.zeros_like(v) for k, v in p0.items()},
          {k: jnp.zeros_like(v) for k, v in p0.items()})
    for t in range(1, 101):
        st = step(st, batch(YA), t, {k: 1.0 for k in p0})
    plan = BatchPlan(batches=[batch(YB) for _ in range(6)])
    modules = {"layer1": ["W1", "b1"], "head": ["W2", "b2"]}

    def gate_of(act):
        g = {k: 1.0 for k in p0}
        if act is not None:
            for m in act[0]:
                for lf in modules[m]:
                    g[lf] = act[1]
        return g

    loss_A = lambda p: mse(p, jnp.array(X[:256]), jnp.array(YA[:256]))
    bbone = JaxBackbone(step, params_of, moments_view, lr_for_frozen=1e-3)
    acts = [(["layer1"], 0.1), (["head"], 0.1), (["layer1"], 0.5),
            (["layer1", "head"], 0.1)]
    return dict(bbone=bbone, st=st, plan=plan, gate_of=gate_of,
                loss_A=loss_A, acts=acts, step=step, modules=modules,
                lossB_b=lambda p, b: mse(p, b[0], b[1]),
                params_of=params_of, mse=mse, X=X, YA=YA)


def test_batched_equals_looped(mini):
    kw = dict(gate_of=mini["gate_of"], loss_A=mini["loss_A"],
              frozen_d=True, loss_B_of_batch=mini["lossB_b"],
              partition=mini["modules"])
    rb = mini["bbone"].measure(mini["st"], 100, mini["plan"], mini["acts"],
                               [1, 3, 6], batched=True, **kw)
    rl = mini["bbone"].measure(mini["st"], 100, mini["plan"], mini["acts"],
                               [1, 3, 6], batched=False, **kw)
    for a in rb:
        for h in rb[a]:
            tb, tl = rb[a][h], rl[a][h]
            assert tb.tau_hat_A == pytest.approx(tl.tau_hat_A, rel=1e-9,
                                                 abs=1e-15)
            assert tb.extras["tau_hat_A_frozen_d"] == pytest.approx(
                tl.extras["tau_hat_A_frozen_d"], rel=1e-9, abs=1e-15)
            for f in ("first_order", "drift", "self_curv"):
                assert getattr(tb, f) == pytest.approx(
                    getattr(tl, f), rel=1e-9, abs=1e-18)


def test_terms_populated_and_onestep_identity(mini):
    """first_order + drift + self_curv must approximate the TRUE paired
    tau^A(h=1) on a real nonlinear learner (O(step^3) identity — tolerance
    is loose but meaningful: 15% relative on the dominant actions)."""
    res = mini["bbone"].measure(mini["st"], 100, mini["plan"], mini["acts"],
                                [1], gate_of=mini["gate_of"],
                                loss_A=mini["loss_A"],
                                partition=mini["modules"])
    step, gate_of, plan = mini["step"], mini["gate_of"], mini["plan"]
    base = step(mini["st"], plan.batches[0], 100, gate_of(None))
    for act in mini["acts"]:
        ga = step(mini["st"], plan.batches[0], 100, gate_of(act))
        t_true = float(mini["loss_A"](mini["params_of"](ga))
                       - mini["loss_A"](mini["params_of"](base)))
        terms = res[repr(act)][1]
        assert terms.first_order is not None
        pred2 = terms.first_order + terms.drift + terms.self_curv
        if abs(t_true) > 1e-10:
            assert pred2 == pytest.approx(t_true, rel=0.15)
    pair_terms = res[repr((["layer1", "head"], 0.1))][1]
    assert pair_terms.cross_curv is not None


def test_pair_cross_curv_matches_synergy(mini):
    """cross_curv on the pair action must equal u_m' H_A u_n computed from
    the singles' injected perturbations (the synergy identity plumbing)."""
    from comcrit.backbone_jax import JaxBackbone, oracles_hvp
    res = mini["bbone"].measure(mini["st"], 100, mini["plan"], mini["acts"],
                                [1], gate_of=mini["gate_of"],
                                loss_A=mini["loss_A"],
                                partition=mini["modules"])
    um = res[repr((["layer1"], 0.1))][1].extras["u_theta"]
    un = res[repr((["head"], 0.1))][1].extras["u_theta"]
    p_t = mini["params_of"](mini["st"])
    syn = JaxBackbone.synergy_hat(
        um, un, lambda v: oracles_hvp(mini["loss_A"], p_t, v))
    cc = res[repr((["layer1", "head"], 0.1))][1].cross_curv
    assert cc == pytest.approx(syn, rel=1e-9, abs=1e-18)
