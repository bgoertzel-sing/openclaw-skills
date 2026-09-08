#!/usr/bin/env python3
"""Tests for Remediation Engine v0.1."""
import sys, os, json, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from atomspace.remediation_engine import RemediationEngine, RemediationPlan, RemediationStep
from atomspace.integrated_governor import IntegratedGovernorPipeline


class TestRemediationStep(unittest.TestCase):
    def test_creation(self):
        s = RemediationStep(step_id='s1', action='test', target='t1', description='d', priority=1)
        self.assertEqual(s.step_id, 's1')
        self.assertEqual(s.priority, 1)
        self.assertEqual(s.depends_on, [])

    def test_with_dependencies(self):
        s = RemediationStep(step_id='s2', action='test', target='t1', description='d',
                            priority=2, depends_on=['s1'])
        self.assertEqual(s.depends_on, ['s1'])


class TestRemediationPlan(unittest.TestCase):
    def test_to_dict(self):
        s = RemediationStep(step_id='s1', action='abandon', target='t1', description='d',
                            priority=1, verification='done')
        p = RemediationPlan(task_id='t1', verdict='STOP_STALE', plan_summary='test',
                           steps=[s], success_criteria='goal')
        d = p.to_dict()
        self.assertEqual(d['task_id'], 't1')
        self.assertEqual(d['verdict'], 'STOP_STALE')
        self.assertEqual(len(d['steps']), 1)
        self.assertEqual(d['steps'][0]['action'], 'abandon')
        self.assertEqual(d['steps'][0]['verification'], 'done')
        self.assertEqual(d['success_criteria'], 'goal')


class TestStopStale(unittest.TestCase):
    def setUp(self):
        d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(d, 'replay_corpus', 'episode_01_stale_codegen.json')) as f:
            self.data = json.load(f)
        self.pipeline = IntegratedGovernorPipeline(self.data)
        self.result = self.pipeline.run(ecan_cycles=10).to_dict()
        self.recs = self.result['recommendations']
        self.engine = RemediationEngine(self.data)

    def test_plan_generated(self):
        stale = [r for r in self.recs if r['unified_verdict'] == 'STOP_STALE']
        self.assertTrue(len(stale) > 0, 'Expected STOP_STALE in stale episode')
        for rec in stale:
            plan = self.engine.generate_plan(rec)
            self.assertEqual(plan.verdict, 'STOP_STALE')
            self.assertTrue(any(s.action == 'abandon_task' for s in plan.steps))

    def test_releases_resources(self):
        for rec in self.recs:
            if rec['task_id'] == 't-codegen':
                plan = self.engine.generate_plan(rec)
                release = [s for s in plan.steps if s.action == 'release_resource']
                res = self.engine.task_resources.get('t-codegen', [])
                if res:
                    self.assertEqual(len(release), len(res))
                break

    def test_notifies_stakeholders(self):
        stale = [r for r in self.recs if r['unified_verdict'] == 'STOP_STALE']
        for rec in stale:
            plan = self.engine.generate_plan(rec)
            notify = [s for s in plan.steps if s.action == 'notify_stakeholders']
            self.assertTrue(len(notify) > 0)
            self.assertEqual(notify[0].priority, 3)


class TestEscalate(unittest.TestCase):
    def setUp(self):
        self.escalate_recs = []
        d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        for ep in ['episode_01_stale_codegen.json', 'episode_02_chem_blocking.json',
                    'episode_03_premature_hardening.json', 'episode_04_overengineered_repair.json',
                    'episode_05_control_justified_long_running.json']:
            with open(os.path.join(d, 'replay_corpus', ep)) as f:
                data = json.load(f)
            pipeline = IntegratedGovernorPipeline(data)
            result = pipeline.run(ecan_cycles=10).to_dict()
            for rec in result['recommendations']:
                if rec['unified_verdict'] == 'ESCALATE':
                    self.escalate_recs.append((rec, data))

    def test_plan_generated(self):
        if not self.escalate_recs:
            self.skipTest('No ESCALATE verdicts')
        for rec, data in self.escalate_recs:
            engine = RemediationEngine(data)
            plan = engine.generate_plan(rec)
            self.assertEqual(plan.verdict, 'ESCALATE')
            actions = [s.action for s in plan.steps]
            self.assertIn('boost_priority', actions)
            self.assertIn('allocate_resources', actions)

    def test_priority_ordering(self):
        if not self.escalate_recs:
            self.skipTest('No ESCALATE verdicts')
        for rec, data in self.escalate_recs:
            engine = RemediationEngine(data)
            plan = engine.generate_plan(rec)
            boost = [s for s in plan.steps if s.action == 'boost_priority'][0]
            self.assertEqual(boost.priority, 1)


class TestPause(unittest.TestCase):
    def setUp(self):
        d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(d, 'replay_corpus', 'episode_02_chem_blocking.json')) as f:
            self.data = json.load(f)
        self.pipeline = IntegratedGovernorPipeline(self.data)
        self.result = self.pipeline.run(ecan_cycles=10).to_dict()
        self.recs = self.result['recommendations']
        self.engine = RemediationEngine(self.data)

    def test_plan_generated(self):
        pause = [r for r in self.recs if r['unified_verdict'] == 'PAUSE_RECOVERABLY']
        self.assertTrue(len(pause) > 0, 'Expected PAUSE_RECOVERABLY in chem blocking')
        for rec in pause:
            plan = self.engine.generate_plan(rec)
            self.assertEqual(plan.verdict, 'PAUSE_RECOVERABLY')
            self.assertIn('pause_task', [s.action for s in plan.steps])


class TestDefer(unittest.TestCase):
    def setUp(self):
        d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(d, 'replay_corpus', 'episode_03_premature_hardening.json')) as f:
            self.data = json.load(f)
        self.pipeline = IntegratedGovernorPipeline(self.data)
        self.result = self.pipeline.run(ecan_cycles=10).to_dict()
        self.recs = self.result['recommendations']
        self.engine = RemediationEngine(self.data)

    def test_plan_generated(self):
        defer = [r for r in self.recs if r['unified_verdict'] == 'DEFER']
        self.assertTrue(len(defer) > 0, 'Expected DEFER in premature hardening')
        for rec in defer:
            plan = self.engine.generate_plan(rec)
            self.assertEqual(plan.verdict, 'DEFER')
            self.assertIn('park_task', [s.action for s in plan.steps])


class TestContinue(unittest.TestCase):
    def setUp(self):
        d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(d, 'replay_corpus', 'episode_05_control_justified_long_running.json')) as f:
            self.data = json.load(f)
        self.pipeline = IntegratedGovernorPipeline(self.data)
        self.result = self.pipeline.run(ecan_cycles=10).to_dict()
        self.recs = self.result['recommendations']
        self.engine = RemediationEngine(self.data)

    def test_plan_generated(self):
        cont = [r for r in self.recs if r['unified_verdict'] == 'CONTINUE']
        self.assertTrue(len(cont) > 0, 'Expected CONTINUE in control episode')
        for rec in cont:
            plan = self.engine.generate_plan(rec)
            self.assertEqual(plan.verdict, 'CONTINUE')
            self.assertIn('monitor_task', [s.action for s in plan.steps])
            self.assertIn('set_checkpoint', [s.action for s in plan.steps])


class TestGenerateAll(unittest.TestCase):
    def setUp(self):
        d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(d, 'replay_corpus', 'episode_01_stale_codegen.json')) as f:
            self.data = json.load(f)
        self.pipeline = IntegratedGovernorPipeline(self.data)
        self.result = self.pipeline.run(ecan_cycles=10).to_dict()
        self.engine = RemediationEngine(self.data)

    def test_all_plans(self):
        plans = self.engine.generate_all(self.result['recommendations'])
        self.assertEqual(len(plans), len(self.result['recommendations']))
        for p in plans:
            self.assertIsInstance(p, RemediationPlan)
            self.assertTrue(p.steps)

    def test_to_dict_roundtrip(self):
        plans = self.engine.generate_all(self.result['recommendations'])
        for p in plans:
            d = p.to_dict()
            self.assertEqual(d['task_id'], p.task_id)
            self.assertEqual(d['verdict'], p.verdict)
            self.assertEqual(len(d['steps']), len(p.steps))


class TestUnknownVerdict(unittest.TestCase):
    def test_unknown(self):
        d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(d, 'replay_corpus', 'episode_01_stale_codegen.json')) as f:
            data = json.load(f)
        engine = RemediationEngine(data)
        plan = engine.generate_plan({'task_id': 'x', 'unified_verdict': 'BOGUS', 'signals': []})
        self.assertEqual(plan.verdict, 'BOGUS')
        self.assertEqual(plan.steps, [])


if __name__ == '__main__':
    unittest.main()
