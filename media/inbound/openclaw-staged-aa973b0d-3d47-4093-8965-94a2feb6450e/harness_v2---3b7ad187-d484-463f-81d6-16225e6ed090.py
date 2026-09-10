"""harness_v2.py -- repaired instruments for CAROM Exp2/Exp3.

Addresses the audit's Priority-0 items:
  1. Frozen corpora: deterministic splits, independent RNG streams, example IDs.
  2. Validated itinerary metrics: station coverage, transition precision/recall,
     exact-order rate, Kendall tau, dwell stats, revisit count -- with a
     SELF-TEST on constructed positive/negative trajectories.
  3. Edge metrics: AUROC, AUPRC, positive recall@0.5, exact-graph accuracy
     (no sklearn dependency).
  4. Trajectory INTERVENTION executor: run the compiled-channel workspace under
     externally clamped control states (forced-correct / shuffled / smeared /
     natural) and compare endpoint accuracy -- the causal probe.
  5. Test-time budget sweep: evaluate at multiple integration depths S.
  6. Exp3 paired M2: identical old-program corpus before/after registration,
     with routing-vs-operator error decomposition.

Usage (Exp2):
    from harness_v2 import *
    corp = build_corpora(seed=1234)              # or load_corpora(path)
    rep  = eval_checkpoint(model, lm, corp["val_L24"])          # metrics
    iv   = intervention_suite(model, lm, corp["val_L24"])       # causal probe
    sw   = budget_sweep(model, lm, corp["val_L5"], Ss=[72,110,150])
Self-test:  python harness_v2.py --selftest
"""
import math, random, argparse
import torch, torch.nn.functional as F

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# ---------------------------------------------------------------------------
# 1. FROZEN CORPORA  (wraps exp2's generator with dedicated RNG per split)
# ---------------------------------------------------------------------------
def build_corpora(seed=1234, exp2_module=None, sizes=None):
    """Each split gets its own random.Random(seed+offset); example id =
    (split, index). Saved as plain tensors so all arms share bytes."""
    import exp2_compiled_channel as E2
    E2 = exp2_module or E2
    sizes = sizes or {"val_L24": 512, "test_L24": 512, "val_L5": 256, "test_L5": 256}
    out = {}
    offs = {"val_L24": 1, "test_L24": 2, "val_L5": 3, "test_L5": 4}
    for name, n in sizes.items():
        rng = random.Random(seed + 1000 * offs[name])
        fl = 5 if name.endswith("L5") else None
        lr = (2, 4)
        out[name] = dict(zip(
            ["T","SP","X","Y","E","ENT","ORD","Ls"],
            E2.make_batch(n, rng, fixed_len=fl, len_range=lr)))
        out[name]["ids"] = [f"{name}:{i}" for i in range(n)]
    return out

def save_corpora(corp, path):  torch.save(corp, path)
def load_corpora(path):        return torch.load(path, weights_only=False)

# ---------------------------------------------------------------------------
# 2. ITINERARY METRICS (validated)
# ---------------------------------------------------------------------------
def _phases_with_dwell(traj_b, live_mask):
    """traj_b [S, M] -> (sequence of live modes, dwell steps per phase)."""
    am = traj_b.argmax(-1).tolist()
    seq, dwell = [], []
    for m in am:
        if not live_mask[m]:
            continue
        if seq and seq[-1] == m:
            dwell[-1] += 1
        else:
            seq.append(m); dwell.append(1)
    return seq, dwell

def itinerary_metrics(traj_b, ord_b):
    """ord_b [M]: topological rank of each mode; -1 = padded/absent.
    True order = modes sorted by rank. Returns dict of per-example metrics."""
    live = [(r >= 0) for r in ord_b.tolist()]
    ranks = {m: r for m, r in enumerate(ord_b.tolist()) if r >= 0}
    L = len(ranks)
    true_seq = [m for m, _ in sorted(ranks.items(), key=lambda kv: kv[1])]
    seq, dwell = _phases_with_dwell(traj_b, live)
    uniq = list(dict.fromkeys(seq))
    coverage = len(set(uniq)) / max(1, L)
    # transitions (in mode space): predicted consecutive unique pairs
    pred_tr = set(zip(uniq[:-1], uniq[1:]))
    true_tr = set(zip(true_seq[:-1], true_seq[1:]))
    tp = len(pred_tr & true_tr)
    prec = tp / max(1, len(pred_tr))
    rec = tp / max(1, len(true_tr))
    exact = float(uniq == true_seq)
    # kendall on the ranks of the visited unique modes
    rs = [ranks[m] for m in uniq]
    if len(rs) < 2:
        tau = 0.0
    else:
        c = sum(rs[i] < rs[j] for i in range(len(rs)) for j in range(i+1, len(rs)))
        d = sum(rs[i] > rs[j] for i in range(len(rs)) for j in range(i+1, len(rs)))
        tau = (c - d) / max(1, c + d)
    revisits = len(seq) - len(uniq)
    return {"coverage": coverage, "trans_prec": prec, "trans_rec": rec,
            "exact_order": exact, "tau": tau,
            "mean_dwell": sum(dwell)/max(1,len(dwell)), "revisits": revisits}

def itinerary_report(traj, ORD):
    ms = [itinerary_metrics(traj[b], ORD[b]) for b in range(traj.shape[0])]
    return {k: sum(m[k] for m in ms)/len(ms) for k in ms[0]}

def _selftest_itinerary():
    """Constructed positive/negative trajectories; asserts the audit's
    failure case (ordered-subset -> old tau 1.0) is now flagged."""
    S, M = 40, 4
    ORD = torch.tensor([0,1,2,3])                 # true order = 0,1,2,3
    def mk(seq_dwells):
        t = torch.zeros(S, M); i = 0
        for m, d in seq_dwells:
            t[i:i+d, m] = 1.0; i += d
        t[i:, seq_dwells[-1][0]] = 1.0
        return t
    perfect  = mk([(0,10),(1,10),(2,10),(3,10)])
    subset   = mk([(0,20),(2,20)])                # ordered but half-covered
    reversed_= mk([(3,10),(2,10),(1,10),(0,10)])
    smeared  = torch.full((S, M), 0.25)
    for name, t, expect in [
        ("perfect",  perfect,  dict(coverage=1.0, exact_order=1.0, tau=1.0)),
        ("subset",   subset,   dict(coverage=0.5, exact_order=0.0, tau=1.0)),
        ("reversed", reversed_,dict(coverage=1.0, exact_order=0.0, tau=-1.0)),
    ]:
        m = itinerary_metrics(t, ORD)
        for k, v in expect.items():
            assert abs(m[k]-v) < 1e-6, (name, k, m)
        print(f"  selftest[{name}]: {m}")
    m = itinerary_metrics(smeared, ORD)
    assert m["coverage"] <= 0.26 and m["exact_order"] == 0.0
    print(f"  selftest[smeared]: {m}")
    print("  KEY: 'subset' has tau=1.0 but coverage=0.5 / exact=0 -> the old",
          "tau-only reading is repaired.")

# ---------------------------------------------------------------------------
# 3. EDGE METRICS (no sklearn)
# ---------------------------------------------------------------------------
def edge_metrics(el, E, live):
    """el: logits [B,M,M]; E: 0/1 targets; live: [B,M]."""
    M = E.shape[-1]
    pair = (live.unsqueeze(1)*live.unsqueeze(2) *
            (1-torch.eye(M, device=E.device)[None])).bool()
    s = torch.sigmoid(el[pair]).detach().cpu()
    y = E[pair].detach().cpu()
    order = torch.argsort(s, descending=True)
    y_sorted = y[order]
    P = y.sum().item(); N = len(y) - P
    # AUROC via rank statistic
    ranks = torch.empty_like(order, dtype=torch.float)
    ranks[order] = torch.arange(len(y), dtype=torch.float)
    auroc = ((len(y)-1-ranks)[y.bool()].sum().item() - P*(P-1)/2) / max(1, P*N)
    # AUPRC via precision at each positive hit
    tp = torch.cumsum(y_sorted, 0)
    prec_at = tp / torch.arange(1, len(y)+1)
    auprc = (prec_at[y_sorted.bool()].sum().item() / max(1, P))
    pos_rec = ((s > 0.5) & y.bool()).sum().item() / max(1, P)
    # exact graph: per example, all live pairs thresholded correct
    hard = (torch.sigmoid(el) > 0.5).float()
    ok = ((hard == E) | ~pair).all(-1).all(-1).float().mean().item()
    return {"auroc": auroc, "auprc": auprc, "pos_recall@.5": pos_rec,
            "exact_graph": ok, "pos_rate": P/max(1,len(y))}

# ---------------------------------------------------------------------------
# 4. INTERVENTION EXECUTOR  (clamped control states)
# ---------------------------------------------------------------------------
def _clamped_traj(mode, ORD_b, S, M, amp=1.5, rng=None):
    live = [m for m in range(M) if ORD_b[m] >= 0]
    if mode == "smeared":
        t = torch.zeros(S, M); t[:, live] = amp/len(live); return t
    if mode == "forced":
        order = sorted(live, key=lambda m: ORD_b[m].item())
    elif mode == "shuffled":
        order = live[:]; rng.shuffle(order)
        if len(order) > 1 and order == sorted(live, key=lambda m: ORD_b[m].item()):
            order = order[::-1]                    # guarantee wrong order
    t = torch.zeros(S, M); seg = S // len(order)
    for i, m in enumerate(order):
        t[i*seg:(i+1)*seg if i < len(order)-1 else S, m] = amp
    return t

def run_clamped(model, H, X, ORD, a_traj):
    """Workspace dynamics with control clamped to a_traj [B,S,M]."""
    with torch.no_grad():
        B = H.shape[0]
        e = F.normalize(model.sym(X), dim=-1) * math.sqrt(model.d)
        p = model.pos(torch.arange(X.shape[1], device=X.device)).expand_as(e)
        w, feat = e, torch.cat([e, p], -1)
        beta_cmd = F.softmax(model.hyper(H), -1)
        live = (ORD >= 0).float()
        for t in range(a_traj.shape[1]):
            beta = torch.einsum("bm,bmk->bk", a_traj[:, t]*live, beta_cmd)
            u = model.core(w, feat)
            w = w + model.dt*(torch.einsum("bk,bknd->bnd", beta, u)
                              - model.leak*w)
        return model.out(w)

def intervention_suite(model, lm, split, seed=7, amp=1.5):
    import exp2_compiled_channel as E2
    model.eval(); rng = random.Random(seed)
    T, X, Y, ORD = split["T"], split["X"], split["Y"], split["ORD"]
    H = E2.span_reps(lm, T, split["SP"])
    live = (ORD >= 0).float()
    res = {}
    with torch.no_grad():
        out, _, traj = model(H, X, live, return_traj=True)
        res["natural"] = (out.argmax(-1) == Y).float().mean().item()
    S, M = model.S, ORD.shape[1]
    for mode in ["forced", "shuffled", "smeared"]:
        A = torch.stack([_clamped_traj(mode, ORD[b], S, M, amp, rng)
                         for b in range(ORD.shape[0])]).to(DEVICE)
        out = run_clamped(model, H, X, ORD, A)
        res[mode] = (out.argmax(-1) == Y).float().mean().item()
    res["causal_gap"] = res["forced"] - res["shuffled"]
    return res

# ---------------------------------------------------------------------------
# 5. BUDGET SWEEP
# ---------------------------------------------------------------------------
def budget_sweep(model, lm, split, Ss=(72, 110, 150)):
    import exp2_compiled_channel as E2
    model.eval(); out = {}
    H = E2.span_reps(lm, split["T"], split["SP"])
    live = (split["ORD"] >= 0).float()
    S0 = model.S
    with torch.no_grad():
        for S in Ss:
            model.S = S
            o, _, traj = model(H, split["X"], live, return_traj=True)
            acc = (o.argmax(-1) == split["Y"]).float().mean().item()
            it = itinerary_report(traj, split["ORD"])
            out[S] = {"acc": acc, **{k: round(v,3) for k,v in it.items()}}
    model.S = S0
    return out

# ---------------------------------------------------------------------------
# 6. FULL CHECKPOINT REPORT (Exp2)
# ---------------------------------------------------------------------------
def eval_checkpoint(model, lm, split):
    import exp2_compiled_channel as E2
    model.eval()
    H = E2.span_reps(lm, split["T"], split["SP"])
    live = (split["ORD"] >= 0).float()
    with torch.no_grad():
        out, el, traj = model(H, split["X"], live, return_traj=True)
        acc = (out.argmax(-1) == split["Y"]).float().mean().item()
    return {"task_acc": round(acc, 4),
            "edges": {k: round(v,4) for k,v in
                      edge_metrics(el, split["E"], live).items()},
            "itinerary": {k: round(v,4) for k,v in
                          itinerary_report(traj, split["ORD"]).items()}}

# ---------------------------------------------------------------------------
# 7. EXP3 PAIRED M2 (routing-vs-operator decomposition)
# ---------------------------------------------------------------------------
def paired_m2(cap_before, cap_after, lm, exp3_module, seed=4321, n=512,
              route_tau=0.10):
    """Same frozen old-program corpus through both models. Decomposes flipped
    examples by whether >=route_tau routing mass moved onto new slots."""
    E3 = exp3_module
    rng = random.Random(seed)
    T, SP, PR, X, Y = E3.make_batch(n, rng, prim_pool=list(range(E3.N_OLD)))
    H = E3.span_reps(lm, T, SP)
    outs, routes = [], []
    for m in (cap_before, cap_after):
        m.eval()
        with torch.no_grad():
            outs.append(m(H, PR, X).argmax(-1))
            r = m.route(H)                                   # [B,L,K+n_new]
            new_mass = (r[..., E3.K:].sum(-1) if r.shape[-1] > E3.K
                        else torch.zeros(r.shape[:-1], device=r.device))
            routes.append(new_mass.max(-1).values)           # worst slot leak
    ok_b = (outs[0] == Y).float().mean(-1)
    ok_a = (outs[1] == Y).float().mean(-1)
    flipped = (ok_b - ok_a) > 1e-6
    leak = routes[1] > route_tau
    n_f = flipped.sum().item()
    return {"acc_before": round(ok_b.mean().item(), 4),
            "acc_after": round(ok_a.mean().item(), 4),
            "paired_delta": round((ok_a-ok_b).mean().item(), 4),
            "examples_degraded": int(n_f),
            "degraded_with_routing_leak": int((flipped & leak).sum().item()),
            "degraded_without_leak": int((flipped & ~leak).sum().item()),
            "mean_new_slot_mass_after": round(routes[1].mean().item(), 4)}

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--selftest",
                                                    action="store_true")
    if ap.parse_args().selftest:
        print("itinerary metric self-test:")
        _selftest_itinerary()
        # edge-metric sanity: perfect scorer -> auroc/auprc 1.0
        el = torch.full((2,3,3), -5.0); E = torch.zeros(2,3,3)
        el[0,1,0]=5.0; E[0,1,0]=1; el[1,2,1]=5.0; E[1,2,1]=1
        live = torch.ones(2,3)
        m = edge_metrics(el, E, live)
        assert m["auroc"] > 0.99 and m["exact_graph"] == 1.0
        print("edge metric self-test:", m)
        print("ALL SELF-TESTS PASS")
