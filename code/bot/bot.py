# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------

# Начинка бота

# ----------------------------------------------------------------------------------------------------------------------

import os
import random
import telebot
import webbrowser

from code.API import postgresql as ps
from code.different import config

bot = telebot.TeleBot(config.TOKEN)

if os.path.exists('../../logs'):
    pass
else:
    os.mkdir('../../logs')

print('234')


def stickers(name=None):
    # СЮДА, ЧЕРЕЗ ЗАПЯТУЮ, ДОБАВЛЯЙ СТИКЕРЫ, НО ТОЛЬКО, СНАЧАЛА ДОБАВЬ ИХ В ПАПКУ С ПРОЕКТОМ!!!!
    # ------------------------------------------------------------------------------------------------------------------
    list_name_sticker = ['data/stickers/sticker_patriarch_1.webp', 'data/stickers/sticker_patriarch_2.webp',
                         'data/stickers/sticker_putin_1.webp', 'data/stickers/sticker_putin_2.webp']
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
    # bot.send_sticker(message.chat.id, stickers())
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\n"
                                      "Я - <b>{1.first_name}</b>, и я - добряк!"
                     .format(message.from_user, bot.get_me()), parse_mode='html')


@bot.message_handler(content_types=['text'])
def speak(message):
    text = str(message.text).lower()

    def db_output(name_table):
        list_smile = ['😂', '👋', '🤓', '😎', '😀', '😁']

        for i in range(1, ps.inquiry_to_db(
                """SELECT COUNT (id_) from public.{} having COUNT (id_) > 0;""".format(name_table),
                flag=True)[0]):

            print(text)
            print(str(ps.inquiry_to_db(
                """SELECT examples FROM {} WHERE id_ = {};""".format(name_table, i),
                flag=True)).rstrip().lower()[2:-3])

            if str(ps.inquiry_to_db(
                    """SELECT examples FROM {} WHERE id_ = {};""".format(name_table, i),
                    flag=True)).rstrip().lower()[2:-3] in text:

                random_smile = ''
                if not random.randint(0, 3):
                    random_smile = random.choice(list_smile)

                print_to_chat(str(ps.inquiry_to_db(
                    """SELECT responses FROM {} ORDER BY random() LIMIT 1;""".format(name_table),
                    flag=True))[2:-3] + random_smile)

                return True

    def print_to_chat(output, type_out='t'):
        if type_out != 't' and type_out != 's':
            print('Error: [incorrect argument! Try "s" or "t".]')
            bot.send_message(message.chat.id, 'Error: [incorrect argument! Try "s" or "t".]')
        else:
            if type_out == 't':
                bot.send_message(message.chat.id, output)
            elif type_out == 's':
                bot.send_sticker(message.chat.id, output)

        # print('USER_NAME[ ' + str(message.from_user) + '] = ' + str(message.text) + '\n\t' +
        #       'BOT[ ' + str(bot.get_me()) + '] = ' + str(output) + '\n',
        #       file=open(r'logs/message_{0.first_name}_log.txt'.format(message.from_user), 'a'))

    if message.chat.type == 'private':
        list_table = ['hello', 'how_do_you_do', 'bye']
        flag_default = False

        # print_to_chat()
        # webbrowser.open('https://yandex.ru/search/?text={}'.format(text.replace(' ', '_')), new=2)

        for i in list_table:
            if db_output(i):
                flag_default = False
                break
            else:
                flag_default = True

        if flag_default:
            list_smile = ['😂', '👋', '🤓', '😎', '😀', '😁']

            random_smile = ''
            if not random.randint(0, 3):
                random_smile = random.choice(list_smile)

            print_to_chat(str(ps.inquiry_to_db(
                """SELECT responses FROM default_ ORDER BY random() LIMIT 1;""".format(),
                flag=True))[2:-3] + random_smile)


# postgresql.inquiry_to_db("INSERT INTO public.ai (id, id_message, dialogs) values (0002, 02, '😎');")
# RUN BOT
bot.polling(none_stop=True)
