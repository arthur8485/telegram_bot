import configparser
import logging
import telebot
import telegram
from flask import Flask, request
from telegram.ext import *
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import function1
# Load data from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Initial Flask app
app = Flask(__name__)

# Initial bot by Telegram access token
bot = telegram.Bot(token=(config['TELEGRAM']['ACCESS_TOKEN']))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
    return 'ok'

# New a dispatcher for bot
dispatcher = Dispatcher(bot, None)

# 當你對你的機器人說'/url'，就會執行這串
dispatcher.add_handler(CommandHandler('url', function1.getUrl))
# 當你對你的機器人說'/today'，就會執行這串
dispatcher.add_handler(CommandHandler('today', function1.clickButton))
# 當使用者點擊了 clickButton時，會獲取到 callback_data 這時會執行下方的指令，針對callback_data的參數值回應對應的訊息
dispatcher.add_handler(CallbackQueryHandler(function1.getClickButtonData))

if __name__ == "__main__":
    # Running server
    app.run(port=80,debug=True)


#telegram webhook setup steps:



#	1. fill in your token and webhook in 'config,ini'
	
#	2. If testing your BOT in ngrok ,fill in the same port in main.py
	
#	3, Changing the port in main.py and put ur port in the end
		

#		if __name__ == "__main__":

#		    app.run(port= *** YOUR PORT ***,debug=True)

#   4. Run main.py (pipenv run main.py)

#	5. setting your webhook (don't forget to put "/hook" in the end):

#		https://api.telegram.org/bot{TOKEN_HERE}/setWebhook?url={ngrok_URL}/hook

#		https://api.telegram.org/bot960949087:AAF_bb_FdEXxH1OuJd0PL_KJLzWPEY1UIek/setWebhook?url={ngrok_URL}/hook

	
#	  And you will got these info. on the website.
#	{
#		ok: true,
#		result: true,
#		description: "Webhook was set"
#	}

#DONE!