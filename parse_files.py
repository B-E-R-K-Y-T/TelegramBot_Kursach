# This file is my file(BERKYT)

# ----------------------------------------------------------------------------------------------------------------------

# API для работы с файлами

# ----------------------------------------------------------------------------------------------------------------------

import os
import postgresql
import codecs


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

    with codecs.open(path, 'r', 'utf_8') as f:
        return sum(1 for _ in f)


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
        with codecs.open(path_from + str(names[i]), 'r', 'utf_8') as f:
            print(f.read(), file=codecs.open(path_to_save + '/all_files_result.txt', 'a', 'utf_8'), end='')


def replace_file(path, replace_from, replace_to, bool_list=False):

    """
    Тот же replace только в масштабе файла.

    :param bool_list:
        Проверка, является ли replace_from списком строк или строкой
    :param path:
        Путь до файла.
    :param replace_from:
        Строка, которую нужно удалить в файле.
    :param replace_to:
        Строка, на которую нужно заменить.
    :return:
        Ничего не возвращает.
    """

    with codecs.open(path, 'r', 'utf_8_sig') as f:
        if bool_list:
            str_file = f.read()
            for i in range(len(replace_from)):
                str_file = str_file.replace(replace_from[i], replace_to)

            print(str_file, file=codecs.open(path + '_new.txt', 'w', 'utf_8'), end='')

        else:
            print(f.read().replace(replace_from, replace_to),
                  file=codecs.open(path + '_new.txt', 'w', 'utf_8'), end='')


def del_space(path):

    """
    Удаляет все пустые строки в файле.

    :param path:
        Путь до файла.
    :return:
        Ничего не возвращает.
    """

    with codecs.open(path, 'r', 'utf_8') as f:
        for i in range(count_lines_in_file(path)):
            line = str(f.readline())
            if line.isspace():
                continue
            else:
                print(line, file=codecs.open(path + 'del_space_RESULT.txt', 'a', 'utf_8'), end='')


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

    for i in range(count_lines_in_file(path)):
        postgresql.inquiry_to_db(inquiry)


def split_file(path):
    with codecs.open(path, 'r', 'utf_8') as f:
        for (offset, line) in enumerate(f):
            if offset % 2 == 0:
                print(line, file=codecs.open(path + '_question', 'a', 'utf_8'), end='')
            else:
                print(line, file=codecs.open(path + '_answer', 'a', 'utf_8'), end='')
