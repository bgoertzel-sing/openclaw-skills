#!/usr/bin/env python3
"""Tests for Reasoning Explanation Layer v0.1."""
import json, sys, os, unittest
sys.path.insert(0, os.path.dirname(__file__))
from reasoning_explainer import ReasoningExplainer, TaskExplanation
from integrated_governor import IntegratedGovernorPipeline

REPLAY_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')
ALL_EPISODES = [
    'episode_01_stale_codegen.json',
    'episode_02_chem_blocking.json',
    'episode_03_premature_hardening.json',
    'episode_04_overengineered_repair.json',
    'episode_05_control_justified_long_running.json',
]

def load_episode(fname):
    with open(os.path.join(REPLAY_DIR, fname)) as f:
        return json.load(f)


class TestReasoningExplainer(unittest.TestCase):

    def test_explains_all_episodes(self):
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=5)
                d = result.to_dict()
                explainer = ReasoningExplainer(data)
                explanations = explainer.explain_all(d)
                self.assertGreater(len(explanations), 0)

    def test_explanation_has_required_fields(self):
        data = load_episode('episode_02_chem_blocking.json')
        pipeline = IntegratedGovernorPipeline(data)
        d = pipeline.run(ecan_cycles=5).to_dict()
        explainer = ReasoningExplainer(data)
        explanations = explainer.explain_all(d)
        for exp in explanations:
            self.assertIsInstance(exp, TaskExplanation)
            self.assertTrue(exp.task_id)
            self.assertTrue(exp.verdict)
            self.assertTrue(exp.headline)
            self.assertIsInstance(exp.evidence_points, list)
            self.assertGreater(len(exp.evidence_points), 0)
            self.assertTrue(exp.chain_summary)
            self.assertTrue(exp.recommended_action)
            self.assertTrue(exp.confidence_note)

    def test_verdict_headlines_correct(self):
        data = load_episode('episode_01_stale_codegen.json')
        pipeline = IntegratedGovernorPipeline(data)
        d = pipeline.run(ecan_cycles=5).to_dict()
        explainer = ReasoningExplainer(data)
        explanations = explainer.explain_all(d)
        self.assertEqual(len(explanations), 1)
        self.assertIn('stale', explanations[0].headline.lower())

    def test_conflict_summary_populated(self):
        """Episode 02 has resource conflict - explanation should mention it."""
        data = load_episode('episode_02_chem_blocking.json')
        pipeline = IntegratedGovernorPipeline(data)
        d = pipeline.run(ecan_cycles=5).to_dict()
        explainer = ReasoningExplainer(data)
        explanations = explainer.explain_all(d)
        has_conflict = any(e.conflict_summary for e in explanations)
        self.assertTrue(has_conflict, 'Expected at least one task with conflict summary')

    def test_no_conflict_summary_in_control(self):
        """Episode 05 has no conflicts - no conflict summary expected."""
        data = load_episode('episode_05_control_justified_long_running.json')
        pipeline = IntegratedGovernorPipeline(data)
        d = pipeline.run(ecan_cycles=5).to_dict()
        explainer = ReasoningExplainer(data)
        explanations = explainer.explain_all(d)
        for exp in explanations:
            self.assertEqual(exp.conflict_summary, '')

    def test_chain_summary_mentions_goals(self):
        data = load_episode('episode_02_chem_blocking.json')
        pipeline = IntegratedGovernorPipeline(data)
        d = pipeline.run(ecan_cycles=5).to_dict()
        explainer = ReasoningExplainer(data)
        explanations = explainer.explain_all(d)
        for exp in explanations:
            self.assertIn('chain', exp.chain_summary.lower())

    def test_markdown_output_valid(self):
        data = load_episode('episode_02_chem_blocking.json')
        pipeline = IntegratedGovernorPipeline(data)
        d = pipeline.run(ecan_cycles=5).to_dict()
        explainer = ReasoningExplainer(data)
        md = explainer.explain_to_markdown(d)
        self.assertIn('###', md)
        self.assertIn('Evidence:', md)
        self.assertIn('Action:', md)

    def test_json_output_valid(self):
        data = load_episode('episode_03_premature_hardening.json')
        pipeline = IntegratedGovernorPipeline(data)
        d = pipeline.run(ecan_cycles=5).to_dict()
        explainer = ReasoningExplainer(data)
        s = explainer.explain_to_json(d)
        parsed = json.loads(s)
        self.assertIsInstance(parsed, list)
        self.assertGreater(len(parsed), 0)
        self.assertIn('task_id', parsed[0])
        self.assertIn('evidence_points', parsed[0])

    def test_signal_interpretation(self):
        """Known signals should produce human-readable interpretations."""
        data = load_episode('episode_02_chem_blocking.json')
        explainer = ReasoningExplainer(data)
        # Test specific signal interpretations
        result = explainer._interpret_signal('resource_contention', {})
        self.assertIn('Resource contention', result)
        result = explainer._interpret_signal('no_evidence_produced', {})
        self.assertIn('No evidence', result)
        result = explainer._interpret_signal('justified_long_running', {})
        self.assertIn('justified', result.lower())

    def test_evidence_points_nonempty_for_all(self):
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                pipeline = IntegratedGovernorPipeline(data)
                d = pipeline.run(ecan_cycles=5).to_dict()
                explainer = ReasoningExplainer(data)
                explanations = explainer.explain_all(d)
                for exp in explanations:
                    self.assertGreater(len(exp.evidence_points), 2,
                        f'{exp.task_id} in {fname} has too few evidence points')


if __name__ == '__main__':
    unittest.main()
