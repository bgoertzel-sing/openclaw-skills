#!/usr/bin/env python3
"""Paired, multi-seed CAROM E0/E1 exposure-normalization experiment."""
import argparse
import hashlib
import json
import math
import random
import time
from pathlib import Path

import torch
import torch.nn.functional as F

from model import Itinerant
from task import C_VOCAB, L_MAX, make_batch

ARMS = {
    "fixed_raw": (True, False),
    "free_raw": (False, False),
    "fixed_norm": (True, True),
    "free_norm": (False, True),
}


def make_eval_corpus(n, seed):
    rng = random.Random(seed)
    chunks = []
    for depth in range(2, L_MAX + 1):
        size = n // (L_MAX - 1) + (depth - 2 < n % (L_MAX - 1))
        chunks.append(make_batch(size, rng, fixed_len=depth))
    return tuple(torch.cat([x[i] for x in chunks], dim=0) if i != 1 else None
                 for i in range(5))


def corpus_hash(corpus):
    h = hashlib.sha256()
    for tensor in (corpus[0], corpus[2], corpus[3], corpus[4]):
        h.update(tensor.contiguous().numpy().tobytes())
    return h.hexdigest()


def compressed(values):
    out = []
    for value in values:
        if not out or value != out[-1]:
            out.append(value)
    return out


def activity_metrics(activity, update_norm):
    # activity [B,S,M], update_norm [B,S]
    dominant = activity.argmax(-1)
    mass = activity.sum(-1)
    exposure = activity.sum(1) * 0.2
    overlap = (activity > 0.5).sum(-1)
    rows = []
    for b in range(activity.shape[0]):
        seq = compressed(dominant[b].tolist())
        diffs = [v - u for u, v in zip(seq, seq[1:])]
        revisits = len(seq) - len(set(seq))
        dwell = torch.bincount(dominant[b], minlength=L_MAX).tolist()
        rows.append({
            "dominant_sequence": seq,
            "dwell_counts": dwell,
            "integrated_exposure": exposure[b].tolist(),
            "integrated_activity_mass": float(mass[b].sum().item() * 0.2),
            "mean_activity_mass": float(mass[b].mean().item()),
            "overlap_fraction": float((overlap[b] > 1).float().mean().item()),
            "mean_active_modes": float(overlap[b].float().mean().item()),
            "skips": sum(abs(d) > 1 for d in diffs),
            "reversals": sum(d < 0 for d in diffs),
            "revisits": revisits,
            "terminal_mode": int(dominant[b, -1].item()),
            "terminal_trapping": bool((dominant[b, -10:] == dominant[b, -1]).all()),
            "integrated_workspace_update_norm": float(update_norm[b].sum().item()),
        })
    return rows


def evaluate(model, corpus, device, batch_size, activity_source=None,
             include_rows=True):
    model.eval()
    C, _, X, Y, D = corpus
    rows = []
    correct_slots = 0
    exact = 0
    total_slots = 0
    with torch.no_grad():
        for start in range(0, len(C), batch_size):
            sl = slice(start, start + batch_size)
            cb, xb, yb, db = C[sl].to(device), X[sl].to(device), Y[sl].to(device), D[sl]
            override = None
            if activity_source is not None:
                activity_source.eval()
                _, source_diag = activity_source(cb, xb, return_diagnostics=True)
                override = source_diag["activity"]
            logits, diag = model(cb, xb, return_diagnostics=True,
                                 activity_override=override)
            pred = logits.argmax(-1)
            slot = (pred == yb)
            correct_slots += int(slot.sum().item())
            exact += int(slot.all(-1).sum().item())
            total_slots += slot.numel()
            if include_rows:
                mech = activity_metrics(diag["activity"].cpu(),
                                        diag["workspace_update_norm"].cpu())
                for j, m in enumerate(mech):
                    m.update({
                        "example_id": start + j,
                        "depth": int(db[j].item()),
                        "commands": cb[j].cpu().tolist(),
                        "slot_accuracy": float(slot[j].float().mean().item()),
                        "exact_workspace": bool(slot[j].all().item()),
                    })
                    rows.append(m)
    return {
        "slot_accuracy": correct_slots / total_slots,
        "exact_workspace_accuracy": exact / len(C),
        "rows": rows,
    }


def arm_model(arm, args):
    fixed, normalized = ARMS[arm]
    return Itinerant(
        d=args.d, K=args.K, steps=args.controller_steps, dt=args.dt,
        noise=args.noise, fatigue_tau=args.fatigue_tau,
        fatigue_k=args.fatigue_k, leak=args.leak, fixed_chain=fixed,
        normalize_activity=normalized, activity_gain=args.activity_gain,
    )


def train_arm(arm, seed, args, corpus, outdir, device):
    torch.manual_seed(seed)
    rng = random.Random(seed)
    model = arm_model(arm, args).to(device)
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.OneCycleLR(opt, args.lr,
                                                     total_steps=args.steps)
    t0 = time.time()
    telemetry = []
    for step in range(args.steps):
        C, _, X, Y, _ = make_batch(args.batch_size, rng, device=device)
        model.train()
        logits = model(C, X)
        loss = F.cross_entropy(logits.reshape(-1, logits.shape[-1]), Y.reshape(-1))
        opt.zero_grad()
        loss.backward()
        grad_norm = torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()
        scheduler.step()
        if step % args.log_every == 0 or step == args.steps - 1:
            telemetry.append({"step": step, "loss": float(loss.item()),
                              "grad_norm": float(grad_norm.item()),
                              "elapsed_s": time.time() - t0})
            print(f"[{arm} seed={seed}] {step}/{args.steps} loss={loss.item():.4f}",
                  flush=True)
    result = evaluate(model, corpus, device, args.eval_batch_size)
    repeat = evaluate(model, corpus, device, args.eval_batch_size,
                      include_rows=False)
    result["deterministic_repeat_match"] = (
        result["slot_accuracy"] == repeat["slot_accuracy"] and
        result["exact_workspace_accuracy"] == repeat["exact_workspace_accuracy"]
    )
    result["telemetry"] = telemetry
    result["elapsed_s"] = time.time() - t0
    result["seed"] = seed
    result["arm"] = arm
    checkpoint = outdir / f"{arm}_seed{seed}.pt"
    torch.save({"model": model.state_dict(), "arm": arm, "seed": seed,
                "args": vars(args)}, checkpoint)
    with (outdir / f"{arm}_seed{seed}.json").open("w") as f:
        json.dump(result, f)
    return model, result


def mean(xs):
    return sum(xs) / len(xs)


def summarize(results, replays, corpus_sha):
    summary = {"corpus_sha256": corpus_sha, "arms": {}, "contrasts": {},
               "replays": replays}
    for arm in ARMS:
        rs = [r for (a, _), r in results.items() if a == arm]
        summary["arms"][arm] = {
            "n_seeds": len(rs),
            "slot_accuracy_mean": mean([r["slot_accuracy"] for r in rs]),
            "exact_accuracy_mean": mean([r["exact_workspace_accuracy"] for r in rs]),
            "all_deterministic": all(r["deterministic_repeat_match"] for r in rs),
            "per_seed_slot_accuracy": {str(r["seed"]): r["slot_accuracy"] for r in rs},
        }
    for name, left, right in [
        ("raw_fixed_minus_free", "fixed_raw", "free_raw"),
        ("norm_fixed_minus_free", "fixed_norm", "free_norm"),
        ("free_norm_minus_raw", "free_norm", "free_raw"),
    ]:
        diffs = []
        for seed in sorted({s for _, s in results}):
            diffs.append(results[(left, seed)]["slot_accuracy"] -
                         results[(right, seed)]["slot_accuracy"])
        brng = random.Random(20260720)
        boots = sorted(mean([brng.choice(diffs) for _ in diffs]) for _ in range(10000))
        summary["contrasts"][name] = {
            "mean": mean(diffs), "per_seed": diffs,
            "bootstrap_seed_95ci": [boots[249], boots[9749]],
        }
    return summary


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--outdir", required=True)
    p.add_argument("--seeds", nargs="+", type=int, default=[7, 17, 27, 37, 47])
    p.add_argument("--steps", type=int, default=3000)
    p.add_argument("--batch-size", type=int, default=128)
    p.add_argument("--eval-size", type=int, default=2048)
    p.add_argument("--eval-batch-size", type=int, default=256)
    p.add_argument("--eval-seed", type=int, default=20260720)
    p.add_argument("--lr", type=float, default=2e-3)
    p.add_argument("--d", type=int, default=64)
    p.add_argument("--K", type=int, default=16)
    p.add_argument("--controller-steps", type=int, default=70)
    p.add_argument("--dt", type=float, default=.2)
    p.add_argument("--noise", type=float, default=.02)
    p.add_argument("--fatigue-tau", type=float, default=6.)
    p.add_argument("--fatigue-k", type=float, default=1.5)
    p.add_argument("--leak", type=float, default=.02)
    p.add_argument("--activity-gain", type=float, default=1.)
    p.add_argument("--log-every", type=int, default=100)
    args = p.parse_args()
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    corpus = make_eval_corpus(args.eval_size, args.eval_seed)
    sha = corpus_hash(corpus)
    torch.save({"C": corpus[0], "X": corpus[2], "Y": corpus[3], "D": corpus[4]},
               outdir / "paired_eval_corpus.pt")
    results, replays = {}, {}
    for seed in args.seeds:
        models = {}
        for arm in ARMS:
            model, result = train_arm(arm, seed, args, corpus, outdir, device)
            models[arm] = model
            results[(arm, seed)] = result
        for suffix in ("raw", "norm"):
            fixed, free = models[f"fixed_{suffix}"], models[f"free_{suffix}"]
            ff = evaluate(fixed, corpus, device, args.eval_batch_size,
                          activity_source=free, include_rows=False)
            xf = evaluate(free, corpus, device, args.eval_batch_size,
                          activity_source=fixed, include_rows=False)
            replays[f"seed{seed}_{suffix}_fixed_core_free_trajectory"] = ff
            replays[f"seed{seed}_{suffix}_free_core_fixed_trajectory"] = xf
        del models
        if device.type == "cuda":
            torch.cuda.empty_cache()
    summary = summarize(results, replays, sha)
    summary["config"] = vars(args)
    summary["device"] = str(device) if device.type == "cpu" else torch.cuda.get_device_name(0)
    with (outdir / "summary.json").open("w") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary["contrasts"], indent=2), flush=True)


if __name__ == "__main__":
    main()
