# shepherd
<b> a simple quant trading bot with CLI interface </b>

<br>

![](https://user-images.githubusercontent.com/71098497/134826072-b99b649f-72e3-457f-b4b9-b4a107247616.png)


<br>

## Features

 - clean CLI shell interface
 - utilizes alpaca API and yahoo finance API
 - concise commands for executing various orders and strategies
    - buy-side market orders
    - sell-side limit orders
    - trailing stop orders (supports both trail price and trail percentage)
    - bracket orders (stop-loss + take-profit or only stop-loss)
    - long-only price momentum strategy based on cumulative returns of stocks in S&P 500 coded from scratch
    
 - miscellaneous helpful commands 
    - portfolio gain/loss
    - market open/close indicator
    - portfolio buying power indicator
    - closed orders display
    - rudimentary client ID system
    - asset check to see if it's tradeable on alpaca
 
 <br>
 
 ## To-Do

- implement mean return and risk-adjusted return based long-only price momentum strategies
- earnings-momentum strategy implementation
- low-volatility anomaly strategy implementation
- add a mean-reversion pairs trading strategy implementation
- calendar spread strategy implementation
- some form of sentiment analysis
