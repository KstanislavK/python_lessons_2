"""
Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""
import re


def compare_nums(number):
    nums_list = re.split("\.|,", number)
    if nums_list[0] == nums_list[1]:
        return True
    else:
        return False


def get_num_type(number):
    if '.' in number or ',' in number:
        return compare_nums(number)
    else:
        return 'Int num'


def main():
    number = input('Insert number: ')
    print(get_num_type(number))


if __name__ == '__main__':
    main()
