from user import User
from db import Db

class Users():

    def __init__(self):
        self.userList = {}
        self.userMaxId = 0
    
    def addUser(name, surrname, login, email, password):
        db = Db()
        db.query("INSERT INTO users(name, surrname, email, login, password) VALUES(%s, %s, %s, %s, %s)", (name, surrname, login, email, password))
    
    def deleteUser(self, user):
        if user.id in self.userList:
            del self.userList[user.id]
            #self.userMaxId = self.userMaxId - 1
            return True
        
        return False
    
    def getUserList(self):
        return self.userList;

    def getUser(self, id = None, name = None, surrname = None, login = None):
        if not id == None:
            if id in self.userList:
                return self.userList[id]

        if not name == None and not surrname == None:
            users = []
            for key, value in self.userList.items():
                if value.getName == name and value.getSurrname == surrname:
                    users.append(value)
            return users

        if not login == None:
            for key, value in self.userList.items():
                if value.getLogin() == login:
                    return value

        return False

    def printUsers(self):
        for key, value in self.userList.items():
            value.info()
    
    def loadUsers(self):
        pass
        #TODO