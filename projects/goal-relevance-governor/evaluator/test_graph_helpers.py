"""Tests for get_blocking_constraints and get_superseding_goals on pure-Python Graph."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'evaluator'))

import pytest
from relevance_evaluator import Graph, Verdict


def _ids(nodes):
    """Extract sorted IDs from list of node dicts."""
    return sorted(n['id'] for n in nodes)


def test_get_blocking_constraints():
    """get_blocking_constraints returns tasks blocking a given task via 'blocks' edges."""
    data = {
        'tasks': [
            {'id': 't1'},
            {'id': 't2'},
            {'id': 't3'},
        ],
        'edges': [
            {'from': 't2', 'to': 't1', 'relation': 'blocks'},
            {'from': 't3', 'to': 't1', 'relation': 'blocks'},
        ],
    }
    g = Graph(data)
    blockers = g.get_blocking_constraints('t1')
    assert _ids(blockers) == ['t2', 't3']


def test_get_blocking_constraints_no_blockers():
    """get_blocking_constraints returns empty list when no blockers exist."""
    data = {
        'tasks': [{'id': 't1'}],
        'edges': [],
    }
    g = Graph(data)
    blockers = g.get_blocking_constraints('t1')
    assert blockers == []


def test_get_blocking_constraints_nonexistent_task():
    """get_blocking_constraints returns empty list for nonexistent task."""
    data = {'edges': []}
    g = Graph(data)
    blockers = g.get_blocking_constraints('nonexistent')
    assert blockers == []


def test_get_blocking_constraints_excludes_non_blocks():
    """get_blocking_constraints only returns 'blocks' edges, not other relations."""
    data = {
        'tasks': [
            {'id': 't1'},
            {'id': 't2'},
            {'id': 't3'},
        ],
        'edges': [
            {'from': 't2', 'to': 't1', 'relation': 'blocks'},
            {'from': 't3', 'to': 't1', 'relation': 'contributes_to'},
        ],
    }
    g = Graph(data)
    blockers = g.get_blocking_constraints('t1')
    assert _ids(blockers) == ['t2']


def test_get_superseding_goals():
    """get_superseding_goals returns goals that supersede a given goal via 'supersedes' edges."""
    data = {
        'goals': [
            {'id': 'g1'},
            {'id': 'g2'},
            {'id': 'g3'},
        ],
        'edges': [
            {'from': 'g2', 'to': 'g1', 'relation': 'supersedes'},
            {'from': 'g3', 'to': 'g1', 'relation': 'supersedes'},
        ],
    }
    g = Graph(data)
    supers = g.get_superseding_goals('g1')
    assert _ids(supers) == ['g2', 'g3']


def test_get_superseding_goals_no_superseding():
    """get_superseding_goals returns empty list when no superseding goals exist."""
    data = {
        'goals': [{'id': 'g1'}],
        'edges': [],
    }
    g = Graph(data)
    supers = g.get_superseding_goals('g1')
    assert supers == []


def test_get_superseding_goals_nonexistent():
    """get_superseding_goals returns empty list for nonexistent goal."""
    data = {'edges': []}
    g = Graph(data)
    supers = g.get_superseding_goals('nonexistent')
    assert supers == []
