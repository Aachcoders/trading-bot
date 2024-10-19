import schedule
import time
import threading
from .market_data import get_token_price
from .transaction import execute_buy
from .database import get_user_wallet

def perform_dca_trade(wallet_address: str, token: str, amount: float):
    """Perform the DCA trade by executing a buy order."""
    price = get_token_price(token)
    if price > 0:
        execute_buy(wallet_address, token, amount, price)
        print(f"DCA: Bought {amount} {token} for {wallet_address} at price ${price}")
    else:
        print(f"DCA: Failed to retrieve the price for {token}. No trade executed.")

def dca_scheduler(wallet_address: str, token: str, amount: float, interval: int) -> None:
    """
    Schedule DCA trades at specified intervals.

    :param wallet_address: The user's wallet address.
    :param token: The token to buy.
    :param amount: The amount to invest in each DCA order.
    :param interval: The time interval (in minutes) for DCA trades.
    """
    schedule.every(interval).minutes.do(lambda: perform_dca_trade(wallet_address, token, amount))

    while True:
        schedule.run_pending()
        time.sleep(1)  # Sleep to prevent high CPU usage

def start_dca(update, token, amount, interval):
    """
    Start the DCA process.

    :param update: Telegram update object to send messages.
    :param token: The token to buy.
    :param amount: The amount to invest in each DCA order.
    :param interval: The time interval (in minutes) for DCA trades.
    """
    wallet_address = get_user_wallet(update.message.from_user.id)
    if not wallet_address:
        update.message.reply_text("Please register your wallet using /register before starting DCA.")
        return

    threading.Thread(target=dca_scheduler, args=(wallet_address, token, amount, interval)).start()
    update.message.reply_text(f"Started DCA for {amount} {token} every {interval} minutes.")
    
