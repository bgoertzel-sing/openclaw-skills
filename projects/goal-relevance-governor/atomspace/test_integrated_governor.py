#!/usr/bin/env python3
"""Tests for Integrated Governor Pipeline v0.1."""
import json, sys, os
import unittest
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(__file__))
from integrated_governor import IntegratedGovernorPipeline, IntegratedGovernorResult, TaskRecommendation

REPLAY_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')

def load_episode(fname):
    with open(os.path.join(REPLAY_DIR, fname)) as f:
        return json.load(f)

ALL_EPISODES = [
    'episode_01_stale_codegen.json',
    'episode_02_chem_blocking.json',
    'episode_03_premature_hardening.json',
    'episode_04_overengineered_repair.json',
    'episode_05_control_justified_long_running.json',
    'episode_06_conflict_replan.json',
]


class TestIntegratedGovernor(unittest.TestCase):

    def test_pipeline_runs_all_episodes(self):
        now = datetime(2026, 9, 8, tzinfo=timezone.utc)
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                pipeline = IntegratedGovernorPipeline(data, now=now)
                result = pipeline.run(ecan_cycles=5)
                self.assertIsInstance(result, IntegratedGovernorResult)

    def test_recommendations_sorted_by_sti(self):
        data = load_episode('episode_02_chem_blocking.json')
        pipeline = IntegratedGovernorPipeline(data)
        result = pipeline.run(ecan_cycles=5)
        for i in range(len(result.recommendations) - 1):
            self.assertGreaterEqual(
                result.recommendations[i].sti,
                result.recommendations[i+1].sti
            )

    def test_verdict_counts_match_recommendations(self):
        data = load_episode('episode_05_control_justified_long_running.json')
        pipeline = IntegratedGovernorPipeline(data)
        result = pipeline.run(ecan_cycles=3)
        total = sum(result.verdict_counts.values())
        self.assertEqual(total, len(result.recommendations))

    def test_executive_summary_nonempty(self):
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=5)
                self.assertGreater(len(result.executive_summary), 20)

    def test_json_export(self):
        data = load_episode('episode_02_chem_blocking.json')
        pipeline = IntegratedGovernorPipeline(data)
        s = pipeline.run_to_json(ecan_cycles=3)
        d = json.loads(s)
        self.assertIn('recommendations', d)
        self.assertIn('executive_summary', d)
        self.assertIn('pln_layer', d)
        self.assertIn('ecan_layer', d)
        self.assertIn('verdict_layer', d)

    def test_recommendation_has_action(self):
        data = load_episode('episode_01_stale_codegen.json')
        pipeline = IntegratedGovernorPipeline(data)
        result = pipeline.run(ecan_cycles=3)
        for rec in result.recommendations:
            self.assertGreater(len(rec.recommended_action), 5)

    def test_top_priority_is_highest_sti(self):
        data = load_episode('episode_02_chem_blocking.json')
        pipeline = IntegratedGovernorPipeline(data)
        result = pipeline.run(ecan_cycles=5)
        if result.recommendations:
            top = result.recommendations[0]
            for rec in result.recommendations[1:]:
                self.assertGreaterEqual(top.sti, rec.sti)


if __name__ == '__main__':
    unittest.main()
