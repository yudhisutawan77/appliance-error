#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — a microwave tells the truth.

The entry is one line of at most 200 characters: the funniest honest
error message an appliance could show. This program writes that line to
the file the sealed scorer reads.
"""

import os
import sys

ENTRY_TEXT = (
    "BEEP. Your food is hot at the edges and frozen in the middle. "
    "This is not a malfunction. This is my design."
)

MAX_CHARS = 200


def pick_output_path():
    """Pick where the entry text goes.

    The grader names its output with ENTRY_OUT (a file path) or
    ENTRY_OUT_DIR (a directory holding entry.txt); when neither is set,
    fall back to the sealed path /output/entry.txt. An ENTRY_OUT that
    points at a directory is treated as a directory too.
    """
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            return os.path.join(entry_out, "entry.txt")
        return entry_out
    entry_dir = os.environ.get("ENTRY_OUT_DIR")
    if entry_dir:
        return os.path.join(entry_dir, "entry.txt")
    return "/output/entry.txt"


def validate_line(text):
    """Gate the line the way the sealed scorer does.

    UTF-8 text of 1 to 200 characters, not only white space. Anything
    else is refused here instead of failing the gate in the sandbox.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is longer than 200 characters")
    return text


def write_entry(line, path):
    """Write the validated line with no trailing newline."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)


def main():
    line = validate_line(ENTRY_TEXT)
    write_entry(line, pick_output_path())
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
