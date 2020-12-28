
from django.db.models import Q
from django.shortcuts import render

from consult.models import CV, Project, Page
from blog.models import Blog
from consult.signals import site_tracker
from django.views.generic import TemplateView


def get_page(slug):
    try:
        page = Page.objects.get(slug=slug, active=True)
    except Page.DoesNotExist:
        return None
    return page


class HomeView(TemplateView):
    def get(self, request):
        site_tracker.send(sender=None, request=request)
        projects = Project.objects.filter(active=True).order_by('order_by')
        news = Blog.objects.filter(active=True).order_by('-display_date')[:3]
        return render(request,
                      'consult/home.html',
                      {'home_active': True,
                       'projects': projects,
                       'page': get_page('home'),
                       'news': news})


class CVView(TemplateView):
    def get(self, request):
        site_tracker.send(sender=None, request=request)
        experience = CV.objects.filter(active=True,
                                       type='experience').order_by('-date')
        publications = CV.objects.filter(active=True,
                                         type='publication').order_by('-date')
        conferences = CV.objects.filter(active=True) \
            .filter(Q(type='workshop')
                    | Q(type='presentation')
                    | Q(type='conference')).order_by('-date')
        return render(request,
                      'consult/cv.html',
                      {'cv_active': True,
                       'page': get_page('cv'),
                       'experience': experience,
                       'publications': publications,
                       'conferences': conferences})


class ContactView(TemplateView):
    def get(self, request):
        site_tracker.send(sender=None, request=request)
        return render(request,
                      'consult/contact.html',
                      {'contact_active': True})
