from django.conf import settings
from django.conf.urls import include, url
from django.views.generic import TemplateView

from consult import views as consult_views

urlpatterns = [
    url(r'^$', consult_views.home_view, name="consult_home"),
    url(r'^cv/$', consult_views.cv_view, name="consult_cv"),
    url(r'^contact/$', consult_views.contact_view, name="consult_contact"),
]