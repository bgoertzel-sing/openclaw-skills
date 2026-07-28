"""Intrinsic bridge clocks and feasibility reference governors."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Literal, Protocol

import numpy as np

from .types import ActuationPlan, ChannelState


class ProgressWarp(Protocol):
    def __call__(self, normalized_step: float) -> float:
        ...


@dataclass(frozen=True, slots=True)
class LinearWarp:
    def __call__(self, normalized_step: float) -> float:
        return float(np.clip(normalized_step, 0.0, 1.0))


@dataclass(frozen=True, slots=True)
class SmoothstepWarp:
    """Cubic endpoint-flat progress warp, ``3t² - 2t³``."""

    def __call__(self, normalized_step: float) -> float:
        t = float(np.clip(normalized_step, 0.0, 1.0))
        return t * t * (3.0 - 2.0 * t)


@dataclass(frozen=True, slots=True)
class SmootherstepWarp:
    """Quintic endpoint-flat progress warp, ``6t⁵ - 15t⁴ + 10t³``."""

    def __call__(self, normalized_step: float) -> float:
        t = float(np.clip(normalized_step, 0.0, 1.0))
        return t**3 * (t * (6.0 * t - 15.0) + 10.0)


@dataclass(frozen=True, slots=True)
class ClockDecision:
    requested_progress: float
    accepted_progress: float
    plan: ActuationPlan
    evaluations: int
    governed: bool


@dataclass(frozen=True, slots=True)
class FeasibilityClock:
    """A nominal clock wrapped in a one-dimensional reference governor.

    The clock proposes a physical-time progress point, asks the adapter whether
    the corresponding transition is realizable, and slows intrinsic progress
    when necessary.  It never advances the channel state by itself.
    """

    total_steps: int
    warp: ProgressWarp = SmootherstepWarp()
    search_points: int = 24
    bisection_steps: int = 20
    progress_tolerance: float = 1e-8
    permit_approximate_progress: bool = False

    def __post_init__(self) -> None:
        if self.total_steps <= 0:
            raise ValueError("total_steps must be positive.")
        if self.search_points < 2:
            raise ValueError("search_points must be at least 2.")
        if self.bisection_steps < 0:
            raise ValueError("bisection_steps must be non-negative.")
        if self.progress_tolerance <= 0.0:
            raise ValueError("progress_tolerance must be positive.")

    @classmethod
    def from_name(
        cls,
        *,
        total_steps: int,
        warp: Literal["linear", "smoothstep", "smootherstep"] = "smootherstep",
        **kwargs: object,
    ) -> "FeasibilityClock":
        warps: dict[str, ProgressWarp] = {
            "linear": LinearWarp(),
            "smoothstep": SmoothstepWarp(),
            "smootherstep": SmootherstepWarp(),
        }
        try:
            selected = warps[warp]
        except KeyError as exc:
            raise ValueError(f"unknown warp {warp!r}") from exc
        return cls(total_steps=total_steps, warp=selected, **kwargs)

    def nominal_progress(self, next_step: int) -> float:
        normalized = min(max(next_step / self.total_steps, 0.0), 1.0)
        return float(np.clip(self.warp(normalized), 0.0, 1.0))

    def choose(
        self,
        *,
        state: ChannelState,
        evaluate: Callable[[float], ActuationPlan],
    ) -> ClockDecision:
        requested = max(state.progress, self.nominal_progress(state.step + 1))
        requested = min(requested, 1.0)

        cache: dict[float, ActuationPlan] = {}

        def cached(progress: float) -> ActuationPlan:
            key = float(progress)
            if key not in cache:
                cache[key] = evaluate(key)
            return cache[key]

        requested_plan = cached(requested)
        if requested_plan.feasible:
            return ClockDecision(
                requested_progress=requested,
                accepted_progress=requested,
                plan=requested_plan,
                evaluations=len(cache),
                governed=False,
            )

        current = float(state.progress)
        if requested - current <= self.progress_tolerance:
            return ClockDecision(
                requested_progress=requested,
                accepted_progress=current,
                plan=requested_plan,
                evaluations=len(cache),
                governed=True,
            )

        # Search backward for the farthest feasible point.  Sampling rather
        # than assuming global monotonicity also handles a step that crosses a
        # covariance peak.
        grid = np.linspace(current, requested, self.search_points + 1)
        feasible_index: int | None = None
        best_index = 0
        best_error = np.inf
        for index in range(self.search_points, -1, -1):
            plan = cached(float(grid[index]))
            max_error = float(np.max(np.abs(plan.error)))
            if max_error < best_error:
                best_error = max_error
                best_index = index
            if plan.feasible:
                feasible_index = index
                break

        if feasible_index is None:
            selected_index = best_index if self.permit_approximate_progress else 0
            selected_progress = float(grid[selected_index])
            return ClockDecision(
                requested_progress=requested,
                accepted_progress=selected_progress,
                plan=cached(selected_progress),
                evaluations=len(cache),
                governed=True,
            )

        low = float(grid[feasible_index])
        if feasible_index == self.search_points:
            high = requested
        else:
            high = float(grid[feasible_index + 1])

        # Locally refine the feasible boundary.  The preceding grid search is
        # what makes this robust to non-monotone feasibility farther away.
        for _ in range(self.bisection_steps):
            if high - low <= self.progress_tolerance:
                break
            midpoint = 0.5 * (low + high)
            if cached(midpoint).feasible:
                low = midpoint
            else:
                high = midpoint

        accepted = low
        return ClockDecision(
            requested_progress=requested,
            accepted_progress=accepted,
            plan=cached(accepted),
            evaluations=len(cache),
            governed=True,
        )

    def done(self, state: ChannelState) -> bool:
        return state.progress >= 1.0 - self.progress_tolerance
