#!/usr/bin/env python3
"""Write the dog's excuse to /output/entry.txt.

Stdlib only. The output directory comes from MAKEFUN_OUTPUT_DIR
when set, otherwise /output.
"""

import os

# The excuse, in the dog's own voice.
EXCUSE = (
    "It said 'rough draft' right on top, so I roughed it up. "
    "I was only following instructions."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
