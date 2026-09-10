"""Reference-transition policies.

A bridge is defined relative to a reference process.  v0.2 makes that choice a
first-class object so the covariance path, cross-time coupling, and local plant
model can share one reference instead of drifting independently.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Protocol

import numpy as np

from .types import ChannelObservation, GaussianTransition, broadcast_array


class ReferencePolicy(Protocol):
    def select(self, observation: ChannelObservation) -> GaussianTransition:
        ...


@dataclass(frozen=True, slots=True)
class ObservedReferencePolicy:
    """Use the observation's supplied reference transition unchanged.

    This is convenient but can inherit controller hysteresis when the supplied
    reference is computed from the current command.  Prefer a fixed or filtered
    commanded reference for scientific experiments.
    """

    def select(self, observation: ChannelObservation) -> GaussianTransition:
        return observation.reference

    def state_dict(self) -> dict[str, object]:
        return {"type": "observed"}


@dataclass(frozen=True, slots=True)
class FixedReferencePolicy:
    """A fixed, explicitly commanded local reference transition."""

    transition: GaussianTransition

    def select(self, observation: ChannelObservation) -> GaussianTransition:
        if observation.state.size != self.transition.size:
            raise ValueError("fixed reference size does not match observation.")
        return self.transition

    def state_dict(self) -> dict[str, object]:
        return {
            "type": "fixed",
            "contraction": self.transition.contraction.tolist(),
            "innovation": self.transition.innovation.tolist(),
        }


@dataclass(slots=True)
class FilteredReferencePolicy:
    """Slowly filter a commanded or observed transition.

    Contraction is filtered linearly.  Innovation is filtered in log-space so
    positivity is preserved.  The policy updates once per controller plan, not
    once per feasibility candidate, avoiding a hidden dependence on the search
    procedure itself.
    """

    alpha: float = 0.05
    innovation_floor: float = 1e-12
    max_contraction_change: float | None = 0.05
    max_log_innovation_change: float | None = 0.35
    source: Callable[[ChannelObservation], GaussianTransition] | None = None
    contraction: np.ndarray | None = None
    innovation: np.ndarray | None = None

    def __post_init__(self) -> None:
        if not 0.0 < self.alpha <= 1.0:
            raise ValueError("alpha must lie in (0, 1].")
        if self.innovation_floor <= 0.0:
            raise ValueError("innovation_floor must be positive.")

    def select(self, observation: ChannelObservation) -> GaussianTransition:
        raw = self.source(observation) if self.source is not None else observation.reference
        if raw.size != observation.state.size:
            raise ValueError("reference source size does not match observation.")
        raw_a = raw.contraction
        raw_r = np.maximum(raw.innovation, self.innovation_floor)
        if self.contraction is None or self.innovation is None:
            self.contraction = raw_a.copy()
            self.innovation = raw_r.copy()
        else:
            previous_a = broadcast_array(self.contraction, raw.size, name="reference_contraction")
            previous_r = broadcast_array(self.innovation, raw.size, name="reference_innovation")
            target_a = raw_a
            target_log_r = np.log(raw_r)
            previous_log_r = np.log(np.maximum(previous_r, self.innovation_floor))
            next_a = previous_a + self.alpha * (target_a - previous_a)
            next_log_r = previous_log_r + self.alpha * (target_log_r - previous_log_r)
            if self.max_contraction_change is not None:
                delta = float(self.max_contraction_change)
                if delta <= 0.0:
                    raise ValueError("max_contraction_change must be positive.")
                next_a = np.clip(next_a, previous_a - delta, previous_a + delta)
            if self.max_log_innovation_change is not None:
                delta = float(self.max_log_innovation_change)
                if delta <= 0.0:
                    raise ValueError("max_log_innovation_change must be positive.")
                next_log_r = np.clip(
                    next_log_r,
                    previous_log_r - delta,
                    previous_log_r + delta,
                )
            self.contraction = next_a
            self.innovation = np.exp(next_log_r)
        return GaussianTransition(
            contraction=np.asarray(self.contraction, dtype=np.float64),
            innovation=np.asarray(self.innovation, dtype=np.float64),
        )

    def reset(self) -> None:
        self.contraction = None
        self.innovation = None

    def state_dict(self) -> dict[str, Any]:
        return {
            "type": "filtered",
            "alpha": self.alpha,
            "contraction": None if self.contraction is None else self.contraction.tolist(),
            "innovation": None if self.innovation is None else self.innovation.tolist(),
        }

    def load_state_dict(self, state: dict[str, Any]) -> None:
        self.contraction = (
            None
            if state.get("contraction") is None
            else np.asarray(state["contraction"], dtype=np.float64)
        )
        self.innovation = (
            None
            if state.get("innovation") is None
            else np.asarray(state["innovation"], dtype=np.float64)
        )


@dataclass(frozen=True, slots=True)
class CallbackReferencePolicy:
    callback: Callable[[ChannelObservation], GaussianTransition]

    def select(self, observation: ChannelObservation) -> GaussianTransition:
        transition = self.callback(observation)
        if transition.size != observation.state.size:
            raise ValueError("callback reference size does not match observation.")
        return transition
