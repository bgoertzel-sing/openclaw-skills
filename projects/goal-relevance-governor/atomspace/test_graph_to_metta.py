#!/usr/bin/env python3
"""Tests for graph_to_metta atomspace mapper."""

import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from atomspace.graph_to_metta import (
    graph_to_metta, metta_to_edges, count_metta_nodes,
    _atom_id, encode_goal, encode_task, encode_edge
)

REPLAY_DIR = os.path.join(os.path.dirname(__file__), "..", "replay_corpus")


def load_episode(name):
    with open(os.path.join(REPLAY_DIR, name)) as f:
        return json.load(f)


def test_atom_id_sanitization():
    assert _atom_id("g-build-omegaclaw") == "g_build_omegaclaw"
    assert _atom_id("t-p2m-codegen") == "t_p2m_codegen"
    assert _atom_id("v1.2") == "v1_2"
    print("PASS test_atom_id_sanitization")


def test_encode_goal():
    node = {
        "id": "g-test",
        "kind": "goal",
        "title": "Test Goal",
        "level": "top",
        "status": "active",
        "priority": {"rank": 1, "urgency": "high"}
    }
    out = encode_goal(node)
    assert ": g_g_test Goal" in out
    assert "Test Goal" in out
    assert "active" in out
    assert "1" in out
    assert "high" in out
    print("PASS test_encode_goal")


def test_encode_task():
    node = {
        "id": "t-foo",
        "kind": "task",
        "title": "Foo Task",
        "status": "active",
        "reversibility": "checkpointable"
    }
    out = encode_task(node)
    assert ": t_t_foo Task" in out
    assert "Foo Task" in out
    assert "active" in out
    assert "checkpointable" in out
    print("PASS test_encode_task")


def test_encode_edge():
    edge = {"from": "t-foo", "to": "g-bar", "relation": "contributes_to"}
    out = encode_edge(edge)
    assert "(contributes_to t_foo g_bar)" == out
    print("PASS test_encode_edge")


def test_full_graph_to_metta_episode_01():
    data = load_episode("episode_01_stale_codegen.json")
    metta = graph_to_metta(data)
    # Should contain type declarations
    assert "(: Goal Concept)" in metta
    assert "(: Task Concept)" in metta
    # Should contain node declarations
    assert "g_initial_demo" in metta
    assert "g_build_omegaclaw" in metta
    assert "t_p2m_codegen" in metta
    # Should contain edges
    assert "(contributes_to t_t_p2m_codegen g_g_initial_demo)" in metta
    # Should contain verdict rules
    assert "check_stop_stale" in metta
    assert "evaluate_task" in metta
    print("PASS test_full_graph_to_metta_episode_01")


def test_metta_to_edges_roundtrip():
    data = load_episode("episode_01_stale_codegen.json")
    metta = graph_to_metta(data)
    edges = metta_to_edges(metta)
    # Original has 2 edges
    assert len(edges) == 2
    rels = {e["relation"] for e in edges}
    assert "contributes_to" in rels
    print("PASS test_metta_to_edges_roundtrip")


def test_count_nodes_episode_01():
    data = load_episode("episode_01_stale_codegen.json")
    metta = graph_to_metta(data)
    counts = count_metta_nodes(metta)
    assert counts["goal"] == 3  # g-initial-demo, g-build-omegaclaw, g-ir-translation-v2
    assert counts["task"] == 1  # t-p2m-codegen
    print("PASS test_count_nodes_episode_01")


def test_count_nodes_episode_02():
    data = load_episode("episode_02_chem_blocking.json")
    metta = graph_to_metta(data)
    counts = count_metta_nodes(metta)
    assert counts["goal"] == 3
    assert counts["task"] == 2
    assert counts["resource"] == 1
    print("PASS test_count_nodes_episode_02")


def test_all_5_episodes_generate_valid_metta():
    for i in range(1, 6):
        fname = sorted(os.listdir(REPLAY_DIR))[i-1]  # rough
    # More explicit:
    episodes = [
        "episode_01_stale_codegen.json",
        "episode_02_chem_blocking.json",
        "episode_03_premature_hardening.json",
        "episode_04_overengineered_repair.json",
        "episode_05_control_justified_long_running.json",
    ]
    for ep in episodes:
        data = load_episode(ep)
        metta = graph_to_metta(data)
        assert "(: Goal Concept)" in metta
        assert "evaluate_task" in metta
        edges = metta_to_edges(metta)
        assert len(edges) > 0, f"No edges found for {ep}"
    print("PASS test_all_5_episodes_generate_valid_metta")


def test_verdict_rules_present():
    data = load_episode("episode_01_stale_codegen.json")
    metta = graph_to_metta(data)
    for rule_name in ["check_stop_stale", "check_blocked",
                       "check_pause_recoverably", "check_defer",
                       "check_replan", "check_escalate", "evaluate_task"]:
        assert rule_name in metta, f"Missing rule: {rule_name}"
    print("PASS test_verdict_rules_present")


if __name__ == "__main__":
    test_atom_id_sanitization()
    test_encode_goal()
    test_encode_task()
    test_encode_edge()
    test_full_graph_to_metta_episode_01()
    test_metta_to_edges_roundtrip()
    test_count_nodes_episode_01()
    test_count_nodes_episode_02()
    test_all_5_episodes_generate_valid_metta()
    test_verdict_rules_present()
    print("\nAll atomspace mapper tests passed!")
