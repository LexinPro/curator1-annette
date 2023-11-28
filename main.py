import telebot

bot = telebot.TeleBot('6834887698:AAFoNvLS3XazERnp5dkIZeLattpTeI97LcM')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, text='Сообщение')

@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, text='Беги.\nБЕГИ')

bot.infinity_polling()
