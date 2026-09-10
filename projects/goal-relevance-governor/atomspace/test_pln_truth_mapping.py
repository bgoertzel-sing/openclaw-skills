"""Tests for PLN truth-value mapping."""

import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from pln_truth_mapping import (
    TruthValue, status_to_truth, edge_to_truth, verdict_to_truth,
    pln_and, pln_or, pln_not, graph_to_pln_atoms, export_pln_json,
    compute_task_relevance,
)


def test_truth_value_defaults():
    assert status_to_truth("active").strength == 1.0
    assert status_to_truth("achieved").confidence == 1.0
    assert status_to_truth("cancelled").strength == 0.0
    assert status_to_truth("superseded").strength == 0.0

def test_edge_truth():
    assert edge_to_truth("contributes_to").strength == 1.0
    assert edge_to_truth("blocks").strength == 0.0

def test_verdict_truth():
    assert verdict_to_truth("CONTINUE").strength == 1.0
    assert verdict_to_truth("STOP_STALE").strength == 0.0

def test_pln_and():
    tv1 = TruthValue(0.8, 0.9)
    tv2 = TruthValue(0.6, 0.7)
    result = pln_and(tv1, tv2)
    assert result.strength == 0.6
    assert abs(result.confidence - 0.63) < 0.01

def test_pln_or():
    tv1 = TruthValue(0.8, 0.9)
    tv2 = TruthValue(0.6, 0.7)
    result = pln_or(tv1, tv2)
    assert result.strength == 0.8
    assert result.confidence == 0.9

def test_pln_not():
    tv = TruthValue(0.8, 0.9)
    result = pln_not(tv)
    assert abs(result.strength - 0.2) < 1e-9
    assert result.confidence == 0.9

def test_graph_to_pln_atoms():
    graph = {
        "tasks": [{"id": "t1", "kind": "task", "status": "active", "title": "T1"}],
        "goals": [{"id": "g1", "kind": "goal", "status": "active", "title": "G1"}],
        "edges": [{"from": "t1", "to": "g1", "relation": "contributes_to"}],
    }
    atoms = graph_to_pln_atoms(graph)
    assert len(atoms) == 3
    names = [a["name"] for a in atoms]
    assert "t1" in names
    assert "g1" in names

def test_export_pln_json():
    graph = {
        "tasks": [{"id": "t1", "kind": "task", "status": "active", "title": "T1"}],
        "goals": [{"id": "g1", "kind": "goal", "status": "achieved", "title": "G1"}],
        "edges": [{"from": "t1", "to": "g1", "relation": "contributes_to"}],
    }
    s = export_pln_json(graph)
    data = json.loads(s)
    assert data["format"] == "PLN-AtomSpace-JSON-v0.1"
    assert len(data["atoms"]) == 3

def test_compute_relevance_active_goal():
    graph = {
        "tasks": [{"id": "t1", "kind": "task", "status": "active"}],
        "goals": [{"id": "g1", "kind": "goal", "status": "active"}],
        "edges": [{"from": "t1", "to": "g1", "relation": "contributes_to"}],
    }
    tv = compute_task_relevance(graph, "t1")
    assert tv.strength == 1.0

def test_compute_relevance_achieved_goal():
    graph = {
        "tasks": [{"id": "t1", "kind": "task", "status": "active"}],
        "goals": [{"id": "g1", "kind": "goal", "status": "achieved"}],
        "edges": [{"from": "t1", "to": "g1", "relation": "contributes_to"}],
    }
    tv = compute_task_relevance(graph, "t1")
    assert tv.strength == 1.0  # achieved has strength 1.0
    assert abs(tv.confidence - 0.9) < 1e-9  # AND(achieved, contributes_to) = 0.9

def test_compute_relevance_no_goals():
    graph = {
        "tasks": [{"id": "t1", "kind": "task", "status": "active"}],
        "goals": [],
        "edges": [],
    }
    tv = compute_task_relevance(graph, "t1")
    assert tv.strength == 0.0

def test_compute_relevance_cancelled_goal():
    graph = {
        "tasks": [{"id": "t1", "kind": "task", "status": "active"}],
        "goals": [{"id": "g1", "kind": "goal", "status": "cancelled"}],
        "edges": [{"from": "t1", "to": "g1", "relation": "contributes_to"}],
    }
    tv = compute_task_relevance(graph, "t1")
    assert tv.strength == 0.0

def test_compute_relevance_mixed_goals():
    graph = {
        "tasks": [{"id": "t1", "kind": "task", "status": "active"}],
        "goals": [
            {"id": "g1", "kind": "goal", "status": "cancelled"},
            {"id": "g2", "kind": "goal", "status": "active"},
        ],
        "edges": [
            {"from": "t1", "to": "g1", "relation": "contributes_to"},
            {"from": "t1", "to": "g2", "relation": "contributes_to"},
        ],
    }
    tv = compute_task_relevance(graph, "t1")
    # OR of cancelled(0.0) and active(1.0) = 1.0
    assert tv.strength == 1.0
