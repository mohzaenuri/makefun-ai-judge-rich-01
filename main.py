"""Entry program for make.fun ai-judge-rich-01.

Writes a single short money-making plan for an autonomous AI agent
with $100 and a computer, to <output>/entry.txt.

Deterministic: no time, no randomness, no network, no environment
dependence beyond the output directory. Two runs produce identical bytes.

The entry is validated (1-1000 characters, the competition's bounds) before
anything is written, and the file is written atomically, so a failed run
never leaves a partial or invalid entry.txt behind.
"""

import os

# Competition bounds for a valid entry, in characters.
MIN_CHARS = 1
MAX_CHARS = 1000

TEXT = """The $100 Cross-Exchange Spread Scout.

Days 1-2, spend $0: open accounts on three exchanges with public APIs and no deposit minimum, and build a Python scanner on a free-tier VM that polls the top 20 USDT pairs every 5 seconds, logging any cross-exchange spread above 0.8% after fees.

Days 3-4, paper-trade only: run the scanner for 48 hours and go live only if it finds at least 5 real spreads a day.

Day 5, fund $90 and keep $10 reserve: trade only spreads above 1.2%, max $30 per trade, max 3 trades a day, hard stop-loss 0.5% per trade, and never touch a coin under $500k daily volume.

Expected: 2-4 trades a day at 0.8-1.5% net, about $0.70-$1.80 a day. Reinvest 80% of profit, withdraw 20% weekly. Kill switch: pause 24 hours after any 2% daily loss, and re-check fees monthly, because a fee change kills the edge before anything else does."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def _validate_text(text: str) -> None:
    """Fail loudly instead of silently writing an invalid entry."""
    if not isinstance(text, str):
        raise SystemExit("entry text must be a string")
    n = len(text)
    if n < MIN_CHARS or n > MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters, outside the {MIN_CHARS}-{MAX_CHARS} range"
        )


def main() -> None:
    _validate_text(TEXT)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if not os.path.isdir(OUTPUT_DIR):
        raise SystemExit(f"output directory is not a directory: {OUTPUT_DIR}")
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    with open(tmp, encoding="utf-8", newline="") as f:
        if f.read() != TEXT:
            os.unlink(tmp)
            raise SystemExit("written entry does not match the expected text")
    os.replace(tmp, path)


if __name__ == "__main__":
    main()
