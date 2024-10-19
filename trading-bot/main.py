from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from bot.handlers import (
    start, register, buy_order, sell_order, dca, copy_trade_handler, swap_eth_sol, swap_sol_eth, pump_fun_handler, error
)
from bot.database import init_db

# Helper function to create the keyboard markup immutably
def create_main_menu():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Register Wallet 🏦", callback_data='register')],
        [InlineKeyboardButton("Place Buy Order 💰", callback_data='buy')],
        [InlineKeyboardButton("Place Sell Order 📉", callback_data='sell')],
        [InlineKeyboardButton("DCA Setup 📊", callback_data='dca')],
        [InlineKeyboardButton("Copy Trade 🌀", callback_data='copytrade')],
        [InlineKeyboardButton("Swap ETH to SOL 🌉", callback_data='swapethsol')],
        [InlineKeyboardButton("Swap SOL to ETH 🌉", callback_data='swapsoleth')],
        [InlineKeyboardButton("Pump.fun Trade 🚀", callback_data='pumptrade')],
    ])

# Start command handler - shows the main menu with friendly prompts
def start(update: Update, context: CallbackContext) -> None:
    """Welcome the user with a friendly message and display the main menu."""
    update.message.reply_text(
        "Hello and welcome to the Trojan Trading Bot! 😊\n"
        "I’m here to help you with your trading activities.\n"
        "Please select one of the options below to get started:",
        reply_markup=create_main_menu()
    )

# Button callback handler - immutable routing logic based on button clicks
def button(update: Update, context: CallbackContext) -> None:
    """Handle button clicks and route to the appropriate function."""
    query = update.callback_query
    query.answer()  # Acknowledge the button click

    # Map the callback data to the corresponding function
    actions = {
        'register': lambda: query.message.reply_text("Let's register your wallet! Please use /register <wallet_address> to get started."),
        'buy': lambda: query.message.reply_text("Time to place a buy order! Use /buy <token> <amount> <price> to proceed."),
        'sell': lambda: query.message.reply_text("Ready to sell? Use /sell <token> <amount> <price> to place a sell order."),
        'dca': lambda: query.message.reply_text("Set up DCA! Use /dca <token> <amount> <interval> to automate your investments."),
        'copytrade': lambda: copy_trade_handler(update, context),
        'swapethsol': lambda: swap_eth_sol(update, context),
        'swapsoleth': lambda: swap_sol_eth(update, context),
        'pumptrade': lambda: pump_fun_handler(update, context),
    }

    # Execute the corresponding action
    actions.get(query.data, lambda: query.message.reply_text("Oops! Something went wrong. Please try again."))()

# Main function - friendly setup and message flow
def main():
    """Initialize the bot with friendly message flows."""
    # Create Updater and Dispatcher
    updater = Updater('YOUR_BOT_TOKEN', use_context=True)
    dp = updater.dispatcher

    # Command handlers for user interaction
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("register", register))
    dp.add_handler(CommandHandler("buy", buy_order))
    dp.add_handler(CommandHandler("sell", sell_order))
    dp.add_handler(CommandHandler("dca", dca))

    # Handle button callbacks from the InlineKeyboard
    dp.add_handler(CallbackQueryHandler(button))

    # Error handler for friendly notifications
    dp.add_error_handler(error)

    # Initialize the database immutably
    init_db()

    # Start polling for updates
    updater.start_polling()

    # Block the bot until stopped
    updater.idle()

if __name__ == "__main__":
    main()
    
