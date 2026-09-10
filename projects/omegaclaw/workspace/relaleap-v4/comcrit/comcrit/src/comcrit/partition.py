"""ModulePartition (R1): named module -> parameter leaves.

Two dual views, one object:
  * gate mappings {leaf_name: scalar} for pytree/named-parameter learners
    (Transformers, MLPs, CAROM operator blocks);
  * flat index masks over a parameter vector (the quadratic fixture,
    or any flattened view).

Dense projector matrices are banned by construction: a projector is an
index mask, applied by fancy indexing or leaf-wise multiplication.
"""
from __future__ import annotations

from typing import Mapping, Sequence

import numpy as np

from .protocols import Action


class ModulePartition:
    def __init__(self, modules: Mapping[str, Sequence[str]] | None = None,
                 index_modules: Mapping[str, np.ndarray] | None = None,
                 all_leaves: Sequence[str] | None = None,
                 dim: int | None = None):
        """Provide `modules` (name -> leaf names, with `all_leaves`) for
        pytree learners, and/or `index_modules` (name -> index array, with
        `dim`) for flat-vector learners. Disjointness is enforced."""
        self.modules = dict(modules or {})
        self.index_modules = {k: np.asarray(v) for k, v in
                              (index_modules or {}).items()}
        self.all_leaves = list(all_leaves or [])
        self.dim = dim
        if self.modules:
            seen: set[str] = set()
            for name, leaves in self.modules.items():
                for lf in leaves:
                    if lf in seen:
                        raise ValueError(f"leaf {lf!r} in two modules")
                    if self.all_leaves and lf not in self.all_leaves:
                        raise ValueError(f"unknown leaf {lf!r} in {name!r}")
                    seen.add(lf)
        if self.index_modules:
            if dim is None:
                raise ValueError("index_modules requires dim")
            cover = np.zeros(dim, dtype=int)
            for idx in self.index_modules.values():
                cover[idx] += 1
            if cover.max() > 1:
                raise ValueError("index modules overlap")

    @property
    def names(self) -> list[str]:
        return list(self.modules or self.index_modules)

    # ---- pytree view -------------------------------------------------
    def gate(self, action: Action | None) -> dict[str, float]:
        """{leaf_name: multiplier}; identity for ordinary."""
        g = {lf: 1.0 for lf in self.all_leaves}
        if action is not None:
            mods, alpha = action
            for m in mods:
                for lf in self.modules[m]:
                    g[lf] = float(alpha)
        return g

    @staticmethod
    def apply_gate(grads: Mapping[str, object],
                   gate: Mapping[str, float]) -> dict:
        """Post-backward, pre-optimizer gradient gating (the R3 helper)."""
        return {k: gate[k] * v for k, v in grads.items()}

    # ---- flat view ---------------------------------------------------
    def gate_vec(self, action: Action | None) -> np.ndarray:
        g = np.ones(self.dim)
        if action is not None:
            mods, alpha = action
            for m in mods:
                g[self.index_modules[m]] = alpha
        return g

    def mask(self, module: str) -> np.ndarray:
        return self.index_modules[module]

    def restrict(self, v: np.ndarray, module: str) -> np.ndarray:
        return v[self.index_modules[module]]
