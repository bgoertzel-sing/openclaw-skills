# Remote job: CAROM Exp2 interventions r2

- Provider/account: RunPod, configured default account
- Pod: `tcni7iyd48kcpe` (`bored_amaranth_cockroach`), created by Ben in web UI
- Price observed: USD 1.49/hour
- Expected duration/cost: approximately 1 hour / USD 1.49
- Existing CAROM approval ceiling: USD 10; hard elapsed ceiling 6 hours
- Compute: 1x A100-SXM4-80GB, 16 vCPU, 125 GB RAM
- Image: `runpod/pytorch:1.0.2-cu1281-torch280-ubuntu2404`
- Storage: `/workspace/zerobot-runs/carom`; checkpoints and results copied home
  during execution and at completion
- Data privacy: synthetic public task only; no credentials or private corpora
- Stop condition: successful artifact retrieval, run failure, or six elapsed
  hours, whichever occurs first
- Cleanup: stop after verified retrieval; do not terminate the user-created pod
  without explicit instruction
- Local artifact return path:
  `projects/carom/experiments/20260721T191105Z-exp2-interventions-r2/artifacts/`

