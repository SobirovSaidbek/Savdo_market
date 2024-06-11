from django import forms

from products.models import *


class ProductCommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['message']