from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',  'slug', 'active')
    search_fields = ['title',  'body', 'slug']
    
admin.site.register(Blog, BlogAdmin) 