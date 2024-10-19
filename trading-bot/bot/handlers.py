from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from .transaction import buy, sell
from .database import register_wallet, get_user_wallet
from .scheduler import start_dca

# Start command handler with welcome message
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome to Trojan Trading Bot! 🚀\n"
        "Here’s what you can do:\n"
        "• /register <wallet_address> - Register your wallet\n"
        "• /buy <token> <amount> <price> - Place a buy order\n"
        "• /sell <token> <amount> <price> - Place a sell order\n"
        "• /dca <token> <amount> <interval> - Set up Dollar-Cost Averaging (DCA)\n"
        "Type /help for more details."
    )

# Wallet registration handler
def register(update: Update, context: CallbackContext) -> None:
    if context.args:
        wallet_address = context.args[0]
        register_wallet(update.message.from_user.id, wallet_address)
        update.message.reply_text(f"✅ Wallet {wallet_address} successfully registered!")
    else:
        update.message.reply_text("❌ Please provide a wallet address. Usage: /register <wallet_address>")

# Buy order handler
def buy_order(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 3:
        try:
            token = context.args[0]
            amount = float(context.args[1])
            price = float(context.args[2])
            buy(update, token, amount, price)
            update.message.reply_text(f"💰 Placing a buy order for {amount} of {token} at ${price}.")
        except ValueError:
            update.message.reply_text("❌ Invalid amount or price. Please ensure they are numbers.")
    else:
        update.message.reply_text("❌ Incorrect usage. Usage: /buy <token> <amount> <price>")

# Sell order handler
def sell_order(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 3:
        try:
            token = context.args[0]
            amount = float(context.args[1])
            price = float(context.args[2])
            sell(update, token, amount, price)
            update.message.reply_text(f"📉 Placing a sell order for {amount} of {token} at ${price}.")
        except ValueError:
            update.message.reply_text("❌ Invalid amount or price. Please ensure they are numbers.")
    else:
        update.message.reply_text("❌ Incorrect usage. Usage: /sell <token> <amount> <price>")

# Dollar-Cost Averaging (DCA) handler
def dca(update: Update, context: CallbackContext) -> None:
    if len(context.args) == 3:
        try:
            token = context.args[0]
            amount = float(context.args[1])
            interval = int(context.args[2])
            start_dca(update, token, amount, interval)
            update.message.reply_text(f"📊 DCA set up for {amount} of {token} across {interval} intervals.")
        except ValueError:
            update.message.reply_text("❌ Invalid amount or interval. Please ensure they are numbers.")
    else:
        update.message.reply_text("❌ Incorrect usage. Usage: /dca <token> <amount> <interval>")

