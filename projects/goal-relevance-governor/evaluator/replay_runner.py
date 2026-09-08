#!/usr/bin/env python3
"""Replay runner: evaluate all episodes in the replay corpus and check verdicts."""

import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from relevance_evaluator import Graph, RelevanceEvaluator

CORPUS_DIR = os.path.join(os.path.dirname(__file__), "..", "replay_corpus")

def run_replay(verbose=False):
    """Run the replay corpus and return True if all episodes match expected verdicts."""
    episodes = sorted(f for f in os.listdir(CORPUS_DIR) if f.startswith("episode_") and f.endswith(".json"))
    results = []
    all_pass = True
    for fname in episodes:
        path = os.path.join(CORPUS_DIR, fname)
        data = json.load(open(path))
        g = Graph(data)
        ev = RelevanceEvaluator(g)
        verdicts = ev.evaluate_all()
        expected = data.get("base_expected_verdict", data.get("expected_verdict", "?"))
        v = verdicts[0]
        match = (v.verdict == expected)
        if not match:
            all_pass = False
        results.append({
            "episode": data.get("episode_id", fname),
            "task": v.task_id,
            "expected": expected,
            "actual": v.verdict,
            "match": match,
        })
        if verbose or not match:
            status = 'PASS' if match else 'FAIL'
            print(f"{status} {data.get('episode_id','?')}: expected={expected}, actual={v.verdict}")
            if not match:
                print(f"  reasons: {v.reasons}")
                print(f"  evidence: {v.evidence}")
    correct = sum(1 for r in results if r['match'])
    print(f"\n{correct}/{len(results)} episodes correct")
    return all_pass

if __name__ == "__main__":
    ok = run_replay(verbose="--quiet" not in sys.argv)
    sys.exit(0 if ok else 1)
