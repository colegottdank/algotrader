import backtrader.feeds as btfeeds
import backtrader as bt
from DataGrabber import assetsToDownload


class JoesStrat(bt.Strategy):

    def __init__(self):
        self.dataclose = self.data.close
        self.dataopen = self.data.open
        self.sma = bt.indicators.SimpleMovingAverage(self.data[0], period=10)

    def next(self):
        if self.order or self.position:
            return



if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.addstrategy(JoesStrat)

    data = btfeeds.GenericCSVData(
        dataname='../Data/AAPL.csv',
        nullvalue=0.0,
        dtformat=('%Y-%m-%d'),
        datetime=0,
        high=2,
        low=3,
        open=1,
        close=4,
        volume=5,
        openinterest=-1
    )

    cerebro.adddata(data)
    cerebro.broker.set_cash(10000)
    cerebro.run()
    cerebro.plot()
