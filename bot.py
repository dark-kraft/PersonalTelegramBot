import os
import telebot

bot: telebot.TeleBot = telebot.TeleBot(token=os.environ.get('BOT_TOKEN'))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Hi ma friend')


bot.polling()
