from django.contrib import admin

from consult.models import CV, CVDetail

# Register your models here.
class CVAdmin(admin.ModelAdmin):
    list_display = ('date', 'date_display','title', 'active')
    
  
class CVDetailAdmin(admin.ModelAdmin):
    list_display = ('cv', 'description')
      
    
admin.site.register(CV, CVAdmin)  
admin.site.register(CVDetail, CVDetailAdmin)  