"""Tests for the hybrid Python-MeTTa evaluator v0.3.

Cross-validates against relevance_evaluator.py rule cascade.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from metta_evaluator import MeTTaEvaluator


EPISODE_01 = r'''
(: t_codegen Task)
(t_codegen "P2M codegen migration" active reversible)
(: g_p2m Goal)
(g_p2m "P2M complete" terminal achieved 2 medium)
(: g_test Goal)
(g_test "Full test suite pass" terminal achieved 1 medium)
(contributes_to t_codegen g_p2m)
(contributes_to t_codegen g_test)
(supersedes g_test g_p2m)
'''

EPISODE_02 = r'''
(: t_chem Task)
(t_chem "Chemistry RL training" active reversible)
(: g_chem Goal)
(g_chem "Chem RL converged" intermediate active 2 high)
(contributes_to t_chem g_chem)
(: c_gpu Constraint)
(c_gpu "GPU unavailable" hard)
(blocks c_gpu t_chem)
'''

EPISODE_03 = r'''
(: t_hard Task)
(t_hard "Premature hardening fix" active reversible)
(: g_old Goal)
(g_old "Old approach" intermediate superseded 2 medium)
(: g_new Goal)
(g_new "New approach" intermediate active 2 high)
(contributes_to t_hard g_old)
(supersedes g_new g_old)
'''

EPISODE_04 = r'''
(: t_healthy Task)
(t_healthy "Normal task" active reversible)
(: g_active Goal)
(g_active "Active goal" intermediate active 2 medium)
(contributes_to t_healthy g_active)
'''

EPISODE_05 = r'''
(: t_orphan Task)
(t_orphan "Orphan task" active reversible)
'''


def test_episode_01_stale():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_01)
    assert ev.evaluate("t_codegen") == "STOP_STALE"

def test_episode_02_blocked():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_02)
    assert ev.evaluate("t_chem") == "BLOCKED"

def test_episode_03_replan():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_03)
    assert ev.evaluate("t_hard") == "REPLAN"

def test_episode_04_continue():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_04)
    assert ev.evaluate("t_healthy") == "CONTINUE"

def test_episode_05_no_goals():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_05)
    assert ev.evaluate("t_orphan") == "STOP_STALE"

def test_get_direct_goals():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_01)
    goals = ev.get_direct_goals("t_codegen")
    assert set(goals) == {"g_p2m", "g_test"}

def test_get_goal_status():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_01)
    assert ev.get_goal_status("g_p2m") == "achieved"
    assert ev.get_goal_status("g_test") == "achieved"

def test_has_active_goal_false():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_01)
    goals = ev.get_direct_goals("t_codegen")
    statuses = [ev.get_goal_status(g) for g in goals]
    assert all(s in ("achieved", "cancelled") for s in statuses)

def test_has_active_goal_true():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_04)
    goals = ev.get_direct_goals("t_healthy")
    statuses = [ev.get_goal_status(g) for g in goals]
    assert any(s == "active" for s in statuses)

def test_get_blocking_constraints():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_02)
    blockers = ev.get_blocking_constraints("t_chem")
    assert "c_gpu" in blockers

def test_no_blocking_constraints():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_04)
    blockers = ev.get_blocking_constraints("t_healthy")
    assert blockers == []

def test_get_superseding_goals():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_03)
    supers = ev.get_superseding_goals("g_old")
    assert "g_new" in supers

def test_replan_requires_superseded_status():
    """REPLAN requires both status=superseded AND supersedes edge."""
    ev = MeTTaEvaluator()
    ev.load_string(r'''
    (: t Task)
    (t "test" active reversible)
    (: g Goal)
    (g "goal" intermediate active 2 medium)
    (: g2 Goal)
    (g2 "new goal" intermediate active 1 high)
    (contributes_to t g)
    (supersedes g2 g)
    ''')
    # g is still active (not superseded), so no REPLAN
    assert ev.evaluate("t") == "CONTINUE"

def test_cancelled_goal_is_stale():
    ev = MeTTaEvaluator()
    ev.load_string(r'''
    (: t Task)
    (t "test" active reversible)
    (: g Goal)
    (g "cancelled goal" terminal cancelled 1 medium)
    (contributes_to t g)
    ''')
    assert ev.evaluate("t") == "STOP_STALE"

def test_mixed_goals():
    """Task with one achieved and one active goal -> CONTINUE."""
    ev = MeTTaEvaluator()
    ev.load_string(r'''
    (: t_mixed Task)
    (t_mixed "mixed" active reversible)
    (: g_done Goal)
    (g_done "done" terminal achieved 1 medium)
    (: g_active Goal)
    (g_active "active" intermediate active 2 high)
    (contributes_to t_mixed g_done)
    (contributes_to t_mixed g_active)
    ''')
    assert ev.evaluate("t_mixed") == "CONTINUE"

def test_evaluate_all():
    ev = MeTTaEvaluator()
    ev.load_string(EPISODE_01)
    ev.load_string(EPISODE_04)
    results = ev.evaluate_all()
    assert results["t_codegen"] == "STOP_STALE"
    assert results["t_healthy"] == "CONTINUE"
