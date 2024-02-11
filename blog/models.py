from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from consult.fields import AutoSlugField

from consult.models import Tracker


class Blog(models.Model):
    display_date = models.DateTimeField(default=timezone.now)
    title = models.TextField(blank=False)
    slug = AutoSlugField(populate_from='title',
                         max_length=100,
                         blank=True,
                         null=True)
    body = HTMLField()
    image = models.FileField(upload_to="images", blank=True, default=None)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_hits(self):
        return Tracker.objects.filter(url__endswith=self.slug).count()
