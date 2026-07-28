#!/usr/bin/env python3
"""
Commutator-critic sandbox, part 1: block-quadratic fixture (NumPy, float64).

Everything here has closed-form ground truth, so each mechanism of the
grey-box commutator critic can be validated exactly:

  D1  CRN paired rollouts == closed-form counterfactual (machine precision)
  D2  Backbone (tangent propagator via HVP oracle only) vs exact truth
      -- both the validation-mode backbone (rides the baseline rollout)
      -- and the decision-time backbone (noise-free preview rollout)
  D3  Exact one-step synergy identity  tau(pair)-tau(m)-tau(n) = u_m^T H_A u_n
      and its horizon-h propagated form; additive comparator = cross term deleted
  D4  Null family: first-order term provably >= 0 at every state
  D5  Margin decay along the trajectory (why V3's declared orderings HAD to fail)
  D6  Insufficient statistics: feature-identical states with different /
      sign-flipped tau at h>1  +  black-box regressor ceiling vs backbone

Conventions match the V-series: the action gates the *realized stochastic*
incoming gradient after backward, before the (SGD) step; both arms then share
all continuation noise (CRN). The backbone touches the fixture ONLY through
decision-time-legal oracles: grad_A, grad_B(+noise), hvp_A(v), hvp_B(v).
"""

import json
import numpy as np

rng_global = np.random.default_rng(0)

# ----------------------------------------------------------------------------
# small utilities
# ----------------------------------------------------------------------------

def spearman(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 3 or np.std(x) == 0 or np.std(y) == 0:
        return np.nan
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    return float(np.corrcoef(rx, ry)[0, 1])


def log_uniform(rng, lo, hi, n):
    return np.exp(rng.uniform(np.log(lo), np.log(hi), n))


# ----------------------------------------------------------------------------
# fixture
# ----------------------------------------------------------------------------

class QuadFixture:
    """L_A = 1/2 (th-a*)' QA (th-a*),  L_B = 1/2 (th-b*)' QB (th-b*).
    SGD:  th <- th - eta * G_a * (QB(th-b*) + sigma*xi)."""

    def __init__(self, QA, QB, a_star, b_star, eta, sigma, modules):
        self.QA, self.QB = QA, QB
        self.a, self.b = a_star, b_star
        self.eta, self.sigma = eta, sigma
        self.modules = modules  # list of index arrays
        self.d = len(a_star)

    # ---- decision-time-legal oracles (the only fixture access the backbone gets)
    def grad_A(self, th):
        return self.QA @ (th - self.a)

    def grad_B_clean(self, th):
        return self.QB @ (th - self.b)

    def hvp_A(self, v):
        return self.QA @ v

    def hvp_B(self, v):
        return self.QB @ v

    def loss_A(self, th):
        r = th - self.a
        return 0.5 * r @ (self.QA @ r)

    # ---- dynamics
    def gate_vec(self, action):
        """action = (list_of_modules, alpha) or None for ordinary.
        Returns diagonal of G_a."""
        g = np.ones(self.d)
        if action is not None:
            mods, alpha = action
            for m in mods:
                g[self.modules[m]] = alpha
        return g

    def rollout(self, th0, action, h, noise):
        """One arm: gate applies only at step 0; noise is (h,d), shared CRN."""
        th = th0.copy()
        for k in range(h):
            ghat = self.grad_B_clean(th) + self.sigma * noise[k]
            if k == 0:
                ghat = self.gate_vec(action) * ghat
            th = th - self.eta * ghat
        return th

    def tau_rollout(self, th0, action, h, noise):
        thA = self.rollout(th0, action, h, noise)
        th0_ = self.rollout(th0, None, h, noise)
        return self.loss_A(thA) - self.loss_A(th0_), th0_

    # ---- exact counterfactual (affine dynamics: continuation noise cancels)
    def injected_u(self, th0, action, noise0):
        ghat = self.grad_B_clean(th0) + self.sigma * noise0
        mods, alpha = action
        u = np.zeros(self.d)
        for m in mods:
            idx = self.modules[m]
            u[idx] = self.eta * (1.0 - alpha) * ghat[idx]
        return u

    def propagate(self, v, h_minus_1, hvp=None):
        """v <- (I - eta*QB)^(h-1) v, via the HVP oracle only."""
        hvp = hvp or self.hvp_B
        for _ in range(h_minus_1):
            v = v - self.eta * hvp(v)
        return v

    def tau_exact(self, th0, action, h, noise):
        """Closed form: Delta_h = (I-eta QB)^(h-1) u ;
        tau = gA(th0_{t+h})' Delta + 1/2 Delta' QA Delta (EXACT for quadratics)."""
        u = self.injected_u(th0, action, noise[0])
        Delta = self.propagate(u, h - 1)
        th0_h = self.rollout(th0, None, h, noise)
        return self.grad_A(th0_h) @ Delta + 0.5 * Delta @ (self.QA @ Delta)


# ----------------------------------------------------------------------------
# backbone (uses oracles only; never touches QA/QB matrices directly)
# ----------------------------------------------------------------------------

def backbone_validation(fx, th0, action, h, noise):
    """First-order linear response, riding the realized baseline rollout
    (validation mode -- how Stage C2's paired runner computes it)."""
    u = fx.injected_u(th0, action, noise[0])
    v = fx.propagate(u, h - 1)                       # h-1 HVPs
    th0_h = fx.rollout(th0, None, h, noise)          # the baseline arm (run anyway)
    return fx.grad_A(th0_h) @ v


def backbone_decision_time(fx, th0, action, h, noise0):
    """Decision-time-legal version: noise-free deterministic PREVIEW rollout
    stands in for the future baseline (no peeking at future minibatches)."""
    u = fx.injected_u(th0, action, noise0)
    v = fx.propagate(u, h - 1)
    th_prev = th0.copy()
    for _ in range(h):                               # sigma = 0 preview
        th_prev = th_prev - fx.eta * fx.grad_B_clean(th_prev)
    return fx.grad_A(th_prev) @ v


def backbone_synergy(fx, th0, m, n, alpha, h, noise0):
    """Propagated cross-curvature (Phi u_m)' H_A (Phi u_n), oracles only."""
    um = fx.injected_u(th0, ([m], alpha), noise0)
    un = fx.injected_u(th0, ([n], alpha), noise0)
    vm = fx.propagate(um, h - 1)
    vn = fx.propagate(un, h - 1)
    return vm @ fx.hvp_A(vn)


# ----------------------------------------------------------------------------
# fixture families (d=64, M=4x16)
# ----------------------------------------------------------------------------

def make_families(seed=1, d=64, M=4, eta=0.1, sigma=1e-3):
    rng = np.random.default_rng(seed)
    modules = [np.arange(i * (d // M), (i + 1) * (d // M)) for i in range(M)]

    def diag_spec(lo=0.05, hi=1.0):
        return np.diag(log_uniform(rng, lo, hi, d))

    fams = {}

    # NULL: shared minimizer, both diagonal -> provably aligned everywhere.
    QA, QB = diag_spec(), diag_spec()
    c = rng.normal(size=d)
    fams["null"] = QuadFixture(QA, QB, c, c.copy(), eta, sigma, modules)

    # LOCAL-SPECIFIC: targets differ only on module 0; QA stiffened there.
    QA, QB = diag_spec(), diag_spec()
    QA[np.ix_(modules[0], modules[0])] *= 3.0
    a = rng.normal(size=d)
    b = a.copy()
    disp = rng.normal(size=len(modules[0]))
    b[modules[0]] += 2.0 * disp / np.linalg.norm(disp)
    fams["local"] = QuadFixture(QA, QB, a, b, eta, sigma, modules)

    # CHAIN: QB cross-block couples modules 0<->1 (spectral norm 0.3).
    QA = diag_spec()
    qb = log_uniform(rng, 0.05, 1.0, d)
    qb[modules[0]] = log_uniform(rng, 0.4, 1.0, len(modules[0]))
    qb[modules[1]] = log_uniform(rng, 0.4, 1.0, len(modules[1]))
    QB = np.diag(qb)
    C = rng.normal(size=(len(modules[0]), len(modules[1])))
    C *= 0.3 / np.linalg.svd(C, compute_uv=False)[0]
    QB[np.ix_(modules[0], modules[1])] = C
    QB[np.ix_(modules[1], modules[0])] = C.T
    assert np.linalg.eigvalsh(QB).min() > 0
    a = rng.normal(size=d)
    b = a + 1.5 * rng.normal(size=d) / np.sqrt(d) * np.sqrt(d)  # broad conflict
    fams["chain"] = QuadFixture(QA, QB, a, b, eta, sigma, modules)

    # SYNERGY: QA cross-block couples modules 2<->3. The block is rank-1 and
    # ALIGNED with the early-phase incoming gradient (effect-size precheck:
    # planted synergy must clear 5x the noise floor -- the C1 design rule).
    qa = log_uniform(rng, 0.05, 1.0, d)
    qa[modules[2]] = log_uniform(rng, 0.5, 1.0, len(modules[2]))
    qa[modules[3]] = log_uniform(rng, 0.5, 1.0, len(modules[3]))
    QA = np.diag(qa)
    QB = diag_spec()
    a = rng.normal(size=d)
    b = a.copy()
    for m in (2, 3):
        dsp = rng.normal(size=len(modules[m]))
        b[modules[m]] += 2.5 * dsp / np.linalg.norm(dsp)
    gB_at_a = QB @ (a - b)                      # incoming gradient at theta=a
    u2 = gB_at_a[modules[2]] / np.linalg.norm(gB_at_a[modules[2]])
    u3 = gB_at_a[modules[3]] / np.linalg.norm(gB_at_a[modules[3]])
    C = 0.4 * np.outer(u2, u3)
    QA[np.ix_(modules[2], modules[3])] = C
    QA[np.ix_(modules[3], modules[2])] = C.T
    assert np.linalg.eigvalsh(QA).min() > 0
    fams["synergy"] = QuadFixture(QA, QB, a, b, eta, sigma, modules)

    # stability check eta*lmax <= 0.5 for every family
    for name, fx in fams.items():
        lmax = np.linalg.eigvalsh(fx.QB).max()
        assert eta * lmax <= 0.5 + 1e-12, (name, eta * lmax)
    return fams


def gen_states(fx, n_steps=240, every=4, seed=7):
    """Run a noisy training trajectory on task B, harvest decision states
    (state = theta + the realized step-0 noise draw + a CRN continuation seed)."""
    rng = np.random.default_rng(seed)
    th = fx.a + rng.normal(size=fx.d)
    states = []
    for t in range(n_steps):
        if t % every == 0:
            states.append((t, th.copy(), rng.integers(1 << 30)))
        th = th - fx.eta * (fx.grad_B_clean(th) + fx.sigma * rng.normal(size=fx.d))
    return states


def noise_for(fx, seed, h):
    return np.random.default_rng(seed).normal(size=(h, fx.d))


# ----------------------------------------------------------------------------
# D-suite
# ----------------------------------------------------------------------------

HORIZONS = [1, 2, 5, 10, 20]
ALPHAS = [0.5, 0.1]


def actions_for(fx, fam):
    acts = [([m], a) for m in range(len(fx.modules)) for a in ALPHAS]
    pair = {"chain": (0, 1), "synergy": (2, 3)}.get(fam, (0, 1))
    acts.append(([pair[0], pair[1]], 0.1))       # planted / default pair
    acts.append(([0, 3], 0.1))                   # control pair
    return acts


def noise_floor(fx, states, h, n_rep=32, n_probe=10, seed=99):
    """sigma_noise(h): std of tau over resampled CRN continuations, at probe
    states, for a strong single action -- the protocol's measured floor."""
    rng = np.random.default_rng(seed)
    probes = states[:: max(1, len(states) // n_probe)][:n_probe]
    stds = []
    for (_, th, _) in probes:
        taus = [fx.tau_rollout(th, ([0], 0.1), h,
                               rng.normal(size=(h, fx.d)))[0]
                for _ in range(n_rep)]
        stds.append(np.std(taus))
    return float(np.median(stds))


def run_family(name, fx):
    out = {"family": name}
    states = gen_states(fx)
    floors = {h: noise_floor(fx, states, h) for h in HORIZONS}
    out["noise_floor"] = {str(h): floors[h] for h in HORIZONS}

    # D1: rollout vs closed form; D2 backbones; collect per horizon
    d1_err = []
    per_h = {h: {"true": [], "bb_val": [], "bb_dt": []} for h in HORIZONS}
    for (_, th, cseed) in states:
        nz_full = noise_for(fx, cseed, max(HORIZONS))
        for act in actions_for(fx, name):
            for h in HORIZONS:
                nz = nz_full[:h]
                t_roll, _ = fx.tau_rollout(th, act, h, nz)
                t_exact = fx.tau_exact(th, act, h, nz)
                d1_err.append(abs(t_roll - t_exact) / max(abs(t_exact), 1e-300))
                per_h[h]["true"].append(t_roll)
                per_h[h]["bb_val"].append(backbone_validation(fx, th, act, h, nz))
                per_h[h]["bb_dt"].append(
                    backbone_decision_time(fx, th, act, h, nz[0]))
    out["D1_max_rel_err_rollout_vs_closed_form"] = float(np.max(d1_err))

    out["D2"] = {}
    for h in HORIZONS:
        tr = np.array(per_h[h]["true"])
        bv = np.array(per_h[h]["bb_val"])
        bd = np.array(per_h[h]["bb_dt"])
        q = np.abs(tr) >= 3 * floors[h]            # margin-qualified
        rel = np.median(np.abs(bv[q] - tr[q]) /
                        np.maximum(np.abs(tr[q]), 3 * floors[h])) if q.any() else np.nan
        out["D2"][str(h)] = {
            "n_qualified": int(q.sum()), "n_total": int(len(tr)),
            "spearman_backbone_validation": spearman(bv[q], tr[q]),
            "spearman_backbone_decision_time": spearman(bd[q], tr[q]),
            "median_rel_err_validation": float(rel),
        }

    # D3: synergy identity, planted vs control pair
    if name == "synergy":
        m, n = 2, 3
        rows = {h: {"true": [], "hat": [], "ctrl_true": []} for h in [1, 5, 10]}
        early = [s for s in states if s[0] <= 40]    # effect-size precheck slice
        for (_, th, cseed) in early:
            nz_full = noise_for(fx, cseed, 10)
            for h in [1, 5, 10]:
                nz = nz_full[:h]
                tp = fx.tau_rollout(th, ([m, n], 0.1), h, nz)[0]
                tm = fx.tau_rollout(th, ([m], 0.1), h, nz)[0]
                tn = fx.tau_rollout(th, ([n], 0.1), h, nz)[0]
                rows[h]["true"].append(tp - tm - tn)
                rows[h]["hat"].append(backbone_synergy(fx, th, m, n, 0.1, h, nz[0]))
                cp = fx.tau_rollout(th, ([0, 1], 0.1), h, nz)[0] \
                    - fx.tau_rollout(th, ([0], 0.1), h, nz)[0] \
                    - fx.tau_rollout(th, ([1], 0.1), h, nz)[0]
                rows[h]["ctrl_true"].append(cp)
        out["D3"] = {}
        for h in [1, 5, 10]:
            tr, ht = np.array(rows[h]["true"]), np.array(rows[h]["hat"])
            out["D3"][str(h)] = {
                "median_rel_err_synergy_identity":
                    float(np.median(np.abs(ht - tr) / np.abs(tr))),
                "median_abs_planted_synergy": float(np.median(np.abs(tr))),
                "median_abs_control_pair_synergy":
                    float(np.median(np.abs(rows[h]["ctrl_true"]))),
                "noise_floor": floors.get(h, floors[5]),
                "precheck_ratio_planted_over_floor":
                    float(np.median(np.abs(tr)) / floors.get(h, floors[5])),
            }

    # D4: null nonnegativity (analytic, every state, every module)
    if name == "null":
        worst = np.inf
        for (_, th, cseed) in states:
            gA, gB = fx.grad_A(th), fx.grad_B_clean(th)
            for m in range(4):
                worst = min(worst, gA[fx.modules[m]] @ gB[fx.modules[m]])
        out["D4_min_firstorder_alignment"] = float(worst)   # must be >= 0
        fb = 0
        for (_, th, cseed) in states:
            nz = noise_for(fx, cseed, 10)
            for act in actions_for(fx, name):
                if fx.tau_rollout(th, act, 10, nz)[0] < -3 * floors[10]:
                    fb += 1
        out["D4_false_beneficial_beyond_3sigma"] = fb

    # D5: margin decay along the trajectory
    if name == "local":
        margins, tsteps = [], []
        long_states = gen_states(fx, n_steps=640, every=8, seed=7)
        for (t, th, cseed) in long_states:
            nz = noise_for(fx, cseed, 10)
            taus = [fx.tau_exact(th, act, 10, nz) for act in actions_for(fx, name)]
            margins.append(max(taus) - min(taus))
            tsteps.append(t)
        margins = np.array(margins)
        k = np.polyfit(tsteps, np.log(np.maximum(margins, 1e-300)), 1)[0]
        out["D5"] = {
            "margin_first": float(margins[0]), "margin_last": float(margins[-1]),
            "fitted_decay_rate_per_step": float(k),
            "predicted_rate_ln(1-eta*lmin(QB))":
                float(np.log(1 - fx.eta * np.linalg.eigvalsh(fx.QB).min())),
            "no_signal_frac_first_quartile":
                float(np.mean(margins[: len(margins) // 4] < 3 * floors[10])),
            "no_signal_frac_last_quartile":
                float(np.mean(margins[-len(margins) // 4:] < 3 * floors[10])),
        }
        out["_margin_curve"] = [tsteps, margins.tolist()]

    out["_scatter"] = {str(h): (per_h[h]["true"], per_h[h]["bb_val"])
                       for h in [1, 10]}
    return out


# ----------------------------------------------------------------------------
# D6a: feature-identical states, different tau (constructive)
# ----------------------------------------------------------------------------

def demo_insufficient_statistics(seed=3):
    """Single 16-dim module. qA uniform, a*=0, b*=delta*1, qB log-spread.
    V2-style features on the module: (|gA|, |gB|, cos(gA,gB), |theta|).
    With qA uniform and a*=0, |theta| = |gA|/q, so three constraints bind.
    We Gauss-Newton-project candidate states onto a reference state's exact
    feature values and show tau at h>1 still differs / flips sign, while the
    h=1 EXACT tau (first order + uniform-curvature term) provably coincides."""
    rng = np.random.default_rng(seed)
    d, q, delta, eta = 16, 0.3, 0.8, 0.1
    qB = log_uniform(rng, 0.05, 1.0, d)
    fx = QuadFixture(np.diag(np.full(d, q)), np.diag(qB),
                     np.zeros(d), np.full(d, delta), eta, 0.0, [np.arange(d)])

    def feats(th):
        gA, gB = fx.grad_A(th), fx.grad_B_clean(th)
        return np.array([gA @ gA, gB @ gB, gA @ gB])

    def tau_h(th, h):
        nz = np.zeros((h, d))
        return fx.tau_exact(th, ([0], 0.1), h, nz)

    def gn_project(th, target, iters=40):
        for _ in range(iters):
            r = feats(th) - target
            if np.max(np.abs(r)) < 1e-13:
                break
            gA, gB = fx.grad_A(th), fx.grad_B_clean(th)
            J = np.stack([2 * q * gA, 2 * qB * gB, q * gB + qB * gA])
            th = th - J.T @ np.linalg.solve(J @ J.T + 1e-12 * np.eye(3),
                                            r)
        return th

    th_ref = rng.uniform(-0.4, 1.6, d)
    target = feats(th_ref)
    found = []
    for _ in range(4000):
        cand = gn_project(rng.uniform(-0.4, 1.6, d), target)
        if np.max(np.abs(feats(cand) - target)) < 1e-10:
            found.append(cand)
        if len(found) >= 400:
            break
    ref = {h: tau_h(th_ref, h) for h in [1, 5, 10]}
    rows, flips = [], 0
    for cand in found:
        tv = {h: tau_h(cand, h) for h in [1, 5, 10]}
        if np.sign(tv[10]) != np.sign(ref[10]):
            flips += 1
            if len(rows) < 3:
                rows.append({str(h): (ref[h], tv[h]) for h in [1, 5, 10]})
    spread10 = np.array([tau_h(c, 10) for c in found])
    return {
        "n_feature_identical_states": len(found),
        "max_feature_mismatch": 1e-10,
        "tau_h1_all_equal_check":
            float(np.max(np.abs([tau_h(c, 1) - ref[1] for c in found]))),
        "tau_h10_reference": ref[10],
        "tau_h10_range_over_identical_features":
            [float(spread10.min()), float(spread10.max())],
        "n_sign_flips_at_h10": flips,
        "example_pairs (ref, feature-identical-state)": rows,
    }


# ----------------------------------------------------------------------------
# D6b: black-box regressor ceiling vs backbone (local family, h=10)
# ----------------------------------------------------------------------------

def make_local_instance(seed, d=64, M=4, eta=0.1, sigma=1e-3):
    """Instances for the ceiling test use WIDE spectra (qB in [0.05, 4], so
    eta*lmax = 0.4, still stable) and are evaluated at h=50: there the
    propagator reweighting (1 - eta*qB_i)^(h-1) spans ~1e-11 .. 0.78, so the
    horizon content of tau dominates its feature-visible first-order shadow.
    (At h=1 the first-order term is EXACTLY cos*|gA|*|gB| and hence
    feature-determined -- black-box features fail with horizon and curvature,
    not at leading order; cf. the constructive D6a demo.)"""
    rng = np.random.default_rng(seed)
    modules = [np.arange(i * (d // M), (i + 1) * (d // M)) for i in range(M)]
    QA = np.diag(log_uniform(rng, 0.05, 2.0, d))
    QB = np.diag(log_uniform(rng, 0.05, 4.0, d))
    QA[np.ix_(modules[0], modules[0])] *= 3.0
    a = rng.normal(size=d)
    b = a.copy()
    disp = rng.normal(size=len(modules[0]))
    b[modules[0]] += 2.0 * disp / np.linalg.norm(disp)
    return QuadFixture(QA, QB, a, b, eta, sigma, modules)


def demo_regressor_ceiling(seed=11):
    """V2's actual setting: the critic must generalize across fixture INSTANCES
    (spectra redrawn), not just interpolate one trajectory. Features alias
    across instances (the insufficient-statistics proposition); the backbone
    does not, because it measures each instance's curvature at runtime."""
    rng = np.random.default_rng(seed)
    inst = [make_local_instance(s) for s in range(101, 106)]
    data = []
    for fx in inst:
        X, y, bb = [], [], []
        for (_, th, cseed) in gen_states(fx, n_steps=240, every=4,
                                         seed=int(rng.integers(1 << 30))):
            H = 50
            nz = noise_for(fx, cseed, H)
            gA, gB0 = fx.grad_A(th), fx.grad_B_clean(th) + fx.sigma * nz[0]
            fvec = []
            for idx in fx.modules:
                aa, bv = gA[idx], gB0[idx]
                fvec += [np.linalg.norm(aa), np.linalg.norm(bv),
                         aa @ bv / (np.linalg.norm(aa) * np.linalg.norm(bv)
                                    + 1e-30),
                         np.linalg.norm(th[idx])]
            for m in range(4):
                X.append(fvec + list(np.eye(4)[m]))
                y.append(fx.tau_exact(th, ([m], 0.1), H, nz))
                bb.append(backbone_validation(fx, th, ([m], 0.1), H, nz))
        data.append((np.array(X), np.array(y), np.array(bb)))

    Xtr = np.vstack([d[0] for d in data[:4]])
    ytr = np.concatenate([d[1] for d in data[:4]])
    Xte, yte, bbte = data[4]
    mu, sd = Xtr.mean(0), Xtr.std(0) + 1e-12
    Xtr_s, Xte_s = (Xtr - mu) / sd, (Xte - mu) / sd
    best = (-2.0, None)
    for lam in [1e-6, 1e-4, 1e-2, 1.0]:
        w = np.linalg.solve(Xtr_s.T @ Xtr_s + lam * np.eye(Xtr.shape[1]),
                            Xtr_s.T @ ytr)
        s = spearman(Xtr_s @ w, ytr)
        if s > best[0]:
            best = (s, w)
    D2 = ((Xte_s[:, None, :] - Xtr_s[None, :, :]) ** 2).sum(-1)
    knn_pred = ytr[np.argsort(D2, 1)[:, :5]].mean(1)
    return {
        "setting": "train on 4 wide-spectrum instances, test on a 5th; h=50",
        "n_train": len(ytr), "n_test": len(yte),
        "spearman_ridge_on_V2_features": spearman(Xte_s @ best[1], yte),
        "spearman_knn5_on_V2_features": spearman(knn_pred, yte),
        "spearman_backbone_same_test_set": spearman(bbte, yte),
    }


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------

if __name__ == "__main__":
    np.seterr(all="raise")
    fams = make_families()
    results = {}
    for name, fx in fams.items():
        print(f"[{name}] running ...", flush=True)
        results[name] = run_family(name, fx)
    print("[D6a] insufficient statistics (constructive) ...", flush=True)
    results["D6a_insufficient_statistics"] = demo_insufficient_statistics()
    print("[D6b] regressor ceiling ...", flush=True)
    results["D6b_regressor_ceiling"] = demo_regressor_ceiling()

    # plots
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(1, 3, figsize=(13, 4))
        for name, c in zip(["null", "local", "chain", "synergy"],
                           ["tab:gray", "tab:blue", "tab:green", "tab:red"]):
            for ax, h in zip(axes[:2], ["1", "10"]):
                t, b = results[name]["_scatter"][h]
                ax.plot(t, b, ".", ms=3, alpha=0.5, color=c, label=name)
                ax.set_title(f"backbone vs true tau, h={h}")
                ax.set_xlabel("true paired tau^A"); ax.set_ylabel("backbone")
        lo = min(axes[0].get_xlim()[0], axes[1].get_xlim()[0])
        for ax in axes[:2]:
            xl = ax.get_xlim(); ax.plot(xl, xl, "k-", lw=0.6); ax.legend(fontsize=7)
        ts, mg = results["local"]["_margin_curve"]
        axes[2].semilogy(ts, mg, "o-", ms=3)
        fl = results["local"]["noise_floor"]["10"]
        axes[2].axhline(3 * fl, color="r", ls="--", label="3 x noise floor")
        axes[2].set_title("action margin along trajectory (local family)")
        axes[2].set_xlabel("training step t"); axes[2].legend(fontsize=8)
        fig.tight_layout(); fig.savefig("quadratic_demo.png", dpi=130)
        print("wrote quadratic_demo.png")
    except Exception as e:  # plots are optional
        print("plotting skipped:", e)

    for r in results.values():
        if isinstance(r, dict):
            r.pop("_scatter", None); r.pop("_margin_curve", None)
    with open("results_quadratic.json", "w") as f:
        json.dump(results, f, indent=2, default=float)
    print(json.dumps(results, indent=2, default=float))
