import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from db import Db

class Currency():

    def __init__(self, name):
        self.name = name
        
        self.fullName = None
        self.rank = None
        self.priceUsd = None
        self.priceBtc = None
        self.marketCap = None
        self.availableSupply = None
        self.totalSupply = None
        self.maxSupply = None
        self.change1h = None
        self.change24h = None
        self.change7d = None
        self.updatedDate = None
        self.updateData()

    def getName(self):
        return self.name

    def getPriceUsd(self):
        #self.updateData()
        return self.priceUsd

    def getCount(self, user_id):
        db = Db()
        count = db.querySelectOne('SELECT %s FROM wallets WHERE user_id="%s" LIMIT 1' %(self.name, user_id))[0]
        return count
    
    def updateData(self):
        db = Db()
        response = db.querySelectOne('SELECT name, rank, priceUsd, marketCap, availableSupply, totalSupply, maxSupply, change1h, change24h, change7d, date FROM coinmarket_data WHERE date IN (SELECT max(date) FROM coinmarket_data WHERE symbol="%s") AND symbol="%s"' %(self.name, self.name))
        self.fullName, self.rank, self.priceUsd, self.marketCap, self.availableSupply, self.totalSupply, self.maxSupply, self.change1h, self.change24h, self.change7d, self.date = response