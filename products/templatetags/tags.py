# django own imports
from django import template
from django.db.models import Sum

# products own imports
from products.models import ProductModel

# Library imports
register = template.Library()


@register.filter
def in_cart(request, product):
    return product.pk in request.session.get('cart', [])


@register.filter
def get_total_cart(request):
    cart = request.session.get('cart', [])
    total_price = ProductModel.objects.filter(pk__in=cart).aggregate(Sum('real_pirce')).get('real_pirce__sum')
    if total_price:
        return total_price
    return 0


@register.filter
def get_likes(request):
    likes = request.session.get('likes', [])
    products = ProductModel.objects.filter(pk__in=likes)
    return products


@register.filter
def get_likes_in(product_like, request):
    return product_like.pk in request.session.get('likes', [])


@register.filter
def get_cart_user(request):
    cart = request.session.get('cart', [])
    products = ProductModel.objects.filter(pk__in=cart)
    return products