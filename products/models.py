from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
