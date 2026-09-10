"""Gray-box and fallback identification for momentum learning dynamics.

Known commands should be removed algebraically before fitting the plant.  For
heavy-ball dynamics,

    z[k+1] = (1 + mu[k] - eta[k] h) z[k] - mu[k] z[k-1] - eta[k] xi[k],

we reconstruct

    zeta[k] = ((1+mu[k])z[k] - mu[k]z[k-1] - z[k+1]) / eta[k]
            = h z[k] + xi[k],

and estimate ``h`` by weighted least squares (or an instrumental-variable
variant when the centered state is noisy).  A black-box AR(2) fit remains an
adequacy diagnostic rather than the primary estimator.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Sequence

import numpy as np
import numpy.typing as npt

from .types import FloatArray


@dataclass(frozen=True, slots=True)
class GrayBoxMomentumEstimate:
    curvature: FloatArray
    noise_scale: FloatArray
    curvature_standard_error: FloatArray
    contrast_standard_error: FloatArray
    contrast: FloatArray
    confidence: FloatArray
    sample_count: FloatArray
    used_instrumental_variables: bool
    one_step_rmse: FloatArray

    def local_dynamics_kwargs(self) -> dict[str, FloatArray]:
        return {
            "curvature": self.curvature.copy(),
            "noise_scale": self.noise_scale.copy(),
            "confidence": self.confidence.copy(),
        }

    def probe_metadata(self) -> dict[str, FloatArray]:
        return {
            "contrast_standard_error": self.contrast_standard_error.copy(),
            "c1_minus_c2": self.contrast.copy(),
            "gray_box_one_step_rmse": self.one_step_rmse.copy(),
        }


@dataclass(slots=True)
class GrayBoxMomentumObserver:
    """Estimate curvature and gradient-noise scale under varying commands."""

    ridge: float = 1e-10
    curvature_floor: float = 0.0
    minimum_samples: int = 24
    relative_error_scale: float = 0.25
    instrument_lag: int | None = None

    def __post_init__(self) -> None:
        if self.ridge < 0.0:
            raise ValueError("ridge must be non-negative.")
        if self.minimum_samples < 4:
            raise ValueError("minimum_samples must be at least 4.")
        if self.relative_error_scale <= 0.0:
            raise ValueError("relative_error_scale must be positive.")
        if self.instrument_lag is not None and self.instrument_lag < 2:
            raise ValueError("instrument_lag must be at least 2 when supplied.")

    def estimate(
        self,
        histories: Sequence[npt.ArrayLike],
        step_histories: Sequence[npt.ArrayLike],
        momentum_histories: Sequence[npt.ArrayLike],
        batch_histories: Sequence[npt.ArrayLike],
    ) -> GrayBoxMomentumEstimate:
        count = len(histories)
        if not (
            len(step_histories)
            == len(momentum_histories)
            == len(batch_histories)
            == count
        ):
            raise ValueError("all history collections must have the same block count.")

        curvature: list[float] = []
        noise: list[float] = []
        standard_error: list[float] = []
        contrast_error: list[float] = []
        contrast: list[float] = []
        confidence: list[float] = []
        sample_count: list[float] = []
        one_step_rmse: list[float] = []

        for state_raw, eta_raw, mu_raw, batch_raw in zip(
            histories, step_histories, momentum_histories, batch_histories, strict=True
        ):
            state = np.asarray(state_raw, dtype=np.float64)
            if state.ndim == 1:
                state = state[:, None]
            if state.shape[0] < 4:
                raise ValueError("each state history needs at least four time points.")
            transitions = state.shape[0] - 1
            eta = _command_array(eta_raw, transitions, "step_history")
            mu = _command_array(mu_raw, transitions, "momentum_history")
            batch = _command_array(batch_raw, transitions, "batch_history")
            if np.any(eta <= 0.0):
                raise ValueError("gray-box reconstruction requires positive step sizes.")
            if np.any((mu < 0.0) | (mu >= 1.0)):
                raise ValueError("momentum commands must lie in [0, 1).")
            if np.any(batch <= 0.0):
                raise ValueError("batch sizes must be positive.")

            # Recurrence index k=1,...,T-2 uses command k.
            z_prev = state[:-2]
            z = state[1:-1]
            z_next = state[2:]
            eta_k = eta[1:, None]
            mu_k = mu[1:, None]
            batch_k = batch[1:, None]
            zeta = ((1.0 + mu_k) * z - mu_k * z_prev - z_next) / eta_k
            weights = np.broadcast_to(batch_k, z.shape)
            z_prev_used = z_prev
            z_next_used = z_next

            if self.instrument_lag is None:
                numerator = float(np.sum(weights * z * zeta))
                denominator = float(np.sum(weights * z * z)) + self.ridge
            else:
                lag = int(self.instrument_lag)
                if state.shape[0] <= lag + 2:
                    raise ValueError("history is too short for the requested instrument lag.")
                # Align q=z[k-lag] with k=lag,...,T-2.
                q = state[: -(lag + 1)]
                z_iv = state[lag:-1]
                z_next_iv = state[lag + 1 :]
                z_prev_iv = state[lag - 1 : -2]
                eta_iv = eta[lag:, None]
                mu_iv = mu[lag:, None]
                batch_iv = batch[lag:, None]
                zeta_iv = (
                    (1.0 + mu_iv) * z_iv - mu_iv * z_prev_iv - z_next_iv
                ) / eta_iv
                weights_iv = np.broadcast_to(batch_iv, z_iv.shape)
                numerator = float(np.sum(weights_iv * q * zeta_iv))
                denominator = float(np.sum(weights_iv * q * z_iv))
                if abs(denominator) <= self.ridge:
                    denominator = np.sign(denominator or 1.0) * self.ridge
                z = z_iv
                zeta = zeta_iv
                weights = weights_iv
                eta_k = eta_iv
                mu_k = mu_iv
                batch_k = batch_iv
                z_prev_used = z_prev_iv
                z_next_used = z_next_iv

            h = max(numerator / denominator, self.curvature_floor)
            residual = zeta - h * z
            nu = float(np.mean(weights * residual**2))
            information = float(np.sum(weights * z**2)) + self.ridge
            se_h = float(np.sqrt(max(nu, 0.0) / information))
            latest_eta = float(np.asarray(eta_k).reshape(-1)[-1])
            latest_mu = float(np.asarray(mu_k).reshape(-1)[-1])
            c1 = 1.0 + latest_mu - latest_eta * h
            c2 = -latest_mu
            c_contrast = c1 - c2
            se_contrast = latest_eta * se_h

            predicted_next = (
                (1.0 + mu_k - eta_k * h) * z - mu_k * z_prev_used
            )
            # The prediction excludes the martingale innovation, so its RMSE is
            # a direct calibration scale for the structural one-step model.
            rmse = float(np.sqrt(np.mean((z_next_used - predicted_next) ** 2)))
            samples = float(z.size)
            sample_factor = min(1.0, samples / self.minimum_samples)
            relative = se_h / max(abs(h), self.curvature_floor, 1e-12)
            score = sample_factor * np.exp(-(
                relative / self.relative_error_scale
            ) ** 2)

            curvature.append(h)
            noise.append(max(nu, 0.0))
            standard_error.append(se_h)
            contrast_error.append(se_contrast)
            contrast.append(c_contrast)
            confidence.append(float(np.clip(score, 0.0, 1.0)))
            sample_count.append(samples)
            one_step_rmse.append(rmse)

        return GrayBoxMomentumEstimate(
            curvature=np.asarray(curvature),
            noise_scale=np.asarray(noise),
            curvature_standard_error=np.asarray(standard_error),
            contrast_standard_error=np.asarray(contrast_error),
            contrast=np.asarray(contrast),
            confidence=np.asarray(confidence),
            sample_count=np.asarray(sample_count),
            used_instrumental_variables=self.instrument_lag is not None,
            one_step_rmse=np.asarray(one_step_rmse),
        )


def _command_array(value: npt.ArrayLike, transitions: int, name: str) -> FloatArray:
    array = np.asarray(value, dtype=np.float64).reshape(-1)
    if array.size == 1:
        return np.full(transitions, float(array[0]), dtype=np.float64)
    if array.size == transitions + 1:
        array = array[:-1]
    if array.size != transitions:
        raise ValueError(f"{name} must be scalar or have {transitions} values.")
    if not np.all(np.isfinite(array)):
        raise ValueError(f"{name} must be finite.")
    return array


@dataclass(frozen=True, slots=True)
class StructuralAdequacyEstimate:
    gray_box_rmse: FloatArray
    black_box_rmse: FloatArray
    relative_gap: FloatArray
    confidence: FloatArray
    gray_box_preferred: FloatArray


@dataclass(slots=True)
class StructuralAR2AdequacyObserver:
    """Compare a declared gray-box momentum model to black-box AR(2)."""

    gap_scale: float = 0.25
    error_floor: float = 1e-10

    def __post_init__(self) -> None:
        if self.gap_scale <= 0.0:
            raise ValueError("gap_scale must be positive.")

    def estimate(
        self,
        histories: Sequence[npt.ArrayLike],
        step_histories: Sequence[npt.ArrayLike],
        momentum_histories: Sequence[npt.ArrayLike],
        curvature: npt.ArrayLike,
    ) -> StructuralAdequacyEstimate:
        h_values = np.asarray(curvature, dtype=np.float64).reshape(-1)
        if h_values.size != len(histories):
            raise ValueError("curvature needs one value per block.")
        gray_rmse: list[float] = []
        black_rmse: list[float] = []
        gap: list[float] = []
        confidence: list[float] = []
        preferred: list[float] = []
        for index, (state_raw, eta_raw, mu_raw) in enumerate(
            zip(histories, step_histories, momentum_histories, strict=True)
        ):
            state = np.asarray(state_raw, dtype=np.float64)
            if state.ndim == 1:
                state = state[:, None]
            transitions = state.shape[0] - 1
            eta = _command_array(eta_raw, transitions, "step_history")
            mu = _command_array(mu_raw, transitions, "momentum_history")
            z_prev = state[:-2]
            z = state[1:-1]
            actual = state[2:]
            eta_k = eta[1:, None]
            mu_k = mu[1:, None]
            gray_prediction = (
                (1.0 + mu_k - eta_k * h_values[index]) * z - mu_k * z_prev
            )
            gray = float(np.sqrt(np.mean((actual - gray_prediction) ** 2)))

            y = actual.reshape(-1)
            design = np.column_stack([z.reshape(-1), z_prev.reshape(-1)])
            coefficients, *_ = np.linalg.lstsq(design, y, rcond=None)
            black_prediction = (design @ coefficients).reshape(actual.shape)
            black = float(np.sqrt(np.mean((actual - black_prediction) ** 2)))
            relative = max(gray - black, 0.0) / max(black, self.error_floor)
            score = float(np.exp(-(relative / self.gap_scale) ** 2))
            gray_rmse.append(gray)
            black_rmse.append(black)
            gap.append(relative)
            confidence.append(score)
            preferred.append(float(relative <= self.gap_scale))
        return StructuralAdequacyEstimate(
            gray_box_rmse=np.asarray(gray_rmse),
            black_box_rmse=np.asarray(black_rmse),
            relative_gap=np.asarray(gap),
            confidence=np.asarray(confidence),
            gray_box_preferred=np.asarray(preferred),
        )


@dataclass(frozen=True, slots=True)
class RLSAR2Estimate:
    c1: FloatArray
    c2: FloatArray
    covariance: FloatArray
    contrast_standard_error: FloatArray
    effective_memory: float
    recommended_coefficient_slew: float


@dataclass(slots=True)
class ForgettingFactorAR2Observer:
    """Black-box fallback for blocks whose structural map is not trusted."""

    blocks: int
    forgetting: float = 0.99
    initial_covariance: float = 1e3
    slew_fraction: float = 0.25
    _coefficients: FloatArray = field(init=False, repr=False)
    _covariance: FloatArray = field(init=False, repr=False)
    _residual_variance: FloatArray = field(init=False, repr=False)

    def __post_init__(self) -> None:
        if self.blocks <= 0:
            raise ValueError("blocks must be positive.")
        if not 0.0 < self.forgetting < 1.0:
            raise ValueError("forgetting must lie in (0, 1).")
        if self.initial_covariance <= 0.0:
            raise ValueError("initial_covariance must be positive.")
        if self.slew_fraction <= 0.0:
            raise ValueError("slew_fraction must be positive.")
        self._coefficients = np.zeros((self.blocks, 2), dtype=np.float64)
        self._covariance = np.repeat(
            (self.initial_covariance * np.eye(2))[None, :, :], self.blocks, axis=0
        )
        self._residual_variance = np.ones(self.blocks, dtype=np.float64)

    @property
    def effective_memory(self) -> float:
        return 1.0 / (1.0 - self.forgetting)

    @property
    def recommended_coefficient_slew(self) -> float:
        return self.slew_fraction / self.effective_memory

    def update(
        self,
        previous_previous: npt.ArrayLike,
        previous: npt.ArrayLike,
        current: npt.ArrayLike,
    ) -> RLSAR2Estimate:
        z2 = np.asarray(previous_previous, dtype=np.float64).reshape(self.blocks, -1)
        z1 = np.asarray(previous, dtype=np.float64).reshape(self.blocks, -1)
        z0 = np.asarray(current, dtype=np.float64).reshape(self.blocks, -1)
        if z2.shape != z1.shape or z1.shape != z0.shape:
            raise ValueError("state arrays must have matching block/replicate shapes.")
        for block in range(self.blocks):
            design = np.column_stack([z1[block], z2[block]])
            response = z0[block]
            covariance = self._covariance[block]
            information = np.linalg.inv(covariance)
            updated_information = (
                self.forgetting * information + design.T @ design
            )
            rhs = (
                self.forgetting * information @ self._coefficients[block]
                + design.T @ response
            )
            self._coefficients[block] = np.linalg.solve(updated_information, rhs)
            self._covariance[block] = np.linalg.inv(updated_information)
            residual = response - design @ self._coefficients[block]
            residual_energy = float(np.mean(residual**2))
            self._residual_variance[block] = (
                self.forgetting * self._residual_variance[block]
                + (1.0 - self.forgetting) * residual_energy
            )
        contrast_vector = np.asarray([1.0, -1.0])
        contrast_se = np.sqrt(
            np.maximum(
                [
                    self._residual_variance[index]
                    * contrast_vector
                    @ self._covariance[index]
                    @ contrast_vector
                    for index in range(self.blocks)
                ],
                0.0,
            )
        )
        return RLSAR2Estimate(
            c1=self._coefficients[:, 0].copy(),
            c2=self._coefficients[:, 1].copy(),
            covariance=self._covariance.copy(),
            contrast_standard_error=np.asarray(contrast_se),
            effective_memory=self.effective_memory,
            recommended_coefficient_slew=self.recommended_coefficient_slew,
        )

    def reset(self) -> None:
        self._coefficients = np.zeros((self.blocks, 2), dtype=np.float64)
        self._covariance = np.repeat(
            (self.initial_covariance * np.eye(2))[None, :, :], self.blocks, axis=0
        )
        self._residual_variance = np.ones(self.blocks, dtype=np.float64)

    def state_dict(self) -> dict[str, object]:
        return {
            "coefficients": self._coefficients.tolist(),
            "covariance": self._covariance.tolist(),
            "residual_variance": self._residual_variance.tolist(),
        }

    def load_state_dict(self, state: dict[str, object]) -> None:
        coefficients = np.asarray(state["coefficients"], dtype=np.float64)
        covariance = np.asarray(state["covariance"], dtype=np.float64)
        residual = np.asarray(state["residual_variance"], dtype=np.float64)
        if coefficients.shape != (self.blocks, 2):
            raise ValueError("RLS coefficient checkpoint has the wrong shape.")
        if covariance.shape != (self.blocks, 2, 2):
            raise ValueError("RLS covariance checkpoint has the wrong shape.")
        if residual.shape != (self.blocks,):
            raise ValueError("RLS residual checkpoint has the wrong shape.")
        self._coefficients = coefficients
        self._covariance = covariance
        self._residual_variance = residual
