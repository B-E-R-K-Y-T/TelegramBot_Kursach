import parse_files


L = ['Berkyt Berk [b_e_r_k_y_t]', 'Аполлинария Хорош [casper_ff]']
# L1 = ['Проверка']
# s = 'Проверка, является ли replace_from списком строк или строкой'
# print(s.replace(L1[0], ''))
parse_files.replace_file('data/dialogs_vk/dialog2.txt', L, '', True)
# parse_files.replace_file('data/dialogs_vk/dialog2.txt', 'Berkyt Berk [b_e_r_k_y_t]', '')
# parse_files.del_space('data/dialogs_vk/dialog2.txt')
# parse_files.split_file('data/dialogs_vk/dialog2.txt')