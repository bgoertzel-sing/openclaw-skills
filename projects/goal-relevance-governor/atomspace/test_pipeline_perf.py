#!/usr/bin/env python3
"""Performance benchmarks for the Integrated Governor Pipeline."""
import sys, os, json, time, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from atomspace.integrated_governor import IntegratedGovernorPipeline
from atomspace.remediation_engine import RemediationEngine
from atomspace.reasoning_explainer import ReasoningExplainer
from atomspace.temporal_simulator import TemporalSimulator


class TestPipelinePerformance(unittest.TestCase):
    """Benchmark the full pipeline on each episode."""

    def setUp(self):
        self.d = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.episodes = [
            'episode_01_stale_codegen.json',
            'episode_02_chem_blocking.json',
            'episode_03_premature_hardening.json',
            'episode_04_overengineered_repair.json',
            'episode_05_control_justified_long_running.json',
        ]

    def test_pipeline_under_100ms(self):
        """Each episode should process in under 100ms."""
        for ep in self.episodes:
            with open(os.path.join(self.d, 'replay_corpus', ep)) as f:
                data = json.load(f)
            pipeline = IntegratedGovernorPipeline(data)
            start = time.perf_counter()
            pipeline.run(ecan_cycles=10)
            elapsed = (time.perf_counter() - start) * 1000
            self.assertLess(elapsed, 100,
                           f'{ep}: pipeline took {elapsed:.1f}ms (limit 100ms)')

    def test_remediation_under_10ms(self):
        """Remediation plan generation should be under 10ms per episode."""
        for ep in self.episodes:
            with open(os.path.join(self.d, 'replay_corpus', ep)) as f:
                data = json.load(f)
            pipeline = IntegratedGovernorPipeline(data)
            result = pipeline.run(ecan_cycles=10).to_dict()
            engine = RemediationEngine(data)
            start = time.perf_counter()
            engine.generate_all(result['recommendations'])
            elapsed = (time.perf_counter() - start) * 1000
            self.assertLess(elapsed, 10,
                           f'{ep}: remediation took {elapsed:.1f}ms (limit 10ms)')

    def test_explainer_under_10ms(self):
        """Reasoning explanation should be under 10ms per episode."""
        for ep in self.episodes:
            with open(os.path.join(self.d, 'replay_corpus', ep)) as f:
                data = json.load(f)
            pipeline = IntegratedGovernorPipeline(data)
            result = pipeline.run(ecan_cycles=10).to_dict()
            explainer = ReasoningExplainer(data)
            start = time.perf_counter()
            explainer.explain_all(result)
            elapsed = (time.perf_counter() - start) * 1000
            self.assertLess(elapsed, 10,
                           f'{ep}: explainer took {elapsed:.1f}ms (limit 10ms)')

    def test_temporal_simulator_under_50ms(self):
        """Temporal simulation should complete in under 50ms per timeline."""
        for ep, timeline_fn in [
            ('episode_01_stale_codegen.json', 'create_timeline_stale_task'),
            ('episode_02_chem_blocking.json', 'create_timeline_conflict_resolution'),
            ('episode_03_premature_hardening.json', 'create_timeline_premature_to_justified'),
        ]:
            with open(os.path.join(self.d, 'replay_corpus', ep)) as f:
                data = json.load(f)
            sim = TemporalSimulator(data)
            mutations = getattr(sim, timeline_fn)()
            start = time.perf_counter()
            sim.run_timeline(mutations)
            elapsed = (time.perf_counter() - start) * 1000
            self.assertLess(elapsed, 50,
                           f'{ep}: temporal sim took {elapsed:.1f}ms (limit 50ms)')

    def test_full_pipeline_throughput(self):
        """Full pipeline (5 episodes) should complete in under 200ms total."""
        start = time.perf_counter()
        for ep in self.episodes:
            with open(os.path.join(self.d, 'replay_corpus', ep)) as f:
                data = json.load(f)
            pipeline = IntegratedGovernorPipeline(data)
            result = pipeline.run(ecan_cycles=10).to_dict()
            engine = RemediationEngine(data)
            engine.generate_all(result['recommendations'])
            explainer = ReasoningExplainer(data)
            explainer.explain_all(result)
        elapsed = (time.perf_counter() - start) * 1000
        self.assertLess(elapsed, 200,
                       f'Full pipeline took {elapsed:.1f}ms (limit 200ms)')


if __name__ == '__main__':
    unittest.main()
