#!/usr/bin/env python3
"""Basic smoke tests for OmegaSim A6."""
from __future__ import annotations

import numpy as np

from analysis import analyze_result, build_observable, residualize
from conditions import CONDITIONS
from omegasim_a6 import ACTIONS, FIELD_DIMS, ROLES, STATE_VARS, SimConfig, run_simulation


def test_simulation_shapes_and_bounds():
    result = run_simulation(SimConfig(condition_id=5, timesteps=40, seed=123, noise=0.01))
    assert result["states"].shape == (40, len(ROLES), len(STATE_VARS))
    assert result["fields"].shape == (40, len(FIELD_DIMS))
    assert result["action_counts"].shape == (40, len(ACTIONS))
    assert result["appraisals"].shape[-1] == 8
    assert np.all(result["fields"] >= 0) and np.all(result["fields"] <= 1)
    assert np.all(result["states"] >= 0) and np.all(result["states"] <= 1)


def test_actions_are_valid():
    result = run_simulation(SimConfig(condition_id=3, timesteps=25, seed=99))
    valid = set(ACTIONS)
    assert all(a in valid for row in result["actions"] for a in row)
    assert result["actions_idx"].min() >= 0
    assert result["actions_idx"].max() < len(ACTIONS)


def test_residualization_and_analysis():
    result = run_simulation(SimConfig(condition_id=6, timesteps=60, seed=5))
    y = build_observable(result)
    r = residualize(y, result["action_counts"])
    assert y.shape == r.shape
    assert np.all(np.isfinite(r))
    metrics = analyze_result(result)
    assert metrics["latent_shape"] == [60, len(ROLES), len(STATE_VARS)]
    assert metrics["field_minmax"][0] >= 0
    assert metrics["field_minmax"][1] <= 1


def test_conditions_one_and_five_differ():
    r1 = run_simulation(SimConfig(condition_id=1, timesteps=80, seed=44, noise=0.01))
    r5 = run_simulation(SimConfig(condition_id=5, timesteps=80, seed=44, noise=0.01))
    diff = float(np.mean(np.abs(r1["fields"] - r5["fields"])))
    assert diff > 1e-3, f"condition dynamics too similar: {diff}"


def test_condition_registry():
    assert sorted(CONDITIONS) == list(range(1, 8))


if __name__ == "__main__":
    tests = [
        test_simulation_shapes_and_bounds,
        test_actions_are_valid,
        test_residualization_and_analysis,
        test_conditions_one_and_five_differ,
        test_condition_registry,
    ]
    for t in tests:
        t()
        print(f"PASS {t.__name__}")
