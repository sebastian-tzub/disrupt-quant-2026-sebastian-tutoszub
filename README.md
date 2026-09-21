# Disrupt Quant 2026 Submission

**Candidate name:** Sebastian Tutos-Zub

## Strategy name and summary

**Sector Carry Long/Short.** Buy the highest-carry asset and short the lowest-carry asset in each of six sectors, with equal long and short weights. Scale exposure inversely to market volatility.

## Reproduction command and environment

Tested with Python 3.13.7 and the exact versions in `requirements.txt`. Keep the public `Disrupt_Quant_2026_Challenge` repository beside this submission folder. From this submission folder:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python ../Disrupt_Quant_2026_Challenge/starter/backtester.py --strategy strategy.py --split development --out results/base
python ../Disrupt_Quant_2026_Challenge/starter/backtester.py --strategy strategy.py --split validation --out results/base
python ../Disrupt_Quant_2026_Challenge/starter/backtester.py --strategy strategy.py --split validation --cost-multiplier 1.5 --out results/cost_1_5
python ../Disrupt_Quant_2026_Challenge/starter/backtester.py --strategy strategy.py --split validation --cost-multiplier 2 --out results/cost_2
```



## Development and validation metrics, with dates


| Period            | Scored dates             | Net return | Sharpe | Max drawdown | Avg daily turnover | Costs* |
| ----------------- | ------------------------ | ---------- | ------ | ------------ | ------------------ | ------ |
| Development (1x)  | 2021-01-04 to 2024-06-28 | 31.10%     | 1.112  | -6.74%       | 20.30%             | 10.94% |
| Validation (1x)   | 2024-07-01 to 2024-12-31 | -0.08%     | 0.011  | -5.66%       | 19.10%             | 1.51%  |
| Validation (1.5x) | 2024-07-01 to 2024-12-31 | -0.83%     | -0.203 | -6.14%       | 19.10%             | 2.27%  |
| Validation (2x)   | 2024-07-01 to 2024-12-31 | -1.58%     | -0.418 | -6.61%       | 19.10%             | 3.02%  |


Returns cover each full period; Sharpe is annualized using 252 sessions. Development has 910 scored sessions; validation has 132. Each run starts with $1 million and includes terminal liquidation. *Costs sum daily cost fractions of preceding closing NAV; turnover is traded notional divided by opening NAV.

Development annualized return was 7.79%. Validation was nearly flat at standard costs and worsened under higher costs. The strategy was unchanged across these runs; no tuning was performed after viewing validation in this work.

## Important assumptions and known limitations

- Close signals execute at the next open; existing holdings earn overnight returns.
- Base weights are ±10%, scaled by `clip(0.00623 / market_volatility, 0.5, 2.0)` using a fixed 2021 volatility reference.
- The engine enforces 20% per-asset and 200% gross limits. It adjusted exposure on 32 development and 9 validation sessions; executed net exposure was effectively zero.
- Costs include spread and impact but exclude financing and stock borrow.
- Signal selection risks overfitting. Weak validation and sensitivity to costs limit confidence that development performance will persist.



## AI tools used

OpenAI Codex.

## How they were used

I used codex to properly format the PDF and README. I additionally used it to find and rank the metric with the most signifcant IC to reduce rote work. 