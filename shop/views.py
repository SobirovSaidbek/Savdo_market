from django.shortcuts import render
from django.views.generic import TemplateView


class ShopView(TemplateView):
    template_name = 'shops/shop-list-right-sidebar.html'