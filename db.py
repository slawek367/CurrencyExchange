from config import singleton

@singleton
class Db():

    def __init__(self, app):
        pass
    
    def query(self, queryToExecute):
        self.cur.execute(queryToExecute)