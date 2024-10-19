from telegram import Update
from telegram.ext import CallbackContext
from .transaction import buy, sell
from .database import register_wallet
from .scheduler import start_dca
from .copy_trading import copy_trade
from .eth_sol_bridge import swap_eth_to_sol, swap_sol_to_eth
from .pump_fun import trade_pump_fun_token


# Start command handler with welcome message
def start(update: Update, context: CallbackContext) -> None:
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


# Wallet registration handler
def register(update: Update, context: CallbackContext) -> None:
    # Use message if present or callback query's message
    chat = update.message or update.callback_query.message

    if context.args:
        wallet_address = context.args[0]
        register_wallet(update.effective_user.id, wallet_address)
        chat.reply_text(f"✅ Wallet {wallet_address} successfully registered!")
    else:
        chat.reply_text("❌ Please provide a wallet address. Usage: /register <wallet_address>")


# Buy order handler
def buy_order(update: Update, context: CallbackContext) -> None:
    chat = update.message or update.callback_query.message

    if len(context.args) == 3:
        try:
            token = context.args[0]
            amount = float(context.args[1])
            price = float(context.args[2])
            buy(update, token, amount, price)
            chat.reply_text(f"💰 Placing a buy order for {amount} of {token} at ${price}.")
        except ValueError:
            chat.reply_text("❌ Invalid amount or price. Please ensure they are numbers.")
    else:
        chat.reply_text("❌ Incorrect usage. Usage: /buy <token> <amount> <price>")


# Sell order handler
def sell_order(update: Update, context: CallbackContext) -> None:
    chat = update.message or update.callback_query.message

    if len(context.args) == 3:
        try:
            token = context.args[0]
            amount = float(context.args[1])
            price = float(context.args[2])
            sell(update, token, amount, price)
            chat.reply_text(f"📉 Placing a sell order for {amount} of {token} at ${price}.")
        except ValueError:
            chat.reply_text("❌ Invalid amount or price. Please ensure they are numbers.")
    else:
        chat.reply_text("❌ Incorrect usage. Usage: /sell <token> <amount> <price>")


# Dollar-Cost Averaging (DCA) handler
def dca(update: Update, context: CallbackContext) -> None:
    chat = update.message or update.callback_query.message

    if len(context.args) == 3:
        try:
            token = context.args[0]
            amount = float(context.args[1])
            interval = int(context.args[2])
            start_dca(update, token, amount, interval)
            chat.reply_text(f"📊 DCA set up for {amount} of {token} across {interval} intervals.")
        except ValueError:
            chat.reply_text("❌ Invalid amount or interval. Please ensure they are numbers.")
    else:
        chat.reply_text("❌ Incorrect usage. Usage: /dca <token> <amount> <interval>")


# Copy trading handler
def copy_trade_handler(update: Update, context: CallbackContext) -> None:
    chat = update.message or update.callback_query.message
    copy_trade(update, context)
    chat.reply_text("🌀 Copy trading initiated!")


# ETH to SOL bridge handler
def swap_eth_sol(update: Update, context: CallbackContext) -> None:
    chat = update.message or update.callback_query.message
    swap_eth_to_sol(update, context)
    chat.reply_text("🌉 Swapping ETH to SOL.")


# SOL to ETH bridge handler
def swap_sol_eth(update: Update, context: CallbackContext) -> None:
    chat = update.message or update.callback_query.message
    swap_sol_to_eth(update, context)
    chat.reply_text("🌉 Swapping SOL to ETH.")


# Pump.fun trading handler
def pump_fun_handler(update: Update, context: CallbackContext) -> None:
    chat = update.message or update.callback_query.message
    trade_pump_fun_token(update, context)
    chat.reply_text("🚀 Pump.fun token trade initiated.")


# Error handling function
def error(update: Update, context: CallbackContext) -> None:
    try:
        if update.message:
            user_id = update.message.from_user.id
        elif update.callback_query:
            user_id = update.callback_query.from_user.id
        else:
            user_id = "unknown"
        
        print(f"Error with user ID {user_id}: {context.error}")
        
        # Notify user about the error
        if update.message:
            update.message.reply_text('An error occurred. Please try again later.')
        elif update.callback_query:
            update.callback_query.message.reply_text('An error occurred. Please try again later.')

    except Exception as e:
        print(f"Error while handling error: {e}")
        
