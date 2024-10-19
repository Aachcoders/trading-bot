from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from .transaction import buy, sell
from .database import register_wallet, get_user_wallet
from .scheduler import start_dca
from .copy_trading import copy_trade
from .eth_sol_bridge import swap_eth_to_sol, swap_sol_to_eth
from .pump_fun import trade_pump_fun_token

# Start command handler with a welcome message
def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message and instructions on how to use the bot."""
    update.message.reply_text(
        "Welcome to Trojan Trading Bot! 🚀\n"
        "Here’s what you can do:\n"
        "• /register <wallet_address> - Register your wallet\n"
        "• /buy <token> <amount> <price> - Place a buy order\n"
        "• /sell <token> <amount> <price> - Place a sell order\n"
        "• /limit <token> <amount> <price> - Place a limit order\n"
        "• /dca <token> <amount> <interval> - Set up Dollar-Cost Averaging (DCA)\n"
        "• /copytrade <solana_wallet> - Copy trade a Solana wallet\n"
        "• /swapethsol - Swap tokens between Ethereum and Solana\n"
        "• /pumptrade <contract_address> - Trade Pump.fun tokens\n"
        "• /wallet - Check your registered wallet address\n"
        "• /help - Display this help message again."
    )

# Wallet registration handler
def register(update: Update, context: CallbackContext) -> None:
    """Register a wallet address for the user."""
    if context.args:
        wallet_address = context.args[0]
        register_wallet(update.message.from_user.id, wallet_address)
        update.message.reply_text(f"✅ Wallet {wallet_address} successfully registered!")
    else:
        update.message.reply_text("❌ Please provide a wallet address. Usage: /register <wallet_address>")

# Wallet information handler
def wallet_info(update: Update, context: CallbackContext) -> None:
    """Retrieve and display the user's registered wallet address."""
    wallet_address = get_user_wallet(update.message.from_user.id)
    if wallet_address:
        update.message.reply_text(f"💼 Your registered wallet address is: {wallet_address}")
    else:
        update.message.reply_text("❌ No wallet address registered. Please register one using /register <wallet_address>.")

# Buy order handler
def buy_order(update: Update, context: CallbackContext) -> None:
    """Place a buy order for a specified token."""
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
    """Place a sell order for a specified token."""
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

# Limit order handler
def limit_order(update: Update, context: CallbackContext) -> None:
    """Place a limit order for a specified token."""
    if len(context.args) == 3:
        try:
            token = context.args[0]
            amount = float(context.args[1])
            price = float(context.args[2])
            # Here you would implement the logic for placing a limit order.
            update.message.reply_text(f"🔒 Placing a limit order for {amount} of {token} at ${price}.")
        except ValueError:
            update.message.reply_text("❌ Invalid amount or price. Please ensure they are numbers.")
    else:
        update.message.reply_text("❌ Incorrect usage. Usage: /limit <token> <amount> <price>")

# Dollar-Cost Averaging (DCA) handler
def dca(update: Update, context: CallbackContext) -> None:
    """Set up Dollar-Cost Averaging for a specified token."""
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

# Copy trading handler
def copy_trade_handler(update: Update, context: CallbackContext) -> None:
    """Copy trade a specified Solana wallet."""
    if context.args:
        solana_wallet = context.args[0]
        # Here you would implement the logic for copy trading.
        copy_trade(update, solana_wallet)
        update.message.reply_text(f"🔄 Started copy trading for Solana wallet: {solana_wallet}.")
    else:
        update.message.reply_text("❌ Please provide a Solana wallet address. Usage: /copytrade <solana_wallet>")

# ETH-SOL bridge handler
def swap_eth_sol(update: Update, context: CallbackContext) -> None:
    """Swap tokens between Ethereum and Solana."""
    # Implement swapping logic here
    update.message.reply_text("🔗 Initiating swap between Ethereum and Solana...")

def swap_sol_eth(update: Update, context: CallbackContext) -> None:
    """Swap tokens between Solana and Ethereum."""
    # Implement swapping logic here
    update.message.reply_text("🔗 Initiating swap between Solana and Ethereum...")

# Pump.fun trading handler
def pump_trade(update: Update, context: CallbackContext) -> None:
    """Trade Pump.fun tokens using a contract address."""
    if context.args:
        contract_address = context.args[0]
        trade_pump_fun_token(update, contract_address)
        update.message.reply_text(f"🎉 Trading Pump.fun token at contract address: {contract_address}.")
    else:
        update.message.reply_text("❌ Please provide a Pump.fun contract address. Usage: /pumptrade <contract_address>")

# Help command handler
def help_command(update: Update, context: CallbackContext) -> None:
    """Send help information to the user."""
    update.message.reply_text(
        "Here’s a list of commands you can use:\n"
        "• /start - Welcome message and command list\n"
        "• /register <wallet_address> - Register your wallet\n"
        "• /buy <token> <amount> <price> - Place a buy order\n"
        "• /sell <token> <amount> <price> - Place a sell order\n"
        "• /limit <token> <amount> <price> - Place a limit order\n"
        "• /dca <token> <amount> <interval> - Set up Dollar-Cost Averaging (DCA)\n"
        "• /copytrade <solana_wallet> - Copy trade a Solana wallet\n"
        "• /swapethsol - Swap tokens between Ethereum and Solana\n"
        "• /pumptrade <contract_address> - Trade Pump.fun tokens\n"
        "• /wallet - Check your registered wallet address\n"
        "• /help - Show this help message again."
    )

# Adding command handlers for additional functionalities
def setup_handlers(dispatcher):
    """Set up command handlers for the bot."""
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("register", register))
    dispatcher.add_handler(CommandHandler("wallet", wallet_info))
    dispatcher.add_handler(CommandHandler("buy", buy_order))
    dispatcher.add_handler(CommandHandler("sell", sell_order))
    dispatcher.add_handler(CommandHandler("limit", limit_order))
    dispatcher.add_handler(CommandHandler("dca", dca))
    dispatcher.add_handler(CommandHandler("copytrade", copy_trade_handler))
    dispatcher.add_handler(CommandHandler("swapethsol", swap_eth_sol))
    dispatcher.add_handler(CommandHandler("swapsoleth", swap_sol_eth))
    dispatcher.add_handler(CommandHandler("pumptrade", pump_trade))
    dispatcher.add_handler(CommandHandler("help", help_command))
    
