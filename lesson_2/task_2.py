"""Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения."""


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = 'good'
        self.__price = 300


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(self.__name, self.__price)


item = ItemDiscountReport('good', 30)
item.get_parent_data()

item_2 = ItemDiscount('123', 40)
print(item_2.__name)  # не сработает
