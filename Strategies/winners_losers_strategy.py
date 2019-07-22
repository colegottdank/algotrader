import backtrader.feeds as btfeeds
import backtrader as bt

assets = ['AAPL', 'ABC', 'ACB', 'A', 'AA', 'AAC', 'AAN', 'AAP', 'AAT']


class WinnersLosersStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.momentum = bt.indicators.Momentum(self.data, period=1)
        return

    def next(self):
        if self.momentum[0] > 1:
            self.buy()
        elif self.momentum[0] < 0:
            self.sell()


if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.addstrategy(WinnersLosersStrategy)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    path = "A_Intraday_Training"
    data = btfeeds.GenericCSVData(
        dataname='../Data/{}.csv'.format(path),
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
    cerebro.broker.setcommission(commission=0.001)
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.plot()