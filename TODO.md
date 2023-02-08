TODO:   Add comparison to official option premiums, use cron instead of bot.py
                Note: moving on from project... learning diminishing-returns

PLAN:
Familiarizing yourself with the Black Scholes model: Before you can build a bot that implements the model, you'll need to understand how the model works and what inputs it requires.

Write a program in a programming language such as Python or Java that implements the Black-Scholes formula. This can be done by using the math library in the programming language to calculate the various components of the formula, such as the d1 and d2 variables.

Obtain real-time financial data for the stock or other underlying asset, as well as for the option in question. This data can be obtained from financial data providers such as Yahoo Finance or Google Finance.

Use the real-time financial data to input into the Black-Scholes formula, which will then calculate the theoretical value of the option in real time.

Create a bot that can automatically retrieve and input the real-time financial data into the Black-Scholes formula and then output the calculated theoretical value.

Use an API to make the bot available to other systems to consume the results.

Note that, this model assumptions like constant volatility, no dividends, no transaction costs, no taxes, etc. So, the output might not reflect the real-world scenario. Also, this model
can be drastically improved by training an ML model using previous market data.


BSM
Call model:     C = SN(d1) - Ke^(-rt)N(d2)
Put model:      P = Ke^(-rt)N(-d2) - SN(-d1)

Variables:
Where:
C = the theoretical value of the call option
P = the theoretical value of the put option
S = the current price of the underlying stock
K = the strike price of the option
r = the risk-free interest rate
t = the time to expiration of the option (in years)
N(x) = the cumulative probability density function of the standard normal distribution
d1 and d2 are defined as:
d1 = (ln(S/K) + (r + σ^2/2)t) / σ√t
d2 = d1 - σ√t

Where:
ln = the natural logarithm
σ = the volatility of the underlying stock

Variables Expanded:
C&P:    Estimate of what the contract(option) is ACTUALLY worth... may differ from actual price... difference is 'implied volatility'
S:      Should be easy to pull the stock price into script... prioritse DB that contains multiple variables... In python, you can use any financial library or package such as        pandas_datareader, yfinance, etc to fetch the current stock price and other data
K:      Strike price; price the buyer is able to sell/buy the asset at until the expiration date... inherent to the contract
r:      Libraries such as Quantlib, FRED, and Pyfolio, provide risk-free interest rate data for different countries and currencies.
t:      Measured in years (decimal) the time to expiration from now, can be pulled from the above libraries for given contracts... is inherent to the contract like K
N(x):   CDF; the probability that a random variable from the normal distribution will be <= the input... found int scipy.norm.cdf
σ:      Multiply standard deviation of stock returns over past year by sqrt(252) (number of days market is open per year)