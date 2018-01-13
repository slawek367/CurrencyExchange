from currency_factory.currency import Currency

class EthCurrency(Currency):

    def __init__(self):
        super().__init__("ETH")
        self.priceUsd = self.updateCurrentPriceUsd()
        
    def updateCurrentPriceUsd(self):
        return 1200