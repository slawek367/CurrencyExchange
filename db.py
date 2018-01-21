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
    
    def query(self, queryToExecute, params=None):
        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor();

        if params == None:
            self.cursor.execute(queryToExecute)
        else:
            self.cursor.execute(queryToExecute, params)

        self.cnx.commit()
        self.cursor.close()
        self.cnx.close()
