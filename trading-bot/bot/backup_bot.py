from random import choice
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

# List of backup bot tokens (these should ideally be stored in your config)
BACKUP_BOTS = [
    "BACKUP_BOT_TOKEN_1",
    "BACKUP_BOT_TOKEN_2",
    "BACKUP_BOT_TOKEN_3",
    "BACKUP_BOT_TOKEN_4",
    "BACKUP_BOT_TOKEN_5",
    "BACKUP_BOT_TOKEN_6",
    "BACKUP_BOT_TOKEN_7"
]

# Placeholder main bot token (this would be your main bot's token)
MAIN_BOT_TOKEN = "7432436789:AAG9DXdWe4kPDdM3W3S7dcQYa_VoCf7AYvo"


def notify_backup_switch(update, context):
    """Notify users that the bot is switching to a backup bot."""
    update.message.reply_text("Main bot is experiencing heavy load. Switching to a backup bot now...")


def switch_to_backup_bot():
    """Switch to a backup bot if the main bot experiences heavy load."""
    return choice(BACKUP_BOTS)


def handle_backup_switch(update, context):
    """Simulate the scenario where the bot switches to a backup bot and notify the user."""
    notify_backup_switch(update, context)

    # Logic to switch to a new bot token (in real use-case, this would restart with a new token)
    new_bot_token = switch_to_backup_bot()
    update.message.reply_text(f"Switched to backup bot with token: {new_bot_token}")


def start(update, context):
    """Initial start command with backup switch option."""
    keyboard = [
        [InlineKeyboardButton("Switch to Backup Bot", callback_data='switch_backup')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome! Choose an option below:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'switch_backup':
        handle_backup_switch(update, context)


def main():
    updater = Updater(MAIN_BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("switchbackup", handle_backup_switch))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
    
