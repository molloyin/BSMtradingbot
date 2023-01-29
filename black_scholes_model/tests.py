import formula
import webscrubber as ws
import numpy as np

try:
    assert type(ws.s) == np.float64
    print("Current stock price: passed")
except AssertionError:
    print("Current stock price: failed")
