import telebot
from config import api_key

bot = telebot.TeleBot(api_key)


def say(username, messageText):
    mark = telebot.types.ReplyKeyboardMarkup(True)
    mark.row("спасибо")
    bot.send_message(username, messageText, reply_markup=mark)


if __name__ == '__main__':
    bot.polling(none_stop=True)
