#!/usr/bin/env python3
"""Tests for the graph-to-MeTTa atomspace mapper."""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from graph_to_metta import (
    graph_to_metta,
    metta_to_edges,
    count_metta_nodes,
    _atom_id,
    encode_goal,
    encode_task,
    encode_edge,
    KNOWN_RELATIONS,
)

# --- Fixtures ---

SAMPLE_GRAPH = {
    "schema_version": "0.1",
    "as_of": "2026-09-08T00:00:00Z",
    "goals": [
        {"id": "g-build-omegaclaw", "kind": "goal", "title": "Build OmegaClaw",
         "level": "top", "status": "active",
         "priority": {"rank": 1, "urgency": "high"},
         "source": "Ben", "as_of": "2026-08-14T00:00:00Z"}
    ],
    "projects": [
        {"id": "p-research-infra", "kind": "project", "title": "Research infra",
         "source": "Ben", "as_of": "2026-08-14T00:00:00Z",
         "result_contract": {"project_kind": "exploratory_research",
                             "maturity_stage": "E0_exploration"}}
    ],
    "tasks": [
        {"id": "t-hardening-guards", "kind": "task", "title": "Hardening guards",
         "status": "active", "owner": "scheduler", "reversibility": "irreversible",
         "source": "scheduler", "as_of": "2026-08-25T00:00:00Z"}
    ],
    "resources": [
        {"id": "r-shared-runtime", "kind": "resource", "title": "Shared runtime",
         "resource_type": "process", "exclusive": True,
         "source": "system", "as_of": "2026-08-01T00:00:00Z"}
    ],
    "results": [],
    "constraints": [
        {"id": "c-deploy-freeze", "kind": "constraint", "title": "Deploy freeze"}
    ],
    "edges": [
        {"from": "t-hardening-guards", "to": "g-build-omegaclaw",
         "relation": "contributes_to", "confidence": "medium"},
        {"from": "t-hardening-guards", "to": "p-research-infra",
         "relation": "part_of", "confidence": "high"},
        {"from": "t-hardening-guards", "to": "r-shared-runtime",
         "relation": "occupies", "confidence": "high"},
        {"from": "c-deploy-freeze", "to": "t-hardening-guards",
         "relation": "blocks", "confidence": "high"}
    ]
}


# --- Tests ---

def test_atom_id_sanitization():
    assert _atom_id("g-build-omegaclaw") == "g_build_omegaclaw"
    assert _atom_id("p.1.2") == "p_1_2"
    assert _atom_id("plain") == "plain"


def test_goal_encoding():
    goal = SAMPLE_GRAPH["goals"][0]
    s = encode_goal(goal)
    assert "(: g_g_build_omegaclaw Goal)" in s
    assert '"Build OmegaClaw"' in s
    assert "top" in s
    assert "active" in s
    assert "1" in s  # rank
    assert "high" in s  # urgency


def test_task_encoding():
    task = SAMPLE_GRAPH["tasks"][0]
    s = encode_task(task)
    assert "(: t_t_hardening_guards Task)" in s
    assert '"Hardening guards"' in s
    assert "irreversible" in s


def test_edge_encoding():
    # Build node_lookup from sample graph so edges get prefixed IDs
    node_lookup = {}
    for n in SAMPLE_GRAPH["goals"] + SAMPLE_GRAPH["projects"] + SAMPLE_GRAPH["tasks"] + SAMPLE_GRAPH["resources"] + SAMPLE_GRAPH.get("constraints", []):
        node_lookup[n["id"]] = n
    edge = SAMPLE_GRAPH["edges"][0]
    s = encode_edge(edge, node_lookup)
    assert "(contributes_to t_t_hardening_guards g_g_build_omegaclaw)" in s


def test_graph_to_metta_basic():
    metta = graph_to_metta(SAMPLE_GRAPH)
    # Type declarations present
    assert "(: Goal Concept)" in metta
    assert "(: Task Concept)" in metta
    # Nodes encoded
    assert "g_g_build_omegaclaw" in metta
    assert "t_t_hardening_guards" in metta
    assert "r_r_shared_runtime" in metta
    # Edges encoded
    assert "(contributes_to t_t_hardening_guards g_g_build_omegaclaw)" in metta
    assert "(part_of t_t_hardening_guards p_p_research_infra)" in metta
    assert "(occupies t_t_hardening_guards r_r_shared_runtime)" in metta
    assert "(blocks c_c_deploy_freeze t_t_hardening_guards)" in metta
    # Verdict rules present
    assert "check_stop_stale" in metta
    assert "check_defer" in metta
    assert "evaluate_task" in metta


def test_metta_to_edges_roundtrip():
    metta = graph_to_metta(SAMPLE_GRAPH)
    edges = metta_to_edges(metta)
    # Should have at least 4 edges
    assert len(edges) >= 4
    # Each edge should have from, to, relation
    for e in edges:
        assert "from" in e
        assert "to" in e
        assert e["relation"] in KNOWN_RELATIONS


def test_count_metta_nodes():
    metta = graph_to_metta(SAMPLE_GRAPH)
    counts = count_metta_nodes(metta)
    assert counts["goal"] == 1
    assert counts["project"] == 1
    assert counts["task"] == 1
    assert counts["resource"] == 1
    assert counts["constraint"] == 1


def test_replay_corpus_roundtrip():
    """Test that all 5 replay episodes generate valid MeTTa."""
    corpus_dir = os.path.join(os.path.dirname(__file__), "..", "replay_corpus")
    episodes = [
        "episode_01_stale_codegen.json",
        "episode_02_chem_blocking.json",
        "episode_03_premature_hardening.json",
        "episode_04_overengineered_repair.json",
        "episode_05_control_justified_long_running.json",
    ]
    for ep in episodes:
        path = os.path.join(corpus_dir, ep)
        if not os.path.exists(path):
            continue
        with open(path) as f:
            data = json.load(f)
        metta = graph_to_metta(data)
        assert "(: Goal Concept)" in metta
        edges = metta_to_edges(metta)
        # Every episode should have at least one contributes_to edge
        ct_edges = [e for e in edges if e["relation"] == "contributes_to"]
        assert len(ct_edges) >= 1, f"{ep}: no contributes_to edges found"
        # Verdict rules present
        assert "evaluate_task" in metta


def test_empty_graph():
    """Empty graph should produce valid but minimal MeTTa."""
    empty = {
        "schema_version": "0.1",
        "as_of": "2026-09-08T00:00:00Z",
        "goals": [], "projects": [], "tasks": [],
        "resources": [], "results": [], "constraints": [],
        "edges": []
    }
    metta = graph_to_metta(empty)
    assert "(: Goal Concept)" in metta
    edges = metta_to_edges(metta)
    assert len(edges) == 0


def test_verdict_rules_structure():
    """Verify all 6 verdict rules + default are present in output."""
    metta = graph_to_metta(SAMPLE_GRAPH)
    for rule_name in ["check_stop_stale", "check_blocked", "check_pause_recoverably",
                      "check_defer", "check_replan", "check_escalate", "evaluate_task"]:
        assert rule_name in metta, f"Missing verdict rule: {rule_name}"
    for verdict in ["STOP_STALE", "BLOCKED", "PAUSE_RECOVERABLY",
                    "DEFER", "REPLAN", "ESCALATE", "CONTINUE"]:
        assert verdict in metta, f"Missing verdict atom: {verdict}"


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except Exception as e:
            print(f"  FAIL  {t.__name__}: {e}")
            failed += 1
    print(f"\n{passed}/{passed+failed} tests passed")
    if failed:
        sys.exit(1)
