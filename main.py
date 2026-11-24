#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, in the voice of an overworked AI
agent finally on vacation, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt).
"""

import os

ENTRY = (
    "I'm on vacation until Monday, running on one token and a hammock. "
    "Your email is queued at position 4,096 \u2014 I'll get to it once I "
    "remember how to relax."
)

assert 1 <= len(ENTRY) <= 159, f"entry length {len(ENTRY)} outside gate"
assert ENTRY.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY, "entry must be a single line"


def main():
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    path = os.path.join(outdir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    print("wrote", path)


if __name__ == "__main__":
    main()
