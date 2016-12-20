
from django.shortcuts import render,render_to_response
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext

from consult.models import *


def home_view(request):
    return render_to_response('consult/home.html',
                          {'home_active': True}, 
                          context_instance=RequestContext(request))
    
def cv_view(request):
    
    experience = CV.objects.filter(active=True, type='experience').order_by('-date')
    
    
    return render_to_response('consult/cv.html',
                          {'cv_active': True,
                           'experience': experience, }, 
                          context_instance=RequestContext(request))
    
def contact_view(request):
    return render_to_response('consult/contact.html',
                          {'contact_active': True},  
                          context_instance=RequestContext(request))