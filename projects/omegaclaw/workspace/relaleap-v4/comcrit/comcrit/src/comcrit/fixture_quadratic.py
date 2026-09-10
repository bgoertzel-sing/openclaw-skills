"""The block-quadratic fixture: comcrit's built-in positive control.

Ported from the validated sandbox (`quadratic_demo.py`). Ground truth is
recomputed analytically PER STATE — nothing is declared, so nothing can be
"violated" by the trajectory; only the expansion's validity radius can
shrink, and that is measured.

The backbone functions here access the fixture only through the same
decision-time-legal oracle surface a real learner exposes (grad/HVP),
mimicking the production API.
"""
from __future__ import annotations

import numpy as np

from .partition import ModulePartition
from .protocols import Action


def _log_uniform(rng, lo, hi, n):
    return np.exp(rng.uniform(np.log(lo), np.log(hi), n))


class QuadFixture:
    """L_A = 1/2 (th-a*)' QA (th-a*),  L_B = 1/2 (th-b*)' QB (th-b*).
    SGD: th <- th - eta * G_a * (QB(th-b*) + sigma*xi); gate at step 0 only;
    both arms share continuation noise (CRN)."""

    def __init__(self, QA, QB, a_star, b_star, eta, sigma,
                 partition: ModulePartition):
        self.QA, self.QB, self.a, self.b = QA, QB, a_star, b_star
        self.eta, self.sigma, self.part = eta, sigma, partition
        self.d = len(a_star)
        lmax = np.linalg.eigvalsh(QB).max()
        if eta * lmax > 0.5 + 1e-12:            # binding hygiene rule
            raise ValueError(f"eta*lambda_max = {eta * lmax:.3f} > 0.5")

    # ---- oracle surface (all the backbone may touch)
    def grad_A(self, th): return self.QA @ (th - self.a)
    def grad_B_clean(self, th): return self.QB @ (th - self.b)
    def hvp_A(self, v): return self.QA @ v
    def hvp_B(self, v): return self.QB @ v
    def loss_A(self, th):
        r = th - self.a
        return 0.5 * r @ (self.QA @ r)

    # ---- dynamics
    def rollout(self, th0, action: Action | None, h, noise):
        th = th0.copy()
        for k in range(h):
            g = self.grad_B_clean(th) + self.sigma * noise[k]
            if k == 0:
                g = self.part.gate_vec(action) * g
            th = th - self.eta * g
        return th

    def tau_rollout(self, th0, action, h, noise):
        thA = self.rollout(th0, action, h, noise)
        thO = self.rollout(th0, None, h, noise)
        return self.loss_A(thA) - self.loss_A(thO)

    # ---- exact counterfactual (affine: continuation noise cancels)
    def injected_u(self, th0, action: Action, noise0):
        g = self.grad_B_clean(th0) + self.sigma * noise0
        mods, alpha = action
        u = np.zeros(self.d)
        for m in mods:
            idx = self.part.mask(m)
            u[idx] = self.eta * (1.0 - alpha) * g[idx]
        return u

    def propagate(self, v, h_minus_1):
        for _ in range(h_minus_1):
            v = v - self.eta * self.hvp_B(v)
        return v

    def tau_exact(self, th0, action, h, noise):
        u = self.injected_u(th0, action, noise[0])
        Delta = self.propagate(u, h - 1)
        thO = self.rollout(th0, None, h, noise)
        return self.grad_A(thO) @ Delta + 0.5 * Delta @ (self.QA @ Delta)

    # ---- reference backbone (validation mode; first order only)
    def backbone_validation(self, th0, action, h, noise):
        u = self.injected_u(th0, action, noise[0])
        v = self.propagate(u, h - 1)
        thO = self.rollout(th0, None, h, noise)
        return self.grad_A(thO) @ v

    def backbone_preview(self, th0, action, h, noise0):
        """Decision-time-legal: noise-free preview rollout stands in for the
        realized future baseline."""
        u = self.injected_u(th0, action, noise0)
        v = self.propagate(u, h - 1)
        th = th0.copy()
        for _ in range(h):
            th = th - self.eta * self.grad_B_clean(th)
        return self.grad_A(th) @ v

    def synergy_hat(self, th0, m, n, alpha, h, noise0):
        um = self.injected_u(th0, ([m], alpha), noise0)
        un = self.injected_u(th0, ([n], alpha), noise0)
        return self.propagate(um, h - 1) @ self.hvp_A(self.propagate(un, h - 1))

    def decompose_onestep(self, th0, action: Action, noise0) -> dict:
        """Lemma-1 terms at the decision state (decision-time observable):
            first_order = <g_A, u>
            drift       = delta0' H_A u        (delta0 = ordinary step)
            self_curv   = 1/2 u' H_A u
            cross_curv  = u_m' H_A u_n         (pair actions only)
        For quadratic L_A the identity
            first_order + drift + self_curv == tau_exact(h=1)
        holds EXACTLY (tested to 1e-10); generally it holds to O(step^3)."""
        u = self.injected_u(th0, action, noise0)
        delta0 = -self.eta * (self.grad_B_clean(th0) + self.sigma * noise0)
        Hu = self.hvp_A(u)
        d = {"first_order": float(self.grad_A(th0) @ u),
             "drift": float(delta0 @ Hu),
             "self_curv": float(0.5 * u @ Hu),
             "cross_curv": None}
        mods = action[0]
        if len(mods) == 2:
            u_m = np.zeros(self.d); u_n = np.zeros(self.d)
            im, jn = self.part.mask(mods[0]), self.part.mask(mods[1])
            u_m[im], u_n[jn] = u[im], u[jn]
            d["cross_curv"] = float(u_m @ self.hvp_A(u_n))
        d["total_onestep"] = d["first_order"] + d["drift"] + d["self_curv"]
        return d


def default_partition(d=64, M=4) -> ModulePartition:
    idx = {f"m{i}": np.arange(i * (d // M), (i + 1) * (d // M))
           for i in range(M)}
    return ModulePartition(index_modules=idx, dim=d)


def make_family(name: str, seed=1, d=64, M=4, eta=0.1, sigma=1e-3,
                synergy_disp=2.5) -> QuadFixture:
    """Families: 'null' (shared minimizer, both diagonal: provably aligned),
    'local' (conflict on m0, QA stiffened there), 'chain' (QB cross-block
    m0<->m1), 'synergy' (QA cross-block m2<->m3, RANK-1 AND ALIGNED with the
    early-phase incoming gradient — the sandbox showed a random-direction
    block lands at 0.1x the noise floor; Lesson 1)."""
    rng = np.random.default_rng(seed)
    part = default_partition(d, M)
    mods = [part.mask(f"m{i}") for i in range(M)]
    diag = lambda lo=0.05, hi=1.0: np.diag(_log_uniform(rng, lo, hi, d))

    if name == "null":
        c = rng.normal(size=d)
        return QuadFixture(diag(), diag(), c, c.copy(), eta, sigma, part)

    if name == "local":
        QA, QB = diag(), diag()
        QA[np.ix_(mods[0], mods[0])] *= 3.0
        a = rng.normal(size=d); b = a.copy()
        disp = rng.normal(size=len(mods[0]))
        b[mods[0]] += 2.0 * disp / np.linalg.norm(disp)
        return QuadFixture(QA, QB, a, b, eta, sigma, part)

    if name == "chain":
        QA = diag()
        qb = _log_uniform(rng, 0.05, 1.0, d)
        for i in (0, 1):
            qb[mods[i]] = _log_uniform(rng, 0.4, 1.0, len(mods[i]))
        QB = np.diag(qb)
        C = rng.normal(size=(len(mods[0]), len(mods[1])))
        C *= 0.3 / np.linalg.svd(C, compute_uv=False)[0]
        QB[np.ix_(mods[0], mods[1])] = C
        QB[np.ix_(mods[1], mods[0])] = C.T
        assert np.linalg.eigvalsh(QB).min() > 0
        a = rng.normal(size=d)
        b = a + 1.5 * rng.normal(size=d)
        return QuadFixture(QA, QB, a, b, eta, sigma, part)

    if name == "synergy":
        qa = _log_uniform(rng, 0.05, 1.0, d)
        for i in (2, 3):
            qa[mods[i]] = _log_uniform(rng, 0.5, 1.0, len(mods[i]))
        QA = np.diag(qa)
        QB = diag()
        a = rng.normal(size=d); b = a.copy()
        for i in (2, 3):
            dsp = rng.normal(size=len(mods[i]))
            b[mods[i]] += synergy_disp * dsp / np.linalg.norm(dsp)
        gB = QB @ (a - b)
        u2 = gB[mods[2]] / np.linalg.norm(gB[mods[2]])
        u3 = gB[mods[3]] / np.linalg.norm(gB[mods[3]])
        C = 0.4 * np.outer(u2, u3)
        QA[np.ix_(mods[2], mods[3])] = C
        QA[np.ix_(mods[3], mods[2])] = C.T
        assert np.linalg.eigvalsh(QA).min() > 0
        return QuadFixture(QA, QB, a, b, eta, sigma, part)

    raise ValueError(name)


def gen_states(fx: QuadFixture, n_steps=240, every=4, seed=7):
    """(t, theta, continuation_seed) harvested along a noisy trajectory."""
    rng = np.random.default_rng(seed)
    th = fx.a + rng.normal(size=fx.d)
    out = []
    for t in range(n_steps):
        if t % every == 0:
            out.append((t, th.copy(), int(rng.integers(1 << 30))))
        th = th - fx.eta * (fx.grad_B_clean(th)
                            + fx.sigma * rng.normal(size=fx.d))
    return out


def noise_for(fx, seed, h):
    return np.random.default_rng(seed).normal(size=(h, fx.d))
