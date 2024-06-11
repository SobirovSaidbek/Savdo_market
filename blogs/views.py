# django own imports

from django.shortcuts import render
from django.views.generic import TemplateView, ListView


#blogs own imports
from blogs.models import BlogModel, BlogCategoryModel, BlogTagModel


class BlogListView(ListView):
    template_name = 'blogs/blog-list.html'
    context_object_name = 'blogs'
    model = BlogModel
    paginate_by = 2

    def get_queryset(self):
        queryset = BlogModel.objects.all().order_by('-pk')
        tags = self.request.GET.get('tags')
        categories = self.request.GET.get('categories')

        if tags:
            queryset = queryset.filter(tags=tags)
        if categories:
            queryset = queryset.filter(categories=categories)

        return queryset

    def get_context_data(self, *, object_list=None,  **kwargs):
        context = {
            "blogs": BlogModel.objects.all().order_by('-created_at'),
            "categories": BlogCategoryModel.objects.all(),
            "tags": BlogTagModel.objects.all(),
            "famous_blogs": BlogModel.objects.all().order_by('-created_at')[::-2]
        }
        return context


class BlogDetailView(TemplateView):
    template_name = 'blogs/blog-detail.html'
    context_object_name = 'blog'
    model = BlogModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {
            "categories": BlogCategoryModel.objects.all(),
            "blog": BlogModel.objects.get(pk=self.kwargs['pk']),
            "tags": BlogTagModel.objects.all(),
            "famous_blogs": BlogModel.objects.all().order_by('-created_at')[:2],
            "related_blogs": BlogModel.objects.filter(categories__in=self.object.categories.all()).order_by(
                '-created_at')[:3],
        }
        return context