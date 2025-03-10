import sqlite3

DATABASE_URL = "data/flights.db"  # Use a relative path

def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE_URL)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.DatabaseError as e:
        print(f"Database error: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise
