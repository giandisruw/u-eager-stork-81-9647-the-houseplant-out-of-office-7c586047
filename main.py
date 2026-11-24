#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Stdlib only, no network, no API key.

The line was chosen by pairwise judging (Caffeine router, kit's judge
brief) over 6 drafted candidates: it won all 3 of its pairings
(margins 3, 2, 3). The em dash in the line is part of the judged text;
do not replace it with a hyphen or comma.
"""

import os

LINE = "Hi, I'm out \u2014 the cactus. I haven't been watered since March and honestly, I'm thriving on neglect and spite."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars, must be 1-120"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
