import logging

# Set up logging configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def log_message(update):
    """
    Log incoming Telegram messages for debugging or tracking.
    
    Args:
        update: Update object representing an incoming Telegram message.
    """
    user = update.message.from_user
    logger.info(f"Received message from {user.username} (ID: {user.id}): {update.message.text}")

def error(update, context):
    """
    Log any errors that occur during bot execution.
    
    Args:
        update: Update object representing an incoming Telegram update (can be None).
        context: Context object representing the current conversation context or state.
    """
    if update:
        user_id = update.message.from_user.id
        logger.error(f"An error occurred from User {user_id}: {context.error}")
    else:
        logger.error(f"An error occurred: {context.error} (No update info available)")

def log_order_action(user_id, token, amount, order_type):
    """
    Log the details of an order action.
    
    Args:
        user_id: The Telegram user ID placing the order.
        token: The token symbol being traded (e.g., BTC, ETH).
        amount: The amount of the token being traded.
        order_type: Type of order (buy, sell, limit, DCA, etc.).
    """
    logger.info(f"Order placed by User {user_id}: {order_type} {amount} {token}")

def validate_user_input(input_text):
    """
    Validate user input to ensure it follows expected formats or conditions.
    
    Args:
        input_text: The text input from the user.

    Returns:
        bool: True if the input is valid, False otherwise.
    """
    if not input_text or not input_text.strip():
        return False
    # Additional validation can be added here (e.g., regex for price or amount)
    return True

def rate_limit_message(update):
    """
    Send a message to the user informing them they've hit the rate limit.
    
    Args:
        update: Update object representing the Telegram message.
    """
    update.message.reply_text("You are sending messages too quickly. Please wait a moment before trying again.")

def success_message(update, message):
    """
    Send a success message to the user after a successful operation.

    Args:
        update: Update object representing the Telegram message.
        message: Custom success message to send.
    """
    update.message.reply_text(f"✅ Success! {message}")

def validate_amount(amount):
    """
    Validate if the provided amount is a positive number.
    
    Args:
        amount: The amount to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        return float(amount) > 0
    except ValueError:
        return False

def validate_price(price):
    """
    Validate if the provided price is a positive number.
    
    Args:
        price: The price to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        return float(price) > 0
    except ValueError:
        return False
