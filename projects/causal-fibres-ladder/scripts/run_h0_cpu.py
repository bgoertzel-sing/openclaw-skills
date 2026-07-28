#!/usr/bin/env python3
"""CPU smoke instantiation of the Formalization 0014 H0 interface gate."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
import random
import time
from pathlib import Path
from typing import Any

import numpy as np
import torch
import torch.nn.functional as F
from causal_fibres.observability import FrozenReadProbe
from torch import Tensor, nn


FACTOR_NAMES = ["subject_number", "object_number", "tense", "negation", "agreement"]


def seed_everything(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.use_deterministic_algorithms(True)
    torch.set_num_threads(min(4, torch.get_num_threads()))


def make_examples(n: int, seed: int) -> tuple[Tensor, Tensor, Tensor]:
    generator = torch.Generator().manual_seed(seed)
    factors = torch.randint(0, 2, (n, 5), generator=generator)
    nuisance = torch.randint(0, 8, (n,), generator=generator)
    positions = [1 + 2 * j + factors[:, j] for j in range(5)]
    tokens = torch.stack(
        [
            torch.zeros(n, dtype=torch.long),
            *positions,
            11 + nuisance,
        ],
        dim=1,
    )
    powers = 2 ** torch.arange(5)
    labels = (factors * powers).sum(dim=1)
    return tokens, factors, labels


def counterfactual_tokens(factors: Tensor, nuisance_tokens: Tensor, factor: int) -> Tensor:
    edited = factors.clone()
    edited[:, factor] = 1 - edited[:, factor]
    positions = [1 + 2 * j + edited[:, j] for j in range(5)]
    return torch.stack(
        [torch.zeros(len(edited), dtype=torch.long), *positions, nuisance_tokens],
        dim=1,
    )


def oracle_logits(labels: Tensor, margin: float, n_classes: int = 32) -> Tensor:
    logits = torch.zeros((len(labels), n_classes), dtype=torch.float32)
    logits.scatter_(1, labels[:, None], margin)
    return logits


class SixLayerStudent(nn.Module):
    def __init__(self, d_model: int, n_heads: int, n_layers: int) -> None:
        super().__init__()
        self.embedding = nn.Embedding(19, d_model)
        self.position = nn.Parameter(torch.randn(7, d_model) * 0.02)
        self.layers = nn.ModuleList(
            [
                nn.TransformerEncoderLayer(
                    d_model,
                    n_heads,
                    dim_feedforward=2 * d_model,
                    dropout=0.0,
                    batch_first=True,
                    norm_first=True,
                    activation="gelu",
                )
                for _ in range(n_layers)
            ]
        )
        self.norm = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, 32)

    def forward(self, tokens: Tensor, capture: bool = False) -> tuple[Tensor, dict[str, Tensor]]:
        hidden = self.embedding(tokens) + self.position
        reads: dict[str, Tensor] = {}
        for index, layer in enumerate(self.layers):
            hidden = layer(hidden)
            if capture:
                reads[f"block_{index}"] = hidden[:, 0].detach()
        logits = self.head(self.norm(hidden[:, 0]))
        return logits, reads


def train_student(model: SixLayerStudent, tokens: Tensor, labels: Tensor, cfg: dict[str, Any]) -> list[float]:
    optimizer = torch.optim.AdamW(model.parameters(), lr=3e-3, weight_decay=1e-3)
    generator = torch.Generator().manual_seed(cfg["seed"] + 1)
    history = []
    model.train()
    for _ in range(cfg["student_steps"]):
        index = torch.randint(0, len(tokens), (cfg["batch_size"],), generator=generator)
        logits, _ = model(tokens[index])
        loss = F.cross_entropy(logits, labels[index])
        optimizer.zero_grad(set_to_none=True)
        loss.backward()
        optimizer.step()
        history.append(float(loss.detach()))
    return history


def selected_reads(reads: dict[str, Tensor], sites: list[str]) -> dict[str, Tensor]:
    result = {}
    for site in sites:
        if site.startswith("blocks_"):
            indices = site.removeprefix("blocks_").split("_")
            result[site] = torch.cat([reads[f"block_{index}"] for index in indices], dim=1)
        else:
            result[site] = reads[site]
    return result


def task_arrays(logits: Tensor, labels: Tensor) -> tuple[np.ndarray, np.ndarray]:
    loss = F.cross_entropy(logits, labels, reduction="none").detach().numpy()
    correct = (logits.argmax(dim=1) == labels).float().detach().numpy()
    return loss, correct


def bootstrap_closure(
    base: np.ndarray,
    residual: np.ndarray,
    teacher: np.ndarray,
    *,
    higher_is_better: bool,
    seed: int,
    samples: int,
) -> dict[str, float | list[float] | None]:
    if higher_is_better:
        numerator = residual.mean() - base.mean()
        denominator = teacher.mean() - base.mean()
    else:
        numerator = base.mean() - residual.mean()
        denominator = base.mean() - teacher.mean()
    estimate = float(numerator / denominator) if denominator > 0 else None
    rng = np.random.default_rng(seed)
    values = []
    for _ in range(samples):
        index = rng.integers(0, len(base), len(base))
        if higher_is_better:
            num = residual[index].mean() - base[index].mean()
            den = teacher[index].mean() - base[index].mean()
        else:
            num = base[index].mean() - residual[index].mean()
            den = base[index].mean() - teacher[index].mean()
        if den > 1e-12:
            values.append(float(num / den))
    ci = [float(x) for x in np.quantile(values, [0.025, 0.975])] if values else None
    return {"estimate": estimate, "ci95": ci, "valid_bootstrap_samples": len(values)}


def factor_scores(logits: Tensor) -> Tensor:
    classes = torch.arange(32)
    scores = []
    for factor in range(5):
        on = ((classes >> factor) & 1).bool()
        scores.append(torch.logsumexp(logits[:, on], dim=1) - torch.logsumexp(logits[:, ~on], dim=1))
    return torch.stack(scores, dim=1)


def factor_metrics(
    model: SixLayerStudent,
    probe: FrozenReadProbe,
    site: str,
    tokens: Tensor,
    factors: Tensor,
    base_logits: Tensor,
    base_reads: dict[str, Tensor],
    margin: float,
) -> dict[str, dict[str, float]]:
    output: dict[str, dict[str, float]] = {}
    base_selected = selected_reads(base_reads, [site])[site]
    with torch.no_grad():
        residual_original = base_logits + probe.model(base_selected)
    nuisance = tokens[:, -1]
    for j, name in enumerate(FACTOR_NAMES):
        edited_tokens = counterfactual_tokens(factors, nuisance, j)
        powers = 2 ** torch.arange(5)
        edited_factors = factors.clone()
        edited_factors[:, j] = 1 - edited_factors[:, j]
        edited_labels = (edited_factors * powers).sum(dim=1)
        teacher_original_labels = (factors * powers).sum(dim=1)
        teacher_original = oracle_logits(teacher_original_labels, margin)
        teacher_edited = oracle_logits(edited_labels, margin)
        with torch.no_grad():
            base_edited, edited_reads_all = model(edited_tokens, capture=True)
            edited_reads = selected_reads(edited_reads_all, [site])[site]
            residual_edited = base_edited + probe.model(edited_reads)
        delta_teacher = teacher_edited - teacher_original
        delta_base = base_edited - base_logits
        delta_residual = residual_edited - residual_original
        error_base = ((delta_base - delta_teacher) ** 2).mean(dim=1)
        error_residual = ((delta_residual - delta_teacher) ** 2).mean(dim=1)
        gamma = 1.0 - float(
            (error_residual.mean() / error_base.mean().clamp_min(1e-12)).detach()
        )
        residual_score_edit = factor_scores(residual_edited) - factor_scores(residual_original)
        teacher_score_edit = factor_scores(teacher_edited) - factor_scores(teacher_original)
        score_error = (residual_score_edit - teacher_score_edit) ** 2
        spill = float(score_error[:, [k for k in range(5) if k != j]].sum(dim=1).mean())
        output[name] = {
            "base_edit_mse": float(error_base.mean()),
            "residual_edit_mse": float(error_residual.mean()),
            "gamma_j": gamma,
            "spill_to_other_factor_scores": spill,
        }
    return output


def evaluate_arm(
    model: SixLayerStudent,
    arm: dict[str, Any],
    site: str,
    train_reads: dict[str, Tensor],
    validation_reads: dict[str, Tensor],
    train_base: Tensor,
    train_teacher: Tensor,
    validation_base: Tensor,
    validation_teacher: Tensor,
    validation_tokens: Tensor,
    validation_factors: Tensor,
    validation_labels: Tensor,
    cfg: dict[str, Any],
    arm_index: int,
) -> dict[str, Any]:
    probe = FrozenReadProbe(
        input_dim=train_reads[site].shape[1],
        output_dim=32,
        kind=arm["kind"],
        capacity=arm["capacity"],
        steps=cfg["probe_steps"],
        batch_size=cfg["batch_size"],
        learning_rate=3e-3,
        seed=cfg["seed"] + 100 + arm_index,
    )
    started = time.perf_counter()
    fit = probe.fit(
        train_reads[site],
        train_base,
        train_teacher,
        validation_reads[site],
        validation_base,
        validation_teacher,
        name=f"{site}/{arm['name']}",
    )
    train_seconds = time.perf_counter() - started
    with torch.no_grad():
        started = time.perf_counter()
        logits = validation_base + probe.model(validation_reads[site])
        deployment_seconds = time.perf_counter() - started
    base_loss, base_acc = task_arrays(validation_base, validation_labels)
    residual_loss, residual_acc = task_arrays(logits, validation_labels)
    teacher_loss, teacher_acc = task_arrays(validation_teacher, validation_labels)
    loss_closure = bootstrap_closure(
        base_loss,
        residual_loss,
        teacher_loss,
        higher_is_better=False,
        seed=cfg["seed"] + 10000 + arm_index,
        samples=cfg["n_bootstrap"],
    )
    accuracy_closure = bootstrap_closure(
        base_acc,
        residual_acc,
        teacher_acc,
        higher_is_better=True,
        seed=cfg["seed"] + 20000 + arm_index,
        samples=cfg["n_bootstrap"],
    )
    factors = factor_metrics(
        model,
        probe,
        site,
        validation_tokens,
        validation_factors,
        validation_base,
        {key: value for key, value in validation_reads.items() if key.startswith("block_")},
        cfg["teacher_margin"],
    )
    output_rank = min(arm["capacity"], train_reads[site].shape[1], 32)
    if arm["kind"] in {"linear", "mlp"}:
        output_rank = 32
    return {
        "name": arm["name"],
        "site": site,
        "kind": arm["kind"],
        "lora_equivalent": arm.get("lora_equivalent", False),
        "raw": {
            "base_loss": float(base_loss.mean()),
            "residual_loss": float(residual_loss.mean()),
            "teacher_loss": float(teacher_loss.mean()),
            "base_accuracy": float(base_acc.mean()),
            "residual_accuracy": float(residual_acc.mean()),
            "teacher_accuracy": float(teacher_acc.mean()),
            "loss_denominator": float(base_loss.mean() - teacher_loss.mean()),
            "accuracy_denominator": float(teacher_acc.mean() - base_acc.mean()),
            "distillation_validation_loss": fit.validation_loss,
        },
        "gamma_l": loss_closure,
        "gamma_a": accuracy_closure,
        "factors": factors,
        "budget": {
            "parameters_ever_trained": fit.parameter_count,
            "parameters_deployed": fit.parameter_count,
            "mean_active_features": arm["capacity"] if arm["kind"] != "linear" else train_reads[site].shape[1],
            "code_width": arm["capacity"] if arm["kind"] != "linear" else train_reads[site].shape[1],
            "group_count": 0,
            "training_seconds": train_seconds,
            "deployment_seconds_for_validation_set": deployment_seconds,
            "residual_output_rank_bound": output_rank,
            "read_width": train_reads[site].shape[1],
        },
    }


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.config.read_text())
    seed_everything(cfg["seed"])

    train_tokens, train_factors, train_labels = make_examples(cfg["n_train"], cfg["seed"] + 10)
    validation_tokens, validation_factors, validation_labels = make_examples(
        cfg["n_validation"], cfg["seed"] + 20
    )
    model = SixLayerStudent(cfg["d_model"], cfg["n_heads"], cfg["n_layers"])
    started = time.perf_counter()
    student_history = train_student(model, train_tokens, train_labels, cfg)
    student_seconds = time.perf_counter() - started
    model.eval()
    for parameter in model.parameters():
        parameter.requires_grad_(False)
    with torch.no_grad():
        train_base, train_all_reads = model(train_tokens, capture=True)
        validation_base, validation_all_reads = model(validation_tokens, capture=True)
    train_teacher = oracle_logits(train_labels, cfg["teacher_margin"])
    validation_teacher = oracle_logits(validation_labels, cfg["teacher_margin"])
    train_reads = selected_reads(train_all_reads, cfg["read_sites"])
    validation_reads = selected_reads(validation_all_reads, cfg["read_sites"])
    # Retain individual reads for counterfactual feature extraction.
    validation_reads.update(validation_all_reads)

    arms = []
    index = 0
    for site in cfg["read_sites"]:
        for arm in cfg["arms"]:
            arms.append(
                evaluate_arm(
                    model,
                    arm,
                    site,
                    train_reads,
                    validation_reads,
                    train_base,
                    train_teacher,
                    validation_base,
                    validation_teacher,
                    validation_tokens,
                    validation_factors,
                    validation_labels,
                    cfg,
                    index,
                )
            )
            index += 1

    def gate_lower_bound(arm: dict[str, Any]) -> float:
        bounds = []
        for metric in ("gamma_l", "gamma_a"):
            ci = arm[metric]["ci95"]
            if ci is not None:
                bounds.append(ci[0])
        return max(bounds, default=-math.inf)

    # Accuracy saturates at one for many arms in this toy task. Break gate-bound
    # ties with the loss-closure lower bound, which retains resolution.
    best = max(
        arms,
        key=lambda arm: (
            gate_lower_bound(arm),
            arm["gamma_l"]["ci95"][0] if arm["gamma_l"]["ci95"] is not None else -math.inf,
        ),
    )
    passed = gate_lower_bound(best) > 0.50
    point_values = [
        value
        for value in (best["gamma_l"]["estimate"], best["gamma_a"]["estimate"])
        if value is not None
    ]
    result = {
        "schema": "causal-fibres-h0-smoke-v1",
        "scope": "local CPU toy/smoke; not the GPT-2-small target replication",
        "config": cfg,
        "provenance": {
            "config_path": str(args.config),
            "config_sha256": sha256(args.config),
            "python": platform.python_version(),
            "platform": platform.platform(),
            "torch": torch.__version__,
            "numpy": np.__version__,
            "causal_fibres": "0.4.0",
            "cuda_available": torch.cuda.is_available(),
        },
        "data": {
            "generator": "five independent binary factors plus 8-way nuisance token",
            "class_encoding": "sum factor_j * 2**j",
            "counterfactual": "toggle exactly one factor token; preserve all others and nuisance",
            "train_examples": cfg["n_train"],
            "validation_examples": cfg["n_validation"],
            "train_seed": cfg["seed"] + 10,
            "validation_seed": cfg["seed"] + 20,
        },
        "interface": {
            "base": "six-layer pre-norm Transformer encoder, all parameters frozen after pretraining",
            "reads": cfg["read_sites"],
            "read_pooling": "position-0 hidden state",
            "write": "additive final 32-class logits",
            "teacher": "deterministic oracle logits with target-class margin",
        },
        "student": {
            "parameters": sum(parameter.numel() for parameter in model.parameters()),
            "training_seconds": student_seconds,
            "initial_training_loss": student_history[0],
            "final_training_loss": student_history[-1],
        },
        "arms": arms,
        "gate": {
            "rule": "max lower 95% paired-bootstrap bound of Gamma_L or Gamma_A > 0.50",
            "passed": passed,
            "best_arm": f"{best['site']}/{best['name']}",
            "best_lower_bound": gate_lower_bound(best),
            "point_max_gamma": max(point_values) if point_values else None,
            "claim_scope": "H0 toy/smoke only",
        },
        "limitations": [
            "One student/probe training seed; bootstrap quantifies held-out-example uncertainty only.",
            "Oracle teacher is simpler than GPT-2-small.",
            "LoRA and low-rank residual labels are algebraically equivalent at this final-logit write site.",
            "Synthetic examples repeat the complete 32-state factor support with sampled nuisance values.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["gate"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
