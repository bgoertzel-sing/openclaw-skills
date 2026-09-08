# RelaLeap EO/ePC C1 execution authority — EU-SE-1

- Approved by: Ben Goertzel, Telegram, 2026-08-06 23:04 PDT
- Scope: execute the frozen C1 five-seed official EO/ePC reference
  reproduction. Prefer the Secure Cloud A40; use an alternative GPU only if
  the A40 is unavailable and it can execute the unchanged frozen C1 protocol.
- Provider/account: RunPod, existing operator credential store.
- Selected resource (observed available immediately before this record): one
  Secure Cloud NVIDIA A40, 48 GB, EU-SE-1, USD 0.44/GPU-hour.
- Image: `runpod/pytorch@sha256:61a4aafb0094cd773f11eefa378929d5a687bd775febeb78eac62fc824141fb5`.
- Storage/network: 50 GB disposable container disk; SSH only; no endpoint,
  network volume, or persistent volume.
- Expected duration/cost: 12 GPU-hours / USD 5.28 compute; science stops at
  12 hours. Provider-side termination is set at 24 hours; Ben authorizes up
  to USD 15.00, while the frozen lifecycle retains its stricter USD 12.00 cap.
- Data: public official EMNIST/MNIST reference data; no private inputs.
- Return/cleanup: retrieve declared artifacts, verify hashes locally, then
  terminate (not merely stop) on success, frozen failure, readiness failure,
  or a cost/time stop. Confirm no remaining pod, volume, endpoint, or snapshot.

This is authority for C1 only. It does not authorize C2/C3, hyperparameter
search, a changed scientific configuration, or any other project work.
