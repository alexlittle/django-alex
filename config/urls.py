from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static

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
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
