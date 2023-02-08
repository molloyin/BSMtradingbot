from formula import call_option, put_option
from webscrubber import stock, s, strike, contract_period, sigma, r
import csv

print("stock: ", stock, " current price: ", s,
      " risk-free rate: ", r, " volatility: ", sigma, " strike", strike)

print("For:", stock, " with strike price: ", strike,
      " and contract period: ", "{:.2f}".format(contract_period*12), " months")
call = call_option(s, strike, r, contract_period, sigma)
put = put_option(s, strike, r, contract_period, sigma)

print("Call option price: ", call)
print("Put option price: ", put)


with open("options_prices.csv", "a", newline="") as file:
      writer = csv.writer(file)
      writer.writerow([stock, strike, "{:.2f}".format(contract_period*12), "{:.2f}".format(call), "{:.2f}".format(put)])      