# bot/market_data.py
import requests
from config.config import COINGECKO_API_URL

def get_token_price(token_symbol: str) -> float:
    url = COINGECKO_API_URL.format(token_symbol)
    try:
        response = requests.get(url)
        data = response.json()
        return data[token_symbol]['usd']
    except (KeyError, ValueError, requests.RequestException) as e:
        return 0.0  # Return 0 if there's an error
