from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView


urlpatterns = patterns('',

    url(r'^$', 'consult.views.home_view', name="consult_home"),
    
)