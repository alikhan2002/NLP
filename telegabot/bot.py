import telebot

bot = telebot.TeleBot('6834068007:AAHWfpolYhtnxfthgQjPfUjtLxCBPmt2Bq0')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет!')

bot.polling(none_stop=True)