# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0007_tracker_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracker',
            old_name='page',
            new_name='url',
        ),
    ]
