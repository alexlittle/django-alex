# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0003_auto_20161220_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=300)),
                ('title_url', models.CharField(max_length=300, null=True, blank=True)),
                ('location', models.CharField(max_length=300, null=True, blank=True)),
                ('location_url', models.CharField(max_length=300, null=True, blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'date')),
                ('date_display', models.CharField(max_length=300, null=True, blank=True)),
                ('description', models.TextField(default=None, null=True, blank=True)),
                ('order_by', models.IntegerField(default=0)),
            ],
        ),
    ]
