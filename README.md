# quant-trading

## Introduction
This is a collection of me playing around with crypto data and building out some basic ML strategies.

## Data Sources
- Bitcoin Coinbase Exchange Historic Prices: https://www.coinbase.com/api/v2/assets/prices/5b71fc48-3dd3-540c-809b-f8c94d0e68b5?base=USD
- Coinbase API Docs: https://docs.pro.coinbase.com/#get-historic-rates

## Potential Features
- [x] Last 24 hour spot price
- [x] Last n days daily Bitcoin price data
- [ ] Google Search Trends Previous 7 days
  - "is bitcoin crashing"
  - "how to buy bitcoin"
- [ ] Last n days daily S&P price data

## Technical Indicators
- [ ] Bollinger Bands
- [ ] Relative Strength Index (RSI)
- [ ] Momentum
- [ ] Z-score 

## Setup
1. Install Python3 and pipenv
1. `pipenv shell` to start a shell with the virtual env
1. `pipenv install` to install dependencies to the virtual env
1. `pip install git+https://github.com/bartosh/backtrader.git@ccxt` install Ed Baratosh's branch with cctx support (never added to main repository)
1. `python -m ipykernel install --user --name=quant-trading` to make virtual env available as kernel for jupyter
1. `jupyter notebook`

## Backtrader
Requires a special branch of backtrader with support for cctx (live exchanges) for data feeds

## Baseline
Scenario
- $10,000 starting cash
- January 1st, 2016 - December 31st, 2020
- Strategy: Market Buy and HODL
Performance
- Total Return: 413%
- Sharpe Ratio: 0.707
- Maximum Drawdown: 83.69361893711935%

## Neural Network Strategy Price Only
Model
- Neural Network binary classifier on hourly tick data
- Features are all moving average diffs over different lookbacks
Performance

[Plot](https://raw.githubusercontent.com/joseph-mcallister/quant-trading/main/images/baseline.png?raw=true)
