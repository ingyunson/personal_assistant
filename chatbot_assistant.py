import telegram
from telegram.ext import Updater, MessageHandler, Filters
import yahoo_news_jp
from google_search import search

my_token = '711334098:AAHhNP3Hondc76pJcbOlNXPtJ2f0HlYYVBk'
chatbot = telegram.Bot(token=my_token)
chat_id = chatbot.getUpdates()[-1].message.chat.id
text1 = yahoo_news_jp.headline_title
text2 = yahoo_news_jp.headline_url
print(text1)
print(text2)

chatbot.sendMessage(chat_id=chat_id, text=text2)

print('start')

def get_message(bot, update) :
    update.message.reply_text("got text")
    word = update.message.text
    text = search(word)
    update.message.reply_text(text)

updater = Updater(my_token)

message_handler = MessageHandler(Filters.text, get_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()

