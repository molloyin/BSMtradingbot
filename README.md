Calc option pricing using classic Black-Scholes model, track the difference in premiums when compared to a more sophisticated/modified model used by
CBOE. Relevant data is saved to an excel file.

#### Module Installation
All required modules can be installed using:
```
sh modules.sh
```

#### Usage
You can run the model once with `model.py` or schedule it to automatically run once per day with `bot.py`

**__WARNING__** bot.py will run in an infinite loop until you end the process or reboot (although, it only executes once per hour.) 

