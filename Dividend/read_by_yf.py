import yfinance as yf
import math
#  import datetime


def adj_close_by_list(ticker_list, start_date, end_date):
    res = dict()
    data = yf.download(
        " ".join(ticker_list), start_date, end_date)
    for ticker in ticker_list:
        try:
            price = float(data['Adj Close'][ticker][-1])
            if math.isnan(price):
                price = float(data['Close'][ticker][-1])
                if math.isnan(price):
                    price = 1e6
        except BaseException:
            price = 1e6
        res[ticker] = price
    return res


def read_current_price(ticker="SPY"):
    msft = yf.Ticker(ticker)

# get stock info
    return msft.info['regularMarketPrice']


if __name__ == "__main__":
    print(read_current_price())
    pass


# get historical market data
#  hist = msft.history(period="max")

# show actions (dividends, splits)
#  msft.actions

# show dividends
#  print(msft.dividends)

# show splits
#  msft.splits

# show financials
#  msft.financials
#  msft.quarterly_financials

# show major holders
#  msft.major_holders

# show institutional holders
#  msft.institutional_holders

# show balance sheet
#  msft.balance_sheet
#  msft.quarterly_balance_sheet

# show cashflow
#  msft.cashflow
#  msft.quarterly_cashflow

# show earnings
#  msft.earnings
#  msft.quarterly_earnings

# show sustainability
#  msft.sustainability

# show analysts recommendations
#  msft.recommendations

# show next event (earnings, etc)
#  print(msft.calendar)

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
#  msft.isin

# show options expirations
#  msft.options

#  show news
#  msft.news

# get option chain for specific expiration
#  opt = msft.option_chain('YYYY-MM-DD')
# data available via: opt.calls, opt.puts
