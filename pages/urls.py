from django.urls import path
from django.conf.urls.i18n import i18n_patterns

from pages.views import HomePageView, ContactTemplateView

app_name = 'pages'

urlpatterns = i18n_patterns(
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
)