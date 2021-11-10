import parse_files

# Список строк, кторые надо заменить
list_str_to_replace = ['Berkyt Berk [b_e_r_k_y_t]', 'Аполлинария Хорош [casper_ff]']

# Заменяет строки
parse_files.replace_file('data/dialogs_vk/dialog2.txt', list_str_to_replace, '', True)
# Удаляет пробелы
parse_files.del_space('data/dialogs_vk/dialog2.txt_new.txt')
# Разделяет файлы на ответы и вопросы
parse_files.split_file('data/dialogs_vk/dialog2.txt_new.txtdel_space_RESULT.txt')

