"""Nonlinear float64 Torch fixture for the V4-0 functional admission gate.

Ground truth is produced by ordinary ``torch.optim.Adam`` instances restored
from a complete snapshot.  The prediction path is deliberately labelled
approximate_full_state_AD: it uses the functional Adam replica and propagates
the full (parameters, first moments, second moments) tangent with torch.func.
"""
from __future__ import annotations

import copy
from dataclasses import dataclass
from typing import Iterable

import numpy as np
import torch
from torch import func as tfunc

from .backbone_torch import adamw_step
from .stats import spearman

torch.set_default_dtype(torch.float64)

BETAS = (0.9, 0.999)
EPS = 1e-8
MODULES = {
    "layer1": ("W1", "b1"),
    "layer2": ("W2", "b2"),
    "head": ("W3", "b3"),
}


def mlp(params, x):
    h = torch.tanh(x @ params["W1"] + params["b1"])
    h = torch.tanh(h @ params["W2"] + params["b2"])
    return h @ params["W3"] + params["b3"]


def mse(params, x, y):
    return torch.mean((mlp(params, x) - y) ** 2)


def init_params(generator, din=8, hidden=16, dout=4, scale=0.5):
    rand = lambda *shape: torch.randn(
        *shape, generator=generator, dtype=torch.float64)
    return {
        "W1": scale * rand(din, hidden) / np.sqrt(din),
        "b1": torch.zeros(hidden),
        "W2": scale * rand(hidden, hidden) / np.sqrt(hidden),
        "b2": torch.zeros(hidden),
        "W3": scale * rand(hidden, dout) / np.sqrt(hidden),
        "b3": torch.zeros(dout),
    }


def gate_dict(action):
    gate = {k: 1.0 for ks in MODULES.values() for k in ks}
    if action is not None:
        modules, alpha = action
        for module in modules:
            for name in MODULES[module]:
                gate[name] = float(alpha)
    return gate


def functional_step(state, batch, step_number, gate, lr):
    params, moments, variances = state
    x, y = batch
    grads = tfunc.grad(mse)(params, x, y)
    grads = {k: grads[k] * gate[k] for k in grads}
    return adamw_step(
        params, moments, variances, step_number, grads, lr=lr,
        betas=BETAS, eps=EPS, weight_decay=0.0)


def actual_step(snapshot, batch, step_number, action, lr):
    """One actual torch.optim.Adam step from a serializable snapshot."""
    params0, moments0, variances0 = snapshot
    params = {
        k: torch.nn.Parameter(v.detach().clone()) for k, v in params0.items()}
    optimizer = torch.optim.Adam(
        params.values(), lr=lr, betas=BETAS, eps=EPS, foreach=False,
        fused=False)
    # Populate the actual optimizer state, including its scalar step.
    for name, param in params.items():
        optimizer.state[param]["step"] = torch.tensor(
            float(step_number - 1), dtype=torch.float64)
        optimizer.state[param]["exp_avg"] = moments0[name].detach().clone()
        optimizer.state[param]["exp_avg_sq"] = variances0[name].detach().clone()
    optimizer.zero_grad(set_to_none=True)
    loss = mse(params, *batch)
    loss.backward()
    gate = gate_dict(action)
    for name, param in params.items():
        param.grad.mul_(gate[name])
    optimizer.step()
    out_p, out_m, out_v = {}, {}, {}
    for name, param in params.items():
        state = optimizer.state[param]
        out_p[name] = param.detach().clone()
        out_m[name] = state["exp_avg"].detach().clone()
        out_v[name] = state["exp_avg_sq"].detach().clone()
    return out_p, out_m, out_v


def actual_rollout(snapshot, batches, t0, action, horizons, lr, eval_sets):
    state = snapshot
    out = {}
    for k in range(1, max(horizons) + 1):
        state = actual_step(
            state, batches[k - 1], t0 + k - 1,
            action if k == 1 else None, lr)
        if k in horizons:
            out[k] = tuple(float(mse(state[0], x, y)) for x, y in eval_sets)
    return out


def tangent_predictions(snapshot, batches, t0, action, horizons, lr, eval_sets):
    """Return full-state and frozen-D predictions on one CRN plan."""
    ordinary = gate_dict(None)
    gated = functional_step(snapshot, batches[0], t0, gate_dict(action), lr)
    baseline = functional_step(snapshot, batches[0], t0, ordinary, lr)
    tangent = _tree_sub(gated, baseline)
    injected_theta = {k: v.clone() for k, v in tangent[0].items()}
    frozen = {k: v.clone() for k, v in tangent[0].items()}
    out = {}
    state = baseline
    for k in range(1, max(horizons) + 1):
        if k > 1:
            batch = batches[k - 1]
            step_number = t0 + k - 1
            fn = lambda s: functional_step(
                s, batch, step_number, ordinary, lr)
            next_state, tangent = tfunc.jvp(fn, (state,), (tangent,))
            _, hvp = tfunc.jvp(
                lambda p: tfunc.grad(mse)(p, *batch),
                (state[0],), (frozen,))
            bc2 = 1.0 - BETAS[1] ** step_number
            preconditioner = {
                name: 1.0 / (torch.sqrt(next_state[2][name] / bc2) + EPS)
                for name in frozen
            }
            frozen = {
                name: frozen[name] - lr * preconditioner[name] * hvp[name]
                for name in frozen
            }
            state = next_state
        if k in horizons:
            vals = []
            for x, y in eval_sets:
                full = tfunc.jvp(
                    lambda p: mse(p, x, y), (state[0],), (tangent[0],))[1]
                frz = tfunc.jvp(
                    lambda p: mse(p, x, y), (state[0],), (frozen,))[1]
                vals.append((float(full), float(frz)))
            out[k] = vals
    return out, injected_theta


def _tree_sub(a, b):
    return tuple(
        {k: av[k] - bv[k] for k in av} for av, bv in zip(a, b))


def _dot(a, b):
    return float(sum(torch.vdot(a[k].reshape(-1), b[k].reshape(-1)) for k in a))


def _auc(labels, scores):
    labels, scores = np.asarray(labels, bool), np.asarray(scores, float)
    pos, neg = scores[labels], scores[~labels]
    if not len(pos) or not len(neg):
        return float("nan")
    return float(np.mean(pos[:, None] > neg[None, :])
                 + 0.5 * np.mean(pos[:, None] == neg[None, :]))


def _metrics(truth, prediction):
    truth, prediction = np.asarray(truth), np.asarray(prediction)
    denom = np.maximum(np.abs(truth), 1e-15)
    return {
        "spearman": spearman(prediction, truth),
        "median_relative_error": float(np.median(np.abs(prediction-truth)/denom)),
        "median_absolute_error": float(np.median(np.abs(prediction-truth))),
        "magnitude_ratio_median": float(np.median(
            np.abs(prediction) / denom)),
        "sign_auroc": _auc(truth < 0.0, -prediction),
    }


@dataclass
class FixtureConfig:
    family: str
    seed: int
    lr: float
    n_probe_states: int = 30
    horizons: tuple = (1, 2, 5, 10, 25)
    batch_size: int = 64
    pool_size: int = 2048
    pretrain_steps: int = 400
    probe_every: int = 5
    noise_replicates: int = 64


def run_family(config: FixtureConfig):
    """Execute one frozen V4-0 family and return raw summary metrics."""
    torch.manual_seed(config.seed)
    torch.use_deterministic_algorithms(True)
    generator = torch.Generator().manual_seed(config.seed)
    teacher = init_params(generator, scale=1.0)
    xpool = torch.randn(
        config.pool_size, 8, generator=generator, dtype=torch.float64)
    ya = mlp(teacher, xpool).detach()
    if config.family.startswith("B1"):
        yb = mlp(teacher, torch.flip(xpool, dims=(1,))).detach()
    elif config.family == "B2_output_shift":
        yb = ya + 1.0
    elif config.family == "aligned_null":
        # Replaced after pretraining below with the learner's own outputs,
        # yielding a genuine no-signal (zero-gradient) aligned control.
        yb = ya.clone()
    else:
        raise ValueError(config.family)
    eval_sets = ((xpool[:512], ya[:512]), (xpool[:512], yb[:512]))
    params = init_params(generator)
    state = (
        params,
        {k: torch.zeros_like(v) for k, v in params.items()},
        {k: torch.zeros_like(v) for k, v in params.items()})
    np_rng = np.random.default_rng(config.seed + 1)

    def draw_batch(rng):
        idx = rng.integers(0, config.pool_size, config.batch_size)
        return xpool[idx], ya[idx]

    # Pretrain through actual torch.optim so snapshots originate in the real
    # learner, then reset moments before incoming-task adaptation.
    for t in range(1, config.pretrain_steps + 1):
        state = actual_step(state, draw_batch(np_rng), t, None, 1e-3)
    if config.family == "aligned_null":
        ya = mlp(state[0], xpool).detach()
        yb = ya.clone()
        eval_sets = ((xpool[:512], ya[:512]), (xpool[:512], yb[:512]))
    state = (
        state[0],
        {k: torch.zeros_like(v) for k, v in state[0].items()},
        {k: torch.zeros_like(v) for k, v in state[0].items()})

    actions = [
        ((module,), alpha)
        for module in ("layer1", "layer2") for alpha in (0.5, 0.1)
    ] + [(("layer1", "layer2"), alpha) for alpha in (0.5, 0.1)]
    rows = {h: [] for h in config.horizons}
    synergy = {"truth": [], "prediction": []}
    false_beneficial = []
    strong_effect_sigmas = []

    def make_plan(seed):
        rng = np.random.default_rng(seed)
        batches = []
        for _ in range(max(config.horizons)):
            idx = rng.integers(0, config.pool_size, config.batch_size)
            batches.append((xpool[idx], yb[idx]))
        return batches

    probes = 0
    adapt_steps = config.n_probe_states * config.probe_every
    for t in range(1, adapt_steps + 1):
        train_idx = np_rng.integers(0, config.pool_size, config.batch_size)
        if t % config.probe_every == 1 and probes < config.n_probe_states:
            plan_seed = int(np_rng.integers(1 << 31))
            plan = make_plan(plan_seed)
            baseline = actual_rollout(
                state, plan, t, None, config.horizons, config.lr, eval_sets)
            injected = {}
            truths = {}
            for action in actions:
                rollout = actual_rollout(
                    state, plan, t, action, config.horizons, config.lr,
                    eval_sets)
                prediction, u = tangent_predictions(
                    state, plan, t, action, config.horizons, config.lr,
                    eval_sets)
                injected[action] = u
                truths[action] = {}
                for h in config.horizons:
                    tau = rollout[h][0] - baseline[h][0]
                    tau_b = rollout[h][1] - baseline[h][1]
                    truths[action][h] = tau
                    rows[h].append({
                        "probe": probes, "action": repr(action),
                        "truth": tau, "truth_incoming": tau_b,
                        "full": prediction[h][0][0],
                        "frozen": prediction[h][0][1],
                    })
                    if config.family == "aligned_null":
                        false_beneficial.append(tau < -1e-12)
            # Pair synergy at alpha=.1, h=1 and its Hessian prediction.
            pair = (("layer1", "layer2"), 0.1)
            one = (("layer1",), 0.1)
            two = (("layer2",), 0.1)
            synergy["truth"].append(
                truths[pair][1] - truths[one][1] - truths[two][1])
            hvp = tfunc.jvp(
                lambda p: tfunc.grad(mse)(p, *eval_sets[0]),
                (state[0],), (injected[two],))[1]
            synergy["prediction"].append(_dot(injected[one], hvp))

            # Frozen measurement rule: 64 independent CRN continuations for
            # the strong pair action at h=5 at every probe state.
            replicate_effects = []
            for rep in range(config.noise_replicates):
                rep_plan = make_plan(
                    config.seed * 10_000_000 + probes * 1000 + rep)
                rep_base = actual_rollout(
                    state, rep_plan, t, None, (5,), config.lr, eval_sets)
                rep_gate = actual_rollout(
                    state, rep_plan, t, pair, (5,), config.lr, eval_sets)
                replicate_effects.append(rep_gate[5][0] - rep_base[5][0])
            sigma = float(np.std(replicate_effects, ddof=1))
            strong_effect_sigmas.append(
                abs(float(np.median(replicate_effects))) / max(sigma, 1e-30))
            probes += 1
        state = actual_step(
            state, (xpool[train_idx], yb[train_idx]), t, None, config.lr)

    result = {
        "family": config.family,
        "config": vars(config),
        "probe_states": probes,
        "cells": {},
        "synergy": {
            **_metrics(synergy["truth"], synergy["prediction"]),
            "median_absolute_truth": float(np.median(np.abs(synergy["truth"]))),
        },
        "median_strong_action_sigma": float(np.median(strong_effect_sigmas)),
        "null_false_benefit_rate": (
            float(np.mean(false_beneficial)) if false_beneficial else None),
    }
    for h, cell_rows in rows.items():
        truth = [r["truth"] for r in cell_rows]
        result["cells"][str(h)] = {
            "n": len(cell_rows),
            "full_state": _metrics(truth, [r["full"] for r in cell_rows]),
            "frozen_D": _metrics(truth, [r["frozen"] for r in cell_rows]),
            "incoming_nonnegative_fraction": float(np.mean(
                [r["truth_incoming"] >= -1e-12 for r in cell_rows])),
        }
    return result
