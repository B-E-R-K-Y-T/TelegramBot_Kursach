import parse_files
import codecs
# Список строк, кторые надо заменить
import postgresql

list_str_to_replace = ['Самсор Разми [hell_oworld]', 'Аполлинария Хорош [casper_ff]']

# Заменяет строки
# parse_files.replace_file('data/dialogs_vk/dialog1.txt', list_str_to_replace, '', True)
# Удаляет пробелы
# parse_files.del_space('data/dialogs_vk/dialog1.txt_new.txt')
# Разделяет файлы на ответы и вопросы
# parse_files.split_file('data/dialogs_vk/dialog1.txt_new.txtdel_space_RESULT.txt')
with codecs.open('all_files_result.txt', 'r', 'utf_8') as f:
    for (offset, line) in enumerate(f):
        if offset>20:
            postgresql.inquiry_to_db( "INSERT INTO public.suka (id, answer)"
                                                 " values (0{0}, '{1}')".format(offset, line))
        else:
            postgresql.inquiry_to_db("INSERT INTO public.suka (id, question)"
                                     " values (0{0}, '{1}')".format(offset, line))

# with codecs.open('data/dialogs_vk/dialog1.txt_new.txtdel_space_RESULT.txt_question', 'r', 'utf_8') as f:
#      for (offset, line) in enumerate(f):
#             postgresql.inquiry_to_db("INSERT INTO public.suka (question)"
#                                          " values ('{1}')".format(offset, line))


# parse_files.attach_file_to_file('data/dialogs_vk/', ['dialog1.txt_new.txtdel_space_RESULT.txt_question',
#                                                     'dialog1.txt_new.txtdel_space_RESULT.txt_answer'])


        # parse_files.generation_sql_inquiry_to_db('data/dialogs_vk/dialog1.txt_new.txtdel_space_RESULT.txt_answer',
        #                                          "INSERT INTO public.dialogs (answers_)"
        #                                          " values ('{1}')".format(offset, line))

# with codecs.open('data/dialogs_vk/dialog1.txt_new.txtdel_space_RESULT.txt_question', 'r', 'utf_8') as f:
#     for (offset, line) in enumerate(f):
#         parse_files.generation_sql_inquiry_to_db('data/dialogs_vk/dialog1.txt_new.txtdel_space_RESULT.txt_question',
#                                                  "INSERT INTO public.dialogs (question)"
#                                                  " values ('{}')".format(line))