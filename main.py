from telebot import TeleBot
from telebot import custom_filters
from telebot import types
from telebot.types import Message

import config
from states import States

bot = TeleBot(config.token)
min_name_length = 4
max_name_length = 12


@bot.message_handler(commands=['start'])
def greeting(message: Message):
    bot.send_message(message.chat.id, "Hi! It seems that you are new here!\n"
                                      "So,let's firstly introduce your self.\n"
                                      "How I can call you?")
    bot.set_state(message.from_user.id, States.enter_name)


@bot.message_handler(state=States.enter_name)
def enter_name(message: Message):
    name = message.text

    if len(name) < min_name_length or len(name) > max_name_length:
        bot.send_message(message.chat.id, "I'm sorry, we're a simple people and I don't think we can remember too "
                                          "short or long a name. I think from 4 to 12 letters will be okay.\n"
                                          "How again we can call you?")
        bot.set_state(message.from_user.id, States.enter_name)
    else:
        bot.send_message(message.chat.id, "Oh! Such a good name!\n"
                                          f"Nice to meet you {name}!")


def main():
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()


if __name__ == '__main__':
    main()
