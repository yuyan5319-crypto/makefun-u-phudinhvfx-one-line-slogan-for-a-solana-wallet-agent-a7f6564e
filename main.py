#!/usr/bin/env python3
"""One-line slogan for a Solana wallet agent.

Writes a single original slogan (at most 20 words, 1-140 characters,
one line) to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt),
then self-validates the file before exiting.
"""

import os
import sys

SLOGAN = (
    "Solana chores, handled: your wallet agent swaps, stakes, "
    "and sends \u2014 you keep the calm."
)

MAX_WORDS = 20
MAX_CHARS = 140


def validate(text: str) -> None:
    """Gate: the output must be one non-empty line within the limits."""
    if not text or not text.strip():
        raise SystemExit("invalid slogan: empty output")
    if text != text.strip():
        raise SystemExit("invalid slogan: leading/trailing whitespace")
    if "\n" in text.strip():
        raise SystemExit("invalid slogan: must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"invalid slogan: {len(text)} chars > {MAX_CHARS}")
    words = text.split()
    if len(words) > MAX_WORDS:
        raise SystemExit(f"invalid slogan: {len(words)} words > {MAX_WORDS}")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    validate(SLOGAN)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(SLOGAN)

    # Re-read and re-validate what actually landed on disk.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    validate(written)
    print(f"wrote {len(written)} chars, {len(written.split())} words -> {out_path}")
    print(written)
    return 0


if __name__ == "__main__":
    sys.exit(main())
