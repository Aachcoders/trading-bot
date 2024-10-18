# bot/pump_fun.py
import requests

PUMP_FUN_API = "https://pump.fun/api/token/"

def fetch_pump_fun_token(contract_address):
    """Fetch token data from pump.fun using contract address."""
    response = requests.get(f"{PUMP_FUN_API}{contract_address}")
    if response.status_code == 200:
        token_data = response.json()
        return token_data
    else:
        return None

def trade_pump_fun_token(update, contract_address, amount, action):
    """Trade Pump.fun token by contract address."""
    token = fetch_pump_fun_token(contract_address)
    if token:
        token_name = token['name']
        if action == "buy":
            update.message.reply_text(f"Buying {amount} {token_name} tokens.")
        elif action == "sell":
            update.message.reply_text(f"Selling {amount} {token_name} tokens.")
    else:
        update.message.reply_text("Invalid contract address for Pump.fun token.")
