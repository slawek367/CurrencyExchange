from currency_factory.currency_manager import CurrencyManager
from user import User
from wallet import Wallet
from users import Users

#get user informations
#user1.info()

#get wallet informations
#user1.wallet.info()

#manage wallet
'''
user1.wallet.depositMoney("BTC", 30)
user2.wallet.depositMoney("ETH", 50)
user3.wallet.depositMoney("BTC", 50)
user1.wallet.withdrawMoney("BTC", 15)
user2.wallet.withdrawMoney("ETH", 20)
user3.wallet.withdrawMoney("BTC", 20)
'''

userList = Users()
userList.addUser("Tomasz", "Kowalski", "tomcio123", "12345")
userList.addUser("Robert", "Mateja", "matej123", "12345")
userList.addUser("Jarek", "Kon", "jaro123", "12345")
userList.printUsers()

print("\n@@@ Deleting tomcio123 @@@\n")
userList.deleteUser(userList.getUser(login="tomcio123"))

print("\n@@@ Adding 30btc to matej123 account @@@\n")
userList.getUser(login="matej123").wallet.depositMoney("BTC", 30)

userList.printUsers()
