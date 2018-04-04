# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allinone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothsphoto',
            name='year',
            field=models.DateTimeField(),
        ),
    ]
