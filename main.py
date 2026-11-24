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

def main() -> None:
    text = BIO.strip()
    assert 1 <= len(text) <= 180, f"bio length {len(text)} out of range"
    assert "\n" not in text, "bio must be exactly one line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
