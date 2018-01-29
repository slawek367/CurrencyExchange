import urllib.request
import json

#import Db from parent folder
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from db import Db

class CoinmarketApi:
    coinApiUrl = "https://api.coinmarketcap.com/v1/ticker/"

    btcUrl = "https://api.coinmarketcap.com/v1/ticker/bitcoin/"
    ethUrl = "https://api.coinmarketcap.com/v1/ticker/ethereum/"
    ltcUrl = "https://api.coinmarketcap.com/v1/ticker/litecoin/"

    @staticmethod
    def updateDatabase(currencies):
        db = Db()
        with urllib.request.urlopen(CoinmarketApi.coinApiUrl) as url:
            data = json.loads(url.read().decode())

            for currencySymbol in currencies:
                for currencyData in data:
                    if currencySymbol == currencyData["symbol"]:
                        name = currencyData["name"]
                        rank = currencyData["rank"]
                        priceUsd = currencyData["price_usd"]
                        priceBtc = currencyData["price_btc"]
                        marketCap = currencyData["market_cap_usd"]
                        availableSupply = currencyData["available_supply"]
                        totalSupply = currencyData["total_supply"]
                        change1h = currencyData["percent_change_1h"]
                        change24h = currencyData["percent_change_24h"]
                        change7d = currencyData["percent_change_7d"]
                        db.queryInsert("INSERT INTO \
                        coinmarket_data(symbol, name, rank, priceUsd, priceBtc, marketCap, availableSupply, totalSupply, change1h, change24h, change7d) \
                        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", \
                        (currencySymbol, name, rank, priceUsd, priceBtc, marketCap, availableSupply, totalSupply, change1h, change24h, change7d))
                        break
                    else:
                        continue

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