# bot/eth_sol_bridge.py
from web3 import Web3
from solana.rpc.api import Client as SolanaClient

from config.config import ETH_RPC_URL, SOL_RPC_URL

eth_web3 = Web3(Web3.HTTPProvider(ETH_RPC_URL))
solana_client = SolanaClient(SOL_RPC_URL)

def swap_eth_to_sol(eth_wallet, sol_wallet, amount_eth):
    """Swap Ethereum-based tokens (ERC-20) to Solana-based tokens (SPL)."""
    # Fetch ETH balance and swap logic (implement actual bridge logic with APIs)
    eth_balance = eth_web3.eth.get_balance(eth_wallet)
    if eth_balance < amount_eth:
        return "Insufficient Ethereum balance"
    
    # Assuming a swap was successful
    return f"Swapped {amount_eth} ETH to SOL for wallet {sol_wallet}"

def swap_sol_to_eth(sol_wallet, eth_wallet, amount_sol):
    """Swap Solana-based tokens (SPL) to Ethereum-based tokens (ERC-20)."""
    sol_balance = solana_client.get_balance(sol_wallet)['result']['value']
    if sol_balance < amount_sol:
        return "Insufficient Solana balance"
    
    # Assuming a swap was successful
    return f"Swapped {amount_sol} SOL to ETH for wallet {eth_wallet}"
