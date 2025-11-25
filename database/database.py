# database/database.py
# Handles SQLite connection and table creation

import sqlite3

class Database:
    def __init__(self, db_path="logistech.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS shipment_logs (
                tracking_id TEXT,
                bin_id INTEGER,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                status TEXT
            )
            """
        )
        self.conn.commit()

    def log_event(self, tracking_id, bin_id, status):
        self.cursor.execute(
            "INSERT INTO shipment_logs (tracking_id, bin_id, status) VALUES (?, ?, ?)",
            (tracking_id, bin_id, status)
        )
        self.conn.commit()

    def close(self):
        self.conn.close()