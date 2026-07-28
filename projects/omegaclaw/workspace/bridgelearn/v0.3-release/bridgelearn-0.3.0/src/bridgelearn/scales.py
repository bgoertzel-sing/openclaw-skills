"""Pluggable active-width estimators, including robust heavy-tail alternatives."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, Sequence

import numpy as np
import numpy.typing as npt

from .types import FloatArray


class ScaleEstimator(Protocol):
    def variance(self, values: npt.ArrayLike) -> float:
        ...


@dataclass(frozen=True, slots=True)
class VarianceScale:
    ddof: int = 0

    def variance(self, values: npt.ArrayLike) -> float:
        array = np.asarray(values, dtype=np.float64).reshape(-1)
        if array.size <= self.ddof:
            raise ValueError("not enough values for requested ddof.")
        return float(np.var(array, ddof=self.ddof))


@dataclass(frozen=True, slots=True)
class TrimmedVarianceScale:
    trim_fraction: float = 0.05

    def __post_init__(self) -> None:
        if not 0.0 <= self.trim_fraction < 0.5:
            raise ValueError("trim_fraction must lie in [0, 0.5).")

    def variance(self, values: npt.ArrayLike) -> float:
        array = np.sort(np.asarray(values, dtype=np.float64).reshape(-1))
        if array.size < 2:
            raise ValueError("at least two values are required.")
        trim = int(np.floor(self.trim_fraction * array.size))
        selected = array[trim : array.size - trim] if trim else array
        if selected.size < 2:
            raise ValueError("trim_fraction leaves too few observations.")
        return float(np.var(selected))


@dataclass(frozen=True, slots=True)
class IQRScale:
    """Gaussian-calibrated variance from the interquartile range."""

    normal_iqr: float = 1.3489795003921634

    def variance(self, values: npt.ArrayLike) -> float:
        array = np.asarray(values, dtype=np.float64).reshape(-1)
        if array.size < 4:
            raise ValueError("at least four values are required for IQR scale.")
        q25, q75 = np.quantile(array, [0.25, 0.75])
        sigma = (q75 - q25) / self.normal_iqr
        return float(max(sigma * sigma, 0.0))


@dataclass(frozen=True, slots=True)
class MADScale:
    """Gaussian-calibrated variance from median absolute deviation."""

    normal_mad: float = 0.6744897501960817

    def variance(self, values: npt.ArrayLike) -> float:
        array = np.asarray(values, dtype=np.float64).reshape(-1)
        if array.size < 3:
            raise ValueError("at least three values are required for MAD scale.")
        median = float(np.median(array))
        mad = float(np.median(np.abs(array - median)))
        sigma = mad / self.normal_mad
        return float(max(sigma * sigma, 0.0))


@dataclass(slots=True)
class CenteredWidthObserver:
    """Track an explicit EMA center and measure scale around it.

    The centering filter is part of the plant/observer model, not an invisible
    preprocessing choice.  ``mixing_ratio(control_interval)`` reports how many
    approximate EMA time constants elapse between control interventions.
    """

    center_alpha: float = 0.2
    scale: ScaleEstimator = field(default_factory=VarianceScale)
    centers: list[np.ndarray] | None = None

    def __post_init__(self) -> None:
        if not 0.0 < self.center_alpha <= 1.0:
            raise ValueError("center_alpha must lie in (0, 1].")

    @property
    def mixing_time(self) -> float:
        return 1.0 / self.center_alpha

    def mixing_ratio(self, control_interval: int) -> float:
        if control_interval <= 0:
            raise ValueError("control_interval must be positive.")
        return float(control_interval / self.mixing_time)

    def update(self, blocks: Sequence[npt.ArrayLike]) -> tuple[FloatArray, FloatArray]:
        arrays = [np.asarray(block, dtype=np.float64) for block in blocks]
        if any(array.size == 0 for array in arrays):
            raise ValueError("blocks must be non-empty.")
        means = [np.asarray(np.mean(array, axis=0), dtype=np.float64) for array in arrays]
        if self.centers is None:
            self.centers = [mean.copy() for mean in means]
        elif len(self.centers) != len(arrays):
            raise ValueError("block count changed after centering observer initialization.")
        else:
            self.centers = [
                center + self.center_alpha * (mean - center)
                for center, mean in zip(self.centers, means, strict=True)
            ]
        widths = []
        center_norms = []
        for array, center in zip(arrays, self.centers, strict=True):
            residual = array - center
            widths.append(self.scale.variance(residual))
            center_norms.append(float(np.linalg.norm(np.asarray(center).reshape(-1))))
        return np.asarray(widths, dtype=np.float64), np.asarray(center_norms, dtype=np.float64)

    def state_dict(self) -> dict[str, object]:
        return {
            "center_alpha": self.center_alpha,
            "centers": None if self.centers is None else [center.tolist() for center in self.centers],
            "scale": type(self.scale).__name__,
        }
