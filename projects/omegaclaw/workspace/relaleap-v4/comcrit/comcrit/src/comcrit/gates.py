"""The gate suite. Thresholds are constructor arguments frozen at
instantiation and echoed in every result — never module globals an
experiment can quietly edit. A gate returns (passed, details); it never
raises on failure (fail-closed means *report and stop*, not crash)."""
from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np

from .stats import ValidityCell, spearman


@dataclass(frozen=True)
class ValidityGate:
    """Backbone-validity: rho >= rho_min, e <= e_max inside the declared
    operating region; the no-signal fraction is reported, not penalized."""

    rho_min: float = 0.8
    e_max: float = 0.25

    def check(self, cells: list[ValidityCell], operating: set[tuple]):
        fails = [c for c in cells if (c.horizon, c.alpha) in operating
                 and not (c.rho >= self.rho_min and c.e <= self.e_max)]
        details = {"thresholds": asdict(self), "cells": [asdict(c) for c in cells],
                   "no_signal_frac": {f"h{c.horizon}_a{c.alpha}":
                                      1 - c.n_qualified / max(c.n_total, 1)
                                      for c in cells}}
        return len(fails) == 0, details


@dataclass(frozen=True)
class SynergyGate:
    """Measured cross-curvature u_m' H_A u_n must predict pair-minus-singles.
    The additive comparator is *defined* as this term deleted."""

    rel_err_max_h1: float = 0.10
    spearman_min: float = 0.6

    def check(self, syn_hat, syn_true, horizon: int):
        syn_hat, syn_true = np.asarray(syn_hat), np.asarray(syn_true)
        rel = float(np.median(np.abs(syn_hat - syn_true) /
                              np.maximum(np.abs(syn_true), 1e-300)))
        rho = spearman(syn_hat, syn_true)
        ok = (rel <= self.rel_err_max_h1) if horizon == 1 else \
             (rho >= self.spearman_min)
        return ok, {"median_rel_err": rel, "spearman": rho,
                    "horizon": horizon, "thresholds": asdict(self)}


@dataclass(frozen=True)
class NullGate:
    """In the provably-aligned null family the first-order term is
    nonnegative ANALYTICALLY at every state. A violation is a fixture or
    code defect and halts the stage (fail-closed, hard)."""

    k_sigma_false_benefit: float = 3.0
    false_benefit_frac_max: float = 0.05

    def check(self, min_firstorder_alignment: float,
              tau_true: np.ndarray, floor: float):
        analytic_ok = min_firstorder_alignment >= 0.0
        fb = float(np.mean(np.asarray(tau_true) <
                           -self.k_sigma_false_benefit * floor))
        return (analytic_ok and fb <= self.false_benefit_frac_max), {
            "min_firstorder_alignment": min_firstorder_alignment,
            "false_benefit_frac": fb, "halt_on_analytic_violation":
                not analytic_ok, "thresholds": asdict(self)}


@dataclass(frozen=True)
class ResidualSkillGate:
    """Do-no-harm inside the validity radius; earn-your-keep outside.
    The null model is the theory, not a constant."""

    inside_mse_inflation_max: float = 0.05
    outside_mse_improvement_min: float = 0.20

    def check(self, mse_backbone_inside, mse_combined_inside,
              mse_backbone_outside, mse_combined_outside):
        inside_ok = (mse_combined_inside <=
                     (1 + self.inside_mse_inflation_max) * mse_backbone_inside)
        outside_ok = (mse_combined_outside <=
                      (1 - self.outside_mse_improvement_min)
                      * mse_backbone_outside)
        return inside_ok and outside_ok, {
            "inside_ok": inside_ok, "outside_ok": outside_ok,
            "thresholds": asdict(self)}
