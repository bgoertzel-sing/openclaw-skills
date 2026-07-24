#!/usr/bin/env python3
"""CPU-first E2/E3 CAROM ladder with fixed corpus and paired seeds."""
import argparse
import hashlib
import json
import random
import time
from pathlib import Path

import torch
import torch.nn.functional as F

from model import Itinerant, direction_free_channel_penalties
from run_carom_e0_e1 import activity_metrics, corpus_hash, make_eval_corpus
from task import make_batch


FEATURE_ARMS = {
    "e2_full": ("workspace", "command", "position", "interaction"),
    "e2_no_workspace": ("command", "position"),
    "e2_no_command": ("workspace", "position"),
    "e2_no_position": ("workspace", "command", "interaction"),
}


def corpus_to_device(corpus, device):
    return tuple(x.to(device) if torch.is_tensor(x) else x for x in corpus)
E3_WEIGHTS = {
    "overlap": 2e-4,
    "switching_progress": 2e-3,
    "revisit": 2e-4,
    "terminal_trapping": 1e-6,
    "activity_mass": 2e-4,
}


def evaluate(model, corpus, batch_size):
    model.eval()
    C, _, X, Y, D = corpus
    rows, correct, exact, count = [], 0, 0, 0
    with torch.no_grad():
        for start in range(0, len(C), batch_size):
            sl = slice(start, start + batch_size)
            logits, diag = model(C[sl], X[sl], return_diagnostics=True)
            pred = logits.argmax(-1)
            slot = pred.eq(Y[sl])
            correct += int(slot.sum())
            exact += int(slot.all(-1).sum())
            count += slot.numel()
            mech = activity_metrics(diag["activity"],
                                    diag["workspace_update_norm"])
            for j, row in enumerate(mech):
                row.update(example_id=start + j, depth=int(D[sl][j]),
                           slot_accuracy=float(slot[j].float().mean()),
                           exact_workspace=bool(slot[j].all()))
                rows.append(row)
    return {"slot_accuracy": correct / count,
            "exact_workspace_accuracy": exact / len(C), "rows": rows}


def train(arm, features, regularized, seed, args, corpus, device):
    torch.manual_seed(seed)
    if device.type == "cuda":
        torch.cuda.manual_seed_all(seed)
    train_rng = random.Random(seed)
    model = Itinerant(
        d=args.d, K=args.K, steps=args.controller_steps, noise=args.noise,
        fixed_chain=False, mode_specific_fitness=True,
        fitness_features=features,
    ).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr,
                                  weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.OneCycleLR(
        optimizer, args.lr, total_steps=args.steps)
    t0 = time.time()
    for _ in range(args.steps):
        C, _, X, Y, _ = make_batch(args.batch_size, train_rng)
        C, X, Y = C.to(device), X.to(device), Y.to(device)
        model.train()
        logits, activity = model(C, X, return_traj=True)
        loss = F.cross_entropy(logits.flatten(0, 1), Y.flatten())
        if regularized:
            penalties = direction_free_channel_penalties(activity)
            loss = loss + sum(E3_WEIGHTS[k] * v for k, v in penalties.items())
        optimizer.zero_grad()
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        optimizer.step()
        scheduler.step()
    first = evaluate(model, corpus, args.eval_batch_size)
    second = evaluate(model, corpus, args.eval_batch_size)
    finite = all(torch.isfinite(torch.tensor(value)) for value in (
        first["slot_accuracy"], first["exact_workspace_accuracy"]))
    if not finite:
        raise FloatingPointError(f"non-finite output for {arm} seed {seed}")
    if first != second:
        raise RuntimeError(
            f"deterministic evaluation gate failed for {arm} seed {seed}")
    digest = hashlib.sha256(json.dumps(first, sort_keys=True).encode()).hexdigest()
    return {
        "arm": arm, "seed": seed, "features": list(features),
        "regularized": regularized, "metrics": first,
        "deterministic_repeat_match": first == second,
        "result_sha256": digest, "elapsed_s": time.time() - t0,
    }


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
    p.add_argument("--noise", type=float, default=.02)
    p.add_argument("--device", default="auto",
                   choices=("auto", "cpu", "cuda"))
    args = p.parse_args()
    device_name = ("cuda" if torch.cuda.is_available() else "cpu"
                   if args.device == "auto" else args.device)
    if args.device != "auto":
        device_name = args.device
    if device_name == "cuda" and not torch.cuda.is_available():
        raise RuntimeError("CUDA requested but unavailable")
    device = torch.device(device_name)
    if device.type == "cuda":
        torch.backends.cudnn.benchmark = False
        torch.use_deterministic_algorithms(True)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    corpus = make_eval_corpus(args.eval_size, args.eval_seed)
    torch.save({"C": corpus[0], "X": corpus[2], "Y": corpus[3], "D": corpus[4]},
               outdir / "paired_eval_corpus.pt")
    device_corpus = corpus_to_device(corpus, device)
    results = []
    arms = [(name, feats, False) for name, feats in FEATURE_ARMS.items()]
    arms.append(("e3_generic_regularized", FEATURE_ARMS["e2_full"], True))
    for seed in args.seeds:
        for name, features, regularized in arms:
            print(f"START arm={name} seed={seed}", flush=True)
            result = train(name, features, regularized, seed, args,
                           device_corpus, device)
            results.append(result)
            (outdir / f"{name}_seed{seed}.json").write_text(
                json.dumps(result, indent=2))
            print(
                f"DONE arm={name} seed={seed} "
                f"slot_accuracy={result['metrics']['slot_accuracy']:.6f} "
                f"elapsed_s={result['elapsed_s']:.2f}",
                flush=True)
    summary = {
        "config": vars(args), "device": str(device),
        "torch_version": torch.__version__, "cuda_version": torch.version.cuda,
        "gpu_name": (torch.cuda.get_device_name(0)
                     if device.type == "cuda" else None),
        "corpus_sha256": corpus_hash(corpus),
        "e3_weights": E3_WEIGHTS, "results": [
            {k: v for k, v in r.items() if k != "metrics"} | {
                "slot_accuracy": r["metrics"]["slot_accuracy"],
                "exact_workspace_accuracy":
                    r["metrics"]["exact_workspace_accuracy"]}
            for r in results],
    }
    (outdir / "summary.json").write_text(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
