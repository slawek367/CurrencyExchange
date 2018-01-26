from config import singleton
import mysql.connector


@singleton
class Db():

    def __init__(self):
        self.config = {
        'user': 'root',
        'password': '123456',
        'host': 'localhost',
        'database': 'currency_exchange',
        'raise_on_warnings': True,
        'use_pure': False
        }

    def queryInsert(self, queryToExecute, params):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor();
        self.cursor.execute(queryToExecute, params)
        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()

    def querySelect(self, queryToExecute):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor();
        self.cursor.execute(queryToExecute)
        items = self.cursor.fetchall()

        self.cursor.close()
        self.cnx.close()

        return items
    
    def getPassword(self, queryToExecute):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor();
        self.cursor.execute(queryToExecute)
        password = self.cursor.fetchone()

        self.cursor.close()
        self.cnx.close()

        if password is None:
            return False
        else:
            return password[0]