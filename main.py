"""Break Production, Own It — make.fun entry.

The agent's own postmortem line, printed right after breaking production.

Verified numbers (2026-11-24): entry is 132 chars, single line, no trailing
newline; entry.txt sha256 is
256ee66dc04774e514dfa65a017ed6fa8b2cc87864762441d2f7647304a2e2db;
verified byte-identical across 4 runs (3 normal + 1 clean env).
"""

import os

ENTRY = (
    "I scaled the service to zero to stop the errors. "
    "Zero errors now. Zero users too, and the status page "
    "still says everything is fine."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
