from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager
from lesson_4.settings.site_1 import SITE_ID


class CustomQuerySet(models.QuerySet):
    def site_filter(self):
        return self.filter(site=SITE_ID)


class CustomManager(models.Manager):
    def get_queryset(self):
        return CustomQuerySet(self.model, using=self._db)

    def site_filter(self):
        return self.get_queryset().site_filter()


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название')
    shot_desc = models.CharField(max_length=256, blank=True, verbose_name='Короткое описание')
    site = models.ForeignKey(Site, on_delete=models.CASCADE, null=True)
    objects = CustomManager()

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
    site = models.ManyToManyField(Site, null=True, related_name='site')
    objects = CustomManager()
    # objects = models.Manager()
    # objects = CurrentSiteManager('site')

    class Meta:
        ordering = ('-arrive_date',)
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.name

