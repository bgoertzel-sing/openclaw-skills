#!/usr/bin/env python3
"""Tests for replay_corpus/validate_corpus.py run_corpus function."""
import unittest, sys, os, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "evaluator"))
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "atomspace"))

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from validate_corpus import run_corpus


class TestRunCorpus(unittest.TestCase):
    def test_run_corpus_all_pass(self):
        corpus_dir = str(pathlib.Path(__file__).resolve().parent.parent / "replay_corpus")
        results, status = run_corpus(corpus_dir)
        self.assertEqual(status, "OK")
        self.assertEqual(len(results), 6)
        for name, expected, actual, matched in results:
            self.assertTrue(matched, f"{name}: expected {expected}, got {actual}")

    def test_run_corpus_empty_dir(self):
        results, status = run_corpus("/tmp/nonexistent_corpus_dir")
        self.assertEqual(status, "No episode files found")
        self.assertEqual(results, [])


if __name__ == "__main__":
    unittest.main()
