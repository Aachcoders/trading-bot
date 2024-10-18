# main.py
from telegram.ext import Updater, CommandHandler
from bot.handlers import start, register, buy_order, sell_order, dca
from bot.utils import error
from bot.database import init_db
from bot.copy_trading import copy_trade
from bot.eth_sol_bridge import swap_eth_to_sol, swap_sol_to_eth
from bot.pump_fun import trade_pump_fun_token

def main():
    updater = Updater('432436789:AAG9DXdWe4kPDdM3W3S7dcQYa_VoCf7AYvo')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("register", register))
    dp.add_handler(CommandHandler("buy", buy_order))
    dp.add_handler(CommandHandler("sell", sell_order))
    dp.add_handler(CommandHandler("dca", dca))
    dp.add_handler(CommandHandler("copytrade", copy_trade))
    dp.add_handler(CommandHandler("swapethsol", swap_eth_to_sol))
    dp.add_handler(CommandHandler("swapsoleth", swap_sol_to_eth))
    dp.add_handler(CommandHandler("pumptrade", trade_pump_fun_token))

    dp.add_error_handler(error)

    init_db()

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
