#django own imports
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

#orders own imports
from orders.forms import OrderForm
from orders.models import OrderModel, OrderItems
from products.models import ProductModel

#users own imports
from users.models import AccountModel


class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'products/checkout.html'


@login_required
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = OrderModel.objects.create(user=request.user, status=False)
            cart = request.session.get('cart', None)
            if cart is None:
                return redirect(reverse_lazy('products:checkout'))
            product = ProductModel.objects.filter(pk__in=cart)
            for product in product:
                OrderItems.objects.create(product=product, product_name=product.name,
                                          quantity=1, price=product.real_price,
                                          size='nimadur', order=new_order,
                                          image1=product.image1, image2=product.image2
                                          )
            request.session['cart'] = []
            return redirect('orders:order_list')
        else:
            return render(request, 'products/checkout.html')


@login_required
def order_history(request):
    if request.method == 'GET':
        orders = OrderModel.objects.filter(user=request.user)
        context = {'orders': orders}
        return render(request, 'users/orders-history.html', context)