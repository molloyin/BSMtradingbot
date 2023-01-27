from math import sqrt, e, log
from scipy.stats import norm


def call_option(current, strike, risk_free_interest, t, sigma):
    d1 = _d1(current, strike, risk_free_interest, t, sigma) 
    d2 = _d2(d1, sigma, t)
    return current * norm.cdf(d1) - strike * e(-risk_free_interest * t) * norm.cdf(d2)


def put_option(current, strike, risk_free_interest, t, sigma):
    d1 = _d1(current, strike, risk_free_interest, t, sigma) 
    d2 = _d2(d1, sigma, t)
    return strike * e(-risk_free_interest * t) * norm.cdf(d2) - current * norm.cdf(d1)

def _d1(S, K, r, t, sigma):
    return (log(S / K) + (r + sigma ** 2 / 2) * t) / (sigma * sqrt(t))

def _d2(d1, sigma, t):
    return d1 - sigma * sqrt(t)
