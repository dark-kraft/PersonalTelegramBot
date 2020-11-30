import datetime
import os
import datetime
import telebot
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


job_stores = {
    'default': SQLAlchemyJobStore(url=os.environ.get('DATABASE_URL'))
}

executors = {
    'default': ThreadPoolExecutor(10)
}

job_defaults = {
    'coalesce': False,
    'max_instances': 3
}

scheduler = BackgroundScheduler(jobstores=job_stores, executors=executors, job_defaults=job_defaults)
scheduler.start()

bot: telebot.TeleBot = telebot.TeleBot(token=os.environ.get('BOT_TOKEN'))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Hi ma friend')


@bot.message_handler(commands=['Mongo'])
def get_data_from_db_handler(message):
    bot.reply_to(message, 'Enter your word')


@bot.message_handler(commands=['time'])
def set_scheduled_job(message):
    msg = bot.send_message(message.chat.id, 'Введите время в секундах')
    bot.register_next_step_handler(msg, is_digit)


def is_digit(message):
    seconds = message.text
    if not seconds.isdigit():
        msg = bot.reply_to(message, 'Время в секундах я сказал')
        bot.register_next_step_handler(msg, is_digit)
        return
    current_time = datetime.datetime.now()
    run_time = current_time + datetime.timedelta(0, int(seconds))
    scheduler.add_job(test_job, 'date', run_date=run_time, args=[message.chat.id, seconds])


def test_job(chat_id, seconds):
    print('text')
    bot.send_message(chat_id, f'Ответ через {seconds} секунд')


while True:
    try:
        bot.polling()
    except:
        bot.polling()
