#!/usr/bin/env python3
"""One-Star Review of Something Essential.

A one-star review of sleep: it promised eight hours of rest and
delivered a sore neck and an alarm, with no refunds. The review is
the whole entry; it goes to /output/entry.txt and to stdout.
"""

import os

ENTRY = "One star. Sleep promised eight hours of rest and delivered a sore neck and an alarm. No refunds."


def main():
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry must be 1-200 non-blank chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
