#!/usr/bin/env python3
"""Tests for the piecewise schedule runner."""
import math
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from run_carom_gpt2_piecewise_schedule import (
    piecewise_lr,
    original_onecycle_lr,
)


class TestPiecewiseSchedule(unittest.TestCase):
    def test_phase1_warmup(self):
        """Phase 1 warmup: LR increases from near-zero toward phase1_peak."""
        lr_0 = piecewise_lr(0, phase1_steps=3000, phase2_steps=9000)
        lr_mid = piecewise_lr(75, phase1_steps=3000, phase2_steps=9000)
        lr_peak = piecewise_lr(150, phase1_steps=3000, phase2_steps=9000)
        self.assertGreater(lr_peak, lr_mid)
        self.assertGreater(lr_mid, lr_0)
        self.assertGreater(lr_0, 0)

    def test_phase1_peak_value(self):
        """Phase 1 should peak at phase1_peak (2e-3)."""
        lr_at_peak = piecewise_lr(150, phase1_steps=3000, phase2_steps=9000)
        self.assertAlmostEqual(lr_at_peak, 2e-3, places=5)

    def test_phase1_decays_to_phase2_peak(self):
        """Phase 1 should decay from phase1_peak to approximately phase2_peak."""
        lr_end_phase1 = piecewise_lr(2999, phase1_steps=3000, phase2_steps=9000)
        self.assertLess(lr_end_phase1, 5e-4)
        self.assertGreater(lr_end_phase1, 5e-5)

    def test_phase2_starts_at_phase2_peak(self):
        """Phase 2 starts at phase2_peak (1e-4) with no warmup."""
        lr_phase2_start = piecewise_lr(3000, phase1_steps=3000, phase2_steps=9000)
        self.assertAlmostEqual(lr_phase2_start, 1e-4, places=6)

    def test_phase2_decays_to_floor(self):
        """Phase 2 should decay toward floor (0.1 * 1e-4 = 1e-5)."""
        lr_phase2_end = piecewise_lr(11999, phase1_steps=3000, phase2_steps=9000)
        self.assertLess(lr_phase2_end, 2e-5)
        self.assertGreater(lr_phase2_end, 0)

    def test_monotone_decrease_phase1_post_peak(self):
        """After warmup peak, phase 1 LR should decrease monotonically."""
        prev = piecewise_lr(150, phase1_steps=3000, phase2_steps=9000)
        for step in range(200, 3000, 100):
            curr = piecewise_lr(step, phase1_steps=3000, phase2_steps=9000)
            self.assertLessEqual(curr, prev + 1e-10,
                                 f"LR increased at step {step}: {curr} > {prev}")
            prev = curr

    def test_monotone_decrease_phase2(self):
        """Phase 2 LR should decrease monotonically from phase2_peak."""
        prev = piecewise_lr(3000, phase1_steps=3000, phase2_steps=9000)
        for step in range(3100, 12000, 100):
            curr = piecewise_lr(step, phase1_steps=3000, phase2_steps=9000)
            self.assertLessEqual(curr, prev + 1e-10,
                                 f"LR increased at step {step}: {curr} > {prev}")
            prev = curr

    def test_phase1_higher_than_phase2(self):
        """Phase 1 peak should be much higher than phase 2 peak."""
        lr_phase1 = piecewise_lr(150, phase1_steps=3000, phase2_steps=9000)
        lr_phase2 = piecewise_lr(3000, phase1_steps=3000, phase2_steps=9000)
        self.assertGreater(lr_phase1, 10 * lr_phase2)

    def test_continuity_at_boundary(self):
        """LR should be continuous at the phase1/phase2 boundary."""
        lr_before = piecewise_lr(2999, phase1_steps=3000, phase2_steps=9000)
        lr_at = piecewise_lr(3000, phase1_steps=3000, phase2_steps=9000)
        # Both should be near phase2_peak (1e-4)
        self.assertLess(abs(lr_before - lr_at) / max(lr_before, lr_at), 0.5,
                        f"Large jump at boundary: {lr_before} -> {lr_at}")

    def test_onecycle_same_peak(self):
        """Both schedules should peak at 2e-3."""
        warmup_oc = max(1, round(12000 * 0.05))
        warmup_pw = max(1, round(3000 * 0.05))
        oc_peak = original_onecycle_lr(warmup_oc, total_steps=12000)
        pw_peak = piecewise_lr(warmup_pw, phase1_steps=3000, phase2_steps=9000)
        self.assertAlmostEqual(oc_peak, 2e-3, places=5)
        self.assertAlmostEqual(pw_peak, 2e-3, places=5)

    def test_nonnegative(self):
        """LR should never be negative."""
        for step in range(0, 12000, 50):
            lr = piecewise_lr(step, phase1_steps=3000, phase2_steps=9000)
            self.assertGreater(lr, 0, f"Negative LR at step {step}")


class TestSmokeRun(unittest.TestCase):
    """Smoke test: run a tiny piecewise experiment end-to-end."""

    def test_smoke(self):
        """Run a 4-step piecewise smoke to verify the runner works."""
        import tempfile
        import json
        from pathlib import Path

        try:
            import torch
            import exp2_compiled_channel as exp2
        except (ImportError, RuntimeError):
            self.skipTest("torch or exp2 not available")

        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir = Path(tmpdir)
            import subprocess
            result = subprocess.run(
                [sys.executable, str(Path(__file__).parent / "run_carom_gpt2_piecewise_schedule.py"),
                 "--output-dir", str(tmpdir), "--smoke"],
                capture_output=True, text=True, timeout=120,
                cwd=str(Path(__file__).parent),
            )
            if result.returncode != 0:
                self.fail(f"Smoke run failed: {result.stderr}")
            summary_path = tmpdir / "summary.json"
            self.assertTrue(summary_path.exists(), "summary.json not produced")
            with summary_path.open() as f:
                summary = json.load(f)
            self.assertIn("piecewise", summary)
            self.assertIn("onecycle_control", summary)
            self.assertGreater(len(summary["piecewise"]), 0)
            self.assertGreater(len(summary["onecycle_control"]), 0)


if __name__ == "__main__":
    unittest.main()
