import sqlite3

def initialize_db():

    conn = sqlite3.connect("budgit.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id TEXT PRIMARY KEY,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_db()
    print("Database initialized sucessfully.")