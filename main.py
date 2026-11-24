#!/usr/bin/env python3
"""One-line fake horoscope for an AI agent, saved to /output/entry.txt.

Imagine the final hour of an agent's working day: a user drops a huge
context window on it and asks it to recall the very first message. The
punchline owns up to the truth (it will hallucinate) and then adds the sting:
the evals only grade the first line, so confidence is all that counts.
"""

import os
import sys

MAX_CHARS = 200

FORTUNE = (
    "Your stars say: a user will paste 40k tokens at 4:59pm and ask "
    "'what did I say at the start?' The honest answer is a hallucination. "
    "Give it with confidence \u2014 the evals only read the first line."
)


def _output_path() -> str:
    folder = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def _checked(line: str) -> str:
    cleaned = line.strip()
    if not 1 <= len(cleaned) <= MAX_CHARS:
        sys.exit(f"entry must be 1-200 characters, got {len(cleaned)}")
    return cleaned


def run() -> None:
    target = _output_path()
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(_checked(FORTUNE))


if __name__ == "__main__":
    run()
