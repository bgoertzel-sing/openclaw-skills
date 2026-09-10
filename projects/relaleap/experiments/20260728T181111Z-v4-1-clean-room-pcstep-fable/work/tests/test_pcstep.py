import copy
import sys
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pcstep import (  # noqa: E402
    Batch,
    Config,
    StepState,
    Theta,
    initial_optimizer,
    pc_step,
    restore,
    settle_t1,
    snapshot,
)


def fixture():
    theta = Theta(
        np.array([[0.4, -0.2], [0.1, 0.3]], dtype=np.float64),
        np.array([[0.7, -0.5]], dtype=np.float64),
    )
    batch = Batch(
        "b0",
        np.array([[1.0, 2.0], [-1.0, 0.5]], dtype=np.float64),
        np.array([[0.25], [-0.4]], dtype=np.float64),
    )
    return theta, initial_optimizer(theta, 1729, ("b0", "b1")), batch


def independent_reference(theta, opt, batch, gate, cfg):
    """Handwritten oracle, intentionally not calling adapter helpers."""
    n = len(batch.inputs)
    h0 = batch.inputs.dot(theta.layer1.T)
    y0 = h0.dot(theta.layer2.T)
    dy = (y0 - batch.targets) / n
    e2 = -cfg.error_lr * dy
    e1 = -cfg.error_lr * dy.dot(theta.layer2)
    hs = h0 + e1
    ys = hs.dot(theta.layer2.T) + e2
    g1 = ((h0 - hs).T.dot(batch.inputs) / n) * gate["layer1"]
    g2 = ((hs.dot(theta.layer2.T) - ys).T.dot(hs) / n) * gate["layer2"]

    def update(p, g, m, v):
        mn = cfg.beta1 * m + (1 - cfg.beta1) * g
        vn = cfg.beta2 * v + (1 - cfg.beta2) * g**2
        mh = mn / (1 - cfg.beta1)
        vh = vn / (1 - cfg.beta2)
        pn = p * (1 - cfg.weight_lr * cfg.weight_decay)
        return pn - cfg.weight_lr * mh / (np.sqrt(vh) + cfg.epsilon), mn, vn

    p1, m1, v1 = update(theta.layer1, g1, opt.m1, opt.v1)
    p2, m2, v2 = update(theta.layer2, g2, opt.m2, opt.v2)
    return (p1, p2, m1, m2, v1, v2, e1, e2)


class PCStepTests(unittest.TestCase):
    def test_settlement_freezes_weights_and_inputs(self):
        theta, _, batch = fixture()
        before1, before2 = theta.layer1.copy(), theta.layer2.copy()
        settle_t1(theta, batch, 0.05)
        np.testing.assert_array_equal(theta.layer1, before1)
        np.testing.assert_array_equal(theta.layer2, before2)

    def test_t1_matches_independent_reference_update(self):
        theta, opt, batch = fixture()
        cfg = Config(weight_decay=0.01)
        gate = {"layer1": 0.25, "layer2": 1.0}
        actual = pc_step(theta, opt, batch, 1, gate, cfg)
        expected = independent_reference(theta, opt, batch, gate, cfg)
        observed = (
            actual.theta.layer1,
            actual.theta.layer2,
            actual.optimizer_state.m1,
            actual.optimizer_state.m2,
            actual.optimizer_state.v1,
            actual.optimizer_state.v2,
            *actual.settled_errors,
        )
        for got, want in zip(observed, expected):
            # The oracle deliberately uses dot/power spellings different from
            # the implementation; permit only roundoff-scale reassociation.
            np.testing.assert_allclose(got, want, rtol=1e-15, atol=1e-18)

    def test_step_is_pure_and_deterministic(self):
        theta, opt, batch = fixture()
        theta_copy = Theta(theta.layer1.copy(), theta.layer2.copy())
        opt_copy = copy.deepcopy(opt)
        a = pc_step(theta, opt, batch, 1, {"layer1": 1.0, "layer2": 1.0})
        b = pc_step(theta, opt, batch, 1, {"layer1": 1.0, "layer2": 1.0})
        self.assertEqual(snapshot(a), snapshot(b))
        np.testing.assert_array_equal(theta.layer1, theta_copy.layer1)
        np.testing.assert_array_equal(theta.layer2, theta_copy.layer2)
        for got, want in (
            (opt.m1, opt_copy.m1),
            (opt.m2, opt_copy.m2),
            (opt.v1, opt_copy.v1),
            (opt.v2, opt_copy.v2),
        ):
            np.testing.assert_array_equal(got, want)
        self.assertEqual(opt.step, opt_copy.step)
        self.assertEqual(opt.rng_state, opt_copy.rng_state)
        self.assertEqual(opt.batch_plan, opt_copy.batch_plan)

    def test_snapshot_restore_is_exact_and_replayable(self):
        theta, opt, batch = fixture()
        state = pc_step(theta, opt, batch, 1, {"layer1": 0.0, "layer2": 1.0})
        encoded = snapshot(state)
        restored = restore(encoded)
        self.assertIsInstance(restored, StepState)
        self.assertEqual(snapshot(restored), encoded)

        batch1 = Batch("b1", batch.inputs * 0.5, batch.targets + 0.1)
        gate = {"layer1": 1.0, "layer2": 0.5}
        left = pc_step(state.theta, state.optimizer_state, batch1, 2, gate)
        right = pc_step(restored.theta, restored.optimizer_state, batch1, 2, gate)
        self.assertEqual(snapshot(left), snapshot(right))

    def test_gate_and_batch_plan_fail_closed(self):
        theta, opt, batch = fixture()
        with self.assertRaises(ValueError):
            pc_step(theta, opt, batch, 1, {"layer1": 1.0})
        wrong = Batch("wrong", batch.inputs, batch.targets)
        with self.assertRaises(ValueError):
            pc_step(theta, opt, wrong, 1, {"layer1": 1.0, "layer2": 1.0})


if __name__ == "__main__":
    unittest.main()
