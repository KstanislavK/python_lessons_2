"""
Реализовать расчет цены товара со скидкой.
Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка),
и перегрузку метода str дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат —
цена товара со скидкой. Чтобы все работало корректно,
не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
"""


class ItemDiscount:

    def __init__(self):
        self.__name = 'good'
        self.__price = 300

    def set_price(self, price):
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def __init__(self, discount):
        super().__init__()
        self.discount = discount

    def get_parent_data(self):
        disc_price = self.get_price() - self.get_price() * self.discount
        print(f'{self.get_name()} = {disc_price}')


disc = 0.05
item = ItemDiscountReport(disc)
item.get_parent_data()


