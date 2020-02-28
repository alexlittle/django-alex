from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView

from blog import views as blog_views
from blog.feeds import LatestNews

urlpatterns = [
    url(r'^$', blog_views.home_view, name="blog_home"),
    url(r'^feed/$', LatestNews(), name="blog_feed"),
    url(r'^(?P<blog_slug>\w[\w/-]*)$', blog_views.blog_view, name="blog_article"),
    
]