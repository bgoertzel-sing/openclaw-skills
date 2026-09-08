#!/usr/bin/env python3
"""Reasoning Explanation Layer v0.1
==================================

Generates human-readable justifications for each verdict by combining
signals from all pipeline layers: PLN truth values, ECAN attention,
verdict bridge, multi-hop chains, and conflict detection.

Each explanation follows the pattern:
  1. VERDICT: What was decided
  2. EVIDENCE: Why (signals, truth values, chain paths)
  3. CONTEXT: Multi-hop goal coverage, resource conflicts
  4. ACTION: What to do next
"""

from __future__ import annotations
import json
from dataclasses import dataclass, field
from typing import Optional

import sys, os
sys.path.insert(0, os.path.dirname(__file__))


@dataclass
class TaskExplanation:
    """Human-readable explanation for a single task verdict."""
    task_id: str
    verdict: str
    headline: str
    evidence_points: list
    chain_summary: str
    conflict_summary: str
    recommended_action: str
    confidence_note: str

    def to_dict(self) -> dict:
        return {
            'task_id': self.task_id,
            'verdict': self.verdict,
            'headline': self.headline,
            'evidence_points': self.evidence_points,
            'chain_summary': self.chain_summary,
            'conflict_summary': self.conflict_summary,
            'recommended_action': self.recommended_action,
            'confidence_note': self.confidence_note,
        }

    def to_markdown(self) -> str:
        lines = [
            f'### {self.task_id} - {self.verdict}',
            f'**{self.headline}**',
            '',
            '**Evidence:**',
        ]
        for ep in self.evidence_points:
            lines.append(f'  - {ep}')
        if self.chain_summary:
            lines.append('')
            lines.append(f'**Multi-hop chains:** {self.chain_summary}')
        if self.conflict_summary:
            lines.append('')
            lines.append(f'**Resource conflicts:** {self.conflict_summary}')
        lines.append('')
        lines.append(f'**Action:** {self.recommended_action}')
        lines.append('')
        lines.append(f'_{self.confidence_note}_')
        return '\n'.join(lines)


VERDICT_HEADLINES = {
    'STOP_STALE': 'Task is stale and no longer relevant to active goals.',
    'ESCALATE': 'Task blocks critical goals and needs immediate attention.',
    'PAUSE_RECOVERABLY': 'Task is paused due to recoverable blockers.',
    'DEFER': 'Task is deferred - premature given current state.',
    'REPLAN': 'Task needs replanning - approach is not working.',
    'CONTINUE': 'Task is justified and should continue running.',
    'BLOCKED': 'Task is blocked and cannot proceed.',
}


class ReasoningExplainer:
    """Generates explanations for pipeline verdicts."""

    def __init__(self, data: dict):
        self.data = data
        self.nodes = {}
        for key in ('goals', 'projects', 'tasks', 'resources',
                     'results', 'constraints'):
            for node in data.get(key, []):
                self.nodes[node['id']] = node

    def _node_label(self, nid: str) -> str:
        node = self.nodes.get(nid, {})
        label = node.get('label', node.get('id', nid))
        return f'{label} ({nid})'

    def explain_task(self, rec: dict, conflict_chains: list = None) -> TaskExplanation:
        """Generate explanation for a single task recommendation."""
        task_id = rec['task_id']
        verdict = rec['unified_verdict']

        evidence_points = []
        for signal in rec.get('signals', []):
            evidence_points.append(self._interpret_signal(signal, rec))

        rel = rec.get('relevance_score', 0.0)
        if rel > 0.7:
            evidence_points.append(f'High relevance score ({rel:.3f}) - strongly connected to active goals')
        elif rel > 0.3:
            evidence_points.append(f'Moderate relevance ({rel:.3f}) - partially connected to goals')
        elif rel > 0:
            evidence_points.append(f'Low relevance ({rel:.3f}) - weakly connected to goals')
        else:
            evidence_points.append(f'Zero relevance - no active goal connection detected')

        sti = rec.get('sti', 0)
        lti = rec.get('lti', 0)
        if sti > 40:
            evidence_points.append(f'High short-term attention (STI={sti:.1f}) - system is focused here')
        elif sti < 5:
            evidence_points.append(f'Low short-term attention (STI={sti:.1f}) - system has deprioritized this')

        mh_chains = rec.get('multihop_chains', 0)
        mh_goals = rec.get('multihop_goal_coverage', [])
        mh_depth = rec.get('multihop_max_depth', 0)
        if mh_chains > 0:
            goal_labels = [self._node_label(g) for g in mh_goals]
            chain_summary = (f'{mh_chains} chain(s) reaching {len(mh_goals)} goal(s) '
                            f'at max depth {mh_depth}: {", ".join(goal_labels)}')
        else:
            chain_summary = 'No multi-hop chains found to any goal.'

        conflict_summary = ''
        if conflict_chains:
            task_conflicts = [c for c in conflict_chains
                            if task_id in (c.get('task_a'), c.get('task_b'))]
            if task_conflicts:
                parts = []
                for c in task_conflicts:
                    other = c['task_b'] if c['task_a'] == task_id else c['task_a']
                    parts.append(
                        f'contends with {self._node_label(other)} for '
                        f'{self._node_label(c["resource_id"])}'
                        + (' (competing goals)' if c.get('is_competing') else ' (shared goals)')
                    )
                conflict_summary = '; '.join(parts)

        eviction = rec.get('eviction_candidate', False)
        stale = rec.get('staleness_flag', False)
        notes = [f'STI={sti:.1f}, LTI={lti:.1f}']
        if eviction:
            notes.append('eviction candidate')
        if stale:
            notes.append('flagged stale')
        confidence_note = ' | '.join(notes)

        headline = VERDICT_HEADLINES.get(verdict, f'Verdict: {verdict}')

        return TaskExplanation(
            task_id=task_id,
            verdict=verdict,
            headline=headline,
            evidence_points=evidence_points,
            chain_summary=chain_summary,
            conflict_summary=conflict_summary,
            recommended_action=rec.get('recommended_action', ''),
            confidence_note=confidence_note,
        )

    def _interpret_signal(self, signal: str, rec: dict) -> str:
        """Convert a raw signal into a human-readable evidence point."""
        if signal.startswith('temporal_staleness:'):
            goals_part = signal.split(':', 1)[1] if ':' in signal else ''
            return f'Temporal staleness detected - goals {goals_part} may have shifted'
        if signal == 'resource_contention':
            return 'Resource contention detected - another task needs the same resource'
        if signal.startswith('resource='):
            res = signal.split('=', 1)[1]
            return f'Contended resource: {self._node_label(res)}'
        if signal.startswith('higher_priority_task='):
            other = signal.split('=', 1)[1]
            return f'Higher priority task {self._node_label(other)} takes precedence'
        if signal == 'multiple_active_goals_no_evidence':
            return 'Task targets multiple active goals but produces no evidence'
        if signal.endswith('_active_goals'):
            count = signal.split('_')[0]
            return f'Task connected to {count} active goal(s)'
        if signal == 'no_evidence_produced':
            return 'No evidence/results produced by this task'
        if signal == 'premature_implementation':
            return 'Premature implementation - foundational work not yet complete'
        if signal.startswith('overengineering:'):
            return f'Overengineering detected: {signal.split(":", 1)[1]}'
        if signal == 'justified_long_running':
            return 'Long-running task is justified by consistent evidence production'
        return signal

    def explain_all(self, pipeline_dict: dict) -> list[TaskExplanation]:
        """Generate explanations for all task recommendations."""
        recs = pipeline_dict.get('recommendations', [])
        conflicts = pipeline_dict.get('conflict_layer', {}).get('conflicts', [])
        explanations = []
        for rec in recs:
            explanations.append(self.explain_task(rec, conflicts))
        return explanations

    def explain_to_markdown(self, pipeline_dict: dict) -> str:
        """Generate a full markdown report of all explanations."""
        explanations = self.explain_all(pipeline_dict)
        lines = ['# Reasoning Explanations', '']
        lines.append(f'Episode: {pipeline_dict.get("episode_id", "unknown")}')
        lines.append(f'Timestamp: {pipeline_dict.get("timestamp", "?")}')
        lines.append('')
        for exp in explanations:
            lines.append(exp.to_markdown())
            lines.append('---')
            lines.append('')
        return '\n'.join(lines)

    def explain_to_json(self, pipeline_dict: dict) -> str:
        """Generate JSON of all explanations."""
        explanations = self.explain_all(pipeline_dict)
        return json.dumps(
            [e.to_dict() for e in explanations],
            indent=2
        )
