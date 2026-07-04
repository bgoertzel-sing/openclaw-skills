"""OmegaSim A6 experiment conditions.

Seven controls from ProtomegaTron's 2026-07-01 feedback, ordered from
non-coupled baselines to full delayed thresholded appraisal with prediction.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Dict


@dataclass(frozen=True)
class Condition:
    id: int
    name: str
    description: str
    coupling_mode: str = "none"  # none | linear | logistic
    coupling_gain: float = 1.0
    logistic_slope: float = 2.0
    delay_tau: int = 0
    hysteresis_rho: float = 0.0
    adaptive_thresholds: bool = False
    costly_prediction: bool = False


CONDITIONS: Dict[int, Condition] = {
    1: Condition(1, "no_cross_role_coupling", "Roles evolve only from shared field, noise, and self-state."),
    2: Condition(2, "amplitude_matched_linear_coupling", "Linear cross-role influence scaled to match logistic amplitude.", "linear"),
    3: Condition(3, "same_tick_logistic_coupling", "Sigmoidal bounded appraisal coupling with no delay.", "logistic", delay_tau=0),
    4: Condition(4, "delayed_logistic_coupling", "Sigmoidal bounded appraisal coupling through delayed role state.", "logistic", delay_tau=2),
    5: Condition(5, "delayed_logistic_coupling_with_hysteresis", "Delayed logistic coupling plus action/state hysteresis.", "logistic", delay_tau=2, hysteresis_rho=0.85),
    6: Condition(6, "delayed_logistic_coupling_with_adaptive_thresholds", "Condition 5 plus threshold drift with load, fatigue, success, and risk.", "logistic", delay_tau=2, hysteresis_rho=0.85, adaptive_thresholds=True),
    7: Condition(7, "delayed_logistic_coupling_with_costly_prediction", "Condition 6 plus costly prediction actions and delayed forecast payoff.", "logistic", delay_tau=2, hysteresis_rho=0.85, adaptive_thresholds=True, costly_prediction=True),
}


def get_condition(condition_id: int, **overrides) -> Condition:
    if condition_id not in CONDITIONS:
        raise KeyError(f"unknown A6 condition {condition_id}; valid={sorted(CONDITIONS)}")
    c = CONDITIONS[condition_id]
    return replace(c, **{k: v for k, v in overrides.items() if v is not None})
