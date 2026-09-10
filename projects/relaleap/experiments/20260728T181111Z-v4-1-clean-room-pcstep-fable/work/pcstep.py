"""Clean-room synthetic T=1 predictive-coding step.

See ASSUMPTIONS.md for the provenance boundary and intentional limitations.
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
class Theta:
    layer1: Array
    layer2: Array


@dataclass(frozen=True)
class Batch:
    identifier: str
    inputs: Array
    targets: Array


@dataclass(frozen=True)
class BatchPlanState:
    identifiers: tuple[str, ...]
    cursor: int


@dataclass(frozen=True)
class OptimizerState:
    m1: Array
    m2: Array
    v1: Array
    v2: Array
    step: int
    rng_state: dict
    batch_plan: BatchPlanState


@dataclass(frozen=True)
class StepState:
    theta: Theta
    optimizer_state: OptimizerState
    settled_errors: tuple[Array, Array]


@dataclass(frozen=True)
class Config:
    error_lr: float = 0.05
    weight_lr: float = 0.01
    beta1: float = 0.9
    beta2: float = 0.999
    epsilon: float = 1e-8
    weight_decay: float = 0.0


def _theta_digest(theta: Theta) -> str:
    h = hashlib.sha256()
    for array in (theta.layer1, theta.layer2):
        a = np.ascontiguousarray(array, dtype=np.float64)
        h.update(a.shape.__repr__().encode("ascii"))
        h.update(a.tobytes())
    return h.hexdigest()


def settle_t1(theta: Theta, batch: Batch, error_lr: float) -> tuple[Array, Array]:
    """Take one epsilon descent step, asserting weights remain frozen."""
    before = _theta_digest(theta)
    x1 = batch.inputs @ theta.layer1.T
    prediction = x1 @ theta.layer2.T
    output_adjoint = (prediction - batch.targets) / batch.inputs.shape[0]
    hidden_adjoint = output_adjoint @ theta.layer2
    eps1 = -error_lr * hidden_adjoint
    eps2 = -error_lr * output_adjoint
    if _theta_digest(theta) != before:
        raise AssertionError("model weights changed during settlement")
    return eps1, eps2


def local_gradients(
    theta: Theta, batch: Batch, errors: tuple[Array, Array]
) -> tuple[Array, Array]:
    """Differentiate layer-local regressions with settled states held fixed."""
    eps1, eps2 = errors
    x1_forward = batch.inputs @ theta.layer1.T
    x1_settled = (x1_forward + eps1).copy()
    x2_settled = (x1_settled @ theta.layer2.T + eps2).copy()
    n = batch.inputs.shape[0]
    grad1 = ((x1_forward - x1_settled).T @ batch.inputs) / n
    layer2_prediction = x1_settled @ theta.layer2.T
    grad2 = ((layer2_prediction - x2_settled).T @ x1_settled) / n
    return grad1, grad2


def _adamw(
    parameter: Array, gradient: Array, m: Array, v: Array, step: int, cfg: Config
) -> tuple[Array, Array, Array]:
    m_new = cfg.beta1 * m + (1.0 - cfg.beta1) * gradient
    v_new = cfg.beta2 * v + (1.0 - cfg.beta2) * gradient * gradient
    m_hat = m_new / (1.0 - cfg.beta1**step)
    v_hat = v_new / (1.0 - cfg.beta2**step)
    p_new = parameter * (1.0 - cfg.weight_lr * cfg.weight_decay)
    p_new = p_new - cfg.weight_lr * m_hat / (np.sqrt(v_hat) + cfg.epsilon)
    return p_new, m_new, v_new


def pc_step(
    theta: Theta,
    optimizer_state: OptimizerState,
    batch: Batch,
    t: int,
    gate: Mapping[str, float],
    config: Config = Config(),
) -> StepState:
    """Pure conceptual boundary: (theta, optimizer_state, batch, t, gate)->state."""
    if t != optimizer_state.step + 1:
        raise ValueError("t must be the next one-based optimizer step")
    if optimizer_state.batch_plan.cursor >= len(optimizer_state.batch_plan.identifiers):
        raise ValueError("batch plan exhausted")
    expected = optimizer_state.batch_plan.identifiers[optimizer_state.batch_plan.cursor]
    if batch.identifier != expected:
        raise ValueError(f"expected batch {expected!r}, got {batch.identifier!r}")
    if set(gate) != {"layer1", "layer2"} or any(
        not 0.0 <= float(value) <= 1.0 for value in gate.values()
    ):
        raise ValueError("gate must contain layer1/layer2 multipliers in [0,1]")

    errors = settle_t1(theta, batch, config.error_lr)
    grad1, grad2 = local_gradients(theta, batch, errors)
    grad1 = float(gate["layer1"]) * grad1
    grad2 = float(gate["layer2"]) * grad2
    p1, m1, v1 = _adamw(
        theta.layer1, grad1, optimizer_state.m1, optimizer_state.v1, t, config
    )
    p2, m2, v2 = _adamw(
        theta.layer2, grad2, optimizer_state.m2, optimizer_state.v2, t, config
    )

    generator = np.random.default_rng()
    generator.bit_generator.state = copy.deepcopy(optimizer_state.rng_state)
    generator.random()  # explicit deterministic RNG-state transition
    plan = optimizer_state.batch_plan
    new_optimizer = OptimizerState(
        m1=m1,
        m2=m2,
        v1=v1,
        v2=v2,
        step=t,
        rng_state=copy.deepcopy(generator.bit_generator.state),
        batch_plan=BatchPlanState(plan.identifiers, plan.cursor + 1),
    )
    return StepState(Theta(p1, p2), new_optimizer, errors)


def initial_optimizer(theta: Theta, seed: int, batch_ids: tuple[str, ...]) -> OptimizerState:
    rng = np.random.default_rng(seed)
    return OptimizerState(
        np.zeros_like(theta.layer1),
        np.zeros_like(theta.layer2),
        np.zeros_like(theta.layer1),
        np.zeros_like(theta.layer2),
        0,
        copy.deepcopy(rng.bit_generator.state),
        BatchPlanState(batch_ids, 0),
    )


def _array_record(array: Array) -> dict:
    a = np.ascontiguousarray(array, dtype=np.float64)
    return {"shape": list(a.shape), "hex": a.tobytes().hex()}


def _array_restore(record: dict) -> Array:
    return np.frombuffer(bytes.fromhex(record["hex"]), dtype=np.float64).copy().reshape(
        record["shape"]
    )


def snapshot(state: StepState) -> bytes:
    opt = state.optimizer_state
    record = {
        "theta": [_array_record(state.theta.layer1), _array_record(state.theta.layer2)],
        "moments": [
            _array_record(opt.m1),
            _array_record(opt.m2),
            _array_record(opt.v1),
            _array_record(opt.v2),
        ],
        "step": opt.step,
        "rng_state": opt.rng_state,
        "batch_plan": {
            "identifiers": list(opt.batch_plan.identifiers),
            "cursor": opt.batch_plan.cursor,
        },
        "errors": [_array_record(x) for x in state.settled_errors],
    }
    return json.dumps(record, sort_keys=True, separators=(",", ":")).encode("utf-8")


def restore(payload: bytes) -> StepState:
    record = json.loads(payload.decode("utf-8"))
    theta = Theta(*(_array_restore(x) for x in record["theta"]))
    m1, m2, v1, v2 = (_array_restore(x) for x in record["moments"])
    plan_record = record["batch_plan"]
    opt = OptimizerState(
        m1, m2, v1, v2, record["step"], record["rng_state"],
        BatchPlanState(tuple(plan_record["identifiers"]), plan_record["cursor"]),
    )
    return StepState(theta, opt, tuple(_array_restore(x) for x in record["errors"]))
