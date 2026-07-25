import copy
import unittest

import torch
import torch.nn.functional as F

from model import Itinerant
from run_carom_e2_e3 import make_activity_noise


class E2E3CompileTests(unittest.TestCase):
    def setUp(self):
        torch.manual_seed(314159)
        self.commands = torch.tensor([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
        self.workspace = torch.randint(0, 9, (2, 6))
        self.targets = torch.randint(0, 8, (2, 6))

    def test_explicit_noise_exactly_replays_original_eager_draw_order(self):
        model = Itinerant(
            d=8, K=4, steps=3, noise=0.02, mode_specific_fitness=True
        ).train()
        torch.manual_seed(2026)
        implicit = model(
            self.commands, self.workspace, return_traj=True
        )
        torch.manual_seed(2026)
        initial, steps = make_activity_noise(model, len(self.commands), torch.device("cpu"))
        explicit = model(
            self.commands, self.workspace, return_traj=True,
            initial_activity_noise=initial, activity_noise=steps,
        )
        self.assertTrue(torch.equal(implicit[0], explicit[0]))
        self.assertTrue(torch.equal(implicit[1], explicit[1]))

    def test_compiled_forward_gradients_and_optimizer_step_match_reference(self):
        reference = Itinerant(
            d=8, K=4, steps=3, noise=0.02, mode_specific_fitness=True
        ).train()
        candidate = copy.deepcopy(reference).train()
        candidate.enable_compiled_recurrence(
            backend="aot_eager", fullgraph=True
        )
        torch.manual_seed(2718)
        initial, steps = make_activity_noise(reference, len(self.commands), torch.device("cpu"))

        opt_reference = torch.optim.AdamW(reference.parameters(), lr=1e-3)
        opt_candidate = torch.optim.AdamW(candidate.parameters(), lr=1e-3)
        out_reference, activity_reference = reference(
            self.commands, self.workspace, return_traj=True,
            initial_activity_noise=initial, activity_noise=steps,
        )
        out_candidate, activity_candidate = candidate(
            self.commands, self.workspace, return_traj=True,
            initial_activity_noise=initial, activity_noise=steps,
        )
        loss_reference = F.cross_entropy(
            out_reference.flatten(0, 1), self.targets.flatten()
        )
        loss_candidate = F.cross_entropy(
            out_candidate.flatten(0, 1), self.targets.flatten()
        )
        loss_reference.backward()
        loss_candidate.backward()

        self.assertTrue(torch.equal(out_reference, out_candidate))
        self.assertTrue(torch.equal(activity_reference, activity_candidate))
        self.assertEqual(
            float(loss_reference.detach()), float(loss_candidate.detach())
        )
        for left, right in zip(reference.parameters(), candidate.parameters()):
            if left.grad is None or right.grad is None:
                self.assertIsNone(left.grad)
                self.assertIsNone(right.grad)
            else:
                self.assertTrue(
                    torch.allclose(left.grad, right.grad, atol=1e-7, rtol=1e-6)
                )

        opt_reference.step()
        opt_candidate.step()
        for left, right in zip(reference.parameters(), candidate.parameters()):
            self.assertTrue(torch.allclose(left, right, atol=1e-7, rtol=1e-6))

    def test_compiled_evaluation_is_bitwise_repeatable(self):
        model = Itinerant(
            d=8, K=4, steps=3, noise=0.02, mode_specific_fitness=True
        ).eval()
        model.enable_compiled_recurrence(
            backend="aot_eager", fullgraph=True
        )
        first = model(
            self.commands, self.workspace, return_diagnostics=True
        )
        second = model(
            self.commands, self.workspace, return_diagnostics=True
        )
        self.assertTrue(torch.equal(first[0], second[0]))
        for key in first[1]:
            self.assertTrue(torch.equal(first[1][key], second[1][key]), key)


if __name__ == "__main__":
    unittest.main()
