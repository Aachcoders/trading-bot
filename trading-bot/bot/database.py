# bot/database.py
import sqlite3

def init_db():
    conn = sqlite3.connect('trading_bot.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            telegram_id INTEGER PRIMARY KEY,
            wallet_address TEXT
        )
    ''')
    conn.commit()
    conn.close()

def register_wallet(telegram_id, wallet_address):
    conn = sqlite3.connect('trading_bot.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO users (telegram_id, wallet_address) VALUES (?, ?)', (telegram_id, wallet_address))
    conn.commit()
    conn.close()

def get_user_wallet(telegram_id):
    conn = sqlite3.connect('trading_bot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT wallet_address FROM users WHERE telegram_id = ?', (telegram_id,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
