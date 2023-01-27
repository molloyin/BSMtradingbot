import math


def call_option(current, strike, risk_free_interest, expire_t, cdf1, cdf2):
    return current * cdf1 - strike * math.e(-risk_free_interest * expire_t) * cdf2


def put_option(current, strike, risk_free_interest, expire_t, cdf1, cdf2):
    return strike * math.e(-risk_free_interest * expire_t) * cdf2 - current * cdf1
