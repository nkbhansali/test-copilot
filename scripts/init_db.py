import sqlite3
import os
from datetime import datetime

DATABASE_URL = "/Users/naveenbhansali/git/flights/data/flights.db"

def initialize_database():
    if os.path.exists(DATABASE_URL):
        os.remove(DATABASE_URL)
    conn = sqlite3.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS flights (
        flight_id INTEGER PRIMARY KEY,
        flight_no TEXT NOT NULL,
        scheduled_departure TIMESTAMP NOT NULL,
        scheduled_arrival TIMESTAMP NOT NULL,
        departure_airport TEXT NOT NULL,
        arrival_airport TEXT NOT NULL,
        status TEXT NOT NULL,
        aircraft_code TEXT NOT NULL,
        airline_name TEXT NOT NULL
    );
    ''')
    # Insert dummy data
    cursor.executemany('''
    INSERT INTO flights (flight_no, scheduled_departure, scheduled_arrival, departure_airport, arrival_airport, status, aircraft_code, airline_name)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', [
        ("AA123", datetime(2023, 10, 1, 8, 0), datetime(2023, 10, 1, 10, 0), "JFK", "LAX", "On Time", "A320", "American Airlines"),
        ("BA456", datetime(2023, 10, 2, 9, 0), datetime(2023, 10, 2, 11, 0), "LHR", "CDG", "Delayed", "B737", "British Airways"),
        ("CA789", datetime(2023, 10, 3, 10, 0), datetime(2023, 10, 3, 12, 0), "PEK", "HND", "Cancelled", "A380", "China Airlines")
    ])
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
