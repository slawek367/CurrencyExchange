from currency_factory.currency import Currency
from currency_factory.coinmarket_api import CoinmarketApi

class LtcCurrency(Currency):

    def __init__(self):
        super().__init__("LTC")