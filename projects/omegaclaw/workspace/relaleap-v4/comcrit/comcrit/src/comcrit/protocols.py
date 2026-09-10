"""Protocols: the four portability requirements, plus the named-terms
contract (the anti-black-box guarantee).

A host system integrates with comcrit by supplying:
  R1  a ModulePartition                        (partition.py)
  R2  task oracles (loss/grad/HVP closures)    (Oracles)
  R3  a pure gated update step                 (StepFunction)
  R4  CRN rollout control                      (BatchPlan + snapshotable state)

Everything else — injection, propagation, projection, decomposition,
gates, floors — is comcrit's job.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Mapping, Protocol, Sequence

# An action gates one or more modules' incoming gradient for one step.
#   (["module_name", ...], alpha)   alpha in [0,1]; alpha=1 is ordinary.
Action = tuple[Sequence[str], float]
ORDINARY: Action | None = None


class StepFunction(Protocol):
    """R3 -- the single genuine intrusion into user code.

    Must be a PURE function of its arguments: no global RNG, no hidden
    in-place state. `state` bundles parameters AND optimizer moments;
    `gate` is a pytree/dict of scalar multipliers applied to the gradient
    after backward and before the optimizer (use partition.apply_gate).
    Purity is what makes exact-D possible: the backbone jvp's through the
    entire step, moments included.
    """

    def __call__(self, state: Any, batch: Any, t: int,
                 gate: Mapping[str, float]) -> Any: ...


class StateView(Protocol):
    """Minimal lens into an opaque learner state."""

    def params_of(self, state: Any) -> Any: ...


@dataclass(frozen=True)
class Oracles:
    """R2 -- evaluation-objective closures over *parameters* (not state).

    loss_A/loss_B: params -> scalar (fixed eval data closed over).
    grad_X, hvp_X derive mechanically in JAX / torch.func; helpers in the
    backend modules build them from the loss closures.
    """

    loss_A: Callable[[Any], float]
    loss_B: Callable[[Any], float]
    grad_A: Callable[[Any], Any]
    grad_B: Callable[[Any], Any]
    hvp_A: Callable[[Any, Any], Any]   # (params, v) -> H_A v
    hvp_B: Callable[[Any, Any], Any]


@dataclass(frozen=True)
class BatchPlan:
    """R4 -- deterministic CRN batch sequence for one decision state.

    batches[k] is the minibatch consumed at rollout step k; both arms of
    every paired comparison consume the identical sequence. A separate
    `preview_batch` (typically the eval batch) supports the decision-time
    preview backbone mode.
    """

    batches: Sequence[Any]
    preview_batch: Any | None = None


@dataclass
class BackboneTerms:
    """The named decomposition returned per (action, horizon).

    tau_hat_A/tau_hat_B are the headline predictions; the remaining fields
    are the decomposition that gates, residual features, confusion export,
    and reports all consume. `mode` records how the number was produced
    ("exact_d" | "frozen_d" | "preview"). Fields that a mode does not
    populate stay None rather than silently zero.
    """

    action: Any
    horizon: int
    mode: str
    tau_hat_A: float
    tau_hat_B: float | None = None
    first_order: float | None = None     # <g_A, u> at injection
    drift: float | None = None           # delta_0' H_A u
    self_curv: float | None = None       # 1/2 u' H_A u
    cross_curv: float | None = None      # u_m' H_A u_n (pair actions)
    extras: dict = field(default_factory=dict)
