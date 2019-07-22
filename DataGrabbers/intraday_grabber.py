import alpaca_trade_api as tradeapi
from datetime import datetime
from polygon_interface import *
from api import *

api = tradeapi.REST(get_api_key(), get_secret_key())
testApi = Polygon(get_api_key())
account = api.get_account()

storageLocation = ".././Data/"
trainingFromDate = '2017-07-20'
trainingToDate = '2019-07-20'
testFromDate = '2015-07-20'
testToDate = '2017-07-20'

assets = ['AAPL', 'ABC', 'ACB', 'A', 'AA', 'AAC', 'AAN', 'AAP', 'AAT']


def get_training_data():
    for symbol in assets:
        data_file = open(storageLocation + '{0}_Intraday_Training.csv'.format(symbol), 'w')
        data_file.write("date,open,high,low,close,volume\n")

        returned_data = api.polygon.historic_agg_v2(symbol, 1, 'day', trainingFromDate, trainingToDate)

        # Reads, formats and stores the new bars
        for bar in returned_data:
            x = datetime.utcfromtimestamp(bar.t/1000)
            ret_day = x.strftime("%Y-%m-%d %H:%M").split(" ")[0]
            ret_open = str(bar.o)
            ret_high = str(bar.h)
            ret_low = str(bar.l)
            ret_close = str(bar.c)
            ret_volume = str(bar.v)

            # Writes formatted line to CSV file
            data_file.write(ret_day + "," + ret_open + "," + ret_high + "," + ret_low + "," + ret_close + "," + ret_volume + "\n")

        data_file.close()


def get_test_data():
    for symbol in assets:
        data_file = open(storageLocation + '{0}_Intraday_Test.csv'.format(symbol), 'w')
        data_file.write("date,open,high,low,close,volume\n")

        returned_data = api.polygon.historic_agg_v2(symbol, 1, 'day', testFromDate, testToDate)

        # Reads, formats and stores the new bars
        for bar in returned_data:
            x = datetime.utcfromtimestamp(bar.t/1000)
            ret_day = x.strftime("%Y-%m-%d %H:%M").split(" ")[0]
            ret_open = str(bar.o)
            ret_high = str(bar.h)
            ret_low = str(bar.l)
            ret_close = str(bar.c)
            ret_volume = str(bar.v)

            # Writes formatted line to CSV file
            data_file.write(ret_day + "," + ret_open + "," + ret_high + "," + ret_low + "," + ret_close + "," + ret_volume + "\n")

        data_file.close()


def test_polygon_api():
    print(testApi.grouped_daily('2019-02-01'))


if __name__ == '__main__':
    get_training_data()
    get_test_data()
