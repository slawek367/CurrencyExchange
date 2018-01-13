from currency_factory.currency import Currency

class BtcCurrency(Currency):

    def __init__(self):
        super().__init__("BTC")
        self.priceUsd = self.updateCurrentPriceUsd()

    def updateCurrentPriceUsd(self):
        return 50000