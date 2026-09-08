"""Tests for _get_transitive_goals, _has_evidence_for, _get_direct_goals, _get_project_for_task, _get_superseding_goals."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import pytest
from pln_propagation import PLNPropagator, TruthValue


def _make_graph(**kwargs):
    """Build minimal graph data from kwargs."""
    data = {}
    for key in ('goals', 'projects', 'tasks', 'resources', 'results', 'constraints'):
        if key in kwargs:
            data[key] = kwargs[key]
    data['edges'] = kwargs.get('edges', [])
    return data


# ─── _get_direct_goals ──────────────────────────────────────────────

def test_get_direct_goals_basic():
    """_get_direct_goals returns goals connected via contributes_to."""
    data = _make_graph(
        tasks=[{'id': 't1', 'kind': 'task'}],
        goals=[{'id': 'g1', 'kind': 'goal'}],
        edges=[{'from': 't1', 'to': 'g1', 'relation': 'contributes_to'}],
    )
    p = PLNPropagator(data)
    result = p._get_direct_goals('t1')
    assert result == ['g1']


def test_get_direct_goals_excludes_non_goals():
    """_get_direct_goals only returns nodes with kind=='goal'."""
    data = _make_graph(
        tasks=[{'id': 't1', 'kind': 'task'}],
        projects=[{'id': 'p1', 'kind': 'project'}],
        edges=[{'from': 't1', 'to': 'p1', 'relation': 'contributes_to'}],
    )
    p = PLNPropagator(data)
    result = p._get_direct_goals('t1')
    assert result == []


def test_get_direct_goals_no_goals():
    """_get_direct_goals returns empty list when task has no contributes_to edges."""
    data = _make_graph(
        tasks=[{'id': 't1', 'kind': 'task'}],
        edges=[],
    )
    p = PLNPropagator(data)
    assert p._get_direct_goals('t1') == []


# ─── _get_transitive_goals ─────────────────────────────────────────

def test_get_transitive_goals_flat():
    """_get_transitive_goals returns direct goals when no intermediate goals."""
    data = _make_graph(
        tasks=[{'id': 't1', 'kind': 'task'}],
        goals=[{'id': 'g1', 'kind': 'goal'}],
        edges=[{'from': 't1', 'to': 'g1', 'relation': 'contributes_to'}],
    )
    p = PLNPropagator(data)
    result = p._get_transitive_goals('t1')
    assert result == ['g1']


def test_get_transitive_goals_intermediate():
    """_get_transitive_goals follows intermediate goals to parent goals."""
    data = _make_graph(
        tasks=[{'id': 't1', 'kind': 'task'}],
        goals=[
            {'id': 'g1', 'kind': 'goal', 'level': 'intermediate'},
            {'id': 'g2', 'kind': 'goal'},
        ],
        edges=[
            {'from': 't1', 'to': 'g1', 'relation': 'contributes_to'},
            {'from': 'g1', 'to': 'g2', 'relation': 'contributes_to'},
        ],
    )
    p = PLNPropagator(data)
    result = p._get_transitive_goals('t1')
    assert result == ['g1', 'g2']


def test_get_transitive_goals_non_intermediate_skipped():
    """_get_transitive_goals does not follow non-intermediate goals."""
    data = _make_graph(
        tasks=[{'id': 't1', 'kind': 'task'}],
        goals=[
            {'id': 'g1', 'kind': 'goal', 'level': 'top'},
            {'id': 'g2', 'kind': 'goal'},
        ],
        edges=[
            {'from': 't1', 'to': 'g1', 'relation': 'contributes_to'},
            {'from': 'g1', 'to': 'g2', 'relation': 'contributes_to'},
        ],
    )
    p = PLNPropagator(data)
    result = p._get_transitive_goals('t1')
    assert result == ['g1']  # g2 not included because g1.level != 'intermediate'


def test_get_transitive_goals_empty():
    """_get_transitive_goals returns empty list for task with no goals."""
    data = _make_graph(
        tasks=[{'id': 't1', 'kind': 'task'}],
        edges=[],
    )
    p = PLNPropagator(data)
    assert p._get_transitive_goals('t1') == []


# ─── _has_evidence_for ─────────────────────────────────────────────

def test_has_evidence_for_true():
    """_has_evidence_for returns True when provides_evidence_for edge exists."""
    data = _make_graph(
        goals=[{'id': 'g1', 'kind': 'goal'}],
        results=[{'id': 'r1', 'kind': 'result'}],
        edges=[{'from': 'r1', 'to': 'g1', 'relation': 'provides_evidence_for'}],
    )
    p = PLNPropagator(data)
    assert p._has_evidence_for('g1') is True


def test_has_evidence_for_false():
    """_has_evidence_for returns False when no provides_evidence_for edge exists."""
    data = _make_graph(
        goals=[{'id': 'g1', 'kind': 'goal'}],
        edges=[],
    )
    p = PLNPropagator(data)
    assert p._has_evidence_for('g1') is False


def test_has_evidence_for_excludes_other_relations():
    """_has_evidence_for only checks 'provides_evidence_for' edges, not other relations."""
    data = _make_graph(
        goals=[{'id': 'g1', 'kind': 'goal'}],
        tasks=[{'id': 't1', 'kind': 'task'}],
        edges=[{'from': 't1', 'to': 'g1', 'relation': 'contributes_to'}],
    )
    p = PLNPropagator(data)
    assert p._has_evidence_for('g1') is False


# ─── _get_project_for_task ─────────────────────────────────────────

def test_get_project_for_task_found():
    """_get_project_for_task returns project node connected via part_of."""
    data = _make_graph(
        tasks=[{'id': 't1', 'kind': 'task'}],
        projects=[{'id': 'p1', 'kind': 'project'}],
        edges=[{'from': 't1', 'to': 'p1', 'relation': 'part_of'}],
    )
    p = PLNPropagator(data)
    result = p._get_project_for_task('t1')
    assert result is not None
    assert result['id'] == 'p1'


def test_get_project_for_task_none():
    """_get_project_for_task returns None when no part_of edge exists."""
    data = _make_graph(
        tasks=[{'id': 't1', 'kind': 'task'}],
        edges=[],
    )
    p = PLNPropagator(data)
    assert p._get_project_for_task('t1') is None


# ─── _get_superseding_goals ────────────────────────────────────────

def test_get_superseding_goals_basic():
    """_get_superseding_goals returns goals connected via incoming supersedes edges."""
    data = _make_graph(
        goals=[
            {'id': 'g1', 'kind': 'goal'},
            {'id': 'g2', 'kind': 'goal'},
        ],
        edges=[{'from': 'g2', 'to': 'g1', 'relation': 'supersedes'}],
    )
    p = PLNPropagator(data)
    result = p._get_superseding_goals('g1')
    assert result == ['g2']


def test_get_superseding_goals_none():
    """_get_superseding_goals returns empty list when no supersedes edges."""
    data = _make_graph(
        goals=[{'id': 'g1', 'kind': 'goal'}],
        edges=[],
    )
    p = PLNPropagator(data)
    assert p._get_superseding_goals('g1') == []
