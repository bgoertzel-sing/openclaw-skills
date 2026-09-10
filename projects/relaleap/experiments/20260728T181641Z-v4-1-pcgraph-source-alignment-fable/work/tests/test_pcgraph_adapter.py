import copy
import sys
import unittest
from pathlib import Path

import numpy as np

WORK = Path(__file__).resolve().parents[1]
RUN = WORK.parent
REPO = RUN.parents[1] / "repos" / "metta-on-mork"
ORACLE = REPO / "demos" / "pcgraph" / "oracle" / "xor_jpc_reference.npz"
sys.path.insert(0, str(WORK))

from pcgraph_adapter import (  # noqa: E402
    Batch,
    StepState,
    Weights,
    initial_optimizer,
    pc_step,
    restore,
    settle,
    settle_tick,
    snapshot,
)


class SourceAlignmentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.oracle = np.load(ORACLE)
        cls.weights = Weights(
            cls.oracle["initial_wxh"].copy(), cls.oracle["initial_why"].copy()
        )
        cls.batch = Batch(
            "xor-01", cls.oracle["x_single"].copy(), cls.oracle["y_single"].copy()
        )

    def test_one_tick_matches_checked_oracle_fp32_tolerance(self):
        zeros = np.zeros((1, 2), dtype=np.float32)
        tick = settle_tick(self.weights, self.batch, zeros, zeros)
        expected = {
            "pre_h": "settle_pre_h",
            "pcs_h": "settle_pcs_h",
            "phi_h": "settle_phi_h",
            "pre_y": "settle_pre_y",
            "pcs_y": "settle_pcs_y",
            "residual": "settle_residual",
            "energy": "settle_energy",
            "pcb_h": "settle_pcb_h",
            "pcg_h": "settle_pcg_h",
            "pcg_y": "settle_pcg_y",
        }
        for cell, key in expected.items():
            np.testing.assert_allclose(
                tick.cells[cell], self.oracle[key][0], rtol=2.4e-6, atol=6e-8
            )
        np.testing.assert_allclose(
            tick.e_h, self.oracle["settle_pce_h_after"][0], rtol=2.4e-6, atol=6e-8
        )
        np.testing.assert_allclose(
            tick.e_y, self.oracle["settle_pce_y_after"][0], rtol=2.4e-6, atol=6e-8
        )

    def test_end_of_settle_local_update_matches_checked_oracle(self):
        # The oracle's "local_m1_after_one" is training update 0, hence the
        # first XOR training row (x=[0,0]), not the separate x_single trace.
        training_batch = Batch(
            "xor-00",
            self.oracle["x_train"][:1].copy(),
            self.oracle["y_train"][:1].copy(),
        )
        settled = settle(self.weights, training_batch, ticks=16)
        state = pc_step(
            self.weights,
            initial_optimizer(20260715, ("xor-00",)),
            training_batch,
            1,
            {"xh": 1.0, "hy": 1.0},
        )
        np.testing.assert_array_equal(state.settled.e_h, settled.e_h)
        np.testing.assert_allclose(
            state.weights.wxh,
            self.oracle["local_m1_after_one_wxh"],
            rtol=2.4e-6,
            atol=6e-8,
        )
        np.testing.assert_allclose(
            state.weights.why,
            self.oracle["local_m1_after_one_why"],
            rtol=2.4e-6,
            atol=6e-8,
        )

    def test_settlement_freezes_weights_and_adapter_is_pure(self):
        before = (self.weights.wxh.copy(), self.weights.why.copy())
        opt = initial_optimizer(17, ("xor-01",))
        opt_before = copy.deepcopy(opt)
        a = pc_step(self.weights, opt, self.batch, 1, {"xh": 0.0, "hy": 1.0})
        b = pc_step(self.weights, opt, self.batch, 1, {"xh": 0.0, "hy": 1.0})
        np.testing.assert_array_equal(self.weights.wxh, before[0])
        np.testing.assert_array_equal(self.weights.why, before[1])
        self.assertEqual(opt, opt_before)
        self.assertEqual(snapshot(a), snapshot(b))
        np.testing.assert_array_equal(a.weights.wxh, self.weights.wxh)

    def test_snapshot_restore_exact_and_replayable(self):
        first = pc_step(
            self.weights,
            initial_optimizer(23, ("xor-01", "xor-01")),
            self.batch,
            1,
            {"xh": 1.0, "hy": 0.5},
        )
        payload = snapshot(first)
        restored = restore(payload)
        self.assertIsInstance(restored, StepState)
        self.assertEqual(snapshot(restored), payload)
        left = pc_step(first.weights, first.optimizer_state, self.batch, 2, {"xh": 1.0, "hy": 1.0})
        right = pc_step(restored.weights, restored.optimizer_state, self.batch, 2, {"xh": 1.0, "hy": 1.0})
        self.assertEqual(snapshot(left), snapshot(right))

    def test_gate_and_batch_plan_fail_closed(self):
        opt = initial_optimizer(1, ("xor-01",))
        with self.assertRaises(ValueError):
            pc_step(self.weights, opt, self.batch, 1, {"xh": 1.0})
        wrong = Batch("wrong", self.batch.x, self.batch.y)
        with self.assertRaises(ValueError):
            pc_step(self.weights, opt, wrong, 1, {"xh": 1.0, "hy": 1.0})


if __name__ == "__main__":
    unittest.main()
