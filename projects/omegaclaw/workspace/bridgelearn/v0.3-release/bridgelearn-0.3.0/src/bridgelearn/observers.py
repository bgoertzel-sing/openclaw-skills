"""Backend-neutral observers and robust filters."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Mapping, Sequence

import numpy as np
import numpy.typing as npt

from .types import FloatArray, GaussianState, GaussianTransition, as_float_array, broadcast_array


@dataclass(slots=True)
class AttackReleaseFilter:
    """Asymmetric exponential filter.

    Increases use ``attack`` and decreases use ``release``.  For noise and
    curvature safety estimates, a larger attack than release reacts quickly to
    dangerous increases while relaxing conservatism slowly.
    """

    attack: float = 0.7
    release: float = 0.1
    value: FloatArray | None = None

    def __post_init__(self) -> None:
        if not 0.0 < self.attack <= 1.0:
            raise ValueError("attack must lie in (0, 1].")
        if not 0.0 < self.release <= 1.0:
            raise ValueError("release must lie in (0, 1].")
        if self.value is not None:
            self.value = as_float_array(self.value, name="value")

    def update(self, observation: float | Sequence[float] | npt.ArrayLike) -> FloatArray:
        observed = as_float_array(observation, name="observation")
        if self.value is None:
            self.value = observed.copy()
            return self.value.copy()
        current = broadcast_array(self.value, observed.size, name="filter_value")
        alpha = np.where(observed >= current, self.attack, self.release)
        self.value = current + alpha * (observed - current)
        return self.value.copy()

    def state_dict(self) -> dict[str, object]:
        return {
            "attack": self.attack,
            "release": self.release,
            "value": None if self.value is None else self.value.tolist(),
        }


@dataclass(slots=True)
class ExponentialFilter:
    alpha: float = 0.1
    value: FloatArray | None = None

    def __post_init__(self) -> None:
        if not 0.0 < self.alpha <= 1.0:
            raise ValueError("alpha must lie in (0, 1].")
        if self.value is not None:
            self.value = as_float_array(self.value, name="value")

    def update(self, observation: float | Sequence[float] | npt.ArrayLike) -> FloatArray:
        observed = as_float_array(observation, name="observation")
        if self.value is None:
            self.value = observed.copy()
        else:
            current = broadcast_array(self.value, observed.size, name="filter_value")
            self.value = current + self.alpha * (observed - current)
        return self.value.copy()


@dataclass(frozen=True, slots=True)
class EmpiricalTransitionEstimate:
    state: GaussianState
    transition: GaussianTransition


@dataclass(slots=True)
class EmpiricalTransitionObserver:
    """Estimate diagonal contractions and innovations from paired samples.

    Each sequence element represents a block.  Arrays within a block may have
    arbitrary shape; they are flattened and centered before estimation.
    """

    variance_floor: float = 1e-12
    contraction_clip: tuple[float, float] | None = (-1.5, 1.5)

    def estimate(
        self,
        previous: Sequence[npt.ArrayLike],
        current: Sequence[npt.ArrayLike],
        *,
        labels: tuple[str, ...] = (),
    ) -> EmpiricalTransitionEstimate:
        if len(previous) != len(current):
            raise ValueError("previous and current must have the same number of blocks.")
        variances = []
        contractions = []
        innovations = []
        confidences = []
        for before_raw, after_raw in zip(previous, current, strict=True):
            before = np.asarray(before_raw, dtype=np.float64).reshape(-1)
            after = np.asarray(after_raw, dtype=np.float64).reshape(-1)
            if before.size != after.size or before.size < 2:
                raise ValueError("paired block samples must have equal size >= 2.")
            before = before - np.mean(before)
            after = after - np.mean(after)
            before_energy = float(np.dot(before, before) / before.size)
            after_variance = float(np.dot(after, after) / after.size)
            covariance = float(np.dot(after, before) / before.size)
            if before_energy <= self.variance_floor:
                contraction = 0.0
                confidence = 0.0
            else:
                contraction = covariance / before_energy
                confidence = before_energy / (before_energy + self.variance_floor)
            if self.contraction_clip is not None:
                contraction = float(np.clip(contraction, *self.contraction_clip))
            innovation = max(after_variance - contraction**2 * before_energy, 0.0)
            variances.append(after_variance)
            contractions.append(contraction)
            innovations.append(innovation)
            confidences.append(confidence)
        return EmpiricalTransitionEstimate(
            state=GaussianState(
                variance=np.asarray(variances),
                confidence=np.asarray(confidences),
                labels=labels,
            ),
            transition=GaussianTransition(
                contraction=np.asarray(contractions),
                innovation=np.asarray(innovations),
            ),
        )


@dataclass(slots=True)
class SecantCurvatureObserver:
    """Blockwise positive secant curvature estimator."""

    floor: float = 1e-8
    ceiling: float = np.inf
    filter: AttackReleaseFilter | ExponentialFilter | None = None

    def estimate(
        self,
        parameter_delta: Sequence[npt.ArrayLike],
        gradient_delta: Sequence[npt.ArrayLike],
    ) -> FloatArray:
        if len(parameter_delta) != len(gradient_delta):
            raise ValueError("parameter_delta and gradient_delta lengths differ.")
        values = []
        for dx_raw, dg_raw in zip(parameter_delta, gradient_delta, strict=True):
            dx = np.asarray(dx_raw, dtype=np.float64).reshape(-1)
            dg = np.asarray(dg_raw, dtype=np.float64).reshape(-1)
            if dx.size != dg.size:
                raise ValueError("secant arrays must have equal sizes within each block.")
            denominator = float(np.dot(dx, dx))
            if denominator <= self.floor:
                value = self.floor
            else:
                value = float(np.dot(dx, dg) / denominator)
                value = max(value, self.floor)
            values.append(min(value, self.ceiling))
        estimate = np.asarray(values, dtype=np.float64)
        return self.filter.update(estimate) if self.filter is not None else estimate


@dataclass(slots=True)
class SplitBatchNoiseObserver:
    """Estimate unit-batch gradient-noise trace from two independent half-batches."""

    floor: float = 0.0
    filter: AttackReleaseFilter | ExponentialFilter | None = None

    def estimate(
        self,
        gradients_a: Sequence[npt.ArrayLike],
        gradients_b: Sequence[npt.ArrayLike],
        *,
        full_batch_size: int,
    ) -> FloatArray:
        if full_batch_size <= 1:
            raise ValueError("full_batch_size must exceed 1.")
        if len(gradients_a) != len(gradients_b):
            raise ValueError("gradient block lengths differ.")
        values = []
        for first_raw, second_raw in zip(gradients_a, gradients_b, strict=True):
            first = np.asarray(first_raw, dtype=np.float64).reshape(-1)
            second = np.asarray(second_raw, dtype=np.float64).reshape(-1)
            if first.size != second.size or first.size == 0:
                raise ValueError("gradient blocks must have equal nonzero size.")
            difference = first - second
            mean_square = float(np.dot(difference, difference) / difference.size)
            # Two independent half-batch means have difference variance 4Q/m.
            unit_batch_variance = 0.25 * full_batch_size * mean_square
            values.append(max(unit_batch_variance, self.floor))
        estimate = np.asarray(values, dtype=np.float64)
        return self.filter.update(estimate) if self.filter is not None else estimate


@dataclass(slots=True)
class ResidualDecayObserver:
    """Estimate contraction from consecutive fixed-point or predictive residuals."""

    floor: float = 1e-12
    contraction_clip: tuple[float, float] = (0.0, 1.5)
    filter: ExponentialFilter | None = None

    def estimate(
        self,
        previous_residuals: Sequence[npt.ArrayLike],
        current_residuals: Sequence[npt.ArrayLike],
    ) -> FloatArray:
        if len(previous_residuals) != len(current_residuals):
            raise ValueError("residual block lengths differ.")
        contractions = []
        for previous_raw, current_raw in zip(
            previous_residuals,
            current_residuals,
            strict=True,
        ):
            previous = np.asarray(previous_raw, dtype=np.float64).reshape(-1)
            current = np.asarray(current_raw, dtype=np.float64).reshape(-1)
            if previous.size != current.size:
                raise ValueError("residual arrays must have equal block sizes.")
            denominator = float(np.linalg.norm(previous))
            ratio = float(np.linalg.norm(current)) / max(denominator, self.floor)
            contractions.append(float(np.clip(ratio, *self.contraction_clip)))
        estimate = np.asarray(contractions, dtype=np.float64)
        return self.filter.update(estimate) if self.filter is not None else estimate


def block_variances(blocks: Iterable[npt.ArrayLike]) -> FloatArray:
    """Return population variances for an iterable of arbitrary-shaped blocks."""

    result = []
    for block_raw in blocks:
        block = np.asarray(block_raw, dtype=np.float64).reshape(-1)
        if block.size == 0:
            raise ValueError("blocks must be non-empty.")
        result.append(float(np.var(block)))
    return np.asarray(result, dtype=np.float64)


@dataclass(frozen=True, slots=True)
class AR2AdequacyEstimate:
    """Blockwise AR(2) fit and an AR(1)-adequacy confidence score."""

    phi1: FloatArray
    phi2: FloatArray
    innovation: FloatArray
    spectral_radius: FloatArray
    ar1_residual_autocorrelation: FloatArray
    ar1_adequacy: FloatArray
    regressor_condition: FloatArray
    contrast_standard_error: FloatArray
    c1_minus_c2: FloatArray

    def probe_metadata(self) -> dict[str, FloatArray]:
        return {
            "c1": self.phi1.copy(),
            "c2": self.phi2.copy(),
            "regressor_condition": self.regressor_condition.copy(),
            "contrast_standard_error": self.contrast_standard_error.copy(),
            "ar2_spectral_radius": self.spectral_radius.copy(),
        }


@dataclass(slots=True)
class AR2AdequacyObserver:
    """Detect first-order misspecification caused by momentum or oscillatory plants.

    Each block is supplied as an array whose first axis is time.  Remaining
    axes are treated as independent replicate coordinates and flattened into
    the regression.  The returned ``ar1_adequacy`` should multiply the ordinary
    observer confidence before a scalar AR(1) controller is allowed to act.
    """

    autocorrelation_scale: float = 0.20
    minimum_samples: int = 24
    ridge: float = 1e-8

    def __post_init__(self) -> None:
        if self.autocorrelation_scale <= 0.0:
            raise ValueError("autocorrelation_scale must be positive.")
        if self.minimum_samples < 6:
            raise ValueError("minimum_samples must be at least 6.")
        if self.ridge < 0.0:
            raise ValueError("ridge must be non-negative.")

    def estimate(self, histories: Sequence[npt.ArrayLike]) -> AR2AdequacyEstimate:
        phi1: list[float] = []
        phi2: list[float] = []
        innovation: list[float] = []
        radius: list[float] = []
        residual_corr: list[float] = []
        adequacy: list[float] = []
        conditions: list[float] = []
        contrast_errors: list[float] = []
        contrasts: list[float] = []
        for raw in histories:
            series = np.asarray(raw, dtype=np.float64)
            if series.ndim == 1:
                series = series[:, None]
            if series.shape[0] < 4:
                raise ValueError("each AR history needs at least four time points.")
            centered = series - np.mean(series, axis=0, keepdims=True)
            y = centered[2:].reshape(-1)
            x1 = centered[1:-1].reshape(-1)
            x2 = centered[:-2].reshape(-1)
            design = np.column_stack([x1, x2])
            raw_gram = design.T @ design
            gram = raw_gram + self.ridge * np.eye(2)
            coefficients = np.linalg.solve(gram, design.T @ y)
            first, second = map(float, coefficients)
            residual = y - design @ coefficients
            innovation_value = float(np.mean(residual**2))
            roots = np.roots([1.0, -first, -second])
            spectral = float(np.max(np.abs(roots)))

            ar1_denominator = float(np.dot(x1, x1)) + self.ridge
            ar1 = float(np.dot(x1, y) / ar1_denominator)
            ar1_residual_matrix = centered[2:] - ar1 * centered[1:-1]
            if ar1_residual_matrix.shape[0] < 2 or np.std(ar1_residual_matrix) <= 1e-15:
                correlation = 0.0
            else:
                later = ar1_residual_matrix[1:].reshape(-1)
                earlier = ar1_residual_matrix[:-1].reshape(-1)
                correlation = float(np.corrcoef(later, earlier)[0, 1])
                if not np.isfinite(correlation):
                    correlation = 0.0
            sample_factor = min(1.0, y.size / self.minimum_samples)
            score = sample_factor * np.exp(
                -(abs(correlation) / self.autocorrelation_scale) ** 2
            )
            condition = float(np.linalg.cond(raw_gram + max(self.ridge, 1e-15) * np.eye(2)))
            try:
                coefficient_covariance = innovation_value * np.linalg.inv(gram)
                contrast_vector = np.asarray([1.0, -1.0])
                contrast_error = float(
                    np.sqrt(
                        max(
                            float(contrast_vector @ coefficient_covariance @ contrast_vector),
                            0.0,
                        )
                    )
                )
            except np.linalg.LinAlgError:
                contrast_error = float("inf")
            phi1.append(first)
            phi2.append(second)
            innovation.append(max(innovation_value, 0.0))
            radius.append(spectral)
            residual_corr.append(correlation)
            adequacy.append(float(np.clip(score, 0.0, 1.0)))
            conditions.append(condition)
            contrast_errors.append(contrast_error)
            contrasts.append(first - second)
        return AR2AdequacyEstimate(
            phi1=np.asarray(phi1),
            phi2=np.asarray(phi2),
            innovation=np.asarray(innovation),
            spectral_radius=np.asarray(radius),
            ar1_residual_autocorrelation=np.asarray(residual_corr),
            ar1_adequacy=np.asarray(adequacy),
            regressor_condition=np.asarray(conditions),
            contrast_standard_error=np.asarray(contrast_errors),
            c1_minus_c2=np.asarray(contrasts),
        )


@dataclass(slots=True)
class CurvatureResponseObserver:
    """Fit ``h(eta) = intercept + slope * (eta - eta_ref)`` per block."""

    ridge: float = 1e-8
    slope_clip: tuple[float, float] = (-1e6, 1e6)

    def estimate(
        self,
        step_histories: Sequence[npt.ArrayLike],
        curvature_histories: Sequence[npt.ArrayLike],
    ) -> tuple[FloatArray, FloatArray]:
        if len(step_histories) != len(curvature_histories):
            raise ValueError("step and curvature history block counts differ.")
        intercepts: list[float] = []
        slopes: list[float] = []
        for step_raw, curvature_raw in zip(
            step_histories, curvature_histories, strict=True
        ):
            step = np.asarray(step_raw, dtype=np.float64).reshape(-1)
            curvature = np.asarray(curvature_raw, dtype=np.float64).reshape(-1)
            if step.size != curvature.size or step.size < 3:
                raise ValueError("each response history needs equal length >= 3.")
            reference = float(step[-1])
            centered_step = step - reference
            design = np.column_stack([np.ones_like(centered_step), centered_step])
            coefficients = np.linalg.solve(
                design.T @ design + self.ridge * np.eye(2),
                design.T @ curvature,
            )
            intercepts.append(max(float(coefficients[0]), 0.0))
            slopes.append(float(np.clip(coefficients[1], *self.slope_clip)))
        return np.asarray(intercepts), np.asarray(slopes)
