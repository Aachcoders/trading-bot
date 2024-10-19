import requests
from telegram import Update

PUMP_FUN_API = "https://pump.fun/api/token/"

def fetch_pump_fun_token(contract_address):
    """
    Fetch token data from pump.fun using the contract address.
    
    :param contract_address: The token's contract address.
    :return: The token data as a dictionary if successful, otherwise None.
    """
    try:
        response = requests.get(f"{PUMP_FUN_API}{contract_address}")
        response.raise_for_status()  # Ensure any HTTP errors are caught
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")
    return None

def trade_pump_fun_token(update: Update, contract_address: str, amount: float, action: str) -> None:
    """
    Handle trading of Pump.fun tokens using the specified contract address.
    
    :param update: Telegram update object to send messages.
    :param contract_address: The contract address of the token.
    :param amount: The number of tokens to trade.
    :param action: The type of trade action ('buy' or 'sell').
    """
    token = fetch_pump_fun_token(contract_address)
    
    if token:
        token_name = token.get('name', 'Unknown Token')
        if action == "buy":
            update.message.reply_text(f"Initiating purchase of {amount} {token_name} tokens.")
        elif action == "sell":
            update.message.reply_text(f"Initiating sale of {amount} {token_name} tokens.")
        else:
            update.message.reply_text("Invalid action specified. Use 'buy' or 'sell'.")
    else:
        update.message.reply_text(f"Could not fetch data for the token with contract address {contract_address}. Please check the address and try again.")
