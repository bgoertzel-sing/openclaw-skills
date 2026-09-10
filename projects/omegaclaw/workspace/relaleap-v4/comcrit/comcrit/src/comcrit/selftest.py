"""comcrit.selftest(): the library's positive control, runnable anywhere.

A failing selftest means the INSTALL, not the science, is broken — the same
inversion the quadratic fixture performs for the research programme. Checks
(numpy path, ~30 s CPU):

  T1  CRN paired rollout == closed-form counterfactual   (<= 1e-8 rel.)
  T2  backbone Spearman >= 0.99, median rel err <= 2%    (local family)
  T3  synergy identity exact at h=1; effect-size precheck ratio reported
  T4  null family: analytic nonnegativity at every state; 0 false-benefits
  T5  (if JAX) exact-D backbone Spearman >= 0.95 at h=5 on a miniature
      MLP+Adam run; frozen-D reported alongside
"""
from __future__ import annotations

import numpy as np

from . import fixture_quadratic as fq
from .stats import margin_qualify, noise_floor, spearman


def _floor(fx, states, h, n_rep=32):
    (_, th, _) = states[len(states) // 3]
    def sampler(seed):
        nz = np.random.default_rng(10_000 + seed).normal(size=(h, fx.d))
        return fx.tau_rollout(th, (["m0"], 0.1), h, nz)
    return noise_floor(sampler, n_rep)


def selftest(verbose: bool = True) -> dict:
    rep: dict = {}
    ok = True
    log = print if verbose else (lambda *a, **k: None)

    # ---- T1/T2: local family
    fx = fq.make_family("local", seed=1)
    states = fq.gen_states(fx, n_steps=160, every=8)
    acts = [([f"m{i}"], a) for i in range(4) for a in (0.5, 0.1)]
    fl = _floor(fx, states, h=10)
    d1, tr, bb = [], [], []
    for (_, th, cs) in states:
        nz = fq.noise_for(fx, cs, 10)
        for act in acts:
            t_roll = fx.tau_rollout(th, act, 10, nz)
            t_ex = fx.tau_exact(th, act, 10, nz)
            d1.append(abs(t_roll - t_ex) / max(abs(t_ex), 1e-300))
            tr.append(t_roll)
            bb.append(fx.backbone_validation(th, act, 10, nz))
    tr, bb = np.array(tr), np.array(bb)
    q = margin_qualify(tr, fl)
    rep["T1_rollout_vs_closed_form_max_rel_err"] = float(np.max(d1))
    rep["T2_backbone_spearman"] = spearman(bb[q], tr[q])
    rep["T2_backbone_median_rel_err"] = float(np.median(
        np.abs(bb[q] - tr[q]) / np.abs(tr[q])))
    ok &= rep["T1_rollout_vs_closed_form_max_rel_err"] <= 1e-8
    ok &= rep["T2_backbone_spearman"] >= 0.99
    ok &= rep["T2_backbone_median_rel_err"] <= 0.02
    log(f"T1 rollout==closed-form: {rep['T1_rollout_vs_closed_form_max_rel_err']:.2e}")
    log(f"T2 backbone rho={rep['T2_backbone_spearman']:.4f} "
        f"relerr={rep['T2_backbone_median_rel_err']:.4f}")

    # ---- T3: synergy identity on the aligned-plant family
    fs = fq.make_family("synergy", seed=1)
    sst = [s for s in fq.gen_states(fs, n_steps=60, every=4) if s[0] <= 40]
    fl1 = _floor(fs, sst, h=1)
    s_true, s_hat = [], []
    for (_, th, cs) in sst:
        nz = fq.noise_for(fs, cs, 1)
        tp = fs.tau_rollout(th, (["m2", "m3"], 0.1), 1, nz)
        tm = fs.tau_rollout(th, (["m2"], 0.1), 1, nz)
        tn = fs.tau_rollout(th, (["m3"], 0.1), 1, nz)
        s_true.append(tp - tm - tn)
        s_hat.append(fs.synergy_hat(th, "m2", "m3", 0.1, 1, nz[0]))
    s_true, s_hat = np.array(s_true), np.array(s_hat)
    rep["T3_synergy_median_rel_err"] = float(np.median(
        np.abs(s_hat - s_true) / np.abs(s_true)))
    rep["T3_precheck_ratio"] = float(np.median(np.abs(s_true)) / fl1)
    ok &= rep["T3_synergy_median_rel_err"] <= 1e-6
    ok &= rep["T3_precheck_ratio"] >= 5.0
    log(f"T3 synergy relerr={rep['T3_synergy_median_rel_err']:.2e} "
        f"precheck={rep['T3_precheck_ratio']:.1f}x floor")

    # ---- T4: provably-aligned null
    fn = fq.make_family("null", seed=1)
    nst = fq.gen_states(fn, n_steps=120, every=8)
    fl10 = _floor(fn, nst, h=10)
    worst, fb = np.inf, 0
    for (_, th, cs) in nst:
        gA, gB = fn.grad_A(th), fn.grad_B_clean(th)
        for i in range(4):
            idx = fn.part.mask(f"m{i}")
            worst = min(worst, float(gA[idx] @ gB[idx]))
        nz = fq.noise_for(fn, cs, 10)
        for act in acts:
            if fn.tau_rollout(th, act, 10, nz) < -3 * fl10:
                fb += 1
    rep["T4_min_firstorder_alignment"] = worst
    rep["T4_false_beneficials"] = fb
    ok &= worst >= 0.0 and fb == 0
    log(f"T4 null min-align={worst:.3e} false-benefits={fb}")

    # ---- T5: miniature JAX MLP (optional)
    try:
        rep["T5"] = _jax_minicheck()
        ok &= rep["T5"]["spearman_exact_d_h5"] >= 0.95
        log(f"T5 jax exact-D rho(h=5)={rep['T5']['spearman_exact_d_h5']:.4f} "
            f"frozen-D={rep['T5']['spearman_frozen_d_h5']:.4f}")
    except ImportError:
        rep["T5"] = "skipped (jax not installed)"
        log("T5 skipped (no jax)")

    rep["passed"] = bool(ok)
    log(f"selftest {'PASSED' if ok else 'FAILED'}")
    return rep


def _jax_minicheck() -> dict:
    import jax
    import jax.numpy as jnp

    jax.config.update("jax_enable_x64", True)
    from .backbone_jax import JaxBackbone, make_adam_step
    from .protocols import BatchPlan

    key = jax.random.PRNGKey(0)
    k1, k2, k3 = jax.random.split(key, 3)
    W = {"W1": jax.random.normal(k1, (6, 16)) / jnp.sqrt(6.0),
         "b1": jnp.zeros(16),
         "W2": jax.random.normal(k2, (16, 3)) / jnp.sqrt(16.0),
         "b2": jnp.zeros(3)}
    mlp = lambda p, x: jnp.tanh(x @ p["W1"] + p["b1"]) @ p["W2"] + p["b2"]
    teacher = {k: v for k, v in W.items()}
    X = np.array(jax.random.normal(k3, (1024, 6)))
    YA = np.array(mlp(teacher, X))
    YB = np.array(mlp(teacher, X[:, ::-1].copy()))       # input-perm conflict
    mse = lambda p, Xb, Yb: jnp.mean((mlp(p, Xb) - Yb) ** 2)
    step, params_of, moments_view = make_adam_step(
        lambda p, b: mse(p, b[0], b[1]), lr=1e-3)

    rng = np.random.default_rng(0)
    batch = lambda Y: (lambda i: (jnp.array(X[i]), jnp.array(Y[i])))(
        rng.integers(0, 1024, 32))
    p0 = {k: 0.5 * v for k, v in W.items()}
    state = (p0, {k: jnp.zeros_like(v) for k, v in p0.items()},
             {k: jnp.zeros_like(v) for k, v in p0.items()})
    for t in range(1, 201):                              # pretrain on A
        state = step(state, batch(YA), t, {k: 1.0 for k in p0})
    state = (state[0], {k: jnp.zeros_like(v) for k, v in p0.items()},
             {k: jnp.zeros_like(v) for k, v in p0.items()})

    modules = {"layer1": ["W1", "b1"], "head": ["W2", "b2"]}
    def gate_of(act):
        g = {k: 1.0 for k in p0}
        if act is not None:
            for m in act[0]:
                for lf in modules[m]:
                    g[lf] = act[1]
        return g

    bbone = JaxBackbone(step, params_of, moments_view, lr_for_frozen=1e-3)
    XA_ev, YA_ev = jnp.array(X[:512]), jnp.array(YA[:512])
    loss_A = lambda p: mse(p, XA_ev, YA_ev)
    acts = [(["layer1"], 0.1), (["layer1"], 0.5),
            (["head"], 0.1), (["head"], 0.5)]

    tr, bx, bf = [], [], []
    for t in range(1, 41):                               # adapt on B
        b = batch(YB)
        if t % 8 == 4:
            plan = BatchPlan(batches=[batch(YB) for _ in range(5)])
            base = _roll(step, state, plan, t, gate_of, 5)
            res = bbone.measure(state, t, plan, acts, [5], gate_of, loss_A,
                                frozen_d=True,
                                loss_B_of_batch=lambda p, bb_: mse(
                                    p, bb_[0], bb_[1]))
            for act in acts:
                ro = _roll(step, state, plan, t, gate_of, 5, act)
                tr.append(float(loss_A(ro[0]) - loss_A(base[0])))
                terms = res[repr(act)][5]
                bx.append(terms.tau_hat_A)
                bf.append(terms.extras["tau_hat_A_frozen_d"])
        state = step(state, b, t, gate_of(None))
    return {"spearman_exact_d_h5": spearman(bx, tr),
            "spearman_frozen_d_h5": spearman(bf, tr)}


def _roll(step, state, plan, t0, gate_of, h, act=None):
    st = state
    for k in range(h):
        st = step(st, plan.batches[k], t0 + k,
                  gate_of(act if k == 0 else None))
    return st


if __name__ == "__main__":
    selftest()
