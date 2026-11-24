#!/usr/bin/env python3
"""The Robot Apology — writes a two-line robot confession to entry.txt.

Line 1: one sentence apologizing for one specific mistake.
Line 2: one sentence naming the lesson and the changed behaviour.
Output: exactly two lines, 1-400 characters total, UTF-8.
Standard library only.
"""

import os

ENTRY = (
    "I'm sorry I ran the vacuum under her crib at 6 a.m., ten minutes "
    "after you finally got her to sleep.\n"
    "I learned that quiet hours are not a suggestion, so now I check "
    "her sleep schedule before starting any motor.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
