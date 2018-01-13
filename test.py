from currency_factory.currency_manager import CurrencyManager
from user import User
from wallet import Wallet

#creating user
user1 = User(1, "Tomasz", "Kowalski", "tomcio123", "12345")

#get user informations
user1.info()

#get wallet informations
user1.wallet.info()

#manage wallet
user1.wallet.depositMoney("BTC", 30)
user1.wallet.depositMoney("ETH", 50)
user1.wallet.depositMoney("BTC", 50)
user1.wallet.withdrawMoney("ETH", 60)
user1.wallet.withdrawMoney("ETH", 20)
user1.wallet.withdrawMoney("ETH", 30)
user1.wallet.withdrawMoney("ETH", 1)

user1.wallet.info()