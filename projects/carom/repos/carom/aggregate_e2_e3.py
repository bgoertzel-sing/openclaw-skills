#!/usr/bin/env python3
"""Aggregate CAROM E2/E3 arm results from example-level evaluation rows.

The runner has emitted two compatible formats:
  * metrics.rows contains per-example records, with optional cached aggregates;
  * metrics itself is a list of per-example records.

Scientific endpoint values are always recomputed from the per-example records.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from collections import defaultdict
from pathlib import Path
from statistics import mean
from typing import Any, Iterable


ARMS = (
    "e2_full",
    "e2_no_workspace",
    "e2_no_command",
    "e2_no_position",
    "e3_generic_regularized",
)
ABLATIONS = ("e2_no_workspace", "e2_no_command", "e2_no_position")


def example_rows(result: dict[str, Any]) -> list[dict[str, Any]]:
    metrics = result.get("metrics")
    if isinstance(metrics, list):
        rows = metrics
    elif isinstance(metrics, dict) and isinstance(metrics.get("rows"), list):
        rows = metrics["rows"]
    else:
        raise ValueError("result has neither metrics list nor metrics.rows list")
    if not rows:
        raise ValueError("metrics contain no per-example rows")
    return rows


def _finite_mean(values: Iterable[float], label: str) -> float:
    values = [float(v) for v in values]
    if not values or not all(math.isfinite(v) for v in values):
        raise ValueError(f"{label} is empty or non-finite")
    return mean(values)


def summarize_result(result: dict[str, Any]) -> dict[str, Any]:
    rows = example_rows(result)
    required = {
        "slot_accuracy",
        "exact_workspace",
        "revisits",
        "terminal_trapping",
        "integrated_activity_mass",
        "integrated_workspace_update_norm",
        "integrated_exposure",
    }
    missing = required - set(rows[0])
    if missing:
        raise ValueError(f"per-example rows missing keys: {sorted(missing)}")

    exposure_totals = [sum(map(float, row["integrated_exposure"])) for row in rows]
    return {
        "arm": result["arm"],
        "seed": int(result["seed"]),
        "n_examples": len(rows),
        "slot_accuracy": _finite_mean((r["slot_accuracy"] for r in rows), "slot_accuracy"),
        "exact_workspace": _finite_mean(
            (float(bool(r["exact_workspace"])) for r in rows), "exact_workspace"
        ),
        "revisit_fraction": _finite_mean(
            (float(r["revisits"] > 0) for r in rows), "revisit_fraction"
        ),
        "mean_revisit_count": _finite_mean(
            (r["revisits"] for r in rows), "mean_revisit_count"
        ),
        "terminal_trapping_fraction": _finite_mean(
            (float(bool(r["terminal_trapping"])) for r in rows),
            "terminal_trapping_fraction",
        ),
        "integrated_activity_mass": _finite_mean(
            (r["integrated_activity_mass"] for r in rows), "integrated_activity_mass"
        ),
        "total_integrated_exposure": _finite_mean(
            exposure_totals, "total_integrated_exposure"
        ),
        "workspace_update_norm": _finite_mean(
            (r["integrated_workspace_update_norm"] for r in rows),
            "workspace_update_norm",
        ),
    }


def load_results(input_dir: Path) -> list[dict[str, Any]]:
    results = []
    for path in sorted(input_dir.glob("*_seed*.json")):
        with path.open() as handle:
            result = json.load(handle)
        summary = summarize_result(result)
        summary["source"] = path.name
        results.append(summary)
    expected = {(arm, seed) for arm in ARMS for seed in (7, 17, 27, 37, 47)}
    observed = {(row["arm"], row["seed"]) for row in results}
    if observed != expected:
        raise ValueError(
            f"expected 25 arm/seed results; missing={sorted(expected-observed)}, "
            f"extra={sorted(observed-expected)}"
        )
    return results


def aggregate(results: list[dict[str, Any]]) -> dict[str, Any]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_key = {}
    for row in results:
        grouped[row["arm"]].append(row)
        by_key[(row["arm"], row["seed"])] = row
    metric_names = (
        "slot_accuracy",
        "exact_workspace",
        "revisit_fraction",
        "mean_revisit_count",
        "terminal_trapping_fraction",
        "integrated_activity_mass",
        "total_integrated_exposure",
        "workspace_update_norm",
    )
    arms = {
        arm: {metric: mean(row[metric] for row in grouped[arm]) for metric in metric_names}
        for arm in ARMS
    }

    e2_differences = {}
    e2_pass = True
    for ablation in ABLATIONS:
        paired = [
            by_key[("e2_full", seed)]["slot_accuracy"]
            - by_key[(ablation, seed)]["slot_accuracy"]
            for seed in (7, 17, 27, 37, 47)
        ]
        entry = {
            "mean_slot_accuracy_difference": mean(paired),
            "nonnegative_seed_count": sum(value >= 0 for value in paired),
            "paired_seed_differences": paired,
            "pass": mean(paired) >= 0.010 and sum(value >= 0 for value in paired) >= 4,
        }
        e2_differences[ablation] = entry
        e2_pass &= entry["pass"]

    full = arms["e2_full"]
    e3 = arms["e3_generic_regularized"]
    e3_checks = {
        "slot_accuracy_loss_at_most_0.010": e3["slot_accuracy"] >= full["slot_accuracy"] - 0.010,
        "terminal_trapping_no_greater": (
            e3["terminal_trapping_fraction"] <= full["terminal_trapping_fraction"]
        ),
        "revisit_fraction_no_greater": e3["revisit_fraction"] <= full["revisit_fraction"],
        "activity_mass_at_most_1.10x": (
            e3["integrated_activity_mass"] <= 1.10 * full["integrated_activity_mass"]
        ),
    }
    e3_pass = all(e3_checks.values())
    return {
        "threshold_provenance": (
            "experiments/20260724T194500Z-e2-e3-gpu-r1/RUN.md, "
            "frozen before r2 provisioning"
        ),
        "arm_means": arms,
        "e2_feature_gate": {"contrasts": e2_differences, "pass": e2_pass},
        "e3_safety_trajectory_gate": {
            "slot_accuracy_difference_vs_e2_full": e3["slot_accuracy"]
            - full["slot_accuracy"],
            "checks": e3_checks,
            "pass": e3_pass,
        },
        "joint_gate_pass": e2_pass and e3_pass,
    }


def write_outputs(output_dir: Path, results: list[dict[str, Any]], report: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / "e2_e3_aggregate.json").open("w") as handle:
        json.dump({"per_seed": results, **report}, handle, indent=2, sort_keys=True)
        handle.write("\n")
    fields = [key for key in results[0] if key != "source"] + ["source"]
    with (output_dir / "e2_e3_per_seed.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)
    with (output_dir / "e2_e3_results.md").open("w") as handle:
        handle.write("| arm | slot accuracy | exact workspace | revisit frac. | terminal trap frac. | activity mass | exposure |\n")
        handle.write("|---|---:|---:|---:|---:|---:|---:|\n")
        for arm in ARMS:
            row = report["arm_means"][arm]
            handle.write(
                f"| {arm} | {row['slot_accuracy']:.4f} | {row['exact_workspace']:.4f} "
                f"| {row['revisit_fraction']:.4f} | {row['terminal_trapping_fraction']:.4f} "
                f"| {row['integrated_activity_mass']:.4f} | "
                f"{row['total_integrated_exposure']:.4f} |\n"
            )
        handle.write(f"\nJoint frozen gate: **{'PASS' if report['joint_gate_pass'] else 'FAIL'}**.\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    results = load_results(args.input_dir)
    report = aggregate(results)
    write_outputs(args.output_dir, results, report)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
