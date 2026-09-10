# BridgeLearn 0.3 sandbox experiments

This bundle contains four reproducible synthetic experiments for BridgeLearn
0.3.0:

1. dynamic sharpness-plant identification and counterfactual edge prediction;
2. equal-width white versus antithetic order-2 probing;
3. companion stability, non-normal transient growth, and Lyapunov metrics;
4. momentum-limited covariance reachability.

## Run

```bash
python -m pip install --no-deps vendor/bridgelearn-0.3.0-py3-none-any.whl
python run_all.py --output artifacts
```

The run produces `REPORT.md`, `summary.json`, CSV traces, and PNG plots. Fixed
random seeds are used throughout.

## Scope

These are mechanism tests on scalar and two-dimensional synthetic plants. They
do not establish performance improvements on neural networks, CAROM,
predictive coding, or reinforcement learning.
