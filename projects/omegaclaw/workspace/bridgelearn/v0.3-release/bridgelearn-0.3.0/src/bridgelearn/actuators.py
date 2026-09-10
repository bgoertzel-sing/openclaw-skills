"""Actuators that map ideal Gaussian transitions to algorithm controls."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol, Sequence

import numpy as np
import numpy.typing as npt

from .types import (
    ActuationPlan,
    ChannelObservation,
    FloatArray,
    GaussianTransition,
    broadcast_array,
)


class TransitionActuator(Protocol):
    def realize(
        self,
        *,
        target: GaussianTransition,
        observation: ChannelObservation,
    ) -> ActuationPlan:
        ...


def _bounds(
    bounds: tuple[float | Sequence[float] | npt.ArrayLike, float | Sequence[float] | npt.ArrayLike],
    size: int,
    *,
    name: str,
) -> tuple[FloatArray, FloatArray]:
    low = broadcast_array(bounds[0], size, name=f"{name}_low")
    high = broadcast_array(bounds[1], size, name=f"{name}_high")
    if np.any(low < 0.0) or np.any(high < low):
        raise ValueError(f"invalid {name} bounds.")
    return low, high


def _rate_limit_positive(
    proposed: FloatArray,
    previous: FloatArray,
    max_log_change: float | None,
    *,
    floor: float = 1e-16,
) -> FloatArray:
    if max_log_change is None:
        return proposed
    if max_log_change <= 0.0:
        raise ValueError("max_log_change must be positive when supplied.")
    previous_safe = np.maximum(previous, floor)
    low = previous_safe * np.exp(-max_log_change)
    high = previous_safe * np.exp(max_log_change)
    return np.clip(proposed, low, high)



def _limit_contraction_slew(proposed: FloatArray, dynamics: Any) -> tuple[FloatArray, float]:
    """Rate-limit the induced first-order coefficient using observer bandwidth."""

    current = dynamics.step_size
    current_c = dynamics.contraction_at(current)
    proposed_c = dynamics.contraction_at(proposed)
    difference = np.abs(proposed_c - current_c)
    limit = dynamics.coefficient_slew_limit
    scale = np.minimum(1.0, limit / np.maximum(difference, 1e-30))
    limited = current + scale * (proposed - current)
    return limited, float(np.mean(scale < 1.0 - 1e-12))

def _plan(
    *,
    controls: dict[str, Any],
    predicted: GaussianTransition,
    target: GaussianTransition,
    observation: ChannelObservation,
    relative_tolerance: float,
    absolute_tolerance: float,
    diagnostics: dict[str, Any],
) -> ActuationPlan:
    current = observation.state.variance
    target_variance = target.next_variance(current)
    predicted_variance = predicted.next_variance(current)
    difference = predicted_variance - target_variance
    scale = np.maximum.reduce(
        [
            np.abs(target_variance),
            np.abs(current),
            np.full_like(current, absolute_tolerance),
        ]
    )
    relative_error = difference / scale
    allowed = absolute_tolerance + relative_tolerance * scale
    feasible = bool(np.all(np.abs(difference) <= allowed))
    diagnostics = {
        **diagnostics,
        "max_absolute_error": float(np.max(np.abs(difference))),
        "max_relative_error": float(np.max(np.abs(relative_error))),
    }
    return ActuationPlan(
        controls=controls,
        predicted=predicted,
        feasible=feasible,
        target_variance=target_variance,
        predicted_variance=predicted_variance,
        error=relative_error,
        diagnostics=diagnostics,
    )


@dataclass(frozen=True, slots=True)
class StepBatchActuator:
    """Realize contraction with blockwise steps and innovation with a resource.

    v0.2 prices compute explicitly and can quantize the effective batch or
    accumulation count.  With the default ``compute_price=0`` and no
    quantization it reduces to the v0.1 weighted least-squares coordinator.
    """

    step_bounds: tuple[
        float | Sequence[float] | npt.ArrayLike,
        float | Sequence[float] | npt.ArrayLike,
    ] = (0.0, np.inf)
    batch_bounds: tuple[float, float] = (1.0, np.inf)
    block_weights: float | Sequence[float] | npt.ArrayLike = 1.0
    stability_margin: float = 1.8
    edge_of_stability_threshold: float = 1.6
    curvature_floor: float = 1e-10
    relative_tolerance: float = 0.05
    absolute_tolerance: float = 1e-8
    max_log_step_change: float | None = 0.35
    max_log_batch_change: float | None = 0.70
    step_control_name: str = "step_size"
    batch_control_name: str = "effective_batch"
    refinement_iterations: int = 3
    compute_price: float = 0.0
    batch_quantum: float | None = None
    batch_values: tuple[float, ...] | None = None
    resource_deadband: float = 0.03
    compute_reference: float | None = None
    dominant_coordinator: Any | None = None

    def __post_init__(self) -> None:
        if self.batch_bounds[0] <= 0.0 or self.batch_bounds[1] < self.batch_bounds[0]:
            raise ValueError("invalid batch_bounds.")
        if self.stability_margin <= 0.0 or self.stability_margin >= 2.0:
            raise ValueError("stability_margin must lie in (0, 2).")
        if not 0.0 < self.edge_of_stability_threshold < 2.0:
            raise ValueError("edge_of_stability_threshold must lie in (0, 2).")
        if self.curvature_floor <= 0.0:
            raise ValueError("curvature_floor must be positive.")
        if self.relative_tolerance < 0.0 or self.absolute_tolerance < 0.0:
            raise ValueError("tolerances must be non-negative.")
        if self.compute_price < 0.0:
            raise ValueError("compute_price must be non-negative.")
        if self.batch_quantum is not None and self.batch_quantum <= 0.0:
            raise ValueError("batch_quantum must be positive.")
        if self.resource_deadband < 0.0:
            raise ValueError("resource_deadband must be non-negative.")
        if self.batch_values is not None:
            if not self.batch_values or any(value <= 0.0 for value in self.batch_values):
                raise ValueError("batch_values must contain positive values.")

    def _candidate_batches(self, continuous: float, previous: float) -> np.ndarray:
        low, high = map(float, self.batch_bounds)
        if self.batch_values is not None:
            candidates = np.asarray(
                [value for value in self.batch_values if low <= value <= high],
                dtype=np.float64,
            )
            if candidates.size == 0:
                raise ValueError("batch_values contain no value inside batch_bounds.")
            return np.unique(candidates)
        if self.batch_quantum is not None and np.isfinite(high):
            quantum = float(self.batch_quantum)
            first = np.ceil(low / quantum) * quantum
            count = int(np.floor((high - first) / quantum)) + 1
            if count <= 4096:
                values = first + quantum * np.arange(max(count, 1))
                return np.unique(np.clip(np.r_[values, low, high, continuous, previous], low, high))
        if self.compute_price == 0.0 and self.batch_quantum is None:
            return np.asarray([np.clip(continuous, low, high)], dtype=np.float64)
        if np.isfinite(high):
            grid = np.geomspace(low, high, 96)
        else:
            upper = max(low * 1024.0, continuous * 8.0, previous * 8.0)
            grid = np.geomspace(low, upper, 96)
        return np.unique(np.clip(np.r_[grid, continuous, previous, low, high], low, high))

    def _choose_batch(
        self,
        *,
        step: FloatArray,
        desired_innovation: FloatArray,
        dynamics: Any,
        weights: FloatArray,
    ) -> tuple[float, dict[str, float]]:
        coefficient = step**2 * dynamics.noise_scale
        denominator = float(np.sum(weights * coefficient**2))
        numerator = float(np.sum(weights * coefficient * np.maximum(desired_innovation, 0.0)))
        low, high = map(float, self.batch_bounds)
        if denominator <= 1e-30 or numerator <= 0.0:
            continuous = high
        else:
            inverse_batch = numerator / denominator
            continuous = np.inf if inverse_batch <= 0.0 else 1.0 / inverse_batch
        continuous = float(np.clip(continuous, low, high))
        previous = float(np.clip(dynamics.effective_batch, low, high))
        candidates = self._candidate_batches(continuous, previous)
        reference = self.compute_reference or low
        scale = np.maximum.reduce(
            [
                np.abs(desired_innovation),
                coefficient / max(previous, 1e-12),
                np.full_like(coefficient, 1e-12),
            ]
        )

        def objective(batch: float) -> float:
            tracking = float(
                np.sum(weights * ((coefficient / batch - desired_innovation) / scale) ** 2)
            )
            compute = self.compute_price * max(batch / reference - 1.0, 0.0)
            return tracking + compute

        values = np.asarray([objective(float(batch)) for batch in candidates])
        best_index = int(np.argmin(values))
        selected = float(candidates[best_index])
        best_value = float(values[best_index])
        previous_value = objective(previous)
        if previous_value <= best_value * (1.0 + self.resource_deadband) + 1e-12:
            selected = previous
            best_value = previous_value
        return selected, {
            "continuous_batch": continuous,
            "resource_objective": best_value,
            "compute_units": selected / reference,
            "compute_price": self.compute_price,
            "batch_quantized": float(not np.isclose(selected, continuous)),
        }

    def _stability_high(self, dynamics: Any, step_high: FloatArray) -> FloatArray:
        safe_curvature = np.maximum(dynamics.curvature_upper, self.curvature_floor)
        return np.minimum.reduce(
            [
                step_high,
                self.stability_margin / safe_curvature,
                dynamics.trust_region_step,
            ]
        )

    def _enforce_endogenous_stability(
        self, step: FloatArray, dynamics: Any, low: FloatArray, high: FloatArray
    ) -> FloatArray:
        result = np.clip(step, low, high)
        for _ in range(12):
            _lower_h, upper_h = dynamics.curvature_bounds_at(result)
            ratio = result * upper_h
            unsafe = ratio > self.stability_margin
            if not np.any(unsafe):
                break
            result = np.where(unsafe, 0.85 * result, result)
        return np.clip(result, low, high)

    def realize(
        self,
        *,
        target: GaussianTransition,
        observation: ChannelObservation,
    ) -> ActuationPlan:
        dynamics = observation.local_dynamics
        if dynamics is None:
            raise ValueError("StepBatchActuator requires observation.local_dynamics.")
        size = dynamics.size
        if target.size != size:
            raise ValueError("target and local dynamics sizes do not match.")

        step_low, step_high = _bounds(self.step_bounds, size, name="step")
        weights = broadcast_array(self.block_weights, size, name="block_weights")
        if np.any(weights < 0.0) or not np.any(weights > 0.0):
            raise ValueError("block_weights must be non-negative with at least one positive entry.")

        valid_curvature = dynamics.curvature > self.curvature_floor
        desired_step = dynamics.step_for_contraction(
            target.contraction,
            curvature_floor=self.curvature_floor,
            curvature_override=dynamics.curvature_lower,
        )
        desired_step = np.where(valid_curvature, desired_step, dynamics.step_size)
        effective_high = self._stability_high(dynamics, step_high)
        desired_step = self._enforce_endogenous_stability(
            desired_step, dynamics, step_low, effective_high
        )
        desired_step = _rate_limit_positive(
            desired_step, dynamics.step_size, self.max_log_step_change
        )
        desired_step, coefficient_slew_fraction = _limit_contraction_slew(
            desired_step, dynamics
        )
        desired_step = self._enforce_endogenous_stability(
            desired_step, dynamics, step_low, effective_high
        )

        confidence = observation.state.confidence
        step = confidence * desired_step + (1.0 - confidence) * dynamics.step_size
        step = self._enforce_endogenous_stability(step, dynamics, step_low, effective_high)
        dominant_diag: dict[str, Any] = {}
        if self.dominant_coordinator is not None:
            step, dominant_diag = self.dominant_coordinator.scale_steps(
                step, dynamics.momentum, dynamics.curvature_upper
            )
            step = self._enforce_endogenous_stability(step, dynamics, step_low, effective_high)
        target_variance = target.next_variance(dynamics.variance)

        proposed_batch, resource_diag = self._choose_batch(
            step=step,
            desired_innovation=target.innovation,
            dynamics=dynamics,
            weights=weights,
        )

        for _ in range(max(self.refinement_iterations, 0)):
            q = dynamics.noise_scale / proposed_batch
            projected_step = np.empty_like(step)
            effective_curvature, _upper_refinement = dynamics.curvature_bounds_at(step)
            for index in range(size):
                projected_step[index] = _closest_variance_step(
                    current_variance=float(dynamics.variance[index]),
                    target_variance=float(target_variance[index]),
                    curvature=float(effective_curvature[index]),
                    noise=float(q[index]),
                    preferred=float(desired_step[index]),
                    low=float(step_low[index]),
                    high=float(effective_high[index]),
                )
            projected_step = _rate_limit_positive(
                projected_step, dynamics.step_size, self.max_log_step_change
            )
            step = self._enforce_endogenous_stability(
                projected_step, dynamics, step_low, effective_high
            )
            lower_contraction, _upper_contraction = dynamics.contraction_bounds_at(step)
            deterministic = lower_contraction**2 * dynamics.variance
            required_innovation = np.maximum(target_variance - deterministic, 0.0)
            proposed_batch, resource_diag = self._choose_batch(
                step=step,
                desired_innovation=required_innovation,
                dynamics=dynamics,
                weights=weights,
            )

        if self.max_log_batch_change is not None and np.isfinite(dynamics.effective_batch):
            previous = max(float(dynamics.effective_batch), 1e-16)
            proposed_batch = float(
                np.clip(
                    proposed_batch,
                    previous * np.exp(-self.max_log_batch_change),
                    previous * np.exp(self.max_log_batch_change),
                )
            )
            proposed_batch = float(np.clip(proposed_batch, *self.batch_bounds))

        contraction = dynamics.contraction_at(step)
        innovation = step**2 * dynamics.noise_scale / proposed_batch
        predicted = GaussianTransition(contraction=contraction, innovation=innovation)
        _lower_h_final, upper_h_final = dynamics.curvature_bounds_at(step)
        ratio = step * upper_h_final
        diagnostics = {
            "step_saturated_fraction": float(
                np.mean(np.isclose(step, step_low) | np.isclose(step, effective_high))
            ),
            "batch_saturated": bool(
                np.isclose(proposed_batch, self.batch_bounds[0])
                or np.isclose(proposed_batch, self.batch_bounds[1])
            ),
            "requested_batch": proposed_batch,
            "invalid_curvature_fraction": float(np.mean(~valid_curvature)),
            "coefficient_slew_limited_fraction": coefficient_slew_fraction,
            "edge_of_stability_fraction": float(
                np.mean(ratio >= self.edge_of_stability_threshold)
            ),
            "curvature_endogeneity_fraction": float(
                np.mean(np.abs(dynamics.curvature_slope) > 1e-14)
            ),
            "curvature_funnel_relative_width": (
                (dynamics.curvature_upper - dynamics.curvature_lower)
                / np.maximum(dynamics.curvature, self.curvature_floor)
            ),
            "robust_stability_satisfied": bool(np.all(ratio <= self.stability_margin)),
            **resource_diag,
            **dominant_diag,
        }
        controls = {
            self.step_control_name: step.copy(),
            self.batch_control_name: proposed_batch,
        }
        plan = _plan(
            controls=controls,
            predicted=predicted,
            target=target,
            observation=observation,
            relative_tolerance=self.relative_tolerance,
            absolute_tolerance=self.absolute_tolerance,
            diagnostics=diagnostics,
        )
        lower_contraction, _upper_contraction = dynamics.contraction_bounds_at(step)
        contraction_scale = np.maximum(np.abs(target.contraction), 1.0)
        lower_match = np.abs(lower_contraction - target.contraction) <= (
            self.absolute_tolerance + self.relative_tolerance * contraction_scale
        )
        robust_feasible = bool(np.all(lower_match) and np.all(ratio <= self.stability_margin))
        if robust_feasible and not plan.feasible:
            return ActuationPlan(
                controls=plan.controls,
                predicted=plan.predicted,
                feasible=True,
                target_variance=plan.target_variance,
                predicted_variance=plan.predicted_variance,
                error=plan.error,
                diagnostics={
                    **dict(plan.diagnostics),
                    "robust_funnel_projection": True,
                    "lower_edge_contraction": lower_contraction,
                },
            )
        return plan


@dataclass(frozen=True, slots=True)
class StepNoiseActuator:
    """Realize contraction with step size and innovation with explicit noise."""

    step_bounds: tuple[
        float | Sequence[float] | npt.ArrayLike,
        float | Sequence[float] | npt.ArrayLike,
    ] = (0.0, np.inf)
    noise_std_bounds: tuple[
        float | Sequence[float] | npt.ArrayLike,
        float | Sequence[float] | npt.ArrayLike,
    ] = (0.0, np.inf)
    stability_margin: float = 1.8
    curvature_floor: float = 1e-10
    relative_tolerance: float = 0.02
    absolute_tolerance: float = 1e-8
    max_log_step_change: float | None = 0.35
    dominant_coordinator: Any | None = None
    step_control_name: str = "step_size"
    noise_control_name: str = "noise_std"

    def realize(
        self,
        *,
        target: GaussianTransition,
        observation: ChannelObservation,
    ) -> ActuationPlan:
        dynamics = observation.local_dynamics
        if dynamics is None:
            raise ValueError("StepNoiseActuator requires observation.local_dynamics.")
        size = dynamics.size
        step_low, step_high = _bounds(self.step_bounds, size, name="step")
        noise_low, noise_high = _bounds(self.noise_std_bounds, size, name="noise_std")
        safe_curvature = np.maximum(dynamics.curvature_upper, self.curvature_floor)
        valid_curvature = dynamics.curvature_lower > self.curvature_floor

        step = dynamics.step_for_contraction(
            target.contraction,
            curvature_floor=self.curvature_floor,
            curvature_override=dynamics.curvature_lower,
        )
        step = np.where(valid_curvature, step, dynamics.step_size)
        effective_high = np.minimum.reduce(
            [step_high, self.stability_margin / safe_curvature, dynamics.trust_region_step]
        )
        step = np.clip(step, step_low, effective_high)
        step = _rate_limit_positive(step, dynamics.step_size, self.max_log_step_change)
        step, coefficient_slew_fraction = _limit_contraction_slew(step, dynamics)
        step = np.clip(step, step_low, effective_high)
        for _ in range(12):
            _lower_bound, upper_bound = dynamics.curvature_bounds_at(step)
            unsafe = step * upper_bound > self.stability_margin
            if not np.any(unsafe):
                break
            step = np.where(unsafe, 0.85 * step, step)
        step = observation.state.confidence * step + (
            1.0 - observation.state.confidence
        ) * dynamics.step_size
        step = np.clip(step, step_low, effective_high)
        dominant_diag: dict[str, Any] = {}
        if self.dominant_coordinator is not None:
            step, dominant_diag = self.dominant_coordinator.scale_steps(
                step, dynamics.momentum, dynamics.curvature_upper
            )
            step = np.clip(step, step_low, effective_high)

        noise_std = np.sqrt(np.maximum(target.innovation, 0.0))
        noise_std = np.clip(noise_std, noise_low, noise_high)

        predicted = GaussianTransition(
            contraction=dynamics.contraction_at(step),
            innovation=noise_std**2,
        )
        controls = {
            self.step_control_name: step.copy(),
            self.noise_control_name: noise_std.copy(),
        }
        return _plan(
            controls=controls,
            predicted=predicted,
            target=target,
            observation=observation,
            relative_tolerance=self.relative_tolerance,
            absolute_tolerance=self.absolute_tolerance,
            diagnostics={
                "coefficient_slew_limited_fraction": coefficient_slew_fraction,
                "step_saturated_fraction": float(
                    np.mean(np.isclose(step, step_low) | np.isclose(step, effective_high))
                ),
                "coefficient_slew_limited_fraction": coefficient_slew_fraction,
                "noise_saturated_fraction": float(
                    np.mean(np.isclose(noise_std, noise_low) | np.isclose(noise_std, noise_high))
                ),
                "curvature_funnel_relative_width": (
                    (dynamics.curvature_upper - dynamics.curvature_lower)
                    / np.maximum(dynamics.curvature, self.curvature_floor)
                ),
                **dominant_diag,
            },
        )


@dataclass(frozen=True, slots=True)
class StepOnlyActuator:
    """Project an ideal transition onto a fixed-noise, fixed-batch step control.

    Each block solves a small bounded one-dimensional problem.  This is the
    appropriate fallback when a training loop cannot change batch size or add
    explicit innovation.
    """

    step_bounds: tuple[
        float | Sequence[float] | npt.ArrayLike,
        float | Sequence[float] | npt.ArrayLike,
    ] = (0.0, np.inf)
    stability_margin: float = 1.8
    curvature_floor: float = 1e-10
    contraction_weight: float = 1.0
    innovation_weight: float = 1.0
    smoothness_weight: float = 0.05
    relative_tolerance: float = 0.08
    absolute_tolerance: float = 1e-8
    max_log_step_change: float | None = 0.35
    golden_iterations: int = 48
    step_control_name: str = "step_size"

    def realize(
        self,
        *,
        target: GaussianTransition,
        observation: ChannelObservation,
    ) -> ActuationPlan:
        dynamics = observation.local_dynamics
        if dynamics is None:
            raise ValueError("StepOnlyActuator requires observation.local_dynamics.")
        size = dynamics.size
        low, high = _bounds(self.step_bounds, size, name="step")
        safe_h = np.maximum(dynamics.curvature_upper, self.curvature_floor)
        high = np.minimum.reduce(
            [high, self.stability_margin / safe_h, dynamics.trust_region_step]
        )
        q = dynamics.noise_scale / dynamics.effective_batch
        result = np.empty(size, dtype=np.float64)

        for index in range(size):
            if dynamics.curvature[index] <= self.curvature_floor:
                result[index] = dynamics.step_size[index]
                continue
            lo = float(low[index])
            hi = float(high[index])
            if not np.isfinite(hi):
                hi = self.stability_margin / float(safe_h[index])
            result[index] = _golden_minimize(
                lambda eta, i=index: self._objective(
                    eta=eta,
                    curvature=float(dynamics.curvature[i]),
                    noise=float(q[i]),
                    target_contraction=float(target.contraction[i]),
                    target_innovation=float(target.innovation[i]),
                    previous_step=float(dynamics.step_size[i]),
                ),
                lo,
                hi,
                iterations=self.golden_iterations,
            )

        result = _rate_limit_positive(result, dynamics.step_size, self.max_log_step_change)
        result, coefficient_slew_fraction = _limit_contraction_slew(result, dynamics)
        result = np.clip(result, low, high)
        result = observation.state.confidence * result + (
            1.0 - observation.state.confidence
        ) * dynamics.step_size
        predicted = GaussianTransition(
            contraction=dynamics.contraction_at(result),
            innovation=result**2 * q,
        )
        return _plan(
            controls={self.step_control_name: result.copy()},
            predicted=predicted,
            target=target,
            observation=observation,
            relative_tolerance=self.relative_tolerance,
            absolute_tolerance=self.absolute_tolerance,
            diagnostics={
                "step_saturated_fraction": float(
                    np.mean(np.isclose(result, low) | np.isclose(result, high))
                )
            },
        )

    def _objective(
        self,
        *,
        eta: float,
        curvature: float,
        noise: float,
        target_contraction: float,
        target_innovation: float,
        previous_step: float,
    ) -> float:
        contraction = 1.0 - eta * curvature
        innovation = eta * eta * noise
        innovation_scale = max(target_innovation, noise * previous_step**2, 1e-12)
        smooth = np.log(max(eta, 1e-16) / max(previous_step, 1e-16))
        return float(
            self.contraction_weight * (contraction - target_contraction) ** 2
            + self.innovation_weight
            * ((innovation - target_innovation) / innovation_scale) ** 2
            + self.smoothness_weight * smooth**2
        )


@dataclass(frozen=True, slots=True)
class DirectTransitionActuator:
    """Expose ideal contraction and innovation directly as controls."""

    contraction_control_name: str = "contraction"
    innovation_control_name: str = "innovation"

    def realize(
        self,
        *,
        target: GaussianTransition,
        observation: ChannelObservation,
    ) -> ActuationPlan:
        return _plan(
            controls={
                self.contraction_control_name: target.contraction.copy(),
                self.innovation_control_name: target.innovation.copy(),
            },
            predicted=target,
            target=target,
            observation=observation,
            relative_tolerance=0.0,
            absolute_tolerance=1e-12,
            diagnostics={},
        )


def _closest_variance_step(
    *,
    current_variance: float,
    target_variance: float,
    curvature: float,
    noise: float,
    preferred: float,
    low: float,
    high: float,
) -> float:
    """Closest preferred step among exact roots, or best reachable step."""

    if high <= low:
        return low
    if curvature <= 0.0:
        candidates = np.asarray([low, high, preferred], dtype=np.float64)
    else:
        coefficient = curvature * curvature * current_variance + noise
        radicand = coefficient * target_variance - noise * current_variance
        roots: list[float] = []
        if coefficient > 0.0 and radicand >= 0.0:
            root_term = np.sqrt(max(radicand, 0.0))
            roots.extend(
                [
                    (curvature * current_variance - root_term) / coefficient,
                    (curvature * current_variance + root_term) / coefficient,
                ]
            )
        minimizer = curvature * current_variance / max(coefficient, 1e-30)
        candidates = np.asarray([low, high, preferred, minimizer, *roots], dtype=np.float64)
    candidates = np.clip(candidates[np.isfinite(candidates)], low, high)
    if candidates.size == 0:
        return float(np.clip(preferred, low, high))
    predicted = (1.0 - candidates * curvature) ** 2 * current_variance + candidates**2 * noise
    error = np.abs(predicted - target_variance)
    minimum = np.min(error)
    near_best = np.flatnonzero(error <= minimum + 1e-12 * max(1.0, abs(target_variance)))
    if near_best.size == 1:
        return float(candidates[near_best[0]])
    preferred_distance = np.abs(candidates[near_best] - preferred)
    return float(candidates[near_best[np.argmin(preferred_distance)]])


def _golden_minimize(
    function: Any,
    low: float,
    high: float,
    *,
    iterations: int,
) -> float:
    if high <= low:
        return low
    ratio = 0.5 * (np.sqrt(5.0) - 1.0)
    x1 = high - ratio * (high - low)
    x2 = low + ratio * (high - low)
    f1 = float(function(x1))
    f2 = float(function(x2))
    for _ in range(iterations):
        if f1 <= f2:
            high = x2
            x2 = x1
            f2 = f1
            x1 = high - ratio * (high - low)
            f1 = float(function(x1))
        else:
            low = x1
            x1 = x2
            f1 = f2
            x2 = low + ratio * (high - low)
            f2 = float(function(x2))
    return 0.5 * (low + high)


@dataclass(frozen=True, slots=True)
class MomentumStepBatchActuator:
    """Momentum-aware contraction/innovation actuation in the AR(2) triangle.

    The target remains the scalar marginal Gaussian transition used by the
    reference-consistent bridge.  The actuator uses the declared lag covariance
    to realize its desired adjacent cross-covariance with heavy-ball controls,
    while checking the full companion matrix at the *upper* sharpness-funnel
    edge.  Contraction inversion uses the *lower* edge.

    For a candidate momentum ``mu`` and desired marginal contraction ``a``,

    ``c2 = -mu`` and ``c1*V + c2*C = a*V``

    determine ``c1``.  The learning rate follows from
    ``eta = (1 + mu - c1) / h_lower``.  A small grid over ``mu`` is sufficient;
    everything else is closed form.
    """

    step_bounds: tuple[
        float | Sequence[float] | npt.ArrayLike,
        float | Sequence[float] | npt.ArrayLike,
    ] = (0.0, np.inf)
    momentum_bounds: tuple[
        float | Sequence[float] | npt.ArrayLike,
        float | Sequence[float] | npt.ArrayLike,
    ] = (0.0, 0.999)
    batch_bounds: tuple[float, float] = (1.0, np.inf)
    block_weights: float | Sequence[float] | npt.ArrayLike = 1.0
    control_momentum: bool = True
    momentum_grid_points: int = 33
    safety_offset: float = 0.1
    triangle_margin: float = 1e-4
    max_spectral_radius: float = 0.999
    max_lyapunov_condition: float = 1e6
    rho_bar_slack: float = 0.02
    curvature_floor: float = 1e-10
    relative_tolerance: float = 0.08
    absolute_tolerance: float = 1e-8
    max_log_step_change: float | None = 0.35
    max_momentum_change: float | None = 0.03
    max_log_batch_change: float | None = 0.70
    compute_price: float = 0.0
    batch_quantum: float | None = None
    batch_values: tuple[float, ...] | None = None
    resource_deadband: float = 0.03
    compute_reference: float | None = None
    smoothness_weight: float = 0.02
    conditioning_weight: float = 1e-4
    dominant_coordinator: Any | None = None
    step_control_name: str = "step_size"
    momentum_control_name: str = "momentum"
    batch_control_name: str = "effective_batch"

    def __post_init__(self) -> None:
        if self.momentum_grid_points < 2:
            raise ValueError("momentum_grid_points must be at least two.")
        if self.safety_offset < 0.0:
            raise ValueError("safety_offset must be non-negative.")
        if not 0.0 <= self.triangle_margin < 1.0:
            raise ValueError("triangle_margin must lie in [0,1).")
        if not 0.0 < self.max_spectral_radius < 1.0:
            raise ValueError("max_spectral_radius must lie in (0,1).")
        if self.max_lyapunov_condition <= 1.0:
            raise ValueError("max_lyapunov_condition must exceed one.")
        if self.rho_bar_slack <= 0.0:
            raise ValueError("rho_bar_slack must be positive.")
        if self.batch_bounds[0] <= 0.0 or self.batch_bounds[1] < self.batch_bounds[0]:
            raise ValueError("invalid batch_bounds.")
        if self.batch_quantum is not None and self.batch_quantum <= 0.0:
            raise ValueError("batch_quantum must be positive.")
        if self.compute_price < 0.0:
            raise ValueError("compute_price must be non-negative.")

    def _momentum_candidates(self, current: float, low: float, high: float) -> FloatArray:
        if not self.control_momentum or np.isclose(low, high):
            return np.asarray([float(np.clip(current, low, high))])
        grid = np.linspace(low, high, self.momentum_grid_points)
        return np.unique(np.clip(np.r_[grid, current, 0.0], low, high))

    def _batch_candidates(self, continuous: float, previous: float) -> FloatArray:
        low, high = map(float, self.batch_bounds)
        if self.batch_values is not None:
            values = np.asarray(
                [value for value in self.batch_values if low <= value <= high],
                dtype=np.float64,
            )
            if values.size == 0:
                raise ValueError("batch_values contain no feasible value.")
            return np.unique(values)
        if self.batch_quantum is not None and np.isfinite(high):
            quantum = float(self.batch_quantum)
            first = np.ceil(low / quantum) * quantum
            count = int(np.floor((high - first) / quantum)) + 1
            if count <= 4096:
                grid = first + quantum * np.arange(max(count, 1))
                return np.unique(np.clip(np.r_[grid, continuous, previous, low, high], low, high))
        if self.compute_price == 0.0 and self.batch_quantum is None:
            return np.asarray([float(np.clip(continuous, low, high))])
        upper = high if np.isfinite(high) else max(low * 1024.0, continuous * 8.0, previous * 8.0)
        return np.unique(
            np.clip(np.r_[np.geomspace(low, upper, 96), continuous, previous], low, high)
        )

    def _choose_batch(
        self,
        *,
        coefficient: FloatArray,
        desired_innovation: FloatArray,
        previous: float,
        weights: FloatArray,
    ) -> tuple[float, dict[str, float]]:
        denominator = float(np.sum(weights * coefficient**2))
        numerator = float(np.sum(weights * coefficient * np.maximum(desired_innovation, 0.0)))
        low, high = map(float, self.batch_bounds)
        continuous = high if denominator <= 1e-30 or numerator <= 0.0 else 1.0 / (numerator / denominator)
        continuous = float(np.clip(continuous, low, high))
        previous = float(np.clip(previous, low, high))
        candidates = self._batch_candidates(continuous, previous)
        reference = self.compute_reference or low
        scale = np.maximum.reduce(
            [np.abs(desired_innovation), coefficient / max(previous, 1e-12), np.full_like(coefficient, 1e-12)]
        )

        def objective(batch: float) -> float:
            tracking = float(np.sum(weights * ((coefficient / batch - desired_innovation) / scale) ** 2))
            compute = self.compute_price * max(batch / reference - 1.0, 0.0)
            return tracking + compute

        scores = np.asarray([objective(float(value)) for value in candidates])
        selected = float(candidates[int(np.argmin(scores))])
        selected_score = float(np.min(scores))
        previous_score = objective(previous)
        if previous_score <= selected_score * (1.0 + self.resource_deadband) + 1e-12:
            selected = previous
            selected_score = previous_score
        return selected, {
            "continuous_batch": continuous,
            "resource_objective": selected_score,
            "compute_units": selected / reference,
            "batch_quantized": float(not np.isclose(selected, continuous)),
        }

    def realize(
        self,
        *,
        target: GaussianTransition,
        observation: ChannelObservation,
    ) -> ActuationPlan:
        from .stability import (
            damping_regime,
            inside_stability_triangle,
            lyapunov_metric,
            spectral_radius,
        )

        dynamics = observation.local_dynamics
        if dynamics is None:
            raise ValueError("MomentumStepBatchActuator requires local_dynamics.")
        size = dynamics.size
        if target.size != size:
            raise ValueError("target and local dynamics sizes do not match.")
        step_low, step_high = _bounds(self.step_bounds, size, name="step")
        mu_low, mu_high = _bounds(self.momentum_bounds, size, name="momentum")
        if np.any(mu_high >= 1.0):
            raise ValueError("momentum upper bounds must be below one.")
        weights = broadcast_array(self.block_weights, size, name="block_weights")
        lower_h = np.maximum(dynamics.curvature_lower, self.curvature_floor)
        upper_h = np.maximum(dynamics.curvature_upper, lower_h)
        center_h = dynamics.curvature
        target_variance = target.next_variance(dynamics.variance)

        step = np.empty(size, dtype=np.float64)
        momentum = np.empty(size, dtype=np.float64)
        c1_center = np.empty(size, dtype=np.float64)
        c2 = np.empty(size, dtype=np.float64)
        deterministic = np.empty(size, dtype=np.float64)
        radii = np.empty(size, dtype=np.float64)
        conditions = np.empty(size, dtype=np.float64)
        regimes: list[str] = []
        candidate_found = np.ones(size, dtype=bool)
        contraction_floor_binding = np.zeros(size, dtype=bool)

        for index in range(size):
            variance = float(dynamics.variance[index])
            previous_variance = float(dynamics.previous_variance[index])
            lag = float(dynamics.lag_covariance[index])
            desired_cross = float(target.contraction[index]) * variance
            current_mu = float(dynamics.momentum[index])
            current_step = float(dynamics.step_size[index])
            best: tuple[float, float, float, float, float, str, float] | None = None
            for mu in self._momentum_candidates(
                current_mu, float(mu_low[index]), float(mu_high[index])
            ):
                if variance <= 1e-30:
                    desired_c1 = 1.0 + mu - current_step * float(lower_h[index])
                else:
                    desired_c1 = (desired_cross + mu * lag) / variance
                eta = (1.0 + mu - desired_c1) / float(lower_h[index])
                if not np.isfinite(eta):
                    continue
                eta = float(np.clip(eta, step_low[index], min(step_high[index], dynamics.trust_region_step[index])))
                if self.max_log_step_change is not None:
                    eta = float(
                        _rate_limit_positive(
                            np.asarray([eta]),
                            np.asarray([current_step]),
                            self.max_log_step_change,
                        )[0]
                    )
                if self.max_momentum_change is not None:
                    mu = float(np.clip(mu, current_mu - self.max_momentum_change, current_mu + self.max_momentum_change))
                    mu = float(np.clip(mu, mu_low[index], mu_high[index]))
                candidate_c1_upper = 1.0 + mu - eta * float(upper_h[index])
                candidate_c2 = -mu
                if not inside_stability_triangle(
                    candidate_c1_upper, candidate_c2, margin=self.triangle_margin
                ):
                    continue
                rho = spectral_radius(candidate_c1_upper, candidate_c2)
                if rho > self.max_spectral_radius:
                    continue
                try:
                    _metric, _rho_bar, kappa = lyapunov_metric(
                        candidate_c1_upper,
                        candidate_c2,
                        rho_bar=min(
                            0.999999,
                            max(rho + self.rho_bar_slack, 0.5 * (1.0 + rho)),
                        ),
                    )
                except ValueError:
                    continue
                if kappa > self.max_lyapunov_condition:
                    continue
                current_c1 = 1.0 + current_mu - current_step * float(center_h[index])
                coefficient_slew = max(
                    abs((1.0 + mu - eta * float(center_h[index])) - current_c1),
                    abs(mu - current_mu),
                )
                if coefficient_slew > float(dynamics.coefficient_slew_limit[index]):
                    continue
                center_c1 = 1.0 + mu - eta * float(center_h[index])
                predicted_cross = center_c1 * variance - mu * lag
                det = (
                    center_c1**2 * variance
                    + mu**2 * previous_variance
                    - 2.0 * center_c1 * mu * lag
                )
                cross_scale = max(abs(desired_cross), variance, 1e-12)
                variance_scale = max(abs(float(target_variance[index])), variance, 1e-12)
                cross_error = ((predicted_cross - desired_cross) / cross_scale) ** 2
                overshoot = max(det - float(target_variance[index]), 0.0) / variance_scale
                smooth = self.smoothness_weight * (
                    np.log(max(eta, 1e-16) / max(current_step, 1e-16)) ** 2
                    + (mu - current_mu) ** 2
                )
                objective = cross_error + overshoot**2 + smooth + self.conditioning_weight * np.log1p(kappa)
                regime = damping_regime(candidate_c1_upper, candidate_c2)
                if regime == "underdamped":
                    floor = np.sqrt(mu)
                    requested = np.sqrt(
                        max(float(target_variance[index]), 0.0) / max(variance, 1e-30)
                    )
                    if requested < floor:
                        objective += (floor - requested) ** 2
                record = (objective, eta, mu, center_c1, rho, regime, kappa)
                if best is None or record[0] < best[0]:
                    best = record
            if best is None:
                candidate_found[index] = False
                mu = float(np.clip(current_mu, mu_low[index], mu_high[index]))
                eta = min(
                    current_step,
                    float(dynamics.trust_region_step[index]),
                    max(
                        (2.0 * (1.0 + mu) - self.safety_offset)
                        / max(float(upper_h[index]), self.curvature_floor),
                        0.0,
                    ),
                )
                center_c1 = 1.0 + mu - eta * float(center_h[index])
                candidate_c1_upper = 1.0 + mu - eta * float(upper_h[index])
                rho = spectral_radius(candidate_c1_upper, -mu)
                try:
                    _p, _r, kappa = lyapunov_metric(candidate_c1_upper, -mu)
                except ValueError:
                    kappa = float("inf")
                regime = damping_regime(candidate_c1_upper, -mu)
            else:
                _objective, eta, mu, center_c1, rho, regime, kappa = best
            step[index] = eta
            momentum[index] = mu
            c1_center[index] = center_c1
            c2[index] = -mu
            deterministic[index] = (
                center_c1**2 * variance
                + mu**2 * previous_variance
                - 2.0 * center_c1 * mu * lag
            )
            radii[index] = rho
            conditions[index] = kappa
            regimes.append(regime)
            if regime == "underdamped":
                requested = np.sqrt(
                    max(float(target_variance[index]), 0.0) / max(variance, 1e-30)
                )
                contraction_floor_binding[index] = requested < np.sqrt(mu)

        dominant_diagnostics: dict[str, Any] = {}
        if self.dominant_coordinator is not None:
            step, dominant_diagnostics = self.dominant_coordinator.scale_steps(
                step, momentum, upper_h
            )

        # Recompute every companion diagnostic after shared/global scaling.
        # Reducing eta can move an overdamped pole back toward +1, so an edge
        # utilization cap alone is not a substitute for a full triangle check.
        c1_center = 1.0 + momentum - step * center_h
        c2 = -momentum
        deterministic = (
            c1_center**2 * dynamics.variance
            + momentum**2 * dynamics.previous_variance
            - 2.0 * c1_center * momentum * dynamics.lag_covariance
        )
        regimes = []
        for index in range(size):
            c1_upper = 1.0 + float(momentum[index]) - float(step[index]) * float(upper_h[index])
            c2_value = -float(momentum[index])
            stable = inside_stability_triangle(
                c1_upper, c2_value, margin=self.triangle_margin
            )
            rho = spectral_radius(c1_upper, c2_value)
            kappa = float("inf")
            if stable and rho < 1.0:
                try:
                    _metric, _rho_bar, kappa = lyapunov_metric(
                        c1_upper,
                        c2_value,
                        rho_bar=min(
                            0.999999,
                            max(rho + self.rho_bar_slack, 0.5 * (1.0 + rho)),
                        ),
                    )
                except ValueError:
                    stable = False
            current_c1 = (
                1.0
                + float(dynamics.momentum[index])
                - float(dynamics.step_size[index]) * float(center_h[index])
            )
            coefficient_slew = max(
                abs(float(c1_center[index]) - current_c1),
                abs(float(momentum[index]) - float(dynamics.momentum[index])),
            )
            if (
                not stable
                or rho > self.max_spectral_radius
                or kappa > self.max_lyapunov_condition
                or coefficient_slew > float(dynamics.coefficient_slew_limit[index])
            ):
                candidate_found[index] = False
            radii[index] = rho
            conditions[index] = kappa
            regime = damping_regime(c1_upper, c2_value)
            regimes.append(regime)
            if regime == "underdamped":
                requested = np.sqrt(
                    max(float(target_variance[index]), 0.0)
                    / max(float(dynamics.variance[index]), 1e-30)
                )
                contraction_floor_binding[index] = requested < np.sqrt(
                    float(momentum[index])
                )

        required_innovation = np.maximum(target_variance - deterministic, 0.0)
        coefficient = step**2 * dynamics.noise_scale
        batch, batch_diagnostics = self._choose_batch(
            coefficient=coefficient,
            desired_innovation=required_innovation,
            previous=float(dynamics.effective_batch),
            weights=weights,
        )
        if self.max_log_batch_change is not None:
            previous_batch = float(dynamics.effective_batch)
            batch = float(
                np.clip(
                    batch,
                    previous_batch * np.exp(-self.max_log_batch_change),
                    previous_batch * np.exp(self.max_log_batch_change),
                )
            )
            batch = float(np.clip(batch, *self.batch_bounds))

        process_innovation = coefficient / batch
        next_variance = deterministic + process_innovation
        next_cross = c1_center * dynamics.variance + c2 * dynamics.lag_covariance
        effective_contraction = np.divide(
            next_cross,
            np.maximum(dynamics.variance, 1e-30),
            out=np.zeros_like(next_cross),
            where=dynamics.variance > 1e-30,
        )
        effective_innovation = np.maximum(
            next_variance - effective_contraction**2 * dynamics.variance, 0.0
        )
        predicted = GaussianTransition(
            contraction=effective_contraction,
            innovation=effective_innovation,
        )
        controls = {
            self.step_control_name: step.copy(),
            self.momentum_control_name: momentum.copy(),
            self.batch_control_name: batch,
        }
        diagnostics = {
            "companion_c1": c1_center.copy(),
            "companion_c2": c2.copy(),
            "companion_spectral_radius": radii.copy(),
            "companion_lyapunov_condition": conditions.copy(),
            "companion_regime": tuple(regimes),
            "candidate_found_fraction": float(np.mean(candidate_found)),
            "momentum_floor_binding_fraction": float(np.mean(contraction_floor_binding)),
            "robust_stability_satisfied": bool(
                np.all(radii <= self.max_spectral_radius)
                and np.all(conditions <= self.max_lyapunov_condition)
            ),
            "curvature_funnel_relative_width": (
                (upper_h - lower_h) / np.maximum(center_h, self.curvature_floor)
            ),
            **batch_diagnostics,
            **dominant_diagnostics,
        }
        plan = _plan(
            controls=controls,
            predicted=predicted,
            target=target,
            observation=observation,
            relative_tolerance=self.relative_tolerance,
            absolute_tolerance=self.absolute_tolerance,
            diagnostics=diagnostics,
        )
        if not bool(np.all(candidate_found)) or not diagnostics["robust_stability_satisfied"]:
            return ActuationPlan(
                controls=plan.controls,
                predicted=plan.predicted,
                feasible=False,
                target_variance=plan.target_variance,
                predicted_variance=plan.predicted_variance,
                error=plan.error,
                diagnostics={**dict(plan.diagnostics), "companion_guard_rejected": True},
            )
        return plan
