"""
Написать программу, в которой реализовать две функции.
В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции.
"""
import os
import random
import string


def create_word_list():
    words_list = []
    letters = string.ascii_lowercase
    for _ in range(10):
        rand_string = ''.join(random.choice(letters) for _ in range(random.randint(2, 8)))
        words_list.append(rand_string)
    return words_list


def create_file(file_name):
    num_list = [str(random.randint(1, 1000)) for _ in range(10)]
    words_list = create_word_list()
    common_list = zip(num_list, words_list)

    if os.path.isfile(file_name):
        print('Такой файл есть')
    else:
        with open(file_name, 'w', encoding='utf-8') as f:
            for item in common_list:
                st = ', '.join(item)
                f.write(st + '\n')
        read_file(file_name)


def read_file(file_path):
    with open(file_path, encoding='utf') as f:
        lines = f.readlines()
        for line in lines:
            print(line)


def main():
    file_name = f"{input('Insert file name: ')}.txt"
    create_file(file_name)


if __name__ == '__main__':
    main()
