"""
Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    def __init__(self):
        self.__name = 'good'
        self.__price = 300

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):

    def get_parent_data(self):
        print(self.get_name(), self.get_price())


item = ItemDiscountReport()
item.get_parent_data()
