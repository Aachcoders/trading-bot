# bot/scheduler.py
import schedule
import time
import threading

from .market_data import get_token_price
from .transaction import execute_buy

def dca_scheduler(wallet_address: str, token: str, amount: float, interval: int) -> None:
    def perform_dca_trade():
        price = get_token_price(token)
        execute_buy(wallet_address, token, amount, price)
        print(f"DCA: Bought {amount} {token} for {wallet_address} at price ${price}")
    
    schedule.every(interval).minutes.do(perform_dca_trade)

    while True:
        schedule.run_pending()
        time.sleep(1)  # Sleep to prevent high CPU usage

def start_dca(update, token, amount, interval):
    wallet_address = get_user_wallet(update.message.from_user.id)
    if not wallet_address:
        update.message.reply_text("Please register your wallet using /register before starting DCA.")
        return

    threading.Thread(target=dca_scheduler, args=(wallet_address, token, amount, interval)).start()
    update.message.reply_text(f"Started DCA for {amount} {token} every {interval} minutes.")
