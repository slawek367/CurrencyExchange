from currency_factory.currency_manager import CurrencyManager
from wallet import Wallet

mywallet = Wallet(1)
print(mywallet.currencies)
mywallet.depositMoney("BTC", 30)
mywallet.depositMoney("ETH", 50)
mywallet.depositMoney("BTC", 50)
mywallet.withdrawMoney("ETH", 60)
mywallet.withdrawMoney("ETH", 20)
mywallet.withdrawMoney("ETH", 30)
mywallet.withdrawMoney("ETH", 1)
print(mywallet.currencies)

