import json
from user import User
from wallet import Wallet
from users import Users

class Serialize():
    
    @staticmethod
    def toJSON(self):
        data = json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        
        file = open("savedUsers.json","w") 
        file.write(data) 
        file.close()

    @staticmethod
    def loadJSON():
        data = json.load(open('savedUsers.json'))
        users = Users()
        users.userMaxId = data["userMaxId"]

        for userId in data["userList"]:
            createdUser = User(
                data["userList"][userId]["id"],
                data["userList"][userId]["name"],
                data["userList"][userId]["surrname"],
                data["userList"][userId]["login"],
                data["userList"][userId]["password"]
            )
            
            userWallet = Wallet(userId)
            for walletCurrency, count in data["userList"][userId]["wallet"]["currencies"]:
                userWallet.depositMoney(walletCurrency["name"], count)

            createdUser.wallet = userWallet
            users.userList[userId] = createdUser
        
        return users