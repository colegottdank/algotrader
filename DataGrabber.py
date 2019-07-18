import alpaca_trade_api as tradeapi
from api import *
import csv

api = tradeapi.REST(get_api_key(), get_secret_key())
account = api.get_account()
storageLocation = "././Data/"
fromDate = '2008-1-1'
toDate = ''
# barTimeframe = "15Min"  # 1Min, 5Min, 15Min, 1H, 1D
assets = ["GWPH", 'AAPL']


def get_data():
    for symbol in assets:
        data_file = open(storageLocation + '{0}.csv'.format(symbol), 'w')
        data_file.write("day,open,high,low,close,volume\n")

        returned_data = api.polygon.historic_agg("day", symbol, _from=fromDate)

        # Reads, formats and stores the new bars
        for day in returned_data:
            ret_day = str(day.day).split(" ", 1)[0]
            ret_open = str(day.open)
            ret_high = str(day.high)
            ret_low = str(day.low)
            ret_close = str(day.close)
            ret_volume = str(day.volume)

            # Writes formatted line to CSV file
            data_file.write(ret_day + "," + ret_open + "," + ret_high + "," + ret_low + "," + ret_close + "," + ret_volume + "\n")

        data_file.close()


def clean_data():
    for symbol in assets:
        for row in 



if __name__ == '__main__':
    get_data()