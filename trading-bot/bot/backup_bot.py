# bot/backup_bot.py
from random import choice

# List of backup bot tokens (you should have them in your config)
BACKUP_BOTS = [
    "BACKUP_BOT_TOKEN_1",
    "BACKUP_BOT_TOKEN_2",
    "BACKUP_BOT_TOKEN_3",
    "BACKUP_BOT_TOKEN_4",
    "BACKUP_BOT_TOKEN_5",
    "BACKUP_BOT_TOKEN_6",
    "BACKUP_BOT_TOKEN_7"
]

def switch_to_backup_bot():
    """Switch to a backup bot if the main bot experiences heavy load."""
    return choice(BACKUP_BOTS)
