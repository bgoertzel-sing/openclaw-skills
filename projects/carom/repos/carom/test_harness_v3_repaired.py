import unittest
import tempfile

import torch

import harness_v3_probes as probes


class HarnessV3RepairTests(unittest.TestCase):
    def test_commuting_and_noncommuting_controls(self):
        diagonal = torch.diag(torch.tensor([0.5, 0.8]))
        scalar = 0.7 * torch.eye(2)
        self.assertEqual(probes.linear_commutator_energy(diagonal, scalar), 0)
        shear = torch.tensor([[1.0, 1.0], [0.0, 1.0]])
        swap = torch.tensor([[0.0, 1.0], [1.0, 0.0]])
        self.assertGreater(probes.linear_commutator_energy(shear, swap), 0)

    def test_stable_and_unstable_word_controls(self):
        contractions = [0.5 * torch.eye(2), 0.8 * torch.eye(2)]
        self.assertLess(probes.switching_word_growth(contractions, [0, 1] * 4), 1)
        # Individually nilpotent matrices whose alternating product expands.
        first = torch.tensor([[0.0, 2.0], [0.0, 0.0]])
        second = torch.tensor([[0.0, 0.0], [2.0, 0.0]])
        self.assertGreater(probes.switching_word_growth([first, second], [0, 1] * 4), 1)

    def test_local_generator_is_repeatable_without_global_rng_mutation(self):
        torch.manual_seed(99)
        before = torch.random.get_rng_state().clone()
        first = torch.randn(8, generator=probes._local_generator("cpu", 7))
        second = torch.randn(8, generator=probes._local_generator("cpu", 7))
        self.assertTrue(torch.equal(first, second))
        self.assertTrue(torch.equal(before, torch.random.get_rng_state()))

    def test_zero_coupling_is_safe(self):
        result = probes.cross_slot_effects([torch.zeros(3, 3)])
        self.assertTrue(result["zero_total_effect"])
        self.assertTrue(torch.isfinite(result["normalized_effect_matrix"]).all())
        self.assertEqual(result["offdiag_mass"], 0)

    def test_nonzero_coupling_preserves_device_and_effect(self):
        matrix = torch.eye(3)
        result = probes.cross_slot_effects([matrix, matrix])
        self.assertEqual(result["effect_matrix"].device, matrix.device)
        self.assertAlmostEqual(result["offdiag_mass"], 0)

    def test_padded_modes_do_not_change_decisiveness(self):
        base = torch.tensor([[[0.9, 0.1]]])
        padded = torch.tensor([[[0.9, 0.1, 100.0, 100.0]]])
        first = probes.decisiveness_from_trajectory(base, torch.tensor([[0, 1]]))
        second = probes.decisiveness_from_trajectory(
            padded, torch.tensor([[0, 1, -1, -1]])
        )
        self.assertAlmostEqual(first["live_normalized_entropy_mean"],
                               second["live_normalized_entropy_mean"], places=6)

    def test_checkpoint_loading_is_portable(self):
        with tempfile.NamedTemporaryFile() as handle:
            torch.save({"value": torch.ones(1)}, handle.name)
            loaded = probes.load_checkpoint(handle.name, "cpu")
        self.assertEqual(loaded["value"].device.type, "cpu")


if __name__ == "__main__":
    unittest.main()
