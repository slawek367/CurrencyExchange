import threading
from currency_factory.coinmarket_api import CoinmarketApi
from currency_factory.currency_manager import CurrencyManager
from config import Config

class Update():

    def __init__(self):
        self.curFactory = CurrencyManager()

    def updatePrices(self):
        threading.Timer(Config.updateDatabaseTime, self.updatePrices).start()
        CoinmarketApi.updateDatabase(self.curFactory.currencies.keys())        
