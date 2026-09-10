#!/usr/bin/env python3
"""Preregistered same-path calibration for the frozen OmegaSim CLA proxy."""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path
import random

from chaoslang.benchmarks.attractors import lorenz96, mackey_glass
from scripts.run_cla_detector import FEATURES, evaluate_trace

SEEDS = (211, 223, 227, 229, 233)
N_SAMPLES = 1024


def _roles8_rows(points):
    names = FEATURES["roles8"]
    rows = []
    for point in points:
        if len(point) != len(names) or not all(math.isfinite(value) for value in point):
            raise ValueError("benchmark point is not a finite roles8 vector")
        rows.append(dict(zip(names, map(float, point))))
    if len(rows) != N_SAMPLES:
        raise ValueError(f"expected {N_SAMPLES} rows, got {len(rows)}")
    return rows


def _mackey_glass_points(index):
    lag = 17
    embedding = 8
    needed = N_SAMPLES + lag * (embedding - 1)
    raw = mackey_glass(
        steps=needed * 10,
        discard=5000,
        dt=0.1,
        initial=0.498 + 0.001 * index,
        tau=170,
        beta=0.2,
        gamma=0.1,
        n=10.0,
    )
    sampled = raw[::10]
    return tuple(
        tuple(sampled[t - lag * axis] for axis in range(embedding))
        for t in range(lag * (embedding - 1), needed)
    )


def _lorenz96_points(index):
    initial = [8.0] * 8
    initial[index] += 0.008 + 0.001 * index
    raw = lorenz96(
        steps=N_SAMPLES * 5,
        discard=5000,
        dt=0.01,
        initial=tuple(initial),
        F=8.0,
    )
    return raw[::5]


def _joint_shuffle(points, seed):
    shuffled = list(points)
    random.Random(seed * 1000 + 17).shuffle(shuffled)
    return tuple(shuffled)


def main():
    output = Path(__file__).with_name("artifacts") / "results.json"
    rows = []
    summaries = []
    generators = {
        "mackey_glass": _mackey_glass_points,
        "lorenz96": _lorenz96_points,
    }
    for system, generator in generators.items():
        wins = 0
        for index, seed in enumerate(SEEDS):
            points = generator(index)
            metrics_by_control = {}
            for control, trace in (
                ("ordered", points),
                ("joint_time_shuffle", _joint_shuffle(points, seed)),
            ):
                metrics = evaluate_trace(
                    _roles8_rows(trace),
                    stratum="roles8",
                    seed=seed,
                    surrogates=5,
                )
                metrics.update({"system": system, "replicate": index, "seed": seed, "control": control})
                if not all(
                    math.isfinite(metrics[key])
                    for key in (
                        "compression_margin_proxy_bits",
                        "heldout_loss_bits_per_symbol",
                        "heldout_advantage_bits_per_symbol",
                    )
                ):
                    raise ValueError("nonfinite detector metric")
                rows.append(metrics)
                metrics_by_control[control] = metrics
            ordered = metrics_by_control["ordered"]
            shuffled = metrics_by_control["joint_time_shuffle"]
            win = (
                ordered["detector_positive"]
                and ordered["compression_margin_proxy_bits"]
                > shuffled["compression_margin_proxy_bits"]
                and ordered["heldout_loss_bits_per_symbol"]
                < shuffled["heldout_loss_bits_per_symbol"]
            )
            wins += int(win)
            ordered["matched_control_win"] = win
        summaries.append({"system": system, "wins": wins, "required_wins": 4, "passed": wins >= 4})

    passed = len(summaries) == 2 and all(item["passed"] for item in summaries)
    payload = {
        "schema": "omegasim.cla_same_path_external_calibration.v1",
        "config": {"seeds": SEEDS, "samples": N_SAMPLES, "stratum": "roles8", "surrogates": 5},
        "summaries": summaries,
        "rows": rows,
        "passed": passed,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    with output.with_suffix(".csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"output": str(output), "passed": passed, "summaries": summaries}, sort_keys=True))


if __name__ == "__main__":
    main()
