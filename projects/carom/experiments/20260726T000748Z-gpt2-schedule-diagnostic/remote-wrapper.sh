#!/usr/bin/env bash
set -euo pipefail
run_root=/workspace/carom-schedule
export HF_HOME="${run_root}/hf-cache"
export PYTHONUNBUFFERED=1
cd "${run_root}/src"
started="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
set +e
"${run_root}/.venv/bin/python" run_carom_gpt2_schedule_diagnostic.py \
  --step3000 "${run_root}/input/step_3000.pt" \
  --output-dir "${run_root}/output" \
  >"${run_root}/experiment.log" 2>"${run_root}/experiment.err"
status=$?
set -e
finished="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
(
  cd "${run_root}"
  find output -type f -print0 | sort -z | xargs -0 sha256sum
  sha256sum experiment.log experiment.err input/step_3000.pt
) >"${run_root}/sha256.txt"
printf '%s\n' "${started}" >"${run_root}/started_at.txt"
printf '%s\n' "${finished}" >"${run_root}/finished_at.txt"
printf '%s\n' "${status}" >"${run_root}/exit_status.txt"
exit "${status}"
