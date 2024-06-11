# django own imports
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryModel(models.Model):
    name = models.CharField(max_length=128, db_index=True, verbose_name=_('name'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class TagModel(models.Model):
    name = models.CharField(max_length=128, db_index=True, verbose_name=_('name'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class ColorModel(models.Model):
    name = models.CharField(max_length=128, db_index=True, verbose_name=_('name'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')


class SizeModel(models.Model):
    name = models.CharField(max_length=128, db_index=True, verbose_name=_('name'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Size')
        verbose_name_plural = _('Sizes')


class ManufactureModel(models.Model):
    name = models.CharField(max_length=128, db_index=True, verbose_name=_('name'))
    logo = models.ImageField(null=True, blank=True, upload_to='media/manufacture')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Manufacture')
        verbose_name_plural = _('Manufactures')


class ProductModel(models.Model):
    image1 = models.ImageField(null=True, blank=True, upload_to='media/products')
    image2 = models.ImageField(null=True, blank=True, upload_to='media/products')

    name = models.CharField(max_length=128, db_index=True, verbose_name=_('name'))
    long_description = models.TextField(verbose_name=_('long_description'))
    short_description = models.CharField(max_length=255, verbose_name=_('short_description'))
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.PositiveSmallIntegerField(default=0,
                                                validators=
                                                [MaxValueValidator(100), MinValueValidator(0)]
                                                )
    sku = models.CharField(max_length=10, unique=True)
    count = models.PositiveIntegerField()
    real_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    manufacture = models.ForeignKey(ManufactureModel, on_delete=models.CASCADE, related_name='products')
    colors = models.ManyToManyField(ColorModel, related_name='products_colors')
    tags = models.ManyToManyField(TagModel, related_name='products_tags')
    categories = models.ManyToManyField(CategoryModel, related_name='products_categories')
    sizes = models.ManyToManyField(SizeModel, related_name='products_size')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def is_discount(self):
        return self.discount != 0

    def is_available(self):
        return self.count != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.discount * self.price / 100

    def get_related_products(self):
        return ProductModel.objects.filter(categories=1).exclude(pk=self.pk)[:3]

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class ProductImageModel(models.Model):
    image = models.ImageField(upload_to='media/products')
    product = models.ForeignKey(ProductModel(), on_delete=models.CASCADE, related_name='images')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')


UserModel = get_user_model()


class CommentModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='comments')
    message = models.TextField(verbose_name=_('message'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
