#!/usr/bin/env python3
"""Decisive wrapper for the frozen E0 coder calibration."""
from __future__ import annotations

import json
from pathlib import Path

from chaoslang.benchmarks.e0_coder_calibration import run


REPO = Path("/home/openclaw/research-agent/scratch/chaoslang-strict-replay")
HISTORICAL_LEDGER = Path(
    "/home/openclaw/research-agent/projects/chaos-language-algorithm/"
    "experiments/20260718T031500Z-synthetic-universal-control-v1"
)


if __name__ == "__main__":
    print(
        json.dumps(
            run(REPO, HISTORICAL_LEDGER),
            sort_keys=True,
            separators=(",", ":"),
        )
    )
