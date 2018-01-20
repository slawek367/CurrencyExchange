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

        self.cnx = mysql.connector.connect(**self.config)
        self.cursor = self.cnx.cursor();
    
    def query(self, queryToExecute):
        self.cursor.execute(queryToExecute)
