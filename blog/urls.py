from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView

from blog import views as blog_views

urlpatterns = [
    url(r'^$', blog_views.home_view, name="blog_home"),
]