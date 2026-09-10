"""Momentum companion dynamics, stability geometry, and Lyapunov diagnostics.

The heavy-ball/first-moment local model is

    z[k+1] = c1 * z[k] + c2 * z[k-1] + eps[k+1],

with ``c1 = 1 + mu - eta*h`` and ``c2 = -mu``.  The public helpers in
this module deliberately stay two-dimensional and dependency-free: every
calculation is either closed form or a 4-by-4 linear solve.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
import numpy.typing as npt

FloatArray = npt.NDArray[np.float64]


def companion_matrix(c1: float, c2: float) -> FloatArray:
    """Return the 2x2 companion matrix ``[[c1, c2], [1, 0]]``."""

    values = np.asarray([c1, c2], dtype=np.float64)
    if not np.all(np.isfinite(values)):
        raise ValueError("c1 and c2 must be finite.")
    return np.asarray([[float(c1), float(c2)], [1.0, 0.0]], dtype=np.float64)


def companion_roots(c1: float, c2: float) -> FloatArray:
    """Return roots of ``s**2 - c1*s - c2``."""

    return np.roots([1.0, -float(c1), -float(c2)]).astype(np.complex128)


def spectral_radius(c1: float, c2: float) -> float:
    """Return the spectral radius of the companion matrix."""

    return float(np.max(np.abs(companion_roots(c1, c2))))


def jury_margins(c1: float, c2: float) -> tuple[float, float, float]:
    """Return signed margins to the three Schur/Jury triangle edges.

    Stability is equivalent to all three values being positive:

    ``1 - c1 - c2 > 0``, ``1 + c1 - c2 > 0``, and ``1 + c2 > 0``.

    This is the same triangle as
    ``c1 + c2 < 1, c2 - c1 < 1, |c2| < 1``; the omitted upper bound
    ``c2 < 1`` follows from the first two inequalities but is checked by
    :func:`inside_stability_triangle` for numerical clarity.
    """

    return (1.0 - c1 - c2, 1.0 + c1 - c2, 1.0 + c2)


def inside_stability_triangle(c1: float, c2: float, *, margin: float = 0.0) -> bool:
    """Return whether ``(c1, c2)`` lies in a margin-shrunk stability triangle."""

    if margin < 0.0 or margin >= 1.0:
        raise ValueError("margin must lie in [0, 1).")
    first, second, third = jury_margins(float(c1), float(c2))
    return bool(
        first > margin
        and second > margin
        and third > margin
        and 1.0 - float(c2) > margin
    )


def damping_regime(c1: float, c2: float, *, tolerance: float = 1e-12) -> str:
    """Return ``'overdamped'``, ``'critical'``, or ``'underdamped'``."""

    discriminant = float(c1) ** 2 + 4.0 * float(c2)
    if discriminant > tolerance:
        return "overdamped"
    if discriminant < -tolerance:
        return "underdamped"
    return "critical"


def momentum_coefficients(step_size: float, momentum: float, curvature: float) -> tuple[float, float]:
    """Map heavy-ball controls to companion coefficients."""

    eta = float(step_size)
    mu = float(momentum)
    h = float(curvature)
    if eta < 0.0 or mu < 0.0 or mu >= 1.0 or h < 0.0:
        raise ValueError("require eta>=0, 0<=momentum<1, and curvature>=0.")
    return 1.0 + mu - eta * h, -mu


def edge_margin(step_size: float, momentum: float, curvature: float, *, safety_offset: float = 0.0) -> float:
    """Return margin to the momentum edge ``eta*h < 2*(1+mu)-offset``."""

    if safety_offset < 0.0:
        raise ValueError("safety_offset must be non-negative.")
    return 2.0 * (1.0 + float(momentum)) - safety_offset - float(step_size) * float(curvature)


def underdamped_contraction_floor(momentum: float) -> float:
    """Return the pole-radius floor ``sqrt(mu)`` in the underdamped regime."""

    mu = float(momentum)
    if mu < 0.0 or mu >= 1.0:
        raise ValueError("momentum must lie in [0, 1).")
    return float(np.sqrt(mu))


def lyapunov_metric(
    c1: float,
    c2: float,
    *,
    rho_bar: float | None = None,
    q: npt.ArrayLike | None = None,
    regularization: float = 1e-12,
) -> tuple[FloatArray, float, float]:
    """Solve a Lyapunov-adapted metric for one companion matrix.

    The returned ``P`` solves

    ``rho_bar**2 * P - A.T @ P @ A = Q``.

    ``rho_bar`` must exceed the spectral radius and remain below one.  The
    function also returns ``rho_bar`` and ``cond(P)``.  Near a repeated root,
    the latter exposes non-normal transient amplification.
    """

    a = companion_matrix(c1, c2)
    rho = spectral_radius(c1, c2)
    if rho >= 1.0:
        raise ValueError("the companion matrix must be Schur stable.")
    if rho_bar is None:
        rho_bar = min(0.999, rho + max(0.02, 0.25 * (1.0 - rho)))
    rho_bar = float(rho_bar)
    if not rho < rho_bar < 1.0:
        raise ValueError("rho_bar must satisfy spectral_radius < rho_bar < 1.")
    q_matrix = np.eye(2, dtype=np.float64) if q is None else np.asarray(q, dtype=np.float64)
    if q_matrix.shape != (2, 2):
        raise ValueError("q must be a 2x2 matrix.")
    q_matrix = 0.5 * (q_matrix + q_matrix.T)
    eigenvalues = np.linalg.eigvalsh(q_matrix)
    if np.min(eigenvalues) <= 0.0:
        raise ValueError("q must be positive definite.")

    # vec(A.T P A) = (A.T kron A.T) vec(P), using column-major vec.
    coefficient = rho_bar**2 * np.eye(4) - np.kron(a.T, a.T)
    rhs = q_matrix.reshape(-1, order="F")
    try:
        vector = np.linalg.solve(coefficient, rhs)
    except np.linalg.LinAlgError:
        vector = np.linalg.solve(coefficient + regularization * np.eye(4), rhs)
    p = vector.reshape((2, 2), order="F")
    p = 0.5 * (p + p.T)
    minimum = float(np.min(np.linalg.eigvalsh(p)))
    if minimum <= 0.0:
        p = p + (abs(minimum) + regularization) * np.eye(2)
    condition = float(np.linalg.cond(p))
    return p, rho_bar, condition


def covariance_norm(error: npt.ArrayLike, metric: npt.ArrayLike) -> float:
    """Return ``||P^(1/2) E P^(1/2)||_F`` for symmetric covariance error."""

    e = np.asarray(error, dtype=np.float64)
    p = np.asarray(metric, dtype=np.float64)
    if e.shape != (2, 2) or p.shape != (2, 2):
        raise ValueError("error and metric must be 2x2 matrices.")
    eigenvalues, eigenvectors = np.linalg.eigh(0.5 * (p + p.T))
    if np.min(eigenvalues) <= 0.0:
        raise ValueError("metric must be positive definite.")
    root = (eigenvectors * np.sqrt(eigenvalues)) @ eigenvectors.T
    transformed = root @ e @ root
    return float(np.linalg.norm(transformed, ord="fro"))


def verify_common_lyapunov(
    coefficients: Iterable[tuple[float, float]],
    metric: npt.ArrayLike,
    *,
    rho_bar: float,
    tolerance: float = 1e-10,
) -> bool:
    """Check a supplied common Lyapunov metric over a finite coefficient grid."""

    p = np.asarray(metric, dtype=np.float64)
    if p.shape != (2, 2):
        raise ValueError("metric must be 2x2.")
    for c1, c2 in coefficients:
        a = companion_matrix(c1, c2)
        residual = rho_bar**2 * p - a.T @ p @ a
        if float(np.min(np.linalg.eigvalsh(0.5 * (residual + residual.T)))) <= tolerance:
            return False
    return True


@dataclass(frozen=True, slots=True)
class CompanionDiagnostics:
    """Stability and transient-amplification diagnostics for one block."""

    c1: float
    c2: float
    spectral_radius: float
    regime: str
    jury_margins: tuple[float, float, float]
    rho_bar: float
    lyapunov_condition: float
    edge_margin: float

    @classmethod
    def from_controls(
        cls,
        *,
        step_size: float,
        momentum: float,
        curvature: float,
        safety_offset: float = 0.0,
        rho_bar: float | None = None,
    ) -> "CompanionDiagnostics":
        c1, c2 = momentum_coefficients(step_size, momentum, curvature)
        rho = spectral_radius(c1, c2)
        if rho < 1.0:
            _p, selected_rho, condition = lyapunov_metric(c1, c2, rho_bar=rho_bar)
        else:
            selected_rho = float("nan")
            condition = float("inf")
        return cls(
            c1=c1,
            c2=c2,
            spectral_radius=rho,
            regime=damping_regime(c1, c2),
            jury_margins=jury_margins(c1, c2),
            rho_bar=selected_rho,
            lyapunov_condition=condition,
            edge_margin=edge_margin(
                step_size, momentum, curvature, safety_offset=safety_offset
            ),
        )


@dataclass(frozen=True, slots=True)
class CompanionSmallGainReport:
    """Conditional ISS bound in a Lyapunov-adapted covariance norm."""

    rho_bar: float
    disturbance_lipschitz: float
    disturbance_bound: float
    lyapunov_condition: float
    condition_satisfied: bool
    asymptotic_bound: float
    recommended_matrix_slew: float


def companion_small_gain_bound(
    c1: float,
    c2: float,
    *,
    disturbance_lipschitz: float,
    disturbance_bound: float,
    rho_bar: float | None = None,
    slew_fraction: float = 0.25,
) -> CompanionSmallGainReport:
    """Evaluate ``rho_bar**2 + L_P < 1`` and its conditional ISS bound.

    The returned Euclidean bound includes ``sqrt(cond(P))`` to expose the
    non-normal transient-amplification penalty.  ``recommended_matrix_slew`` is
    a conservative slowly-varying-plant rate proportional to ``1-rho_bar``;
    the same rate can be used as an identification-bandwidth contract.
    """

    if disturbance_lipschitz < 0.0 or disturbance_bound < 0.0:
        raise ValueError("disturbance terms must be non-negative.")
    if slew_fraction <= 0.0:
        raise ValueError("slew_fraction must be positive.")
    _metric, selected_rho, condition = lyapunov_metric(c1, c2, rho_bar=rho_bar)
    denominator = 1.0 - selected_rho**2 - disturbance_lipschitz
    satisfied = denominator > 0.0
    bound = (
        np.sqrt(condition) * disturbance_bound / denominator
        if satisfied
        else float("inf")
    )
    return CompanionSmallGainReport(
        rho_bar=selected_rho,
        disturbance_lipschitz=float(disturbance_lipschitz),
        disturbance_bound=float(disturbance_bound),
        lyapunov_condition=condition,
        condition_satisfied=satisfied,
        asymptotic_bound=float(bound),
        recommended_matrix_slew=float(slew_fraction * (1.0 - selected_rho)),
    )
