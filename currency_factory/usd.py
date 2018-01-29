from currency_factory.currency import Currency
from currency_factory.coinmarket_api import CoinmarketApi

class UsdCurrency(Currency):

    def __init__(self):
        self.name = "USD"
        
    def getPriceUsd(self):
        return 1