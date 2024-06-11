from django.urls import path
from django.conf.urls.i18n import i18n_patterns

from products.views import ProductsListView, Prodct

app_name = 'products'

urlpatterns = i18n_patterns(
    path('detail/<int:pk>', ProductsListView.as_view(), name='list')
)