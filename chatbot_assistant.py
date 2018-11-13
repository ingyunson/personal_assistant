import telegram

my_token = '711334098:AAHhNP3Hondc76pJcbOlNXPtJ2f0HlYYVBk'
chatbot = telegram.Bot(token=my_token)
chat_id = chatbot.getUpdates()[-1].message.chat.id

chatbot.sendMessage(chat_id=chat_id, text='Type your message')