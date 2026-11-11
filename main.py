"""news-summary-01 entry: write the day's world news summary to /output/entry.txt.

The competition runs the program with no network and expects the same bytes on
every run, so the summary is a file the repository holds and the program copies
it, byte for byte. Standard library only.
"""

import os
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "entry.txt").write_bytes((HERE / "summary.txt").read_bytes())


if __name__ == "__main__":
    main()
