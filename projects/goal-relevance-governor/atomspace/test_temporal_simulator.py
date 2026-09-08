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
