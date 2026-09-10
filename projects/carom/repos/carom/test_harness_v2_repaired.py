import tempfile
import unittest

import torch

import harness_v2 as harness


class HarnessV2RepairTests(unittest.TestCase):
    def test_revisit_is_not_erased(self):
        trajectory = torch.zeros(5, 4)
        for index, mode in enumerate((0, 1, 0, 2, 3)):
            trajectory[index, mode] = 1
        result = harness.itinerary_metrics(
            trajectory, torch.tensor([0, 1, 2, 3]),
            dominance_margin=0.01, max_normalized_entropy=1.0,
        )
        self.assertEqual(result["exact_order"], 0)
        self.assertEqual(result["revisits"], 1)
        self.assertLess(result["trans_prec"], 1)

    def test_auroc_all_tied_is_half_regardless_of_position(self):
        for positive in range(6):
            labels = torch.zeros(6)
            labels[positive] = 1
            self.assertEqual(harness.tie_correct_auroc(torch.zeros(6), labels), 0.5)

    def test_auroc_mixed_ties(self):
        scores = torch.tensor([1.0, 1.0, 0.0, 0.0])
        labels = torch.tensor([1, 0, 1, 0])
        self.assertEqual(harness.tie_correct_auroc(scores, labels), 0.5)

    def test_degenerate_auroc_is_undefined(self):
        self.assertIsNone(harness.tie_correct_auroc(torch.ones(3), torch.ones(3)))
        self.assertIsNone(harness.tie_correct_auroc(torch.ones(3), torch.zeros(3)))

    def test_smeared_activity_is_unclassified(self):
        result = harness.itinerary_metrics(
            torch.ones(8, 4), torch.tensor([0, 1, 2, 3])
        )
        self.assertEqual(result["classified_fraction"], 0)
        self.assertEqual(result["coverage"], 0)

    def test_span_adapter_is_called(self):
        token = object()
        self.assertIs(harness.span_embeddings(lambda lm, t, s: token, None,
                                              {"T": None, "SP": None}), token)
        with self.assertRaises(ValueError):
            harness.span_embeddings(None, None, {"T": None, "SP": None})

    def test_temporary_steps_restored_on_exception(self):
        model = type("Model", (), {"S": 72})()
        with self.assertRaises(RuntimeError):
            with harness.temporary_integration_steps(model, 100):
                raise RuntimeError
        self.assertEqual(model.S, 72)

    def test_loaded_corpus_is_cpu_canonical(self):
        with tempfile.NamedTemporaryFile() as handle:
            harness.save_corpora({"x": torch.ones(2)}, handle.name)
            loaded = harness.load_corpora(handle.name)
        self.assertEqual(loaded["x"].device.type, "cpu")


if __name__ == "__main__":
    unittest.main()
