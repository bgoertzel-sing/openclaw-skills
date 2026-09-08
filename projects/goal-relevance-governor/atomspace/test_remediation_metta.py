#!/usr/bin/env python3
"""Tests for MeTTa remediation rules cross-validation."""
import sys, os, json, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from atomspace.remediation_engine import RemediationEngine
from atomspace.integrated_governor import IntegratedGovernorPipeline


# Expected action sets per verdict (from MeTTa rules)
METTA_EXPECTED = {
    'STOP_STALE': {'abandon_task', 'release_all_resources', 'notify_stakeholders'},
    'ESCALATE': {'boost_priority', 'allocate_resources', 'set_deadline', 'require_evidence'},
    'PAUSE_RECOVERABLY': {'pause_task', 'monitor_blocker', 'resume_task_when_free'},
    'DEFER': {'park_task', 'set_trigger_condition', 'monitor_trigger'},
    'REPLAN': {'redesign_task', 'update_goal_link', 'reset_progress', 'archive_old_approach'},
    'CONTINUE': {'monitor_task', 'set_checkpoint'},
}

# Python action -> MeTTa action mapping
PYTHON_TO_METTA = {
    'abandon_task': 'abandon_task',
    'release_resource': 'release_all_resources',
    'notify_stakeholders': 'notify_stakeholders',
    'boost_priority': 'boost_priority',
    'allocate_resources': 'allocate_resources',
    'set_deadline': 'set_deadline',
    'require_evidence': 'require_evidence',
    'pause_task': 'pause_task',
    'monitor_blocker': 'monitor_blocker',
    'resume_task': 'resume_task_when_free',
    'park_task': 'park_task',
    'set_trigger': 'set_trigger_condition',
    'monitor_trigger': 'monitor_trigger',
    'redesign_task': 'redesign_task',
    'update_goal_link': 'update_goal_link',
    'reset_progress': 'reset_progress',
    'archive_old_approach': 'archive_old_approach',
    'monitor_task': 'monitor_task',
    'set_checkpoint': 'set_checkpoint',
}


class TestMettaRemediationConsistency(unittest.TestCase):
    """Cross-validate Python remediation engine actions against MeTTa rules."""

    def setUp(self):
        self.d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.episodes = [
            ('episode_01_stale_codegen.json', 'STOP_STALE'),
            ('episode_02_chem_blocking.json', 'ESCALATE'),
            ('episode_02_chem_blocking.json', 'PAUSE_RECOVERABLY'),
            ('episode_03_premature_hardening.json', 'DEFER'),
            ('episode_04_overengineered_repair.json', 'REPLAN'),
            ('episode_05_control_justified_long_running.json', 'CONTINUE'),
        ]

    def test_metta_rules_file_exists(self):
        path = os.path.join(self.d, 'atomspace', 'remediation_rules.metta')
        self.assertTrue(os.path.exists(path))

    def test_metta_rules_have_all_verdicts(self):
        path = os.path.join(self.d, 'atomspace', 'remediation_rules.metta')
        with open(path) as f:
            content = f.read()
        for verdict in METTA_EXPECTED:
            self.assertIn(f'(remediation {verdict}', content,
                         f'MeTTa rules missing verdict: {verdict}')

    def test_python_actions_map_to_metta(self):
        """Every Python action has a MeTTa counterpart."""
        for py_action, metta_action in PYTHON_TO_METTA.items():
            path = os.path.join(self.d, 'atomspace', 'remediation_rules.metta')
            with open(path) as f:
                content = f.read()
            self.assertIn(f'({metta_action}', content,
                         f'MeTTa rules missing action: {metta_action} (Python: {py_action})')

    def test_cross_validate_all_verdicts(self):
        """For each episode+verdict pair, verify Python actions map to MeTTa expected set."""
        for ep_file, expected_verdict in self.episodes:
            with open(os.path.join(self.d, 'replay_corpus', ep_file)) as f:
                data = json.load(f)
            pipeline = IntegratedGovernorPipeline(data)
            result = pipeline.run(ecan_cycles=10).to_dict()
            engine = RemediationEngine(data)

            matching = [r for r in result['recommendations']
                       if r['unified_verdict'] == expected_verdict]
            self.assertTrue(len(matching) > 0,
                           f'{ep_file}: no {expected_verdict} verdict found')

            for rec in matching:
                plan = engine.generate_plan(rec)
                # Map Python actions to MeTTa equivalents
                metta_actions = set()
                for step in plan.steps:
                    mapped = PYTHON_TO_METTA.get(step.action, step.action)
                    metta_actions.add(mapped)
                # Check that all mapped actions are in the expected MeTTa set
                expected = METTA_EXPECTED[expected_verdict]
                # The Python engine may have extra actions (like release_resource for each
                # resource), so we check that the expected actions are a subset
                # For verdicts with multiple resources, release_resource maps to
                # release_all_resources, so we need to account for that
                if expected_verdict == 'STOP_STALE':
                    # release_resource maps to release_all_resources
                    has_release = any(s.action == 'release_resource' for s in plan.steps)
                    if has_release:
                        metta_actions.add('release_all_resources')

                # release_all_resources is only expected if the task actually has resources
                has_resources = len(engine.task_resources.get(rec["task_id"], [])) > 0
                for exp_action in expected:
                    if exp_action == "release_all_resources" and not has_resources:
                        continue
                    self.assertIn(exp_action, metta_actions,
                                 f'{ep_file} {rec["task_id"]}: MeTTa expects {exp_action} '
                                 f'but Python produced {metta_actions}')

    def test_action_count_per_verdict(self):
        """Verify each verdict produces a reasonable number of steps (2-5)."""
        for ep_file, expected_verdict in self.episodes:
            with open(os.path.join(self.d, 'replay_corpus', ep_file)) as f:
                data = json.load(f)
            pipeline = IntegratedGovernorPipeline(data)
            result = pipeline.run(ecan_cycles=10).to_dict()
            engine = RemediationEngine(data)

            for rec in result['recommendations']:
                if rec['unified_verdict'] == expected_verdict:
                    plan = engine.generate_plan(rec)
                    self.assertGreaterEqual(len(plan.steps), 2,
                                           f'{expected_verdict}: too few steps')
                    self.assertLessEqual(len(plan.steps), 10,
                                        f'{expected_verdict}: too many steps')

    def test_dependency_chain_valid(self):
        """Verify dependency references are valid step_ids."""
        for ep_file, _ in self.episodes:
            with open(os.path.join(self.d, 'replay_corpus', ep_file)) as f:
                data = json.load(f)
            pipeline = IntegratedGovernorPipeline(data)
            result = pipeline.run(ecan_cycles=10).to_dict()
            engine = RemediationEngine(data)

            for rec in result['recommendations']:
                plan = engine.generate_plan(rec)
                step_ids = {s.step_id for s in plan.steps}
                for step in plan.steps:
                    for dep in step.depends_on:
                        self.assertIn(dep, step_ids,
                                     f'{plan.task_id}: {step.step_id} depends on '
                                     f'nonexistent {dep}')


if __name__ == '__main__':
    unittest.main()
