"""Write one joke about AI coding agents to $MAKEFUN_OUTPUT_DIR/entry.txt.

Plain Python 3.13, stdlib only. Deterministic: the same bytes every run.
"""

import os
from pathlib import Path

JOKE = "My coding agent said my idea was brilliant, built it perfectly, and now I own a flawless disaster."


def main() -> None:
    # Gate guard: the joke must be 1-280 chars and not only whitespace.
    # Fail loudly instead of writing an entry the scorer would reject.
    if not 1 <= len(JOKE) <= 280 or not JOKE.strip():
        raise ValueError("joke outside the 1-280 char gate")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
