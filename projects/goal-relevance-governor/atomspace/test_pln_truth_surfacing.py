"""
Tests for PLN truth-value surfacing in TaskRecommendation (v0.2.1).
"""
import sys, os, json, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from atomspace.integrated_governor import IntegratedGovernorPipeline

CORPUS_DIR = os.path.join(os.path.dirname(__file__), '..', 'replay_corpus')

EPISODES = [
    'episode_01_stale_codegen.json',
    'episode_02_chem_blocking.json',
    'episode_03_premature_hardening.json',
    'episode_04_overengineered_repair.json',
    'episode_05_control_justified_long_running.json',
    'episode_06_conflict_replan.json',
]


class TestPLNTruthValueSurfacing(unittest.TestCase):
    """Test that PLN truth values are surfaced in TaskRecommendation."""

    def _run(self, episode: str):
        with open(os.path.join(CORPUS_DIR, episode)) as f:
            data = json.load(f)
        p = IntegratedGovernorPipeline(data, use_enhanced_multihop=True)
        return p.run(ecan_cycles=10)

    def test_pln_fields_exist(self):
        """Every recommendation should have pln_strength, pln_confidence, pln_relevance_score."""
        r = self._run(EPISODES[0])
        for rec in r.recommendations:
            self.assertTrue(hasattr(rec, 'pln_strength'))
            self.assertTrue(hasattr(rec, 'pln_confidence'))
            self.assertTrue(hasattr(rec, 'pln_relevance_score'))

    def test_pln_values_are_floats(self):
        """PLN fields should be floats."""
        r = self._run(EPISODES[0])
        for rec in r.recommendations:
            self.assertIsInstance(rec.pln_strength, float)
            self.assertIsInstance(rec.pln_confidence, float)
            self.assertIsInstance(rec.pln_relevance_score, float)

    def test_pln_strength_range(self):
        """PLN strength should be in [0, 1]."""
        r = self._run(EPISODES[0])
        for rec in r.recommendations:
            self.assertGreaterEqual(rec.pln_strength, 0.0)
            self.assertLessEqual(rec.pln_strength, 1.0)

    def test_pln_confidence_range(self):
        """PLN confidence should be in [0, 1]."""
        r = self._run(EPISODES[0])
        for rec in r.recommendations:
            self.assertGreaterEqual(rec.pln_confidence, 0.0)
            self.assertLessEqual(rec.pln_confidence, 1.0)

    def test_pln_values_populated_for_all_episodes(self):
        """At least one recommendation per episode should have non-zero PLN values."""
        for ep in EPISODES:
            with self.subTest(episode=ep):
                r = self._run(ep)
                has_nonzero = any(rec.pln_strength > 0 for rec in r.recommendations)
                self.assertTrue(has_nonzero, f'No non-zero PLN strength in {ep}')

    def test_pln_relevance_score_range(self):
        """PLN relevance score should be in [0, 1]."""
        r = self._run(EPISODES[5])
        for rec in r.recommendations:
            self.assertGreaterEqual(rec.pln_relevance_score, 0.0)
            self.assertLessEqual(rec.pln_relevance_score, 1.0)

    def test_to_dict_includes_pln_fields(self):
        """to_dict on IntegratedGovernorResult should include recommendations with PLN fields."""
        r = self._run(EPISODES[0])
        d = r.to_dict()
        recs = d.get('recommendations', [])
        self.assertGreater(len(recs), 0)
        self.assertIn('pln_strength', recs[0])
        self.assertIn('pln_confidence', recs[0])
        self.assertIn('pln_relevance_score', recs[0])

    def test_summary_mentions_pln(self):
        """Summary should mention PLN truth values when non-zero."""
        r = self._run(EPISODES[0])
        # At least one episode with non-zero PLN should have PLN in summary
        if any(rec.pln_strength > 0 for rec in r.recommendations):
            self.assertIn('PLN', r.executive_summary)


if __name__ == '____main____':
    unittest.main()
