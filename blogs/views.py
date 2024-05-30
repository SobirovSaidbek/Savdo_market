from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


class BlogListView(ListView):
    template_name = 'blogs/blog-list.html'
    context_object_name = 'blogs'
    model = BlogModel

    def get_context_data(self, *, object_list=None,  **kwargs):
        context = {
            "blogs": BlogModel.objects.all().order_by('-created_at'),
            "categories": BlogCategoryModel.objects.all(),
            "tags": BlogTagModel.objects.all(),
            "famous_blogs": BlogModel.objects.all().order_by('-created_at')[::-2]
        }
        return context
