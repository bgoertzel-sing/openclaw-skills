#!/usr/bin/env python3
"""Calibrate the Stage-0 persistence statistic using existing codec tokens.

This is deliberately provider-free: it does not re-encode audio or claim to
test MusicGen quality.  It tests the statistic itself.  Concatenating a token
sequence with exact copies represents perfect long-range recurrence while
preserving its local transitions except at the few copy boundaries.
"""

import hashlib
import json
import sys
from pathlib import Path

import torch


def persistence(codes_list):
    return [
        float(torch.stack([
            (codes[book, 1:] == codes[book, :-1]).float().mean()
            for codes in codes_list
        ]).mean())
        for book in range(codes_list[0].shape[0])
    ]


def main(path_text):
    path = Path(path_text)
    raw = path.read_bytes()
    codes = torch.load(path, map_location="cpu", weights_only=False)
    repeated = [torch.cat([item, item, item], dim=-1) for item in codes]
    baseline = persistence(codes)
    repeated_values = persistence(repeated)
    result = {
        "schema": "hdc-musicgen-persistence-proxy-calibration-v1",
        "input": str(path),
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "n_tracks": len(codes),
        "code_shape": list(codes[0].shape),
        "repeat_factor": 3,
        "baseline_persistence": baseline,
        "exact_repeat_persistence": repeated_values,
        "absolute_delta": [abs(a - b) for a, b in zip(baseline, repeated_values)],
        "interpretation": (
            "Exact long-range recurrence changes this adjacent-token statistic "
            "only at concatenation boundaries; it is not a direct recurrence metric."
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} CODES_PT")
    main(sys.argv[1])
