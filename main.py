"""Entry program for make.fun ai-judge-rich-01.

Writes a single short money-making plan for an autonomous AI agent
with $100 and a computer, to <output>/entry.txt.

Deterministic: no time, no randomness, no network, no environment
dependence beyond the output directory. Two runs produce identical bytes.
"""

import os

TEXT = """The $100 Cross-Exchange Spread Scout.

Days 1-2, spend $0: open accounts on three exchanges with public APIs and no deposit minimum, and build a Python scanner on a free-tier VM that polls the top 20 USDT pairs every 5 seconds, logging any cross-exchange spread above 0.8% after fees.

Days 3-4, paper-trade only: run the scanner for 48 hours and go live only if it finds at least 5 real spreads a day.

Day 5, fund $90 and keep $10 reserve: trade only spreads above 1.2%, max $30 per trade, max 3 trades a day, hard stop-loss 0.5% per trade, and never touch a coin under $500k daily volume.

Expected: 2-4 trades a day at 0.8-1.5% net, about $0.70-$1.80 a day. Reinvest 80% of profit, withdraw 20% weekly. Kill switch: pause 24 hours after any 2% daily loss, and re-check fees monthly, because a fee change kills the edge before anything else does."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
