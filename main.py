"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
Python standard library only; no third-party packages.
"""

import os

JOKE = (
    "My password is so secure even I can't log in \u2014 "
    "which is great for security and terrible for the meeting "
    "I was supposed to join ten minutes ago."
)

assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} characters"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts every character in the file.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
