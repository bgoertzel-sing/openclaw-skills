#!/usr/bin/env python3
"""CAROM Exp2 GPT-2 arm: same 3 interventions but using frozen GPT-2-small.

Trains exp2 with --base gpt2 (frozen GPT-2 124M span encoder), checkpoints
every 500 steps, then runs:
  1. τ-decline curve with repaired itinerary metrics
  2. Trajectory intervention (forced/shuffled/smeared/natural)
  3. L=5 budget sweep (S=72, 100, 120)
"""
import json, math, random, time, os, sys
import torch
import torch.nn as nn
import torch.nn.functional as F

sys.path.insert(0, "/workspace")
import exp2_compiled_channel as E2
from exp2_compiled_channel import (
    CompiledChannel, span_reps, span_reps_gpt2, GPT2Base,
    make_batch, evaluate, DEVICE, V, N_SLOTS, L_MAX, W2I, T_VOCAB, MAXTOK,
    PRIMS, PARA, WORDS
)

CKPT_DIR = "/workspace/zerobot-runs/carom-gpt2/exp2_gpt2_ckpts"
OUT_DIR = "/workspace/zerobot-runs/carom-gpt2/results"
SEED = 0
STEPS = 4000
BS = 64  # smaller batch for GPT-2 (larger hidden states)
EDGES = 1.0
CKPT_INTERVAL = 500

# ============================================================================
# Repaired itinerary metrics (same as TinyLM version)
# ============================================================================

def phases_with_dwell(traj_b, live_mask):
    am = traj_b.argmax(-1).tolist()
    seq, dwell = [], []
    for m in am:
        if not live_mask[m]:
            continue
        if seq and seq[-1] == m:
            dwell[-1] += 1
        else:
            seq.append(m)
            dwell.append(1)
    return seq, dwell

def itinerary_metrics_repaired(traj_b, ord_b):
    live = [(r >= 0) for r in ord_b.tolist()]
    ranks = {m: r for m, r in enumerate(ord_b.tolist()) if r >= 0}
    L = len(ranks)
    true_seq = [m for m, _ in sorted(ranks.items(), key=lambda kv: kv[1])]
    seq, dwell = phases_with_dwell(traj_b, live)
    uniq = list(dict.fromkeys(seq))
    coverage = len(set(uniq)) / max(1, L)
    pred_tr = set(zip(uniq[:-1], uniq[1:]))
    true_tr = set(zip(true_seq[:-1], true_seq[1:]))
    tp = len(pred_tr & true_tr)
    prec = tp / max(1, len(pred_tr))
    rec = tp / max(1, len(true_tr))
    exact = float(uniq == true_seq)
    rs = [ranks[m] for m in uniq]
    if len(rs) < 2:
        tau = 0.0
    else:
        c = sum(rs[i] < rs[j] for i in range(len(rs)) for j in range(i+1, len(rs)))
        d = sum(rs[i] > rs[j] for i in range(len(rs)) for j in range(i+1, len(rs)))
        tau = (c - d) / max(1, c + d)
    revisits = len(seq) - len(uniq)
    mean_dwell = sum(dwell) / max(1, len(dwell))
    return {
        "coverage": coverage, "trans_prec": prec, "trans_rec": rec,
        "exact_order": exact, "tau": tau,
        "mean_dwell": mean_dwell, "revisits": revisits,
        "n_phases": len(seq), "n_unique": len(uniq),
    }

def itinerary_report_repaired(traj, ORD):
    ms = [itinerary_metrics_repaired(traj[b], ORD[b]) for b in range(traj.shape[0])]
    return {k: sum(m[k] for m in ms) / len(ms) for k in ms[0]}

# ============================================================================
# Frozen evaluation corpus
# ============================================================================

def build_frozen_corpus(seed=1234, n=256, fixed_len=None, len_range=(2,4)):
    rng = random.Random(seed + 1000)
    T, SP, X, Y, E, ENT, ORD, Ls = make_batch(n, rng, fixed_len=fixed_len, len_range=len_range)
    return {"T": T, "SP": SP, "X": X, "Y": Y, "E": E, "ENT": ENT, "ORD": ORD, "Ls": Ls}

# ============================================================================
# Trajectory intervention
# ============================================================================

def clamped_trajectory(mode, ord_b, S, M, amp=1.5, rng=None):
    live = [m for m in range(M) if ord_b[m] >= 0]
    if mode == "smeared":
        t = torch.zeros(S, M)
        t[:, live] = amp / len(live)
        return t
    if mode == "forced":
        order = sorted(live, key=lambda m: ord_b[m].item())
    elif mode == "shuffled":
        order = live[:]
        rng.shuffle(order)
        if len(order) > 1 and order == sorted(live, key=lambda m: ord_b[m].item()):
            order = order[::-1]
    else:
        raise ValueError(f"Unknown mode: {mode}")
    t = torch.zeros(S, M)
    seg = S // len(order)
    for i, m in enumerate(order):
        end = (i+1)*seg if i < len(order)-1 else S
        t[i*seg:end, m] = amp
    return t

def run_clamped(model, H, X, ORD, a_traj):
    with torch.no_grad():
        B = H.shape[0]
        e = F.normalize(model.sym(X), dim=-1) * math.sqrt(model.d)
        p = model.pos(torch.arange(N_SLOTS, device=X.device)).expand_as(e)
        w, feat = e, torch.cat([e, p], -1)
        beta_cmd = F.softmax(model.hyper(H), -1)
        live = (ORD >= 0).float()
        for t in range(a_traj.shape[1]):
            beta = torch.einsum("bm,bmk->bk", a_traj[:, t] * live, beta_cmd)
            u = model.core(w, feat)
            w = w + model.dt * (torch.einsum("bk,bknd->bnd", beta, u) - model.leak * w)
        return model.out(w)

def intervention_suite(model, lm, corpus, span_fn, seed=7, amp=1.5):
    model.eval()
    rng = random.Random(seed)
    T, SP, X, Y, ORD = (
        corpus["T"], corpus["SP"], corpus["X"], corpus["Y"], corpus["ORD"]
    )
    H = span_fn(lm, T, SP)
    live = (ORD >= 0).float()
    results = {}
    with torch.no_grad():
        out, _, traj = model(H, X, live, return_traj=True)
        results["natural_acc"] = (out.argmax(-1) == Y).float().mean().item()
        results["natural_itinerary"] = itinerary_report_repaired(traj, ORD)
    S, M = model.S, ORD.shape[1]
    for mode in ["forced", "shuffled", "smeared"]:
        A = torch.stack([
            clamped_trajectory(mode, ORD[b], S, M, amp, rng)
            for b in range(ORD.shape[0])
        ]).to(DEVICE)
        with torch.no_grad():
            out = run_clamped(model, H, X, ORD, A)
            results[f"{mode}_acc"] = (out.argmax(-1) == Y).float().mean().item()
    results["causal_gap"] = results["forced_acc"] - results["shuffled_acc"]
    results["natural_vs_shuffled"] = results["natural_acc"] - results["shuffled_acc"]
    results["natural_vs_forced"] = results["natural_acc"] - results["forced_acc"]
    return results

# ============================================================================
# Budget sweep
# ============================================================================

def budget_sweep(model, lm, corpus, span_fn, Ss=(72, 100, 120)):
    model.eval()
    T, SP, X, Y, ORD = (
        corpus["T"], corpus["SP"], corpus["X"], corpus["Y"], corpus["ORD"]
    )
    H = span_fn(lm, T, SP)
    live = (ORD >= 0).float()
    S0 = model.S
    results = {}
    with torch.no_grad():
        for S in Ss:
            model.S = S
            out, _, traj = model(H, X, live, return_traj=True)
            acc = (out.argmax(-1) == Y).float().mean().item()
            it = itinerary_report_repaired(traj, ORD)
            results[S] = {"acc": acc, "itinerary": {k: round(v, 4) for k, v in it.items()}}
    model.S = S0
    return results

# ============================================================================
# Training with checkpointing (GPT-2 base)
# ============================================================================

def train_gpt2_with_checkpoints(lm, steps, bs, edges, seed, ckpt_dir, span_fn):
    os.makedirs(ckpt_dir, exist_ok=True)
    torch.manual_seed(seed)
    rng = random.Random(seed)
    model = CompiledChannel(lm.d).to(DEVICE)
    opt = torch.optim.AdamW(model.parameters(), lr=2e-3, weight_decay=1e-4)
    sched = torch.optim.lr_scheduler.OneCycleLR(opt, 2e-3, total_steps=steps)

    ckpt_path = os.path.join(ckpt_dir, "step_0000.pt")
    torch.save({"m": model.state_dict(), "it": 0, "rng": rng.getstate()}, ckpt_path)
    print(f"  saved checkpoint: {ckpt_path}", flush=True)

    t0 = time.time()
    for it in range(steps):
        T, SP, X, Y, E, ENT, ORD, Ls = make_batch(bs, rng)
        live = (ORD >= 0).float()
        H = span_fn(lm, T, SP)
        out, el, _ = model(H, X, live)
        loss = F.cross_entropy(out.reshape(-1, V), Y.reshape(-1))
        if edges > 0:
            pair = live.unsqueeze(1) * live.unsqueeze(2) * (1 - torch.eye(L_MAX, device=DEVICE)[None])
            eloss = F.binary_cross_entropy_with_logits(el, E, weight=pair)
            loss = loss + edges * eloss
            ent_logit = model.entry(H).squeeze(-1) - 30.0 * (1 - live)
            loss = loss + 0.2 * edges * F.cross_entropy(ent_logit, ENT.argmax(-1))
        opt.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        sched.step()

        if (it + 1) % CKPT_INTERVAL == 0:
            ckpt_path = os.path.join(ckpt_dir, f"step_{it+1:04d}.pt")
            torch.save({"m": model.state_dict(), "it": it + 1, "rng": rng.getstate()}, ckpt_path)
            acc, eacc, tau = evaluate(model, lm, rng, span_fn=span_fn)
            print(f"  step {it+1} loss {loss.item():.3f} | L2-4: acc {acc:.3f} edge {eacc:.3f} tau {tau:.3f} "
                  f"({time.time()-t0:.0f}s) -> {ckpt_path}", flush=True)

    ckpt_path = os.path.join(ckpt_dir, f"step_{steps:04d}.pt")
    torch.save({"m": model.state_dict(), "it": steps, "rng": rng.getstate()}, ckpt_path)
    print(f"  saved final: {ckpt_path}", flush=True)
    return model

# ============================================================================
# Main
# ============================================================================

def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    print("="*60, flush=True)
    print("CAROM GPT-2 ARM: Frozen GPT-2-small (124M) span encoder", flush=True)
    print("="*60, flush=True)

    # Load frozen GPT-2
    print("Loading frozen GPT-2-small...", flush=True)
    lm = GPT2Base(layer=-1).to(DEVICE)
    span_fn = span_reps_gpt2
    print(f"  GPT-2 loaded, d={lm.d}", flush=True)

    interventions_only = "--interventions-only" in sys.argv
    if interventions_only:
        ckpt_files = sorted(
            f for f in os.listdir(CKPT_DIR) if f.endswith(".pt")
        )
        if not ckpt_files:
            raise RuntimeError(
                f"--interventions-only requested but no checkpoints found in {CKPT_DIR}"
            )
        print(
            f"\nSkipping training; resuming interventions from {len(ckpt_files)} checkpoints.",
            flush=True,
        )
        model = CompiledChannel(lm.d).to(DEVICE)
    else:
        print(
            f"\nTraining exp2 with GPT-2 base ({STEPS} steps, ckpt every {CKPT_INTERVAL})...",
            flush=True,
        )
        model = train_gpt2_with_checkpoints(
            lm, STEPS, BS, EDGES, SEED, CKPT_DIR, span_fn
        )

    # Build frozen corpora
    print("\nBuilding frozen evaluation corpora...", flush=True)
    corpus_L24 = build_frozen_corpus(seed=1234, n=256, len_range=(2, 4))
    corpus_L5 = build_frozen_corpus(seed=5678, n=128, fixed_len=5)
    print(f"  L2-4: {corpus_L24['T'].shape[0]} examples, L5: {corpus_L5['T'].shape[0]} examples", flush=True)

    # Run interventions on all checkpoints
    print("\nRunning interventions on all checkpoints...", flush=True)
    ckpt_files = sorted([f for f in os.listdir(CKPT_DIR) if f.endswith(".pt")])
    all_results = []

    for ckpt_file in ckpt_files:
        ckpt_path = os.path.join(CKPT_DIR, ckpt_file)
        print(f"\n--- {ckpt_file} ---", flush=True)
        t0 = time.time()

        st = torch.load(ckpt_path, weights_only=False, map_location=DEVICE)
        model.load_state_dict(st["m"])
        model.eval()
        step = st.get("it", 0)

        # 1. τ-decline
        print("  [1] τ-decline (repaired itinerary)...", flush=True)
        with torch.no_grad():
            T, SP, X, Y, E, ENT, ORD = (
                corpus_L24["T"], corpus_L24["SP"], corpus_L24["X"],
                corpus_L24["Y"], corpus_L24["E"], corpus_L24["ENT"],
                corpus_L24["ORD"],
            )
            live = (ORD >= 0).float()
            H = span_fn(lm, T, SP)
            out, el, traj = model(H, X, live, return_traj=True)
            acc = (out.argmax(-1) == Y).float().mean().item()
            pair = (live.unsqueeze(1) * live.unsqueeze(2) * (1 - torch.eye(L_MAX, device=DEVICE)[None])).bool()
            eacc = ((torch.sigmoid(el[pair]) > 0.5).float() == E[pair]).float().mean().item()
            it_L24 = itinerary_report_repaired(traj, ORD)

            T5, SP5, X5, Y5, E5, ENT5, ORD5 = (
                corpus_L5["T"], corpus_L5["SP"], corpus_L5["X"],
                corpus_L5["Y"], corpus_L5["E"], corpus_L5["ENT"],
                corpus_L5["ORD"],
            )
            live5 = (ORD5 >= 0).float()
            H5 = span_fn(lm, T5, SP5)
            out5, el5, traj5 = model(H5, X5, live5, return_traj=True)
            acc5 = (out5.argmax(-1) == Y5).float().mean().item()
            it_L5 = itinerary_report_repaired(traj5, ORD5)

        # 2. Trajectory intervention
        print("  [2] Trajectory intervention...", flush=True)
        interv = intervention_suite(model, lm, corpus_L24, span_fn, seed=7)

        # 3. L=5 budget sweep
        print("  [3] L=5 budget sweep...", flush=True)
        sweep = budget_sweep(model, lm, corpus_L5, span_fn, Ss=(72, 100, 120))

        result = {
            "checkpoint": ckpt_file, "step": step,
            "base_model": "gpt2-small-124M",
            "elapsed_seconds": round(time.time() - t0, 1),
            "L2_4": {"task_acc": round(acc, 4), "edge_acc": round(eacc, 4),
                     "itinerary": {k: round(v, 4) for k, v in it_L24.items()}},
            "L5": {"task_acc": round(acc5, 4),
                   "itinerary": {k: round(v, 4) for k, v in it_L5.items()}},
            "intervention": {
                "natural_acc": round(interv["natural_acc"], 4),
                "forced_acc": round(interv["forced_acc"], 4),
                "shuffled_acc": round(interv["shuffled_acc"], 4),
                "smeared_acc": round(interv["smeared_acc"], 4),
                "causal_gap": round(interv["causal_gap"], 4),
                "natural_vs_shuffled": round(interv["natural_vs_shuffled"], 4),
                "natural_itinerary": {k: round(v, 4) for k, v in interv["natural_itinerary"].items()},
            },
            "budget_sweep": {
                str(S): {"acc": v["acc"], "itinerary": v["itinerary"]}
                for S, v in sweep.items()
            },
        }
        all_results.append(result)

        out_path = os.path.join(OUT_DIR, f"result_{ckpt_file.replace('.pt', '.json')}")
        with open(out_path, "w") as f:
            json.dump(result, f, indent=2)
        print(f"  done in {time.time()-t0:.1f}s -> {out_path}", flush=True)

    # Summary
    print("\n" + "="*60, flush=True)
    print("SUMMARY (GPT-2 arm)", flush=True)
    print("="*60, flush=True)
    summary_path = os.path.join(OUT_DIR, "summary.json")
    with open(summary_path, "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"\n{'Step':>6} {'L24_acc':>8} {'L24_tau':>8} {'L24_cov':>8} {'L5_acc':>8} {'L5_tau':>8}", flush=True)
    for r in all_results:
        print(f"{r['step']:6d} {r['L2_4']['task_acc']:8.3f} {r['L2_4']['itinerary']['tau']:8.3f} "
              f"{r['L2_4']['itinerary']['coverage']:8.3f} {r['L5']['task_acc']:8.3f} "
              f"{r['L5']['itinerary']['tau']:8.3f}", flush=True)

    print(f"\n{'Step':>6} {'Natural':>8} {'Forced':>8} {'Shuffled':>8} {'Smeared':>8} {'Nat-Shuf':>8}", flush=True)
    for r in all_results:
        i = r["intervention"]
        print(f"{r['step']:6d} {i['natural_acc']:8.3f} {i['forced_acc']:8.3f} "
              f"{i['shuffled_acc']:8.3f} {i['smeared_acc']:8.3f} "
              f"{i['natural_vs_shuffled']:8.3f}", flush=True)

    print(f"\n{'Step':>6} {'S=72':>8} {'S=100':>8} {'S=120':>8}", flush=True)
    for r in all_results:
        bs = r["budget_sweep"]
        print(f"{r['step']:6d} {bs.get('72',{}).get('acc',0):8.3f} "
              f"{bs.get('100',{}).get('acc',0):8.3f} {bs.get('120',{}).get('acc',0):8.3f}", flush=True)

    print(f"\nAll results: {OUT_DIR}/", flush=True)
    print("DONE", flush=True)

if __name__ == "__main__":
    main()
