"""Dynamic sharpness plants and robustness funnels.

Edge-of-stability curvature is treated here as a slow controlled state rather
than as a static response curve.  The default plant is deliberately small:

    h[k+1] = h[k] + gamma_p * g[k]
                     - gamma_r * max(eta[k] * h[k] - theta[k], 0) + noise,
    theta[k] = 2 * (1 + mu[k]) - delta.

The two unknown rates enter linearly and are therefore identified by ordinary
forgetting-factor recursive least squares.  Planning uses interval funnels,
with stability checked at the upper edge and promised contraction evaluated at
the lower edge.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Mapping, Protocol, Sequence

import numpy as np
import numpy.typing as npt

from .types import FloatArray, as_float_array, broadcast_array


@dataclass(frozen=True, slots=True)
class CurvatureFunnel:
    """Blockwise interval prediction for curvature/sharpness."""

    lower: FloatArray
    center: FloatArray
    upper: FloatArray
    confidence: FloatArray | float = 1.0
    model_name: str = "unknown"
    adequate: FloatArray | bool = True

    def __post_init__(self) -> None:
        center = as_float_array(self.center, name="center")
        lower = broadcast_array(self.lower, center.size, name="lower")
        upper = broadcast_array(self.upper, center.size, name="upper")
        confidence = broadcast_array(self.confidence, center.size, name="confidence")
        adequate = np.asarray(self.adequate, dtype=bool)
        if adequate.ndim == 0:
            adequate = np.full(center.size, bool(adequate), dtype=bool)
        if adequate.ndim != 1 or adequate.size != center.size:
            raise ValueError("adequate must be scalar or one value per block.")
        if np.any(lower < 0.0) or np.any(center < lower) or np.any(upper < center):
            raise ValueError("require 0 <= lower <= center <= upper.")
        if np.any((confidence < 0.0) | (confidence > 1.0)):
            raise ValueError("confidence must lie in [0, 1].")
        object.__setattr__(self, "lower", lower)
        object.__setattr__(self, "center", center)
        object.__setattr__(self, "upper", upper)
        object.__setattr__(self, "confidence", confidence)
        object.__setattr__(self, "adequate", adequate)

    @property
    def size(self) -> int:
        return int(self.center.size)

    @property
    def relative_width(self) -> FloatArray:
        return (self.upper - self.lower) / np.maximum(self.center, 1e-12)

    def local_dynamics_kwargs(self) -> dict[str, FloatArray]:
        """Return fields ready to splice into :class:`LocalDynamics`."""

        return {
            "curvature": self.center.copy(),
            "curvature_lower": self.lower.copy(),
            "curvature_upper": self.upper.copy(),
            "curvature_adequacy": np.asarray(self.confidence, dtype=np.float64).copy(),
        }

    def diagnostics(self) -> dict[str, object]:
        return {
            "curvature_model": self.model_name,
            "curvature_lower": self.lower.copy(),
            "curvature_center": self.center.copy(),
            "curvature_upper": self.upper.copy(),
            "curvature_relative_width": self.relative_width.copy(),
            "curvature_confidence": np.asarray(self.confidence).copy(),
            "curvature_adequate": np.asarray(self.adequate).copy(),
        }


class SharpnessModel(Protocol):
    """Protocol consumed by sharpness-aware planners."""

    def predict_step(
        self,
        funnel: CurvatureFunnel,
        *,
        step_size: npt.ArrayLike,
        momentum: npt.ArrayLike,
        progress_signal: npt.ArrayLike,
    ) -> CurvatureFunnel:
        ...


@dataclass(slots=True)
class SharpnessPlant:
    """Identified progressive-sharpening/restoration plant.

    Parameters are blockwise even when initialized from scalars.  Call
    :meth:`update` with consecutive curvature observations to identify
    ``gamma_p`` and ``gamma_r``.  The RLS feature vector is
    ``[g, -(eta*h - theta)_+]``.
    """

    gamma_p: float | Sequence[float] | npt.ArrayLike = 1e-3
    gamma_r: float | Sequence[float] | npt.ArrayLike = 0.2
    safety_offset: float = 0.1
    forgetting: float = 0.995
    initial_covariance: float = 1e3
    residual_quantile: float = 0.95
    residual_window: int = 128
    uncertainty_scale: float = 2.0
    curvature_floor: float = 1e-10
    parameter_ceiling: float = 1e6
    _parameters: FloatArray | None = field(default=None, init=False, repr=False)
    _covariance: FloatArray | None = field(default=None, init=False, repr=False)
    _residuals: list[deque[float]] | None = field(default=None, init=False, repr=False)
    _updates: FloatArray | None = field(default=None, init=False, repr=False)

    def __post_init__(self) -> None:
        if not 0.0 < self.forgetting <= 1.0:
            raise ValueError("forgetting must lie in (0, 1].")
        if self.safety_offset < 0.0:
            raise ValueError("safety_offset must be non-negative.")
        if self.initial_covariance <= 0.0:
            raise ValueError("initial_covariance must be positive.")
        if not 0.5 < self.residual_quantile < 1.0:
            raise ValueError("residual_quantile must lie in (0.5, 1).")
        if self.residual_window < 8:
            raise ValueError("residual_window must be at least 8.")
        if self.uncertainty_scale < 0.0:
            raise ValueError("uncertainty_scale must be non-negative.")

    def _ensure(self, size: int) -> None:
        if self._parameters is not None:
            if self._parameters.shape[0] != size:
                raise ValueError("sharpness plant block count changed.")
            return
        gp = broadcast_array(self.gamma_p, size, name="gamma_p")
        gr = broadcast_array(self.gamma_r, size, name="gamma_r")
        if np.any(gp < 0.0) or np.any(gr < 0.0):
            raise ValueError("gamma_p and gamma_r must be non-negative.")
        self._parameters = np.column_stack([gp, gr]).astype(np.float64)
        self._covariance = np.repeat(
            (self.initial_covariance * np.eye(2, dtype=np.float64))[None, :, :],
            size,
            axis=0,
        )
        self._residuals = [deque(maxlen=self.residual_window) for _ in range(size)]
        self._updates = np.zeros(size, dtype=np.float64)

    @property
    def parameters(self) -> FloatArray:
        if self._parameters is None:
            raise RuntimeError("sharpness plant has not been initialized.")
        return self._parameters.copy()

    @property
    def parameter_standard_error(self) -> FloatArray:
        if self._covariance is None:
            raise RuntimeError("sharpness plant has not been initialized.")
        return np.sqrt(
            np.maximum(np.diagonal(self._covariance, axis1=1, axis2=2), 0.0)
        )

    def update(
        self,
        *,
        previous_curvature: npt.ArrayLike,
        current_curvature: npt.ArrayLike,
        step_size: npt.ArrayLike,
        momentum: npt.ArrayLike = 0.0,
        progress_signal: npt.ArrayLike = 1.0,
    ) -> CurvatureFunnel:
        """Update the plant by forgetting-factor RLS and return a current funnel."""

        previous = as_float_array(previous_curvature, name="previous_curvature")
        size = previous.size
        self._ensure(size)
        current = broadcast_array(current_curvature, size, name="current_curvature")
        step = broadcast_array(step_size, size, name="step_size")
        mu = broadcast_array(momentum, size, name="momentum")
        progress = broadcast_array(progress_signal, size, name="progress_signal")
        if np.any(step < 0.0) or np.any((mu < 0.0) | (mu >= 1.0)):
            raise ValueError("require step_size>=0 and momentum in [0,1).")
        if np.any(progress < 0.0):
            raise ValueError("progress_signal must be non-negative.")
        assert self._parameters is not None
        assert self._covariance is not None
        assert self._residuals is not None
        assert self._updates is not None

        theta = 2.0 * (1.0 + mu) - self.safety_offset
        edge_excess = np.maximum(step * previous - theta, 0.0)
        response = current - previous
        for index in range(size):
            phi = np.asarray([progress[index], -edge_excess[index]], dtype=np.float64)
            covariance = self._covariance[index]
            denominator = self.forgetting + float(phi @ covariance @ phi)
            gain = covariance @ phi / max(denominator, 1e-30)
            prediction = float(phi @ self._parameters[index])
            residual = float(response[index] - prediction)
            updated = self._parameters[index] + gain * residual
            self._parameters[index] = np.clip(updated, 0.0, self.parameter_ceiling)
            self._covariance[index] = (
                covariance - np.outer(gain, phi) @ covariance
            ) / self.forgetting
            self._covariance[index] = 0.5 * (
                self._covariance[index] + self._covariance[index].T
            )
            self._residuals[index].append(residual)
            self._updates[index] += 1.0
        center = np.maximum(current, self.curvature_floor)
        radius = self._observation_radius(size)
        confidence = self._confidence(size)
        return CurvatureFunnel(
            lower=np.maximum(center - radius, self.curvature_floor),
            center=center,
            upper=center + radius,
            confidence=confidence,
            model_name="sharpness_plant",
            adequate=confidence > 0.1,
        )

    def _observation_radius(self, size: int) -> FloatArray:
        assert self._residuals is not None
        values = np.empty(size, dtype=np.float64)
        for index, residuals in enumerate(self._residuals):
            if len(residuals) < 4:
                values[index] = 0.0
            else:
                values[index] = float(
                    np.quantile(np.abs(np.asarray(residuals)), self.residual_quantile)
                )
        return values

    def _confidence(self, size: int) -> FloatArray:
        assert self._covariance is not None
        assert self._updates is not None
        trace = np.trace(self._covariance, axis1=1, axis2=2)
        sample = np.clip(self._updates / 24.0, 0.0, 1.0)
        parameter = 1.0 / (1.0 + np.sqrt(np.maximum(trace, 0.0)))
        return np.clip(sample * parameter, 0.0, 1.0)

    def _map_value(
        self,
        h: float,
        *,
        step_size: float,
        momentum: float,
        progress_signal: float,
        parameters: npt.ArrayLike,
    ) -> float:
        gp, gr = map(float, np.asarray(parameters, dtype=np.float64))
        theta = 2.0 * (1.0 + momentum) - self.safety_offset
        return max(
            h + gp * progress_signal - gr * max(step_size * h - theta, 0.0),
            self.curvature_floor,
        )

    def predict_step(
        self,
        funnel: CurvatureFunnel,
        *,
        step_size: npt.ArrayLike,
        momentum: npt.ArrayLike,
        progress_signal: npt.ArrayLike,
    ) -> CurvatureFunnel:
        size = funnel.size
        self._ensure(size)
        step = broadcast_array(step_size, size, name="step_size")
        mu = broadcast_array(momentum, size, name="momentum")
        progress = broadcast_array(progress_signal, size, name="progress_signal")
        assert self._parameters is not None
        assert self._covariance is not None
        residual_radius = self._observation_radius(size)
        centers = np.empty(size, dtype=np.float64)
        lowers = np.empty(size, dtype=np.float64)
        uppers = np.empty(size, dtype=np.float64)
        confidence = self._confidence(size) * funnel.confidence

        for index in range(size):
            parameters = self._parameters[index]
            center = self._map_value(
                float(funnel.center[index]),
                step_size=float(step[index]),
                momentum=float(mu[index]),
                progress_signal=float(progress[index]),
                parameters=parameters,
            )
            candidates = [float(funnel.lower[index]), float(funnel.upper[index])]
            if step[index] > 0.0:
                kink = (
                    2.0 * (1.0 + float(mu[index])) - self.safety_offset
                ) / float(step[index])
                if funnel.lower[index] <= kink <= funnel.upper[index]:
                    candidates.append(float(kink))
            # Conservative set-membership box over the identified rates.  The
            # model is affine in (gamma_p, gamma_r) for fixed h and piecewise
            # affine in h, so endpoint/kink and parameter-corner enumeration is
            # sufficient for this scalar plant.
            parameter_std = np.sqrt(
                np.maximum(np.diag(self._covariance[index]), 0.0)
            )
            parameter_low = np.clip(
                parameters - self.uncertainty_scale * parameter_std,
                0.0,
                self.parameter_ceiling,
            )
            parameter_high = np.clip(
                parameters + self.uncertainty_scale * parameter_std,
                0.0,
                self.parameter_ceiling,
            )
            mapped = []
            for candidate in candidates:
                for gamma_p in (parameter_low[0], parameter_high[0]):
                    for gamma_r in (parameter_low[1], parameter_high[1]):
                        mapped.append(
                            self._map_value(
                                candidate,
                                step_size=float(step[index]),
                                momentum=float(mu[index]),
                                progress_signal=float(progress[index]),
                                parameters=np.asarray([gamma_p, gamma_r]),
                            )
                        )
            radius = float(residual_radius[index])
            centers[index] = center
            lowers[index] = max(min(mapped) - radius, self.curvature_floor)
            uppers[index] = max(max(mapped) + radius, centers[index])
        return CurvatureFunnel(
            lower=lowers,
            center=centers,
            upper=uppers,
            confidence=np.clip(confidence, 0.0, 1.0),
            model_name="sharpness_plant",
            adequate=np.asarray(funnel.adequate, dtype=bool) & (confidence > 0.05),
        )

    def rollout(
        self,
        initial: CurvatureFunnel,
        *,
        step_sizes: npt.ArrayLike,
        momenta: npt.ArrayLike,
        progress_signals: npt.ArrayLike,
    ) -> list[CurvatureFunnel]:
        """Roll a funnel forward through command sequences.

        Arrays may be shape ``(horizon, blocks)`` or one-dimensional for a
        single block.  The returned list includes ``initial``.
        """

        steps = np.asarray(step_sizes, dtype=np.float64)
        if steps.ndim == 1:
            steps = steps[:, None]
        horizon, size = steps.shape
        if size != initial.size:
            raise ValueError("step_sizes block count does not match initial funnel.")
        mu = np.asarray(momenta, dtype=np.float64)
        progress = np.asarray(progress_signals, dtype=np.float64)
        if mu.ndim == 1:
            mu = np.broadcast_to(mu[:, None], (horizon, size))
        if progress.ndim == 1:
            progress = np.broadcast_to(progress[:, None], (horizon, size))
        if mu.shape != steps.shape or progress.shape != steps.shape:
            raise ValueError("momenta and progress_signals must match step_sizes.")
        result = [initial]
        current = initial
        for index in range(horizon):
            current = self.predict_step(
                current,
                step_size=steps[index],
                momentum=mu[index],
                progress_signal=progress[index],
            )
            result.append(current)
        return result

    def reset(self) -> None:
        self._parameters = None
        self._covariance = None
        self._residuals = None
        self._updates = None

    def state_dict(self) -> dict[str, object]:
        return {
            "type": "sharpness_plant",
            "parameters": None if self._parameters is None else self._parameters.tolist(),
            "covariance": None if self._covariance is None else self._covariance.tolist(),
            "residuals": (
                None
                if self._residuals is None
                else [list(values) for values in self._residuals]
            ),
            "updates": None if self._updates is None else self._updates.tolist(),
        }

    def load_state_dict(self, state: Mapping[str, object]) -> None:
        parameters = state.get("parameters")
        if parameters is None:
            self._parameters = None
            self._covariance = None
            self._residuals = None
            self._updates = None
            return
        self._parameters = np.asarray(parameters, dtype=np.float64)
        self._covariance = np.asarray(state["covariance"], dtype=np.float64)
        residuals = state.get("residuals")
        assert residuals is not None
        self._residuals = [
            deque((float(value) for value in values), maxlen=self.residual_window)
            for values in residuals  # type: ignore[union-attr]
        ]
        self._updates = np.asarray(state["updates"], dtype=np.float64)


@dataclass(frozen=True, slots=True)
class StaticLinearCurvatureModel:
    """Legacy local response model retained as the shortest adequacy candidate."""

    reference_step: float | Sequence[float] | npt.ArrayLike
    slope: float | Sequence[float] | npt.ArrayLike = 0.0
    residual_radius: float | Sequence[float] | npt.ArrayLike = 0.0

    def predict_step(
        self,
        funnel: CurvatureFunnel,
        *,
        step_size: npt.ArrayLike,
        momentum: npt.ArrayLike,
        progress_signal: npt.ArrayLike,
    ) -> CurvatureFunnel:
        del momentum, progress_signal
        step = broadcast_array(step_size, funnel.size, name="step_size")
        reference = broadcast_array(self.reference_step, funnel.size, name="reference_step")
        slope = broadcast_array(self.slope, funnel.size, name="slope")
        radius = broadcast_array(self.residual_radius, funnel.size, name="residual_radius")
        center = np.maximum(funnel.center + slope * (step - reference), 0.0)
        return CurvatureFunnel(
            lower=np.maximum(center - radius, 0.0),
            center=center,
            upper=center + radius,
            confidence=funnel.confidence,
            model_name="static_linear",
            adequate=funnel.adequate,
        )


@dataclass(slots=True)
class GainScheduledSharpnessModel:
    """Small LPV fallback made of margin-binned local linear models.

    Each bin estimates ``delta_h = beta0 + beta1*g + beta2*edge_excess``.
    Predictions are smoothly blended by Gaussian weights in the current edge
    margin.  This is intentionally a middle model between a static response and
    the mechanistic :class:`SharpnessPlant`.
    """

    margin_centers: tuple[float, ...] = (-0.25, 0.5, 1.5)
    bandwidth: float = 0.5
    safety_offset: float = 0.1
    forgetting: float = 0.995
    initial_covariance: float = 1e3
    residual_radius: float = 0.0
    _parameters: FloatArray | None = field(default=None, init=False, repr=False)
    _covariance: FloatArray | None = field(default=None, init=False, repr=False)

    def __post_init__(self) -> None:
        if len(self.margin_centers) < 2:
            raise ValueError("margin_centers needs at least two bins.")
        if self.bandwidth <= 0.0:
            raise ValueError("bandwidth must be positive.")
        if self.safety_offset < 0.0:
            raise ValueError("safety_offset must be non-negative.")
        if not 0.0 < self.forgetting <= 1.0:
            raise ValueError("forgetting must lie in (0, 1].")

    def _ensure(self, size: int) -> None:
        bins = len(self.margin_centers)
        if self._parameters is None:
            self._parameters = np.zeros((size, bins, 3), dtype=np.float64)
            self._covariance = np.repeat(
                (self.initial_covariance * np.eye(3))[None, None, :, :],
                size * bins,
                axis=0,
            ).reshape(size, bins, 3, 3)
        elif self._parameters.shape[0] != size:
            raise ValueError("LPV model block count changed.")

    def _weights(self, margin: FloatArray) -> FloatArray:
        centers = np.asarray(self.margin_centers, dtype=np.float64)
        weights = np.exp(-0.5 * ((margin[:, None] - centers[None, :]) / self.bandwidth) ** 2)
        return weights / np.maximum(np.sum(weights, axis=1, keepdims=True), 1e-30)

    def update(
        self,
        *,
        previous_curvature: npt.ArrayLike,
        current_curvature: npt.ArrayLike,
        step_size: npt.ArrayLike,
        momentum: npt.ArrayLike = 0.0,
        progress_signal: npt.ArrayLike = 1.0,
        safety_offset: float | None = None,
    ) -> None:
        previous = as_float_array(previous_curvature, name="previous_curvature")
        size = previous.size
        self._ensure(size)
        current = broadcast_array(current_curvature, size, name="current_curvature")
        step = broadcast_array(step_size, size, name="step_size")
        mu = broadcast_array(momentum, size, name="momentum")
        progress = broadcast_array(progress_signal, size, name="progress_signal")
        offset = self.safety_offset if safety_offset is None else float(safety_offset)
        if offset < 0.0:
            raise ValueError("safety_offset must be non-negative.")
        margin = 2.0 * (1.0 + mu) - offset - step * previous
        edge = np.maximum(-margin, 0.0)
        weights = self._weights(margin)
        response = current - previous
        assert self._parameters is not None and self._covariance is not None
        for block in range(size):
            phi = np.asarray([1.0, progress[block], edge[block]], dtype=np.float64)
            for bin_index, blend in enumerate(weights[block]):
                if blend < 1e-6:
                    continue
                covariance = self._covariance[block, bin_index]
                effective_phi = np.sqrt(blend) * phi
                effective_y = np.sqrt(blend) * response[block]
                denominator = self.forgetting + effective_phi @ covariance @ effective_phi
                gain = covariance @ effective_phi / max(float(denominator), 1e-30)
                residual = effective_y - effective_phi @ self._parameters[block, bin_index]
                self._parameters[block, bin_index] += gain * residual
                self._covariance[block, bin_index] = (
                    covariance - np.outer(gain, effective_phi) @ covariance
                ) / self.forgetting

    def predict_step(
        self,
        funnel: CurvatureFunnel,
        *,
        step_size: npt.ArrayLike,
        momentum: npt.ArrayLike,
        progress_signal: npt.ArrayLike,
    ) -> CurvatureFunnel:
        size = funnel.size
        self._ensure(size)
        step = broadcast_array(step_size, size, name="step_size")
        mu = broadcast_array(momentum, size, name="momentum")
        progress = broadcast_array(progress_signal, size, name="progress_signal")
        margin = 2.0 * (1.0 + mu) - self.safety_offset - step * funnel.center
        edge = np.maximum(-margin, 0.0)
        weights = self._weights(margin)
        assert self._parameters is not None
        phi = np.column_stack([np.ones(size), progress, edge])
        local = np.einsum("sbi,si->sb", self._parameters, phi)
        delta = np.sum(weights * local, axis=1)
        center = np.maximum(funnel.center + delta, 0.0)
        radius = broadcast_array(self.residual_radius, size, name="residual_radius")
        return CurvatureFunnel(
            lower=np.maximum(center - radius, 0.0),
            center=center,
            upper=center + radius,
            confidence=funnel.confidence,
            model_name="gain_scheduled",
            adequate=funnel.adequate,
        )

    def reset(self) -> None:
        self._parameters = None
        self._covariance = None

    def state_dict(self) -> dict[str, object]:
        return {
            "type": "gain_scheduled",
            "parameters": None if self._parameters is None else self._parameters.tolist(),
            "covariance": None if self._covariance is None else self._covariance.tolist(),
        }

    def load_state_dict(self, state: Mapping[str, object]) -> None:
        parameters = state.get("parameters")
        covariance = state.get("covariance")
        if parameters is None:
            self.reset()
            return
        if covariance is None:
            raise ValueError("gain-scheduled checkpoint is missing covariance.")
        self._parameters = np.asarray(parameters, dtype=np.float64)
        self._covariance = np.asarray(covariance, dtype=np.float64)


@dataclass(frozen=True, slots=True)
class CurvatureAdequacyReport:
    selected_model: tuple[str, ...]
    normalized_error: Mapping[str, FloatArray]
    interval_coverage: Mapping[str, FloatArray]
    confidence: FloatArray
    fallback_fraction: float


@dataclass(slots=True)
class CurvatureAdequacyObserver:
    """Select the shortest calibrated curvature model per block.

    Supply one-step funnels from candidate models and the realized curvature.
    The order in ``preference`` encodes description length.  If no model meets
    both the normalized-error and interval-coverage thresholds, the block is
    assigned ``'trust_region'``.
    """

    preference: tuple[str, ...] = ("static_linear", "sharpness_plant", "gain_scheduled")
    error_threshold: float = 0.35
    coverage_threshold: float = 0.80
    smoothing: float = 0.1
    scale_floor: float = 1e-8
    _error: dict[str, FloatArray] = field(default_factory=dict, init=False, repr=False)
    _coverage: dict[str, FloatArray] = field(default_factory=dict, init=False, repr=False)

    def __post_init__(self) -> None:
        if not 0.0 < self.smoothing <= 1.0:
            raise ValueError("smoothing must lie in (0, 1].")
        if self.error_threshold <= 0.0:
            raise ValueError("error_threshold must be positive.")
        if not 0.0 <= self.coverage_threshold <= 1.0:
            raise ValueError("coverage_threshold must lie in [0, 1].")

    def update(
        self,
        *,
        observed_curvature: npt.ArrayLike,
        predictions: Mapping[str, CurvatureFunnel],
    ) -> CurvatureAdequacyReport:
        observed = as_float_array(observed_curvature, name="observed_curvature")
        size = observed.size
        for name, funnel in predictions.items():
            if funnel.size != size:
                raise ValueError(f"prediction {name!r} has the wrong block count.")
            scale = np.maximum.reduce(
                [np.abs(observed), np.abs(funnel.center), np.full(size, self.scale_floor)]
            )
            instantaneous_error = np.abs(observed - funnel.center) / scale
            instantaneous_coverage = (
                (observed >= funnel.lower) & (observed <= funnel.upper)
            ).astype(np.float64)
            if name not in self._error:
                self._error[name] = instantaneous_error
                self._coverage[name] = instantaneous_coverage
            else:
                self._error[name] += self.smoothing * (
                    instantaneous_error - self._error[name]
                )
                self._coverage[name] += self.smoothing * (
                    instantaneous_coverage - self._coverage[name]
                )
        selected: list[str] = []
        confidence = np.zeros(size, dtype=np.float64)
        for block in range(size):
            choice = "trust_region"
            for name in self.preference:
                if name not in self._error:
                    continue
                if (
                    self._error[name][block] <= self.error_threshold
                    and self._coverage[name][block] >= self.coverage_threshold
                ):
                    choice = name
                    confidence[block] = min(
                        1.0 - self._error[name][block] / self.error_threshold,
                        self._coverage[name][block],
                    )
                    break
            selected.append(choice)
        return CurvatureAdequacyReport(
            selected_model=tuple(selected),
            normalized_error={key: value.copy() for key, value in self._error.items()},
            interval_coverage={key: value.copy() for key, value in self._coverage.items()},
            confidence=np.clip(confidence, 0.0, 1.0),
            fallback_fraction=float(np.mean(np.asarray(selected) == "trust_region")),
        )

    def reset(self) -> None:
        self._error.clear()
        self._coverage.clear()

    def state_dict(self) -> dict[str, object]:
        return {
            "error": {key: value.tolist() for key, value in self._error.items()},
            "coverage": {key: value.tolist() for key, value in self._coverage.items()},
        }

    def load_state_dict(self, state: Mapping[str, object]) -> None:
        error = state.get("error", {})
        coverage = state.get("coverage", {})
        if not isinstance(error, Mapping) or not isinstance(coverage, Mapping):
            raise ValueError("invalid curvature adequacy checkpoint.")
        self._error = {
            str(key): np.asarray(value, dtype=np.float64) for key, value in error.items()
        }
        self._coverage = {
            str(key): np.asarray(value, dtype=np.float64)
            for key, value in coverage.items()
        }


@dataclass(frozen=True, slots=True)
class SharpnessJumpReport:
    jumped: FloatArray
    relative_change: FloatArray
    latched: FloatArray


@dataclass(slots=True)
class SharpnessJumpDetector:
    """Latch catapult-like discontinuities instead of fitting through them."""

    relative_threshold: float = 0.5
    absolute_threshold: float = np.inf
    _previous: FloatArray | None = field(default=None, init=False, repr=False)
    _latched: FloatArray | None = field(default=None, init=False, repr=False)

    def update(self, curvature: npt.ArrayLike) -> SharpnessJumpReport:
        current = as_float_array(curvature, name="curvature")
        if self._previous is None:
            self._previous = current.copy()
            self._latched = np.zeros(current.size, dtype=bool)
            return SharpnessJumpReport(
                jumped=np.zeros(current.size),
                relative_change=np.zeros(current.size),
                latched=np.zeros(current.size),
            )
        previous = broadcast_array(self._previous, current.size, name="previous")
        assert self._latched is not None
        relative = np.abs(current - previous) / np.maximum(np.abs(previous), 1e-12)
        jumped = (relative >= self.relative_threshold) | (
            np.abs(current - previous) >= self.absolute_threshold
        )
        self._latched = np.asarray(self._latched, dtype=bool) | jumped
        self._previous = current.copy()
        return SharpnessJumpReport(
            jumped=jumped.astype(np.float64),
            relative_change=relative,
            latched=self._latched.astype(np.float64),
        )

    def reset(self, blocks: npt.ArrayLike | None = None) -> None:
        if blocks is None:
            self._latched = None if self._previous is None else np.zeros_like(self._previous, dtype=bool)
            return
        if self._latched is None:
            return
        mask = np.asarray(blocks, dtype=bool)
        if mask.ndim == 0:
            mask = np.full(self._latched.size, bool(mask), dtype=bool)
        if mask.size != self._latched.size:
            raise ValueError("reset mask has the wrong size.")
        self._latched[mask] = False

    def state_dict(self) -> dict[str, object]:
        return {
            "previous": None if self._previous is None else self._previous.tolist(),
            "latched": None if self._latched is None else self._latched.tolist(),
        }

    def load_state_dict(self, state: Mapping[str, object]) -> None:
        previous = state.get("previous")
        latched = state.get("latched")
        self._previous = None if previous is None else np.asarray(previous, dtype=np.float64)
        self._latched = None if latched is None else np.asarray(latched, dtype=bool)
        if (self._previous is None) != (self._latched is None):
            raise ValueError("jump-detector checkpoint is inconsistent.")


@dataclass(frozen=True, slots=True)
class DominantSharpnessCoordinator:
    """Shared global edge guard over blockwise sharpness channels."""

    safety_offset: float = 0.1
    maximum_utilization: float = 1.0
    mode: str = "max"
    temperature: float = 0.05

    def __post_init__(self) -> None:
        if self.safety_offset < 0.0:
            raise ValueError("safety_offset must be non-negative.")
        if not 0.0 < self.maximum_utilization <= 1.0:
            raise ValueError("maximum_utilization must lie in (0, 1].")
        if self.mode not in {"max", "softmax"}:
            raise ValueError("mode must be 'max' or 'softmax'.")
        if self.temperature <= 0.0:
            raise ValueError("temperature must be positive.")

    def utilization(
        self,
        step_size: npt.ArrayLike,
        momentum: npt.ArrayLike,
        curvature_upper: npt.ArrayLike,
    ) -> FloatArray:
        step = as_float_array(step_size, name="step_size")
        mu = broadcast_array(momentum, step.size, name="momentum")
        upper = broadcast_array(curvature_upper, step.size, name="curvature_upper")
        threshold = np.maximum(2.0 * (1.0 + mu) - self.safety_offset, 1e-12)
        return step * upper / threshold

    def dominant_value(self, utilization: npt.ArrayLike) -> float:
        values = as_float_array(utilization, name="utilization")
        if self.mode == "max":
            return float(np.max(values))
        shifted = values - np.max(values)
        weights = np.exp(shifted / self.temperature)
        weights /= np.sum(weights)
        return float(np.sum(weights * values))

    def scale_steps(
        self,
        step_size: npt.ArrayLike,
        momentum: npt.ArrayLike,
        curvature_upper: npt.ArrayLike,
    ) -> tuple[FloatArray, dict[str, float]]:
        step = as_float_array(step_size, name="step_size")
        utilization = self.utilization(step, momentum, curvature_upper)
        dominant = self.dominant_value(utilization)
        scale = min(1.0, self.maximum_utilization / max(dominant, 1e-30))
        return step * scale, {
            "dominant_edge_utilization_before": dominant,
            "dominant_step_scale": scale,
            "dominant_edge_utilization_after": dominant * scale,
        }


@dataclass(slots=True)
class CurvatureModelLadder:
    """Per-block adequacy-gated ladder of nested sharpness models."""

    models: Mapping[str, SharpnessModel]
    selected_model: tuple[str, ...] | None = None

    def __post_init__(self) -> None:
        if not self.models:
            raise ValueError("models must contain at least one sharpness model.")

    def select(self, report: CurvatureAdequacyReport) -> None:
        self.selected_model = report.selected_model

    def predict_step(
        self,
        funnel: CurvatureFunnel,
        *,
        step_size: npt.ArrayLike,
        momentum: npt.ArrayLike,
        progress_signal: npt.ArrayLike,
    ) -> CurvatureFunnel:
        if self.selected_model is None:
            # Prefer the shortest declared model until adequacy data arrive.
            first = next(iter(self.models))
            selected = tuple(first for _ in range(funnel.size))
        else:
            if len(self.selected_model) != funnel.size:
                raise ValueError("selected model count does not match funnel blocks.")
            selected = self.selected_model
        predictions = {
            name: model.predict_step(
                funnel,
                step_size=step_size,
                momentum=momentum,
                progress_signal=progress_signal,
            )
            for name, model in self.models.items()
        }
        lower = np.empty(funnel.size)
        center = np.empty(funnel.size)
        upper = np.empty(funnel.size)
        confidence = np.empty(funnel.size)
        adequate = np.empty(funnel.size, dtype=bool)
        for index, name in enumerate(selected):
            if name == "trust_region" or name not in predictions:
                lower[index] = funnel.lower[index]
                center[index] = funnel.center[index]
                upper[index] = funnel.upper[index]
                confidence[index] = 0.0
                adequate[index] = False
                continue
            prediction = predictions[name]
            lower[index] = prediction.lower[index]
            center[index] = prediction.center[index]
            upper[index] = prediction.upper[index]
            confidence[index] = prediction.confidence[index]
            adequate[index] = bool(prediction.adequate[index])
        return CurvatureFunnel(
            lower=lower,
            center=center,
            upper=upper,
            confidence=confidence,
            model_name="curvature_model_ladder",
            adequate=adequate,
        )

    def reset(self) -> None:
        self.selected_model = None
        for model in self.models.values():
            reset = getattr(model, "reset", None)
            if callable(reset):
                reset()

    def state_dict(self) -> dict[str, object]:
        model_states: dict[str, object] = {}
        for name, model in self.models.items():
            getter = getattr(model, "state_dict", None)
            if callable(getter):
                model_states[name] = getter()
        return {
            "selected_model": None if self.selected_model is None else list(self.selected_model),
            "models": model_states,
        }

    def load_state_dict(self, state: Mapping[str, object]) -> None:
        selected = state.get("selected_model")
        self.selected_model = None if selected is None else tuple(str(x) for x in selected)  # type: ignore[arg-type]
        model_states = state.get("models", {})
        if not isinstance(model_states, Mapping):
            raise ValueError("invalid curvature-model ladder checkpoint.")
        for name, model_state in model_states.items():
            model = self.models.get(str(name))
            loader = None if model is None else getattr(model, "load_state_dict", None)
            if callable(loader):
                loader(model_state)
