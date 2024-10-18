# bot/dca.py
from .market_data import get_token_price

def calculate_dca(total_investment, intervals):
    """Calculate the investment per interval for DCA orders."""
    return total_investment / intervals

def dca_order(wallet_address, token, amount, intervals):
    """Execute Dollar-Cost Averaging (DCA) orders."""
    dca_amount = calculate_dca(amount, intervals)
    for interval in range(intervals):
        current_price = get_token_price(token)
        # Execute buy at the calculated DCA amount
        print(f"DCA Order: Buying {dca_amount} of {token} at price ${current_price} for wallet {wallet_address}")
        # Assume trade is executed for now, extend with transaction logic
