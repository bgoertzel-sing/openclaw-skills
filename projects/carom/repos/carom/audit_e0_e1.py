#!/usr/bin/env python3
"""Recompute complete E0/E1 trajectory/exposure aggregates from raw rows."""
import argparse
import glob
import json
import math
import statistics
from collections import defaultdict
from pathlib import Path


METRICS = (
    "integrated_activity_mass", "mean_activity_mass", "overlap_fraction",
    "mean_active_modes", "skips", "reversals", "revisits",
    "terminal_trapping", "integrated_workspace_update_norm",
)


def mean(xs):
    return statistics.fmean(xs)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--artifacts", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args()
    files = sorted(glob.glob(str(Path(args.artifacts) / "*_seed*.json")))
    arms = defaultdict(list)
    finite = True
    for filename in files:
        result = json.loads(Path(filename).read_text())
        rows = result["rows"]
        by_depth = {}
        for depth in sorted({r["depth"] for r in rows}):
            subset = [r for r in rows if r["depth"] == depth]
            by_depth[str(depth)] = {
                "n": len(subset),
                "slot_accuracy": mean(r["slot_accuracy"] for r in subset),
                **{k: mean(float(r[k]) for r in subset) for k in METRICS},
            }
        aggregate = {k: mean(float(r[k]) for r in rows) for k in METRICS}
        finite &= all(math.isfinite(v) for v in aggregate.values())
        arms[result["arm"]].append({
            "seed": result["seed"],
            "slot_accuracy": result["slot_accuracy"],
            "exact_workspace_accuracy": result["exact_workspace_accuracy"],
            "deterministic_repeat_match":
                result["deterministic_repeat_match"],
            "aggregate": aggregate,
            "by_depth": by_depth,
        })
    output = {
        "source_files": len(files),
        "rows_per_arm_seed": 2048,
        "all_finite": finite,
        "deterministic_gate": {
            "passed": all(
                r["deterministic_repeat_match"]
                for values in arms.values() for r in values),
            "passing_arm_seeds": sum(
                r["deterministic_repeat_match"]
                for values in arms.values() for r in values),
            "total_arm_seeds": sum(map(len, arms.values())),
            "cause": (
                "Itinerant.forward added a random initial activity perturbation "
                "before checking evaluation mode; fixed in subsequent E2/E3 code."
            ),
        },
        "arms": {},
    }
    for arm, values in arms.items():
        output["arms"][arm] = {
            "n_seeds": len(values),
            "seed_results": values,
            "across_seed_mean": {
                k: mean(v["aggregate"][k] for v in values) for k in METRICS
            },
        }
    Path(args.output).write_text(json.dumps(output, indent=2) + "\n")


if __name__ == "__main__":
    main()
