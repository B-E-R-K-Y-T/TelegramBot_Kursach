import psycopg2
from config import host, user, password, db_name


def open_db():
    try:
        assert isinstance(db_name, object)
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            db_name=db_name
        )

        # cursor = connection.cursor()
        with connection.cursor() as cursor:
            cursor.execute(
                'SELECT version();'
            )
            print('Server version: {}'.format(cursor.fetchone()))
    except Exception as e:
        print(e)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("DB is closed")
