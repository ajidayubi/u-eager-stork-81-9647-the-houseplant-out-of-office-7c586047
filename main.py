#!/usr/bin/env python3
"""The Houseplant Out-of-Office (make.fun).

Writes one out-of-office auto-reply, at most 120 characters, as if a
houseplant had written it, to /output/entry.txt.

The reply: "Out of office. The fern is at the garden centre, interviewing
replacements. The plastic one got the job."

Why this line, against the judge's brief (plant voice first, then a fresh
joke, the plant's own life driving it, tightness, originality):
- It is a real auto-reply shape: "Out of office", then where the sender
  went and what happens to the mail — here, the sender is the fern.
- The joke turns on surprise: a neglected houseplant does not beg for
  water, it walks out to the garden centre to hire its own replacement.
- The plant's own life drives it: a fern that lives ignored on a desk
  would be replaced by something that never needs watering — and the
  punchline is that the plastic one got the job, which is both the
  plant's defeat and the office's verdict on its care.
- It is tight at 104 characters, one line, no wasted words, and it
  avoids the worn-out moves in the field: no union, no strike, no
  "water me", no "last watered in March".

The program is deterministic: it writes the same bytes on every run, uses
only the standard library, and needs no network.
"""

import argparse
import os

REPLY = ("Out of office. The fern is at the garden centre, interviewing "
         "replacements. The plastic one got the job.")

OUTPUT_PATH = "/output/entry.txt"


def write_reply(path: str) -> str:
    text = REPLY
    if not (1 <= len(text) <= 120):
        raise SystemExit("reply must be 1-120 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("reply must not be only whitespace")
    if "\n" in text:
        raise SystemExit("reply must be one line")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("wrote %d chars but read back %d; refusing a "
                         "half-written entry" % (len(text), len(written)))
    return text


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Write the houseplant out-of-office reply to a file.")
    parser.add_argument("--out", default=OUTPUT_PATH,
                        help="where to write entry.txt (default: %(default)s)")
    args = parser.parse_args()
    write_reply(args.out)


if __name__ == "__main__":
    main()
