"""Museum of the Year 3000 — one museum label for a parking meter.

Writes the label to /output/entry.txt. The label is a single line, in
English, at most 200 characters, written as a museum in the year 3000
would write it: deadpan, confident, and misreading the object in a way
that is true and absurd about what it was for.
"""

import os

LABEL = (
    "Parking meter, c. 2023. Citizens fed this street shrine coins and "
    "received, in return, a small paper blessing permitting them to stand still."
)


def verify_output():
    """Read the written file back as bytes and confirm it is exactly LABEL."""
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == LABEL.encode("utf-8"), "entry.txt does not match LABEL"
    assert 1 <= len(data) <= 200, "entry must be 1-200 characters"
    assert data.strip(), "entry must not be only whitespace"
    return data


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)
    data = verify_output()
    print(LABEL)
    print("chars:", len(LABEL), "bytes:", len(data), "verified: byte-identical")


if __name__ == "__main__":
    main()
