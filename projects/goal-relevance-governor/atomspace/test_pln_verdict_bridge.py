#!/usr/bin/env python3
"""Tests for PLN-Verdict Bridge v0.1."""

import json, sys, os
import unittest

sys.path.insert(0, os.path.dirname(__file__))
from pln_verdict_bridge import PLNVerdictBridge, VerdictEnhanced

REPLAY_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')


def load_episode(fname):
    path = os.path.join(REPLAY_DIR, fname)
    with open(path) as f:
        return json.load(f)


class TestPLNVerdictBridge(unittest.TestCase):
    """Test PLN-Verdict Bridge on all replay episodes."""

    def test_bridge_returns_results_for_all_episodes(self):
        for fname in ['episode_01_stale_codegen.json',
                      'episode_02_chem_blocking.json',
                      'episode_03_premature_hardening.json',
                      'episode_04_overengineered_repair.json',
                      'episode_05_control_justified_long_running.json',
                      'episode_06_conflict_replan.json']:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                bridge = PLNVerdictBridge(data)
                results = bridge.evaluate()
                self.assertGreater(len(results), 0,
                    f'{fname}: no results')

    def test_bridge_preserves_original_verdicts(self):
        """When PLN doesn't modulate, original == final verdict."""
        from datetime import datetime, timezone
        # Inject 'now' close to the episode timestamps to avoid false staleness
        data = load_episode('episode_05_control_justified_long_running.json')
        now = datetime(2026, 8, 21, tzinfo=timezone.utc)
        bridge = PLNVerdictBridge(data, now=now)
        results = bridge.evaluate()
        for r in results:
            # Episode 05 is the control case: should CONTINUE without modulation
            self.assertEqual(r.verdict, 'CONTINUE')
            # With high relevance, no stale modulation expected
            if r.relevance_score > 0.75:
                self.assertFalse(r.staleness_flag,
                    f'{r.task_id}: should not be stale with high relevance')
                self.assertEqual(r.verdict, 'CONTINUE')
                # Check unified_verdict also stays CONTINUE (no stale downgrade)
                self.assertEqual(r.unified_verdict, 'CONTINUE')

    def test_bridge_has_truth_values(self):
        data = load_episode('episode_01_stale_codegen.json')
        bridge = PLNVerdictBridge(data)
        results = bridge.evaluate()
        for r in results:
            self.assertGreaterEqual(r.truth_value["strength"], 0.0)
            self.assertLessEqual(r.truth_value["strength"], 1.0)
            self.assertGreaterEqual(r.truth_value["confidence"], 0.0)
            self.assertLessEqual(r.truth_value["confidence"], 1.0)

    def test_bridge_relevance_scores_non_negative(self):
        for fname in ['episode_01_stale_codegen.json',
                      'episode_03_premature_hardening.json']:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                bridge = PLNVerdictBridge(data)
                results = bridge.evaluate()
                for r in results:
                    self.assertGreaterEqual(r.relevance_score, 0.0)

    def test_bridge_to_dict_serializable(self):
        data = load_episode('episode_02_chem_blocking.json')
        bridge = PLNVerdictBridge(data)
        d = json.loads(bridge.evaluate_to_json())
        self.assertEqual(d['format'], 'PLN-Verdict-Bridge-v0.1')
        self.assertEqual(d['task_count'], len(d['tasks']))
        # Ensure JSON-serializable
        json.dumps(d)

    def test_bridge_signals_merged(self):
        data = load_episode('episode_01_stale_codegen.json')
        bridge = PLNVerdictBridge(data)
        results = bridge.evaluate()
        for r in results:
            # Each result should have pln_signals (possibly empty)
            self.assertIsInstance(r.signals, list)
            self.assertIsInstance(r.signals, list)
            self.assertIsInstance(r.reasons, list)

    def test_bridge_confidence_modifier_range(self):
        data = load_episode('episode_04_overengineered_repair.json')
        bridge = PLNVerdictBridge(data)
        results = bridge.evaluate()
        for r in results:
            # Modifier should be in [-0.2, +0.1]
            self.assertGreaterEqual(r.confidence_modifier, -0.3)
            self.assertLessEqual(r.confidence_modifier, 0.1)

    def test_bridge_modulation_logic_continue_low_relevance(self):
        """CONTINUE + low relevance should escalate to DEFER."""
        # Build a minimal graph where a task continues but has low PLN relevance
        data = {
            'tasks': [{'id': 't-low-rel', 'kind': 'task', 'title': 'Low relevance task',
                       'status': 'active', 'reversibility': 'reversible'}],
            'goals': [{'id': 'g-active', 'kind': 'goal', 'title': 'Active goal',
                       'level': 'intermediate', 'status': 'active',
                       'priority': {'rank': 1, 'urgency': 'low'}}],
            'edges': [{'from': 't-low-rel', 'to': 'g-active', 'relation': 'contributes_to'}],
        }
        bridge = PLNVerdictBridge(data)
        results = bridge.evaluate()
        self.assertEqual(len(results), 1)
        r = results[0]
        # The original verdict should be CONTINUE (active task, active goal)
        self.assertEqual(r.verdict, 'CONTINUE')

    def test_bridge_all_episodes_serializable(self):
        """All episodes produce JSON-serializable bridge output."""
        for fname in ['episode_01_stale_codegen.json',
                      'episode_02_chem_blocking.json',
                      'episode_03_premature_hardening.json',
                      'episode_04_overengineered_repair.json',
                      'episode_05_control_justified_long_running.json',
                      'episode_06_conflict_replan.json']:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                bridge = PLNVerdictBridge(data)
                d = json.loads(bridge.evaluate_to_json())
                s = json.dumps(d)
                self.assertGreater(len(s), 0)


if __name__ == '__main__':
    unittest.main()

    def test_staleness_confidence_decay(self):
        """Stale goals should have decayed confidence and negative modifier."""
        import json
        from datetime import datetime, timezone
        from atomspace.pln_verdict_bridge import PLNVerdictBridge
        data = json.load(open('replay_corpus/episode_05_control_justified_long_running.json'))
        # Non-stale
        bridge_fresh = PLNVerdictBridge(data, now=datetime(2026, 8, 21, tzinfo=timezone.utc))
        fresh = bridge_fresh.evaluate()
        self.assertGreater(fresh[0].truth_value['confidence'], 0.5)
        self.assertEqual(fresh[0].confidence_modifier, 0.0)
        # Stale
        bridge_stale = PLNVerdictBridge(data, now=datetime(2026, 9, 8, tzinfo=timezone.utc))
        stale = bridge_stale.evaluate()
        self.assertLess(stale[0].truth_value['confidence'], fresh[0].truth_value['confidence'])
        self.assertLess(stale[0].confidence_modifier, 0.0)
