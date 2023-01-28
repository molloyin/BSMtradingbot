from datetime import datetime
from math import sqrt
# wtf, module not found... interpretor correct, latest package installed, no error till runtime
import pandas as pd
import pandas_datareader.data as web

stock = "RKLB"
strike = 4
contract_period = 60/365

t = datetime.now(pytz.timezone('US/New_York'))

print(t)

# assumption: r = 3 month US treasury bill rate; in reality it should match contract period
