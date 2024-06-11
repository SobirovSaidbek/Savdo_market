# django own imports
from django import forms
from django.utils.translation import gettext_lazy as _


class OrderForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=128, verbose_name=_('Phone Number'))
    address = forms.CharField(max_length=200, verbose_name=_('Address'))