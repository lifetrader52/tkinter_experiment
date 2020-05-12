import sqlite3
conn = sqlite3.connect("db/pasiendb.db")

c = conn.cursor()
c.execute('DROP TABLE IF EXISTS pasien')
c.execute('CREATE TABLE IF NOT EXISTS pasien(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT) ')

# insert data pertamanya
c.execute('''INSERT INTO PASIEN(name) VALUES('steven') ''')
c.execute('''INSERT INTO PASIEN(name) VALUES('irawan') ''')

conn.commit()
conn.close()



