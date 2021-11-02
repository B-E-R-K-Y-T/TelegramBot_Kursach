# This file is my file(BERKYT)


import postgresql


def del_attachments(start='Attachments:[', end=']'):
    for i in range(1):
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
                    if end in line:
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
        Путь до файла который нужно разбить на ответы или вопросы
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


def generation_db(path):
    with (open(path)) as f:
        count = sum(1 for _ in f)
        print(count)
        f.close()
        with open(path) as f:
            for i in range(count):
                postgresql.inquiry_to_db("INSERT INTO public.ai (id, id_message, dialogs) "
                                         "values (000{}, 0{}, '{}');".format(str(i), str(i), f.readline()))


del_attachments()
del_nickname('Александр Хаметзянов', 'Аполлинария Хорош', '[realcai_i_ia]')
del_nickname('Аполлинария Хорош', 'Александр Хаметзянов', '[casper_ff]')

dict_name = {'Аполлинария Хорош': True, 'Александр Хаметзянов': False}

for i in range(len(dict_name)):
    flag = dict_name[str(list(dict_name.keys())[i])]
    str_dict = str(list(dict_name.keys())[i])
    try:
        if flag:
            create_answer_question('data/file_{0}.txt'.format(str_dict),
                                   flag)
            generation_db('data/file_{0}.txt'.format(str_dict))
        else:
            pass
            # create_answer_question('data/file_{0}.txt'.format(str_dict),
            #                        flag)
            # generation_db('data/file_{0}.txt'.format(str_dict))
    except Exception as e:
        print(e)
