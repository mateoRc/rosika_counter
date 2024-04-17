import sqlite3


class SQLiteDatabase:
    def __init__(self, db_name='button_events.db'):
        self.conn = None
        self.db_name = db_name

    def init_db(self):
        print("init database...")
        self.conn = sqlite3.connect('button_events.db')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS events
                              (id INTEGER PRIMARY KEY AUTOINCREMENT,
                              button_id TEXT,
                              timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                              sent BOOLEAN)''')
