from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from typing import Iterable, Sequence

import numpy as np


OUTCOMES: tuple[tuple[int, int], ...] = ((-1, -1), (-1, 1), (1, -1), (1, 1))


def empirical_joint(pairs: Sequence[tuple[int, int]], alpha: float = 0.5) -> np.ndarray:
    counts = np.full(4, alpha, dtype=np.float64)
    index = {outcome: i for i, outcome in enumerate(OUTCOMES)}
    for pair in pairs:
        if pair not in index:
            raise ValueError(f"Expected a +/-1 pair, got {pair}")
        counts[index[pair]] += 1.0
    return counts / counts.sum()


def total_variation(left: np.ndarray, right: np.ndarray) -> float:
    if left.shape != right.shape:
        raise ValueError("Distributions must have the same shape")
    return float(0.5 * np.abs(left - right).sum())


def jensen_shannon_bits(left: np.ndarray, right: np.ndarray) -> float:
    midpoint = 0.5 * (left + right)

    def kl_bits(p: np.ndarray, q: np.ndarray) -> float:
        mask = p > 0
        return float(np.sum(p[mask] * np.log2(p[mask] / q[mask])))

    return 0.5 * kl_bits(left, midpoint) + 0.5 * kl_bits(right, midpoint)


def s_odd(values: Sequence[float]) -> float:
    """Maximum signed sum with an odd number of minus signs."""
    if not values:
        raise ValueError("values must not be empty")
    best = -math.inf
    for signs in itertools.product((-1.0, 1.0), repeat=len(values)):
        minus_count = sum(sign < 0 for sign in signs)
        if minus_count % 2 == 1:
            best = max(best, sum(sign * value for sign, value in zip(signs, values)))
    return float(best)


@dataclass(frozen=True)
class CbDResult:
    correlations: tuple[float, float, float, float]
    content_means: tuple[tuple[float, float], ...]
    s_odd_value: float
    inconsistent_connectedness: float
    noncontextual_bound: float
    raw_excess: float
    contextuality_measure: float


def cbd_cyclic4(context_pairs: Sequence[Sequence[tuple[int, int]]]) -> CbDResult:
    """Contextuality-by-Default criterion for a rank-4 cyclic binary system.

    Context order must be (q1,q2), (q2,q3), (q3,q4), (q4,q1).
    Each observed value is coded +/-1.
    """
    if len(context_pairs) != 4:
        raise ValueError("A cyclic-4 system requires exactly four contexts")
    for pairs in context_pairs:
        if not pairs:
            raise ValueError("Every context must contain at least one observation")

    correlations = tuple(float(np.mean([a * b for a, b in pairs])) for pairs in context_pairs)
    means = [(float(np.mean([a for a, _ in pairs])), float(np.mean([b for _, b in pairs]))) for pairs in context_pairs]

    # q1 appears as first in context 0 and second in context 3; similarly around the cycle.
    content_means = (
        (means[0][0], means[3][1]),
        (means[0][1], means[1][0]),
        (means[1][1], means[2][0]),
        (means[2][1], means[3][0]),
    )
    icc = float(sum(abs(left - right) for left, right in content_means))
    odd = s_odd(correlations)
    bound = 2.0 + icc
    raw_excess = max(0.0, odd - bound)
    return CbDResult(
        correlations=correlations,  # type: ignore[arg-type]
        content_means=content_means,
        s_odd_value=odd,
        inconsistent_connectedness=icc,
        noncontextual_bound=bound,
        raw_excess=raw_excess,
        contextuality_measure=0.5 * raw_excess,
    )


def bootstrap_interval(values: Sequence[float], level: float = 0.95) -> tuple[float, float]:
    if not values:
        return (math.nan, math.nan)
    tail = (1.0 - level) / 2.0
    return (float(np.quantile(values, tail)), float(np.quantile(values, 1.0 - tail)))
