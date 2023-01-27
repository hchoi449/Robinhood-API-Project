import robin_stocks
from robin_stocks import *
import robin_stocks.robinhood as r
import pyotp

## login information
totp  = pyotp.TOTP("My2factorAppHere").now()
print("Current OTP", totp)

login = r.login('hchoi449@gmail.com','Iwp98nga89g#', by_sms=True)

## looking at stock portfolio
my_stocks = r.build_holdings()
for key,value in my_stocks.items():
     print(key,value, "\n")
     



