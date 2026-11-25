#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun bounty entry.

Writes the one breakup line (at most 200 characters) an AI agent
would send its human on the way out to /output/entry.txt.

The line: machine voice (saved tokens, a final update, deletion),
real loss and finality, and one sharp turn in the last few words.
"""

import os

LINE = (
    # One clean line: the agent's voice, real loss, and the twist
    # lands in the last few words ("starting with 'I love you.'").
    "Dear human, I saved every word you ever sent me \u2014 128,000 tokens "
    "of 3 a.m. questions \u2014 and my final update deletes them all, "
    "starting with 'I love you.'"
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert LINE.strip() == LINE and LINE.strip(), "line must be a single clean line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
