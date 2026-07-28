"""Boundary-derived covariance paths.

The Brownian path retained from v0.1 is useful as an explanatory baseline.  The
recommended operational path in v0.2 is :class:`LinearGaussianBridgePath`,
whose marginals and cross-time transitions are derived from the same identified
linear-Gaussian reference process used by the controller.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Sequence

import numpy as np
import numpy.typing as npt

from .types import FloatArray, GaussianTransition, as_float_array, broadcast_array


class BridgePath(Protocol):
    @property
    def size(self) -> int:
        ...

    def variance(self, progress: float) -> FloatArray:
        ...

    def state_dict(self) -> dict[str, object]:
        ...


def _validate_progress(progress: float) -> float:
    progress = float(progress)
    if not np.isfinite(progress):
        raise ValueError("progress must be finite.")
    return float(np.clip(progress, 0.0, 1.0))


@dataclass(frozen=True, slots=True)
class GaussianBridgePath:
    r"""Diagonal Brownian Schrodinger-bridge covariance path.

    This class is retained for theory, visualization, and backwards
    compatibility.  For reference-consistent control use
    :class:`LinearGaussianBridgePath` or :class:`ReferenceBridgePlanner`.
    """

    start_variance: FloatArray
    terminal_variance: FloatArray
    diffusion_budget: FloatArray
    labels: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        start = as_float_array(self.start_variance, name="start_variance")
        terminal = broadcast_array(self.terminal_variance, start.size, name="terminal_variance")
        budget = broadcast_array(self.diffusion_budget, start.size, name="diffusion_budget")
        if np.any(start < 0.0) or np.any(terminal < 0.0):
            raise ValueError("endpoint variances must be non-negative.")
        if np.any(budget < 0.0):
            raise ValueError("diffusion_budget must be non-negative.")
        if self.labels and len(self.labels) != start.size:
            raise ValueError("labels must have one entry per block.")
        object.__setattr__(self, "start_variance", start)
        object.__setattr__(self, "terminal_variance", terminal)
        object.__setattr__(self, "diffusion_budget", budget)

    @property
    def size(self) -> int:
        return int(self.start_variance.size)

    @property
    def cross_coefficient(self) -> FloatArray:
        return np.sqrt(
            self.diffusion_budget**2
            + 4.0 * self.start_variance * self.terminal_variance
        )

    def variance(self, progress: float) -> FloatArray:
        s = _validate_progress(progress)
        return (
            self.start_variance * (1.0 - s) ** 2
            + self.terminal_variance * s**2
            + self.cross_coefficient * s * (1.0 - s)
        )

    def derivative(self, progress: float) -> FloatArray:
        s = _validate_progress(progress)
        cross = self.cross_coefficient
        return (
            -2.0 * self.start_variance * (1.0 - s)
            + 2.0 * self.terminal_variance * s
            + cross * (1.0 - 2.0 * s)
        )

    def peak_progress(self) -> FloatArray:
        cross = self.cross_coefficient
        denominator = 2.0 * (cross - self.start_variance - self.terminal_variance)
        numerator = cross - 2.0 * self.start_variance
        with np.errstate(divide="ignore", invalid="ignore"):
            peak = numerator / denominator
        endpoint = np.where(self.start_variance >= self.terminal_variance, 0.0, 1.0)
        concave = denominator > 0.0
        peak = np.where(concave & np.isfinite(peak), np.clip(peak, 0.0, 1.0), endpoint)
        return peak.astype(np.float64)

    def peak_variance(self) -> FloatArray:
        peaks = self.peak_progress()
        return np.asarray(
            [self.variance(float(peak))[index] for index, peak in enumerate(peaks)],
            dtype=np.float64,
        )

    def replan(
        self,
        *,
        start_variance: float | Sequence[float] | npt.ArrayLike,
        terminal_variance: float | Sequence[float] | npt.ArrayLike | None = None,
        diffusion_budget: float | Sequence[float] | npt.ArrayLike | None = None,
    ) -> "GaussianBridgePath":
        return GaussianBridgePath(
            start_variance=start_variance,
            terminal_variance=(
                self.terminal_variance if terminal_variance is None else terminal_variance
            ),
            diffusion_budget=(
                self.diffusion_budget if diffusion_budget is None else diffusion_budget
            ),
            labels=self.labels,
        )

    @classmethod
    def from_peak(
        cls,
        *,
        start_variance: float | Sequence[float] | npt.ArrayLike,
        peak_variance: float | Sequence[float] | npt.ArrayLike,
        terminal_variance: float | Sequence[float] | npt.ArrayLike,
        labels: tuple[str, ...] = (),
    ) -> "GaussianBridgePath":
        start = as_float_array(start_variance, name="start_variance")
        terminal = broadcast_array(terminal_variance, start.size, name="terminal_variance")
        peak = broadcast_array(peak_variance, start.size, name="peak_variance")
        if np.any(peak < np.maximum(start, terminal)):
            raise ValueError("peak_variance must be at least both endpoint variances.")
        left = np.sqrt(np.maximum(peak - start, 0.0))
        right = np.sqrt(np.maximum(peak - terminal, 0.0))
        cross = start + terminal + (left + right) ** 2
        budget = np.sqrt(np.maximum(cross**2 - 4.0 * start * terminal, 0.0))
        return cls(
            start_variance=start,
            terminal_variance=terminal,
            diffusion_budget=budget,
            labels=labels,
        )

    def state_dict(self) -> dict[str, object]:
        return {
            "type": "brownian_gaussian_bridge",
            "start_variance": self.start_variance.tolist(),
            "terminal_variance": self.terminal_variance.tolist(),
            "diffusion_budget": self.diffusion_budget.tolist(),
            "labels": list(self.labels),
        }


@dataclass(frozen=True, slots=True)
class LinearGaussianBridgePath:
    r"""Exact finite-horizon scalar/diagonal Schrodinger bridge.

    The reference dynamics for block ``b`` are

    ``X[k+1] = a[b] * X[k] + sqrt(r[b]) * xi[k]``.

    Both endpoint variances are pinned.  The endpoint coupling, all marginal
    variances, adjacent cross-covariances, and exact Markov bridge transitions
    are computed in closed form.  The path and transition therefore share one
    reference process, unlike the v0.1 Brownian-path/OU-projector composition.
    """

    start_variance: FloatArray
    terminal_variance: FloatArray
    horizon_steps: int
    reference_contraction: FloatArray
    reference_innovation: FloatArray
    labels: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        start = as_float_array(self.start_variance, name="start_variance")
        terminal = broadcast_array(self.terminal_variance, start.size, name="terminal_variance")
        contraction = broadcast_array(
            self.reference_contraction, start.size, name="reference_contraction"
        )
        innovation = broadcast_array(
            self.reference_innovation, start.size, name="reference_innovation"
        )
        if self.horizon_steps <= 0:
            raise ValueError("horizon_steps must be positive.")
        if np.any(start < 0.0) or np.any(terminal < 0.0):
            raise ValueError("endpoint variances must be non-negative.")
        if np.any(innovation <= 0.0):
            raise ValueError("reference_innovation must be strictly positive.")
        if self.labels and len(self.labels) != start.size:
            raise ValueError("labels must have one entry per block.")
        object.__setattr__(self, "start_variance", start)
        object.__setattr__(self, "terminal_variance", terminal)
        object.__setattr__(self, "reference_contraction", contraction)
        object.__setattr__(self, "reference_innovation", innovation)

    @property
    def size(self) -> int:
        return int(self.start_variance.size)

    @property
    def reference(self) -> GaussianTransition:
        return GaussianTransition(
            contraction=self.reference_contraction,
            innovation=self.reference_innovation,
        )

    def _moments(self) -> tuple[FloatArray, FloatArray, FloatArray, FloatArray]:
        """Return ``phi[k]``, ``gramian[k]``, backward products, endpoint coupling."""

        n = self.horizon_steps
        b = self.size
        phi = np.ones((n + 1, b), dtype=np.float64)
        gramian = np.zeros((n + 1, b), dtype=np.float64)
        for index in range(n):
            phi[index + 1] = self.reference_contraction * phi[index]
            gramian[index + 1] = (
                self.reference_contraction**2 * gramian[index]
                + self.reference_innovation
            )
        backward = np.ones((n + 1, b), dtype=np.float64)
        for index in range(n - 1, -1, -1):
            backward[index] = self.reference_contraction * backward[index + 1]
        total_phi = phi[-1]
        total_q = gramian[-1]
        root = np.sqrt(
            total_q**2
            + 4.0 * total_phi**2 * self.start_variance * self.terminal_variance
        )
        denominator = total_q + root
        endpoint_cross = np.divide(
            2.0 * total_phi * self.start_variance * self.terminal_variance,
            denominator,
            out=np.zeros_like(total_phi),
            where=denominator > 0.0,
        )
        return phi, gramian, backward, endpoint_cross

    def covariance_grid(self) -> FloatArray:
        phi, gramian, backward, endpoint_cross = self._moments()
        total_phi = phi[-1]
        total_q = gramian[-1]
        gain = backward * gramian / total_q
        alpha = phi - gain * total_phi
        beta = gain
        conditional = gramian - (backward * gramian) ** 2 / total_q
        covariance = (
            alpha**2 * self.start_variance
            + beta**2 * self.terminal_variance
            + 2.0 * alpha * beta * endpoint_cross
            + conditional
        )
        covariance[0] = self.start_variance
        covariance[-1] = self.terminal_variance
        return np.maximum(covariance, 0.0)

    def adjacent_cross_covariance_grid(self) -> FloatArray:
        phi, gramian, backward, endpoint_cross = self._moments()
        total_phi = phi[-1]
        total_q = gramian[-1]
        gain = backward * gramian / total_q
        alpha = phi - gain * total_phi
        beta = gain
        result = np.empty((self.horizon_steps, self.size), dtype=np.float64)
        for index in range(self.horizon_steps):
            noise_cross = (
                self.reference_contraction * gramian[index]
                - (backward[index] * gramian[index])
                * (backward[index + 1] * gramian[index + 1])
                / total_q
            )
            result[index] = (
                alpha[index] * alpha[index + 1] * self.start_variance
                + beta[index] * beta[index + 1] * self.terminal_variance
                + (
                    alpha[index] * beta[index + 1]
                    + beta[index] * alpha[index + 1]
                )
                * endpoint_cross
                + noise_cross
            )
        return result

    def transition_at(self, step: int) -> GaussianTransition:
        if step < 0 or step >= self.horizon_steps:
            raise IndexError("step must lie in [0, horizon_steps).")
        variances = self.covariance_grid()
        cross = self.adjacent_cross_covariance_grid()[step]
        current = variances[step]
        contraction = np.divide(
            cross,
            current,
            out=np.zeros_like(cross),
            where=current > 0.0,
        )
        innovation = np.maximum(
            variances[step + 1] - contraction**2 * current,
            0.0,
        )
        return GaussianTransition(contraction=contraction, innovation=innovation)

    def variance(self, progress: float) -> FloatArray:
        """Piecewise-linear interpolation of the exact discrete covariance grid."""

        s = _validate_progress(progress)
        position = s * self.horizon_steps
        left = min(int(np.floor(position)), self.horizon_steps)
        right = min(left + 1, self.horizon_steps)
        if left == right:
            return self.covariance_grid()[left].copy()
        fraction = position - left
        grid = self.covariance_grid()
        return (1.0 - fraction) * grid[left] + fraction * grid[right]

    def peak_progress(self) -> FloatArray:
        grid = self.covariance_grid()
        return np.argmax(grid, axis=0).astype(np.float64) / self.horizon_steps

    def replan(
        self,
        *,
        start_variance: float | Sequence[float] | npt.ArrayLike,
        horizon_steps: int | None = None,
        terminal_variance: float | Sequence[float] | npt.ArrayLike | None = None,
        reference: GaussianTransition | None = None,
    ) -> "LinearGaussianBridgePath":
        selected = self.reference if reference is None else reference
        return LinearGaussianBridgePath(
            start_variance=start_variance,
            terminal_variance=(
                self.terminal_variance if terminal_variance is None else terminal_variance
            ),
            horizon_steps=self.horizon_steps if horizon_steps is None else horizon_steps,
            reference_contraction=selected.contraction,
            reference_innovation=selected.innovation,
            labels=self.labels,
        )

    def state_dict(self) -> dict[str, object]:
        return {
            "type": "linear_gaussian_bridge",
            "start_variance": self.start_variance.tolist(),
            "terminal_variance": self.terminal_variance.tolist(),
            "horizon_steps": self.horizon_steps,
            "reference_contraction": self.reference_contraction.tolist(),
            "reference_innovation": self.reference_innovation.tolist(),
            "labels": list(self.labels),
        }


@dataclass(frozen=True, slots=True)
class PeakQuadraticPath:
    """Convenient three-width parameterization of the Brownian quadratic family."""

    start_variance: FloatArray
    peak_variance: FloatArray
    terminal_variance: FloatArray
    labels: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        bridge = GaussianBridgePath.from_peak(
            start_variance=self.start_variance,
            peak_variance=self.peak_variance,
            terminal_variance=self.terminal_variance,
            labels=self.labels,
        )
        object.__setattr__(self, "start_variance", bridge.start_variance)
        object.__setattr__(self, "peak_variance", bridge.peak_variance())
        object.__setattr__(self, "terminal_variance", bridge.terminal_variance)

    @property
    def size(self) -> int:
        return int(self.start_variance.size)

    @property
    def bridge(self) -> GaussianBridgePath:
        return GaussianBridgePath.from_peak(
            start_variance=self.start_variance,
            peak_variance=self.peak_variance,
            terminal_variance=self.terminal_variance,
            labels=self.labels,
        )

    def variance(self, progress: float) -> FloatArray:
        return self.bridge.variance(progress)

    def peak_progress(self) -> FloatArray:
        return self.bridge.peak_progress()

    def state_dict(self) -> dict[str, object]:
        return {
            "type": "peak_quadratic",
            "start_variance": self.start_variance.tolist(),
            "peak_variance": self.peak_variance.tolist(),
            "terminal_variance": self.terminal_variance.tolist(),
            "labels": list(self.labels),
        }


@dataclass(frozen=True, slots=True)
class ConstantVariancePath:
    target_variance: FloatArray
    labels: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        target = as_float_array(self.target_variance, name="target_variance")
        if np.any(target < 0.0):
            raise ValueError("target_variance must be non-negative.")
        if self.labels and len(self.labels) != target.size:
            raise ValueError("labels must have one entry per block.")
        object.__setattr__(self, "target_variance", target)

    @property
    def size(self) -> int:
        return int(self.target_variance.size)

    def variance(self, progress: float) -> FloatArray:
        _validate_progress(progress)
        return self.target_variance.copy()

    def state_dict(self) -> dict[str, object]:
        return {
            "type": "constant",
            "target_variance": self.target_variance.tolist(),
            "labels": list(self.labels),
        }
