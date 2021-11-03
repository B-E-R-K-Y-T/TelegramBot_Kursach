# This file is my file(BERKYT)

# ----------------------------------------------------------------------------------------------------------------------

# API для добавления диалогов в PostgreSQL

# ----------------------------------------------------------------------------------------------------------------------

import os
import postgresql


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

    list_files = os.listdir(path)
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


def attach_file_to_file(path_from, names=None, path_to_save=str(os.getcwd())):

    """
    Объединяет список файлов в один файл.

    :param path_from:
        Путь до файлов.
    :param names:
        Список[] названий этих файлов, включая их тип.
    :param path_to_save:
        Путь, куда надо сохранять результирующий файл.
    :return:
        Ничего не возвращает.
    """

    for i in range(len(names)):
        with open(path_from + str(names[i]), 'r') as f:
            print(f.read(), file=open(path_to_save + '/all_files_result.txt', 'a'), end='')


def replace_file(path, replace_from, replace_to):

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
    Делает sql-запрос столько же раз, сколько строк в файле.

    :param path:
        Принимает путь до файла к которому применить запрос.
    :param inquiry:
        Принимает sql-запрос.
    :return:
        Ничего не возвращает.
    """

    count = count_lines_in_file(path)
    for i in range(count):
        postgresql.inquiry_to_db(inquiry)


attach_file_to_file('data/dialogs_vk/', ['dialog0.txt', 'dialog1.txt', 'dialog2.txt'], 'data/')
replace_file('data/all_files_result.txt', 'Berkyt Berk [b_e_r_k_y_t]', '')
del_space('data/all_files_result.txt')
