from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from products.models import ProductModel


class ProductsListView(TemplateView):
    template_name = 'products/checkout.html'

    def get_context_data(self, **kwargs):
        product = ProductModel.objects.all()
        context = {
            'products': product
        }
        return context
