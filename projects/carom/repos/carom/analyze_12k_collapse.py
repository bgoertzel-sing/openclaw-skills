#!/usr/bin/env python3
"""Deterministic local-CPU forensics for CAROM's preserved 12k checkpoints."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import random
import time
from pathlib import Path

import torch
import torch.nn.functional as F

import exp2_compiled_channel as e2
import harness_v2

STEPS = [0] + list(range(1000, 12001, 1000))


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def groups():
    # L1--L5 are an explicit, CAROM-local operator-core decomposition. They
    # must not be confused with the six-layer ePC network in the RelaLeap run.
    return {
        "embedding": ("sym.", "pos."),
        "L1_query": ("core.Wq",),
        "L2_key": ("core.Wk",),
        "L3_value": ("core.Wv",),
        "L4_transform": ("core.T1", "core.T2"),
        "L5_gate": ("core.Wg", "core.gb"),
        "task_head": ("out.",),
        "hyper_head": ("hyper.",),
        "edge_head": ("edge.",),
        "entry_head": ("entry.",),
        "fitness_head": ("sigma.", "pool_q", "sig_scale"),
    }


def matching(named, prefixes):
    return [(name, tensor) for name, tensor in named if any(name.startswith(p) for p in prefixes)]


def l2_norm(tensors):
    return math.sqrt(sum(float(t.detach().double().square().sum()) for _, t in tensors))


def effective_rank_and_pr(matrix):
    x = matrix.detach().double().reshape(-1, matrix.shape[-1])
    x = x - x.mean(0, keepdim=True)
    singular = torch.linalg.svdvals(x)
    power = singular.square()
    total = power.sum()
    if float(total) <= 0:
        return 0.0, 0.0
    probs = power / total
    erank = float(torch.exp(-(probs * probs.clamp_min(1e-300).log()).sum()))
    pr = float(total.square() / power.square().sum().clamp_min(1e-300))
    return erank, pr


def linear_cka(first, second):
    x = first.detach().double().reshape(-1, first.shape[-1])
    y = second.detach().double().reshape(-1, second.shape[-1])
    x -= x.mean(0, keepdim=True)
    y -= y.mean(0, keepdim=True)
    numerator = torch.linalg.matrix_norm(x.T @ y).square()
    denominator = (
        torch.linalg.matrix_norm(x.T @ x) * torch.linalg.matrix_norm(y.T @ y)
    ).clamp_min(1e-300)
    return float(numerator / denominator)


def fixed_split(n=128, seed=8321):
    batch = e2.make_batch(n, random.Random(seed), len_range=(2, 4))
    keys = ("T", "SP", "X", "Y", "E", "ENT", "ORD", "Ls")
    return {key: value.cpu() for key, value in zip(keys, batch)}


def activations_and_eval(model, hidden, split):
    live = (split["ORD"] >= 0).float()
    captured = {}
    handles = []

    def hook(name):
        def save(_module, _inputs, output):
            value = output[0] if isinstance(output, tuple) else output
            captured[name] = value.detach().cpu()
        return save

    for name, module in (
        ("hyper", model.hyper[3]), ("edge", model.edge[3]),
        ("entry", model.entry[3]), ("fitness", model.sigma[3]),
        ("core", model.core), ("task", model.out[3]),
    ):
        handles.append(module.register_forward_hook(hook(name)))
    model.eval()
    with torch.no_grad():
        output, edge_logits, trajectory = model(hidden, split["X"], live, return_traj=True)
    for handle in handles:
        handle.remove()
    captured["trajectory"] = trajectory.cpu()
    # Core and fitness hooks naturally retain the last recurrent step.
    captured = {
        key: value.reshape(-1, value.shape[-1])
        for key, value in captured.items()
        if value.ndim >= 2 and key != "trajectory"
    } | {"trajectory": trajectory.reshape(-1, trajectory.shape[-1]).cpu()}
    return {
        "task_acc_repaired_corpus": float((output.argmax(-1) == split["Y"]).float().mean()),
        "edges": harness_v2.edge_metrics(edge_logits, split["E"], live),
        "itinerary": harness_v2.itinerary_report(trajectory, split["ORD"]),
    }, captured


def gradient_metrics(model, hidden, split, n=24):
    sub = {key: value[:n] for key, value in split.items()}
    h = hidden[:n]
    live = (sub["ORD"] >= 0).float()
    model.train()
    torch.manual_seed(991)
    output, edge_logits, _ = model(h, sub["X"], live)
    pair = live[:, :, None] * live[:, None, :] * (
        1 - torch.eye(e2.L_MAX)[None]
    )
    loss_task = F.cross_entropy(output.reshape(-1, e2.V), sub["Y"].reshape(-1))
    loss_edge = F.binary_cross_entropy_with_logits(edge_logits, sub["E"], weight=pair)
    entry_logits = model.entry(h).squeeze(-1) - 30.0 * (1 - live)
    loss_entry = F.cross_entropy(entry_logits, sub["ENT"].argmax(-1))
    loss = loss_task + loss_edge + 0.2 * loss_entry
    model.zero_grad(set_to_none=True)
    loss.backward()
    named = list(model.named_parameters())
    by_group = {}
    for group, prefixes in groups().items():
        chosen = matching(named, prefixes)
        sq = sum(
            float(param.grad.detach().double().square().sum())
            for _, param in chosen if param.grad is not None
        )
        by_group[group] = math.sqrt(sq)
    early = sum(by_group[k] for k in ("embedding", "L1_query", "L2_key"))
    late = sum(by_group[k] for k in ("L4_transform", "L5_gate", "task_head"))
    return {
        "loss": float(loss), "task_loss": float(loss_task),
        "edge_loss": float(loss_edge), "entry_loss": float(loss_entry),
        "groups": by_group, "early_to_late": early / max(late, 1e-30),
    }


def source_result(path, step):
    data = json.loads((path / f"result_step_{step:04d}.json").read_text())
    return {
        "task_acc": data["L2_4"]["task_acc"],
        "legacy_edge_acc": data["L2_4"]["edge_acc"],
        "legacy_tau": data["L2_4"]["itinerary"]["tau"],
    }


def pearson(x, y):
    a, b = torch.tensor(x, dtype=torch.double), torch.tensor(y, dtype=torch.double)
    a -= a.mean(); b -= b.mean()
    denom = a.norm() * b.norm()
    return None if float(denom) == 0 else float((a @ b) / denom)


def correlations(rows):
    acc = [row["source"]["task_acc"] for row in rows]
    series = {
        "itinerary.first_visit_tau": [r["evaluation"]["itinerary"]["first_visit_tau"] for r in rows],
        "itinerary.coverage": [r["evaluation"]["itinerary"]["coverage"] for r in rows],
        "itinerary.classified_fraction": [r["evaluation"]["itinerary"]["classified_fraction"] for r in rows],
        "edge.auprc": [r["evaluation"]["edges"]["auprc"] for r in rows],
        "edge.pos_recall@.5": [r["evaluation"]["edges"]["pos_recall@.5"] for r in rows],
        "gradient.early_to_late": [r["gradients"]["early_to_late"] for r in rows],
    }
    for group in groups():
        series[f"weight_ratio.{group}"] = [r["weight_ratio"][group] for r in rows]
    for block in rows[0]["representations"]:
        series[f"erank.{block}"] = [r["representations"][block]["effective_rank"] for r in rows]
        series[f"participation.{block}"] = [r["representations"][block]["participation_ratio"] for r in rows]
    out = {}
    for name, values in series.items():
        out[name] = {
            "coincident_pearson": pearson(values, acc),
            "metric_leads_accuracy_one_checkpoint": pearson(values[:-1], acc[1:]),
        }
    return out


def write_svg(path, rows):
    # Dependency-free timeline plot.
    width, height, pad = 1000, 560, 55
    series = [
        ("accuracy", [r["source"]["task_acc"] for r in rows], "#1f77b4"),
        ("tau", [r["evaluation"]["itinerary"]["first_visit_tau"] for r in rows], "#d62728"),
        ("AUPRC", [r["evaluation"]["edges"]["auprc"] for r in rows], "#2ca02c"),
        ("classified", [r["evaluation"]["itinerary"]["classified_fraction"] for r in rows], "#9467bd"),
    ]
    def point(i, value):
        x = pad + i * (width - 2 * pad) / (len(rows) - 1)
        y = height - pad - value * (height - 2 * pad)
        return x, y
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
             '<rect width="100%" height="100%" fill="white"/>',
             f'<line x1="{pad}" y1="{pad}" x2="{pad}" y2="{height-pad}" stroke="black"/>',
             f'<line x1="{pad}" y1="{height-pad}" x2="{width-pad}" y2="{height-pad}" stroke="black"/>']
    for j in range(6):
        y = height - pad - j / 5 * (height - 2 * pad)
        lines.append(f'<text x="8" y="{y+5}" font-size="12">{j/5:.1f}</text>')
    for offset, (name, values, color) in enumerate(series):
        pts = " ".join(f"{x:.1f},{y:.1f}" for i, value in enumerate(values) for x, y in [point(i, value)])
        lines.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="3"/>')
        lines.append(f'<text x="{pad+offset*150}" y="24" fill="{color}" font-size="15">{name}</text>')
    for i, row in enumerate(rows):
        x, _ = point(i, 0)
        lines.append(f'<text x="{x-13}" y="{height-25}" font-size="10">{row["step"]}</text>')
    lines.append("</svg>")
    path.write_text("\n".join(lines))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoints", type=Path, required=True)
    parser.add_argument("--source-results", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--plot", type=Path, required=True)
    args = parser.parse_args()
    torch.set_num_threads(max(1, min(8, torch.get_num_threads())))
    torch.manual_seed(8321)
    started = time.time()
    checkpoint_paths = {int(p.stem.split("_")[1]): p for p in args.checkpoints.glob("step_*.pt")}
    if sorted(checkpoint_paths) != STEPS:
        raise RuntimeError(f"checkpoint inventory mismatch: {sorted(checkpoint_paths)} != {STEPS}")
    loaded = {}
    schema = None
    inventory = []
    for step in STEPS:
        path = checkpoint_paths[step]
        payload = torch.load(path, map_location="cpu", weights_only=False)
        if set(payload) < {"m", "it", "rng"} or int(payload["it"]) != step:
            raise RuntimeError(f"invalid checkpoint payload: {path}")
        current = {name: tuple(value.shape) for name, value in payload["m"].items()}
        if schema is not None and current != schema:
            raise RuntimeError(f"schema mismatch: {path}")
        if not all(torch.isfinite(value).all() for value in payload["m"].values()):
            raise RuntimeError(f"nonfinite checkpoint: {path}")
        schema = current
        loaded[step] = payload["m"]
        inventory.append({"step": step, "path": str(path), "sha256": sha256(path), "bytes": path.stat().st_size})
    print("loading frozen GPT-2 and constructing fixed probe corpus", flush=True)
    lm = e2.GPT2Base(layer=-1).cpu().eval()
    split = fixed_split()
    hidden = e2.span_reps_gpt2(lm, split["T"], split["SP"]).detach()
    del lm
    baseline = None
    previous_activations = None
    rows = []
    for step in STEPS:
        print(f"checkpoint {step}", flush=True)
        model = e2.CompiledChannel(768).cpu()
        model.load_state_dict(loaded[step], strict=True)
        named = list(model.named_parameters())
        weight = {group: l2_norm(matching(named, prefixes)) for group, prefixes in groups().items()}
        if baseline is None:
            baseline = weight
        ratio = {group: value / baseline[group] for group, value in weight.items()}
        evaluation, activation = activations_and_eval(model, hidden, split)
        geometry = {}
        for block, values in activation.items():
            erank, pr = effective_rank_and_pr(values)
            geometry[block] = {"effective_rank": erank, "participation_ratio": pr}
        cka = None if previous_activations is None else {
            block: linear_cka(previous_activations[block], activation[block])
            for block in activation
        }
        gradients = gradient_metrics(model, hidden, split)
        rows.append({
            "step": step, "source": source_result(args.source_results, step),
            "weight_norm": weight, "weight_ratio": ratio,
            "gradients": gradients, "evaluation": evaluation,
            "representations": geometry, "cka_vs_previous": cka,
        })
        previous_activations = activation
    result = {
        "metadata": {
            "created_unix": time.time(), "elapsed_seconds": time.time() - started,
            "python": platform.python_version(), "torch": torch.__version__,
            "device": "cpu", "threads": torch.get_num_threads(),
            "seed": 8321, "probe_examples": len(split["X"]),
            "gradient_examples": 24,
            "instrument_commit": "975a4c9",
            "layer_mapping": {
                "L1": "core.Wq", "L2": "core.Wk", "L3": "core.Wv",
                "L4": "core.T1+core.T2", "L5": "core.Wg+core.gb",
                "LM_head_note": "Frozen GPT-2 and its LM head are absent from checkpoints; task_head is reported.",
            },
        },
        "inventory": inventory, "checkpoints": rows,
        "correlations": correlations(rows),
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    write_svg(args.plot.with_suffix(".svg"), rows)
    print(f"wrote {args.output}", flush=True)


if __name__ == "__main__":
    main()
