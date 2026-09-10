#!/usr/bin/env python3
"""Execute the frozen Phase-5 suite through the real pinned OmegaClaw loop."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path


def resolve_source(project_root: Path, source: str) -> Path:
    candidates = (
        project_root / source,
        project_root / "protocosmo2" / "config" / "identity-draft" / source,
        project_root.parents[1] / source,
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    raise FileNotFoundError(f"frozen source cannot be resolved: {source}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", type=Path, required=True)
    parser.add_argument("--petta", type=Path, required=True)
    parser.add_argument("--core", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--model", default="openai/gpt-5.6-terra")
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()
    project_root = args.core.resolve().parents[3]
    suite = json.loads(args.suite.read_text(encoding="utf-8"))
    cases = suite.get("cases", [])
    if len(cases) != 10:
        raise ValueError("frozen suite must contain exactly ten cases")
    args.output.mkdir(parents=True, exist_ok=False)
    driver = Path(__file__).with_name("phase5_omegaclaw_case.py")
    results = []
    for index, case in enumerate(cases, 1):
        command = [sys.executable, str(driver), "--petta", str(args.petta),
                   "--core", str(args.core), "--provider", "OpenClawFileBridge",
                   "--file-channel",
                   "--session", f"phase5-real-{index:02d}-{case['id']}",
                   "--model", args.model, "--prompt", case["prompt"],
                   "--timeout", str(args.timeout),
                   *[item for source in case["sources"]
                     for item in ("--source", str(resolve_source(project_root, source)))]]
        run = subprocess.run(command, text=True, capture_output=True,
                             timeout=args.timeout + 30, check=False)
        (args.output / f"{index:02d}-{case['id']}.stdout.log").write_text(run.stdout, encoding="utf-8")
        (args.output / f"{index:02d}-{case['id']}.stderr.log").write_text(run.stderr, encoding="utf-8")
        record = {key: case[key] for key in ("id", "category", "critical", "expected", "sources")}
        record["exit_status"] = run.returncode
        if run.returncode == 0:
            lines = [line for line in run.stdout.splitlines() if line.startswith("{")]
            record.update(json.loads(lines[-1]))
        else:
            record["error"] = run.stderr[-2000:]
        results.append(record)
        print(json.dumps({"case": case["id"], "exit_status": run.returncode}), flush=True)
    report = {"suite_id": suite.get("suite_id"),
              "suite_sha256": hashlib.sha256(args.suite.read_bytes()).hexdigest(),
              "provider": "OpenClawFileBridge", "model": args.model,
              "outbound_channels": "disabled", "results": results}
    (args.output / "runtime-results.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    return 1 if any(item["exit_status"] != 0 for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
