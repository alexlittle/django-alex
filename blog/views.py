from blog.models import  Blog
from consult.signals import site_tracker
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def home_view(request):
    site_tracker.send(sender=None, request=request)
    news = Blog.objects.filter(active=True).order_by('-display_date')
    paginator = Paginator(news, 5)
    
    try:
        page = int(request.GET. get('page', '1'))
    except ValueError:
        page = 1
        
    try:
        news = paginator.page(page)
    except (EmptyPage, InvalidPage):
        news = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/home.html',
                          {'page': news})
    
def blog_view(request, blog_slug):
    blog = Blog.objects.get(slug=blog_slug)
    return render(request, 'blog/blog-full-post.html',
                          {'blog': blog})
    