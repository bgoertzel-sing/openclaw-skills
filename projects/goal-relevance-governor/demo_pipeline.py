#!/usr/bin/env python3
"""
Goal Relevance Governor v0.2 — End-to-End Demo

Runs the full pipeline on all 5 replay episodes:
  Episode Data → PLN → ECAN → Verdict → Multi-hop → Conflict → Explainer → Remediation → Temporal

Usage:
    python3 demo_pipeline.py [episode_file]
    python3 demo_pipeline.py --all
"""
import sys, os, json, time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'atomspace'))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'evaluator'))

from integrated_governor import IntegratedGovernorPipeline
from remediation_engine import RemediationEngine
from reasoning_explainer import ReasoningExplainer
from temporal_simulator import TemporalSimulator


REPLAY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'replay_corpus')


def run_episode(ep_path, verbose=True):
    with open(ep_path) as f:
        data = json.load(f)

    print(f'\n{"="*72}')
    print(f'  EPISODE: {os.path.basename(ep_path)}')
    print(f'  Title: {data.get("episode_title", "?")}')
    print(f'  Expected: {data.get("expected_verdict", "?")}')
    print(f'{"="*72}\n')

    # 1. Run pipeline
    t0 = time.perf_counter()
    pipeline = IntegratedGovernorPipeline(data)
    result = pipeline.run(ecan_cycles=10).to_dict()
    t1 = time.perf_counter()

    recs = result['recommendations']
    print(f'  Pipeline: {len(recs)} recommendation(s) in {(t1-t0)*1000:.1f}ms\n')

    # 2. Remediation
    engine = RemediationEngine(data)
    plans = engine.generate_all(recs)
    t2 = time.perf_counter()
    print(f'  Remediation: {len(plans)} plan(s) in {(t2-t1)*1000:.1f}ms\n')

    for i, (rec, plan) in enumerate(zip(recs, plans)):
        print(f'  [{i+1}] Task: {rec["task_id"]}')
        print(f'      Verdict: {rec["unified_verdict"]}')
        print(f'      Signals: {", ".join(rec.get("signals", []))}')
        print(f'      Plan: {plan.plan_summary}')
        for step in plan.steps:
            deps = f' (after {",".join(step.depends_on)})' if step.depends_on else ''
            print(f'        P{step.priority}: {step.action} -> {step.target}{deps}')
        print(f'      Success: {plan.success_criteria}')
        print(f'      Risk: {plan.risk_notes}')
        print()

    # 3. Reasoning explanation
    explainer = ReasoningExplainer(data)
    explanations = explainer.explain_all(result)
    t3 = time.perf_counter()
    print(f'  Explanation: {len(explanations)} explanation(s) in {(t3-t2)*1000:.1f}ms\n')

    for exp in explanations:
        print(f"  [{exp.task_id}] {exp.verdict}: {exp.headline}")
        if exp.evidence_points:
            for ev in exp.evidence_points:
                print(f'        - {ev}')
        print()

    # 4. Temporal simulation
    sim = TemporalSimulator(data)
    timelines = {
        'episode_01': 'create_timeline_stale_task',
        'episode_02': 'create_timeline_conflict_resolution',
        'episode_03': 'create_timeline_premature_to_justified',
    }
    ep_key = os.path.basename(ep_path).replace('.json', '').replace('-', '_')
    tl_fn = timelines.get(ep_key)
    if tl_fn and hasattr(sim, tl_fn):
        mutations = getattr(sim, tl_fn)()
        sim_result = sim.run_timeline(mutations)
        t4 = time.perf_counter()
        print(f'  Temporal Sim: {len(mutations)} mutations in {(t4-t3)*1000:.1f}ms')
        print(f'      Drift detected: {sim_result.get("drift_detected", False)}')
        if sim_result.get('drift_details'):
            for d in sim_result['drift_details']:
                print(f'        {d}')
        print()

    total = (t4 - t0) * 1000 if 't4' in dir() else (t3 - t0) * 1000
    print(f'  Total: {total:.1f}ms')
    print(f'{"="*72}\n')


def main():
    if len(sys.argv) < 2 or sys.argv[1] == '--all':
        episodes = sorted(f for f in os.listdir(REPLAY)
                         if f.startswith('episode_') and f.endswith('.json'))
        for ep in episodes:
            run_episode(os.path.join(REPLAY, ep))
    else:
        run_episode(sys.argv[1])


if __name__ == '__main__':
    main()
