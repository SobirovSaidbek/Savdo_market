from django.urls import path

from shop.views import ShopView

app_name = 'shops'

urlpatterns = [
    path('', ShopView.as_view(), name='shop')
]