import requests
from config.config import COINGECKO_API_URL

def get_token_price(token_symbol: str) -> float:
    """
    Fetch the latest token price in USD from the CoinGecko API.
    
    :param token_symbol: The symbol of the token (e.g., BTC, ETH).
    :return: The token price in USD as a float, or 0.0 if there's an error.
    """
    url = COINGECKO_API_URL.format(token_symbol.lower())
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure we catch HTTP errors
        data = response.json()
        price = data[token_symbol]['usd']
        
        # Return the price if everything is correct
        return price

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred while fetching {token_symbol} price: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout occurred: {timeout_err}")
    except KeyError as key_err:
        print(f"Invalid response format: {key_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    
    # Return 0 if any error occurs
    return 0.0
    
