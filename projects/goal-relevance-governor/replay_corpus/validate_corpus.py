#!/usr/bin/env python3
"""Replay corpus validation harness for the Goal Relevance Governor."""

import json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "evaluator"))
from relevance_evaluator import Graph, RelevanceEvaluator

def run_corpus(corpus_dir):
    corpus = pathlib.Path(corpus_dir)
    episodes = sorted(corpus.glob("episode_*.json"))
    if not episodes:
        return [], "No episode files found"
    results = []
    all_pass = True
    for ep_path in episodes:
        data = json.loads(ep_path.read_text())
        expected = data.get("expected_verdict", "")
        g = Graph(data)
        ev = RelevanceEvaluator(g)
        verdicts = ev.evaluate_all()
        if not verdicts:
            results.append((ep_path.name, expected, "NO_TASKS", False))
            all_pass = False
            continue
        v = verdicts[0]
        matched = (v.verdict == expected)
        results.append((ep_path.name, expected, v.verdict, matched))
        if not matched:
            all_pass = False
    return results, "OK" if all_pass else "FAIL"

if __name__ == "__main__":
    corpus_dir = sys.argv[1] if len(sys.argv) > 1 else str(pathlib.Path(__file__).resolve().parent)
    results, status = run_corpus(corpus_dir)
    total_pass = sum(1 for r in results if r[3])
    print(f"{total_pass}/{len(results)} episodes passed ({status})")
    sys.exit(0 if status == "OK" else 1)
