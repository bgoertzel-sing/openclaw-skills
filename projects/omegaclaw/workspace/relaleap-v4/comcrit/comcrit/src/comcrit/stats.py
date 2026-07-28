"""Measured statistics. The three functions that carry the protocol's
hard-won lessons are `noise_floor` (floors are measured, never assumed),
`effect_size_precheck` (the 5-sigma rule that caught the sandbox's
0.1x-floor synergy plant — the V2 tiny-utility regime, live), and
`validity_map` (the honest replacement for declared-ordering audits).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence

import numpy as np


def spearman(x, y) -> float:
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 3 or np.std(x) == 0 or np.std(y) == 0:
        return float("nan")
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    return float(np.corrcoef(rx, ry)[0, 1])


def noise_floor(tau_sampler: Callable[[int], float],
                n_replicates: int = 64) -> float:
    """sigma_noise: std of the paired estimand over resampled CRN
    continuations at one probe state. `tau_sampler(seed)` runs one CRN
    pair with continuation noise drawn from `seed` and returns tau.
    Protocol default: >= 64 replicates (floor SE ~ sigma/sqrt(128)).
    Call at >= 20 probe states and take the median."""
    taus = [tau_sampler(s) for s in range(n_replicates)]
    return float(np.std(taus))


@dataclass
class PrecheckResult:
    passed: bool
    ratio: float                 # median|tau| / floor
    floor: float
    median_abs_effect: float
    iterations_used: int


def effect_size_precheck(measure_effects: Callable[[], np.ndarray],
                         floor: float,
                         strengthen: Callable[[], None] | None = None,
                         min_ratio: float = 5.0,
                         max_iterations: int = 3) -> PrecheckResult:
    """The 5-sigma rule with the bounded strengthen-and-retry loop.

    `measure_effects()` returns |tau| over probe states x non-ordinary
    actions at the operating (h, alpha); `strengthen()` scales the planted
    conflict (protocol: displacement x1.5, at most 3 iterations, and NEVER
    lower the noise). Refusing to proceed on sub-5-sigma effects is the
    single rule that would have prevented the V2 tiny-utility regime."""
    it = 0
    while True:
        med = float(np.median(np.abs(measure_effects())))
        ratio = med / floor if floor > 0 else np.inf
        if ratio >= min_ratio:
            return PrecheckResult(True, ratio, floor, med, it)
        it += 1
        if strengthen is None or it > max_iterations:
            return PrecheckResult(False, ratio, floor, med, it - 1)
        strengthen()


def margin_qualify(tau_true: np.ndarray, floor: float,
                   k_sigma: float = 3.0) -> np.ndarray:
    """Boolean mask of states/actions whose effect clears k*sigma. States
    below the floor are *no-signal*, reported as a fraction — never counted
    as ordering violations (the V3 audit repair)."""
    return np.abs(np.asarray(tau_true)) >= k_sigma * floor


@dataclass
class ValidityCell:
    horizon: int
    alpha: float
    rho: float                   # Spearman(backbone, truth), qualified states
    e: float                     # median relative error, floor-clipped denom
    n_qualified: int
    n_total: int
    inside: bool                 # rho >= rho_min and e <= e_max


def validity_map(records, floor_by_h, rho_min: float = 0.8,
                 e_max: float = 0.25, k_sigma: float = 3.0
                 ) -> list[ValidityCell]:
    """records: iterable of (h, alpha, tau_true, tau_hat) arrays grouped by
    cell. Returns the (h, alpha) validity-radius map — the measured trust
    region of the expansion, replacing declared-ordering audits."""
    cells = []
    for (h, alpha, tr, ht) in records:
        tr, ht = np.asarray(tr, float), np.asarray(ht, float)
        fl = floor_by_h[h]
        q = margin_qualify(tr, fl, k_sigma)
        if q.sum() >= 3:
            rho = spearman(ht[q], tr[q])
            e = float(np.median(np.abs(ht[q] - tr[q]) /
                                np.maximum(np.abs(tr[q]), k_sigma * fl)))
        else:
            rho, e = float("nan"), float("nan")
        cells.append(ValidityCell(h, alpha, rho, e, int(q.sum()), len(tr),
                                  bool(rho >= rho_min and e <= e_max)))
    return cells
