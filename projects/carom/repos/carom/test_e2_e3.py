import unittest

import torch

from model import Itinerant, direction_free_channel_penalties
from run_carom_e2_e3 import corpus_to_device, evaluate
from run_carom_e0_e1 import make_eval_corpus


class E2E3Tests(unittest.TestCase):
    def test_corpus_to_device_preserves_non_tensor_fields(self):
        corpus = (torch.tensor([1]), "metadata")
        moved = corpus_to_device(corpus, torch.device("cpu"))
        self.assertTrue(torch.equal(moved[0], corpus[0]))
        self.assertEqual(moved[1], "metadata")

    def test_e2_fitness_is_mode_specific(self):
        model = Itinerant(d=8, K=4, steps=4, mode_specific_fitness=True)
        model.eval()
        w = torch.randn(2, 6, 8)
        commands = torch.tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
        score = model.fitness(w, commands)
        self.assertEqual(tuple(score.shape), (2, 5))
        self.assertGreater(float(score.var(-1).mean().detach()), 0.0)

    def test_feature_ablation_removes_command_dependence(self):
        model = Itinerant(
            d=8, K=4, steps=4, mode_specific_fitness=True,
            fitness_features=("workspace", "position"))
        model.eval()
        w = torch.randn(2, 6, 8)
        p = torch.arange(5).expand(2, -1)
        a = model.fitness(w, torch.tensor([[1, 2, 3, 4, 5]] * 2), p)
        b = model.fitness(w, torch.tensor([[5, 4, 3, 2, 1]] * 2), p)
        self.assertTrue(torch.equal(a, b))

    def test_e3_penalties_are_mode_permutation_invariant(self):
        activity = torch.rand(3, 8, 4)
        perm = torch.tensor([2, 0, 3, 1])
        left = direction_free_channel_penalties(activity)
        right = direction_free_channel_penalties(activity[:, :, perm])
        for key in left:
            self.assertTrue(torch.allclose(left[key], right[key]), key)

    def test_eval_has_no_random_initial_activity(self):
        model = Itinerant(d=8, K=4, steps=4, mode_specific_fitness=True)
        model.eval()
        C = torch.tensor([[1, 2, 3, 4, 5]])
        X = torch.zeros(1, 6, dtype=torch.long)
        first = model(C, X, return_traj=True)
        second = model(C, X, return_traj=True)
        self.assertTrue(torch.equal(first[0], second[0]))
        self.assertTrue(torch.equal(first[1], second[1]))

    def test_evaluation_temporarily_uses_reference_recurrence(self):
        model = Itinerant(d=8, K=4, steps=2, mode_specific_fitness=True)
        sentinel = object()
        object.__setattr__(model, "_compiled_recurrent_step", sentinel)
        corpus = make_eval_corpus(4, 19)
        first = evaluate(model, corpus, batch_size=2)
        second = evaluate(model, corpus, batch_size=2)
        self.assertEqual(first, second)
        self.assertIs(model._compiled_recurrent_step, sentinel)


if __name__ == "__main__":
    unittest.main()
