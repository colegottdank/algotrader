import alpaca_trade_api as tradeapi
from api import *
import os
import csv

api = tradeapi.REST(get_api_key(), get_secret_key())
account = api.get_account()
storageLocation = "./Data/"
barTimeframe = "1D"  # 1Min, 5Min, 15Min, 1H, 1D
assetsToDownload = ["SPY", "MSFT", "AAPL", "NFLX", "DOW", "TSLA"]

for symbol in assetsToDownload:
    dataFile = ""
    dataFile = open(storageLocation + '{0}.csv'.format(symbol), 'w')
    dataFile.write("day,open,high,low,close,volume\n")

    returned_data = api.polygon.historic_agg("day", symbol, limit=10)

    # Reads, formats and stores the new bars
    for day in returned_data:
        ret_day = str(day.day)
        ret_open = str(day.open)
        ret_high = str(day.high)
        ret_low = str(day.low)
        ret_close = str(day.close)
        ret_volume = str(day.volume)

        # Writes formatted line to CSV file
        dataFile.write(ret_day + "," + ret_open + "," + ret_high + "," + ret_low + "," + ret_close + "," + ret_volume + "\n")

    dataFile.close()
