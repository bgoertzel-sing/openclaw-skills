import unittest

from run_carom_gpt2_schedule_diagnostic import normalized_warmup_cosine


class ScheduleDiagnosticTests(unittest.TestCase):
    def test_schedule_is_bounded_and_finishes_at_floor(self):
        values = [normalized_warmup_cosine(step, 100) for step in range(100)]
        self.assertTrue(all(0 < value <= 1 for value in values))
        self.assertAlmostEqual(max(values), 1)
        self.assertAlmostEqual(values[-1], 0.1)

    def test_schedule_has_same_normalized_shape(self):
        short = [normalized_warmup_cosine(step, 100) for step in (4, 50, 99)]
        long = [normalized_warmup_cosine(step, 200) for step in (9, 100, 199)]
        for first, second in zip(short, long):
            self.assertAlmostEqual(first, second, places=2)


if __name__ == "__main__":
    unittest.main()
