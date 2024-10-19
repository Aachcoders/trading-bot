import sqlite3
from telegram import Update
from telegram.ext import CallbackContext

# Initialize the SQLite database
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

# Function to register user's wallet address
def register_wallet(update: Update, context: CallbackContext):
    telegram_id = update.message.from_user.id
    user_message = update.message.text

    try:
        # Parse user input (expecting: "/register <wallet_address>")
        _, wallet_address = user_message.split()

        # Register or update the user's wallet in the database
        conn = sqlite3.connect('trading_bot.db')
        cursor = conn.cursor()
        cursor.execute('INSERT OR REPLACE INTO users (telegram_id, wallet_address) VALUES (?, ?)', (telegram_id, wallet_address))
        conn.commit()
        conn.close()

        # Send confirmation message to the user
        update.message.reply_text(f"Wallet address {wallet_address} registered successfully for user {telegram_id}.")

    except ValueError:
        update.message.reply_text("Invalid input. Please use the command format: /register <wallet_address>.")
    except Exception as e:
        update.message.reply_text(f"An error occurred while registering the wallet: {e}")

# Function to retrieve a user's wallet address
def get_user_wallet(update: Update, context: CallbackContext):
    telegram_id = update.message.from_user.id

    try:
        # Retrieve the wallet address for the given Telegram user
        conn = sqlite3.connect('trading_bot.db')
        cursor = conn.cursor()
        cursor.execute('SELECT wallet_address FROM users WHERE telegram_id = ?', (telegram_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            update.message.reply_text(f"Your registered wallet address is: {row[0]}")
        else:
            update.message.reply_text("No wallet address found for your account. Please register using /register <wallet_address>.")

    except Exception as e:
        update.message.reply_text(f"An error occurred while retrieving your wallet: {e}")
        
