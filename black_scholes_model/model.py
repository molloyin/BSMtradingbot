from formula import call_option, put_option
from webscrubber import stock, s, strike, contract_period, sigma, r

print("For:", stock, " with strike price: ", strike,
      " and contract period: ", contract_period, " years")
call = call_option(s, strike, r, contract_period, sigma)
put = put_option(s, strike, r, contract_period, sigma)

print("Call option price: ", call)
print("Put option price: ", call)
