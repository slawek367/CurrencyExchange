#metoda wytworcza, singleton

class User:

    def __init__(self, id, name, surrname, login, password):
        self.id = id
        self.name = name
        self.surrname = surrname
        self.login = login
        self.password = password
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def setSurrname(self, newSurrname):
        self.surrname = newSurrname

    def getSurrname(self):
        return self.surrname

    def getLogin(self):
        return self.login
    
    def changePassword(self, oldPassword, newPassword):
        if self.password == oldPassword:
            self.password = newPassword
            return 1
        else:
            return 0
