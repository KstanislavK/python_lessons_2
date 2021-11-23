from django.db import models


class Goods(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    arrive_date = models.DateField(verbose_name='Дата постуления')
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    unit = models.CharField(max_length=64, verbose_name='Единица измерения')
    vendor = models.CharField(max_length=128, blank=True, verbose_name='Поставщик')

    class Meta:
        ordering = ('-arrive_date',)
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.name
