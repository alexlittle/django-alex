# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False,
                                        auto_created=True,
                                        primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=300)),
                ('title_url', models.CharField(max_length=300,
                                               null=True,
                                               blank=True)),
                ('type', models.CharField(
                    max_length=100,
                    choices=[(b'Experience', b'Experience'),
                             (b'Presentation', b'Presentation'),
                             (b'Workshop', b'Workshop'),
                             (b'Publication', b'Publication')])),
                ('location', models.CharField(max_length=300,
                                              null=True,
                                              blank=True)),
                ('location_url', models.CharField(max_length=300,
                                                  null=True,
                                                  blank=True)),
                ('date', models.DateTimeField(
                    default=django.utils.timezone.now,
                    verbose_name=b'date')),
                ('date_display', models.CharField(max_length=300,
                                                  null=True,
                                                  blank=True)),
                ('description', models.TextField(default=None,
                                                 null=True,
                                                 blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CVDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID',
                                        serialize=False,
                                        auto_created=True,
                                        primary_key=True)),
                ('description', models.TextField(default=None,
                                                 null=True,
                                                 blank=True)),
                ('order_by', models.IntegerField(default=0)),
                ('cv', models.ForeignKey(to='consult.CV',
                                         on_delete=models.CASCADE)),
            ],
        ),
    ]
