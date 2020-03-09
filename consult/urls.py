from django.urls import path
from consult import views as consult_views

app_name = 'consult'
urlpatterns = [
    path('', consult_views.HomeView.as_view(), name="home"),
    path('cv/', consult_views.CVView.as_view(), name="cv"),
    path('contact/', consult_views.ContactView.as_view(), name="contact"),
]
