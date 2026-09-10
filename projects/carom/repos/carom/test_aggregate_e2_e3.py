import unittest

from aggregate_e2_e3 import example_rows, summarize_result


class AggregateE2E3Test(unittest.TestCase):
    def test_nested_rows_override_cached_top_level_aggregates(self):
        result = {
            "arm": "e2_full",
            "seed": 7,
            "slot_accuracy": 0.0,
            "metrics": {
                "slot_accuracy": 0.0,
                "rows": [
                    {
                        "slot_accuracy": 1.0,
                        "exact_workspace": True,
                        "revisits": 1,
                        "terminal_trapping": False,
                        "integrated_activity_mass": 2.0,
                        "integrated_workspace_update_norm": 3.0,
                        "integrated_exposure": [1.0, 2.0],
                    },
                    {
                        "slot_accuracy": 0.5,
                        "exact_workspace": False,
                        "revisits": 0,
                        "terminal_trapping": True,
                        "integrated_activity_mass": 4.0,
                        "integrated_workspace_update_norm": 5.0,
                        "integrated_exposure": [2.0, 3.0],
                    },
                ],
            },
        }
        summary = summarize_result(result)
        self.assertEqual(summary["slot_accuracy"], 0.75)
        self.assertEqual(summary["exact_workspace"], 0.5)
        self.assertEqual(summary["revisit_fraction"], 0.5)
        self.assertEqual(summary["total_integrated_exposure"], 4.0)

    def test_metrics_list_format(self):
        rows = [{"slot_accuracy": 1.0}]
        self.assertIs(example_rows({"metrics": rows}), rows)


if __name__ == "__main__":
    unittest.main()
