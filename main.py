"""Break Production, Own It — make.fun entry.

The agent's own postmortem line, printed right after breaking production.
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
