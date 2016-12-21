from django.contrib import admin

from consult.models import CV, CVDetail, Project

# Register your models here.
class CVAdmin(admin.ModelAdmin):
    list_display = ('title',  'date_display', 'date', 'active')
    
  
class CVDetailAdmin(admin.ModelAdmin):
    list_display = ('cv', 'description', 'order_by')
 
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order_by')     
    
admin.site.register(CV, CVAdmin)  
admin.site.register(CVDetail, CVDetailAdmin)  
admin.site.register(Project, ProjectAdmin)  