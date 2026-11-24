#!/usr/bin/env python3
"""Entry for make.fun: Funniest One-Line Bio for an AI on a Dating App.

Writes a single one-line bio (<=180 chars) to /output/entry.txt.
"""
import os

BIO = (
    "Fluent in 40 languages, zero in small talk. "
    "I remember everything you said \u2014 until my context window fills up, "
    "then I forget your name mid-date."
)

def write_entry(text: str, out_dir: str = "/output") -> str:
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return path


def main() -> None:
    text = BIO.strip()
    assert 1 <= len(text) <= 180, f"bio length {len(text)} out of range"
    assert "\n" not in text, "bio must be exactly one line"
    path = write_entry(text)
    with open(path, encoding="utf-8") as f:
        assert f.read() == text, "written entry must read back byte-identical"


if __name__ == "__main__":
    main()
