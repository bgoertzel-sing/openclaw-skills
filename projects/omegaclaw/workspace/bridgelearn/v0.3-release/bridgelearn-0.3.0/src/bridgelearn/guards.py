"""Optional progress guards for validation, safety, and trust-region signals."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Literal, Protocol

import numpy as np


@dataclass(frozen=True, slots=True)
class GuardDecision:
    max_progress: float
    tripped: bool = False
    reason: str = ""
    diagnostics: dict[str, Any] | None = None


class ProgressGuard(Protocol):
    def decide(
        self,
        *,
        context: Any,
        current_progress: float,
        proposed_progress: float,
    ) -> GuardDecision:
        ...


@dataclass(slots=True)
class PatienceMetricGuard:
    """Freeze bridge progress after persistent metric degradation.

    The metric is expected to be cached in the supplied context; the guard does
    not prescribe when or how validation is run.  By default the trip is
    latched until ``reset`` is called, making experiment behavior explicit.
    """

    metric: Callable[[Any], float]
    mode: Literal["max", "min"] = "max"
    patience: int = 3
    absolute_tolerance: float = 0.0
    relative_tolerance: float = 0.0
    latched: bool = True
    best: float | None = None
    bad_count: int = 0
    is_tripped: bool = False

    def __post_init__(self) -> None:
        if self.mode not in {"max", "min"}:
            raise ValueError("mode must be 'max' or 'min'.")
        if self.patience <= 0:
            raise ValueError("patience must be positive.")
        if self.absolute_tolerance < 0.0 or self.relative_tolerance < 0.0:
            raise ValueError("tolerances must be non-negative.")

    def decide(
        self,
        *,
        context: Any,
        current_progress: float,
        proposed_progress: float,
    ) -> GuardDecision:
        value = float(self.metric(context))
        if not np.isfinite(value):
            self.bad_count += 1
        elif self.best is None:
            self.best = value
            self.bad_count = 0
        else:
            threshold = self.absolute_tolerance + self.relative_tolerance * max(
                abs(self.best), 1e-12
            )
            improvement = value - self.best if self.mode == "max" else self.best - value
            degradation = self.best - value if self.mode == "max" else value - self.best
            if improvement > threshold:
                self.best = value
                self.bad_count = 0
                if not self.latched:
                    self.is_tripped = False
            elif degradation > threshold:
                self.bad_count += 1
            else:
                self.bad_count = 0

        if self.bad_count >= self.patience:
            self.is_tripped = True
        max_progress = current_progress if self.is_tripped else proposed_progress
        return GuardDecision(
            max_progress=float(max_progress),
            tripped=self.is_tripped,
            reason="metric_degradation" if self.is_tripped else "",
            diagnostics={
                "metric_value": value,
                "metric_best": self.best,
                "metric_bad_count": self.bad_count,
            },
        )

    def reset(self) -> None:
        self.best = None
        self.bad_count = 0
        self.is_tripped = False

    def state_dict(self) -> dict[str, Any]:
        return {
            "mode": self.mode,
            "patience": self.patience,
            "absolute_tolerance": self.absolute_tolerance,
            "relative_tolerance": self.relative_tolerance,
            "latched": self.latched,
            "best": self.best,
            "bad_count": self.bad_count,
            "is_tripped": self.is_tripped,
        }

    def load_state_dict(self, state: dict[str, Any]) -> None:
        self.best = None if state.get("best") is None else float(state["best"])
        self.bad_count = int(state.get("bad_count", 0))
        self.is_tripped = bool(state.get("is_tripped", False))
