import { appendFileSync, chmodSync, mkdirSync, openSync, closeSync } from "node:fs";
import { dirname } from "node:path";

export function appendLedgerRecord(path, record) {
  mkdirSync(dirname(path), { recursive: true, mode: 0o700 });
  const fd = openSync(path, "a", 0o600);
  closeSync(fd);
  chmodSync(path, 0o600);
  appendFileSync(path, `${JSON.stringify(record)}\n`, { encoding: "utf8", mode: 0o600 });
}
