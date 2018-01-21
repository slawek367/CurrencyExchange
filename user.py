class User:

    def __init__(self, id, username, email, password, name, surrname):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.name = name
        self.surrname = surrname
    
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

    def getUsername(self):
        return self.username
    
    def changePassword(self, oldPassword, newPassword):
        if self.password == oldPassword:
            self.password = newPassword
            return 1
        else:
            return 0
    
    def info(self):
        print("\nUser informations:\n")
        print("ID: %s" %self.id)
        print("Name: %s" %self.name)
        print("Surrname: %s" %self.surrname)
        print("Username: %s" %self.username)