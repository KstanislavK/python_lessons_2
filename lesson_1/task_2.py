"""Дополнить следующую функцию недостающим кодом:
def print_directory_contents(sPath):
Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""
import os


def open_directory(path):
    print('#' * 15)
    print(f"Каталог: {path}\nВсе папки и файлы:")
    os.chdir(path)
    for item in os.listdir():
        path = os.path.join(path, item)
        print(path)
        if os.path.isdir(path):
            open_directory(path)


def print_directory_contents(directory):
    print(f"Каталог: {directory}\nВсе папки и файлы:")
    for item in os.listdir():
        path = os.path.join(directory, item)
        print(path)
        if os.path.isdir(path):
            open_directory(path)


def main():
    print_directory_contents(os.getcwd())


if __name__ == '__main__':
    main()
