"""Sweep grid for OmegaSim A6."""
from __future__ import annotations

SWEEP_GRID = {
    "coupling_slope_k": [0, 0.5, 1, 2, 4, 8, 12],
    "threshold_percentile_theta": [30, 50, 70],
    "delay_tau": [0, 1, 2, 4, 8, 16],
    "memory_rho": [0, 0.3, 0.6, 0.85, 0.95],
    "fatigue_gain": {"none": 0.0, "low": 0.01, "medium": 0.03, "high": 0.08},
    "prediction_cost": {"none": 0.0, "low": 0.01, "medium": 0.03, "high": 0.08},
    "noise": [0, 0.01, 0.03, 0.1],
}


def default_params() -> dict:
    return {
        "coupling_slope_k": 2.0,
        "threshold_percentile_theta": 50,
        "delay_tau": 2,
        "memory_rho": 0.85,
        "fatigue_gain": "medium",
        "prediction_cost": "medium",
        "noise": 0.03,
    }
