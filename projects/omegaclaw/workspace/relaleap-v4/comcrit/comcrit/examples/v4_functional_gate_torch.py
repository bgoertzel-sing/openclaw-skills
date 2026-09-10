#!/usr/bin/env python3
"""Run the frozen V4-0 nonlinear Torch functional gate."""
import argparse
import json
from pathlib import Path

from comcrit.fixture_nonlinear_torch import FixtureConfig, run_family


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--quick", action="store_true")
    args = parser.parse_args()
    common = {}
    if args.quick:
        common = dict(n_probe_states=2, pretrain_steps=10, noise_replicates=2)
    configs = [
        FixtureConfig("B1_input_permutation", 1729, 1e-3, **common),
        FixtureConfig("B2_output_shift", 3253, 1e-3, **common),
        FixtureConfig("B1_stress_lr1e-2", 6421, 1e-2, **common),
        FixtureConfig("aligned_null", 7919, 1e-3, **common),
    ]
    results = {"schema_version": 1, "backend": "approximate_full_state_AD",
               "families": {}}
    for config in configs:
        print(f"[{config.family}] running", flush=True)
        results["families"][config.family] = run_family(config)
    # Evaluate only the immutable thresholds in the execution plan.
    admitted = [v for k, v in results["families"].items()
                if k != "aligned_null"]
    checks = {
        "spearman_ge_0_5": all(
            c["full_state"]["spearman"] >= .5
            for f in admitted for c in f["cells"].values()),
        "sign_auroc_ge_0_75_where_identified": all(
            c["full_state"]["sign_auroc"] >= .75
            for f in admitted for c in f["cells"].values()
            if c["full_state"]["sign_auroc"] == c["full_state"]["sign_auroc"]),
        "synergy_spearman_ge_0_6": all(
            f["synergy"]["spearman"] >= .6 for f in admitted),
        "null_false_benefit_le_0_05":
            results["families"]["aligned_null"]["null_false_benefit_rate"] <= .05,
        "valid_cell_h_le_5": all(
            any(int(h) <= 5 and c["full_state"]["spearman"] >= .5
                for h, c in f["cells"].items()) for f in admitted),
        "full_noninferior_every_cell": all(
            c["full_state"]["spearman"] >= c["frozen_D"]["spearman"]
            for f in admitted for c in f["cells"].values()),
        "stress_improvement_ge_0_15": any(
            c["full_state"]["spearman"] - c["frozen_D"]["spearman"] >= .15
            for c in results["families"]["B1_stress_lr1e-2"]["cells"].values()),
        "median_strong_effect_ge_5_sigma": all(
            f["median_strong_action_sigma"] >= 5 for f in admitted),
    }
    results["gate_checks"] = checks
    if not checks["median_strong_effect_ge_5_sigma"]:
        results["gate_verdict"] = "INCONCLUSIVE"
        results["gate_reason"] = (
            "The frozen >=5 sigma family-admission precheck failed; "
            "confirmation metrics are descriptive only.")
    else:
        results["gate_verdict"] = "PASS" if all(checks.values()) else "FAIL"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2, allow_nan=True) + "\n")
    print(json.dumps({"gate_verdict": results["gate_verdict"],
                      "gate_checks": checks}, indent=2), flush=True)


if __name__ == "__main__":
    main()
