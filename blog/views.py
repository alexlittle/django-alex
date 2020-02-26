from blog.models import  Blog
from consult.signals import site_tracker
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _


def home_view(request):
    site_tracker.send(sender=None, request=request)

    
    return render(request, 'blog/home.html',
                          {})