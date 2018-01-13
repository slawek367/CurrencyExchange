from currency_factory.currency import Currency
from currency_factory.coinmarket_api import CoinmarketApi

class LskCurrency(Currency):

    def __init__(self):
        super().__init__("LSK")
        self.priceUsd = self.updateCurrentPriceUsd()
        
    def updateCurrentPriceUsd(self):
        return CoinmarketApi.getLskPrice()