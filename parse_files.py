# This file is my file(BERKYT)

# ----------------------------------------------------------------------------------------------------------------------

# API для добавления диалогов в PostgreSQL

# ----------------------------------------------------------------------------------------------------------------------

import os
import postgresql

# ----------------------------------------------------------------------------------------------------------------------


def count_file_in_folder(path, file_name):

    """
    Подсчитывает кол - во файлов в директории.

    :param path:
        Путь до директории, где мы проверяем кол - во файлов.
    :param file_name:
        Строка, которая должна содержаться в имени файла.
    :return:
        Возвращает кол - во таких файлов в директории.
    """

    try:
        list_files = os.listdir(path)
    except Exception as e:
        print('count_file_in_folder: {}'.format(e))
    else:
        list_out = []
        file_name = str(file_name)
        for i in range(len(list_files)):
            if file_name in str(list_files[i]):
                list_out.append(str(list_files[i]))

        return len(list_out)


def count_lines_in_file(path):

    """
    Считает кол-во строк в файле.

    :param path:
        Путь до файла.
    :return:
        Возвращает кол - во строк.
    """

    with open(path, 'r') as f:
        count = sum(1 for _ in f)
        return count


def attach_file_to_file(path_from, names=[], path_to_save=str(os.getcwd())):

    """
    Объединяет список файлов в один файл.

    :param path_from:
        Путь до файлов.
    :param names:
        Список названий этих файлов, включая их тип.
    :param path_to_save:
        Путь, куда надо сохранять результирующий файл.
    :return:
        Ничего не возвращает.
    """

    for i in range(len(names)):
        with open(path_from + str(names[i]), 'r') as f:
            print(f.read(), file=open(path_to_save + '/all_files_result.txt', 'a'), end='')


def del_str_in_file(path, replace_from, replace_to):

    """
    Тот же replace только в масштабе файла.

    :param path:
        Путь до файла.
    :param replace_from:
        Строка, которую нужно удалить в файле.
    :param replace_to:
        Строка, на которую нужно заменить.
    :return:
        Ничего не возвращает.
    """

    with open(path, 'r') as f:
        _str = f.read()
        _str = _str.replace(replace_from, replace_to)
        print(_str, file=open(path, 'w'), end='')


def del_space(path):

    """
    Удаляет все пустые строки в файле.

    :param path:
        Путь до файла.
    :return:
        Ничего не возвращает.
    """

    with open(path, 'r') as f:
        count_lines = count_lines_in_file(path)
        for i in range(count_lines):
            line = str(f.readline())
            if line.isspace():
                continue
            else:
                print(line, file=open(path + 'del_space_RESULT.txt', 'a'), end='')


def generation_sql_inquiry_to_db(path, inquiry):

    """
    :param path:
        Принимает путь до файла к которому применить запрос.
    :param inquiry:
        Принимает sql-запрос.
    :return:
    """

    count = count_lines_in_file(path)
    with open(path) as f:
        for i in range(count):
            postgresql.inquiry_to_db(inquiry)


# attach_file_to_file(count_file_in_folder('data/dialogs_vk/', 'dialog'), 'data/dialogs_vk/', 'dialog', '.txt', 'data')
attach_file_to_file('data/dialogs_vk/', ['dialog0.txt', 'dialog1.txt', 'dialog2.txt'], 'data/')
del_str_in_file('data/all_files_result.txt', 'Berkyt Berk [b_e_r_k_y_t]', '')
del_space('data/all_files_result.txt')




# del_attachments()
#
# del_nickname('Александр Хаметзянов', 'Самсор Разми', '[realcai_i_ia]')
# del_nickname('Самсор Разми', 'Александр Хаметзянов', '[hell_oworld]')
#
# del_nickname('Аполлинария Хорош', 'Самсор Разми', '[casper_ff]')
# del_nickname('Самсор Разми', 'Аполлинария Хорош', '[hell_oworld]')
#
# del_nickname('Berkyt Berk', 'Аполлинария Хорош', '[b_e_r_k_y_t]')
# del_nickname('Аполлинария Хорош', 'Berkyt Berk', '[casper_ff]')
#
# list_path = ['answers', 'question']
#
# dict_name = {'Александр Хаметзянов': True, 'Самсор Разми': False}
# convert_file_to_db(dict_name, list_path)
#
# dict_name = {'Аполлинария Хорош': True, 'Самсор Разми': False}
# convert_file_to_db(dict_name, list_path)
#
# dict_name = {'Аполлинария Хорош': True, 'Berkyt Berk': False}
# convert_file_to_db(dict_name, list_path)


def del_attachments(start='Attachments:[', end=']'):
    for i in range(3):
        with open(r'data/dialogs_vk/dialog{0}.txt'.format(i), 'r') as f:
            count = sum(1 for _ in f)
            print(count)
            f.close()
            f = open(r'data/dialogs_vk/dialog{0}.txt'.format(i), 'r')
            length = 0
            for j in range(count):
                line = f.readline()
                if start in line:
                    line = f.readline()
                    while length < count:
                        length += 1
                        if end in line:
                            f.readline()
                            line = f.readline()
                            break
                        line = f.readline()
                try:
                    print(line, file=open(r'data/file_without_attachments.txt', 'a'), end='')
                except Exception as e:
                    print(e)
            f.close()


def del_nickname(start='Berkyt Berk', end='Никита Беркут', id_vk='[b_e_r_k_y_t]'):
    with open(r'data/file_without_attachments.txt', 'r') as f:
        count = sum(1 for _ in f)
        print(count)
        f.close()
        f = open(r'data/file_without_attachments.txt', 'r')
        length = 0
        for j in range(count):
            line = f.readline()
            if start in line:
                while length < count:
                    length += 1
                    line = f.readline()
                    if line.isspace():
                        break
                    try:
                        print(line, file=open(r'data/file_{0}.txt'.format(start), 'a'), end='')
                    except Exception as e:
                        print(e)
        f.close()

        with open(r'data/file_{0}.txt'.format(start)) as f:
            text = f.read()
            text = text.replace('{0} {1}'.format(start, id_vk), '')
            try:
                print(text, file=open(r'data/file_{0}.txt'.format(start), 'w'), end='')
            except Exception as e:
                print(e)
            f.close()


def create_answer_question(path, flag):

    """
    :param path:
        Путь до файла который нужно разбить на ответы или вопросы.
    :param flag:
        Является ли файл ответами? Иначе вопросы.
    :return:
        Ничего не возвращает.
    """

    with open(path) as f:
        count = sum(1 for _ in f)
        print(count)
        f.close()
        with open(path) as f:
            for i in range(count):
                line = str(f.readline())
                if flag:
                    if not line.isspace():
                        print(line, file=open(r'data/answers.txt', 'a'), end='')
                    else:
                        continue
                else:
                    if not line.isspace():
                        print(line, file=open(r'data/question.txt', 'a'), end='')
                    else:
                        continue


def generation_db(path, inquiry):

    """
    :param path:
        Принимает путь до файла.
    :param inquiry:
        Принимает sql-запрос.
    :return:
    """

    with (open(path)) as f:
        count = sum(1 for _ in f)
        f.close()
        with open(path) as f:
            for i in range(count):
                postgresql.inquiry_to_db(inquiry)


def convert_file_to_db(dict_name, list_path):

    """
    :param dict_name:
        Принимает словарь флагов-переключателей истина - пользователь иначе - ИИ.
    :param list_path:
        Принимает список названий файлов, которые надо создать.
    :return:
    """

    for i in range(len(dict_name)):
        with (open(r'data/file_{0}.txt'.format(str(list(dict_name.keys())[i])))) as f:
            flag = dict_name[str(list(dict_name.keys())[i])]
            print(flag)
            str_dict = str(list(dict_name.keys())[i])
            path = list_path[i]
            try:
                if flag:
                    create_answer_question('data/file_{0}.txt'.format(str_dict),
                                           flag)
                    generation_db('data/{0}.txt'.format(path), 'SELECT * FROM ai;')
                else:
                    create_answer_question('data/file_{0}.txt'.format(str_dict),
                                           flag)
                    generation_db('data/{0}.txt'.format(path), 'SELECT * FROM ai;')
            except Exception as e:
                print(e)

