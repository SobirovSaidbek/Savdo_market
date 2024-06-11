# django own imports
from django.urls import path
from django.conf.urls.i18n import i18n_patterns

# orders own imports
from orders.views import CheckoutView, order_create, order_history

app_name = 'orders'

urlpatterns = i18n_patterns(
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('orders/', order_create, name='order'),
    path('history/', order_history, name='history')
)