from django.db import models
from django.utils import timezone

# Create your models here.
CV_TYPE = (
        ('Experience', 'Experience'),
        ('Presentation', 'Presentation'),
        ('Workshop', 'Workshop'),
        ('Publication', 'Publication'),
        ('Education', 'Education'),
        ('Award', 'Award'),
        ('Course', 'Course'),
        ('Conference', 'Conference'),
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
    
    
class Project (models.Model):
    active = models.BooleanField(default=False)
    title = models.CharField(max_length=300, blank=False, null=False)
    title_url = models.CharField(max_length=300, blank=True, null=True)
    location = models.CharField(max_length=300, blank=True, null=True)
    location_url = models.CharField(max_length=300, blank=True, null=True)
    date = models.DateTimeField('date', default=timezone.now)
    date_display = models.CharField(max_length=300, blank=True, null=True)  
    description = models.TextField(blank=True, null=True, default=None)
    order_by = models.IntegerField(default=0)
    image = models.FileField(upload_to="projects",blank=True, default=None)
    
    def __unicode__(self):
        return self.title
    
class Tracker (models.Model):
    tracker_date = models.DateTimeField('date tracked',default=timezone.now)
    ip = models.GenericIPAddressField()
    agent = models.TextField(blank=True)
    url = models.TextField(blank=True, null=True, default=None)
    
    def __unicode__(self):
        return self.ip