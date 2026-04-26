import sqlite3

# Name of the SQLite database file
DB_NAME = "mind_balance.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    
    # Establish connection to SQLite database
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sleep REAL,
            screen REAL,
            exercise REAL,
            social REAL,
            risk TEXT,
            score REAL
        )
    """)

    conn.commit()
    conn.close()


def save_record(sleep, screen, exercise, social, risk, score):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Insert new record using parameterised query (prevents SQL injection)
    c.execute("""
        INSERT INTO records (sleep, screen, exercise, social, risk, score)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (sleep, screen, exercise, social, risk, score))

    conn.commit()
    conn.close()