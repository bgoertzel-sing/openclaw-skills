#!/usr/bin/env python3
"""Frozen-protocol 12k wrapper for the repaired CAROM GPT-2 runner."""
import r9_carom_gpt2 as run

run.STEPS = 12_000
run.BS = 64
run.SEED = 0
run.CKPT_INTERVAL = 1_000
run.CKPT_DIR = "/workspace/zerobot-runs/carom-gpt2-12k/checkpoints"
run.OUT_DIR = "/workspace/zerobot-runs/carom-gpt2-12k/results"

if __name__ == "__main__":
    run.main()
