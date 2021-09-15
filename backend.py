import sqlite3
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect("userinfodatabooks.db")
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, name TEXT, "
                    "email TEXT, source TEXT)""")
        self.conn.commit()

    def insert(self, name, email, source):
        print("data inserted")
        self.cur.execute("INSERT INTO book VALUES(NULL,?,?,?)", (name, email, source))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM BOOK")
        rows = self.cur.fetchall()
        print(rows)
        return rows

    def __del__(self):
        self.conn.close()