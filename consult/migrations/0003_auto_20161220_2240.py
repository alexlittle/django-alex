# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult', '0002_auto_20161220_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvdetail',
            name='cv',
            field=models.ForeignKey(related_name='details', to='consult.CV'),
        ),
    ]
