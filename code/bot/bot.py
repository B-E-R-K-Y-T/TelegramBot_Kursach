# This file is my file(BERKYT)


import os
import random

# import apiai
# import json
import telebot

from code.different import config

bot = telebot.TeleBot(config.TOKEN)

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
    on = True
    off = False
    text = str(message.text).lower()

    def print_to_chat(output, type_out):
        if type_out != 't' and type_out != 's':
            print('Error: [incorrect argument! Try "s" or "t".]')
            bot.send_message(message.chat.id, 'Error: [incorrect argument! Try "s" or "t".]')
        else:
            if type_out == 't':
                bot.send_message(message.chat.id, output)
            elif type_out == 's':
                bot.send_sticker(message.chat.id, output)

            print('USER_NAME[ ' + str(message.from_user) + '] = ' + str(message.text) + '\n\t' +
                  'BOT[ ' + str(bot.get_me()) + '] = ' + str(output) + '\n',
                  file=open(r'logs/message_{0.first_name}_log.txt'.format(message.from_user), 'a'))

    # ПИСАТЬ КОД ТУТ:
    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------

    if message.chat.type == 'private':
        # Включить(on) или выключить(off) функционал бота, который написал я
        default_bot = off
        # Включить(on) или выключить(off) функционал бота, который написал ты
        custom_bot = on

        # ТУТ НУЖНО ПИСАТЬ СВОЙ ФУНКЦИОНАЛ
        # --------------------------------------------------------------------------------------------------------------
        if custom_bot:
            # Просто текст
            print_to_chat('Hello! It is custom functional.', 't')
            # Рандомный стикер
            print_to_chat(stickers(), 's')
            # Конкретный стикер
            print_to_chat(stickers('sticker_putin_1.webp'), 's')

            # ВОЗМОЖНЫЕ ОШИБКИ:
            # Ошибка аргумента
            print_to_chat('Привет, как дела?', 'СЮДА НЕЛЬЗЯ ПИСАТЬ НИЧЕГО, КРОМЕ "t" или "s"!!! Иначе, будет ошибка!')
            # Несуществующий стикер
            print_to_chat(stickers('НЕСУЩЕСТВУЮЩИЙ СТИКЕР.webp'), 's')
        # --------------------------------------------------------------------------------------------------------------

        # БАЗОВЫЙ ФУНКЦИОНАЛ, ЭТО ТЕБЕ ДЛЯ ПРИМЕРА
        # --------------------------------------------------------------------------------------------------------------
        if default_bot:
            # Если пользователь написал 'как дела?', то написать ему в ответ 'Хорошо!'
            if text == 'как дела?':
                print_to_chat('Хорошо!', 't')

            # Если пользователь не написал 'как дела?', но написал 'привет', то написать ему в ответ...
            elif text == 'привет' or text == '👋':

                # Все-таки пользователь написал привет. Вот мы и внутри оператора elif
                # внизу логика такая:
                # С вероятностью 50% бот ответит стикером, либо сообщением "Привет! 👋"
                # --------------------------------
                if random.randint(0, 1) == 0:
                    # Ответ случайным стикером
                    print_to_chat(stickers(), 's')
                else:
                    # Ответ "Привет!"
                    print_to_chat('Привет! 👋', 't')
                # --------------------------------

            # Если пользователь хоть как - то упоминает слово "стикер" но не напишет слово "привет" или "как дела?"
            # то мы кинем ему стикер
            elif 'стикер' in text:
                print_to_chat(stickers(), 's')

            # Если мы вообще не смогли угадать, что пользователь пишет, то пишем ему это:
            else:
                # Вот это пишем если быть точным:
                print_to_chat('Я не знаю что ответить, '
                              'так как разработчик не вложил '
                              'в меня такие знания 😢', 't')
        # --------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------------


# RUN BOT
# postgresql.inquiry_to_db("INSERT INTO public.ai (id, id_message, dialogs) values (0002, 02, '😎');")
bot.polling(none_stop=True)
