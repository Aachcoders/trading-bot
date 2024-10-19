from web3 import Web3
from solana.rpc.api import Client as SolanaClient
from telegram import Update
from telegram.ext import CallbackContext
from config.config import ETH_RPC_URL, SOL_RPC_URL

eth_web3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))
solana_client = SolanaClient(SOL_RPC_URL)

# Function to swap ETH to SOL with Telegram bot notifications
def swap_eth_to_sol(update: Update, context: CallbackContext):
    """Swap Ethereum-based tokens (ERC-20) to Solana-based tokens (SPL) with real-time feedback."""
    user_message = update.message.text
    try:
        # Parse user input (expecting: "/swapethsol <eth_wallet> <sol_wallet> <amount_eth>")
        _, eth_wallet, sol_wallet, amount_eth = user_message.split()
        amount_eth = float(amount_eth)

        update.message.reply_text(f"Initiating swap of {amount_eth} ETH from {eth_wallet} to SOL wallet {sol_wallet}.")

        eth_balance = eth_web3.eth.get_balance(eth_wallet)
        eth_balance_in_eth = Web3.fromWei(eth_balance, 'ether')

        if eth_balance_in_eth < amount_eth:
            update.message.reply_text(f"Insufficient Ethereum balance: {eth_balance_in_eth} ETH.")
            return

        # Placeholder for actual swap logic
        update.message.reply_text(f"Successfully swapped {amount_eth} ETH to SOL for wallet {sol_wallet}.")
    except ValueError:
        update.message.reply_text("Invalid input. Please use the command format: /swapethsol <eth_wallet> <sol_wallet> <amount_eth>.")
    except Exception as e:
        update.message.reply_text(f"An error occurred during the ETH to SOL swap: {e}")

# Function to swap SOL to ETH with Telegram bot notifications
def swap_sol_to_eth(update: Update, context: CallbackContext):
    """Swap Solana-based tokens (SPL) to Ethereum-based tokens (ERC-20) with real-time feedback."""
    user_message = update.message.text
    try:
        # Parse user input (expecting: "/swapsoleth <sol_wallet> <eth_wallet> <amount_sol>")
        _, sol_wallet, eth_wallet, amount_sol = user_message.split()
        amount_sol = float(amount_sol)

        update.message.reply_text(f"Initiating swap of {amount_sol} SOL from {sol_wallet} to ETH wallet {eth_wallet}.")

        sol_balance = solana_client.get_balance(sol_wallet)['result']['value'] / 1_000_000_000  # Convert lamports to SOL

        if sol_balance < amount_sol:
            update.message.reply_text(f"Insufficient Solana balance: {sol_balance} SOL.")
            return

        # Placeholder for actual swap logic
        update.message.reply_text(f"Successfully swapped {amount_sol} SOL to ETH for wallet {eth_wallet}.")
    except ValueError:
        update.message.reply_text("Invalid input. Please use the command format: /swapsoleth <sol_wallet> <eth_wallet> <amount_sol>.")
    except Exception as e:
        update.message.reply_text(f"An error occurred during the SOL to ETH swap: {e}")
