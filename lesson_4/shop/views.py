from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Goods, Category


# class GoodsListView(ListView):
#     model = Goods
#     template_name = 'shop/goods_list.html'
#     context_object_name = 'objects'
#
#     queryset = Goods.objects.prefetch_related('category').all()
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(GoodsListView, self).get_context_data(*args, **kwargs)
#         title = 'Все товары'
#         context.update({'title': title})
#         return context


class GoodCreateView(CreateView):
    model = Goods
    template_name = 'shop/good_create.html'
    success_url = reverse_lazy('shop:index', kwargs={'pk': 0})
    fields = '__all__'

    def get_context_data(self):
        context = super(GoodCreateView, self).get_context_data()
        title = 'Добавить товар'
        context.update({'title': title})
        return context


def index(request, pk=None):
    goods = Goods.objects.prefetch_related('category').all()
    links_menu = Category.objects.all()

    if pk is not None:
        if pk == 0:
            goods = Goods.objects.prefetch_related('category').all()
            category = {'name': 'Все', 'pk': 0}
            title = category['name']
        else:
            category = get_object_or_404(Category, pk=pk)
            goods = Goods.objects.filter(category__pk=pk)
            title = category.name

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'objects': goods,
        }
        return render(request, 'shop/goods_list.html', context)

    context = {
        'title': 'Все товары',
        'links_menu': links_menu,
        'objects': goods,
    }
    return render(request, 'shop/goods_list.html', context)
