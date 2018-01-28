from currency_factory.currency import Currency
from currency_factory.coinmarket_api import CoinmarketApi

class UsdCurrency(Currency):

    def __init__(self):
        super().__init__("USD")
        
    def getPriceUsd(self):
        return 1