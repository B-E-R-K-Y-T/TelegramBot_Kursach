# This file is my file(BERKYT)


import os
import random
import telebot

from code.API import postgresql as ps
from code.different import config

bot = telebot.TeleBot(config.TOKEN)

BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': ['Привет!', 'Салам!'],
            'responses': ['Привет!', 'Салам!']
        },
        'bye': {
            'examples': ['Пока!', 'Удачи, бро!'],
            'responses': ['Пока!', 'Удачи, бро!']
        }
    },
    'failure_phrases': [
        'Я ничего не понял!',
        'Что-то непонятно.'
    ]
}

if os.path.exists('../../logs'):
    pass
else:
    os.mkdir('../../logs')


def stickers(name=None):
    # СЮДА, ЧЕРЕЗ ЗАПЯТУЮ, ДОБАВЛЯЙ СТИКЕРЫ, НО ТОЛЬКО, СНАЧАЛА ДОБАВЬ ИХ В ПАПКУ С ПРОЕКТОМ!!!!
    # ------------------------------------------------------------------------------------------------------------------
    list_name_sticker = ['sticker_patriarch_1.webp', 'sticker_patriarch_2.webp',
                         'sticker_putin_1.webp', 'sticker_putin_2.webp']
    # ------------------------------------------------------------------------------------------------------------------
    if len(list_name_sticker) == 0:
        print('Error: [The list is empty!]')
        return open('../../error.webp', 'rb')

    list_file_sticker = []
    for i in range(len(list_name_sticker)):
        try:
            list_file_sticker.append(open(list_name_sticker[i], 'rb'))
        except Exception as e:
            print('Error: [incorrect name file of sticker in "list_name_sticker"! \n\t '
                  'INCORRECT NAME: {0} INDEX: {1} {2}]'.format(list_name_sticker[i], i, e))
            continue

    if name is not None:
        index_sticker = None
        for i in range(len(list_name_sticker)):
            if name == list_name_sticker[i]:
                index_sticker = i
                break
        try:
            return list_file_sticker[index_sticker]
        except Exception as e:
            print('Error: [incorrect sticker! {0}]'.format(e))
            return open('../../error.webp', 'rb')

    return list_file_sticker[random.randint(0, len(list_file_sticker) - 1)]


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_sticker(message.chat.id, stickers())
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\n"
                                      "Я - <b>{1.first_name}</b>, и я - русский!"
                     .format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def speak(message):
    text = str(message.text).lower()

    def print_to_chat(output, type_out='t'):
        if type_out != 't' and type_out != 's':
            print('Error: [incorrect argument! Try "s" or "t".]')
            bot.send_message(message.chat.id, 'Error: [incorrect argument! Try "s" or "t".]')
        else:
            if type_out == 't':
                bot.send_message(message.chat.id, output)
            elif type_out == 's':
                bot.send_sticker(message.chat.id, output)

    if message.chat.type == 'private':
        # if text in str(BOT_CONFIG['intents']['hello']['responses']).rstrip().lower():
        list_text = ['Привет!\n']

        for element in list_text:
            if text in str(ps.inquiry_to_db("""SELECT * FROM ai WHERE dialogs = '{}';""".format(element),
                                            flag=True)).rstrip().lower():
                print_to_chat(random.choice(BOT_CONFIG['intents']['hello']['responses']))
                break
            else:
                # print(ps.inquiry_to_db("""SELECT * FROM ai WHERE dialogs = 'Привет!\n';""", flag=True))
                print_to_chat(random.choice(BOT_CONFIG['failure_phrases']))
                break


# RUN BOT
# postgresql.inquiry_to_db("INSERT INTO public.ai (id, id_message, dialogs) values (0002, 02, '😎');")
bot.polling(none_stop=True)
