# config/config.py
import os

# Load Ethereum and Solana RPC URLs from environment variables
ETH_RPC_URL = os.getenv('ETH_RPC_URL', 'https://mainnet.infura.io/v3/6c6e59a690c04e6f868c4d36fff4a1bb')
SOL_RPC_URL = os.getenv('SOL_RPC_URL', 'https://api.mainnet-beta.solana.com')

TELEGRAM_BOT_TOKEN = '7432436789:AAG9DXdWe4kPDdM3W3S7dcQYa_VoCf7AYvo'
COINGECKO_API_URL = 'https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd'
