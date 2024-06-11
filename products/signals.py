# django own imports signals
from django.db.models.signals import pre_save
from django.dispatch import receiver

# products own imports
from products.models import ProductModel


@receiver(pre_save, sender=ProductModel)
def calculate_total(sender, instance, **kwargs):
    if instance.discount():
        instance.real_price = instance.product.price - (instance.discount * instance.product.price / 100)
    else:
        instance.real_price = instance.price
