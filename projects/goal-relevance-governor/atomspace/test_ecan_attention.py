#!/usr/bin/env python3
"""Tests for ECAN Attention Allocation v0.1."""
import json, sys, os
import unittest

sys.path.insert(0, os.path.dirname(__file__))
from ecan_attention import (
    ECANAttentionAllocator, AttentionValue, ECANResult,
    STI_INITIAL_SCALE, LTI_INITIAL_SCALE, STI_FLOOR,
    STI_DECAY, LTI_DECAY, SPREAD_FACTOR, RENT,
)

REPLAY_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')


def load_episode(fname):
    path = os.path.join(REPLAY_DIR, fname)
    with open(path) as f:
        return json.load(f)


ALL_EPISODES = [
    'episode_01_stale_codegen.json',
    'episode_02_chem_blocking.json',
    'episode_03_premature_hardening.json',
    'episode_04_overengineered_repair.json',
    'episode_05_control_justified_long_running.json',
]


class TestECANAttention(unittest.TestCase):
    """Test ECAN Attention Allocation on all replay episodes."""

    def test_allocator_initializes_attention_for_all_nodes(self):
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                alloc = ECANAttentionAllocator(data)
                node_count = sum(len(data.get(k, [])) for k in
                    ('goals', 'projects', 'tasks', 'resources', 'results', 'constraints'))
                self.assertEqual(len(alloc.attention), node_count,
                    f'{fname}: attention map size mismatch')

    def test_sti_initialized_from_pln_relevance(self):
        """Tasks should get STI from PLN relevance_score."""
        data = load_episode('episode_05_control_justified_long_running.json')
        alloc = ECANAttentionAllocator(data)
        av = alloc.attention['t-run-benchmark']
        self.assertAlmostEqual(av.sti, 92.5, delta=1.0,
            msg='STI should be relevance * STI_INITIAL_SCALE')

    def test_lti_initialized_from_pln_confidence(self):
        """LTI should come from truth_value.confidence."""
        data = load_episode('episode_02_chem_blocking.json')
        alloc = ECANAttentionAllocator(data)
        for nid, av in alloc.attention.items():
            tv = alloc.propagator.tvs[nid]
            expected_lti = tv.confidence * LTI_INITIAL_SCALE
            self.assertAlmostEqual(av.lti, expected_lti, places=4,
                msg=f'{nid}: LTI mismatch')

    def test_vlti_for_terminal_goals(self):
        """Achieved/terminal/abandoned nodes get VLTI=True."""
        data = load_episode('episode_01_stale_codegen.json')
        alloc = ECANAttentionAllocator(data)
        for nid, av in alloc.attention.items():
            node = alloc.nodes[nid]
            if node.get('status') in ('achieved', 'terminal', 'abandoned'):
                self.assertTrue(av.vlti, f'{nid}: should have VLTI')

    def test_run_returns_result(self):
        data = load_episode('episode_02_chem_blocking.json')
        alloc = ECANAttentionAllocator(data)
        result = alloc.run(cycles=5)
        self.assertIsInstance(result, ECANResult)
        self.assertEqual(result.cycle, 5)

    def test_sti_changes_over_cycles(self):
        """STI should change over time due to decay + rent + spread."""
        data = load_episode('episode_05_control_justified_long_running.json')
        alloc = ECANAttentionAllocator(data)
        initial_sti = alloc.attention['t-run-benchmark'].sti
        alloc.run(cycles=5)
        final_sti = alloc.attention['t-run-benchmark'].sti
        self.assertNotAlmostEqual(initial_sti, final_sti, places=2,
            msg='STI should change over cycles')

    def test_priority_queue_sorted_by_sti(self):
        data = load_episode('episode_02_chem_blocking.json')
        alloc = ECANAttentionAllocator(data)
        result = alloc.run(cycles=3)
        pq = result.priority_queue
        for i in range(len(pq) - 1):
            sti1 = alloc.attention[pq[i]].sti
            sti2 = alloc.attention[pq[i+1]].sti
            self.assertGreaterEqual(sti1, sti2,
                'Priority queue should be sorted by STI descending')

    def test_eviction_candidates_below_floor(self):
        """Nodes with STI < STI_FLOOR should be eviction candidates."""
        data = load_episode('episode_01_stale_codegen.json')
        alloc = ECANAttentionAllocator(data)
        result = alloc.run(cycles=10)
        for nid in result.eviction_candidates:
            av = alloc.attention[nid]
            self.assertLess(av.sti, STI_FLOOR,
                f'{nid}: eviction candidate should have STI < floor')
            self.assertFalse(av.vlti,
                f'{nid}: VLTI nodes should not be eviction candidates')

    def test_high_relevance_task_ranks_higher(self):
        """In ep02, t-restore-agents (rel=0.939) should rank above t-petta-chem (rel=0.246)."""
        data = load_episode('episode_02_chem_blocking.json')
        alloc = ECANAttentionAllocator(data)
        result = alloc.run(cycles=5)
        pq = result.priority_queue
        idx_restore = pq.index('t-restore-agents')
        idx_chem = pq.index('t-petta-chem')
        self.assertLess(idx_restore, idx_chem,
            'High-relevance task should rank above low-relevance task')

    def test_json_export_serializable(self):
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                alloc = ECANAttentionAllocator(data)
                s = alloc.run_to_json(cycles=3)
                d = json.loads(s)
                self.assertEqual(d['cycle'], 3)
                self.assertGreater(len(d['priority_queue']), 0)

    def test_rent_charged_each_cycle(self):
        """Total rent should be RENT * non_vlti_count * cycles."""
        data = load_episode('episode_02_chem_blocking.json')
        alloc = ECANAttentionAllocator(data)
        non_vlti = sum(1 for av in alloc.attention.values() if not av.vlti)
        result = alloc.run(cycles=5)
        self.assertAlmostEqual(result.rent_paid, RENT * non_vlti * 5,
            msg='Rent should be RENT * non_vlti_count * cycles')

    def test_cycles_alive_increments(self):
        data = load_episode('episode_05_control_justified_long_running.json')
        alloc = ECANAttentionAllocator(data)
        alloc.run(cycles=7)
        for av in alloc.attention.values():
            self.assertEqual(av.cycles_alive, 7,
                f'{av.node_id}: cycles_alive should be 7')

    def test_empty_graph_does_not_crash(self):
        """ECAN should handle empty/minimal graphs gracefully."""
        data = {'goals': [], 'tasks': [], 'edges': [], 'resources': []}
        alloc = ECANAttentionAllocator(data)
        result = alloc.run(cycles=3)
        self.assertEqual(len(result.priority_queue), 0)
        self.assertEqual(len(result.eviction_candidates), 0)


if __name__ == '__main__':
    unittest.main()
