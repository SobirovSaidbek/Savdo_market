# django own imports
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

# products own imports
from products.models import ProductModel

UserModels = get_user_model()


class OrderModel(models.Model):
    user = models.OneToOneField(UserModels, on_delete=models.CASCADE, primary_key=True, related_name='orders')
    status = models.CharField(default=False, verbose_name=_('status'))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated at'))

    def __str__(self):
        return self.user.name

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')


class OrderItems(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.SET_NULL, null=True, related_name='items')
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True, related_name='items')
    size = models.CharField(max_length=128, verbose_name=_('size'))
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'))
    image1 = models.ImageField(upload_to='media/rasmlar')
    image2 = models.ImageField(upload_to='media/rasmlar')

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')