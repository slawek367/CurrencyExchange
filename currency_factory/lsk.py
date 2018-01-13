from currency_factory.currency import Currency

class LskCurrency(Currency):

    def __init__(self):
        super().__init__("LSK")
        self.priceUsd = self.updateCurrentPriceUsd()
        
    def updateCurrentPriceUsd(self):
        return 230