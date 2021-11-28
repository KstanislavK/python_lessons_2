"""
Создать два списка с различным количеством элементов.
В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
"""


def create_dict(keys, values):
    new_dict = {}
    value = iter(values)
    nullValue = False

    for key in keys:
        try:
            new_dict[key] = next(value) if not nullValue else None
        except StopIteration:
            nullValue = True
            new_dict[key] = None

    return new_dict


def main():
    list_1 = [1, 2, 3]
    list_1_1 = [1, 2, 3, 4, 5, 6, 7, 8]
    list_2 = ['a', 'b', 'c', 'd', 'e']
    print(create_dict(list_1_1, list_2))


if __name__ == '__main__':
    main()
