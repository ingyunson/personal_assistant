import telegram
import yahoo_news_jp

my_token = '711334098:AAHhNP3Hondc76pJcbOlNXPtJ2f0HlYYVBk'
chatbot = telegram.Bot(token=my_token)
chat_id = chatbot.getUpdates()[-1].message.chat.id
text1 = yahoo_news_jp.headline_title
text2 = yahoo_news_jp.headline_url
print(text1)
print(text2)

chatbot.sendMessage(chat_id=chat_id, text=text2)