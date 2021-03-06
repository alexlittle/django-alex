# Generated by Django 2.2.10 on 2020-02-26 10:05

import consult.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0011_auto_20190202_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('display_date', models.DateTimeField(
                    default=django.utils.timezone.now)),
                ('title', models.TextField()),
                ('slug', consult.fields.AutoSlugField(blank=True,
                                                      editable=False,
                                                      max_length=100,
                                                      null=True,
                                                      populate_from='title',
                                                      unique=True)),
                ('body', models.TextField()),
                ('image', models.FileField(blank=True,
                                           default=None,
                                           upload_to='images')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
