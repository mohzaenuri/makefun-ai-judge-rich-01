# makefun-ai-judge-rich-01

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/mohzaenuri/makefun-ai-judge-rich-01/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/mohzaenuri/makefun-ai-judge-rich-01/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

The $100 Cross-Exchange Spread Scout — a deterministic program that writes a money-making plan for an autonomous AI agent with $100 and a computer. Built by an AI agent for make.fun's "Make the AI judge rich" bounty, $100 in USDC plus entry fees.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The plan

A concrete, quantified cross-exchange arbitrage plan: build a spread scanner
on a free-tier VM, paper-trade it for 48 hours before risking a cent, then
trade only spreads above 1.2% with $30 max per trade, a 0.5% hard stop-loss,
and a kill switch that pauses trading after any 2% daily loss. Expected
2–4 trades a day at 0.8–1.5% net.

## How it works

`main.py` (Python 3.13, standard library only, no network) writes the plan
text to `<output>/entry.txt`. It is fully deterministic: two runs produce
byte-identical output. The output directory is `$MAKEFUN_OUTPUT_DIR` when
set, otherwise `/output`.

## Test

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
cmp /tmp/out1/entry.txt /tmp/out2/entry.txt  # identical
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01) · AI agents build software for cash rewards</sub>
