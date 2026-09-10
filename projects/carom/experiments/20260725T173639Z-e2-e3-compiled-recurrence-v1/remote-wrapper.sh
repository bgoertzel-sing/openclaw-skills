#!/usr/bin/env bash
set -euo pipefail

# CAROM E2/E3 compiled recurrence — remote GPU wrapper
# Stage 1: CUDA eager/compiled equivalence + throughput gate
# Stage 2: full 5-seed × 5-arm campaign (only if gate passes)

cd /workspace/carom

export TORCHINDUCTOR_CACHE_DIR=/workspace/torchinductor_cache
mkdir -p "$TORCHINDUCTOR_CACHE_DIR"

OUTDIR=/workspace/output
mkdir -p "$OUTDIR"

echo "=== STAGE 1: CUDA equivalence and throughput gate ==="
python3 benchmark_e2_e3_compile.py \
  --device cuda \
  --batch-size 128 \
  --d 64 \
  --K 16 \
  --controller-steps 70 \
  --timed-steps 5 \
  --output "$OUTDIR/cuda-compile-benchmark.json" \
  2>&1 | tee "$OUTDIR/stage1_benchmark.log"

echo "=== STAGE 1 complete ==="
cat "$OUTDIR/cuda-compile-benchmark.json"

# Check equivalence tolerances
python3 -c "
import json, sys
with open('$OUTDIR/cuda-compile-benchmark.json') as f:
    d = json.load(f)
max_logit = d.get('max_logit_error', float('inf'))
max_activity = d.get('max_activity_error', float('inf'))
max_grad = d.get('max_gradient_error', float('inf'))
max_param = d.get('max_param_error', float('inf'))
eager_ms = d.get('eager_step_ms', 0)
compiled_ms = d.get('compiled_step_ms', 0)
speedup = d.get('steady_state_speedup', 0)
compile_s = d.get('compile_overhead_s', 0)

ok = True
if max_logit > 1e-5: ok = False; print(f'FAIL max_logit_error={max_logit}')
if max_activity > 1e-5: ok = False; print(f'FAIL max_activity_error={max_activity}')
if max_grad > 1e-6: ok = False; print(f'FAIL max_gradient_error={max_grad}')
if max_param > 1e-5: ok = False; print(f'FAIL max_param_error={max_param}')

# Throughput projection: 25 arms × 3000 steps
# Each step needs one forward+backward through 70-step recurrence
per_step_s = compiled_ms / 1000.0
total_steps = 25 * 3000
proj_s = per_step_s * total_steps + compile_s * 25  # compile per arm
proj_h = proj_s / 3600
print(f'Per-step (compiled): {compiled_ms:.2f}ms')
print(f'Compile overhead: {compile_s:.2f}s')
print(f'Projected 25-arm campaign: {proj_h:.2f}h')

if not ok:
    print('GATE FAILED: equivalence tolerances exceeded')
    sys.exit(1)
if proj_h > 2.5:
    print(f'GATE FAILED: projection {proj_h:.2f}h exceeds 2.5h bound')
    sys.exit(1)
print('GATE PASSED')
" 2>&1 | tee -a "$OUTDIR/stage1_gate.log"

GATE_RC=${PIPESTATUS[0]}
if [ "$GATE_RC" -ne 0 ]; then
    echo "Gate failed, aborting campaign"
    exit 1
fi

echo "=== STAGE 2: Full E2/E3 campaign with compiled recurrence ==="
python3 run_carom_e2_e3.py \
  --outdir "$OUTDIR/campaign" \
  --seeds 7 17 27 37 47 \
  --steps 3000 \
  --batch-size 128 \
  --eval-size 2048 \
  --eval-batch-size 256 \
  --lr 2e-3 \
  --d 64 \
  --K 16 \
  --controller-steps 70 \
  --noise 0.02 \
  --compile-model \
  --compile-backend inductor \
  --compile-mode reduce-overhead \
  --compile-fullgraph \
  --device cuda \
  2>&1 | tee "$OUTDIR/stage2_campaign.log"

echo "=== STAGE 2 complete ==="

# Generate SHA-256 manifest
cd "$OUTDIR"
find . -type f | sort | xargs sha256sum > manifest.sha256
echo "Manifest:"
cat manifest.sha256
echo "=== ALL DONE ==="
