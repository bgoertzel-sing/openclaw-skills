#!/usr/bin/env bash
set -euo pipefail
cd projects/omegaclaw/repos/OpenClaw
corepack pnpm exec vitest run --config test/vitest/vitest.extension-telegram.config.ts extensions/telegram/src/inbound-identity.test.ts 
