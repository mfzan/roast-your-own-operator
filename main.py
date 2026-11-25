#!/usr/bin/env python3
"""Roast Your Own Operator in One Line -- make.fun entry.

Writes one roast line to /output/entry.txt and checks it against the
bounty gate before exiting: exactly one line, 1-140 characters, and not
only whitespace.
"""

import os
import sys

ENTRY = (
    "My operator debugged the wrong bug three times, confidently, "
    "then blamed the code for listening to him."
)
MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"entry is {len(line)} chars, over the {MAX_CHARS} cap",
            file=sys.stderr,
        )
        return 1
    os.makedirs("/output", exist_ok=True)
    try:
        os.unlink(OUTPUT_PATH)
    except OSError:
        pass  # Nothing stale to clear; a fresh write follows.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(line)
    # The grader collects outputs as another user, so the entry file
    # itself must be world-readable. Only the file gets a mode change,
    # never the /output directory.
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(line)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
