"""Core data structures for :mod:`bridgelearn`.

The public API remains block-scalar by default, while v0.3 also exposes the
minimal lag covariance and momentum state needed for companion-dynamics
identification, sharpness funnels, and robust edge-of-stability actuation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence

import numpy as np
import numpy.typing as npt

FloatArray = npt.NDArray[np.float64]


def as_float_array(value: float | Sequence[float] | npt.ArrayLike, *, name: str) -> FloatArray:
    """Return *value* as a finite one-dimensional ``float64`` array."""

    array = np.asarray(value, dtype=np.float64)
    if array.ndim == 0:
        array = array.reshape(1)
    if array.ndim != 1:
        raise ValueError(f"{name} must be scalar or one-dimensional; got shape {array.shape}.")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must contain only finite values.")
    return array.copy()


def broadcast_array(
    value: float | Sequence[float] | npt.ArrayLike,
    size: int,
    *,
    name: str,
) -> FloatArray:
    """Broadcast a scalar or validate a one-dimensional array of ``size``."""

    array = as_float_array(value, name=name)
    if array.size == 1 and size != 1:
        array = np.full(size, float(array[0]), dtype=np.float64)
    if array.size != size:
        raise ValueError(f"{name} has length {array.size}; expected {size}.")
    return array


@dataclass(frozen=True, slots=True)
class GaussianState:
    """A diagonal/block-scalar covariance summary.

    ``confidence`` is deliberately part of the state.  It can combine sampling
    uncertainty, centering adequacy, AR(1) model adequacy, and observer health.
    """

    variance: FloatArray
    confidence: FloatArray | float = 1.0
    labels: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        variance = as_float_array(self.variance, name="variance")
        if np.any(variance < 0.0):
            raise ValueError("variance must be non-negative.")
        confidence = broadcast_array(self.confidence, variance.size, name="confidence")
        if np.any((confidence < 0.0) | (confidence > 1.0)):
            raise ValueError("confidence must lie in [0, 1].")
        if self.labels and len(self.labels) != variance.size:
            raise ValueError("labels must have one entry per variance block.")
        object.__setattr__(self, "variance", variance)
        object.__setattr__(self, "confidence", confidence)

    @property
    def size(self) -> int:
        return int(self.variance.size)


@dataclass(frozen=True, slots=True)
class GaussianTransition:
    """A diagonal linear-Gaussian transition.

    The represented dynamics are ``z_next = contraction * z + noise`` with
    blockwise innovation variances ``innovation``.
    """

    contraction: FloatArray
    innovation: FloatArray

    def __post_init__(self) -> None:
        contraction = as_float_array(self.contraction, name="contraction")
        innovation = broadcast_array(self.innovation, contraction.size, name="innovation")
        if np.any(innovation < 0.0):
            raise ValueError("innovation variance must be non-negative.")
        object.__setattr__(self, "contraction", contraction)
        object.__setattr__(self, "innovation", innovation)

    @property
    def size(self) -> int:
        return int(self.contraction.size)

    def next_variance(self, current_variance: npt.ArrayLike) -> FloatArray:
        current = broadcast_array(current_variance, self.size, name="current_variance")
        return self.contraction**2 * current + self.innovation


@dataclass(frozen=True, slots=True)
class LocalDynamics:
    """Local blockwise dynamics exposed by an adapter.

    The baseline model is

    ``a(eta) = 1 - eta * h(eta)`` and
    ``r(eta, m) = eta**2 * noise_scale / m``.

    ``curvature_slope`` retains the legacy static response model; dynamic
    sharpness should be supplied through ``curvature_lower/upper`` by a
    :class:`SharpnessPlant`. ``trust_region_step`` is an independent geometry
    cap. ``structural_adequacy`` is the preferred v0.3 model gate;
    ``ar1_adequacy`` remains a backwards-compatible alias.
    """

    variance: FloatArray
    curvature: FloatArray
    noise_scale: FloatArray
    step_size: FloatArray
    effective_batch: float
    confidence: FloatArray | float = 1.0
    labels: tuple[str, ...] = ()
    curvature_slope: FloatArray | float = 0.0
    trust_region_step: FloatArray | float = 1e30
    ar1_adequacy: FloatArray | float = 1.0
    structural_adequacy: FloatArray | float | None = None
    momentum: FloatArray | float = 0.0
    previous_variance: FloatArray | float | None = None
    lag_covariance: FloatArray | float | None = None
    curvature_lower: FloatArray | float | None = None
    curvature_upper: FloatArray | float | None = None
    curvature_adequacy: FloatArray | float = 1.0
    coefficient_slew_limit: FloatArray | float = 1e30

    def __post_init__(self) -> None:
        variance = as_float_array(self.variance, name="variance")
        size = variance.size
        curvature = broadcast_array(self.curvature, size, name="curvature")
        noise_scale = broadcast_array(self.noise_scale, size, name="noise_scale")
        step_size = broadcast_array(self.step_size, size, name="step_size")
        confidence = broadcast_array(self.confidence, size, name="confidence")
        curvature_slope = broadcast_array(
            self.curvature_slope, size, name="curvature_slope"
        )
        trust_region_step = broadcast_array(
            self.trust_region_step, size, name="trust_region_step"
        )
        ar1_adequacy = broadcast_array(self.ar1_adequacy, size, name="ar1_adequacy")
        structural_adequacy = (
            ar1_adequacy.copy()
            if self.structural_adequacy is None
            else broadcast_array(
                self.structural_adequacy, size, name="structural_adequacy"
            )
        )
        momentum = broadcast_array(self.momentum, size, name="momentum")
        previous_variance = (
            variance.copy()
            if self.previous_variance is None
            else broadcast_array(self.previous_variance, size, name="previous_variance")
        )
        lag_covariance = (
            np.zeros(size, dtype=np.float64)
            if self.lag_covariance is None
            else broadcast_array(self.lag_covariance, size, name="lag_covariance")
        )
        curvature_lower = (
            curvature.copy()
            if self.curvature_lower is None
            else broadcast_array(self.curvature_lower, size, name="curvature_lower")
        )
        curvature_upper = (
            curvature.copy()
            if self.curvature_upper is None
            else broadcast_array(self.curvature_upper, size, name="curvature_upper")
        )
        curvature_adequacy = broadcast_array(
            self.curvature_adequacy, size, name="curvature_adequacy"
        )
        coefficient_slew_limit = broadcast_array(
            self.coefficient_slew_limit, size, name="coefficient_slew_limit"
        )
        if np.any(variance < 0.0):
            raise ValueError("variance must be non-negative.")
        if np.any(noise_scale < 0.0):
            raise ValueError("noise_scale must be non-negative.")
        if np.any(step_size < 0.0):
            raise ValueError("step_size must be non-negative.")
        if not np.isfinite(self.effective_batch) or self.effective_batch <= 0.0:
            raise ValueError("effective_batch must be positive and finite.")
        if np.any((confidence < 0.0) | (confidence > 1.0)):
            raise ValueError("confidence must lie in [0, 1].")
        if np.any((ar1_adequacy < 0.0) | (ar1_adequacy > 1.0)):
            raise ValueError("ar1_adequacy must lie in [0, 1].")
        if np.any((structural_adequacy < 0.0) | (structural_adequacy > 1.0)):
            raise ValueError("structural_adequacy must lie in [0, 1].")
        if np.any((momentum < 0.0) | (momentum >= 1.0)):
            raise ValueError("momentum must lie in [0, 1).")
        if np.any(previous_variance < 0.0):
            raise ValueError("previous_variance must be non-negative.")
        covariance_bound = np.sqrt(np.maximum(variance * previous_variance, 0.0))
        if np.any(np.abs(lag_covariance) > covariance_bound + 1e-10):
            raise ValueError("lag_covariance violates the covariance Cauchy bound.")
        if np.any(curvature_lower < 0.0) or np.any(curvature_upper < curvature_lower):
            raise ValueError("require 0 <= curvature_lower <= curvature_upper.")
        if np.any(curvature < curvature_lower) or np.any(curvature > curvature_upper):
            raise ValueError("curvature must lie inside its declared funnel.")
        if np.any((curvature_adequacy < 0.0) | (curvature_adequacy > 1.0)):
            raise ValueError("curvature_adequacy must lie in [0, 1].")
        if np.any(coefficient_slew_limit <= 0.0):
            raise ValueError("coefficient_slew_limit must be positive.")
        if np.any(trust_region_step <= 0.0):
            raise ValueError("trust_region_step must be positive.")
        if self.labels and len(self.labels) != size:
            raise ValueError("labels must have one entry per block.")
        object.__setattr__(self, "variance", variance)
        object.__setattr__(self, "curvature", curvature)
        object.__setattr__(self, "noise_scale", noise_scale)
        object.__setattr__(self, "step_size", step_size)
        object.__setattr__(self, "confidence", confidence)
        object.__setattr__(self, "curvature_slope", curvature_slope)
        object.__setattr__(self, "trust_region_step", trust_region_step)
        object.__setattr__(self, "ar1_adequacy", ar1_adequacy)
        object.__setattr__(self, "structural_adequacy", structural_adequacy)
        object.__setattr__(self, "momentum", momentum)
        object.__setattr__(self, "previous_variance", previous_variance)
        object.__setattr__(self, "lag_covariance", lag_covariance)
        object.__setattr__(self, "curvature_lower", curvature_lower)
        object.__setattr__(self, "curvature_upper", curvature_upper)
        object.__setattr__(self, "curvature_adequacy", curvature_adequacy)
        object.__setattr__(self, "coefficient_slew_limit", coefficient_slew_limit)

    @property
    def size(self) -> int:
        return int(self.variance.size)

    @property
    def effective_confidence(self) -> FloatArray:
        return np.clip(
            self.confidence * self.structural_adequacy * self.curvature_adequacy,
            0.0,
            1.0,
        )

    def curvature_at(self, step_size: npt.ArrayLike) -> FloatArray:
        step = broadcast_array(step_size, self.size, name="step_size")
        return np.maximum(
            self.curvature + self.curvature_slope * (step - self.step_size),
            0.0,
        )

    def curvature_bounds_at(self, step_size: npt.ArrayLike) -> tuple[FloatArray, FloatArray]:
        """Return a first-order transported curvature funnel at ``step_size``."""

        step = broadcast_array(step_size, self.size, name="step_size")
        shift = self.curvature_slope * (step - self.step_size)
        lower = np.maximum(self.curvature_lower + shift, 0.0)
        upper = np.maximum(self.curvature_upper + shift, lower)
        return lower, upper

    def contraction_at(self, step_size: npt.ArrayLike) -> FloatArray:
        step = broadcast_array(step_size, self.size, name="step_size")
        return 1.0 - step * self.curvature_at(step)

    def contraction_bounds_at(self, step_size: npt.ArrayLike) -> tuple[FloatArray, FloatArray]:
        """Return contraction at the lower and upper curvature funnel edges."""

        step = broadcast_array(step_size, self.size, name="step_size")
        lower_h, upper_h = self.curvature_bounds_at(step)
        return 1.0 - step * lower_h, 1.0 - step * upper_h

    def step_for_contraction(
        self,
        contraction: npt.ArrayLike,
        *,
        curvature_floor: float = 1e-12,
        curvature_override: npt.ArrayLike | None = None,
    ) -> FloatArray:
        """Invert ``1 - eta*h(eta)`` under a linear curvature-response model.

        When the response slope is effectively zero this reduces to the usual
        ``eta = (1-a)/h``.  Otherwise the non-negative root closest to the
        current command is selected.
        """

        target = broadcast_array(contraction, self.size, name="contraction")
        result = np.empty(self.size, dtype=np.float64)
        h_source = self.curvature if curvature_override is None else broadcast_array(curvature_override, self.size, name="curvature_override")
        for index in range(self.size):
            h0 = float(h_source[index])
            slope = float(self.curvature_slope[index])
            eta0 = float(self.step_size[index])
            rhs = 1.0 - float(target[index])
            if h0 <= curvature_floor:
                result[index] = eta0
                continue
            if abs(slope) <= 1e-14:
                result[index] = max(rhs / h0, 0.0)
                continue
            linear = h0 - slope * eta0
            discriminant = linear * linear + 4.0 * slope * rhs
            if discriminant < 0.0:
                result[index] = max(rhs / h0, 0.0)
                continue
            root = np.sqrt(discriminant)
            candidates = [
                (-linear + root) / (2.0 * slope),
                (-linear - root) / (2.0 * slope),
            ]
            feasible = [value for value in candidates if np.isfinite(value) and value >= 0.0]
            result[index] = (
                min(feasible, key=lambda value: abs(value - eta0))
                if feasible
                else max(rhs / h0, 0.0)
            )
        return result

    def companion_coefficients_at(
        self,
        step_size: npt.ArrayLike,
        momentum: npt.ArrayLike | None = None,
        *,
        curvature: npt.ArrayLike | None = None,
    ) -> tuple[FloatArray, FloatArray]:
        """Return heavy-ball companion coefficients ``c1, c2``."""

        step = broadcast_array(step_size, self.size, name="step_size")
        mu = self.momentum if momentum is None else broadcast_array(momentum, self.size, name="momentum")
        h = self.curvature_at(step) if curvature is None else broadcast_array(curvature, self.size, name="curvature")
        return 1.0 + mu - step * h, -mu

    def reference_transition(self) -> GaussianTransition:
        """Return the exact one-step marginal regression transition.

        For momentum blocks this collapses the augmented AR(2) state to the
        conditional Gaussian law of ``z[k+1]`` given ``z[k]`` using the declared
        lag covariance.  This keeps the scalar bridge reference consistent with
        the actually observed marginal channel while companion diagnostics
        retain the second-order stability information.
        """

        c1, c2 = self.companion_coefficients_at(self.step_size)
        process_innovation = self.step_size**2 * self.noise_scale / self.effective_batch
        covariance_next_current = c1 * self.variance + c2 * self.lag_covariance
        contraction = np.divide(
            covariance_next_current,
            np.maximum(self.variance, 1e-30),
            out=np.zeros_like(self.variance),
            where=self.variance > 1e-30,
        )
        next_variance = (
            c1**2 * self.variance
            + c2**2 * self.previous_variance
            + 2.0 * c1 * c2 * self.lag_covariance
            + process_innovation
        )
        innovation = np.maximum(next_variance - contraction**2 * self.variance, 0.0)
        return GaussianTransition(contraction=contraction, innovation=innovation)

    def state(self) -> GaussianState:
        return GaussianState(
            variance=self.variance,
            confidence=self.effective_confidence,
            labels=self.labels,
        )


@dataclass(frozen=True, slots=True)
class ChannelObservation:
    """Everything the generic controller needs before planning a transition."""

    state: GaussianState
    reference: GaussianTransition
    local_dynamics: LocalDynamics | None = None
    payload: Any = None
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.reference.size != self.state.size:
            raise ValueError("state and reference transition sizes do not match.")
        if self.local_dynamics is not None and self.local_dynamics.size != self.state.size:
            raise ValueError("local dynamics and state sizes do not match.")


@dataclass(frozen=True, slots=True)
class ActuationPlan:
    """Adapter-level realization of an ideal Gaussian transition."""

    controls: Mapping[str, Any]
    predicted: GaussianTransition
    feasible: bool
    target_variance: FloatArray
    predicted_variance: FloatArray
    error: FloatArray
    diagnostics: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        target = as_float_array(self.target_variance, name="target_variance")
        predicted = broadcast_array(self.predicted_variance, target.size, name="predicted_variance")
        error = broadcast_array(self.error, target.size, name="error")
        if self.predicted.size != target.size:
            raise ValueError("predicted transition and target sizes do not match.")
        object.__setattr__(self, "target_variance", target)
        object.__setattr__(self, "predicted_variance", predicted)
        object.__setattr__(self, "error", error)


@dataclass(frozen=True, slots=True)
class ControlCommand:
    """A planned but not-yet-applied controller command."""

    channel: str
    controls: Mapping[str, Any]
    desired: GaussianTransition
    predicted: GaussianTransition
    target_variance: FloatArray
    predicted_variance: FloatArray
    requested_progress: float
    accepted_progress: float
    next_step: int
    feasible: bool
    diagnostics: Mapping[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class ChannelState:
    """Serializable mutable state for one persistent or episodic channel."""

    progress: float = 0.0
    step: int = 0
    last_controls: dict[str, Any] = field(default_factory=dict)
    last_target_variance: FloatArray | None = None
    last_predicted_variance: FloatArray | None = None
    cumulative_innovation: FloatArray | None = None
    cumulative_probe_innovation: FloatArray | None = None
    cumulative_compute: float = 0.0

    def state_dict(self) -> dict[str, Any]:
        return {
            "progress": float(self.progress),
            "step": int(self.step),
            "last_controls": _copy_serializable(self.last_controls),
            "last_target_variance": _optional_array(self.last_target_variance),
            "last_predicted_variance": _optional_array(self.last_predicted_variance),
            "cumulative_innovation": _optional_array(self.cumulative_innovation),
            "cumulative_probe_innovation": _optional_array(
                self.cumulative_probe_innovation
            ),
            "cumulative_compute": float(self.cumulative_compute),
        }

    @classmethod
    def from_state_dict(cls, state: Mapping[str, Any]) -> "ChannelState":
        return cls(
            progress=float(state.get("progress", 0.0)),
            step=int(state.get("step", 0)),
            last_controls=dict(state.get("last_controls", {})),
            last_target_variance=_read_optional_array(
                state.get("last_target_variance"), "last_target_variance"
            ),
            last_predicted_variance=_read_optional_array(
                state.get("last_predicted_variance"), "last_predicted_variance"
            ),
            cumulative_innovation=_read_optional_array(
                state.get("cumulative_innovation"), "cumulative_innovation"
            ),
            cumulative_probe_innovation=_read_optional_array(
                state.get("cumulative_probe_innovation"),
                "cumulative_probe_innovation",
            ),
            cumulative_compute=float(state.get("cumulative_compute", 0.0)),
        )


def _optional_array(value: FloatArray | None) -> list[float] | None:
    return None if value is None else np.asarray(value, dtype=np.float64).tolist()


def _read_optional_array(value: Any, name: str) -> FloatArray | None:
    return None if value is None else as_float_array(value, name=name)


def _copy_serializable(value: Any) -> Any:
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, np.generic):
        return value.item()
    if isinstance(value, Mapping):
        return {str(k): _copy_serializable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_copy_serializable(v) for v in value]
    return value
