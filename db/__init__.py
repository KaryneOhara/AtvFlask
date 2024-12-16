import sqlite3

banco = 'flask-sqlite.sql'

def get_db():
    conn = sqlite3.connect(banco)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    try:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL
            )
        ''')
        conn.commit()
    finally:
        conn.close()
