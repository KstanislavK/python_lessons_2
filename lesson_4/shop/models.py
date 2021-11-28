from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    shot_desc = models.CharField(max_length=256, blank=True, verbose_name='Короткое описание')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Goods(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    category = models.ManyToManyField(Category, related_name='category')
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

