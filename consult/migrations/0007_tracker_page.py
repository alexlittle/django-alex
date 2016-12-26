# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0006_tracker'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='page',
            field=models.TextField(default=None, null=True, blank=True),
        ),
    ]
