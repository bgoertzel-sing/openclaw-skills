"""Shared operator core + three execution semantics."""
import math
import torch
import torch.nn as nn
import torch.nn.functional as F
from task import V, N_SLOTS, L_MAX, C_VOCAB

class OperatorCore(nn.Module):
    """K parallel read->transform->gate->write operators, batched along K.

    forward(w, feat, extra) -> u of shape [B(, M), K, n, d]
      w    : [..., n, d]   mutable content
      feat : [..., n, 2d]  concat(evidence, position), constant per sample
      extra: [..., 1, d] or None  additive query/key conditioning (step emb)
    """
    def __init__(self, d, K):
        super().__init__()
        self.d, self.K = d, K
        def pk(*shape):
            t = torch.empty(*shape); nn.init.xavier_uniform_(t.view(shape[0], -1))
            return nn.Parameter(t)
        self.Wq = pk(K, 3 * d, d); self.Wk = pk(K, 3 * d, d); self.Wv = pk(K, 3 * d, d)
        self.T1 = pk(K, 4 * d, 2 * d); self.T2 = pk(K, 2 * d, d)
        self.Wg = pk(K, d, d)
        self.gb = nn.Parameter(torch.zeros(K, d))            # gate bias ~0 -> gate ~0.5
        self.ln = nn.LayerNorm(d)

    def forward(self, w, feat, extra=None):
        h = torch.cat([self.ln(w), feat], dim=-1)            # [..., n, 3d]
        if extra is not None:
            h = h + F.pad(extra, (0, 2 * self.d))            # condition content channel
        q = torch.einsum("...nf,kfd->...knd", h, self.Wq)
        k = torch.einsum("...nf,kfd->...knd", h, self.Wk)
        v = torch.einsum("...nf,kfd->...knd", h, self.Wv)
        att = torch.einsum("...knd,...kmd->...knm", q, k) / math.sqrt(self.d)
        r = torch.einsum("...knm,...kmd->...knd", att.softmax(-1), v)
        z = torch.cat([r, self.ln(w).unsqueeze(-3).expand_as(r),
                       feat.unsqueeze(-3).expand(*r.shape[:-1], 2 * self.d)], dim=-1)
        z = torch.einsum("...knf,kfe->...kne", F.gelu(
            torch.einsum("...knf,kfe->...kne", z, self.T1)), self.T2)
        g = torch.sigmoid(torch.einsum("...knd,kde->...kne", z, self.Wg)
                          + self.gb.view(*([1] * (z.dim() - 3)), self.K, 1, self.d))
        return g * torch.tanh(z)                              # u

class Base(nn.Module):
    def __init__(self, d=48, K=8):
        super().__init__()
        self.d, self.K = d, K
        self.sym = nn.Embedding(V + 1, d)                     # +1 blank
        self.pos = nn.Embedding(N_SLOTS, d)
        self.route = nn.Embedding(C_VOCAB, K)                 # routing table A
        self.core = OperatorCore(d, K)
        self.out = nn.Sequential(nn.LayerNorm(d), nn.Linear(d, 2 * d),
                                 nn.GELU(), nn.Linear(2 * d, V))
        self.tau = 1.0

    def embed(self, X):
        e = F.normalize(self.sym(X), dim=-1) * math.sqrt(self.d)
        p = self.pos(torch.arange(N_SLOTS, device=X.device)).expand_as(e)
        return e, torch.cat([e, p], dim=-1)                   # w0, feat

    def rho(self, C):                                         # [B, M, K]
        return F.softmax(self.route(C) / self.tau, dim=-1)

    def readout(self, w):
        return self.out(w)                                    # [B, n, V]

class Scheduled(Base):
    def forward(self, C, X):
        w, feat = self.embed(X)
        beta = self.rho(C)                                    # [B, L, K]
        for t in range(C.shape[1]):
            u = self.core(w, feat)                            # [B, K, n, d]
            w = w + torch.einsum("bk,bknd->bnd", beta[:, t], u)
        return self.readout(w)

class FixedPoint(Base):
    def __init__(self, d=48, K=8, sweeps=8, alpha=0.5):
        super().__init__(d, K)
        self.sweeps, self.alpha = sweeps, alpha
        self.step = nn.Embedding(L_MAX, d)                    # step embedding s_m

    def field(self, w, feat, C, P):
        s = self.step(P).unsqueeze(2)                         # [B, M, 1, d]
        u = self.core(w.unsqueeze(1), feat.unsqueeze(1), extra=s)   # [B, M, K, n, d]
        beta = self.rho(C)                                    # [B, M, K]
        return w + torch.einsum("bmk,bmknd->bnd", beta, u) / C.shape[1]

    def forward(self, C, X, P=None, return_resid=False):
        w, feat = self.embed(X)
        if P is None:
            P = torch.arange(C.shape[1], device=C.device).expand(C.shape[0], -1)
        resid = []
        for _ in range(self.sweeps):
            wn = (1 - self.alpha) * w + self.alpha * self.field(w, feat, C, P)
            resid.append((wn - w).norm(dim=(-2, -1)) / w.norm(dim=(-2, -1)))
            w = wn
        out = self.readout(w)
        return (out, torch.stack(resid, 1)) if return_resid else out

class Itinerant(Base):
    def __init__(self, d=48, K=8, steps=70, dt=0.2, noise=0.02,
                 fatigue_tau=6.0, fatigue_k=1.5, leak=0.02, fixed_chain=False,
                 normalize_activity=False, activity_gain=1.0,
                 activity_epsilon=1e-6, mode_specific_fitness=False,
                 fitness_features=("workspace", "command", "position",
                                   "interaction")):
        super().__init__(d, K)
        self.S, self.dt, self.noise = steps, dt, noise
        self.ftau, self.fk, self.leak = fatigue_tau, fatigue_k, leak
        self.normalize_activity = normalize_activity
        self.activity_gain = activity_gain
        self.activity_epsilon = activity_epsilon
        self.mode_specific_fitness = mode_specific_fitness
        self.fitness_features = frozenset(fitness_features)
        self.M = L_MAX
        self.sigma = nn.Sequential(nn.LayerNorm(d), nn.Linear(d, d), nn.GELU(),
                                   nn.Linear(d, 1))
        self.sig_cmd = nn.Embedding(C_VOCAB, 1)               # per-token fitness bias
        nn.init.zeros_(self.sig_cmd.weight)
        self.sig_scale = nn.Parameter(torch.tensor(0.5))
        self.fitness_cmd = nn.Embedding(C_VOCAB, d)
        self.fitness_pos = nn.Embedding(L_MAX, d)
        self.mode_sigma = nn.Sequential(
            nn.LayerNorm(4 * d), nn.Linear(4 * d, d), nn.GELU(),
            nn.Linear(d, 1),
        )
        self.base, self.ord = 3.0, 0.1                       # tuned below
        self.pool_q = nn.Parameter(torch.randn(d) / math.sqrt(d))
        rho0 = torch.full((self.M, self.M), 2.5)              # strong mutual inhibition
        if fixed_chain:                                       # hand-built successor chain
            for m in range(self.M):
                rho0[m, m] = 1.0
                if m + 1 < self.M:
                    rho0[m + 1, m] = 0.35                     # successor feels little from m -> can invade
                    rho0[m, m + 1] = 4.0                      # m feels much from successor -> dies
        else:
            rho0 += 0.1 * torch.randn(self.M, self.M)
            rho0.fill_diagonal_(1.0)
        self.rho_raw = nn.Parameter(torch.log(torch.expm1(rho0)))  # inv-softplus
        self.rho_raw.requires_grad = not fixed_chain

    def fitness(self, w, C, P=None):
        if P is None:
            P = torch.arange(C.shape[1], device=C.device).expand(C.shape[0], -1)
        attn = torch.einsum("bnd,d->bn", w, self.pool_q).softmax(-1)
        pooled = torch.einsum("bn,bnd->bd", attn, w)
        if self.mode_specific_fitness:
            cmd = self.fitness_cmd(C)
            pos = self.fitness_pos(P)
            z = torch.cat([
                pooled.unsqueeze(1).expand_as(cmd)
                if "workspace" in self.fitness_features else torch.zeros_like(cmd),
                cmd if "command" in self.fitness_features else torch.zeros_like(cmd),
                pos if "position" in self.fitness_features else torch.zeros_like(pos),
                pooled.unsqueeze(1) * cmd
                if "interaction" in self.fitness_features else torch.zeros_like(cmd),
            ], dim=-1)
            learned = self.mode_sigma(z).squeeze(-1)
            return self.base + self.sig_scale * learned
        learned = self.sigma(pooled) + self.sig_cmd(C).squeeze(-1)
        return self.base + self.sig_scale * learned - self.ord * P.float()
    def forward(self, C, X, P=None, return_traj=False, return_diagnostics=False,
                activity_override=None):
        B = C.shape[0]; dev = C.device
        w, feat = self.embed(X)
        a = torch.full((B, self.M), 0.05, device=dev)
        a[:, 0] = 1.0                                          # enter channel at station 0
        # Evaluation must be bitwise deterministic.  Training retains the
        # independent random entry perturbation used by the supplied model.
        if self.training:
            a = a + 0.01 * torch.randn_like(a).abs()
        f = torch.zeros_like(a)
        rho_m = F.softplus(self.rho_raw)
        beta_cmd = self.rho(C)                                # [B, M, K]
        traj = []
        update_norms = []
        if activity_override is not None and activity_override.shape[1] != self.S:
            raise ValueError("activity_override must have one row per controller step")
        for t in range(self.S):
            if activity_override is None:
                fit = self.fitness(w, C, P) - self.fk * f
                comp = torch.einsum("mj,bj->bm", rho_m, a)
                noise = self.noise * torch.randn_like(a) if self.training else 0.0
                a = (a + self.dt * a * (fit - comp) + noise).clamp(0.05, 4.0)
                f = f + self.dt / self.ftau * (a - f)
            else:
                a = activity_override[:, t]
            beta = torch.einsum("bm,bmk->bk", a, beta_cmd)    # [B, K]
            if self.normalize_activity:
                beta = self.activity_gain * beta / (
                    self.activity_epsilon + a.sum(dim=-1, keepdim=True)
                )
            u = self.core(w, feat)
            delta = self.dt * (torch.einsum("bk,bknd->bnd", beta, u) - self.leak * w)
            w = w + delta
            if return_traj or return_diagnostics:
                traj.append(a if return_traj and not return_diagnostics
                            else a.detach().clone())
            if return_diagnostics:
                update_norms.append(delta.detach().norm(dim=(-2, -1)))
        out = self.readout(w)
        if return_diagnostics:
            return out, {
                "activity": torch.stack(traj, 1),
                "workspace_update_norm": torch.stack(update_norms, 1),
            }
        return (out, torch.stack(traj, 1)) if return_traj else out


def direction_free_channel_penalties(activity, mass_target=2.0,
                                     switch_target=0.08):
    """Permutation-invariant channel penalties; no successor pair is named.

    activity has shape [batch, time, mode].  Every term is differentiable and
    invariant to a common permutation of the mode axis.
    """
    pair_mass = (
        activity.sum(-1).square() - activity.square().sum(-1)
    ).clamp_min(0.0)
    overlap = pair_mass.mean()
    step_change = (activity[:, 1:] - activity[:, :-1]).abs().mean(-1)
    switching = (switch_target - step_change).clamp_min(0.0).mean()
    if activity.shape[1] > 2:
        revisit = (activity[:, 2:] * activity[:, :-2]).sum(-1).mean()
    else:
        revisit = activity.new_zeros(())
    tail = activity[:, -min(10, activity.shape[1]):]
    terminal_trapping = 1.0 / (tail.var(1, unbiased=False).mean() + 1e-4)
    activity_mass = (activity.sum(-1).mean() - mass_target).square()
    return {
        "overlap": overlap,
        "switching_progress": switching,
        "revisit": revisit,
        "terminal_trapping": terminal_trapping,
        "activity_mass": activity_mass,
    }
