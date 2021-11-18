"""
Проверить на практике возможности полиморфизма.
Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно. Внутри каждого поместить функцию get_info,
которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.
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


class ItemNameReport(ItemDiscount):

    def get_info(self):
        return self.get_name()

    def __str__(self):
        return self.get_name()


class ItemDiscountReport(ItemDiscount):

    def __init__(self, discount):
        super().__init__()
        self.discount = discount

    def get_info(self):
        return self.get_price() - self.get_price() * self.discount

    def __str__(self):
        return str(self.get_price() - self.get_price() * self.discount)


disc = 0.05
name = ItemNameReport()
price = ItemDiscountReport(disc)
print(f'{name.get_info()} = {price.get_info()}')
print(ItemNameReport(), ItemDiscountReport(disc))
