#!/usr/bin/env python3
"""Orchestrate the frozen CLA detector over the requested A6 exploration."""
from __future__ import annotations

import argparse
import csv
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


TIGHT_SEEDS = (101, 103, 107, 109, 113)
TIGHT_COUPLINGS = (0.35, 0.60)
TIGHT_DELAYS = (0, 3, 7)
CONTROLS = ("appraisal", "linear", "shuffled")
STRATA = ("core4", "roles8", "full20")

# Balanced exploratory design: all requested gain/coupling/delay levels occur,
# with 12 points rather than the 48-point Cartesian product. Two seeds provide
# a limited stability check. This is characterization, not confirmatory testing.
BROAD_CONFIGS = (
    (3.0, 0.15, 0),
    (3.0, 0.35, 3),
    (3.0, 0.60, 7),
    (3.0, 0.80, 14),
    (5.0, 0.15, 14),
    (5.0, 0.35, 7),
    (5.0, 0.60, 3),
    (5.0, 0.80, 0),
    (7.0, 0.15, 7),
    (7.0, 0.35, 14),
    (7.0, 0.60, 0),
    (7.0, 0.80, 3),
)
BROAD_SEEDS = (101, 113)


def run_capture(command, *, cwd, env, stdout_path, stderr_path):
    started = time.monotonic()
    with stdout_path.open("w", encoding="utf-8") as stdout, stderr_path.open("w", encoding="utf-8") as stderr:
        result = subprocess.run(command, cwd=cwd, env=env, stdout=stdout, stderr=stderr, check=False)
    return {
        "command": command,
        "exit_status": result.returncode,
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "stdout": str(stdout_path),
        "stderr": str(stderr_path),
    }


def broad_task(task):
    gain, coupling, delay, seed, control = task
    repo_root = os.environ["OMEGASIM_EXPERIMENT_REPO"]
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)
    from omegasim.a6_model import A6Params, simulate
    from scripts.run_cla_detector import evaluate_trace

    result = simulate(A6Params(seed=seed, steps=1024, gain=gain, coupling=coupling, delay=delay, control=control))
    retained = result["rows"][128:]
    rows = []
    for stratum in STRATA:
        metrics = evaluate_trace(retained, stratum=stratum, seed=seed, surrogates=5)
        metrics.update({
            "seed": seed,
            "gain": gain,
            "coupling": coupling,
            "delay": delay,
            "control": control,
            "sweep": "broad",
        })
        rows.append(metrics)
    return rows


def write_rows(path, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=tuple(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def cluster(row):
    if int(row["occupied_symbols"]) < 4:
        return "microstate_collapsed"
    compression = float(row["compression_margin_proxy_bits"]) > 0.0
    predictive = float(row["heldout_advantage_bits_per_symbol"]) >= 0.10
    if compression and predictive:
        return "compression_and_predictive"
    if compression:
        return "compression_only"
    if predictive:
        return "predictive_only"
    return "weak_readout"


def app_control_deltas(rows):
    keys = ("sweep", "seed", "gain", "coupling", "delay", "stratum")
    lookup = {tuple(row[key] for key in keys) + (row["control"],): row for row in rows}
    fields = (
        "occupied_symbols",
        "productions",
        "categories",
        "compression_margin_proxy_bits",
        "heldout_advantage_bits_per_symbol",
    )
    deltas = []
    for row in rows:
        if row["control"] != "appraisal":
            continue
        base = {key: row[key] for key in keys}
        for control in ("linear", "shuffled"):
            other = lookup[tuple(row[key] for key in keys) + (control,)]
            item = base | {"comparison": f"appraisal_minus_{control}"}
            for field in fields:
                item[f"delta_{field}"] = float(row[field]) - float(other[field])
            item["appraisal_detector_positive"] = bool(row["detector_positive"])
            item["control_detector_positive"] = bool(other["detector_positive"])
            deltas.append(item)
    return deltas


def aggregate(rows):
    metrics = (
        "occupied_symbols", "productions", "categories",
        "compression_margin_proxy_bits", "heldout_advantage_bits_per_symbol",
    )
    groups = {}
    for row in rows:
        key = tuple(row[name] for name in ("sweep", "gain", "coupling", "delay", "stratum", "control"))
        groups.setdefault(key, []).append(row)
    output = []
    for key, members in sorted(groups.items(), key=lambda item: tuple(map(str, item[0]))):
        item = dict(zip(("sweep", "gain", "coupling", "delay", "stratum", "control"), key))
        item["seeds"] = ",".join(str(row["seed"]) for row in sorted(members, key=lambda r: int(r["seed"])))
        item["n"] = len(members)
        for metric in metrics:
            item[f"mean_{metric}"] = sum(float(row[metric]) for row in members) / len(members)
        item["detector_positive_count"] = sum(bool(row["detector_positive"]) for row in members)
        item["detector_positive_rate"] = item["detector_positive_count"] / len(members)
        counts = {}
        for row in members:
            counts[row["qualitative_cluster"]] = counts.get(row["qualitative_cluster"], 0) + 1
        item["qualitative_cluster_counts"] = json.dumps(counts, sort_keys=True)
        output.append(item)
    return output


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--omegasim", type=Path, required=True)
    parser.add_argument("--chaoslang", type=Path, required=True)
    args = parser.parse_args()
    artifacts = args.run_dir / "artifacts"
    shards = artifacts / "tight-shards"
    shards.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{args.omegasim / 'src'}:{args.chaoslang / 'src'}"
    os.environ["OMEGASIM_EXPERIMENT_REPO"] = str(args.omegasim)
    steps = []

    checks = (
        (args.omegasim, "18c7408fe48eeac9e9ec53f18eb5b2d0ed840e2d"),
        (args.chaoslang, "974af31efaf6e3cc239252f78367d20e657ac45c"),
    )
    for repo, expected in checks:
        actual = subprocess.check_output(["git", "-C", str(repo), "rev-parse", "HEAD"], text=True).strip()
        if actual != expected:
            raise SystemExit(f"pin mismatch: {repo}: expected {expected}, got {actual}")
        dirty = subprocess.check_output(["git", "-C", str(repo), "status", "--porcelain=v1"], text=True)
        if dirty:
            raise SystemExit(f"dirty worktree: {repo}")

    test = run_capture(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=args.omegasim, env=env,
        stdout_path=args.run_dir / "tests.stdout.log", stderr_path=args.run_dir / "tests.stderr.log",
    )
    test["name"] = "unit_tests"
    steps.append(test)
    if test["exit_status"]:
        (args.run_dir / "steps_status.json").write_text(json.dumps(steps, indent=2) + "\n")
        return test["exit_status"]

    def tight_shard(pair):
        coupling, delay = pair
        tag = f"c{coupling:.2f}-d{delay}"
        output = shards / f"{tag}.json"
        command = [
            sys.executable, "scripts/run_cla_detector.py", "--output", str(output),
            "--seeds", ",".join(map(str, TIGHT_SEEDS)),
            "--couplings", str(coupling), "--delays", str(delay),
            "--steps", "1024", "--burn", "128", "--surrogates", "5",
        ]
        result = run_capture(
            command, cwd=args.omegasim, env=env,
            stdout_path=shards / f"{tag}.stdout.log", stderr_path=shards / f"{tag}.stderr.log",
        )
        result.update({"name": f"tight_{tag}", "output": str(output)})
        return result

    tight_pairs = tuple((c, d) for c in TIGHT_COUPLINGS for d in TIGHT_DELAYS)
    pending_pairs = []
    for coupling, delay in tight_pairs:
        tag = f"c{coupling:.2f}-d{delay}"
        output = shards / f"{tag}.json"
        csv_output = output.with_suffix(".csv")
        if output.exists() and csv_output.exists():
            payload = json.loads(output.read_text())
            if len(payload.get("rows", ())) != 45 or len(payload.get("promotions", ())) != 3:
                raise SystemExit(f"incomplete existing tight shard: {output}")
            steps.append({
                "name": f"tight_{tag}",
                "command": [sys.executable, "scripts/run_cla_detector.py", "--output", str(output),
                            "--seeds", ",".join(map(str, TIGHT_SEEDS)), "--couplings", str(coupling),
                            "--delays", str(delay), "--steps", "1024", "--burn", "128", "--surrogates", "5"],
                "exit_status": 0,
                "elapsed_seconds": None,
                "recovery_note": "Validated and reused after attempt 1 broad-import failure; original elapsed time was not persisted.",
                "output": str(output),
            })
        else:
            pending_pairs.append((coupling, delay))
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(tight_shard, pair) for pair in pending_pairs]
        for future in as_completed(futures):
            steps.append(future.result())
    if any(step["exit_status"] for step in steps):
        (args.run_dir / "steps_status.json").write_text(json.dumps(steps, indent=2) + "\n")
        return 1

    tight_rows = []
    promotions = []
    for path in sorted(shards.glob("c*-d*.json")):
        payload = json.loads(path.read_text())
        tight_rows.extend(payload["rows"])
        promotions.extend(payload["promotions"])
    for row in tight_rows:
        row["sweep"] = "tight"
    tight_payload = {
        "schema": "omegasim.cla_dynamics_exploration.tight.v1",
        "design": {"seeds": TIGHT_SEEDS, "gain": 5.0, "couplings": TIGHT_COUPLINGS, "delays": TIGHT_DELAYS,
                   "controls": CONTROLS, "strata": STRATA, "steps": 1024, "burn": 128, "surrogates": 5},
        "rows": tight_rows,
        "promotions": promotions,
        "passed": any(item["promote"] for item in promotions),
    }
    (artifacts / "tight_fingerprints.json").write_text(json.dumps(tight_payload, indent=2, sort_keys=True) + "\n")
    write_rows(artifacts / "tight_fingerprints.csv", tight_rows)

    tasks = [(g, c, d, seed, control) for g, c, d in BROAD_CONFIGS for seed in BROAD_SEEDS for control in CONTROLS]
    broad_rows = []
    started = time.monotonic()
    with ProcessPoolExecutor(max_workers=4) as pool:
        futures = [pool.submit(broad_task, task) for task in tasks]
        for future in as_completed(futures):
            broad_rows.extend(future.result())
    steps.append({"name": "broad_balanced_12_point", "command": ["internal ProcessPoolExecutor", "workers=4"],
                  "exit_status": 0, "elapsed_seconds": round(time.monotonic() - started, 3), "tasks": len(tasks)})
    broad_payload = {
        "schema": "omegasim.cla_dynamics_exploration.broad.v1",
        "design": {"configs": BROAD_CONFIGS, "seeds": BROAD_SEEDS, "controls": CONTROLS, "strata": STRATA,
                   "steps": 1024, "burn": 128, "surrogates": 5,
                   "note": "Balanced 12-point exploration, not the 48-point Cartesian product."},
        "rows": broad_rows,
    }
    (artifacts / "broad_fingerprints.json").write_text(json.dumps(broad_payload, indent=2, sort_keys=True) + "\n")
    write_rows(artifacts / "broad_fingerprints.csv", broad_rows)

    all_rows = tight_rows + broad_rows
    for row in all_rows:
        row["qualitative_cluster"] = cluster(row)
    deltas = app_control_deltas(all_rows)
    aggregates = aggregate(all_rows)
    combined = {
        "schema": "omegasim.cla_dynamics_exploration.v1",
        "claim_status": "observed detector readouts; not validated attractor structure",
        "frozen_thresholds": {"minimum_occupied_symbols": 4, "compression_margin_proxy_bits": 0.0,
                              "heldout_advantage_bits_per_symbol": 0.10},
        "qualitative_cluster_definitions": {
            "microstate_collapsed": "occupied symbols < 4",
            "compression_and_predictive": "compression margin > 0 and held-out advantage >= 0.10",
            "compression_only": "compression margin > 0 and held-out advantage < 0.10",
            "predictive_only": "compression margin <= 0 and held-out advantage >= 0.10",
            "weak_readout": "compression margin <= 0 and held-out advantage < 0.10",
        },
        "rows": all_rows,
        "appraisal_control_deltas": deltas,
        "aggregates": aggregates,
        "tight_promotions": promotions,
    }
    (artifacts / "all_fingerprints.json").write_text(json.dumps(combined, indent=2, sort_keys=True) + "\n")
    write_rows(artifacts / "all_fingerprints.csv", all_rows)
    (artifacts / "appraisal_control_deltas.json").write_text(json.dumps(deltas, indent=2, sort_keys=True) + "\n")
    write_rows(artifacts / "appraisal_control_deltas.csv", deltas)
    (artifacts / "fingerprint_aggregates.json").write_text(json.dumps(aggregates, indent=2, sort_keys=True) + "\n")
    write_rows(artifacts / "fingerprint_aggregates.csv", aggregates)

    hashes = {}
    for path in sorted(artifacts.glob("*")):
        if path.is_file():
            hashes[path.name] = sha256(path)
    (args.run_dir / "artifact_sha256.json").write_text(json.dumps(hashes, indent=2, sort_keys=True) + "\n")
    (args.run_dir / "steps_status.json").write_text(json.dumps(steps, indent=2) + "\n")
    print(json.dumps({"tight_rows": len(tight_rows), "broad_rows": len(broad_rows), "all_rows": len(all_rows),
                      "tight_promotions": [p for p in promotions if p["promote"]], "artifacts": hashes}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
