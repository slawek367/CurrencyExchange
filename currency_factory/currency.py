
class Currency():

    def __init__(self, name):
        self.priceUsd = None
        self.name = name
    
    def updateCurrentPriceUsd(self):
        pass
    
    def getName(self):
        return self.name
    
    def getPriceUsd(self):
        self.priceUsd = self.updateCurrentPriceUsd()
        return self.priceUsd