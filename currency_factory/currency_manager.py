from currency_factory.ltc import LtcCurrency
from currency_factory.eth import EthCurrency
from currency_factory.btc import BtcCurrency
from currency_factory.usd import UsdCurrency


class CurrencyManager():

    def __init__(self):
        self.currencies = {"ETH": EthCurrency, "BTC": BtcCurrency,
                           "LTC": LtcCurrency, "USD": UsdCurrency}

    def getCurrency(self, name):
        if name in self.currencies.keys():
            return self.currencies[name]()
