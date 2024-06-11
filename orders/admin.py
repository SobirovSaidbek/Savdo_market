# django own imports
from django.contrib import admin

# orders own imports
from orders.models import OrderModel, OrderItems


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'created_at', 'updated_at',)
    list_filter = ('created_at', 'status',)


@admin.register(OrderItems)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'quantity', 'price', 'size',)
    list_filter = ('product_name',)
