import alpaca_trade_api as tradeapi
import os
import csv

os.environ["APCA_API_BASE_URL"] = "https://api.alpaca.markets"
api = tradeapi.REST('AKBHEJ0EK9IO98U9DB8K', 'xXdnDTWWyExwkL7jrwsIOiOawnfaUQKVSykMBNk7')
account = api.get_account()
#api.list_positions()

storageLocation = "./Data"
barTimeframe = "1D"  # 1Min, 5Min, 15Min, 1H, 1D
assetsToDownload = ["SPY", "MSFT", "AAPL", "NFLX", "DOW", "TSLA"]

for a in assetsToDownload:
    symbol = a

    dataFile = ""
    lastDate = "2013-00-00T00:00:00.000Z"  # ISO8601 Date

    # Verifies if symbol file exists
    try:  # If file exists, reads the time of the last bar
        dataFile = open(storageLocation + '{0}.csv'.format(symbol), 'a+')
        lastDate = list(csv.DictReader(dataFile))[-1]["time"]
    except:  # If not, initialises new CSV file
        dataFile = open(storageLocation + '{0}.csv'.format(symbol), 'w')
        dataFile.write("open,high,low,close,volume\n")

    returned_data = api.get_barset(symbol, barTimeframe, 1000, start=lastDate)

    # Reads, formats and stores the new bars
    for name in returned_data:

        for bar in returned_data[name]:
            ret_open = str(bar.o)
            ret_high = str(bar.h)
            ret_low = str(bar.l)
            ret_close = str(bar.c)
            ret_volume = str(bar.v)

            # Writes formatted line to CSV file
            # dataFile.write(ret_time + "," + ret_open + "," + ret_high + "," + ret_low + "," + ret_close + "," + ret_volume)
            dataFile.write(ret_open + "," + ret_high + "," + ret_low + "," + ret_close + "," + ret_volume + "\n")

    dataFile.close()