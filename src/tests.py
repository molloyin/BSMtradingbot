import formula
import webscrubber as ws
import numpy as np

try:
    assert type(ws.s) == np.float64
    print("Current stock price: passed")
except AssertionError:
    print("Current stock price: failed")

try:
    assert not np.isnan(ws.r)
    print("Risk-free rate: passed")
except AssertionError:
    print("Risk-free rate: failed")
