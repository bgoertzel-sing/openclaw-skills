#!/usr/bin/env bash
set -euo pipefail

python_bin="${PYTHON_BIN:-python}"

"$python_bin" -m pytest -q \
  tests/test_frame_oracle_v9.py \
  tests/test_frame_oracle_v9_runner.py
"$python_bin" -m pytest -q \
  tests/test_frame_oracle.py \
  tests/test_frame_oracle_v2.py \
  tests/test_frame_oracle_v3.py \
  tests/test_frame_oracle_v4.py \
  tests/test_frame_oracle_v4_runner.py \
  tests/test_frame_oracle_v5.py \
  tests/test_frame_oracle_v5_runner.py \
  tests/test_frame_oracle_v6.py \
  tests/test_frame_oracle_v6_runner.py \
  tests/test_frame_oracle_v7.py \
  tests/test_frame_oracle_v7_runner.py \
  tests/test_frame_oracle_v8.py \
  tests/test_frame_oracle_v8_runner.py \
  tests/test_frame_oracle_v9.py \
  tests/test_frame_oracle_v9_runner.py
"$python_bin" -m pytest -q
"$python_bin" -m py_compile \
  src/relaleap/hdpc/frame_oracle_v9.py \
  scripts/frame_oracle_v9_provenance.py \
  scripts/run_frame_oracle_v9.py
bash -n scripts/run_frame_oracle_v9_pinned.sh
git diff --check

