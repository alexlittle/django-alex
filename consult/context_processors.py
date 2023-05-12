from django.conf import settings


def get_settings(request):
    return {'BLOG_ENABLED': settings.BLOG_ENABLED}
