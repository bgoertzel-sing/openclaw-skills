import sys, os
sys.path.insert(0, 'atomspace')
sys.path.insert(0, 'evaluator')

import pytest
from datetime import datetime, timezone, timedelta

# ─── pln_verdict_bridge: verdicts_disagree ────────────────────────────
from pln_verdict_bridge import compute_staleness, PLNVerdictBridge

def test_verdicts_disagree_same():
    assert PLNVerdictBridge.verdicts_disagree('CONTINUE', 'CONTINUE') == False

def test_verdicts_disagree_diff():
    assert PLNVerdictBridge.verdicts_disagree('CONTINUE', 'PAUSE_RECOVERABLY') == True
    assert PLNVerdictBridge.verdicts_disagree('STOP_STALE', 'CONTINUE') == True

def test_verdicts_disagree_empty():
    assert PLNVerdictBridge.verdicts_disagree('', '') == False

# ─── pln_verdict_bridge: compute_staleness ──────────────────────────
def test_compute_staleness_fresh():
    now = datetime(2026, 9, 8, tzinfo=timezone.utc)
    goal = {'last_updated': '2026-09-07T00:00:00Z'}
    assert compute_staleness(goal, now=now) == False

def test_compute_staleness_stale():
    now = datetime(2026, 9, 8, tzinfo=timezone.utc)
    goal = {'last_updated': '2026-08-01T00:00:00Z'}
    assert compute_staleness(goal, now=now) == True

def test_compute_staleness_no_timestamp():
    now = datetime(2026, 9, 8, tzinfo=timezone.utc)
    goal = {'id': 'g1'}
    assert compute_staleness(goal, now=now) == False

def test_compute_staleness_as_of_field():
    now = datetime(2026, 9, 8, tzinfo=timezone.utc)
    goal = {'as_of': '2026-08-01T00:00:00Z'}
    assert compute_staleness(goal, now=now) == True

def test_compute_staleness_updated_at_field():
    now = datetime(2026, 9, 8, tzinfo=timezone.utc)
    goal = {'updated_at': '2026-08-01T00:00:00Z'}
    assert compute_staleness(goal, now=now) == True

def test_compute_staleness_custom_threshold():
    now = datetime(2026, 9, 8, tzinfo=timezone.utc)
    goal = {'last_updated': '2026-09-06T00:00:00Z'}  # 2 days old
    assert compute_staleness(goal, now=now, threshold_days=1) == True
    assert compute_staleness(goal, now=now, threshold_days=7) == False

def test_compute_staleness_invalid_timestamp():
    now = datetime(2026, 9, 8, tzinfo=timezone.utc)
    goal = {'last_updated': 'not-a-date'}
    assert compute_staleness(goal, now=now) == False

# ─── relevance_evaluator Graph: get_resource_holders, get_project_for_task ──
from relevance_evaluator import Graph

def _make_graph_with_resources():
    return Graph({
        'goals': [{'id': 'g1', 'status': 'active', 'priority': 1.0}],
        'tasks': [
            {'id': 't1', 'kind': 'task', 'status': 'active', 'goal': 'g1'},
            {'id': 't2', 'kind': 'task', 'status': 'active', 'goal': 'g1'},
        ],
        'resources': [
            {'id': 'r1', 'kind': 'resource', 'exclusivity': 'exclusive', 'status': 'active'},
        ],
        'projects': [
            {'id': 'p1', 'kind': 'project', 'status': 'active', 'stage': 'in_progress'},
        ],
        'edges': [
            {'from': 't1', 'to': 'r1', 'relation': 'occupies'},
            {'from': 't2', 'to': 'r1', 'relation': 'occupies'},
            {'from': 't1', 'to': 'p1', 'relation': 'part_of'},
        ],
    })

def test_graph_get_resource_holders():
    g = _make_graph_with_resources()
    holders = g.get_resource_holders('r1')
    assert len(holders) == 2
    ids = {h['id'] for h in holders}
    assert ids == {'t1', 't2'}

def test_graph_get_resource_holders_no_holders():
    g = _make_graph_with_resources()
    holders = g.get_resource_holders('nonexistent')
    assert holders == []

def test_graph_get_resource_holders_inactive_excluded():
    g = Graph({
        'tasks': [
            {'id': 't1', 'kind': 'task', 'status': 'finished', 'goal': 'g1'},
        ],
        'resources': [{'id': 'r1', 'kind': 'resource', 'status': 'active'}],
        'edges': [{'from': 't1', 'to': 'r1', 'relation': 'occupies'}],
        'goals': [{'id': 'g1', 'status': 'active'}],
    })
    holders = g.get_resource_holders('r1')
    assert holders == [], 'finished task should not be counted as active holder'

def test_graph_get_project_for_task():
    g = _make_graph_with_resources()
    proj = g.get_project_for_task('t1')
    assert proj is not None
    assert proj['id'] == 'p1'
    assert proj['kind'] == 'project'

def test_graph_get_project_for_task_none():
    g = _make_graph_with_resources()
    proj = g.get_project_for_task('t2')
    assert proj is None


# ─── metta_evaluator: get_goal_info, get_task_info, get_resource_info ──
from metta_evaluator import MeTTaEvaluator
from hyperon import MeTTa

def _make_metta():
    m = MeTTaEvaluator.__new__(MeTTaEvaluator)
    m.metta = MeTTa()
    m._setup_types()
    m.metta.run('''
    ; Goals
    (g1 "Improve codegen" strategic active 2 0.8)
    ; Tasks
    (t1 "Refactor parser" active reversible)
    (t2 "Write tests" active irreversible)
    ; Resources
    (r1 compute exclusive active)
    ; Projects
    (p1 project in_progress)
    ; Edges
    (contributes_to t1 g1)
    (holds t1 r1)
    (part_of t1 p1)
    (provides_evidence_for result1 g1)
    ''')
    return m

def test_metta_get_goal_info():
    from hyperon import MeTTa
    ev = _make_metta()
    info = ev.get_goal_info("g1")
    assert info is not None
    assert info["status"] == "active"
    assert info["title"] == "Improve codegen"

def test_metta_get_goal_info_missing():
    ev = _make_metta()
    info = ev.get_goal_info("nonexistent")
    assert info is None

def test_metta_get_task_info():
    ev = _make_metta()
    info = ev.get_task_info("t1")
    assert info is not None
    assert info["status"] == "active"
    assert info["title"] == "Refactor parser"
    assert info["reversibility"] == "reversible"

def test_metta_get_task_info_missing():
    ev = _make_metta()
    info = ev.get_task_info("nonexistent")
    assert info is None

def test_metta_get_resource_info():
    ev = _make_metta()
    info = ev.get_resource_info("r1")
    assert info is not None
    assert info["kind"] == "compute"
    assert info["exclusivity"] == "exclusive"
    assert info["status"] == "active"

def test_metta_get_resource_info_missing():
    ev = _make_metta()
    info = ev.get_resource_info("nonexistent")
    assert info is None

def test_metta_get_held_resources():
    ev = _make_metta()
    resources = ev.get_held_resources("t1")
    assert len(resources) == 1
    assert "r1" in str(resources[0])

def test_metta_get_held_resources_none():
    ev = _make_metta()
    resources = ev.get_held_resources("t2")
    assert resources == []

def test_metta_get_resource_holders():
    ev = _make_metta()
    holders = ev.get_resource_holders("r1")
    assert len(holders) == 1
    assert "t1" in str(holders[0])

def test_metta_get_project_for_task():
    ev = _make_metta()
    proj = ev.get_project_for_task("t1")
    assert proj is not None
    assert "p1" in str(proj)

def test_metta_get_project_for_task_none():
    ev = _make_metta()
    proj = ev.get_project_for_task("t2")
    assert proj is None

def test_metta_get_project_info():
    ev = _make_metta()
    info = ev.get_project_info("p1")
    assert info is not None
    assert info["kind"] == "project"
    assert info["stage"] == "in_progress"

def test_metta_get_project_info_missing():
    ev = _make_metta()
    info = ev.get_project_info("nonexistent")
    assert info is None

def test_metta_has_results_for_goal_true():
    ev = _make_metta()
    assert ev.has_results_for_goal("g1") == True

def test_metta_has_results_for_goal_false():
    ev = _make_metta()
    assert ev.has_results_for_goal("nonexistent") == False

