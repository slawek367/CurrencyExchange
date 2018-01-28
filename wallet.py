from config import Config
from db import Db
from currency_factory.currency_manager import CurrencyManager

class Wallet():
        def __init__(self, userId):
            self.userId = userId
            self.currencyManager = CurrencyManager()
            

        @staticmethod
        def registerWallet(username):
            db = Db()
            id = db.querySelectOne('SELECT id FROM users WHERE username="%s" LIMIT 1' %username)
            
            if not id is False:
                db.queryInsert("INSERT INTO wallets(user_id, BTC, ETH, LTC, USD) VALUES (%s, %s, %s, %s, %s)", (id[0], 0, 0, 0, Config.startUsdMoney))
                return True
            else:
                return False
            
'''
    def __init__(self, userId):
        self.id = userId
        self.currencies = []
    
    def depositMoney(self, name, count):
        if(count<=0):
            return False

        if self.isCurrencyInWallet(name):
            self.currencies[self.findCurrencyInListIndex(name)][1] += count*(1-Config.depositTax)
            return True
        else:
            self.addNewCurrency(name, count)
    
    def withdrawMoney(self, name, count):
        if(count<=0):
            return False

        if self.isCurrencyInWallet(name):
            index = self.findCurrencyInListIndex(name)

            if self.currencies[index][1] >= count:
                self.currencies[index][1] -= count
                return True
        else:
            return False

    def addNewCurrency(self, name, count):
        
        currencyManager = CurrencyManager()
        currency = currencyManager.getCurrency(name)

        if currency is None:
            print("Wrong currency name...")
            return False
        else:
            self.currencies.append([currency, count])
            return True
    
    def isCurrencyInWallet(self, name):
        for x in self.currencies:
            if x[0].getName() == name:
                return True
        
        return False
    
    def findCurrencyInListIndex(self, name):
        for x in self.currencies:
            if x[0].getName() == name:
                return self.currencies.index(x)
        
        return False
    
    def info(self):
        print("\nWallet info:")

        if len(self.currencies) < 1:
            print("No founds")

        for currency, count in self.currencies:
            print("Currency:%s\tCount: %s\tDollar exchange: %s$\t\tTotal: %s$" %(currency.getName(), count, currency.getPriceUsd(), count*currency.getPriceUsd()))
'''