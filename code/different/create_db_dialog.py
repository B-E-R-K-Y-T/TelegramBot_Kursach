# ======================================================================================================================

# Author: BERKYT

# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------

# Не смотрите на этот код. Мне просто было лень и я решил сварить макарончиков вместо кода.

# ----------------------------------------------------------------------------------------------------------------------


from code.API import postgresql as ps

# Привет
list_r = ['Привет!', 'Салам!', 'Хэлло', 'Прив', 'Hi', 'Hello', '😂', '👋', '🤓', '😎', '😀', '😁']
list_q = ['Привет', 'Салам', 'Прив', 'Hi', 'Hello', 'Здравствуйте', '😂', '👋', '🤓', '😎', '😀', '😁']
ps.inquiry_to_db("""DELETE FROM hello;""")

ps.inquiry_to_db("""ALTER TABLE hello DROP COLUMN id_;;""")

ps.inquiry_to_db("""ALTER TABLE public.hello ADD COLUMN id_ integer
NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 );""")

for i in zip(list_q, list_r):
    print(i[0], i[1])
    ps.inquiry_to_db("""INSERT INTO public.hello (examples, responses) values ('{}', '{}')""".format(i[0], i[1]))

# Как дела?

list_r = ['Отлично!', 'Круто!', 'Хорошо)', 'Не оч', 'МЕГА КРУТО', 'СУПЕР ТОП Я', 'сойдет',
          'Бывало и лучше', 'Бомба', 'Норм)']
list_q = ['как оно', 'как сам', 'как жизнь', 'как настроение', 'как поживаешь',
          'как делишки', 'как дела', 'все ли хорошо', 'как там ваше ничего', 'How you?']
ps.inquiry_to_db("""DELETE FROM how_do_you_do;""")

ps.inquiry_to_db("""ALTER TABLE how_do_you_do DROP COLUMN id_;;""")

ps.inquiry_to_db("""ALTER TABLE public.how_do_you_do ADD COLUMN id_ integer
NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 );""")

for i in zip(list_q, list_r):
    print(i[0], i[1])
    ps.inquiry_to_db("""INSERT INTO public.how_do_you_do (examples, responses) values ('{}', '{}')""".format(i[0], i[1]))

# Пока

list_r = ['До встречи!', 'Пока!', 'Бывай)', 'Будь здоров', ' Будьте здоровы!', 'До вечера', 'Всех благ',
          'Успехов', 'До новых встреч', 'Удачи']
list_q = ['до встречи', 'пока', 'бывай', 'будь здоров', ' будьте здоровы', 'до вечера', 'всех благ',
          'успехов', 'до новых встреч', 'удачи']
ps.inquiry_to_db("""DELETE FROM bye;""")

ps.inquiry_to_db("""ALTER TABLE bye DROP COLUMN id_;;""")

ps.inquiry_to_db("""ALTER TABLE public.bye ADD COLUMN id_ integer
NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 );""")

for i in zip(list_q, list_r):
    print(i[0], i[1])
    ps.inquiry_to_db("""INSERT INTO public.bye (examples, responses) values ('{}', '{}')""".format(i[0], i[1]))

# Если ничего не подошло

list_r = ['Я на такое не могу ответить...', 'Ха - ха. Очень смешно...', 'Не понял, повтори!',
          'Что? Да повезло им просто', 'Ага, спс', 'Всем похуй', 'И что? Я тут причем', 'Отвали', 'Нахуй пошел!',
          'Да - да, очень интересно, а теперь соси.']
list_q = ['до встречи', 'пока', 'бывай', 'будь здоров', ' будьте здоровы', 'до вечера', 'всех благ',
          'успехов', 'до новых встреч', 'удачи']
ps.inquiry_to_db("""DELETE FROM default_;""")

ps.inquiry_to_db("""ALTER TABLE default_ DROP COLUMN id_;;""")

ps.inquiry_to_db("""ALTER TABLE public.default_ ADD COLUMN id_ integer
NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 );""")

for i in zip(list_q, list_r):
    print(i[0], i[1])
    ps.inquiry_to_db("""INSERT INTO public.default_ (examples, responses) values ('{}', '{}')""".format(i[0], i[1]))