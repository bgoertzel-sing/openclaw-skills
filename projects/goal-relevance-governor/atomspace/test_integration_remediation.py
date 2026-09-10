#!/usr/bin/env python3
"""Integration test: full pipeline -> remediation plans for all episodes."""
import sys, os, json, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from atomspace.integrated_governor import IntegratedGovernorPipeline
from atomspace.remediation_engine import RemediationEngine, RemediationPlan


REPLAY_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'replay_corpus')


class TestFullPipelineRemediation(unittest.TestCase):
    """Every recommendation from every episode must produce a valid remediation plan."""

    @classmethod
    def setUpClass(cls):
        cls.episodes = {}
        for fn in sorted(os.listdir(REPLAY_DIR)):
            if fn.startswith('episode_') and fn.endswith('.json'):
                with open(os.path.join(REPLAY_DIR, fn)) as f:
                    cls.episodes[fn] = json.load(f)

    def test_all_episodes_have_plans(self):
        for ep_name, data in self.episodes.items():
            with self.subTest(episode=ep_name):
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=10).to_dict()
                engine = RemediationEngine(data)
                plans = engine.generate_all(result['recommendations'])
                self.assertEqual(len(plans), len(result['recommendations']))
                for p in plans:
                    self.assertIsInstance(p, RemediationPlan)
                    self.assertTrue(p.steps, f'{ep_name}: empty steps for {p.task_id}')
                    self.assertTrue(p.plan_summary)
                    self.assertIn(p.verdict, [
                        'STOP_STALE', 'ESCALATE', 'PAUSE_RECOVERABLY',
                        'DEFER', 'REPLAN', 'CONTINUE', 'BLOCKED'
                    ])

    def test_step_ids_unique_per_plan(self):
        for ep_name, data in self.episodes.items():
            with self.subTest(episode=ep_name):
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=10).to_dict()
                engine = RemediationEngine(data)
                for rec in result['recommendations']:
                    plan = engine.generate_plan(rec)
                    ids = [s.step_id for s in plan.steps]
                    self.assertEqual(len(ids), len(set(ids)),
                        f'{ep_name}/{rec["task_id"]}: duplicate step_ids {ids}')

    def test_dependency_chain_valid(self):
        """Every depends_on reference must point to an existing step_id."""
        for ep_name, data in self.episodes.items():
            with self.subTest(episode=ep_name):
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=10).to_dict()
                engine = RemediationEngine(data)
                for rec in result['recommendations']:
                    plan = engine.generate_plan(rec)
                    all_ids = {s.step_id for s in plan.steps}
                    for step in plan.steps:
                        for dep in step.depends_on:
                            self.assertIn(dep, all_ids,
                                f'{ep_name}/{rec["task_id"]}: step {step.step_id} depends on '
                                f'nonexistent {dep}')

    def test_priority_range(self):
        """All priorities must be in 1-4 range."""
        for ep_name, data in self.episodes.items():
            with self.subTest(episode=ep_name):
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=10).to_dict()
                engine = RemediationEngine(data)
                for rec in result['recommendations']:
                    plan = engine.generate_plan(rec)
                    for step in plan.steps:
                        self.assertTrue(1 <= step.priority <= 4,
                            f'{ep_name}/{rec["task_id"]}: priority {step.priority} out of range')

    def test_to_dict_serializable(self):
        """All plans must be JSON-serializable."""
        for ep_name, data in self.episodes.items():
            with self.subTest(episode=ep_name):
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=10).to_dict()
                engine = RemediationEngine(data)
                plans = engine.generate_all(result['recommendations'])
                serialized = json.dumps([p.to_dict() for p in plans])
                self.assertTrue(len(serialized) > 10)

    def test_verdict_specific_actions(self):
        """Each verdict must include its signature action."""
        expected = {
            'STOP_STALE': 'abandon_task',
            'ESCALATE': 'boost_priority',
            'PAUSE_RECOVERABLY': 'pause_task',
            'DEFER': 'park_task',
            'REPLAN': 'redesign_task',
            'CONTINUE': 'monitor_task',
        }
        for ep_name, data in self.episodes.items():
            with self.subTest(episode=ep_name):
                pipeline = IntegratedGovernorPipeline(data)
                result = pipeline.run(ecan_cycles=10).to_dict()
                engine = RemediationEngine(data)
                for rec in result['recommendations']:
                    plan = engine.generate_plan(rec)
                    if plan.verdict in expected:
                        sig = expected[plan.verdict]
                        actions = [s.action for s in plan.steps]
                        self.assertIn(sig, actions,
                            f'{ep_name}/{rec["task_id"]}: {plan.verdict} missing {sig}')

    def test_exported_plans_file_exists(self):
        """remediation_plans_all.json should exist and be valid."""
        path = os.path.join(REPLAY_DIR, 'remediation_plans_all.json')
        self.assertTrue(os.path.exists(path), 'remediation_plans_all.json missing')
        with open(path) as f:
            data = json.load(f)
        self.assertTrue(len(data) >= 5, 'Expected at least 5 episodes in export')


if __name__ == '__main__':
    unittest.main()
