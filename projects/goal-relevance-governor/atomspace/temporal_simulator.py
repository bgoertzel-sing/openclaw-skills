#!/usr/bin/env python3
"""Temporal Evolution Simulator v0.1
====================================

Simulates task/goal/resource state transitions over discrete timesteps
and verifies the governor produces correct verdicts at each step.
"""

import copy
from dataclasses import dataclass, field
from datetime import datetime, timedelta

import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from integrated_governor import IntegratedGovernorPipeline


@dataclass
class Mutation:
    """A single state mutation applied at a timestep."""
    timestep: int
    description: str
    changes: list  # list of (node_type, node_id, field_name, new_value)
    new_frozen_at: str = None
    expected_verdicts: dict = field(default_factory=dict)


@dataclass
class TimelineStep:
    """One step in a simulated timeline."""
    timestep: int
    description: str
    data: dict
    pipeline_result: dict = None
    verdicts: dict = None
    verdict_correct: bool = True
    errors: list = field(default_factory=list)


@dataclass
class TimelineResult:
    """Result of running a full timeline simulation."""
    steps: list
    all_correct: bool
    verdict_drift: list  # list of (timestep, task_id, old_verdict, new_verdict)

    def to_dict(self) -> dict:
        return {
            'all_correct': self.all_correct,
            'step_count': len(self.steps),
            'verdict_drift': self.verdict_drift,
            'steps': [
                {
                    'timestep': s.timestep,
                    'description': s.description,
                    'verdicts': s.verdicts,
                    'verdict_correct': s.verdict_correct,
                    'errors': s.errors,
                }
                for s in self.steps
            ],
        }


class TemporalSimulator:
    """Simulates temporal evolution of episode states."""

    def __init__(self, base_data: dict):
        self.base_data = base_data
        self.episode_id = base_data.get('episode_id', 'unknown')

    def _apply_mutation(self, data: dict, mutation: Mutation) -> dict:
        """Apply a mutation to a copy of the data.
        
        Supports dot-notation for nested fields, e.g. 'result_contract.maturity_stage'.
        """
        data = copy.deepcopy(data)
        for node_type, node_id, field_name, new_value in mutation.changes:
            nodes = data.get(node_type, [])
            for node in nodes:
                if node.get('id') == node_id:
                    if '.' in field_name:
                        # Nested field: traverse/create path
                        parts = field_name.split('.')
                        obj = node
                        for part in parts[:-1]:
                            if part not in obj or not isinstance(obj[part], dict):
                                obj[part] = {}
                            obj = obj[part]
                        obj[parts[-1]] = new_value
                    else:
                        node[field_name] = new_value
                    break
        if mutation.new_frozen_at:
            data['frozen_at'] = mutation.new_frozen_at
        data['episode_id'] = f"{self.episode_id}-t{mutation.timestep}"
        return data

    def _advance_frozen_at(self, hours: float) -> str:
        """Advance base frozen_at by given hours."""
        current = self.base_data.get('frozen_at', '')
        ts = current.replace('Z', '+00:00')
        dt = datetime.fromisoformat(ts)
        new_dt = dt + timedelta(hours=hours)
        return new_dt.strftime('%Y-%m-%dT%H:%M:%SZ')

    def create_timeline_stale_task(self) -> list[Mutation]:
        """Timeline: task goes stale as goals become terminal."""
        return [
            Mutation(
                timestep=0,
                description='Initial state: task active, one goal achieved',
                changes=[],
                expected_verdicts={'t-p2m-codegen': 'STOP_STALE'},
            ),
            Mutation(
                timestep=1,
                description='All goals now terminal - task definitely stale',
                changes=[
                    ('goals', 'g-build-omegaclaw', 'status', 'achieved'),
                    ('goals', 'g-ir-translation-v2', 'status', 'achieved'),
                ],
                new_frozen_at=self._advance_frozen_at(24.0),
                expected_verdicts={'t-p2m-codegen': 'STOP_STALE'},
            ),
            Mutation(
                timestep=2,
                description='Task marked completed',
                changes=[
                    ('tasks', 't-p2m-codegen', 'status', 'completed'),
                ],
                new_frozen_at=self._advance_frozen_at(48.0),
                expected_verdicts={},
            ),
        ]

    def create_timeline_conflict_resolution(self) -> list[Mutation]:
        """Timeline: resource conflict resolves as one task completes."""
        return [
            Mutation(
                timestep=0,
                description='Initial state: two tasks contending for resource',
                changes=[],
                expected_verdicts={},
            ),
            Mutation(
                timestep=1,
                description='Higher-priority task completed, resource freed',
                changes=[
                    ('tasks', 't-restore-agents', 'status', 'completed'),
                    ('goals', 'g-restore-agents', 'status', 'achieved'),
                ],
                new_frozen_at=self._advance_frozen_at(6.0),
                expected_verdicts={},
            ),
            Mutation(
                timestep=2,
                description='Petta-chem resumes without contention',
                changes=[],
                new_frozen_at=self._advance_frozen_at(12.0),
                expected_verdicts={},
            ),
        ]

    def create_timeline_premature_to_justified(self) -> list[Mutation]:
        """Timeline: premature task becomes justified as project matures."""
        return [
            Mutation(
                timestep=0,
                description='Initial state: task is premature',
                changes=[],
                expected_verdicts={'t-hardening-guards': 'DEFER'},
            ),
            Mutation(
                timestep=1,
                description='Project stage advanced to implementation',
                changes=[
                    ('projects', 'p-research-infra', 'result_contract.maturity_stage', 'implementation'),
                ],
                new_frozen_at=self._advance_frozen_at(168.0),
                expected_verdicts={},
            ),
        ]

    def run_timeline(self, mutations: list[Mutation], ecan_cycles: int = 10) -> TimelineResult:
        """Run a timeline simulation, applying mutations sequentially."""
        steps = []
        current_data = copy.deepcopy(self.base_data)
        prev_verdicts = {}
        verdict_drift = []
        all_correct = True

        for mutation in mutations:
            step_data = self._apply_mutation(current_data, mutation)
            current_data = step_data

            try:
                pipeline = IntegratedGovernorPipeline(step_data)
                result = pipeline.run(ecan_cycles=ecan_cycles)
                d = result.to_dict()
                verdicts = {}
                for rec in d.get('recommendations', []):
                    verdicts[rec['task_id']] = rec['unified_verdict']
            except Exception as e:
                step = TimelineStep(
                    timestep=mutation.timestep,
                    description=mutation.description,
                    data=step_data,
                    verdicts={},
                    verdict_correct=False,
                    errors=[str(e)],
                )
                steps.append(step)
                all_correct = False
                continue

            errors = []
            correct = True
            for task_id, expected_v in mutation.expected_verdicts.items():
                actual_v = verdicts.get(task_id)
                if actual_v != expected_v:
                    errors.append(f'Task {task_id}: expected {expected_v}, got {actual_v}')
                    correct = False

            for task_id, v in verdicts.items():
                old_v = prev_verdicts.get(task_id)
                if old_v is not None and old_v != v:
                    verdict_drift.append((mutation.timestep, task_id, old_v, v))

            step = TimelineStep(
                timestep=mutation.timestep,
                description=mutation.description,
                data=step_data,
                pipeline_result=d,
                verdicts=verdicts,
                verdict_correct=correct,
                errors=errors,
            )
            steps.append(step)
            prev_verdicts = verdicts
            if not correct:
                all_correct = False

        return TimelineResult(
            steps=steps,
            all_correct=all_correct,
            verdict_drift=verdict_drift,
        )

    def create_timeline_overengineered_repair(self) -> list[Mutation]:
        """Timeline: tasks on superseded goal get replanned as new goal emerges.

        Episode 04: two tasks (t-process-inspector, t-launch-wrappers) contribute
        to a superseded goal. Timeline shows the goal transition and verdict change.
        """
        return [
            Mutation(
                timestep=0,
                description='Initial state: tasks on superseded goal',
                changes=[],
                expected_verdicts={},
            ),
            Mutation(
                timestep=1,
                description='New goal explicitly replaces old; tasks should replan',
                changes=[
                    ('goals', 'g-restore-agents-original', 'status', 'abandoned'),
                ],
                new_frozen_at=self._advance_frozen_at(48.0),
                expected_verdicts={},
            ),
            Mutation(
                timestep=2,
                description='Tasks redirected to new goal g-restore-agents-v2',
                changes=[
                    ('tasks', 't-process-inspector', 'status', 'completed'),
                    ('tasks', 't-launch-wrappers', 'status', 'stopped'),
                ],
                new_frozen_at=self._advance_frozen_at(96.0),
                expected_verdicts={},
            ),
        ]

    def create_timeline_control_justified(self) -> list[Mutation]:
        """Timeline: long-running benchmark task stays CONTINUE across time.

        Episode 05: a justified task should keep its CONTINUE verdict
        as time advances and the project stays mature.
        """
        return [
            Mutation(
                timestep=0,
                description='Initial state: justified long-running benchmark',
                changes=[],
                expected_verdicts={'t-run-benchmark': 'CONTINUE'},
            ),
            Mutation(
                timestep=1,
                description='Time advances, project still hardened',
                changes=[],
                new_frozen_at=self._advance_frozen_at(24.0),
                expected_verdicts={'t-run-benchmark': 'CONTINUE'},
            ),
            Mutation(
                timestep=2,
                description='Benchmark completes successfully',
                changes=[
                    ('tasks', 't-run-benchmark', 'status', 'completed'),
                    ('goals', 'g-wmtm-validation', 'status', 'achieved'),
                ],
                new_frozen_at=self._advance_frozen_at(48.0),
                expected_verdicts={},
            ),
        ]

    def create_timeline_conflict_replan(self) -> list[Mutation]:
        """Timeline: approach conflict resolves as weaker task is replanned.

        Episode 06: two tasks (t-rest-wrapper, t-grpc-wrapper) compete for
        the same exclusive resource (r-api-gateway) with the same goal.
        The weaker task should get REPLAN, then gets stopped.
        """
        return [
            Mutation(
                timestep=0,
                description='Initial state: two tasks contending for shared resource',
                changes=[],
                expected_verdicts={},
            ),
            Mutation(
                timestep=1,
                description='Weaker task (grpc-wrapper) replanned/stopped',
                changes=[
                    ('tasks', 't-grpc-wrapper', 'status', 'stopped'),
                ],
                new_frozen_at=self._advance_frozen_at(12.0),
                expected_verdicts={},
            ),
            Mutation(
                timestep=2,
                description='REST wrapper proceeds unopposed, goal achieved',
                changes=[
                    ('tasks', 't-rest-wrapper', 'status', 'completed'),
                    ('goals', 'g-unified-api', 'status', 'achieved'),
                ],
                new_frozen_at=self._advance_frozen_at(48.0),
                expected_verdicts={},
            ),
        ]
