"""Validated, adapter-pluggable evaluation instruments for compiled CAROM."""
from __future__ import annotations

import contextlib
import hashlib
import math
import random
from pathlib import Path

import torch
import torch.nn.functional as F


def _cpu_tree(value):
    if torch.is_tensor(value):
        return value.detach().cpu()
    if isinstance(value, dict):
        return {key: _cpu_tree(item) for key, item in value.items()}
    if isinstance(value, (tuple, list)):
        return type(value)(_cpu_tree(item) for item in value)
    return value


def build_corpora(seed=1234, exp2_module=None, sizes=None):
    if exp2_module is None:
        import exp2_compiled_channel as exp2_module
    sizes = sizes or {
        "val_L24": 512, "test_L24": 512, "val_L5": 256, "test_L5": 256
    }
    out = {}
    keys = ("T", "SP", "X", "Y", "E", "ENT", "ORD", "Ls")
    for offset, (name, n) in enumerate(sizes.items(), 1):
        batch = exp2_module.make_batch(
            n, random.Random(seed + 1000 * offset),
            fixed_len=5 if name.endswith("L5") else None, len_range=(2, 4),
        )
        split = {key: _cpu_tree(value) for key, value in zip(keys, batch)}
        split["ids"] = [f"{name}:{index}" for index in range(n)]
        out[name] = split
    return out


def save_corpora(corpora, path):
    torch.save(_cpu_tree(corpora), path)


def load_corpora(path):
    return _cpu_tree(torch.load(path, map_location="cpu", weights_only=False))


def corpus_sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def split_to(split, device):
    return {
        key: value.to(device) if torch.is_tensor(value) else value
        for key, value in split.items()
    }


def phases_with_dwell(traj, live_mask, dominance_margin=0.05,
                      max_normalized_entropy=0.90):
    seq, dwell, classified = [], [], 0
    live_indices = torch.as_tensor(live_mask, device=traj.device).bool()
    live_count = int(live_indices.sum())
    for state in traj:
        values = state[live_indices]
        if not live_count:
            continue
        probs = values.clamp_min(0)
        probs = probs / probs.sum().clamp_min(1e-12)
        top = torch.topk(probs, min(2, live_count)).values
        margin = float(top[0] - top[1]) if live_count > 1 else float(top[0])
        entropy = float(-(probs * probs.clamp_min(1e-12).log()).sum())
        normalized_entropy = entropy / max(math.log(live_count), 1e-12)
        if margin < dominance_margin or normalized_entropy > max_normalized_entropy:
            mode = None
        else:
            mode = int(torch.arange(len(live_indices), device=traj.device)[live_indices][
                int(probs.argmax())
            ])
            classified += 1
        if seq and seq[-1] == mode:
            dwell[-1] += 1
        else:
            seq.append(mode)
            dwell.append(1)
    return seq, dwell, classified / max(1, len(traj))


def itinerary_metrics(traj, order, **classification):
    ranks = {mode: rank for mode, rank in enumerate(order.tolist()) if rank >= 0}
    true_sequence = [mode for mode, _ in sorted(ranks.items(), key=lambda item: item[1])]
    sequence, dwell, classified_fraction = phases_with_dwell(
        traj, [mode in ranks for mode in range(len(order))], **classification
    )
    observed = [mode for mode in sequence if mode is not None]
    first_visits = list(dict.fromkeys(observed))
    predicted_transitions = list(zip(observed[:-1], observed[1:]))
    true_transitions = set(zip(true_sequence[:-1], true_sequence[1:]))
    true_positive = sum(pair in true_transitions for pair in predicted_transitions)
    rank_sequence = [ranks[mode] for mode in first_visits]
    concordant = sum(
        rank_sequence[i] < rank_sequence[j]
        for i in range(len(rank_sequence)) for j in range(i + 1, len(rank_sequence))
    )
    discordant = sum(
        rank_sequence[i] > rank_sequence[j]
        for i in range(len(rank_sequence)) for j in range(i + 1, len(rank_sequence))
    )
    return {
        "coverage": len(set(observed)) / max(1, len(ranks)),
        "trans_prec": true_positive / max(1, len(predicted_transitions)),
        "trans_rec": true_positive / max(1, len(true_transitions)),
        "exact_order": float(observed == true_sequence),
        "first_visit_tau": (concordant - discordant) / max(1, concordant + discordant),
        "mean_dwell": sum(dwell) / max(1, len(dwell)),
        "revisits": len(observed) - len(set(observed)),
        "classified_fraction": classified_fraction,
        "unclassified_phases": sum(mode is None for mode in sequence),
    }


def itinerary_report(trajectory, orders, **classification):
    rows = [
        itinerary_metrics(trajectory[index], orders[index], **classification)
        for index in range(len(trajectory))
    ]
    return {key: sum(row[key] for row in rows) / len(rows) for key in rows[0]}


def tie_correct_auroc(scores, labels):
    scores, labels = scores.flatten().double(), labels.flatten().bool()
    positives, negatives = scores[labels], scores[~labels]
    if not len(positives) or not len(negatives):
        return None
    comparisons = (positives[:, None] > negatives[None, :]).double()
    ties = (positives[:, None] == negatives[None, :]).double()
    return float((comparisons + 0.5 * ties).mean())


def average_precision(scores, labels):
    """Threshold-group AP; tied scores enter simultaneously."""
    scores, labels = scores.flatten().double(), labels.flatten().bool()
    positives = int(labels.sum())
    if not positives:
        return None
    total_positive, total_seen, area = 0, 0, 0.0
    for score in sorted(set(scores.tolist()), reverse=True):
        group = scores == score
        newly_positive = int(labels[group].sum())
        total_seen += int(group.sum())
        total_positive += newly_positive
        if newly_positive:
            area += newly_positive * total_positive / total_seen
    return area / positives


def edge_metrics(logits, targets, live):
    modes = targets.shape[-1]
    pair = (
        live[:, :, None].bool() & live[:, None, :].bool()
        & ~torch.eye(modes, device=targets.device, dtype=torch.bool)[None]
    )
    scores = torch.sigmoid(logits[pair]).detach().cpu()
    labels = targets[pair].detach().cpu().bool()
    hard = torch.sigmoid(logits) > 0.5
    exact = ((hard == targets.bool()) | ~pair).all(-1).all(-1).float().mean().item()
    positives, negatives = int(labels.sum()), int((~labels).sum())
    return {
        "auroc": tie_correct_auroc(scores, labels),
        "auprc": average_precision(scores, labels),
        "pos_recall@.5": (
            float((hard[pair] & labels.to(hard.device)).sum() / positives)
            if positives else None
        ),
        "exact_graph": exact,
        "prevalence": positives / max(1, positives + negatives),
        "predicted_positive_rate": float((scores > 0.5).double().mean()),
    }


def span_embeddings(span_fn, language_model, split):
    if span_fn is None:
        raise ValueError("a frozen span_fn adapter is required")
    return span_fn(language_model, split["T"], split["SP"])


def eval_checkpoint(model, language_model, split, *, span_fn, device=None):
    device = device or next(model.parameters()).device
    split = split_to(split, device)
    model.eval()
    hidden = span_embeddings(span_fn, language_model, split)
    live = (split["ORD"] >= 0).float()
    with torch.no_grad():
        output, edge_logits, trajectory = model(
            hidden, split["X"], live, return_traj=True
        )
    return {
        "task_acc": float((output.argmax(-1) == split["Y"]).float().mean()),
        "edges": edge_metrics(edge_logits, split["E"], live),
        "itinerary": itinerary_report(trajectory, split["ORD"]),
    }


@contextlib.contextmanager
def temporary_integration_steps(model, steps):
    original = model.S
    try:
        model.S = steps
        yield
    finally:
        model.S = original


def budget_sweep(model, language_model, split, *, span_fn, steps=(72, 110, 150)):
    output = {}
    for count in steps:
        with temporary_integration_steps(model, count):
            output[count] = eval_checkpoint(
                model, language_model, split, span_fn=span_fn
            )
    return output
