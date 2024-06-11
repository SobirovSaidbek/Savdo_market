from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactModel(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    email = models.EmailField(verbose_name=_('Email'))
    subject = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Subject'))
    message = models.TextField(verbose_name=_('messages'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')


class CommentModel(models.Model):
    name = models.CharField(max_length=128, verbose_name=_('Name'))
    comment = models.TextField(verbose_name=_('Comment'))
    profession = models.CharField(max_length=128, verbose_name=_('Profession'))
    image = models.ImageField(upload_to='media/', verbose_name=_('image'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')