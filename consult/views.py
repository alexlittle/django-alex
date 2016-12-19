
from django.shortcuts import render,render_to_response
from django.utils.translation import ugettext_lazy as _
from django.template import RequestContext

# Create your views here.
def home_view(request):
    return render_to_response('consult/home.html',
                          {}, 
                          context_instance=RequestContext(request))