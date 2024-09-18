# Portfolio

This project provides a simple way to analyze the performance of a stock portfolio using historical data from Yahoo Finance.

## Installation

To install the required dependencies, run:

```sh
pip install yfinance
```

## Usage
Here is an example of how to use the Portfolio and Stock classes:

```python
from datetime import datetime
from portfolio import Stock, Portfolio

# Define the stocks in the portfolio
stocks = [Stock("AAPL", 10), Stock("MSFT", 20)]

# Create a portfolio
portfolio = Portfolio(stocks)

# Calculate the profit of the portfolio
profit = portfolio.Profit(datetime(2020, 1, 1), datetime(2022, 12, 31))
print(f"Portfolio profit: {profit:.4f}")

# Calculate the annualized return of the portfolio
annualized_return = portfolio.AnnualizedReturn(datetime(2020, 1, 1), datetime(2022, 12, 31))
print(f"Portfolio annualized return: {annualized_return:.2%}")
```

## Classes
`Stock`

Represents a stock in the portfolio.

- `__init__(self, symbol, shares)`: Initializes a stock with a symbol and the number of shares.
- `Price(self, date)`: Returns the price of the stock on a given date.

`Portfolio`

Represents a portfolio of stocks.

- `__init__(self, stocks)`: Initializes a portfolio with a list of stocks.
- `Profit(self, start_date, end_date)`: Calculates the profit of the portfolio between two dates.
- `Cost(self, date)`: Calculates the cost of the portfolio on a given date.
- `AnnualizedReturn(self, start_date, end_date)`: Calculates the annualized return of the portfolio between two dates.

