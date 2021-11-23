from django.urls import path

from .views import GoodsListView, GoodCreateView

app_name = 'shop'

urlpatterns = [
    path('', GoodsListView.as_view(), name='index'),
    path('create/', GoodCreateView.as_view(), name='create_good'),
]
