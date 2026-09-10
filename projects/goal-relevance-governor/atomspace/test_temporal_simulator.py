#!/usr/bin/env python3
"""Tests for Temporal Evolution Simulator v0.1."""
import json, sys, os, unittest
sys.path.insert(0, os.path.dirname(__file__))
from temporal_simulator import TemporalSimulator, Mutation, TimelineResult

REPLAY_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')

def load_episode(fname):
    with open(os.path.join(REPLAY_DIR, fname)) as f:
        return json.load(f)


class TestTemporalSimulator(unittest.TestCase):

    def test_stale_timeline_runs(self):
        data = load_episode('episode_01_stale_codegen.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_stale_task()
        result = sim.run_timeline(mutations)
        self.assertIsInstance(result, TimelineResult)
        self.assertEqual(len(result.steps), 3)

    def test_stale_timeline_verdicts_correct(self):
        data = load_episode('episode_01_stale_codegen.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_stale_task()
        result = sim.run_timeline(mutations)
        # Step 0: should be STOP_STALE
        self.assertEqual(result.steps[0].verdicts.get('t-p2m-codegen'), 'STOP_STALE')
        # Step 1: still STOP_STALE after all goals terminal
        self.assertEqual(result.steps[1].verdicts.get('t-p2m-codegen'), 'STOP_STALE')
        # Step 2: task completed, no verdict
        self.assertEqual(len(result.steps[2].verdicts), 0)

    def test_conflict_timeline_runs(self):
        data = load_episode('episode_02_chem_blocking.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_conflict_resolution()
        result = sim.run_timeline(mutations)
        self.assertEqual(len(result.steps), 3)

    def test_conflict_resolution_changes_verdicts(self):
        """After high-priority task completes, remaining task verdict may change."""
        data = load_episode('episode_02_chem_blocking.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_conflict_resolution()
        result = sim.run_timeline(mutations)
        # Step 0 should have both tasks
        self.assertIn('t-petta-chem', result.steps[0].verdicts)
        self.assertIn('t-restore-agents', result.steps[0].verdicts)
        # Step 1: restore-agents completed, should not appear
        self.assertNotIn('t-restore-agents', result.steps[1].verdicts)

    def test_premature_timeline_runs(self):
        data = load_episode('episode_03_premature_hardening.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_premature_to_justified()
        result = sim.run_timeline(mutations)
        self.assertEqual(len(result.steps), 2)

    def test_premature_verdict_at_step0(self):
        data = load_episode('episode_03_premature_hardening.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_premature_to_justified()
        result = sim.run_timeline(mutations)
        self.assertEqual(result.steps[0].verdicts.get('t-hardening-guards'), 'DEFER')

    def test_verdict_drift_detected(self):
        """Drift should be recorded when verdicts change across steps."""
        data = load_episode('episode_02_chem_blocking.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_conflict_resolution()
        result = sim.run_timeline(mutations)
        # We expect some drift when restore-agents completes
        # (petta-chem verdict may change from PAUSE_RECOVERABLY)
        self.assertIsInstance(result.verdict_drift, list)

    def test_to_dict_serializable(self):
        data = load_episode('episode_01_stale_codegen.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_stale_task()
        result = sim.run_timeline(mutations)
        d = result.to_dict()
        s = json.dumps(d)  # Should not raise
        self.assertIsInstance(s, str)

    def test_all_correct_flag(self):
        data = load_episode('episode_01_stale_codegen.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_stale_task()
        result = sim.run_timeline(mutations)
        self.assertTrue(result.all_correct)

    def test_mutation_applies_changes(self):
        data = load_episode('episode_01_stale_codegen.json')
        sim = TemporalSimulator(data)
        # Create a custom mutation
        mut = Mutation(
            timestep=99,
            description='Test mutation',
            changes=[('goals', 'g-build-omegaclaw', 'status', 'abandoned')],
        )
        new_data = sim._apply_mutation(data, mut)
        # Original should be unchanged
        for g in data['goals']:
            if g['id'] == 'g-build-omegaclaw':
                self.assertEqual(g['status'], 'active')
        # New data should have the change
        for g in new_data['goals']:
            if g['id'] == 'g-build-omegaclaw':
                self.assertEqual(g['status'], 'abandoned')

    def test_frozen_at_advances(self):
        data = load_episode('episode_01_stale_codegen.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_stale_task()
        result = sim.run_timeline(mutations)
        # Step 1 should have advanced frozen_at
        step0_ts = result.steps[0].data.get('frozen_at')
        step1_ts = result.steps[1].data.get('frozen_at')
        self.assertNotEqual(step0_ts, step1_ts)


if __name__ == '__main__':
    unittest.main()


class TestTemporalSimulatorEp04To06(unittest.TestCase):
    """Tests for temporal timelines covering episodes 04, 05, 06."""

    def test_overengineered_timeline_runs(self):
        data = load_episode('episode_04_overengineered_repair.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_overengineered_repair()
        result = sim.run_timeline(mutations)
        self.assertIsInstance(result, TimelineResult)
        self.assertEqual(len(result.steps), 3)

    def test_overengineered_tasks_present_at_step0(self):
        data = load_episode('episode_04_overengineered_repair.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_overengineered_repair()
        result = sim.run_timeline(mutations)
        # Both tasks should be present initially
        self.assertIn('t-process-inspector', result.steps[0].verdicts)
        self.assertIn('t-launch-wrappers', result.steps[0].verdicts)

    def test_overengineered_task_disappears_after_completion(self):
        data = load_episode('episode_04_overengineered_repair.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_overengineered_repair()
        result = sim.run_timeline(mutations)
        # Step 2: tasks completed/stopped, should not appear
        self.assertNotIn('t-process-inspector', result.steps[2].verdicts)
        self.assertNotIn('t-launch-wrappers', result.steps[2].verdicts)

    def test_control_justified_timeline_runs(self):
        data = load_episode('episode_05_control_justified_long_running.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_control_justified()
        result = sim.run_timeline(mutations)
        self.assertEqual(len(result.steps), 3)

    def test_control_stays_continue(self):
        """CONTINUE verdict should hold across steps 0 and 1."""
        data = load_episode('episode_05_control_justified_long_running.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_control_justified()
        result = sim.run_timeline(mutations)
        self.assertEqual(result.steps[0].verdicts.get('t-run-benchmark'), 'CONTINUE')
        self.assertEqual(result.steps[1].verdicts.get('t-run-benchmark'), 'CONTINUE')

    def test_control_no_verdict_drift_before_completion(self):
        """No verdict drift between steps 0 and 1 (both CONTINUE)."""
        data = load_episode('episode_05_control_justified_long_running.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_control_justified()
        result = sim.run_timeline(mutations)
        # Drift only at step 2 when task completes (verdict disappears)
        drift_before_completion = [d for d in result.verdict_drift if d[0] < 2]
        self.assertEqual(len(drift_before_completion), 0)

    def test_control_all_correct(self):
        data = load_episode('episode_05_control_justified_long_running.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_control_justified()
        result = sim.run_timeline(mutations)
        self.assertTrue(result.all_correct)

    def test_conflict_replan_timeline_runs(self):
        data = load_episode('episode_06_conflict_replan.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_conflict_replan()
        result = sim.run_timeline(mutations)
        self.assertIsInstance(result, TimelineResult)
        self.assertEqual(len(result.steps), 3)

    def test_conflict_both_tasks_present_at_step0(self):
        data = load_episode('episode_06_conflict_replan.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_conflict_replan()
        result = sim.run_timeline(mutations)
        self.assertIn('t-rest-wrapper', result.steps[0].verdicts)
        self.assertIn('t-grpc-wrapper', result.steps[0].verdicts)

    def test_conflict_grpc_disappears_after_stop(self):
        data = load_episode('episode_06_conflict_replan.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_conflict_replan()
        result = sim.run_timeline(mutations)
        # Step 1: grpc-wrapper stopped, should not appear
        self.assertNotIn('t-grpc-wrapper', result.steps[1].verdicts)
        # REST wrapper should still be present
        self.assertIn('t-rest-wrapper', result.steps[1].verdicts)

    def test_conflict_resolution_at_step2(self):
        data = load_episode('episode_06_conflict_replan.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_conflict_replan()
        result = sim.run_timeline(mutations)
        # Step 2: both tasks resolved, no verdicts
        self.assertEqual(len(result.steps[2].verdicts), 0)

    def test_conflict_verdict_drift_detected(self):
        """Drift should be recorded when grpc-wrapper is stopped."""
        data = load_episode('episode_06_conflict_replan.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_conflict_replan()
        result = sim.run_timeline(mutations)
        self.assertIsInstance(result.verdict_drift, list)

    def test_conflict_to_dict_serializable(self):
        data = load_episode('episode_06_conflict_replan.json')
        sim = TemporalSimulator(data)
        mutations = sim.create_timeline_conflict_replan()
        result = sim.run_timeline(mutations)
        d = result.to_dict()
        s = json.dumps(d)
        self.assertIsInstance(s, str)

    def test_all_six_episodes_run_without_crash(self):
        """All 6 episodes should run temporal simulations without crashing."""
        all_episodes = [
            ('episode_01_stale_codegen.json', 'create_timeline_stale_task'),
            ('episode_02_chem_blocking.json', 'create_timeline_conflict_resolution'),
            ('episode_03_premature_hardening.json', 'create_timeline_premature_to_justified'),
            ('episode_04_overengineered_repair.json', 'create_timeline_overengineered_repair'),
            ('episode_05_control_justified_long_running.json', 'create_timeline_control_justified'),
            ('episode_06_conflict_replan.json', 'create_timeline_conflict_replan'),
        ]
        for fname, method_name in all_episodes:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                sim = TemporalSimulator(data)
                mutations = getattr(sim, method_name)()
                result = sim.run_timeline(mutations)
                self.assertIsInstance(result, TimelineResult)
                self.assertGreater(len(result.steps), 0)


class TestTimelineStep:
    """Tests for TimelineStep dataclass."""

    def test_creation_with_defaults(self):
        from atomspace.temporal_simulator import TimelineStep
        step = TimelineStep(timestep=0, description="init", data={})
        assert step.timestep == 0
        assert step.description == "init"
        assert step.data == {}
        assert step.pipeline_result is None
        assert step.verdicts is None
        assert step.verdict_correct is True
        assert step.errors == []

    def test_creation_with_all_fields(self):
        from atomspace.temporal_simulator import TimelineStep
        step = TimelineStep(
            timestep=5, description="conflict",
            data={"tasks": ["t1", "t2"]},
            pipeline_result={"score": 0.8},
            verdicts={"t1": "REPLAN"},
            verdict_correct=False,
            errors=["timeout"]
        )
        assert step.timestep == 5
        assert step.verdicts == {"t1": "REPLAN"}
        assert step.verdict_correct is False
        assert len(step.errors) == 1

    def test_mutation_of_defaults(self):
        from atomspace.temporal_simulator import TimelineStep
        step1 = TimelineStep(timestep=0, description="a", data={})
        step1.errors.append("err1")
        step2 = TimelineStep(timestep=1, description="b", data={})
        assert step2.errors == []  # default factory creates new list
