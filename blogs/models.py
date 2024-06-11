from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('name'))
    image = models.ImageField(upload_to='blogs-author')
    about = models.TextField(verbose_name=_('about'), blank=True)
    position = models.CharField(max_length=128, verbose_name=_('position'))
    profession = models.CharField(max_length=128, verbose_name=_('profession'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class BlogCategoryModel(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('category name'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class BlogTagModel(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('blog tag'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class BlogModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title blog'), db_index=True)
    image = models.ImageField(upload_to='blog-images')
    short_info = models.TextField(null=True, verbose_name=_('short_info'))
    content = models.TextField(verbose_name=_('content'))
    categories = models.ManyToManyField(BlogCategoryModel, related_name='blogs')
    tags = models.ManyToManyField(BlogTagModel, related_name='tags')
    authors = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, related_name='blogs')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')

