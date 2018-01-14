from currency_factory.currency_manager import CurrencyManager
from user import User
from wallet import Wallet
from users import Users
from serialize import Serialize

userList = Users()
userList = Serialize.loadJSON()

'''
userList.addUser("Tomasz", "Kowalski", "tomcio123", "12345")
userList.addUser("Robert", "Mateja", "matej123", "12345")
userList.addUser("Jarek", "Kon", "jaro123", "12345")
userList.printUsers()
'''

'''
print("\n@@@ Deleting tomcio123 @@@\n")
userList.deleteUser(userList.getUser(login="tomcio123"))

print("\n@@@ Adding 30btc to matej123 account @@@\n")
userList.getUser(login="matej123").wallet.depositMoney("BTC", 30)
'''
userList.printUsers()
Serialize.toJSON(userList)
