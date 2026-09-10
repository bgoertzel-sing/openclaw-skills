#!/usr/bin/env python3
"""
Commutator-critic sandbox, part 2: real nonlinear learner (JAX, float64).

A 3-layer tanh MLP is pretrained on task A, then adapted with Adam to a
conflicting task B. At decision states along the adaptation trajectory we run
the full V-series machinery at toy scale:

  * actions gate one module's (or a pair's) incoming gradient at a single
    step, after backward and before Adam;
  * ground truth = CRN paired rollouts (identical batch sequences, identical
    Adam state at the snapshot) evaluated at horizons h in {1, 5, 10};
  * the BACKBONE computes, with no learned component:
      - the EXACT injected perturbation of the full optimizer state
        (theta, m, v)  -- one gated step vs one ordinary step from snapshot;
      - its linear-response propagation along the baseline rollout via
        forward-mode jax.jvp through the *entire* Adam update (exact-D),
        plus a frozen-D variant (tangent <- tangent - lr * D_k * HVP_B);
      - tau_hat^A = d L_A in the direction of the propagated theta-tangent;
  * the one-step synergy identity u_m' H_A u_n is checked against the
    pair-minus-singles rollout difference.

Two conflict families:
  B1 "input-permutation": y_B = teacher_A(P x)  -> conflict lives in layer 1;
  B2 "output-shift":      y_B = teacher_A(x)+c  -> conflict lives in the head.

Expected picture (the point of the demo): backbone Spearman vs paired truth
is ~1.0 at h=1 and degrades gracefully with horizon (the "validity radius");
exact-D beats frozen-D; protecting the conflict-bearing module is what helps
retention, and every gate costs incoming loss (tau^B >= 0), both read off the
backbone terms directly.
"""

import json
import numpy as np
import jax
import jax.numpy as jnp
from jax import grad, jvp, tree_util as jtu

jax.config.update("jax_enable_x64", True)

# ----------------------------------------------------------------------------
B1M, B2M, EPS = 0.9, 0.999, 1e-8
DIN, H1, H2, DOUT = 8, 32, 32, 4
HORIZONS = [1, 5, 10, 25]
ALPHAS = [0.5, 0.1]
MODULES = {"layer1": ("W1", "b1"), "layer2": ("W2", "b2"), "head": ("W3", "b3")}


def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 3 or np.std(x) == 0 or np.std(y) == 0:
        return float("nan")
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    return float(np.corrcoef(rx, ry)[0, 1])


def init_params(key, scale=0.5):
    ks = jax.random.split(key, 6)
    return {
        "W1": scale * jax.random.normal(ks[0], (DIN, H1)) / np.sqrt(DIN),
        "b1": jnp.zeros(H1),
        "W2": scale * jax.random.normal(ks[1], (H1, H2)) / np.sqrt(H1),
        "b2": jnp.zeros(H2),
        "W3": scale * jax.random.normal(ks[2], (H2, DOUT)) / np.sqrt(H2),
        "b3": jnp.zeros(DOUT),
    }


def mlp(p, x):
    h = jnp.tanh(x @ p["W1"] + p["b1"])
    h = jnp.tanh(h @ p["W2"] + p["b2"])
    return h @ p["W3"] + p["b3"]


def mse(p, X, Y):
    return jnp.mean((mlp(p, X) - Y) ** 2)


def gate_tree(action):
    """action = (list_of_module_names, alpha) or None."""
    g = {k: 1.0 for k in ["W1", "b1", "W2", "b2", "W3", "b3"]}
    if action is not None:
        mods, alpha = action
        for m in mods:
            for k in MODULES[m]:
                g[k] = alpha
    return g


def adam_step(state, X, Y, t, gate, lr):
    """One gated Adam step on the FULL optimizer state (p, m, v)."""
    p, m, v = state
    g = grad(mse)(p, X, Y)
    g = {k: gate[k] * g[k] for k in g}
    m2 = jtu.tree_map(lambda a, b: B1M * a + (1 - B1M) * b, m, g)
    v2 = jtu.tree_map(lambda a, b: B2M * a + (1 - B2M) * b ** 2, v, g)
    bc1, bc2 = 1 - B1M ** t, 1 - B2M ** t
    p2 = jtu.tree_map(
        lambda pp, mm, vv: pp - lr * (mm / bc1) / (jnp.sqrt(vv / bc2) + EPS),
        p, m2, v2)
    return (p2, m2, v2)


adam_step = jax.jit(adam_step, static_argnums=())

tsub = lambda a, b: jtu.tree_map(lambda x, y: x - y, a, b)
tzero = lambda a: jtu.tree_map(jnp.zeros_like, a)


# ----------------------------------------------------------------------------
# the backbone
# ----------------------------------------------------------------------------

def backbone(state, batches, t0, action, XA, YA, XB, YB, horizons, lr):
    """Exact injection + linear-response propagation (exact-D and frozen-D).

    Returns {h: (tauA_hat_exactD, tauA_hat_frozenD, tauB_hat_exactD)} and
    the injected theta-perturbation u (for the synergy check)."""
    # exact injected perturbation of the full optimizer state at step t0
    gate0 = gate_tree(action)
    st_gated = adam_step(state, batches[0][0], batches[0][1], t0, gate0, lr)
    st_base = adam_step(state, batches[0][0], batches[0][1], t0,
                        gate_tree(None), lr)
    tan = tsub(st_gated, st_base)                     # (dtheta, dm, dv), exact
    u_theta = tan[0]

    # frozen-D tangent: theta-only, J ~= I - lr * D_k * H_B  (doc Eq. 6)
    tan_f = jtu.tree_map(jnp.array, tan[0])

    out = {}
    st, hcount = st_base, 1
    for k in range(1, max(horizons) + 1):
        if hcount in []:
            pass
        if k > 1:
            Xb, Yb = batches[k - 1]
            t = t0 + k - 1
            step_fn = lambda s: adam_step(s, Xb, Yb, t, gate_tree(None), lr)
            st_next, tan = jvp(step_fn, (st,), (tan,))       # exact-D
            # frozen-D: D from the *baseline* moments after this step
            _, hvp_t = jvp(lambda p: grad(mse)(p, Xb, Yb), (st[0],), (tan_f,))
            v_now = st_next[2]
            bc2 = 1 - B2M ** t
            D = jtu.tree_map(lambda vv: 1.0 / (jnp.sqrt(vv / bc2) + EPS), v_now)
            tan_f = jtu.tree_map(lambda tf, dd, hh: tf - lr * dd * hh,
                                 tan_f, D, hvp_t)
            st = st_next
        if k in horizons:
            _, dLA = jvp(lambda p: mse(p, XA, YA), (st[0],), (tan[0],))
            _, dLAf = jvp(lambda p: mse(p, XA, YA), (st[0],), (tan_f,))
            _, dLB = jvp(lambda p: mse(p, XB, YB), (st[0],), (tan[0],))
            out[k] = (float(dLA), float(dLAf), float(dLB))
    return out, u_theta


def rollout_losses(state, batches, t0, action, XA, YA, XB, YB, horizons, lr):
    st = state
    out = {}
    for k in range(1, max(horizons) + 1):
        gate = gate_tree(action if k == 1 else None)
        st = adam_step(st, batches[k - 1][0], batches[k - 1][1],
                       t0 + k - 1, gate, lr)
        if k in horizons:
            out[k] = (float(mse(st[0], XA, YA)), float(mse(st[0], XB, YB)))
    return out


def hvp_A(p, XA, YA, v):
    return jvp(lambda q: grad(mse)(q, XA, YA), (p,), (v,))[1]


def tdot(a, b):
    return float(sum(jnp.vdot(a[k], b[k]) for k in a))


# ----------------------------------------------------------------------------
# experiment
# ----------------------------------------------------------------------------

def run_family(fam_name, make_YB, seed=0, lr=1e-3):
    key = jax.random.PRNGKey(seed)
    kt, kp, kd = jax.random.split(key, 3)
    teacher = init_params(kt, scale=1.0)
    Xpool = np.array(jax.random.normal(kd, (4096, DIN)))
    YA_pool = np.array(mlp(teacher, Xpool))
    YB_pool = make_YB(teacher, Xpool)
    XA_ev, YA_ev = jnp.array(Xpool[:1024]), jnp.array(YA_pool[:1024])
    XB_ev, YB_ev = jnp.array(Xpool[:1024]), jnp.array(YB_pool[:1024])

    rng = np.random.default_rng(seed + 1)

    def batch(rs):
        idx = rs.integers(0, 4096, 64)
        return jnp.array(Xpool[idx]), jnp.array(YA_pool[idx]), \
            jnp.array(YB_pool[idx])

    # pretrain on A
    p = init_params(kp)
    state = (p, tzero(p), tzero(p))
    for t in range(1, 601):
        Xb, Yb, _ = batch(rng)
        state = adam_step(state, Xb, Yb, t, gate_tree(None), 1e-3)
    lA0 = float(mse(state[0], XA_ev, YA_ev))

    # adapt on B, fresh Adam
    state = (state[0], tzero(p), tzero(p))
    actions = [([m], a) for m in MODULES for a in ALPHAS]
    pair = (["layer1", "layer2"], 0.1)
    rows = {h: {"true": [], "bb": [], "bbf": [], "trueB": [], "bbB": [],
                "act": []} for h in HORIZONS}
    syn = {"true": [], "hat": []}
    per_module_tau = {m: [] for m in MODULES}

    n_adapt, every = 150, 10
    for t in range(1, n_adapt + 1):
        Xb, _, Yb = batch(rng)
        if t % every == 5:
            # freeze a CRN continuation batch sequence for this decision state
            crn = np.random.default_rng(int(rng.integers(1 << 30)))
            batches = []
            for _ in range(max(HORIZONS)):
                Xc, _, Yc = batch(crn)
                batches.append((Xc, Yc))
            base = rollout_losses(state, batches, t, None,
                                  XA_ev, YA_ev, XB_ev, YB_ev, HORIZONS, lr)
            u_by_action = {}
            for act in actions + [pair]:
                ro = rollout_losses(state, batches, t, act,
                                    XA_ev, YA_ev, XB_ev, YB_ev, HORIZONS, lr)
                bb, u = backbone(state, batches, t, act,
                                 XA_ev, YA_ev, XB_ev, YB_ev, HORIZONS, lr)
                u_by_action[str(act)] = u
                for h in HORIZONS:
                    tA = ro[h][0] - base[h][0]
                    tB = ro[h][1] - base[h][1]
                    rows[h]["true"].append(tA)
                    rows[h]["bb"].append(bb[h][0])
                    rows[h]["bbf"].append(bb[h][1])
                    rows[h]["trueB"].append(tB)
                    rows[h]["bbB"].append(bb[h][2])
                    rows[h]["act"].append(str(act))
                if act in actions and act[1] == 0.1:
                    per_module_tau[act[0][0]].append(
                        ro[10][0] - base[10][0])
            # synergy identity at h=1 for the pair
            um = u_by_action[str((["layer1"], 0.1))]
            un = u_by_action[str((["layer2"], 0.1))]
            tp = rollout_losses(state, batches, t, pair,
                                XA_ev, YA_ev, XB_ev, YB_ev, [1], lr)[1][0]
            tm = rollout_losses(state, batches, t, (["layer1"], 0.1),
                                XA_ev, YA_ev, XB_ev, YB_ev, [1], lr)[1][0]
            tn = rollout_losses(state, batches, t, (["layer2"], 0.1),
                                XA_ev, YA_ev, XB_ev, YB_ev, [1], lr)[1][0]
            b1 = base[1][0]
            syn["true"].append((tp - b1) - (tm - b1) - (tn - b1))
            syn["hat"].append(tdot(um, hvp_A(state[0], XA_ev, YA_ev, un)))
        state = adam_step(state, Xb, Yb, t, gate_tree(None), lr)

    out = {"family": fam_name, "L_A_after_pretrain": lA0,
           "L_A_after_adapt": float(mse(state[0], XA_ev, YA_ev)),
           "L_B_after_adapt": float(mse(state[0], XB_ev, YB_ev))}
    for h in HORIZONS:
        tr = np.array(rows[h]["true"]); bb = np.array(rows[h]["bb"])
        bf = np.array(rows[h]["bbf"])
        trB = np.array(rows[h]["trueB"]); bbB = np.array(rows[h]["bbB"])
        q = np.abs(tr) >= np.quantile(np.abs(tr), 0.2)     # margin filter
        out[f"h{h}"] = {
            "spearman_exactD": spearman(bb[q], tr[q]),
            "spearman_frozenD": spearman(bf[q], tr[q]),
            "spearman_exactD_unfiltered": spearman(bb, tr),
            "median_rel_err_exactD":
                float(np.median(np.abs(bb[q] - tr[q]) / np.abs(tr[q]))),
            "spearman_incoming_tauB": spearman(bbB, trB),
            "frac_tauB_nonneg": float(np.mean(trB >= -1e-12)),
        }
    st_, ht_ = np.array(syn["true"]), np.array(syn["hat"])
    out["synergy_h1"] = {
        "spearman": spearman(ht_, st_),
        "median_rel_err":
            float(np.median(np.abs(ht_ - st_) / np.maximum(np.abs(st_), 1e-30))),
        "median_abs_true": float(np.median(np.abs(st_))),
    }
    out["median_tauA_h10_strong_gate_by_module"] = {
        m: float(np.median(v)) for m, v in per_module_tau.items()}
    return out


if __name__ == "__main__":
    fams = {
        "B1_input_permutation":
            lambda tc, X: np.array(mlp(tc, X[:, ::-1].copy())),
        "B2_output_shift":
            lambda tc, X: np.array(mlp(tc, X)) + 1.0,
    }
    results = {}
    for name, mk in fams.items():
        print(f"[{name}] running ...", flush=True)
        results[name] = run_family(name, mk)
    print("[B1_stress_lr1e-2] running ...", flush=True)
    results["B1_stress_lr1e-2"] = run_family(
        "B1_stress_lr1e-2", fams["B1_input_permutation"], lr=1e-2)
    with open("results_mlp.json", "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))
