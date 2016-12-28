from django.contrib import admin

from consult.models import CV, CVDetail, Project, Tracker

class CVAdmin(admin.ModelAdmin):
    list_display = ('title',  'date_display', 'date', 'active')
    search_fields = ['title','location', 'description']
    
class CVDetailAdmin(admin.ModelAdmin):
    list_display = ('cv', 'description', 'order_by')
 
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order_by')     
    
class TrackerAdmin(admin.ModelAdmin):
    list_display = ('tracker_date', 'ip', 'url', 'agent') 
    
admin.site.register(CV, CVAdmin)  
admin.site.register(CVDetail, CVDetailAdmin)  
admin.site.register(Project, ProjectAdmin) 
admin.site.register(Tracker, TrackerAdmin)  