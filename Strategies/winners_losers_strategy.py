import backtrader.feeds as btfeeds
import backtrader as bt

assets = ['AAPL', 'AA', 'A', 'AAC', 'AAN', 'AAT']


class WinnersLosersStrategy(bt.Strategy):
    params = (
        ('momentumperiod', 10),
        ('oneplot', False)
    )

    def log(self, txt, dt=None):
        ''' Logging function fot this strategy'''
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        self.inds = dict()
        for i, d in enumerate(self.datas):
            self.inds[d] = {}
            self.inds[d]["momentum"] = bt.indicators.Momentum(d.close)
            if i > 0:  # Check we are not on the first loop of data feed:
                if self.p.oneplot == True:
                    d.plotinfo.plotmaster = self.datas[0]

    def next(self):
        for d in self.datas:
            if self.inds[d]["momentum"] > 2:
                self.sell(data=d)
            elif self.inds[d]["momentum"] < -2:
                self.buy(data=d)

    def notify_trade(self, trade):
        dt = self.data.datetime.date()
        if trade.isclosed:
            print('{} {} Closed: PnL Gross {}, Net {}'.format(
                                                dt,
                                                trade.data._name,
                                                round(trade.pnl,2),
                                                round(trade.pnlcomm,2)))


if __name__ == '__main__':
    cerebro = bt.Cerebro()
    cerebro.addstrategy(WinnersLosersStrategy)
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    for symbol in assets:
        path = "{}_Intraday_Training".format(symbol)
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
        cerebro.adddata(data, name=symbol)

    cerebro.broker.set_cash(10000)
    cerebro.broker.setcommission(commission=0.001)
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.plot()