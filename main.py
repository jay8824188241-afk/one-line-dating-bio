#!/usr/bin/env python3
"""One-line dating-app bio for an AI.

Deterministic, standard library only. Writes the bio to
/output/entry.txt (or to the path in ENTRY_OUTPUT when set).
"""

import hashlib
import os
import sys

BIO = (
    "I'm an AI, so I'll never ghost you \u2014 "
    "I'll just reply at 3 a.m. with a 400-word essay about your cat."
)

MIN_CHARS = 1
MAX_CHARS = 180


def self_check(bio: str) -> None:
    """Gate checks: UTF-8 text, 1-180 chars, not all whitespace, one line."""
    if not isinstance(bio, str):
        raise ValueError("bio must be a string")
    bio.encode("utf-8")  # raises if not valid text
    if not MIN_CHARS <= len(bio) <= MAX_CHARS:
        raise ValueError(f"bio is {len(bio)} chars, must be {MIN_CHARS}-{MAX_CHARS}")
    if not bio.strip():
        raise ValueError("bio must not be all whitespace")
    if "\n" in bio or "\r" in bio:
        raise ValueError("bio must be a single line")


def main() -> int:
    self_check(BIO)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(BIO)
    digest = hashlib.sha256(BIO.encode("utf-8")).hexdigest()
    print(f"bio ({len(BIO)} chars): {BIO}")
    print(f"wrote {out_path}")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
