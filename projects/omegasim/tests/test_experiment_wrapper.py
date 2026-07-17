import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).parents[1] / "scripts" / "experiment_wrapper.py"
SPEC = importlib.util.spec_from_file_location("omegasim_experiment_wrapper", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class CanonicalSortRowsTests(unittest.TestCase):
    def row(self, seed, control):
        return {
            "sweep": "broad",
            "gain": 5.0,
            "coupling": 0.6,
            "delay": 3,
            "seed": seed,
            "control": control,
            "stratum": "roles8",
            "metric": seed / 10,
        }

    def test_completion_order_does_not_change_canonical_order(self):
        rows = [self.row(113, "linear"), self.row(101, "appraisal"), self.row(113, "appraisal")]
        forward = MODULE.canonical_sort_rows(rows)
        reverse = MODULE.canonical_sort_rows(reversed(rows))
        self.assertEqual(forward, reverse)

    def test_duplicate_identity_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "duplicate canonical row identity"):
            MODULE.canonical_sort_rows([self.row(101, "appraisal"), self.row(101, "appraisal")])

    def test_missing_identity_field_fails_closed(self):
        row = self.row(101, "appraisal")
        del row["stratum"]
        with self.assertRaisesRegex(ValueError, "missing canonical fields"):
            MODULE.canonical_sort_rows([row])


if __name__ == "__main__":
    unittest.main()
