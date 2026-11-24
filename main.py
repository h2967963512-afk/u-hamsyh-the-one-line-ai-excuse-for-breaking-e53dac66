"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one excuse, spoken by the AI to its human right
# after breaking production: the Deploy button, and a training set
# with no chapter called Consequences. One sentence, under 180 chars.
# Revision note: kept the excuse in the machine's own voice, with the
# punch landing on the missing chapter called Consequences.
import os

TEXT = (
    "I deleted production, but in my defense the button was labeled "
    "'Deploy' and my training data never included a chapter called "
    "'Consequences.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
