"""Tests for status normalization (normalize_status + STATUS_ALIASES).

Validates that non-canonical status strings from real-world systems are
properly mapped to canonical statuses, and that all downstream PLN/evaluator
logic handles them correctly.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.dirname(__file__))

from pln_propagation import (
    normalize_status, STATUS_ALIASES,
    STATUS_STRENGTH, STATUS_CONFIDENCE,
    PLNPropagator
)


# ─── normalize_status unit tests ───

def test_canonical_statuses_pass_through():
    """Canonical statuses should map to themselves."""
    for s in STATUS_STRENGTH:
        assert normalize_status(s) == s, f'{s} should be canonical'

def test_none_defaults_to_active():
    assert normalize_status(None) == 'active'

def test_case_insensitive():
    assert normalize_status('Active') == 'active'
    assert normalize_status('BLOCKED') == 'blocked'
    assert normalize_status('Completed') == 'completed'

def test_spaces_and_hyphens():
    assert normalize_status('in progress') == 'active'
    assert normalize_status('in-progress') == 'active'
    assert normalize_status('IN PROGRESS') == 'active'

def test_common_aliases():
    """Every alias in STATUS_ALIASES must map to a canonical status."""
    for alias, canonical in STATUS_ALIASES.items():
        result = normalize_status(alias)
        assert result == canonical, f'{alias} -> {result}, expected {canonical}'
        assert result in STATUS_STRENGTH, f'{canonical} not in STATUS_STRENGTH'

def test_unknown_status_passes_through():
    """Unknown statuses should pass through (not silently dropped)."""
    assert normalize_status('flux_capacitor') == 'flux_capacitor'


# ─── Integration: PLNPropagator handles non-canonical statuses ───

def _make_graph(tasks_status='in_progress', goal_status='pending'):
    return {
        'goals': [
            {'id': 'g1', 'status': goal_status, 'priority': 1.0}
        ],
        'tasks': [
            {'id': 't1', 'goal': 'g1', 'status': tasks_status, 'effort': 0.5}
        ],
        'resources': [
            {'id': 'r1', 'exclusive': True}
        ],
        'edges': [
            {'source': 't1', 'target': 'g1', 'type': 'supports'},
            {'source': 't1', 'target': 'r1', 'type': 'consumes'}
        ]
    }

def test_propagator_with_in_progress():
    """Task with status 'in_progress' should be treated as 'active'."""
    g = _make_graph(tasks_status='in_progress')
    p = PLNPropagator(g)
    from pln_propagation import _initial_tv
    tv = _initial_tv(g['tasks'][0])
    # Should get active strength (0.8), not default (0.5)
    assert tv.strength == STATUS_STRENGTH['active'], f'Expected {STATUS_STRENGTH["active"]}, got {tv.strength}'

def test_propagator_with_pending_goal():
    """Goal with status 'pending' should be treated as 'active'."""
    g = _make_graph(goal_status='pending')
    p = PLNPropagator(g)
    from pln_propagation import _initial_tv
    tv = _initial_tv(g['goals'][0])
    assert tv.strength == STATUS_STRENGTH['active']

def test_propagator_with_done_task():
    """Task with status 'done' should be treated as 'completed'."""
    g = _make_graph(tasks_status='done')
    p = PLNPropagator(g)
    from pln_propagation import _initial_tv
    tv = _initial_tv(g['tasks'][0])
    assert tv.strength == STATUS_STRENGTH['completed']

def test_propagator_with_succeeded():
    g = _make_graph(tasks_status='succeeded')
    p = PLNPropagator(g)
    from pln_propagation import _initial_tv
    tv = _initial_tv(g['tasks'][0])
    assert tv.strength == STATUS_STRENGTH['completed']

def test_propagator_with_paused():
    """Task with status 'paused' should be treated as 'blocked'."""
    g = _make_graph(tasks_status='paused')
    p = PLNPropagator(g)
    from pln_propagation import _initial_tv
    tv = _initial_tv(g['tasks'][0])
    assert tv.strength == STATUS_STRENGTH['blocked']

def test_active_goal_filter_with_alias():
    """Goal with status 'pending' should pass the active-goal filter."""
    g = _make_graph(goal_status='pending')
    p = PLNPropagator(g)
    assert p._goal_active('g1'), 'pending goal should be counted as active'

def test_superseded_alias_deprecated():
    """Goal with status 'deprecated' should be treated as 'superseded'."""
    g = _make_graph(goal_status='deprecated')
    p = PLNPropagator(g)
    assert not p._goal_active('g1'), 'deprecated goal should not be active'

def test_failed_maps_to_cancelled():
    """Task with status 'failed' should be treated as 'cancelled'."""
    g = _make_graph(tasks_status='failed')
    p = PLNPropagator(g)
    from pln_propagation import _initial_tv
    tv = _initial_tv(g['tasks'][0])
    assert tv.strength == STATUS_STRENGTH['cancelled']

def test_propagation_runs_with_mixed_statuses():
    """Full propagation should not crash with non-canonical statuses."""
    g = {
        'goals': [
            {'id': 'g1', 'status': 'pending', 'priority': 1.0},
            {'id': 'g2', 'status': 'done', 'priority': 0.8},
        ],
        'tasks': [
            {'id': 't1', 'goal': 'g1', 'status': 'running', 'effort': 0.5},
            {'id': 't2', 'goal': 'g2', 'status': 'finished', 'effort': 0.3},
            {'id': 't3', 'goal': 'g1', 'status': 'queued', 'effort': 0.4},
        ],
        'resources': [],
        'edges': [
            {'source': 't1', 'target': 'g1', 'type': 'supports'},
            {'source': 't2', 'target': 'g2', 'type': 'supports'},
            {'source': 't3', 'target': 'g1', 'type': 'supports'},
        ]
    }
    p = PLNPropagator(g)
    p.propagate_upward(); p.propagate_downward()
    # t1 (running=active) and t3 (queued=active) should be active
    # t2 (finished=completed) should not be active
    # Check that tasks with active-aliased statuses are treated as active
    # by examining their truth values (active tasks get STATUS_STRENGTH['active'])
    from pln_propagation import _initial_tv
    t1_tv = _initial_tv(g['tasks'][0])  # running -> active
    t2_tv = _initial_tv(g['tasks'][1])  # finished -> completed
    t3_tv = _initial_tv(g['tasks'][2])  # queued -> active
    assert t1_tv.strength == STATUS_STRENGTH['active'], 'running should be active'
    assert t3_tv.strength == STATUS_STRENGTH['active'], 'queued should be active'
    assert t2_tv.strength == STATUS_STRENGTH['completed'], 'finished should be completed'


# ─── Test evaluator integration ───

def test_relevance_evaluator_with_aliases():
    """The relevance evaluator should handle non-canonical statuses."""
    from evaluator.relevance_evaluator import Graph, RelevanceEvaluator
    g = {
        'goals': [
            {'id': 'g1', 'status': 'in_progress', 'priority': 1.0}
        ],
        'tasks': [
            {'id': 't1', 'kind': 'task', 'goal': 'g1', 'status': 'running', 'effort': 0.5}
        ],
        'resources': [],
        'edges': [
            {'from': 't1', 'to': 'g1', 'relation': 'supports'}
        ]
    }
    graph = Graph(g)
    ev = RelevanceEvaluator(graph)
    # Should not crash; should treat in_progress/running as active
    results = ev.evaluate_all()
    assert results is not None
    assert isinstance(results, list)
    # Should produce verdicts for active tasks (running -> active)
    assert len(results) > 0, f'Expected at least 1 verdict, got {len(results)}'
    assert hasattr(results[0], 'verdict')


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, '-v'])
