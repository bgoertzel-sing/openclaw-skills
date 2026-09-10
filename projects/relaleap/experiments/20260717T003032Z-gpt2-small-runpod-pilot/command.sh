#!/usr/bin/env bash
set -euo pipefail

runpodctl pod create \
  --name relaleap-gpt2-small-epc-pilot-20260716 \
  --cloud-type COMMUNITY \
  --gpu-id "NVIDIA A100 80GB PCIe" \
  --gpu-count 1 \
  --image pytorch/pytorch:2.4.0-cuda12.4-cudnn9-runtime \
  --container-disk-in-gb 40 \
  --volume-in-gb 80 \
  --volume-mount-path /workspace \
  --ssh \
  --terminate-after 2026-07-17T06:30:32Z
