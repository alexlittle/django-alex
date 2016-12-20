# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='type',
            field=models.CharField(max_length=100, choices=[(b'Experience', b'Experience'), (b'Presentation', b'Presentation'), (b'Workshop', b'Workshop'), (b'Publication', b'Publication'), (b'Education', b'Education'), (b'Awards', b'Awards'), (b'Courses', b'Courses')]),
        ),
    ]
