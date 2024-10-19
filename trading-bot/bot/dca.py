from .market_data import get_token_price
from telegram import Update
from telegram.ext import CallbackContext
import time

# Function to calculate the amount per interval for DCA orders
def calculate_dca(total_investment, intervals):
    """Calculate the investment per interval for DCA orders."""
    return total_investment / intervals

# Function to execute DCA orders and provide real-time feedback via the Telegram bot
def dca_order(update: Update, context: CallbackContext):
    """Execute Dollar-Cost Averaging (DCA) orders."""
    user_message = update.message.text
    try:
        # Parse user input (expecting: "/dca <wallet_address> <token> <amount> <intervals>")
        _, wallet_address, token, amount, intervals = user_message.split()
        amount = float(amount)
        intervals = int(intervals)

        dca_amount = calculate_dca(amount, intervals)

        update.message.reply_text(f"Initiating DCA for {amount} across {intervals} intervals. Buying {dca_amount} per interval.")

        for interval in range(1, intervals + 1):
            current_price = get_token_price(token)
            
            # Execute buy at the calculated DCA amount (replace with actual trading logic)
            update.message.reply_text(f"Interval {interval}/{intervals}: Buying {dca_amount} of {token} at price ${current_price} for wallet {wallet_address}")
            
            # Simulate waiting time between DCA intervals (for demonstration purposes)
            time.sleep(2)  # Adjust to actual interval timing in production

        update.message.reply_text(f"DCA completed for {amount} of {token} across {intervals} intervals.")

    except ValueError:
        update.message.reply_text("Invalid input. Please use the command format: /dca <wallet_address> <token> <amount> <intervals>.")
    except Exception as e:
        update.message.reply_text(f"An error occurred while executing the DCA order: {e}")
