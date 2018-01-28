
from db import Db

class Currency():

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
    
    def getPriceUsd(self):
        pass
    
    def getCount(self, user_id):
        db = Db()
        count = db.querySelectOne('SELECT %s FROM wallets WHERE user_id="%s" LIMIT 1' %(self.name, user_id))[0]