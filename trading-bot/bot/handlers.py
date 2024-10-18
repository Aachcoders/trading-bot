# bot/handlers.py
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler

from .transaction import buy, sell
from .database import register_wallet, get_user_wallet
from .scheduler import start_dca

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome to Trojan Trading Bot! Type /help for available commands.")

def register(update: Update, context: CallbackContext) -> None:
    wallet_address = context.args[0]
    register_wallet(update.message.from_user.id, wallet_address)
    update.message.reply_text(f"Wallet {wallet_address} successfully registered!")

def buy_order(update: Update, context: CallbackContext) -> None:
    token = context.args[0]
    amount = float(context.args[1])
    price = float(context.args[2])
    buy(update, token, amount, price)

def sell_order(update: Update, context: CallbackContext) -> None:
    token = context.args[0]
    amount = float(context.args[1])
    price = float(context.args[2])
    sell(update, token, amount, price)

def dca(update: Update, context: CallbackContext) -> None:
    token = context.args[0]
    amount = float(context.args[1])
    interval = int(context.args[2])
    start_dca(update, token, amount, interval)
