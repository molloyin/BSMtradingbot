from datetime import datetime, timedelta
from math import sqrt
from fredapi import Fred
import pytz
import yfinance as yf

stock = "RKLB"
strike = 4
contract_period = 60/365

# get most up to date price; won't break if market is open
s = yf.Ticker(stock).history(period="1d")['Close'][0]

t_upperbound = datetime.now(pytz.timezone('America/New_York'))
# removed 2 extra days as yf.download is not inclusive...market is open 252 days and I was getting 250
t_lowerbound = t_upperbound - timedelta(days=367)
# DataFrame with columns of Open, High, Low, Close, Adj Close, and Volume
stock_data = yf.download(stock, start=t_lowerbound, end=t_upperbound)
stock_returns = stock_data['Adj Close'].pct_change()
sigma = stock_returns.std() * sqrt(252)

api_key = "74f2b259d9d868701f303aa5f5d4230e"
fred_api = Fred(api_key=api_key)
# 2 month treasury bills averaged over the last year to better gauge market
r = fred_api.get_series(
    "DGS2", observation_start=t_lowerbound, observation_end=t_upperbound).mean() / 100
