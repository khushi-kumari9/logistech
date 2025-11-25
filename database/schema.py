# database/schema.py
# Responsible for creating the required SQL tables

import sqlite3

def create_tables(db_path="logistech.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Shipment logs table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shipment_logs (
            tracking_id TEXT,
            bin_id INTEGER,
            timestamp DATETIME,
            status TEXT
        )
    """)

    # Bin configuration table (optional but useful)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bins (
            bin_id INTEGER PRIMARY KEY,
            capacity INTEGER,
            location_code TEXT
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database schema created successfully!")

