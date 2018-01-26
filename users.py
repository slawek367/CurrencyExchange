from user import User
from db import Db
from passlib.hash import sha256_crypt

class Users():

    def __init__(self):
        self.userList = {}
        self.userMaxId = 0

    @staticmethod
    def addUser(username, email, password, name, surrname):
        db = Db()
        db.queryInsert("INSERT INTO users(username, email, password, name, surrname) VALUES(%s, %s, %s, %s, %s)", (username, email, sha256_crypt.encrypt(str(password)), name, surrname))

    def deleteUser(self, user):
        if user.id in self.userList:
            del self.userList[user.id]
            #self.userMaxId = self.userMaxId - 1
            return True

        return False

    @staticmethod
    def getUserList():
        userList = {}
        db = Db()
        userListResponse = db.querySelect("SELECT id, username, email, password, name, surrname FROM users")
        
        for id, username, email, password, name, surrname in userListResponse:
            user = User(id, username, email, password, name, surrname)
            userList[id] = user

        return userList;

    def checkLoginAndPassword(login, password):
        userList = {}
        db = Db()
        passwordHashed = db.getPassword('SELECT password FROM users WHERE username="%s" OR email="%s" LIMIT 1' %(login, login))

        if passwordHashed is False:
            return False
        elif sha256_crypt.verify(password, passwordHashed):
            return True
        else:
            return False

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