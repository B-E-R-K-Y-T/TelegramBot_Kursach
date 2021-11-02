# This file is my file(BERKYT)

# ----------------------------------------------------------------------------------------------------------------------

# API для работы с PostgreSQL

# ----------------------------------------------------------------------------------------------------------------------

import psycopg2
from config import host, user, password, database

connection = None

try:
    assert isinstance(database, object)
    connection = psycopg2.connect(
        database=database,
        user=user,
        password=password,
        host=host
    )
except Exception as e:
    print('ERROR[open_db]: {}'.format(e))


# Закрывает БД
def close_db():

    """
    :return:
        Ничего не возвращает.
    """

    try:
        connection.close()
    except Exception as e:
        print('ERROR[close_db]: {}'.format(e))


# Принимает SQL-запрос и выполняет его
def inquiry_to_db(inquiry, iteration=1):

    """
    :param inquiry:
        Этот параметр принимает в себя string SQL-запрос.
    :param iteration:
        Этот параметр отвечает за количество вызовов вывода результата метода
        на экран.
    :return:
        Ничего не возвращает.
    """

    try:
        with connection.cursor() as cursor:
            cursor.execute(inquiry)
            connection.commit()
            for i in range(iteration):
                print(cursor.fetchone())
    except Exception as e:
        print('ERROR[inquiry_to_db]: {}'.format(e))
