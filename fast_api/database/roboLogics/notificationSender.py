import telebot
from . import config


def say(username, messageText):
    bot = telebot.TeleBot(config.api_key)
    mark = telebot.types.ReplyKeyboardMarkup(True)
    mark.row("спасибо")
    bot.send_message(username, messageText, reply_markup=mark)


if __name__ == '__main__':
    bot = telebot.TeleBot(config.api_key)
    bot.polling(none_stop=True)
