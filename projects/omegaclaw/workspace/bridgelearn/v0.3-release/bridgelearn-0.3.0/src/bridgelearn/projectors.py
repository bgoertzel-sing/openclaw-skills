"""Transition projectors.

A covariance path specifies only marginal variances.  A projector chooses the
cross-time coupling: how much of the old stochastic state is retained and how
much fresh innovation is added.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

import numpy as np

from .types import FloatArray, GaussianTransition, broadcast_array


class TransitionProjector(Protocol):
    def project(
        self,
        *,
        current_variance: FloatArray,
        target_variance: FloatArray,
        reference: GaussianTransition,
    ) -> GaussianTransition:
        ...


@dataclass(frozen=True, slots=True)
class GaussianKLProjector:
    r"""One-step diagonal Gaussian Schrödinger/KL projection.

    For each block this minimizes

    .. math::

        E_{z\sim N(0,V)}\, KL\left[N(az,r)\,\|\,N(a_0z,r_0)\right]

    subject to ``W = a**2 * V + r``.  It therefore resolves the transition
    ambiguity while making the smallest path-space change to the reference
    local dynamics.
    """

    reference_innovation_floor: float = 1e-12
    contraction_bounds: tuple[float, float] | None = None

    def __post_init__(self) -> None:
        if self.reference_innovation_floor <= 0.0:
            raise ValueError("reference_innovation_floor must be positive.")
        if self.contraction_bounds is not None:
            low, high = self.contraction_bounds
            if not np.isfinite(low) or not np.isfinite(high) or low > high:
                raise ValueError("invalid contraction_bounds.")

    def project(
        self,
        *,
        current_variance: FloatArray,
        target_variance: FloatArray,
        reference: GaussianTransition,
    ) -> GaussianTransition:
        size = reference.size
        current = broadcast_array(current_variance, size, name="current_variance")
        target = broadcast_array(target_variance, size, name="target_variance")
        if np.any(current < 0.0) or np.any(target < 0.0):
            raise ValueError("current and target variances must be non-negative.")

        a0 = reference.contraction
        r0 = np.maximum(reference.innovation, self.reference_innovation_floor)
        discriminant = r0**2 + 4.0 * a0**2 * current * target
        denominator = r0 + np.sqrt(np.maximum(discriminant, 0.0))
        with np.errstate(divide="ignore", invalid="ignore"):
            contraction = np.where(
                denominator > 0.0,
                2.0 * a0 * target / denominator,
                0.0,
            )

        # Exact marginal feasibility requires |a| <= sqrt(W / V).
        max_abs = np.full(size, np.inf, dtype=np.float64)
        positive_current = current > 0.0
        max_abs[positive_current] = np.sqrt(
            np.maximum(target[positive_current] / current[positive_current], 0.0)
        )
        contraction = np.clip(contraction, -max_abs, max_abs)

        if self.contraction_bounds is not None:
            low, high = self.contraction_bounds
            feasible_low = np.maximum(low, -max_abs)
            feasible_high = np.minimum(high, max_abs)
            if np.any(feasible_low > feasible_high):
                raise ValueError(
                    "contraction_bounds exclude every exact transition for at least one block."
                )
            # The scalar objective is strictly convex on the exact-feasibility
            # interval, so clipping its unconstrained minimizer is exact.
            contraction = np.minimum(np.maximum(contraction, feasible_low), feasible_high)

        innovation = target - contraction**2 * current
        innovation = np.maximum(innovation, 0.0)
        return GaussianTransition(contraction=contraction, innovation=innovation)

    def objective(
        self,
        *,
        current_variance: FloatArray,
        candidate: GaussianTransition,
        reference: GaussianTransition,
    ) -> FloatArray:
        """Return the blockwise expected transition KL objective."""

        size = reference.size
        current = broadcast_array(current_variance, size, name="current_variance")
        if candidate.size != size:
            raise ValueError("candidate and reference sizes do not match.")
        r = np.maximum(candidate.innovation, self.reference_innovation_floor)
        r0 = np.maximum(reference.innovation, self.reference_innovation_floor)
        return 0.5 * (
            np.log(r0 / r)
            + (
                r
                + (candidate.contraction - reference.contraction) ** 2 * current
            )
            / r0
            - 1.0
        )


@dataclass(frozen=True, slots=True)
class PreserveContractionProjector:
    """Keep the reference contraction and place all mismatch in innovation.

    This is useful when geometry or solver stability fixes the deterministic
    step and only batch size / explicit noise may be changed.
    """

    def project(
        self,
        *,
        current_variance: FloatArray,
        target_variance: FloatArray,
        reference: GaussianTransition,
    ) -> GaussianTransition:
        size = reference.size
        current = broadcast_array(current_variance, size, name="current_variance")
        target = broadcast_array(target_variance, size, name="target_variance")
        innovation = target - reference.contraction**2 * current
        return GaussianTransition(
            contraction=reference.contraction,
            innovation=np.maximum(innovation, 0.0),
        )
