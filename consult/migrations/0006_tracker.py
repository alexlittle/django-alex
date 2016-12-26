# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0005_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tracker_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date tracked')),
                ('ip', models.GenericIPAddressField()),
                ('agent', models.TextField(blank=True)),
            ],
        ),
    ]
