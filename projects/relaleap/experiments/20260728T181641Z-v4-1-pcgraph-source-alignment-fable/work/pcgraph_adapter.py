"""Pure adapter for the public pcgraph jpc-native XOR oracle.

The numerical equations are re-expressed from the attributed GPL source
locations listed in SOURCE_ALIGNMENT.md; this is not a copied source file.
"""
from __future__ import annotations

import copy
import hashlib
import json
from dataclasses import dataclass
from typing import Mapping

import numpy as np


Array = np.ndarray


@dataclass(frozen=True)
class Weights:
    wxh: Array
    why: Array


@dataclass(frozen=True)
class Batch:
    identifier: str
    x: Array
    y: Array


@dataclass(frozen=True)
class BatchPlan:
    identifiers: tuple[str, ...]
    cursor: int


@dataclass(frozen=True)
class OptimizerState:
    """State outside pcgraph's direct local fold, retained for R3/R4 purity."""

    step: int
    rng_state: dict
    batch_plan: BatchPlan


@dataclass(frozen=True)
class SettleState:
    e_h: Array
    e_y: Array
    cells: Mapping[str, Array]


@dataclass(frozen=True)
class StepState:
    weights: Weights
    optimizer_state: OptimizerState
    settled: SettleState


def _f32(value: Array) -> Array:
    return np.asarray(value, dtype=np.float32)


def _weights_digest(weights: Weights) -> str:
    digest = hashlib.sha256()
    for array in (weights.wxh, weights.why):
        item = np.ascontiguousarray(array)
        digest.update(item.dtype.str.encode("ascii"))
        digest.update(repr(item.shape).encode("ascii"))
        digest.update(item.tobytes())
    return digest.hexdigest()


def settle_tick(
    weights: Weights,
    batch: Batch,
    e_h: Array,
    e_y: Array,
    error_lr: float = 0.1,
) -> SettleState:
    """One jpc-native error tick; model weights are asserted frozen."""
    before = _weights_digest(weights)
    n = np.float32(batch.x.shape[0])
    pre_h = _f32(batch.x @ weights.wxh.T)
    pcs_h = _f32(pre_h + e_h)
    phi_h = _f32(np.tanh(pcs_h))
    pre_y = _f32(phi_h @ weights.why.T)
    pcs_y = _f32(pre_y - e_y)
    residual = _f32(batch.y - pcs_y)
    energy = _f32(
        np.float32(0.5) * np.sum(e_h * e_h, dtype=np.float32) / n
        + np.float32(0.5) * np.sum(residual * residual, dtype=np.float32) / n
    )
    pcg_y = _f32(residual / n)
    pcb_h = _f32((residual @ weights.why) / n)
    prime_h = _f32(np.float32(1.0) - phi_h * phi_h)
    pcg_h = _f32((e_h / n) - prime_h * pcb_h)
    next_e_h = _f32(e_h - np.float32(error_lr) * pcg_h)
    next_e_y = _f32(e_y - np.float32(error_lr) * pcg_y)
    if _weights_digest(weights) != before:
        raise AssertionError("model weights changed during settlement")
    cells = {
        "pre_h": pre_h,
        "pcs_h": pcs_h,
        "phi_h": phi_h,
        "pre_y": pre_y,
        "pcs_y": pcs_y,
        "residual": residual,
        "energy": energy,
        "pcb_h": pcb_h,
        "pcg_h": pcg_h,
        "pcg_y": pcg_y,
    }
    return SettleState(next_e_h, next_e_y, cells)


def settle(
    weights: Weights, batch: Batch, ticks: int = 16, error_lr: float = 0.1
) -> SettleState:
    if ticks < 1:
        raise ValueError("ticks must be positive")
    e_h = np.zeros((batch.x.shape[0], weights.wxh.shape[0]), dtype=np.float32)
    e_y = np.zeros((batch.x.shape[0], weights.why.shape[0]), dtype=np.float32)
    state = None
    for _ in range(ticks):
        state = settle_tick(weights, batch, e_h, e_y, error_lr)
        e_h, e_y = state.e_h, state.e_y
    assert state is not None
    return state


def local_update(
    weights: Weights,
    batch: Batch,
    settled: SettleState,
    gate: Mapping[str, float],
    weight_lr: float = 0.01,
) -> Weights:
    """pcgraph m1 end-of-settle outer-product fold with an R3 module gate."""
    if set(gate) != {"xh", "hy"} or any(
        not 0.0 <= float(value) <= 1.0 for value in gate.values()
    ):
        raise ValueError("gate must contain xh/hy multipliers in [0, 1]")
    d_wxh = _f32(settled.e_h.T @ batch.x)
    d_why = _f32(settled.cells["residual"].T @ settled.cells["phi_h"])
    lr = np.float32(weight_lr)
    return Weights(
        _f32(weights.wxh + lr * np.float32(gate["xh"]) * d_wxh),
        _f32(weights.why + lr * np.float32(gate["hy"]) * d_why),
    )


def pc_step(
    weights: Weights,
    optimizer_state: OptimizerState,
    batch: Batch,
    t: int,
    gate: Mapping[str, float],
    *,
    settle_ticks: int = 16,
    error_lr: float = 0.1,
    weight_lr: float = 0.01,
) -> StepState:
    """Pure R3 boundary: (weights, optimizer_state, batch, t, gate) -> state."""
    if t != optimizer_state.step + 1:
        raise ValueError("t must be the next one-based outer update")
    plan = optimizer_state.batch_plan
    if plan.cursor >= len(plan.identifiers):
        raise ValueError("batch plan exhausted")
    if batch.identifier != plan.identifiers[plan.cursor]:
        raise ValueError("batch does not match frozen batch plan")
    settled = settle(weights, batch, settle_ticks, error_lr)
    updated = local_update(weights, batch, settled, gate, weight_lr)
    rng = np.random.default_rng()
    rng.bit_generator.state = copy.deepcopy(optimizer_state.rng_state)
    rng.random()
    next_optimizer = OptimizerState(
        t,
        copy.deepcopy(rng.bit_generator.state),
        BatchPlan(plan.identifiers, plan.cursor + 1),
    )
    return StepState(updated, next_optimizer, settled)


def initial_optimizer(seed: int, batch_ids: tuple[str, ...]) -> OptimizerState:
    rng = np.random.default_rng(seed)
    return OptimizerState(0, copy.deepcopy(rng.bit_generator.state), BatchPlan(batch_ids, 0))


def _array_record(array: Array) -> dict:
    item = np.ascontiguousarray(array)
    return {
        "dtype": item.dtype.str,
        "shape": list(item.shape),
        "hex": item.tobytes().hex(),
    }


def _array_restore(record: dict) -> Array:
    return np.frombuffer(
        bytes.fromhex(record["hex"]), dtype=np.dtype(record["dtype"])
    ).copy().reshape(record["shape"])


def snapshot(state: StepState) -> bytes:
    record = {
        "weights": [_array_record(state.weights.wxh), _array_record(state.weights.why)],
        "optimizer": {
            "step": state.optimizer_state.step,
            "rng_state": state.optimizer_state.rng_state,
            "batch_plan": {
                "identifiers": list(state.optimizer_state.batch_plan.identifiers),
                "cursor": state.optimizer_state.batch_plan.cursor,
            },
        },
        "settled": {
            "e_h": _array_record(state.settled.e_h),
            "e_y": _array_record(state.settled.e_y),
            "cells": {
                key: _array_record(value)
                for key, value in sorted(state.settled.cells.items())
            },
        },
    }
    return json.dumps(record, sort_keys=True, separators=(",", ":")).encode()


def restore(payload: bytes) -> StepState:
    record = json.loads(payload)
    weights = Weights(*(_array_restore(item) for item in record["weights"]))
    opt = record["optimizer"]
    plan = opt["batch_plan"]
    optimizer = OptimizerState(
        opt["step"],
        opt["rng_state"],
        BatchPlan(tuple(plan["identifiers"]), plan["cursor"]),
    )
    settled = record["settled"]
    settle_state = SettleState(
        _array_restore(settled["e_h"]),
        _array_restore(settled["e_y"]),
        {key: _array_restore(value) for key, value in settled["cells"].items()},
    )
    return StepState(weights, optimizer, settle_state)
