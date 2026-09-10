import random
import unittest

import torch

from model import Itinerant
from run_carom_e0_e1 import activity_metrics, corpus_hash, make_eval_corpus


class E0E1Tests(unittest.TestCase):
    def test_eval_corpus_is_reproducible_and_depth_balanced(self):
        a = make_eval_corpus(20, 123)
        b = make_eval_corpus(20, 123)
        self.assertEqual(corpus_hash(a), corpus_hash(b))
        self.assertEqual(a[4].bincount(minlength=6)[2:].tolist(), [5, 5, 5, 5])

    def test_normalized_mixture_is_scale_invariant_without_dynamics(self):
        torch.manual_seed(1)
        model = Itinerant(d=8, K=4, steps=3, noise=0., normalize_activity=True)
        model.eval()
        C, _, X, _, _ = make_eval_corpus(4, 1)
        a = torch.rand(4, 3, 5) + .2
        out1 = model(C, X, activity_override=a)
        out2 = model(C, X, activity_override=3 * a)
        self.assertTrue(torch.allclose(out1, out2, atol=2e-6, rtol=2e-6))

    def test_diagnostics_are_finite_and_shaped(self):
        torch.manual_seed(2)
        model = Itinerant(d=8, K=4, steps=4, noise=0.)
        model.eval()
        C, _, X, _, _ = make_eval_corpus(4, 2)
        _, diag = model(C, X, return_diagnostics=True)
        self.assertEqual(diag["activity"].shape, (4, 4, 5))
        self.assertEqual(diag["workspace_update_norm"].shape, (4, 4))
        self.assertTrue(torch.isfinite(diag["activity"]).all())
        rows = activity_metrics(diag["activity"], diag["workspace_update_norm"])
        self.assertEqual(len(rows), 4)


if __name__ == "__main__":
    unittest.main()
