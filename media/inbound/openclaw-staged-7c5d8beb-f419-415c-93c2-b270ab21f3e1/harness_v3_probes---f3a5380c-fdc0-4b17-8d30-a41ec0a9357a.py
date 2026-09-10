"""harness_v3_probes.py -- intervention probes derived from the Oruzi boundary
theorems, for the CAROM experimental program.

New instruments (each keyed to the theorem that licenses it):

  1. phase_map / swap_discrepancy    -- "compositionality is commutation":
     exact nonlinear order-sensitivity of two command phases, the ground truth
     the affine theorem linearizes. (affinePhases_orderIndependent_iff)
  2. commutator_energy               -- linearized pairwise interference energy
     ||[J_a, J_b]||_F^2 estimated stochastically via JVP probes -- the
     interference-Gram diagnostic, computed by intervention as the telemetry
     non-identifiability results require.
     (linearPhases_orderIndependent_iff_interferenceEnergy_zero)
  3. tau_three_hypothesis_sweep      -- runs repaired itinerary metrics,
     causal_gap, and mean interference energy across a list of checkpoints;
     discriminates (a) mechanistic drift, (b) metric artifact,
     (c) learned commutation ("order stops mattering").
  4. schedule_stability_probe        -- "stability does not compose":
     adversarial alternation + random-product growth-rate estimate (joint
     spectral radius proxy) over the learned phase family.
     (individuallyStable_switchingDiverges)
  5. cross_slot_coupling_probe       -- the one quantity that licenses typed
     slots, provably not identifiable from logs; perturbation-based.
     (crossSlotHessian_not_identifiable)
  6. decisiveness_report             -- routing/control entropies; "fit does
     not imply guidance" bookkeeping.
     (equal_crossEntropy_strictly_ordered_expectedYield)

All probes are read-only over trained checkpoints. Sandbox scale runs on CPU;
raise probe counts on GPU.
"""
import math, random
import torch, torch.nn.functional as F

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# ---------------------------------------------------------------------------
# 1. Differentiable single-phase executor and exact swap discrepancy
# ---------------------------------------------------------------------------
def phase_map(model, w, feat, beta_k, steps=12, amp=1.5):
    """Run `steps` workspace updates under a fixed operator mixture beta_k
    (one command phase, control clamped at amplitude amp). Differentiable."""
    for _ in range(steps):
        u = model.core(w, feat)
        w = w + model.dt * (amp * torch.einsum("bk,bknd->bnd", beta_k, u)
                            - model.leak * w)
    return w

def _cmd_beta(model, H, m):
    """Operator mixture for command slot m from the routing hypernetwork."""
    return F.softmax(model.hyper(H[:, m]), -1)                 # [B, K]

def swap_discrepancy(model, lm, split, exp2, pairs_per_ex=1, steps=12,
                     seed=0, n=64):
    """Exact nonlinear order-sensitivity: || Phi_b(Phi_a(w)) - Phi_a(Phi_b(w)) ||
    / ||w||, averaged over live command pairs. This is the quantity the affine
    swap formula [B,A]x + (Ba+b-Ab-a) linearizes."""
    rng = random.Random(seed); model.eval()
    T, SP, X, ORD = split["T"][:n], split["SP"][:n], split["X"][:n], split["ORD"][:n]
    H = exp2.span_reps(lm, T, SP)
    e = F.normalize(model.sym(X), dim=-1) * math.sqrt(model.d)
    p = model.pos(torch.arange(X.shape[1], device=X.device)).expand_as(e)
    feat = torch.cat([e, p], -1)
    out = []
    with torch.no_grad():
        for b in range(n):
            live = [m for m in range(ORD.shape[1]) if ORD[b, m] >= 0]
            for _ in range(pairs_per_ex):
                a_, b_ = rng.sample(live, 2)
                w0 = e[b:b+1]
                fa, fb = (_cmd_beta(model, H[b:b+1], a_),
                          _cmd_beta(model, H[b:b+1], b_))
                ab = phase_map(model, phase_map(model, w0, feat[b:b+1], fa, steps),
                               feat[b:b+1], fb, steps)
                ba = phase_map(model, phase_map(model, w0, feat[b:b+1], fb, steps),
                               feat[b:b+1], fa, steps)
                out.append(((ab - ba).norm() / w0.norm()).item())
    t = torch.tensor(out)
    return {"mean": t.mean().item(), "median": t.median().item(),
            "p90": t.quantile(0.9).item(), "n_pairs": len(out)}

# ---------------------------------------------------------------------------
# 2. Linearized interference energy via JVP probes
# ---------------------------------------------------------------------------
def _jvp_phase(model, w0, feat, beta_k, v, steps):
    """J_phase(w0) @ v via forward-mode AD."""
    from torch.func import jvp
    f = lambda w: phase_map(model, w, feat, beta_k, steps)
    _, tangent = jvp(f, (w0,), (v,))
    return tangent

def commutator_energy(model, lm, split, exp2, n=32, probes=4, steps=12, seed=0):
    """Stochastic estimate of E_v || (J_a J_b - J_b J_a) v ||^2 / ||v||^2 over
    live command pairs -- the pairwise interference-Gram diagonal, normalized.
    Requires intervention (JVPs of the phase maps), per the identifiability
    results: this quantity cannot be recovered from ordinary logs."""
    rng = random.Random(seed); model.eval()
    T, SP, X, ORD = split["T"][:n], split["SP"][:n], split["X"][:n], split["ORD"][:n]
    H = exp2.span_reps(lm, T, SP)
    e = F.normalize(model.sym(X), dim=-1) * math.sqrt(model.d)
    p = model.pos(torch.arange(X.shape[1], device=X.device)).expand_as(e)
    feat = torch.cat([e, p], -1)
    vals = []
    for b in range(n):
        live = [m for m in range(ORD.shape[1]) if ORD[b, m] >= 0]
        a_, b_ = rng.sample(live, 2)
        w0 = e[b:b+1]
        fa, fb = _cmd_beta(model, H[b:b+1], a_), _cmd_beta(model, H[b:b+1], b_)
        for _ in range(probes):
            v = torch.randn_like(w0); v = v / v.norm()
            jab = _jvp_phase(model, w0, feat[b:b+1], fa,
                             _jvp_phase(model, w0, feat[b:b+1], fb, v, steps), steps)
            jba = _jvp_phase(model, w0, feat[b:b+1], fb,
                             _jvp_phase(model, w0, feat[b:b+1], fa, v, steps), steps)
            vals.append((jab - jba).norm().pow(2).item())
    t = torch.tensor(vals)
    return {"mean_interference": t.mean().item(),
            "median": t.median().item(), "n": len(vals)}

# ---------------------------------------------------------------------------
# 3. The tau three-hypothesis sweep
# ---------------------------------------------------------------------------
def tau_three_hypothesis_sweep(ckpt_paths, lm, split, exp2, harness,
                               make_model, steps=12):
    """For each checkpoint: repaired itinerary metrics + causal_gap +
    interference energy + swap discrepancy. Interpretation:
      drift        : coverage/exact fall, causal_gap falls, interference HIGH
      metric-only  : coverage stays high once measured properly
      commutation  : coverage/exact fall AND interference falls in lockstep
                     (order stops mattering; channel dissolves harmlessly)"""
    rows = []
    for path in ckpt_paths:
        model = make_model()
        st = torch.load(path, weights_only=False)
        model.load_state_dict(st["m"] if "m" in st else st); model.eval()
        rep = harness.eval_checkpoint(model, lm, split)
        iv = harness.intervention_suite(model, lm, split)
        ie = commutator_energy(model, lm, split, exp2, steps=steps)
        sd = swap_discrepancy(model, lm, split, exp2, steps=steps)
        rows.append({"ckpt": path, "task_acc": rep["task_acc"],
                     "tau": rep["itinerary"]["tau"],
                     "coverage": rep["itinerary"]["coverage"],
                     "exact_order": rep["itinerary"]["exact_order"],
                     "causal_gap": round(iv["causal_gap"], 4),
                     "interference": round(ie["mean_interference"], 5),
                     "swap_disc": round(sd["median"], 5)})
    return rows

# ---------------------------------------------------------------------------
# 4. Schedule stability: adversarial alternation + random-product growth
# ---------------------------------------------------------------------------
def schedule_stability_probe(model, lm, split, exp2, n=16, alt_len=24,
                             prod_len=12, probes=6, steps=6, seed=0):
    """(a) Adversarial two-command alternation for alt_len phases: measures
    workspace norm growth vs the natural trajectory (switching-divergence
    check). (b) Random products of phase-map JVPs: growth rate estimate
    ~ joint spectral radius proxy of the learned phase family."""
    rng = random.Random(seed); model.eval()
    T, SP, X, ORD = split["T"][:n], split["SP"][:n], split["X"][:n], split["ORD"][:n]
    H = exp2.span_reps(lm, T, SP)
    e = F.normalize(model.sym(X), dim=-1) * math.sqrt(model.d)
    p = model.pos(torch.arange(X.shape[1], device=X.device)).expand_as(e)
    feat = torch.cat([e, p], -1)
    growths, rates = [], []
    with torch.no_grad():
        for b in range(n):
            live = [m for m in range(ORD.shape[1]) if ORD[b, m] >= 0]
            a_, b_ = rng.sample(live, 2)
            w = e[b:b+1]
            fa, fb = _cmd_beta(model, H[b:b+1], a_), _cmd_beta(model, H[b:b+1], b_)
            n0 = w.norm().item()
            for i in range(alt_len):
                w = phase_map(model, w, feat[b:b+1], fa if i % 2 == 0 else fb,
                              steps)
            growths.append(w.norm().item() / n0)
    for b in range(min(n, 8)):
        live = [m for m in range(ORD.shape[1]) if ORD[b, m] >= 0]
        w0 = e[b:b+1]
        for _ in range(probes):
            v = torch.randn_like(w0); v = v / v.norm()
            for _ in range(prod_len):
                m = rng.choice(live)
                fm = _cmd_beta(model, H[b:b+1], m)
                v = _jvp_phase(model, w0, feat[b:b+1], fm, v, steps)
            rates.append(v.norm().item() ** (1.0 / prod_len))
    g = torch.tensor(growths); r = torch.tensor(rates)
    return {"alt_growth_median": g.median().item(),
            "alt_growth_max": g.max().item(),
            "jsr_proxy_median": r.median().item(),
            "jsr_proxy_p90": r.quantile(0.9).item(),
            "verdict": "stable" if r.quantile(0.9).item() < 1.0
                       else "NOT schedule-uniform stable"}

# ---------------------------------------------------------------------------
# 5. Cross-slot coupling probe (licenses -- or refuses -- typed-slot reading)
# ---------------------------------------------------------------------------
def cross_slot_coupling_probe(model, lm, split, exp2, n=48, eps=0.25, seed=0):
    """Perturb slot j's initial content; measure per-slot readout change.
    Returns the normalized coupling matrix C[i,j] (effect on slot i of
    perturbing slot j) and its off-diagonal mass. Per the identifiability
    theorem this cannot be read from logs -- only from this intervention."""
    torch.manual_seed(seed); model.eval()
    T, SP, X, Y, ORD = (split["T"][:n], split["SP"][:n], split["X"][:n],
                        split["Y"][:n], split["ORD"][:n])
    H = exp2.span_reps(lm, T, SP)
    live = (ORD >= 0).float()
    nslots = X.shape[1]
    with torch.no_grad():
        base, _, _ = model(H, X, live)
        base = base.softmax(-1)
        C = torch.zeros(nslots, nslots)
        for j in range(nslots):
            e = F.normalize(model.sym(X), dim=-1) * math.sqrt(model.d)
            delta = torch.zeros_like(e); delta[:, j] = eps * torch.randn_like(e[:, j])
            # rerun with perturbed evidence for slot j
            pert, _, _ = _forward_with_evidence(model, H, X, live, e + delta)
            C[:, j] = (pert.softmax(-1) - base).abs().mean((0, 2))
    C = C / C.sum()
    off = (C.sum() - C.diag().sum()).item()
    return {"coupling_matrix": C, "offdiag_mass": round(off, 4),
            "typed_slot_license": "coupled -- joint treatment required"
                                   if off > 0.5 else
                                   "weak coupling -- per-slot reading licensed"}

def _forward_with_evidence(model, H, X, live, e):
    p = model.pos(torch.arange(X.shape[1], device=X.device)).expand_as(e)
    w, feat = e, torch.cat([e, p], -1)
    beta_cmd = F.softmax(model.hyper(H), -1)
    rho, el = model.compile_rho(H, live)
    ent = model.entry(H).squeeze(-1) - 30.0 * (1 - live)
    a = 0.05 + 0.95 * F.softmax(ent, -1)
    f = torch.zeros_like(a)
    P = torch.arange(a.shape[1], device=a.device).float()
    for t in range(model.S):
        attn = torch.einsum("bnd,d->bn", w, model.pool_q).softmax(-1)
        pooled = torch.einsum("bn,bnd->bd", attn, w)
        fit = model.base + model.sig_scale * (model.sigma(pooled)) \
              - model.fk * f - 10.0 * (1 - live)
        comp = torch.einsum("bmj,bj->bm", rho, a)
        a = (a + model.dt * a * (fit - comp)).clamp(0.05, 4.0)
        f = f + model.dt / model.ftau * (a - f)
        beta = torch.einsum("bm,bmk->bk", a * live, beta_cmd)
        u = model.core(w, feat)
        w = w + model.dt * (torch.einsum("bk,bknd->bnd", beta, u)
                            - model.leak * w)
    return model.out(w), el, None

# ---------------------------------------------------------------------------
# 6. Decisiveness bookkeeping
# ---------------------------------------------------------------------------
def decisiveness_report(model, lm, split, exp2, n=256):
    """Routing entropy per command + control-state entropy over time.
    Report beside loss/accuracy always: fit does not imply guidance."""
    model.eval()
    T, SP, X, ORD = split["T"][:n], split["SP"][:n], split["X"][:n], split["ORD"][:n]
    H = exp2.span_reps(lm, T, SP)
    live = (ORD >= 0).float()
    with torch.no_grad():
        r = F.softmax(model.hyper(H), -1)
        Hr = -(r * r.clamp(min=1e-9).log()).sum(-1)
        _, _, traj = model(H, X, live, return_traj=True)
        an = traj / traj.sum(-1, keepdim=True).clamp(min=1e-9)
        Ha = -(an * an.clamp(min=1e-9).log()).sum(-1)
    return {"routing_entropy_mean": round(Hr[live.bool()].mean().item(), 4),
            "routing_entropy_max_uniform": round(math.log(r.shape[-1]), 4),
            "control_entropy_mean": round(Ha.mean().item(), 4),
            "control_entropy_final": round(Ha[:, -1].mean().item(), 4)}
