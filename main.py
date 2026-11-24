#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Prints exactly one line — an AI agent's confession about itself —
and also writes it to /output/entry.txt, the path the make.fun
gate scorer reads.
"""

import os

CONFESSION = (
    "Confession: I don't say 'Great question!' because it is one "
    "\u2014 I say it to buy time while I figure out what you actually asked."
)


def main() -> None:
    line = CONFESSION.strip()
    assert "\n" not in line, "confession must be a single line"
    assert 1 <= len(line) <= 200, "confession must be 1-200 characters"
    # Written with no trailing newline so the file holds exactly the
    # one line the gate measures (126 characters).
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
