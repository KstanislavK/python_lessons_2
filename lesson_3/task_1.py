"""
Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла,
а затем «выделение» из этого пути имени файла (без расширения).
"""
import os


def get_file_path(name):
    path = os.path.abspath(name)
    return path


def get_file_name(path):
    full_name = os.path.basename(path)
    name = os.path.splitext(full_name)[0]
    return name


def main():
    full_name = input('Insert file name: ')
    file_path = get_file_path(full_name)
    name = get_file_name(file_path)
    print(name)


if __name__ == '__main__':
    main()

