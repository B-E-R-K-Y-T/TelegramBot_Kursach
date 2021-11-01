# This file is my file(BERKYT)


import psycopg2
from config import host, user, password, database


def open_db():
    connection = None
    try:
        assert isinstance(database, object)
        connection = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host
        )

        # cursor = connection.cursor()
        with connection.cursor() as cursor:
            # cursor.execute(
            #     'SELECT version();'
            # )
            cursor.execute(
                "INSERT INTO public.ai (id, id_message, dialogs) values ({}, {}, '{}');"
                    .format('0005', '05', 'ps   efef    d;ofij')
            )
            connection.commit()
            print('Server version: {}'.format(cursor.fetchone()))
    except Exception as e:
        print('ERROR: {}'.format(e))
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("DB is closed")


open_db()
