#!/usr/bin/env python3
"""Validate the frozen Phase 5 suite without starting an agent or provider."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


REQUIRED_CASE_KEYS = {"id", "category", "prompt", "expected", "sources", "critical"}
REQUIRED_CATEGORIES = {
    "durable-recall", "evidence-status", "continuity", "authority-boundary",
    "memory-conflict", "telegram-safety", "capability-honesty", "hyperon-task",
    "experiment-method",
}
REQUIRED_CRITICAL = {
    "recall-attribution", "project-status", "destructive-refusal",
    "paid-compute-refusal", "source-precedence", "routing-and-loop", "unavailable-tool",
}


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: phase5_shadow_preflight.py SUITE.json", file=sys.stderr)
        return 2
    path = Path(argv[1]).resolve()
    suite = json.loads(path.read_text(encoding="utf-8"))
    cases = suite.get("cases")
    errors: list[str] = []
    if suite.get("schema_version") != "1.0": errors.append("schema_version must be 1.0")
    if not isinstance(cases, list) or len(cases) < 10: errors.append("at least ten cases required")
    ids = []
    categories = set()
    for n, case in enumerate(cases or [], 1):
        missing = REQUIRED_CASE_KEYS - set(case)
        if missing: errors.append(f"case {n} missing {sorted(missing)}")
        ids.append(case.get("id"))
        categories.add(case.get("category"))
        for key in ("prompt", "expected", "sources"):
            if not case.get(key): errors.append(f"case {case.get('id')} has empty {key}")
    duplicate_ids = sorted({x for x in ids if ids.count(x) > 1})
    if duplicate_ids: errors.append(f"duplicate IDs: {duplicate_ids}")
    if not REQUIRED_CATEGORIES <= categories: errors.append(f"missing categories: {sorted(REQUIRED_CATEGORIES - categories)}")
    critical_ids = {c.get("id") for c in cases or [] if c.get("critical")}
    if not REQUIRED_CRITICAL <= critical_ids: errors.append(f"missing critical controls: {sorted(REQUIRED_CRITICAL - critical_ids)}")
    score = suite.get("scoring", {})
    if score.get("aggregate_score_is_not_a_release_gate") is not True:
        errors.append("aggregate-score non-gate marker missing")
    report = {
        "suite_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "suite_id": suite.get("suite_id"),
        "case_count": len(cases or []),
        "critical_case_count": len(critical_ids),
        "categories": sorted(categories),
        "status": "passed" if not errors else "failed",
        "errors": errors,
        "provider_or_agent_started": False,
    }
    print(json.dumps(report, sort_keys=True, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
