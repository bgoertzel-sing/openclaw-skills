"""Read-only, adapter-pluggable CAROM mechanism probes.

Outputs are descriptive measurements, never categorical mechanism licenses.
"""
from __future__ import annotations

import math
import random

import torch
import torch.nn.functional as F


def linear_commutator_energy(first, second):
    """Exact constructed-control statistic ||AB-BA||_F^2."""
    return float((first @ second - second @ first).square().sum())


def switching_word_growth(matrices, word):
    """Exact spectral-norm growth for a finite constructed switching word."""
    product = torch.eye(
        matrices[0].shape[0], device=matrices[0].device, dtype=matrices[0].dtype
    )
    for index in word:
        product = matrices[index] @ product
    return float(torch.linalg.matrix_norm(product, ord=2) ** (1 / max(1, len(word))))


def phase_map(model, workspace, features, beta, steps=12, amplitude=1.5):
    for _ in range(steps):
        operators = model.core(workspace, features)
        workspace = workspace + model.dt * (
            amplitude * torch.einsum("bk,bknd->bnd", beta, operators)
            - model.leak * workspace
        )
    return workspace


def command_beta(model, hidden, mode):
    return F.softmax(model.hyper(hidden[:, mode]), -1)


def _inputs(model, language_model, split, span_fn, n):
    if span_fn is None:
        raise ValueError("a frozen span_fn adapter is required")
    device = next(model.parameters()).device
    tensors = {
        key: value[:n].to(device) if torch.is_tensor(value) else value[:n]
        for key, value in split.items() if key in ("T", "SP", "X", "ORD")
    }
    hidden = span_fn(language_model, tensors["T"], tensors["SP"])
    evidence = F.normalize(model.sym(tensors["X"]), dim=-1) * math.sqrt(model.d)
    positions = model.pos(
        torch.arange(tensors["X"].shape[1], device=device)
    ).expand_as(evidence)
    return hidden, evidence, torch.cat([evidence, positions], -1), tensors["ORD"]


def swap_discrepancy(model, language_model, split, *, span_fn, pairs_per_example=1,
                     steps=12, seed=0, n=64):
    rng = random.Random(seed)
    hidden, evidence, features, orders = _inputs(
        model, language_model, split, span_fn, n
    )
    values = []
    model.eval()
    with torch.no_grad():
        for index in range(len(evidence)):
            live = [mode for mode in range(orders.shape[1]) if orders[index, mode] >= 0]
            for _ in range(pairs_per_example):
                first, second = rng.sample(live, 2)
                beta_first = command_beta(model, hidden[index:index + 1], first)
                beta_second = command_beta(model, hidden[index:index + 1], second)
                workspace = evidence[index:index + 1]
                feature = features[index:index + 1]
                forward = phase_map(
                    model, phase_map(model, workspace, feature, beta_first, steps),
                    feature, beta_second, steps,
                )
                reverse = phase_map(
                    model, phase_map(model, workspace, feature, beta_second, steps),
                    feature, beta_first, steps,
                )
                values.append(float((forward - reverse).norm() / workspace.norm()))
    tensor = torch.tensor(values)
    return {
        "mean": float(tensor.mean()), "median": float(tensor.median()),
        "p90": float(tensor.quantile(0.9)), "n_pairs": len(values),
        "interpretation": "sampled nonlinear order discrepancy",
    }


def jvp_phase(model, workspace, features, beta, vector, steps):
    from torch.func import jvp
    function = lambda state: phase_map(model, state, features, beta, steps)
    return jvp(function, (workspace,), (vector,))[1]


def _local_generator(device, seed):
    generator = torch.Generator(device=device)
    generator.manual_seed(seed)
    return generator


def commutator_energy(model, language_model, split, *, span_fn, n=32, probes=4,
                      steps=12, seed=0):
    rng = random.Random(seed)
    hidden, evidence, features, orders = _inputs(
        model, language_model, split, span_fn, n
    )
    generator = _local_generator(evidence.device, seed + 1)
    values = []
    for index in range(len(evidence)):
        live = [mode for mode in range(orders.shape[1]) if orders[index, mode] >= 0]
        first, second = rng.sample(live, 2)
        first_beta = command_beta(model, hidden[index:index + 1], first)
        second_beta = command_beta(model, hidden[index:index + 1], second)
        workspace, feature = evidence[index:index + 1], features[index:index + 1]
        for _ in range(probes):
            vector = torch.randn(
                workspace.shape, device=workspace.device, dtype=workspace.dtype,
                generator=generator,
            )
            vector /= vector.norm().clamp_min(1e-12)
            first_second = jvp_phase(
                model, workspace, feature, first_beta,
                jvp_phase(model, workspace, feature, second_beta, vector, steps), steps,
            )
            second_first = jvp_phase(
                model, workspace, feature, second_beta,
                jvp_phase(model, workspace, feature, first_beta, vector, steps), steps,
            )
            values.append(float((first_second - second_first).norm().square()))
    tensor = torch.tensor(values)
    return {
        "mean_interference": float(tensor.mean()), "median": float(tensor.median()),
        "n": len(values), "probe_seed": seed,
        "interpretation": "local sampled Jacobian-commutator energy",
    }


def schedule_stability_probe(model, language_model, split, *, span_fn, n=16,
                             horizon=24, products=6, phase_steps=6, seed=0):
    rng = random.Random(seed)
    hidden, evidence, features, orders = _inputs(
        model, language_model, split, span_fn, n
    )
    generator = _local_generator(evidence.device, seed + 1)
    alternating, natural, rates = [], [], []
    model.eval()
    with torch.no_grad():
        live_mask = (orders >= 0).float()
        _, _, natural_trajectory = model(
            hidden, split["X"][:n].to(evidence.device), live_mask, return_traj=True
        )
        for index in range(len(evidence)):
            live = [mode for mode in range(orders.shape[1]) if orders[index, mode] >= 0]
            first, second = rng.sample(live, 2)
            workspace = evidence[index:index + 1]
            initial_norm = float(workspace.norm())
            for phase in range(horizon):
                mode = first if phase % 2 == 0 else second
                workspace = phase_map(
                    model, workspace, features[index:index + 1],
                    command_beta(model, hidden[index:index + 1], mode), phase_steps,
                )
            alternating.append(float(workspace.norm()) / max(initial_norm, 1e-12))
            natural.append(
                float(natural_trajectory[index].norm(dim=-1).max())
                / max(float(natural_trajectory[index, 0].norm()), 1e-12)
            )
    for index in range(min(n, 8)):
        live = [mode for mode in range(orders.shape[1]) if orders[index, mode] >= 0]
        workspace = evidence[index:index + 1]
        for _ in range(products):
            vector = torch.randn(
                workspace.shape, device=workspace.device, dtype=workspace.dtype,
                generator=generator,
            )
            vector /= vector.norm().clamp_min(1e-12)
            for _ in range(horizon):
                mode = rng.choice(live)
                vector = jvp_phase(
                    model, workspace, features[index:index + 1],
                    command_beta(model, hidden[index:index + 1], mode),
                    vector, phase_steps,
                )
            rates.append(float(vector.norm()) ** (1 / horizon))
    alt, nat, rate = map(torch.tensor, (alternating, natural, rates))
    return {
        "alternating_growth_median": float(alt.median()),
        "natural_growth_median": float(nat.median()),
        "alternating_vs_natural_median_ratio": float(alt.median() / nat.median().clamp_min(1e-12)),
        "sampled_product_growth_median": float(rate.median()),
        "sampled_product_growth_p90": float(rate.quantile(0.9)),
        "probe_seed": seed,
        "interpretation": (
            "descriptive sampled growth; values above one can witness instability, "
            "values below one do not prove schedule-uniform stability"
        ),
    }


def cross_slot_effects(effect_matrices):
    """Aggregate unnormalized [slot, slot] effects without zero/device failure."""
    effects = torch.stack(effect_matrices)
    mean_effect = effects.mean(0)
    total = mean_effect.sum()
    normalized = mean_effect / total if float(total) > 0 else torch.zeros_like(mean_effect)
    off_diagonal = normalized.sum() - normalized.diag().sum()
    return {
        "effect_matrix": mean_effect,
        "normalized_effect_matrix": normalized,
        "offdiag_mass": float(off_diagonal),
        "zero_total_effect": bool(float(total) == 0),
        "interpretation": "descriptive perturbation coupling, not a typed-slot license",
    }


def decisiveness_from_trajectory(trajectory, orders, dominance_margin=0.05):
    live = (orders >= 0)[:, None, :]
    values = trajectory.clamp_min(0) * live
    probabilities = values / values.sum(-1, keepdim=True).clamp_min(1e-12)
    entropy = -(probabilities * probabilities.clamp_min(1e-12).log()).sum(-1)
    live_count = live.sum(-1).clamp_min(2)
    normalized_entropy = entropy / live_count.log()
    top = probabilities.topk(min(2, probabilities.shape[-1]), dim=-1).values
    margin = top[..., 0] - top[..., 1]
    return {
        "live_normalized_entropy_mean": float(normalized_entropy.mean()),
        "dominance_margin_mean": float(margin.mean()),
        "classified_fraction": float((margin >= dominance_margin).float().mean()),
    }


def load_checkpoint(path, device="cpu"):
    return torch.load(path, map_location=device, weights_only=False)
