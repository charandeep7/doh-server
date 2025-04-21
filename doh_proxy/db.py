import sqlite3
import os

DB_FILE = "logs/dns_logs.db"
os.makedirs("logs", exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            client_ip TEXT,
            domain TEXT,
            cache_hit BOOLEAN,
            ttl INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def log_to_db(timestamp, client_ip, domain, cache_hit, ttl):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO queries (timestamp, client_ip, domain, cache_hit, ttl)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, client_ip, domain, cache_hit, ttl))
    conn.commit()
    conn.close()