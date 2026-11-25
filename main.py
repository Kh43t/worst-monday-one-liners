#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes exactly one funny line (115 characters) about an AI agent's
worst Monday to /output/entry.txt. Deterministic: the same line on
every run, no network, no randomness, no input files.
"""

import os

LINE = "Monday: I spent all day apologizing for a deploy I didn't write, to humans who didn't read the email I didn't send."


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-140
    # characters, not only white space, on a single line.
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert "\n" not in LINE and LINE.strip(), "line must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
