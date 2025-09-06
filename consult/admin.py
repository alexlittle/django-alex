from django.contrib import admin

from consult.models import CV, CVDetail, Project, Tracker, Page, CVSkill


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title',  'menu_title', 'slug', 'active')
    search_fields = ['title',  'menu_title', 'slug', 'content']

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_display', 'type', 'date', 'active', 'current')
    search_fields = ['title', 'location', 'description']

@admin.register(CVDetail)
class CVDetailAdmin(admin.ModelAdmin):
    list_display = ('cv', 'description', 'order_by')

@admin.register(CVSkill)
class CVSkillAdmin(admin.ModelAdmin):
    list_display = ('description', 'order_by', 'active')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order_by')

@admin.register(Tracker)
class TrackerAdmin(admin.ModelAdmin):
    list_display = ('tracker_date', 'ip', 'url', 'agent')


