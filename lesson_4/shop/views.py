from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Goods


class GoodsListView(ListView):
    model = Goods
    template_name = 'shop/goods_list.html'
    context_object_name = 'objects'

    def get_queryset(self):
        return Goods.objects.all()

    def get_context_data(self):
        context = super(GoodsListView, self). get_context_data()
        title = 'Все товары'
        context.update({'title': title})
        return context


class GoodCreateView(CreateView):
    model = Goods
    template_name = 'shop/good_create.html'
    success_url = reverse_lazy('shop:index')
    fields = '__all__'

    def get_context_data(self):
        context = super(GoodCreateView, self).get_context_data()
        title = 'Добавить товар'
        context.update({'title': title})
        return context
