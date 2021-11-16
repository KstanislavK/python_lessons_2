from time import time

"""Разработать генератор случайных чисел. 
В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
 Заполнить этими данными список и словарь. 
 Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”. 
 Вывести содержимое созданных списка и словаря."""


def time_random():
    return time() - float(str(time()).split('.')[0])


def gen_random_range(numbers):
    return int(time_random() * (numbers[1] - numbers[0]) + numbers[0])


def get_numbers():
    min_num = int(input('Введите минимум: '))
    max_num = int(input('Введите макисмум: '))

    return [min_num, max_num]


def create_dict(new_list):
    dict_num = {}
    count = 1
    for item in new_list:
        dict_num[f'elem_{count}'] = item
        count += 1

    return dict_num


def create_list(numbers, rand_number):
    numbers.append(rand_number)
    return numbers


if __name__ == '__main__':
    numbers = get_numbers()
    rand_number = gen_random_range(numbers)
    new_list = create_list(numbers, rand_number)
    new_dict = create_dict(new_list)
    print(new_list)
    print(new_dict)
