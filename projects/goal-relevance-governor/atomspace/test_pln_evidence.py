"""Tests for PLN evidence propagation (pln_propagation.py).

Verifies TruthValue algebra, edge confidence, propagation, and
verdict parity vs pure-Python evaluator on all 5 replay episodes.
"""

import json, os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'evaluator'))
sys.path.insert(0, os.path.dirname(__file__))

from pln_propagation import PLNPropagator, TruthValue, _edge_confidence, CONFIDENCE_MAP
from relevance_evaluator import Graph, RelevanceEvaluator

REPLAY_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')

EPISODES = [
    ('episode_01_stale_codegen.json', {'t-p2m-codegen': 'STOP_STALE'}),
    ('episode_02_chem_blocking.json', {'t-petta-chem': 'PAUSE_RECOVERABLY', 't-restore-agents': 'ESCALATE'}),
    ('episode_03_premature_hardening.json', {'t-hardening-guards': 'DEFER'}),
    ('episode_04_overengineered_repair.json', {'t-process-inspector': 'REPLAN', 't-launch-wrappers': 'REPLAN'}),
    ('episode_05_control_justified_long_running.json', {'t-run-benchmark': 'CONTINUE'}),
]

def load_episode(fname):
    with open(os.path.join(REPLAY_DIR, fname)) as f:
        return json.load(f)

class TestTruthValue(unittest.TestCase):
    def test_defaults(self):
        tv = TruthValue()
        self.assertEqual(tv.strength, 0.0)
        self.assertEqual(tv.confidence, 0.0)

    def test_conjunction(self):
        a, b = TruthValue(0.8, 0.9), TruthValue(0.6, 0.5)
        c = a.combine_conjunction(b)
        self.assertAlmostEqual(c.strength, 0.6)
        self.assertAlmostEqual(c.confidence, 0.45)

    def test_disjunction(self):
        a, b = TruthValue(0.8, 0.9), TruthValue(0.6, 0.5)
        c = a.combine_disjunction(b)
        self.assertAlmostEqual(c.strength, 0.8)
        self.assertAlmostEqual(c.confidence, 0.95)

    def test_negate(self):
        a = TruthValue(0.8, 0.9)
        c = a.negate()
        self.assertAlmostEqual(c.strength, 0.2)
        self.assertAlmostEqual(c.confidence, 0.9)

    def test_weighted_average(self):
        a, b = TruthValue(1.0, 1.0), TruthValue(0.0, 0.0)
        c = a.weighted_average(b, 0.7)
        self.assertAlmostEqual(c.strength, 0.7)

    def test_to_dict(self):
        tv = TruthValue(0.5, 0.75)
        self.assertEqual(tv.to_dict(), {"strength": 0.5, "confidence": 0.75})

class TestEdgeConfidence(unittest.TestCase):
    def test_high(self):
        self.assertAlmostEqual(_edge_confidence({"confidence": "high"}), CONFIDENCE_MAP["high"])
    def test_medium(self):
        self.assertAlmostEqual(_edge_confidence({"confidence": "medium"}), CONFIDENCE_MAP["medium"])
    def test_low(self):
        self.assertAlmostEqual(_edge_confidence({"confidence": "low"}), CONFIDENCE_MAP["low"])
    def test_default(self):
        self.assertAlmostEqual(_edge_confidence({}), CONFIDENCE_MAP["medium"])

class TestPLNPropagation(unittest.TestCase):
    def test_propagate_upward(self):
        data = load_episode('episode_01_stale_codegen.json')
        prop = PLNPropagator(data)
        prop.propagate_upward()
        self.assertTrue(len(prop.tvs) > 0)

    def test_propagate_downward(self):
        data = load_episode('episode_05_control_justified_long_running.json')
        prop = PLNPropagator(data)
        prop.propagate_upward()
        relevance = prop.propagate_downward()
        self.assertIn('t-run-benchmark', relevance)
        self.assertGreater(relevance['t-run-benchmark'], 0.0)

    def test_relevance_stale_task(self):
        data = load_episode('episode_01_stale_codegen.json')
        result = PLNPropagator(data).evaluate()
        tasks = {t['task_id']: t for t in result['tasks']}
        self.assertEqual(tasks['t-p2m-codegen']['suggested_verdict'], 'STOP_STALE')

    def test_relevance_healthy_task(self):
        data = load_episode('episode_05_control_justified_long_running.json')
        result = PLNPropagator(data).evaluate()
        tasks = {t['task_id']: t for t in result['tasks']}
        self.assertEqual(tasks['t-run-benchmark']['suggested_verdict'], 'CONTINUE')
        self.assertGreater(tasks['t-run-benchmark']['relevance_score'], 0.5)

    def test_result_has_relevance_score(self):
        for fname, _ in EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                result = PLNPropagator(data).evaluate()
                for t in result['tasks']:
                    self.assertIn('relevance_score', t)
                    self.assertIsInstance(t['relevance_score'], float)

    def test_result_has_signals(self):
        for fname, _ in EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                result = PLNPropagator(data).evaluate()
                for t in result['tasks']:
                    self.assertIn('signals', t)
                    self.assertIsInstance(t['signals'], list)

class TestCrossValidation(unittest.TestCase):
    def test_all_episodes_match_expected(self):
        for fname, expected in EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                pln = {t['task_id']: t['suggested_verdict']
                       for t in PLNPropagator(data).evaluate()['tasks']}
                for tid, verdict in expected.items():
                    self.assertEqual(pln.get(tid), verdict,
                                     f"{fname}: {tid} expected {verdict}, got {pln.get(tid)}")

    def test_pln_matches_python_evaluator(self):
        for fname, _ in EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                py = {v.task_id: v.verdict for v in RelevanceEvaluator(Graph(data)).evaluate_all()}
                pln = {t['task_id']: t['suggested_verdict']
                       for t in PLNPropagator(data).evaluate()['tasks']}
                for tid in set(py) & set(pln):
                    self.assertEqual(py[tid], pln[tid],
                                     f"{fname}: {tid} Python={py[tid]} PLN={pln[tid]}")

if __name__ == '__main__':
    unittest.main()
