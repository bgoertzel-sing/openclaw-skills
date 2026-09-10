#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/research-agent/projects/chaos-language-algorithm/repos/chaoslang
env PYTHONPATH=src python3 -m chaoslang.benchmarks.m1_controls --system lorenz96 --steps 1024 --discard 256 --bins 4 --iterations 8 --dimension 20 --seed 0 --miner suffix_trie --category-method js 
