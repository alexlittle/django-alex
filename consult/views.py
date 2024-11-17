
from django.conf import settings
from django.db.models import Q
from django.shortcuts import render

from consult.models import CV, Project, Page, CVSkill
from blog.models import Blog
from django.views.generic import TemplateView


def get_page(slug):
    try:
        page = Page.objects.get(slug=slug, active=True)
    except Page.DoesNotExist:
        return None
    return page


class HomeView(TemplateView):

    template_name = 'consult/home.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if settings.PROJECTS_ENABLED:
            data['projects'] = Project.objects.filter(active=True).order_by('order_by')
        if settings.BLOG_ENABLED:
            data['news'] = Blog.objects.filter(active=True).order_by('-display_date')[:3]
        data['page'] = get_page('home')
        return data


class CVView(TemplateView):

    template_name = 'consult/cv.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['skills'] = CVSkill.objects.filter(active=True).order_by('order_by')
        data['experience'] = CV.objects.filter(active=True, type='experience').order_by('-date')
        data['publications'] = CV.objects.filter(active=True, type='publication').order_by('-date')
        '''
        data['conferences'] = CV.objects.filter(active=True) \
            .filter(Q(type='workshop')
                    | Q(type='presentation')
                    | Q(type='conference')).order_by('-date')
        '''
        data['education'] = CV.objects.filter(active=True, type='education').order_by('-date')
        data['courses'] = CV.objects.filter(active=True, type='course').order_by('-date')
        data['page'] = get_page('cv')
        return data


class ContactView(TemplateView):

    template_name = 'consult/contact.html'


