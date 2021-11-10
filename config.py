# This file is my file(BERKYT)


# Telegram-bot
# ----------------------------------------------------------------------------------------------------------------------

# TOKEN = '2073300120:AAGVjOVVUhLCK2e41L-gOTbLdcH3URq36Rk'  # bot token (Мой токен)
TOKEN = '2018372109:AAGvR5HUasGZPmrhxG6pAv_I7PXBBjmFTJ4'  # bot token (Токен Никиты)

# ----------------------------------------------------------------------------------------------------------------------

# PostgreSQL
# ----------------------------------------------------------------------------------------------------------------------

operating_mode = 'Tim'

host_ = ''
user_ = ''
password_ = ''
database_ = ''

if operating_mode == 'Tim':
    host_ = 'localhost'
    user_ = 'postgres'
    password_ = '1488'
    database_ = 'Telegram_Bot'
elif operating_mode == 'Pol':
    host_ = 'localhost'
    user_ = 'postgres'
    password_ = 'berkytsenpai'
    database_ = 'berkyt'
elif operating_mode == 'San':
    host_ = 'localhost'
    user_ = 'postgres'
    password_ = 'Alex5405'
    database_ = 'KURSACH'


host = host_
user = user_
password = password_
database = database_

# ----------------------------------------------------------------------------------------------------------------------
