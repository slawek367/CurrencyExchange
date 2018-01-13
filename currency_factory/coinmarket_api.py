import urllib.request
import json

class CoinmarketApi:
    
    btcUrl = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
    ethUrl = "https://api.coinmarketcap.com/v1/ticker/ethereum/"
    ltcUrl = "https://api.coinmarketcap.com/v1/ticker/litecoin/"

    @staticmethod
    def getPrice(currencyUrlApi):
        with urllib.request.urlopen(currencyUrlApi) as url:
            data = json.loads(url.read().decode())
            return(data[0]["price_usd"])

    @staticmethod
    def getBtcPrice():
        return (float(CoinmarketApi.getPrice(CoinmarketApi.btcUrl)))

    @staticmethod
    def getEthPrice():
        return (float(CoinmarketApi.getPrice(CoinmarketApi.ethUrl)))

    @staticmethod
    def getLtcPrice():
        return (float(CoinmarketApi.getPrice(CoinmarketApi.ltcUrl)))