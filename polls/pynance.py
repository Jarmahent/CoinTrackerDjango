from binance.client import Client
import time
import math
import os
key = ""
secret = ""




class Pynance():
    def __init__(self, client_key, client_secret):
        self._client = Client(client_key, client_secret)

    def get_usd_coin(self, coin, option):
        info = self._client.get_all_tickers()
        ucoin = float(info[coin].get(option))
        btc = float(info[12].get(option))
        usd = ucoin * btc
        rounded = round(usd, 4)
        return(str(rounded))  #return a dictiornary 1 for value and one for name
