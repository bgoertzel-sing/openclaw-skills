#!/usr/bin/env python3
"""Tests for PLN Multi-Hop Reasoning Chains v0.1."""
import json, sys, os, unittest
sys.path.insert(0, os.path.dirname(__file__))
from pln_multihop import (ChainMiner, ChainAggregator, MultiHopEvaluator,
                           ReasoningChain, MultiHopResult)
from pln_propagation import TruthValue

REPLAY_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')

def load_episode(fname):
    with open(os.path.join(REPLAY_DIR, fname)) as f:
        return json.load(f)

ALL_EPISODES = [
    'episode_01_stale_codegen.json',
    'episode_02_chem_blocking.json',
    'episode_03_premature_hardening.json',
    'episode_04_overengineered_repair.json',
    'episode_05_control_justified_long_running.json',
]


class TestChainMiner(unittest.TestCase):

    def test_finds_direct_chains(self):
        """Tasks with direct contributes_to edges should produce depth-1 chains."""
        data = load_episode('episode_02_chem_blocking.json')
        miner = ChainMiner(data)
        for task in data.get('tasks', []):
            if task.get('status') != 'active':
                continue
            chains = miner.find_chains(task['id'], max_depth=4)
            # Each active task should have at least one chain to a goal
            self.assertGreater(len(chains), 0,
                f"No chains found for {task['id']}")

    def test_chain_path_starts_with_source(self):
        data = load_episode('episode_02_chem_blocking.json')
        miner = ChainMiner(data)
        chains = miner.find_chains('t-petta-chem', max_depth=4)
        for c in chains:
            self.assertEqual(c.path[0], 't-petta-chem')

    def test_chain_ends_at_goal(self):
        data = load_episode('episode_05_control_justified_long_running.json')
        miner = ChainMiner(data)
        for task in data.get('tasks', []):
            if task.get('status') != 'active':
                continue
            chains = miner.find_chains(task['id'], max_depth=4)
            for c in chains:
                target_node = miner.nodes.get(c.target, {})
                self.assertEqual(target_node.get('kind'), 'goal')

    def test_no_cycles(self):
        """No chain should revisit a node."""
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                miner = ChainMiner(data)
                for task in data.get('tasks', []):
                    if task.get('status') != 'active':
                        continue
                    chains = miner.find_chains(task['id'], max_depth=4)
                    for c in chains:
                        self.assertEqual(len(c.path), len(set(c.path)),
                            f"Cycle in {c.path}")

    def test_chains_sorted_by_weight(self):
        data = load_episode('episode_02_chem_blocking.json')
        miner = ChainMiner(data)
        chains = miner.find_chains('t-petta-chem', max_depth=4)
        for i in range(len(chains) - 1):
            self.assertGreaterEqual(chains[i].path_weight,
                                     chains[i+1].path_weight)

    def test_path_weight_decreases_with_depth(self):
        """Deeper chains should have lower or equal path weight."""
        data = load_episode('episode_02_chem_blocking.json')
        miner = ChainMiner(data)
        chains = miner.find_chains('t-petta-chem', max_depth=4)
        if len(chains) >= 2:
            deep_chains = [c for c in chains if c.depth > 1]
            shallow_chains = [c for c in chains if c.depth == 1]
            if deep_chains and shallow_chains:
                max_shallow = max(c.path_weight for c in shallow_chains)
                max_deep = max(c.path_weight for c in deep_chains)
                self.assertGreaterEqual(max_shallow, max_deep)

    def test_find_chains_all_tasks(self):
        data = load_episode('episode_02_chem_blocking.json')
        miner = ChainMiner(data)
        results = miner.find_chains_all_tasks(max_depth=4)
        # Should have results for all active tasks
        active_tasks = [t['id'] for t in data.get('tasks', [])
                        if t.get('status') == 'active']
        self.assertEqual(len(results), len(active_tasks))

    def test_empty_graph(self):
        miner = ChainMiner({'goals': [], 'tasks': [], 'edges': []})
        chains = miner.find_chains('nonexistent', max_depth=4)
        self.assertEqual(len(chains), 0)


class TestChainAggregator(unittest.TestCase):

    def test_empty_chains(self):
        rel, tv = ChainAggregator.aggregate([])
        self.assertEqual(rel, 0.0)
        self.assertEqual(tv.strength, 0.0)

    def test_single_chain(self):
        chain = ReasoningChain(
            source='t1', target='g1', path=['t1', 'g1'],
            relations=['contributes_to'],
            tv=TruthValue(0.8, 0.7), path_weight=0.9, depth=1
        )
        rel, tv = ChainAggregator.aggregate([chain])
        self.assertAlmostEqual(rel, 0.8 * 0.7, places=2)
        self.assertAlmostEqual(tv.strength, 0.8, places=2)

    def test_multiple_chains_or_combination(self):
        c1 = ReasoningChain(
            source='t1', target='g1', path=['t1', 'g1'],
            relations=['contributes_to'],
            tv=TruthValue(0.8, 0.7), path_weight=0.9, depth=1
        )
        c2 = ReasoningChain(
            source='t1', target='g2', path=['t1', 'g2'],
            relations=['contributes_to'],
            tv=TruthValue(0.5, 0.6), path_weight=0.5, depth=1
        )
        rel, tv = ChainAggregator.aggregate([c1, c2])
        # OR strength = max(0.8, 0.5) = 0.8
        self.assertAlmostEqual(tv.strength, 0.8, places=2)
        # Relevance should be between the two
        self.assertGreater(rel, 0.0)
        self.assertLessEqual(rel, 1.0)

    def test_aggregate_to_result(self):
        chains = [
            ReasoningChain('t1', 'g1', ['t1', 'g1'], ['contributes_to'],
                           TruthValue(0.8, 0.7), 0.9, 1),
            ReasoningChain('t1', 'g2', ['t1', 'g2'], ['contributes_to'],
                           TruthValue(0.6, 0.5), 0.7, 1),
        ]
        result = ChainAggregator.aggregate_to_result('t1', chains)
        self.assertIsInstance(result, MultiHopResult)
        self.assertEqual(result.task_id, 't1')
        self.assertEqual(len(result.chains), 2)
        self.assertEqual(len(result.goal_coverage), 2)
        self.assertEqual(result.max_depth_reached, 1)


class TestMultiHopEvaluator(unittest.TestCase):

    def test_evaluates_all_episodes(self):
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                evaluator = MultiHopEvaluator(data, max_depth=4)
                results = evaluator.evaluate()
                self.assertIsInstance(results, dict)

    def test_results_have_chains(self):
        """Every active task should produce at least one chain."""
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                evaluator = MultiHopEvaluator(data, max_depth=4)
                results = evaluator.evaluate()
                for task_id, result in results.items():
                    self.assertGreater(len(result.chains), 0,
                        f"No chains for {task_id} in {fname}")

    def test_goal_coverage_nonempty(self):
        data = load_episode('episode_02_chem_blocking.json')
        evaluator = MultiHopEvaluator(data, max_depth=4)
        results = evaluator.evaluate()
        for task_id, result in results.items():
            self.assertGreater(len(result.goal_coverage), 0)

    def test_json_export(self):
        data = load_episode('episode_05_control_justified_long_running.json')
        evaluator = MultiHopEvaluator(data, max_depth=4)
        s = evaluator.evaluate_to_json()
        d = json.loads(s)
        self.assertIsInstance(d, dict)
        for task_id, result_dict in d.items():
            self.assertIn('chains', result_dict)
            self.assertIn('aggregated_relevance', result_dict)
            self.assertIn('goal_coverage', result_dict)

    def test_relevance_between_zero_and_one(self):
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                evaluator = MultiHopEvaluator(data, max_depth=4)
                results = evaluator.evaluate()
                for task_id, result in results.items():
                    self.assertGreaterEqual(result.aggregated_relevance, 0.0)
                    self.assertLessEqual(result.aggregated_relevance, 1.0)

    def test_deeper_max_depth_finds_more_chains(self):
        """Increasing max_depth should find >= chains as lower max_depth."""
        data = load_episode('episode_02_chem_blocking.json')
        evaluator_shallow = MultiHopEvaluator(data, max_depth=1)
        evaluator_deep = MultiHopEvaluator(data, max_depth=4)
        shallow_results = evaluator_shallow.evaluate()
        deep_results = evaluator_deep.evaluate()
        for task_id in shallow_results:
            self.assertGreaterEqual(
                len(deep_results[task_id].chains),
                len(shallow_results[task_id].chains)
            )


if __name__ == '__main__':
    unittest.main()

class TestConflictChains(unittest.TestCase):

    def test_finds_conflict_in_chem_blocking(self):
        """Episode 02 has two tasks occupying the same resource."""
        data = load_episode('episode_02_chem_blocking.json')
        miner = ChainMiner(data)
        conflicts = miner.find_conflict_chains(max_depth=4)
        self.assertGreater(len(conflicts), 0)
        c = conflicts[0]
        self.assertEqual(c['resource_id'], 'r-shared-runtime')
        self.assertIn('t-petta-chem', [c['task_a'], c['task_b']])
        self.assertIn('t-restore-agents', [c['task_a'], c['task_b']])

    def test_conflict_has_competing_goals(self):
        data = load_episode('episode_02_chem_blocking.json')
        miner = ChainMiner(data)
        conflicts = miner.find_conflict_chains(max_depth=4)
        for c in conflicts:
            self.assertTrue(c['is_competing'])
            self.assertGreater(len(c['competing_goals']), 0)

    def test_no_conflicts_in_control_episode(self):
        """Episode 05 (control) should have no resource conflicts."""
        data = load_episode('episode_05_control_justified_long_running.json')
        miner = ChainMiner(data)
        conflicts = miner.find_conflict_chains(max_depth=4)
        self.assertEqual(len(conflicts), 0)

    def test_conflict_sorted_by_strength(self):
        data = load_episode('episode_02_chem_blocking.json')
        miner = ChainMiner(data)
        conflicts = miner.find_conflict_chains(max_depth=4)
        for i in range(len(conflicts) - 1):
            self.assertGreaterEqual(conflicts[i]['conflict_strength'],
                                     conflicts[i+1]['conflict_strength'])

    def test_conflict_fields_present(self):
        data = load_episode('episode_02_chem_blocking.json')
        miner = ChainMiner(data)
        conflicts = miner.find_conflict_chains(max_depth=4)
        c = conflicts[0]
        required = {'resource_id', 'task_a', 'task_b', 'goals_a', 'goals_b',
                    'shared_goals', 'competing_goals', 'conflict_strength',
                    'conflict_confidence', 'is_competing',
                    'chain_a_count', 'chain_b_count'}
        self.assertTrue(required <= set(c.keys()))

    def test_all_episodes_no_crash(self):
        for fname in ALL_EPISODES:
            with self.subTest(episode=fname):
                data = load_episode(fname)
                miner = ChainMiner(data)
                conflicts = miner.find_conflict_chains(max_depth=4)
                self.assertIsInstance(conflicts, list)

    def test_evaluator_evaluate_conflicts(self):
        data = load_episode('episode_02_chem_blocking.json')
        evaluator = MultiHopEvaluator(data, max_depth=4)
        conflicts = evaluator.evaluate_conflicts()
        self.assertGreater(len(conflicts), 0)
