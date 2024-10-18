# bot/transaction.py
from .market_data import get_token_price

def buy(update, token, amount, price):
    current_price = get_token_price(token)
    if current_price > price:
        update.message.reply_text(f"Buy order placed: {amount} {token} at ${price} each.")
        # Here you'd execute the transaction with the user's wallet
    else:
        update.message.reply_text(f"Current price ${current_price} is higher than your buy price.")

def sell(update, token, amount, price):
    current_price = get_token_price(token)
    if current_price < price:
        update.message.reply_text(f"Sell order placed: {amount} {token} at ${price} each.")
        # Here you'd execute the transaction with the user's wallet
    else:
        update.message.reply_text(f"Current price ${current_price} is lower than your sell price.")

def execute_buy(wallet_address, token, amount, price):
    update.message.reply_text(f"Buying {amount} {token} for wallet {wallet_address} at ${price} each.")
