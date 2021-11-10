from code.API import parse_files
import codecs
# Список строк, кторые надо заменить
from code.API import postgresql

list_str_to_replace = ['Самсор Разми [hell_oworld]', 'Аполлинария Хорош [casper_ff]', 'Александр Хаметзянов [realcai_i_ia]','Алексей Зинкин [everkest]', 'Баба Огонь [id554048594]', 'Berkyt Berk [b_e_r_k_y_t]']

for i in range(parse_files.count_file_in_folder('D:/Users/Molodoy/Documents/GitHub/TelegramBot_Kursach/'
                                                'data/dialogs_vk/', 'text')+1):
    if i==0:
        continue
    parse_files.replace_file('D:/Users/Molodoy/Documents/GitHub/TelegramBot_Kursach/data/dialogs_vk/text{}.txt'
                             .format(i), list_str_to_replace, '', True)
    parse_files.del_space('D:/Users/Molodoy/Documents/GitHub/TelegramBot_Kursach/data/dialogs_vk/text{}.txt_new.txt'
                          .format(i))
    parse_files.split_file('D:/Users/Molodoy/Documents/GitHub/TelegramBot_Kursach/'
                           'data/dialogs_vk/text{}.txt_new.txtdel_space_RESULT.txt'.format(i))




# with codecs.open('data/dialogs_vk/dialog1.txt_new.txtdel_space_RESULT.txt_question', 'r', 'utf_8') as f:
#      for (offset, line) in enumerate(f):
#             postgresql.inquiry_to_db("INSERT INTO public.question (question)"
#                                          " values ('{1}')".format(offset, line))


