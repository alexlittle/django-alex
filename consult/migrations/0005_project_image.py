# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0004_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.FileField(default=None, upload_to=b'projects', blank=True),
        ),
    ]
