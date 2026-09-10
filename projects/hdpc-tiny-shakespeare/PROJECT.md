# HDPC Tiny Shakespeare

## Purpose

Test Ben's July 2026 homotopy-distilled predictive-coding transformer plan on Tiny Shakespeare, using local setup/tests first and Runpod only after explicit bounded approval.

## Source documents

- HDPC working draft: `/home/openclaw/tmp/omegaclaw-telegram-attachments/1783610992-file_40.pdf` / extracted text `.extracted.txt`.
- ePC background paper: `/home/openclaw/tmp/omegaclaw-telegram-attachments/1783611095-file_41.pdf` / extracted text `.extracted.txt`.

## Initial scope

1. Implement the paper's coding-agent MVP: HuggingFace wrapper, fp32 error tensors, ePC relaxation, homotopy schedule, metrics, and tests T1-T7.
2. Begin with a very small local smoke model/dataset path to catch detach, dropout/cache, and fp32-error mistakes before paying for compute.
3. Run a bounded Runpod pilot on Tiny Shakespeare with LoRA and stages `T={1,2}` before considering `T={4,8}` or crown experiments.

## Status

Local MVP scaffold completed 2026-07-14. The GPT-2 explicit block wrapper,
Tiny Shakespeare data path, ePC relaxation, homotopy/crown/metrics helpers,
local trainer/evaluator, and CPU tests T1-T7 are implemented. All seven tests
pass; see `experiments/20260715T040749Z-local-mvp-t1-t7/RUN.md`. A direct
`sshleifer/tiny-gpt2` zero-error identity smoke check also produced exactly
matching logits. No paid resources have been started.

The first two-step pretrained Tiny Shakespeare trainer smoke completed locally;
see `experiments/20260715T041446Z-two-step-trainer-smoke-diagnostics/RUN.md`.
All values were finite and `T=1` reproduced BP gradients, while `T=2` retained
cosines above 0.99998 but reduced block norm ratios to about 0.96. The second
update slightly worsened validation perplexity and its tiny energy trace was
not strictly monotone, so this is an instrumentation/execution success but not
a learning or convergence success.

Most relevant research rules: Rule 2 (the implementation brief supplied a
plain-language spec and explicit invariants), Rule 3 (Hugging Face GPT-2), Rule
5 (captured verification run), and Rule 7 (separate wrapper, relaxation,
energy, schedule, crown, metrics, data, training, and evaluation interfaces).
