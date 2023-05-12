from django.conf import settings
from django.urls import include, path
from django.contrib import admin

if settings.BLOG_ENABLED:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('consult.urls')),
        path('news/', include('blog.urls'))
    ]
else:
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('consult.urls')),
    ]
