from django.db import models
from django.utils import timezone

# Create your models here.
CV_TYPE = (
        ('Experience', 'Experience'),
        ('Presentation', 'Presentation'),
        ('Workshop', 'Workshop'),
        ('Publication', 'Publication'),
        ('Education', 'Education'),
        ('Awards', 'Awards'),
        ('Courses', 'Courses'),
    )


class CV (models.Model):
    active = models.BooleanField(default=False)
    title = models.CharField(max_length=300, blank=False, null=False)
    title_url = models.CharField(max_length=300, blank=True, null=True)
    type = models.CharField(max_length=100, choices=CV_TYPE,)
    location = models.CharField(max_length=300, blank=True, null=True)
    location_url = models.CharField(max_length=300, blank=True, null=True)
    date = models.DateTimeField('date', default=timezone.now)
    date_display = models.CharField(max_length=300, blank=True, null=True)  
    description = models.TextField(blank=True, null=True, default=None)
    
    def __unicode__(self):
        return self.title
    
    
class CVDetail (models.Model):
    cv = models.ForeignKey(CV, related_name='details')
    description = models.TextField(blank=True, null=True, default=None)
    order_by = models.IntegerField(default=0)
    
    def __unicode__(self):
        return self.description