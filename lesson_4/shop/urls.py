from django.urls import path

from .views import GoodCreateView, index

app_name = 'shop'

urlpatterns = [
    # path('', GoodsListView.as_view(), name='index'),
    path('create/', GoodCreateView.as_view(), name='create_good'),
    path('<int:pk>/', index, name='index'),
]
