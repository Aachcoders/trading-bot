from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from bot.handlers import start, register, buy_order, sell_order, dca
from bot.utils import error
from bot.database import init_db
from bot.copy_trading import copy_trade
from bot.eth_sol_bridge import swap_eth_to_sol, swap_sol_to_eth
from bot.pump_fun import trade_pump_fun_token

# Main menu
def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Register", callback_data='register')],
        [InlineKeyboardButton("Buy Order", callback_data='buy')],
        [InlineKeyboardButton("Sell Order", callback_data='sell')],
        [InlineKeyboardButton("DCA Order", callback_data='dca')],
        [InlineKeyboardButton("Copy Trade", callback_data='copytrade')],
        [InlineKeyboardButton("Swap ETH to SOL", callback_data='swapethsol')],
        [InlineKeyboardButton("Swap SOL to ETH", callback_data='swapsoleth')],
        [InlineKeyboardButton("Pump Token Trade", callback_data='pumptrade')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to Trojan Trading Bot! Please select an option:', reply_markup=reply_markup)

# Handle button clicks
def button(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'register':
        register(update, context)
    elif query.data == 'buy':
        buy_order(update, context)
    elif query.data == 'sell':
        sell_order(update, context)
    elif query.data == 'dca':
        dca(update, context)
    elif query.data == 'copytrade':
        copy_trade(update, context)
    elif query.data == 'swapethsol':
        swap_eth_to_sol(update, context)
    elif query.data == 'swapsoleth':
        swap_sol_to_eth(update, context)
    elif query.data == 'pumptrade':
        trade_pump_fun_token(update, context)

def main():
    updater = Updater('YOUR_BOT_TOKEN')
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_error_handler(error)

    init_db()

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
    
