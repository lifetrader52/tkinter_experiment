import sqlite3

class DatabaseOperator():
    def __init__(self):
        self.conn = sqlite3.connect("db/pasiendb.db")
        print(self.conn)
        self.c = self.conn.cursor()
        print(self.c)

    def get_all_data(self,table_name):
        query = 'SELECT id, name from pasien '
        self.c.execute(query)
        print( self.c.fetchall() )
        return


