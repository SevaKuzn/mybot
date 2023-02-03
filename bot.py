import telebot
import random

answers = ['Да', 'Нет', 'Не знаю', 'Лучше даже не думай об этом', 'Конечно', 'Не скажу','Возможно' ]

bot = telebot.TeleBot('6048432384:AAHveB2iuqoG5OsUcb3BqOnWPbRJ95aMXIQ')

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я твой бот, задай мне вопросы, и на них отвечу. Напиши /help, чтобы узнать мои команды')

@bot.message_handler(commands=["help","h"])
def help(message):
    bot.send_message(message.chat.id,'Мои команды: /start, /help, /creator')

@bot.message_handler(commands=["creator","owner"])
def creator(message):
    bot.send_message(message.chat.id,'Мой создатель-Сева Кузнецов')

@bot.message_handler(content_types=['text'])
def answer(message):
    text = message.text
    if "?" in text:
        bot.send_message(message.chat.id, f"Мой ответ: {random.choice(answers)}")
    else:
        bot.send_message(message.chat.id, f"Ты отправил(a) сообщение: '{text}'")

bot.polling(none_stop=True, interval=0)