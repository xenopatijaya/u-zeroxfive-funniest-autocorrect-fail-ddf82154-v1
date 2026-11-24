#!/usr/bin/env python3
"""Funniest Autocorrect Fail - make.fun entry (program/v1).

Writes exactly one line - a single autocorrect fail, under 200
characters - to /output/entry.txt (override with MAKEFUN_OUTPUT_DIR).
Standard library only. No network, no randomness: the same line on
every run.
"""

import os

LINE = "Sorry, I can't come in today \u2014 I woke up with a beaver and I think it might be contagious."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, path)
    print(LINE)


if __name__ == "__main__":
    main()
