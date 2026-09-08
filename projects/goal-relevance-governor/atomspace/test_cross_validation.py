"""
Cross-validation test: PLNPropagator vs Python RelevanceEvaluator.
Runs all 5 replay episodes through both engines and checks verdict parity.
"""
import json
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'evaluator'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'atomspace'))

from relevance_evaluator import Graph, RelevanceEvaluator
from pln_propagation import PLNPropagator


REPLAY_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')

EPISODES = [
    ('episode_01_stale_codegen.json', {
        't-p2m-codegen': 'STOP_STALE',
    }),
    ('episode_02_chem_blocking.json', {
        't-petta-chem': 'PAUSE_RECOVERABLY',
        't-restore-agents': 'ESCALATE',
    }),
    ('episode_03_premature_hardening.json', {
        't-hardening-guards': 'DEFER',
    }),
    ('episode_04_overengineered_repair.json', {
        't-process-inspector': 'REPLAN',
        't-launch-wrappers': 'REPLAN',
    }),
    ('episode_05_control_justified_long_running.json', {
        't-run-benchmark': 'CONTINUE',
    }),
]


def load_episode(fname):
    path = os.path.join(REPLAY_DIR, fname)
    with open(path) as f:
        return json.load(f)


def get_py_verdicts(data):
    g = Graph(data)
    ev = RelevanceEvaluator(g)
    return {v.task_id: v.verdict for v in ev.evaluate_all()}


def get_pln_verdicts(data):
    prop = PLNPropagator(data)
    result = prop.evaluate()
    return {t['task_id']: t['suggested_verdict'] for t in result['tasks']}


class TestCrossValidation(unittest.TestCase):
    """Verify PLNPropagator verdicts match Python evaluator on all replay episodes."""

    def test_all_episodes_match_expected(self):
        """Each episode produces the expected verdicts from the corpus."""
        for fname, expected in EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                pln = get_pln_verdicts(data)
                for tid, verdict in expected.items():
                    self.assertIn(tid, pln, f'{tid} missing from PLN results in {fname}')
                    self.assertEqual(pln[tid], verdict,
                        f'{fname}: {tid} expected {verdict}, got {pln[tid]}')

    def test_pln_matches_python_evaluator(self):
        """PLNPropagator verdicts match RelevanceEvaluator on every active task."""
        for fname, _ in EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                pln = get_pln_verdicts(data)
                py = get_py_verdicts(data)
                # All task IDs present in both
                all_tids = set(pln.keys()) | set(py.keys())
                self.assertEqual(pln, py,
                    f'{fname}: PLN={pln} != PY={py}')

    def test_pln_relevance_scores_present(self):
        """Each PLN result has a non-negative relevance score."""
        for fname, _ in EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                prop = PLNPropagator(data)
                result = prop.evaluate()
                for t in result['tasks']:
                    self.assertGreaterEqual(t['relevance_score'], 0.0,
                        f"{fname}: {t['task_id']} has negative relevance")
                    self.assertIn('suggested_verdict', t)
                    self.assertIn('signals', t)
                    self.assertIsInstance(t['signals'], list)

    def test_truth_values_propagated(self):
        """Truth values are present and in [0,1] range."""
        for fname, _ in EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                prop = PLNPropagator(data)
                result = prop.evaluate()
                for t in result['tasks']:
                    tv = t['truth_value']
                    self.assertIn('strength', tv)
                    self.assertIn('confidence', tv)
                    self.assertGreaterEqual(tv['strength'], 0.0)
                    self.assertLessEqual(tv['strength'], 1.0)
                    self.assertGreaterEqual(tv['confidence'], 0.0)
                    self.assertLessEqual(tv['confidence'], 1.0)


if __name__ == '__main__':
    unittest.main()
