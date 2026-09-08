#!/usr/bin/env python3
"""Remediation Engine v0.1 - generates structured action plans for each verdict."""
from dataclasses import dataclass, field

@dataclass
class RemediationStep:
    """A single step in a remediation plan."""
    step_id: str
    action: str
    target: str
    description: str
    priority: int
    depends_on: list = field(default_factory=list)
    verification: str = ""
    estimated_effort: str = ""

@dataclass
class RemediationPlan:
    """A structured remediation plan with prioritized steps."""
    task_id: str
    verdict: str
    plan_summary: str
    steps: list
    rollback_plan: str = ""
    success_criteria: str = ""
    risk_notes: str = ""

    def to_dict(self):
        """Return a dictionary representation of this object."""
        return {
            'task_id': self.task_id, 'verdict': self.verdict,
            'plan_summary': self.plan_summary,
            'steps': [{
                'step_id': s.step_id, 'action': s.action,
                'target': s.target, 'description': s.description,
                'priority': s.priority, 'depends_on': s.depends_on,
                'verification': s.verification, 'estimated_effort': s.estimated_effort,
            } for s in self.steps],
            'rollback_plan': self.rollback_plan,
            'success_criteria': self.success_criteria,
            'risk_notes': self.risk_notes,
        }

class RemediationEngine:
    """Generates remediation plans from verdicts."""
    def __init__(self, episode_data):
        self.data = episode_data
        self._build_index()

    def _build_index(self):
        self.tasks = {t['id']: t for t in self.data.get('tasks', [])}
        self.goals = {g['id']: g for g in self.data.get('goals', [])}
        self.task_goals = {}
        self.task_resources = {}
        for e in self.data.get('edges', []):
            if e.get('relation') == 'contributes_to':
                self.task_goals.setdefault(e['from'], []).append(e['to'])
            if e.get('relation') == 'occupies':
                self.task_resources.setdefault(e['from'], []).append(e['to'])

    def generate_plan(self, rec):
        """Generate a remediation plan for a given verdict."""
        task_id = rec['task_id']
        verdict = rec['unified_verdict']
        signals = rec.get('signals', [])
        goals = self.task_goals.get(task_id, [])
        resources = self.task_resources.get(task_id, [])
        dispatch = {
            'STOP_STALE': self._plan_stop_stale,
            'ESCALATE': self._plan_escalate,
            'PAUSE_RECOVERABLY': self._plan_pause,
            'DEFER': self._plan_defer,
            'REPLAN': self._plan_replan,
            'CONTINUE': self._plan_continue,
        }
        handler = dispatch.get(verdict)
        if handler:
            return handler(task_id, goals, resources, signals, rec)
        return RemediationPlan(task_id=task_id, verdict=verdict, plan_summary='Unknown', steps=[])

    def generate_all(self, recommendations):
        """Generate remediation plans for all verdicts in a pipeline result."""
        return [self.generate_plan(r) for r in recommendations]

    def _plan_stop_stale(self, task_id, goals, resources, signals, rec):
        steps = [RemediationStep(
            step_id='s1', action='abandon_task', target=task_id,
            description=f'Mark {task_id} as abandoned - goals terminal',
            priority=1, verification=f'{task_id} status == abandoned',
            estimated_effort='trivial')]
        for i, rid in enumerate(resources):
            steps.append(RemediationStep(
                step_id=f's{i+2}', action='release_resource', target=rid,
                description=f'Release {rid}', priority=2, depends_on=['s1'],
                verification=f'{rid} available', estimated_effort='trivial'))
        idx = len(steps) + 1
        steps.append(RemediationStep(
            step_id=f's{idx}', action='notify_stakeholders',
            target=','.join(goals),
            description=f'Notify: {task_id} abandoned, goals {goals} terminal',
            priority=3, depends_on=['s1'], verification='Acknowledged',
            estimated_effort='minutes'))
        return RemediationPlan(
            task_id=task_id, verdict='STOP_STALE', steps=steps,
            plan_summary=f'Abandon {task_id}, release resources',
            rollback_plan=f'Reactivate if new goal links to it',
            success_criteria=f'{task_id} abandoned, resources released',
            risk_notes='Low risk')

    def _plan_escalate(self, task_id, goals, resources, signals, rec):
        sti = rec.get('sti', 0)
        steps = [
            RemediationStep(
                step_id='s1', action='boost_priority', target=task_id,
                description=f'Boost {task_id} to CRITICAL - blocks {len(goals)} goals',
                priority=1, verification='Priority == CRITICAL', estimated_effort='trivial'),
            RemediationStep(
                step_id='s2', action='allocate_resources',
                target=','.join(resources) if resources else 'none',
                description=f'Allocate resources for {task_id} (STI={sti:.1f})',
                priority=1, depends_on=['s1'],
                verification='Resources allocated', estimated_effort='minutes'),
            RemediationStep(
                step_id='s3', action='set_deadline', target=task_id,
                description=f'Set deadline for {task_id}',
                priority=2, depends_on=['s2'],
                verification='Deadline set', estimated_effort='minutes'),
            RemediationStep(
                step_id='s4', action='require_evidence', target=task_id,
                description=f'Require evidence from {task_id} at next checkpoint',
                priority=2, depends_on=['s2'],
                verification='Evidence produced', estimated_effort='hours'),
        ]
        return RemediationPlan(
            task_id=task_id, verdict='ESCALATE', steps=steps,
            plan_summary=f'Escalate {task_id}: boost, allocate, deadline',
            rollback_plan='Revert if evidence produced',
            success_criteria=f'{task_id} produces evidence',
            risk_notes='Medium risk')

    def _plan_pause(self, task_id, goals, resources, signals, rec):
        blocker = None
        res_name = None
        for s in signals:
            if s.startswith('higher_priority_task='):
                blocker = s.split('=', 1)[1]
            if s.startswith('resource='):
                res_name = s.split('=', 1)[1]
        steps = [RemediationStep(
            step_id='s1', action='pause_task', target=task_id,
            description=f'Pause {task_id} - resource contention',
            priority=2, verification=f'{task_id} paused', estimated_effort='trivial')]
        if blocker:
            steps.append(RemediationStep(
                step_id='s2', action='monitor_blocker', target=blocker,
                description=f'Monitor {blocker}',
                priority=2, depends_on=['s1'],
                verification=f'{blocker} completed', estimated_effort='hours'))
            steps.append(RemediationStep(
                step_id='s3', action='resume_task', target=task_id,
                description=f'Resume {task_id} after {blocker} frees {res_name or "resources"}',
                priority=2, depends_on=['s2'],
                verification=f'{task_id} active', estimated_effort='trivial'))
        else:
            steps.append(RemediationStep(
                step_id='s2', action='schedule_recheck', target=task_id,
                description=f'Schedule recheck for {task_id}',
                priority=3, depends_on=['s1'],
                verification='Recheck scheduled', estimated_effort='trivial'))
        return RemediationPlan(
            task_id=task_id, verdict='PAUSE_RECOVERABLY', steps=steps,
            plan_summary=f'Pause {task_id}, wait for blocker, resume',
            rollback_plan='Resume if false positive',
            success_criteria=f'{task_id} resumed',
            risk_notes='Low risk')

    def _plan_defer(self, task_id, goals, resources, signals, rec):
        stage = None
        for s in signals:
            if s.startswith('stage='):
                stage = s.split('=', 1)[1]
        steps = [
            RemediationStep(
                step_id='s1', action='park_task', target=task_id,
                description=f'Park {task_id} until project matures past {stage}',
                priority=3, verification=f'{task_id} parked', estimated_effort='trivial'),
            RemediationStep(
                step_id='s2', action='set_trigger', target=task_id,
                description=f'Set trigger: resume when stage leaves {stage}',
                priority=3, depends_on=['s1'],
                verification='Trigger condition set', estimated_effort='minutes'),
            RemediationStep(
                step_id='s3', action='monitor_trigger', target=task_id,
                description=f'Monitor project stage for {task_id}',
                priority=4, depends_on=['s2'],
                verification='Stage changed', estimated_effort='days'),
        ]
        return RemediationPlan(
            task_id=task_id, verdict='DEFER', steps=steps,
            plan_summary=f'Park {task_id} with trigger condition',
            rollback_plan='Resume early if scope changes',
            success_criteria=f'{task_id} resumed after trigger fires',
            risk_notes='Low risk - task is premature')

    def _plan_replan(self, task_id, goals, resources, signals, rec):
        superseded = None
        superseded_by = None
        for s in signals:
            if s.startswith('superseded_goal='):
                superseded = s.split('=', 1)[1]
            if s.startswith('superseded_by='):
                superseded_by = s.split('=', 1)[1]
        steps = [
            RemediationStep(
                step_id='s1', action='redesign_task', target=task_id,
                description=f'Redesign {task_id} for new goal {superseded_by or "updated goals"}',
                priority=2, verification='New task plan approved',
                estimated_effort='hours'),
            RemediationStep(
                step_id='s2', action='update_goal_link', target=task_id,
                description=f'Update {task_id} goal link: {superseded} -> {superseded_by or "new goal"}',
                priority=2, depends_on=['s1'],
                verification='Edge updated in graph', estimated_effort='trivial'),
            RemediationStep(
                step_id='s3', action='reset_progress', target=task_id,
                description=f'Reset progress counters for {task_id}',
                priority=3, depends_on=['s2'],
                verification='Progress reset', estimated_effort='trivial'),
            RemediationStep(
                step_id='s4', action='archive_old_approach', target=superseded or 'old_goal',
                description=f'Archive old approach targeting {superseded or "superseded goal"}',
                priority=4, depends_on=['s2'],
                verification='Old approach archived', estimated_effort='minutes'),
        ]
        return RemediationPlan(
            task_id=task_id, verdict='REPLAN', steps=steps,
            plan_summary=f'Replan {task_id} for superseded goal',
            rollback_plan='Restore old goal link if replan fails',
            success_criteria=f'{task_id} linked to {superseded_by or "new goal"}, progress restarted',
            risk_notes='Medium risk - lost progress on old approach')

    def _plan_continue(self, task_id, goals, resources, signals, rec):
        rel = rec.get('relevance_score', 0)
        steps = [
            RemediationStep(
                step_id='s1', action='monitor_task', target=task_id,
                description=f'Continue {task_id} - healthy (relevance={rel:.3f})',
                priority=4, verification='Task still progressing',
                estimated_effort='ongoing'),
            RemediationStep(
                step_id='s2', action='set_checkpoint', target=task_id,
                description=f'Set next checkpoint for {task_id}',
                priority=4, verification='Checkpoint scheduled',
                estimated_effort='trivial'),
        ]
        return RemediationPlan(
            task_id=task_id, verdict='CONTINUE', steps=steps,
            plan_summary=f'Continue {task_id} with monitoring',
            rollback_plan='N/A',
            success_criteria=f'{task_id} reaches checkpoint',
            risk_notes='No action needed')
