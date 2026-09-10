"""Confusion-graph accumulation: per-state module-level backbone terms
aggregated into an estimate of the CCL confusion structure restricted to
the partition. v0.1 exports a plain dict; consumers are the CGCCT
commutator loss, the HDC footprint edge proposer, and (later) Atomspace
typed links."""
from __future__ import annotations

from collections import defaultdict

import numpy as np


class ConfusionGraph:
    def __init__(self, module_names):
        self.names = list(module_names)
        self._fo = defaultdict(list)      # (m,) -> first-order conflict terms
        self._cc = defaultdict(list)      # (m, n) -> cross-curvature terms

    def add_first_order(self, module: str, value: float):
        self._fo[(module,)].append(float(value))

    def add_cross_curvature(self, m: str, n: str, value: float):
        self._cc[tuple(sorted((m, n)))].append(float(value))

    def export(self) -> dict:
        stat = lambda xs: {"n": len(xs), "median": float(np.median(xs)),
                           "mean_abs": float(np.mean(np.abs(xs))),
                           "frac_negative": float(np.mean(np.array(xs) < 0))}
        return {"modules": self.names,
                "first_order": {m[0]: stat(v) for m, v in self._fo.items()},
                "cross_curvature": {f"{m}|{n}": stat(v)
                                    for (m, n), v in self._cc.items()}}
