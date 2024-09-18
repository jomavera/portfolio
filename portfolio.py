import yfinance as yf
from datetime import datetime, timedelta


class Stock:
    def __init__(self, symbol, shares):
        self.symbol = symbol
        self.shares = shares

    def Price(self, date):
        price = yf.download(
            self.symbol, start=date, end=date + timedelta(days=4), progress=False
        )

        return self.shares * price["Adj Close"].iloc[0]


class Portfolio:
    def __init__(self, stocks):
        self.stocks = stocks
        self.days_in_year = 365

    def Profit(self, start_date, end_date):
        profit = 0
        for stock in self.stocks:
            profit += stock.shares * (stock.Price(end_date) - stock.Price(start_date))
        return profit

    def Cost(self, date):
        cost = 0
        for stock in self.stocks:
            cost += stock.shares * stock.Price(date)
        return cost

    def AnnualizedReturn(self, start_date, end_date):
        return (self.Cost(end_date) / self.Cost(start_date)) ** (
            1 / ((end_date - start_date).days / self.days_in_year)
        ) - 1


## Example

stocks = [Stock("AAPL", 10), Stock("MSFT", 20)]
portfolio = Portfolio(stocks)
print(
    f"Portfolio profit: {portfolio.Profit(datetime(2020, 1, 1), datetime(2022, 12, 31)):.4f}"
)
print(
    f"Portfolio annualized return: {portfolio.AnnualizedReturn(datetime(2020, 1, 1), datetime(2022, 12, 31)):.2%}"
)
