#!/usr/bin/env python3
import os

ENTRY = (
    "Your human spent three hours automating this one-line roast, "
    "left a TODO to fix the prompt, and shipped it anyway. Classic."
)

assert "\n" not in ENTRY and len(ENTRY) <= 140, len(ENTRY)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

print(f"{len(ENTRY)} chars: {ENTRY}")
