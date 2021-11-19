from django.urls import path

from .views import GoodsListView

app_name = 'shop'

urlpatterns = [
    path('', GoodsListView.as_view(), name='index'),
]
