
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

        cvs_current = CV.objects.filter(active=True, current=True)
        data['experience_current'] = cvs_current.filter(type='experience')
        data['publications_current'] = cvs_current.filter(type='publication')
        data['education_current'] = cvs_current.filter(type='education')
        data['courses_current'] = cvs_current.filter(type='course')

        cvs_older = CV.objects.filter(active=True, current=False)
        data['experience_older'] = cvs_older.filter(type='experience')
        data['publications_older'] = cvs_older.filter(type='publication')
        data['education_older'] = cvs_older.filter(type='education')
        data['courses_older'] = cvs_older.filter(type='course')

        data['page'] = get_page('cv')
        return data


class ContactView(TemplateView):

    template_name = 'consult/contact.html'


