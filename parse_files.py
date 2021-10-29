# This file is my file(BERKYT)


def del_attachments(start='Attachments:[', end=']'):
    for i in range(1, 58):
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


# with open(r'data/file_.txt', 'r') as f:
#     while True:
#         f.readline()
#     f.close()

del_attachments()
del_nickname()
del_nickname('Никита Беркут', 'Berkyt Berk', '[tbtbtbtbtbtbtbtbtbtbtbtbtbtbtbtb]')
