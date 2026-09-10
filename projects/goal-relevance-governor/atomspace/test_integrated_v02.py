#!/usr/bin/env python3
"""Tests for Integrated Governor Pipeline v0.2 — multi-hop enrichment."""
import json, sys, os, unittest
sys.path.insert(0, os.path.dirname(__file__))
from integrated_governor import IntegratedGovernorPipeline

REPLAY_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')
ALL_EPISODES = [
    'episode_01_stale_codegen.json',
    'episode_02_chem_blocking.json',
    'episode_03_premature_hardening.json',
    'episode_04_overengineered_repair.json',
    'episode_05_control_justified_long_running.json',
    'episode_06_conflict_replan.json',
]

def load_episode(fname):
    with open(os.path.join(REPLAY_DIR, fname)) as f:
        return json.load(f)


class TestIntegratedV02(unittest.TestCase):

    def test_multihop_layer_present_in_output(self):
        """Every episode output should have a multihop_layer section."""
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=5)
                d = result.to_dict()
                self.assertIn('multihop_layer', d)
                self.assertIn('total_chains', d['multihop_layer'])
                self.assertIn('max_depth', d['multihop_layer'])

    def test_multihop_total_chains_positive(self):
        """Each episode should find at least one chain."""
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=5)
                d = result.to_dict()
                self.assertGreater(d['multihop_layer']['total_chains'], 0,
                    f"No chains in {fname}")

    def test_recommendations_have_multihop_fields(self):
        """Each recommendation should have multihop enrichment fields."""
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=5)
                d = result.to_dict()
                for rec in d['recommendations']:
                    self.assertIn('multihop_chains', rec)
                    self.assertIn('multihop_goal_coverage', rec)
                    self.assertIn('multihop_max_depth', rec)
                    self.assertGreaterEqual(rec['multihop_chains'], 0)
                    self.assertIsInstance(rec['multihop_goal_coverage'], list)

    def test_executive_summary_mentions_multihop(self):
        """Summary should mention multi-hop chain info."""
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=5)
                self.assertIn('Multi-hop', result.executive_summary)

    def test_verdicts_unchanged_from_v01(self):
        """Adding multi-hop enrichment should not change verdicts."""
        expected = {
            'episode_01_stale_codegen.json': {'STOP_STALE': 1},
            'episode_02_chem_blocking.json': {'ESCALATE': 1, 'PAUSE_RECOVERABLY': 1},
            'episode_03_premature_hardening.json': {'DEFER': 1},
            'episode_04_overengineered_repair.json': {'REPLAN': 2},
            'episode_05_control_justified_long_running.json': {'CONTINUE': 1},
            'episode_06_conflict_replan.json': {'REPLAN': 1, 'ESCALATE': 1},
        }
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=10)
                self.assertEqual(result.verdict_counts, expected[fname])

    def test_json_export_roundtrip(self):
        """Pipeline JSON export should be valid JSON with all layers."""
        data = load_episode('episode_02_chem_blocking.json')
        pipeline = IntegratedGovernorPipeline(data)
        s = pipeline.run_to_json(ecan_cycles=5)
        d = json.loads(s)
        self.assertIn('pln_layer', d)
        self.assertIn('ecan_layer', d)
        self.assertIn('verdict_layer', d)
        self.assertIn('multihop_layer', d)
        self.assertIn('recommendations', d)
        self.assertIn('executive_summary', d)

    def test_frozen_at_timestamp_used(self):
        """Pipeline should use frozen_at as the reference timestamp."""
        data = load_episode('episode_01_stale_codegen.json')
        frozen = data.get('frozen_at')
        self.assertIsNotNone(frozen, "Episode should have frozen_at")
        pipeline = IntegratedGovernorPipeline(data)
        # Check the timestamp in output matches frozen_at
        result = pipeline.run(ecan_cycles=5)
        # frozen_at may have 'Z' suffix; normalize
        expected_ts = frozen.replace('Z', '+00:00')
        self.assertEqual(result.timestamp, expected_ts)


if __name__ == '__main__':
    unittest.main()
