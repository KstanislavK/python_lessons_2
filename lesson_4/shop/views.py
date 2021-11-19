from django.shortcuts import render
from django.views.generic import ListView

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


# def index(request):
#     title = 'Все товары'
#     goods = Goods.objects.all()
#
#     context = {
#         'title': title,
#         'objects': goods
#     }
#
#     return render(request, 'shop/goods_list.html', context)
