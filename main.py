#!/usr/bin/env python3
"""The Weirdest Job Title entry.

Writes a single original job title to /output/entry.txt
(1-60 characters, UTF-8, a few words and nothing else).
Standard library only, no network, no input.

The title is built from three fragments: a seniority that makes it
sound like a real posting (Senior), the gloriously odd object
(Iceberg), and the everyday job it is bolted onto (Tow Truck
Driver). Tow-truck drivers tow cars; this one tows icebergs — a
real activity (ships tow icebergs away from oil rigs) pushed one
step past ordinary work. ``assemble`` joins the fragments into the
single title; ``validate`` checks the entry gate before anything
is written.
"""

from pathlib import Path

SENIORITY = "Senior"
SUBJECT = "Iceberg"
JOB = "Tow Truck Driver"

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(seniority: str, subject: str, job: str) -> str:
    """Join the seniority, subject and job fragments into one title."""
    return f"{seniority} {subject} {job}"


def validate(title: str) -> str:
    """Check the title meets the entry gate before it is written.

    Must be 1-60 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(title) <= 60:
        raise ValueError(f"title must be 1-60 characters, got {len(title)}")
    if "\n" in title or "\r" in title:
        raise ValueError("title must be a single line (no newline characters)")
    if not title.strip():
        raise ValueError("title must not be only whitespace")
    title.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return title


def main() -> None:
    title = validate(assemble(SENIORITY, SUBJECT, JOB))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(title, encoding="utf-8")


if __name__ == "__main__":
    main()
