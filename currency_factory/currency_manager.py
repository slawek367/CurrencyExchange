from currency_factory.lsk import LskCurrency
from currency_factory.eth import EthCurrency
from currency_factory.btc import BtcCurrency

class CurrencyManager():
    currencies = {"ETH":EthCurrency, "BTC":BtcCurrency, "LSK":LskCurrency}

    def __init__(self):
        pass
    
    def getCurrency(self, name):
        if name in self.currencies.keys():
            return self.currencies[name]()