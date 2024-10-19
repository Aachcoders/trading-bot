from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from bot.handlers import start, register, buy_order, sell_order, dca
from bot.utils import error
from bot.database import init_db
from bot.copy_trading import copy_trade
from bot.eth_sol_bridge import swap_eth_to_sol, swap_sol_to_eth
from bot.pump_fun import trade_pump_fun_token

# Main menu display
def start(update, context):
    """Send a welcome message with options to the user."""
    keyboard = [
        [InlineKeyboardButton("Register", callback_data='register')],
        [InlineKeyboardButton("Buy Order", callback_data='buy')],
        [InlineKeyboardButton("Sell Order", callback_data='sell')],
        [InlineKeyboardButton("DCA Order", callback_data='dca')],
        [InlineKeyboardButton("Copy Trade", callback_data='copytrade')],
        [InlineKeyboardButton("Swap ETH to SOL", callback_data='swapethsol')],
        [InlineKeyboardButton("Swap SOL to ETH", callback_data='swapsoleth')],
        [InlineKeyboardButton("Pump Token Trade", callback_data='pumptrade')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to Trojan Trading Bot! Please select an option:', reply_markup=reply_markup)

# Handle button clicks and route to appropriate functions
def button(update, context):
    """Handle button click events from the InlineKeyboard."""
    query = update.callback_query
    query.answer()

    # Routing based on the callback data
    if query.data == 'register':
        register(update, context)
    elif query.data == 'buy':
        buy_order(update, context)
    elif query.data == 'sell':
        sell_order(update, context)
    elif query.data == 'dca':
        dca(update, context)
    elif query.data == 'copytrade':
        copy_trade(update, context)
    elif query.data == 'swapethsol':
        swap_eth_to_sol(update, context)
    elif query.data == 'swapsoleth':
        swap_sol_to_eth(update, context)
    elif query.data == 'pumptrade':
        trade_pump_fun_token(update, context)
    else:
        query.message.reply_text("Invalid selection. Please choose a valid option.")

def main():
    """Start the Telegram bot and handle commands."""
    # Create an Updater object with the bot token
    updater = Updater('7432436789:AAG9DXdWe4kPDdM3W3S7dcQYa_VoCf7AYvo', use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command and callback query handlers
    dp.add_handler(CommandHandler("start", start))  # Start command handler
    dp.add_handler(CallbackQueryHandler(button))    # Inline button handler
    dp.add_error_handler(error)                      # Error handler

    # Initialize the database
    init_db()

    # Start polling for updates from Telegram
    updater.start_polling()
    updater.idle()  # Block until the bot is stopped

if __name__ == "__main__":
    main()
    
