from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path


LEDGER = Path(__file__).resolve().parent
REPO = Path("/home/openclaw/research-agent/scratch/chaoslang-strict-replay")


class E0LedgerFreezeTests(unittest.TestCase):
    def test_manifest_fixes_matrix_without_sampling(self):
        manifest = json.loads((LEDGER / "manifest.json").read_text())
        self.assertEqual(manifest["code_commit"], "096cbb11b2d60e4d07a7bbfffb30b808e169dab4")
        self.assertEqual(manifest["seeds"], [26072601, 26072602, 26072603, 26072604, 26072605])
        self.assertEqual(manifest["lengths"], [1000, 10000, 100000])
        self.assertEqual(len(manifest["source_names"]), 7)
        self.assertEqual(len(manifest["coders"]), 6)

    def test_preregistered_inputs_match_hashes(self):
        for line in (LEDGER / "preregistration-sha256.txt").read_text().splitlines():
            expected, relative = line.split("  ", 1)
            observed = hashlib.sha256((REPO / relative).read_bytes()).hexdigest()
            self.assertEqual(observed, expected, relative)

    def test_historical_artifacts_and_suffix_hashes_are_copied(self):
        manifest = json.loads((LEDGER / "manifest.json").read_text())
        old = Path(
            "/home/openclaw/research-agent/projects/chaos-language-algorithm/"
            "experiments/20260718T031500Z-synthetic-universal-control-v1"
        )
        for name in ("manifest.json", "results.json"):
            observed = hashlib.sha256((old / name).read_bytes()).hexdigest()
            self.assertEqual(observed, manifest["historical_lz78"][name[:-5] + "_sha256"])
        old_manifest = json.loads((old / "manifest.json").read_text())
        copied = manifest["historical_lz78"]["suffix_sha256"]
        self.assertEqual(
            {row["name"]: row["suffix_sha256"] for row in old_manifest["fixtures"]},
            copied,
        )

    def test_command_is_exact_and_results_do_not_exist_before_execution(self):
        expected = (
            "#!/usr/bin/env bash\n"
            "set -u\n"
            "repo=/home/openclaw/research-agent/scratch/chaoslang-strict-replay\n"
            "ledger=/home/openclaw/research-agent/projects/chaos-language-algorithm/experiments/20260726T171500Z-e0-coder-calibration-v1\n"
            'cd "$repo" || exit 97\n'
            '/usr/bin/time -v -o "$ledger/timing.txt" env PYTHONPATH=src python3 "$ledger/benchmark.py" > "$ledger/results.json" 2> "$ledger/stderr.txt"\n'
            "status=$?\n"
            "printf '%s\\n' \"$status\" > \"$ledger/exit-status.txt\"\n"
            'exit "$status"\n'
        )
        self.assertEqual((LEDGER / "command.sh").read_text(), expected)
        for name in ("results.json", "stderr.txt", "timing.txt", "exit-status.txt"):
            self.assertFalse((LEDGER / name).exists(), name)


if __name__ == "__main__":
    unittest.main()
